import os
import requests
from moviepy import AudioFileClip, AudioClip, concatenate_audioclips, VideoFileClip, ImageClip
from backend.agents.base_agent import Agent
import whisper
from backend.prompts import group_scene_prompt
class Editor(Agent):
    """
    Handles TTS generation, merging audio, and final output.
    """
    def __init__(self, voice_ids, model_id="eleven_v3"):
        super().__init__()
        self.voice_ids = voice_ids
        self.model_id = model_id
        self.name_to_voice = {}

    def generate_voice(self, text, speaker, output_path, tts):
        """
        Generate voice using TTS API.
        
        text: text to convert to speech
        speaker: speaker of the line (MAN1, MAN2, OR W1 OR W2)
        output_path: path to save the generated audio file
        returns: duration of the audio in seconds
        """
        output_path = os.path.join(os.getcwd(), output_path)

        if tts == "elevenlabs":
            from elevenlabs.client import ElevenLabs
            client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
            voice_id = self.voice_ids[speaker]
            
            audio_stream = client.text_to_speech.convert(
                voice_id=voice_id,
                model_id=self.model_id,
                text=text,
                output_format="mp3_44100_128",
                voice_settings={"stability": 0.5, "similarity_boost": 0.8},
            )

            with open(output_path, "wb") as f:
                for chunk in audio_stream:
                    f.write(chunk)

        elif tts == "xtts":
            url = "http://127.0.0.1:8000/generate-audio/"
            payload = {
                "text": text,
                "file_path": output_path,
                "voice": speaker
            }
            response = requests.post(url, json=payload)

        elif tts == "kokoro":
            output_path = output_path.replace(".mp3", ".wav")
            url = "http://127.0.0.1:8001/generate-audio/"
            payload = {
                "text": text,
                "file_path": output_path,
                "voice": speaker
            }
            response = requests.post(url, json=payload)

        # Get duration
        audio_clip = AudioFileClip(output_path)
        duration = audio_clip.duration
        audio_clip.close()

        print(f"✅ Audio saved to {output_path}, duration: {duration:.2f}s")
        return duration

    def analyze_script(self, script_text: dict, subtitle_output_path="subtitles.srt"):
        """
        Analyze the script and return structured data.
        script_text: dict with keys "Characters" and "story"
        returns: list of tuples (speaker, line)
        """
        speakers = script_text.get("Characters", [])
        self.name_to_voice = speakers

        script_lines = []
        story_data = script_text.get("story", [])

        for entry in story_data:
            speaker = entry["speaker"]
            line = entry["line"]
            script_lines.append((speaker, line))

        return script_lines


    def generate_subtitles(self, audio_file_path, subtitle_output_path="subtitles.txt"):
        """
        Generate subtitles using Whisper API.
        audio_file_path: path to the audio file
        subtitle_output_path: path to save the SRT file
        """

        # Load model
        model = whisper.load_model("base")

        # Transcribe with word timestamps
        result = model.transcribe(audio_file_path, word_timestamps=True)


        word_list = []
        # Access word level data & add to list
        print("Result word-level timestamps:", result["segments"])
        for segment in result["segments"]:
            for index,word in enumerate(segment["words"]):
                word_list.append({
                    "index": index,
                    "word": word['word'],
                    "start": word['start'],
                    "end": word['end']
                })

        
                print(f"{word['start']:.2f}s - {word['end']:.2f}s: {word['word']}")


        # Format Input with only index and word
        formatted_input = "\n".join([f"{w['index']}: {w['word']}" for w in word_list])

        prompt = group_scene_prompt.format(word_list=formatted_input)

        response = self.ask_llm_no_search(prompt)

        # Write subtitle to file
        with open(subtitle_output_path, "w") as f:
            for i, scene in enumerate(response):
                start_s = float(word_list[scene["start_index"]]["start"])
                
                # Check if there's a next scene
                if i < len(response) - 1:
                    # Use start of next scene as end time
                    end_s = float(word_list[response[i + 1]["start_index"]]["start"])
                else:
                    # Last scene - use its actual end time
                    end_s = float(word_list[scene["end_index"]]["end"])
                
                subtitle = ""
                f.write(f"{start_s} --> {end_s}\n")
                for i in range(scene["start_index"], scene["end_index"] + 1):
                    subtitle += word_list[i]["word"] + ""

                f.write(subtitle.strip() + "\n\n")


        print(f"✅ Subtitles saved to {subtitle_output_path}")

    def generate_audio(self, script_lines, output_dir="voicelines", srt_file="subtitles.srt", tts="kokoro"):
        """
        Generate audio files for each line in the script and create an SRT subtitle file.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        path_order = []
        srt_entries = []
        current_time = 0.0

        for i, (speaker, line) in enumerate(script_lines):
            output_dir = os.path.join(os.getcwd(), output_dir)
            filename = os.path.join(output_dir, f"line_{i}_{speaker}.wav")
            path_order.append(filename)
            print(f"Generating {speaker}: {line[:30]}...")
            
            audio_duration = self.generate_voice(line, self.name_to_voice[speaker], filename, tts=tts)
            
            # Prepare SRT entry
            start_ms = int(current_time * 1000)
            end_ms = int((current_time + audio_duration) * 1000)
            start = f"{start_ms//3600000:02}:{(start_ms//60000)%60:02}:{(start_ms//1000)%60:02},{start_ms%1000:03}"
            end = f"{end_ms//3600000:02}:{(end_ms//60000)%60:02}:{(end_ms//1000)%60:02},{end_ms%1000:03}"
            srt_entries.append(f"{i+1}\n{start} --> {end}\n {line}\n")
            
            current_time += audio_duration

        # Write SRT file
        with open(srt_file, "w") as f:
            f.write("\n".join(srt_entries))
        
        print(f"✅ All lines generated in {output_dir}")
        print(f"✅ Subtitles saved as {srt_file}")
        return path_order

    def merge_audio(self, audio_files, final_output="final_story.mp3", pause_ms=300):
        """
        Merge multiple audio files into one, with pauses in between.
        """
        clips = [AudioFileClip(f) for f in audio_files]

        pause_duration = pause_ms / 1000
        silent_clip = AudioClip(lambda t: 0, duration=pause_duration)

        sequence = []
        for i, clip in enumerate(clips):
            sequence.append(clip)
            if i < len(clips) - 1:
                sequence.append(silent_clip)

        final_clip = concatenate_audioclips(sequence)
        final_clip.write_audiofile(final_output)
        print(f"✅ Story exported as {final_output}")
        return final_output

    def merge_visuals_video(self, visual_file, audio_file, final_output="final_video.mp4", zoom=False, zoom_out=False):
        """
        Merge audio with a video or image.
        """
        import numpy as np
        from PIL import Image
        from moviepy import VideoClip
        
        audio = AudioFileClip(audio_file)
        
        if visual_file.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            print("Merging with video...")
            video = VideoFileClip(visual_file)
            
            if audio.duration > video.duration:
                from moviepy.video.fx.Loop import Loop
                video = video.with_effects([Loop(duration=audio.duration)])
            else:
                video = video.subclipped(0, audio.duration)

            final = video.with_audio(audio)
                
        else:
            print("Merging with Image...")
            video = ImageClip(visual_file, duration=audio.duration)

            if zoom:
                original_frame = video.get_frame(0)
                h, w = original_frame.shape[:2]
                
                def make_zoom_frame(t):
                    scale = 1 + 0.5 * (t / video.duration)
                    img = Image.fromarray(original_frame.astype('uint8'))
                    new_size = (int(w * scale), int(h * scale))
                    img_scaled = img.resize(new_size, Image.LANCZOS)
                    scaled_array = np.array(img_scaled)
                    
                    new_h, new_w = scaled_array.shape[:2]
                    start_h = (new_h - h) // 2
                    start_w = (new_w - w) // 2
                    
                    cropped = scaled_array[start_h:start_h+h, start_w:start_w+w]
                    return cropped
                
                video = VideoClip(make_zoom_frame, duration=video.duration)

            if zoom_out:
                original_frame = video.get_frame(0)
                h, w = original_frame.shape[:2]
                
                def make_zoom_out_frame(t):
                    scale = 1.5 - 0.5 * (t / video.duration)
                    img = Image.fromarray(original_frame.astype('uint8'))
                    new_size = (int(w * scale), int(h * scale))
                    img_scaled = img.resize(new_size, Image.LANCZOS)
                    scaled_array = np.array(img_scaled)
                    
                    new_h, new_w = scaled_array.shape[:2]
                    start_h = (new_h - h) // 2
                    start_w = (new_w - w) // 2
                    
                    cropped = scaled_array[start_h:start_h+h, start_w:start_w+w]
                    return cropped
                
                video = VideoClip(make_zoom_out_frame, duration=video.duration)
                
            final = video.with_audio(audio)
        
        final.write_videofile(final_output, fps=24, codec="libx264", audio_codec="aac")
        print(f"✅ Final video exported as {final_output}")


if __name__ == "__main__":
    editor = Editor(voice_ids={"MAN1": "voice_id_1", "W1": "voice_id_2"})
    script = {
        "Characters": {"NARRATOR": "MAN1"},
        "story": [
            {"speaker": "NARRATOR", "line": "This is the first line of the story."},
            {"speaker": "NARRATOR", "line": "This is the second line of the story."}
        ]
    }

    editor.generate_subtitles("backend/Generated_Audio_Topic_20251014_041715/audio.mp3", "test_subtitles.srt")
