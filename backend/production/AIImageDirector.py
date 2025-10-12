from backend.agents.base_agent import Agent
import os
import requests
from moviepy.video.VideoClip import ImageClip
from moviepy import (
    VideoFileClip,
    AudioFileClip,
    CompositeAudioClip,
    AudioClip,
    concatenate_audioclips,
    CompositeVideoClip,
    ImageSequenceClip,
    concatenate_videoclips,
    vfx,
    VideoClip,
)
from dotenv import load_dotenv
import json
import base64
import math


class Director(Agent):
    """
    Oversees the coordination between the audio and the visuals.
    """

    def __init__(self):
        super().__init__()
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.download_dir = "images"
    
    
    def load_srt_file(self, srt_file="subtitles.srt"):
        srt_file = "subtitles.srt"

        # Read entire SRT file into a string
        with open(srt_file, "r", encoding="utf-8") as f:
            srt_content = f.read()

        # Now srt_content holds the full subtitles as a string
        print(srt_content[:500])  # preview first 500 characters

        return srt_content


    def fetch_image(self, query):
        base_url = "https://pixabay.com/api/"
        params = {
            "key": os.getenv("PIXABAY_API_KEY"),
            "q": query,
            "image_type": "photo",
            "safesearch": "true",
            "per_page": 3
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["hits"]:
                return data["hits"][0]["webformatURL"]
        return None

    def download_image(self, url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(self.download_dir, filename)
            with open(path, "wb") as f:
                f.write(response.content)
            return path
        return None
    
    

    def fetch(self,query, imageRef=None, save_path="generated_image.png"):
        load_dotenv()
        url = "https://openrouter.ai/api/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {os.getenv('OPEN_ROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        if imageRef:
            # Convert imageRef to string if it's an object
            if hasattr(imageRef, 'url'):
                image_url = imageRef.url
            elif hasattr(imageRef, '__str__'):
                image_url = str(imageRef)
            else:
                image_url = imageRef
                
            # Image to image (modify existing image)
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": query},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ]
                }
            ]
        else:
            # Text to image
            messages = [
                {
                    "role": "user",
                    "content": query
                }
            ]
        
        payload = {
            "model": "google/gemini-2.5-flash-image-preview",
            "messages": messages,
            "modalities": ["image", "text"]
        }
        
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        # Check for errors
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(result)
            return
        
        # Process the response
        print("Response received from OpenRouter: ", result)

        if result.get("choices"):
            message = result["choices"][0]["message"]
            
            # Check for images in the response
            if message.get("images"):
                for image in message["images"]:
                    image_url = image["image_url"]["url"]
                    print(f"Generated image URL: {image_url[:50]}...")
                    
                    # If it's a base64 data URL, decode and save it
                    if image_url.startswith("data:image"):
                        # Extract base64 data
                        base64_data = image_url.split(",")[1]
                        img_data = base64.b64decode(base64_data)
                        
                        path = os.path.join(self.download_dir, save_path)
                        with open(path, "wb") as f:
                            f.write(img_data)
                        print(f"Image saved to {path}")
                    else:
                        # If it's a regular URL, download it
                        img_data = requests.get(image_url).content
                        with open(path, "wb") as f:
                            f.write(img_data)
                        print(f"Image saved to {path}")
            
            # Check for text content
            if message.get("content"):
                print(f"Assistant text: {message['content']}")

            return path


    def generate_image_seq_from_subtitles(self, video_file="final_video_no_sound.mp4"):
        """
        Analyze the script with an LLM and fetch appropriate Pixabay images for each story line.

        Returns a list of dicts: [{"line": str, "image_url": str}, ...]
        """
        #story_data = script_text.get("story", [])
        results = []

        srt_content = self.load_srt_file("subtitles.srt")


        # Ask LLM what kind of image would suit this line
        prompt = f"""
            You are an expert story teller visual.
            Given the following subtitles from a story: \"\"\"{srt_content}\"\"\"
            Your goal is to make the best possible video by selecting relevant images for the WHOLE story.
            You do not need to make an image for every line, only the most relevant ones that will help tell the story.
            It is advisable that you should only show the environrment and not the characters, unless it is absolutely necessary.

            Requirements:
            1. Output must be valid JSON, parseable by Python.
            2. JSON format: List of objects with keys:
            - "start_time": time in seconds the image should appear
            - "end_time": time in seconds the image should disappear
            - "keywords": a few words describing the image for Pixabay search
            3. Only include images that are relevant to the line.
            4. Do not add extra text outside the JSON.
            5. The sequence of images have to be longer than the subtitle suggest

            Example output:
            [
            {{"start_time": 0.0, "end_time": 5.2, "keywords": "dark forest, night, fog"}},
            {{"start_time": 5.2, "end_time": 8.7, "keywords": "mysterious cabin, lights on"}}
            ]
            """

        clips = []
        
        print("Promt: ", prompt)
        res = self.ask_llm_no_search(prompt)

        print("\n\n\n\nLLM Response: ", res)
        for i,entry in enumerate(res):
            #url = self.fetch_image(entry["keywords"])
        
            filename = f"{i}.png"
            #path = self.download_image(url, filename)
            path = self.fetch(entry["image_prompt"], imageRef=None, save_path=filename)
            print(f"Downloaded image to {path}")
            if path:
                clip = ImageClip(path, duration=entry["end_time"] - entry["start_time"])
                clip = clip.with_start(entry["start_time"])
                #clip = clip.with_position(("center", "center"))
                clips.append(clip)

        
        """ clips_with_zoom = []

        # Add zoom effect to each clip
        for clip in clips:
            def smooth_zoom(t):
                # Use easing function to smooth the zoom
                progress = t / clip.duration if clip.duration > 0 else 0
                # Smooth easing function
                smooth_progress = 0.5 * (1 - math.cos(math.pi * progress))
                return 1 + 0.02 * smooth_progress * clip.duration
            
            zoomed_clip = clip.with_effects([
                Resize(smooth_zoom)
            ]).with_position('center')
            
            clips_with_zoom.append(zoomed_clip) """


        final_video = CompositeVideoClip(clips)
        final_video.write_videofile(video_file, fps=24, codec="libx264", audio_codec="aac")

        return video_file

if __name__ == "__main__":
    director = Director()
    director.generate_image_seq_from_subtitles()

# ./backend/.venv/bin/python -m backend.production.video_director
