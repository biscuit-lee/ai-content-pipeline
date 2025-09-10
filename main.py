import requests
import os
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip, AudioClip, concatenate_audioclips,CompositeVideoClip, ImageSequenceClip,concatenate_videoclips,vfx,VideoClip
import dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from openai import OpenAI
import json
import numpy as np
from PIL import Image
import subprocess
import shlex
from moviepy.video.VideoClip import ImageClip
from moviepy.video.fx import Resize
import math
from moviepy.video.fx.Loop import Loop
dotenv.load_dotenv()
import prompts
import random
import csv
from datetime import datetime
from googleapiclient.discovery import build
import inquirer
from inquirer.themes import GreenPassion

"""
NOTES

REturn format

return a json 

{
    "Characters": {"NARRATOR": "MAN1", "ALICE": "WOMAN1", "BOB": "MAN2"},
    

    "story": [
        {"speaker": "NARRATOR", "line": "So I walked into the room..."},
        {"speaker": "ALICE", "line": "Are you sure this is safe?"},
}


SCRIPT FORMAT:
- SPEAKERS LIST: NARRATOR, ALICE, BOB
- Return a json list of (SPEAKER, LINE) tuples only, no extra text.
- Example: [("NARRATOR", "So I walked into the room..."), ("ALICE", "Are you sure this is safe?"), ...]

"""


CSV_FILE = "youtube_story_tracking.csv"
CHANNEL_ID = os.getenv("YT_CHANNEL_ID")


class Agent:
    def ask_llm(self, prompt):
        
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        )

        completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
         ]
        )

        res = self.deserialize_response(completion.choices[0].message.content)
        return res
    
    def deserialize_response(self, response) -> dict:

        try:
            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()

            return json.loads(response)
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return response

# ---------------- CONFIG ----------------
API_KEY = os.getenv("ELEVENLABS_API_KEY")
MODEL_ID = "eleven_multilingual_v2"

VOICE_IDS = {
    "MAN1": "JBFqnCBsd6RMkjVDRZzb",
    "MAN2": "JBFqnCBsd6RMkjVDRZzb",
    "WOMAN1": "si0svtk05vPEuvwAW93c",
    "WOMAN2": "si0svtk05vPEuvwAW93c",
    "NARRATOR": "JBFqnCBsd6RMkjVDRZzb"
}

# ---------------- CLASSES ----------------
import itertools
from prompts import business_psych_ideas
class IdeaGeneratorBiz(Agent):
    def __init__(self):
        pass
    def generate_idea(self):

        """Return json 
        
        res : 
        
    {"topic_title": "Why Netflix Cancels Shows Right When They Get Good",
    "hook_angle": "Netflix spends millions making shows, then cancels them at their peak popularity",
    "central_mystery": "Why would a company destroy their most valuable content when viewers are most engaged?",
    "key_examples": [
        "The OA - canceled after massive fan campaign",
        "Sense8 - expensive production, devoted fanbase, canceled after 2 seasons",
        "Teenage Bounty Hunters - 100% Rotten Tomatoes, still canceled"
    ],
    "psychological_principles": [
        "Sunk cost fallacy exploitation",
        "Loss aversion in subscription retention",
        "Novelty bias in content consumption"
    ],
    "viral_potential_score": int,
    "why_it_works": str}
        
        """
        prompt = business_psych_ideas
        res = self.ask_llm(prompt)


        return res
        
        


class IdeaGenerator(Agent):
    def __init__(self):
        self.story_experiments = {
            "formats": [
                {"name": "Single Long Story","description": "One full story, emotional arc from start to finish","example_hook": "The night I discovered my family's darkest secret"},
                {"name": "Multiple Short Stories","description": "2–5 mini stories in one video, each 3–5 min","example_hook": "Three times strangers changed my life forever"},
                {"name": "Series / Parted Story","description": "One story split across multiple episodes","example_hook": "Part 1: My creepy roommate"},
                {"name": "Thematic Compilation","description": "Stories around a theme (betrayal, horror, regret)","example_hook": "Top 5 chilling campfire confessions"},
                {"name": "Interactive / POV","description": "Story told as if viewer is the character","example_hook": "You wake up in a cabin, and it's not empty…"},
                {"name": "What If / Hypothetical","description": "Short fictional 'what would you do?' scenarios","example_hook": "What would you do if your best friend disappeared overnight?"}
            ],
            "styles": [
                {"name": "Dramatic / Emotional", "use_when": "Heavy family/friendship drama, betrayal"},
                {"name": "Cozy / Campfire", "use_when": "Fantasy, light horror, feel-good stories"},
                {"name": "Creepy / Horror", "use_when": "Campfire horror, suspense, urban legends"},
                {"name": "Funny / Relatable", "use_when": "Slice-of-life, awkward moments, social fails"},
                {"name": "Twist / Shock Ending", "use_when": "Story builds normally then hits twist"},
                {"name": "Inspirational / Uplifting", "use_when": "Overcoming struggle, life lessons"}
            ],
            "lengths": [
                {"duration": "5–10 min", "pros": "Fast consumption; high retention", "cons": "Hard to develop emotional arc"},
                {"duration": "15–25 min", "pros": "Solid storytelling; room for multiple arcs", "cons": "Requires good editing & pacing"},
                {"duration": "25–45 min", "pros": "Deep immersion; loyal viewers", "cons": "Needs strong hook upfront"},
                {"duration": "50+ min", "pros": "Marathon content; binge potential", "cons": "Hard to retain casual viewers"}
            ],
            "story_categories": [
                {"name": "Home Invasion/Stalking","appeal": "Universal fear, personal safety","age_range": "16-35","settings": ["apartments","family homes","dorms"]},
                {"name": "Workplace Horror","appeal": "Adult relatability, professional vulnerability","age_range": "22-45","settings": ["offices","retail","restaurants","night shifts"]},
                {"name": "Dating Nightmares","appeal": "Romance vulnerability, trust betrayal","age_range": "18-35","settings": ["online dating","blind dates","college parties"]},
                {"name": "Childhood Trauma","appeal": "Protective instincts, innocence lost","age_range": "8-17","settings": ["school","neighborhood","family events"]},
                {"name": "Travel/Vacation Horror","appeal": "Isolation, unfamiliar territory","age_range": "18-40","settings": ["hotels","airbnb","camping","road trips"]},
                {"name": "Neighbor Situations","appeal": "Ongoing proximity, can't escape","age_range": "25-50","settings": ["suburban homes","apartments","rural properties"]}
            ],
            "narrator_demographics": [
                {"age_group": "Teen (14-17)","voice": "WOMAN1 or MAN1","situations": ["school","family home","part-time jobs"],"vulnerability": "inexperience, dependence on adults"},
                {"age_group": "Young Adult (18-25)","voice": "WOMAN1 or MAN1","situations": ["college","first apartments","early career"],"vulnerability": "independence, financial constraints"},
                {"age_group": "Adult (26-35)","voice": "WOMAN2 or MAN2","situations": ["established career","homeowner","parent"],"vulnerability": "responsibility for others, established routines"},
                {"age_group": "Older Adult (36-50)","voice": "WOMAN2 or MAN2","situations": ["long-term resident","experienced professional"],"vulnerability": "overconfidence, routine predictability"}
            ],
            "emotional_tones": [
                {"name": "Authentic Fear","description": "Genuine terror, realistic reactions","best_for": "Home invasion, stalking, workplace threats"},
                {"name": "Creeping Dread","description": "Slow-building unease, something's not right","best_for": "Neighbor situations, workplace dynamics"},
                {"name": "Betrayal Shock","description": "Trusted person reveals dark side","best_for": "Dating, workplace, family situations"},
                {"name": "Violation/Invasion","description": "Personal space/privacy compromised","best_for": "Home invasion, stalking, travel"}
            ],
            "viral_elements": [
                "Specific memorable detail (figurine, wave, text message)",
                "Universal relatable fear",
                "Authentic dialogue/internal thoughts",
                "Unresolved mystery element",
                "Location/time specificity",
                "Realistic police/authority response"
            ],
            "optimal_specs": {
                "hook_timing": "First 15 seconds",
                "tension_beats": "3-4 escalating moments",
                "resolution": "Clear but leaves questions for engagement"
            }
        }
        
        self.selections = {}

    def create_format_choices(self):
        choices = []
        for fmt in self.story_experiments["formats"]:
            choice_text = f"{fmt['name']} - {fmt['description'][:50]}..."
            choices.append((choice_text, fmt))
        return choices

    def create_style_choices(self):
        choices = []
        for style in self.story_experiments["styles"]:
            choice_text = f"{style['name']} - {style['use_when']}"
            choices.append((choice_text, style))
        return choices

    def create_length_choices(self):
        choices = []
        for length in self.story_experiments["lengths"]:
            choice_text = f"{length['duration']} - {length['pros']}"
            choices.append((choice_text, length))
        return choices

    def create_category_choices(self):
        choices = []
        for cat in self.story_experiments["story_categories"]:
            choice_text = f"{cat['name']} - {cat['appeal']} (Age: {cat['age_range']})"
            choices.append((choice_text, cat))
        return choices

    def create_narrator_choices(self):
        choices = []
        for narrator in self.story_experiments["narrator_demographics"]:
            choice_text = f"{narrator['age_group']} - {narrator['voice']}"
            choices.append((choice_text, narrator))
        return choices

    def create_tone_choices(self):
        choices = []
        for tone in self.story_experiments["emotional_tones"]:
            choice_text = f"{tone['name']} - {tone['description']}"
            choices.append((choice_text, tone))
        return choices

    def create_viral_element_choices(self):
        choices = []
        for element in self.story_experiments["viral_elements"]:
            choices.append((element, element))
        return choices

    def display_summary(self):
        print("\n" + "="*60)
        print("📋  YOUR STORY CONFIGURATION".center(60))
        print("="*60)
        
        print(f"\n🎬 Format: {self.selections['format']['name']}")
        print(f"   {self.selections['format']['description']}")
        print(f"   Example: {self.selections['format']['example_hook']}")
        
        print(f"\n🎭 Style: {self.selections['style']['name']}")
        print(f"   Use when: {self.selections['style']['use_when']}")
        
        print(f"\n⏱️  Length: {self.selections['length']['duration']}")
        print(f"   Pros: {self.selections['length']['pros']}")
        print(f"   Cons: {self.selections['length']['cons']}")
        
        print(f"\n🎯 Category: {self.selections['category']['name']}")
        print(f"   Appeal: {self.selections['category']['appeal']}")
        print(f"   Target Age: {self.selections['category']['age_range']}")
        print(f"   Settings: {', '.join(self.selections['category']['settings'])}")
        
        print(f"\n🎙️  Narrator: {self.selections['narrator']['age_group']}")
        print(f"   Voice: {self.selections['narrator']['voice']}")
        print(f"   Situations: {', '.join(self.selections['narrator']['situations'])}")
        print(f"   Vulnerability: {self.selections['narrator']['vulnerability']}")
        
        print(f"\n😰 Emotional Tone: {self.selections['emotional_tone']['name']}")
        print(f"   Description: {self.selections['emotional_tone']['description']}")
        print(f"   Best for: {self.selections['emotional_tone']['best_for']}")
        
        print(f"\n💡 Viral Element: {self.selections['viral_element']}")
        
        print("\n📊 OPTIMAL SPECS:")
        print("• Hook timing: First 15 seconds")
        print("• Tension beats: 3-4 escalating moments") 
        print("• Resolution: Clear but leaves questions for engagement")
        print("="*60)

    def generate_prompt_from_selections(self):
        """Generate AI prompt using the interactive selections"""
        if not self.selections:
            return "No selections made yet!"
            
        prompt = (
            f"Generate a YouTube story idea with these specifications:\n\n"
            f"FORMAT: {self.selections['format']['name']} ({self.selections['format']['description']})\n"
            f"Example hook: {self.selections['format']['example_hook']}\n\n"
            f"STYLE: {self.selections['style']['name']} (Use when: {self.selections['style']['use_when']})\n"
            f"LENGTH: {self.selections['length']['duration']} (Pros: {self.selections['length']['pros']}, Cons: {self.selections['length']['cons']})\n\n"
            f"CATEGORY: {self.selections['category']['name']} (Appeal: {self.selections['category']['appeal']})\n"
            f"Settings: {', '.join(self.selections['category']['settings'])}\n\n"
            f"NARRATOR: {self.selections['narrator']['age_group']} (Voice: {self.selections['narrator']['voice']})\n"
            f"Typical situations: {', '.join(self.selections['narrator']['situations'])}\n"
            f"Vulnerability: {self.selections['narrator']['vulnerability']}\n\n"
            f"EMOTIONAL TONE: {self.selections['emotional_tone']['name']} ({self.selections['emotional_tone']['description']})\n"
            f"Best for: {self.selections['emotional_tone']['best_for']}\n\n"
            f"VIRAL ELEMENT: {self.selections['viral_element']}\n\n"
            f"TARGET SPECS:\n"
            f"• Hook timing: {self.story_experiments['optimal_specs']['hook_timing']}\n"
            f"• Tension beats: {self.story_experiments['optimal_specs']['tension_beats']}\n"
            f"• Resolution: {self.story_experiments['optimal_specs']['resolution']}\n\n"
            f"Create a compelling story title and description that would make viewers click. "
            f"Only provide the title, idea and description not the whole story and all the important parameters that was given to you above, becuase your response will be given to a writer, make the writer understand everything and fulfil the requirements above"
        )
        
        return {
            "prompt": prompt,
            "format_name": self.selections['format'],   
            "style_name": self.selections['style'],       
            "length_duration": self.selections['length'], 
            "category_name": self.selections['category'], 
            "narrator": self.selections['narrator'],     
            "tone_name": self.selections['emotional_tone'], 
            "viral_element": self.selections['viral_element'] 
        }
    def run(self):
        """Interactive CLI mode with arrow keys"""
        print("🔥 REDDIT STORY GENERATOR 🔥\n")
        
        questions = [
            inquirer.List(
                'format',
                message="📽️  Choose your story format",
                choices=self.create_format_choices(),
                carousel=True
            ),
            inquirer.List(
                'style',
                message="🎭  Choose your story style",
                choices=self.create_style_choices(),
                carousel=True
            ),
            inquirer.List(
                'length',
                message="⏱️  Choose video length",
                choices=self.create_length_choices(),
                carousel=True
            ),
            inquirer.List(
                'category',
                message="🎯  Choose story category",
                choices=self.create_category_choices(),
                carousel=True
            ),
            inquirer.List(
                'narrator',
                message="🎙️  Choose narrator demographics",
                choices=self.create_narrator_choices(),
                carousel=True
            ),
            inquirer.List(
                'tone',
                message="😰  Choose emotional tone",
                choices=self.create_tone_choices(),
                carousel=True
            ),
            inquirer.List(
                'viral_element',
                message="💡  Choose viral element",
                choices=self.create_viral_element_choices(),
                carousel=True
            )
        ]
        
        # Ask all questions with arrow key navigation
        answers = inquirer.prompt(questions, theme=GreenPassion())
        
        if not answers:  # User cancelled
            return None
            
        # Store selections
        self.selections = {
            'format': answers['format'],
            'style': answers['style'], 
            'length': answers['length'],
            'category': answers['category'],
            'narrator': answers['narrator'],
            'emotional_tone': answers['tone'],
            'viral_element': answers['viral_element']
        }
        
        # Display final summary
        self.display_summary()
        
        # Generate prompt with selected options
        prompt = self.generate_prompt_from_selections()
        
        print(f"\n🎉 Configuration complete!")
        print("\n" + "="*60)
        print("🤖 GENERATED PROMPT FOR AI:")
        print("="*60)
        print(prompt)
        print("="*60)
        
        return self.selections


class Writer(Agent):
    """
    Handles scripts: input, formatting, and speaker assignment.
    """
    def __init__(self):
        self.niches = ["relationship betrayal",
            "workplace revenge",
            "family secrets",
            "social media gone wrong",
            "mysterious neighbor",
            "dating app horror story",
            "roommate from hell"
        ]

        self.type = ""

        """
        raw_script: list of (SPEAKER, LINE)
        """
        #self.script_lines = raw_script
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"

    def get_lines(self):
        return self.script_lines
    
    def deserialize_response(self, response) -> dict:

        try:
            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()

            return json.loads(response)
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return None
        
    
    def get_promtpt(self, genre,type_story="narration"):
        if type_story == "narration":
            prompt = prompts.prompt_narration
        elif type_story == "act":
            prompt = prompts.prompt_dialogue
        elif type_story == "mix":
            prompt = prompts.prompt_mixed

        elif type_story == "campfire_long":
            prompt = prompts.campfire_narration_third_person

        elif type_story == "biz":
            prompt = prompts.business_psych_prompt2
            self.type = "biz"
            return prompt

        
        return prompt.format(genre=genre)
    
    def generate_script(self, type,genre="reddit style story relationship"):
        prompt = self.get_promtpt(genre, type_story=type)

        if self.type == "biz":
            topic = genre["topic_title"]
            hook = genre["hook_angle"]
            central_mystery = genre["central_mystery"]
            key_examples = genre["key_examples"]
            psychological_principles = genre["psychological_principles"]
            viral_potential_score = genre["viral_potential_score"]
            why_it_works = genre["why_it_works"]

            prompt = prompt.format(
                topic_title=topic,
                hook_angle=hook,
                central_mystery=central_mystery,
                key_examples=key_examples,
                psychological_principles=psychological_principles,
                why_it_works=why_it_works
            )


        print("GENERATING SCRIPT WITH THE PROMPT: \n\n\n\n\n", prompt, "\n\n\n\n\n")
        response = self.ask_llm(prompt)
        if response:
            self.script_lines = response
            return response
        else:
            print("Failed to generate script.")
            return None
    
    def add_line(self, speaker, line):
        self.script_lines.append((speaker, line))


class Director(Agent):
    """
    Oversees the coordination between the audio and the visuals.
    """

    def __init__(self):
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.download_dir = "images"
    
    
    def deserialize_response(self, response) -> dict:

        try:
            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()

            return json.loads(response)
        except json.JSONDecodeError:
            print(f"[{self.name}] Failed to parse JSON: {response}")
            return None
    
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
        res = self.ask_llm(prompt)

        print("\n\n\n\nLLM Response: ", res)
        for i,entry in enumerate(res):
            url = self.fetch_image(entry["keywords"])
            if url:
                filename = f"img_{i}.jpg"
                path = self.download_image(url, filename)
                if path:
                    clip = ImageClip(path, duration=entry["end_time"] - entry["start_time"])
                    clip = clip.with_start(entry["start_time"])
                    #clip = clip.with_position(("center", "center"))
                    clips.append(clip)

        
        clips_with_zoom = []

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
            
            clips_with_zoom.append(zoomed_clip)


        final_video = CompositeVideoClip(clips_with_zoom)
        final_video.write_videofile(video_file, fps=24, codec="libx264", audio_codec="aac")



        return video_file




class Editor(Agent):
    """
    Handles TTS generation, merging audio, and final output.
    """
    def __init__(self, voice_ids, model_id=MODEL_ID):
        self.voice_ids = voice_ids
        self.model_id = model_id
        self.name_to_voice = {}


    def generate_voice(self, text, speaker, output_path, tts="kokoro"):

        """"
        Generate voice using ElevenLabs TTS API.

        text: text to convert to speech
        speaker: speaker of the line (MAN1, MAN2, OR W1 OR W2)
        output_path: path to save the generated audio file
        returns: duration of the audio in seconds

        """

        output_path = os.path.join(os.getcwd(), output_path)

        if tts == "elevenlabs":
            client = ElevenLabs(api_key=API_KEY)
            voice_id = self.voice_ids[speaker]
            # Generate TTS audio
            audio_stream = client.text_to_speech.convert(
                voice_id=voice_id,
                model_id=self.model_id,
                text=text,
                output_format="mp3_44100_128",
                voice_settings={"stability": 0.6, "similarity_boost": 0.8},
            )

            # Save to file
            with open(output_path, "wb") as f:
                for chunk in audio_stream:
                    f.write(chunk)

        elif tts == "xtts":
            url = "http://127.0.0.1:8000/generate-audio/"
            payload = {
                "text": text,
                "file_path": output_path,
                "voice" : speaker
            }

            response = requests.post(url, json=payload)

        elif tts == "kokoro":
            # Kokoro only accept .wav filename
            output_path = output_path.replace(".mp3", ".wav")
            url = "http://127.0.0.1:8000/generate-audio/"
            payload = {
                "text": text,
                "file_path": output_path,
                "voice" : speaker
            }

            response = requests.post(url, json=payload)
            


        # Get duration
        audio_clip = AudioFileClip(output_path)
        duration = audio_clip.duration  # seconds
        audio_clip.close()

        print(f"✅ Audio saved to {output_path}, duration: {duration:.2f}s")
        return duration


    def analyze_script(self, script_text: dict):
        """
        Analyze the script and return structured data.
        script_text: dict with keys "Characters" and "story"
        returns: list of tuples (speaker, line)
        """
        speakers = script_text.get("Characters", [])
        
        self.name_to_voice = speakers
        amount_of_characters = len(speakers)

        # Fetch scripts for each character
        script_lines = []
        story_data = script_text.get("story", [])

        # Each entry in story_data is expected to be a dict with "speaker" and "line"
        for entry in story_data:
            speaker = entry["speaker"]
            line = entry["line"]
            script_lines.append((speaker, line))

        return script_lines

    def create_srt(script_lines, audio_durations, output_file="subtitles.srt"):
        """
        Creates an .srt subtitle file from script lines and their audio durations.

        Parameters:
        - script_lines: list of tuples (speaker, line)
        - audio_durations: list of floats, duration in seconds for each line
        - output_file: filename for the generated .srt
        """
        current_time = 0.0  # cumulative time for subtitles
        srt_entries = []

        for i, ((speaker, line), duration) in enumerate(zip(script_lines, audio_durations), start=1):
            start_ms = int(current_time * 1000)
            end_ms = int((current_time + duration) * 1000)

            start = f"{start_ms//3600000:02}:{(start_ms//60000)%60:02}:{(start_ms//1000)%60:02},{start_ms%1000:03}"
            end = f"{end_ms//3600000:02}:{(end_ms//60000)%60:02}:{(end_ms//1000)%60:02},{end_ms%1000:03}"

            srt_entries.append(f"{i}\n{start} --> {end}\n{speaker}: {line}\n")
            current_time += duration

        with open(output_file, "w") as f:
            f.write("\n".join(srt_entries))

        print(f"✅ Subtitles saved as {output_file}")

    def generate_audio(self, script_lines, output_dir="voicelines", srt_file="subtitles.srt"):

        """
        Generate audio files for each line in the script and create an SRT subtitle file.
        script_lines: list of tuples (speaker, line)
        output_dir: directory to save audio files
        srt_file: path to save the generated .srt file
        returns: list of generated audio file paths
        
        """


        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        path_order = []
        srt_entries = []
        current_time = 0.0  # cumulative time for subtitles

        for i, (speaker, line) in enumerate(script_lines):
            output_dir = os.path.join(os.getcwd(), output_dir)
            filename = os.path.join(output_dir, f"line_{i}_{speaker}.wav")
            path_order.append(filename)
            print(f"Generating {speaker}: {line[:30]}...")
            
            # Generate TTS and get duration
            audio_duration = self.generate_voice(line, self.name_to_voice[speaker], filename)
            
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
        audio_files: list of audio file paths to merge
        final_output: path to save the merged audio
        pause_ms: duration of pause between clips in milliseconds
        returns: path to the merged audio file

        """

        clips = [AudioFileClip(f) for f in audio_files]

        # Create silent AudioClip dynamically
        pause_duration = pause_ms / 1000  # convert ms to seconds
        silent_clip = AudioClip(lambda t: 0, duration=pause_duration)

        # Build sequence with pauses in between
        sequence = []
        for i, clip in enumerate(clips):
            sequence.append(clip)
            if i < len(clips) - 1:
                sequence.append(silent_clip)  # insert pause between lines

        final_clip = concatenate_audioclips(sequence)
        final_clip.write_audiofile(final_output)
        print(f"✅ Story exported as {final_output}")
        return final_output
    

    def merge_visuals_video(self, visual_file, audio_file, final_output="final_video.mp4", zoom=False, zoom_out=False):
        """
        Merge audio with a video or image.
        
        visual_file: path to video or image
        audio_file: path to audio file (mp3/wav)
        final_output: output video path
        zoom: if True and visual_file is image, apply slow zoom effect
        """
        
        audio = AudioFileClip(audio_file)
        
        # Check if visual is a video or an image
        if visual_file.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            print("Merging with video...")
            #print(__version__)
            # Load video
            video = VideoFileClip(visual_file)
            
            # Trim or loop video to match audio duration
            print(f"Video duration: {video.duration}, Audio duration: {audio.duration}")
            if audio.duration > video.duration:
                video = video.with_effects([Loop(duration=audio.duration)])
            else:
                video = video.subclipped(0, audio.duration)


            if zoom:
                pass
            
            final = video.with_audio(audio)
                
        else:
            print("Merging with Image...")

            # Base image clip with duration
            video = ImageClip(visual_file, duration=audio.duration)

            if zoom:
                # Get the original image data
                original_frame = video.get_frame(0)
                h, w = original_frame.shape[:2]
                
                def make_zoom_frame(t):
                    scale = 1 + 0.5 * (t / video.duration)  # Zoom factor
                    
                    # Convert to PIL Image
                    img = Image.fromarray(original_frame.astype('uint8'))
                    
                    # Resize image
                    new_size = (int(w * scale), int(h * scale))
                    img_scaled = img.resize(new_size, Image.LANCZOS)
                    scaled_array = np.array(img_scaled)
                    
                    # Center crop to keep original dimensions
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
                    
                    
                    # Start at high zoom, reduce over time
                    scale = 1.5 - 0.5 * (t / video.duration)  # Goes from 1.5x to 1.0x
                    
                    # Convert to PIL Image
                    img = Image.fromarray(original_frame.astype('uint8'))
                    
                    # Resize image
                    new_size = (int(w * scale), int(h * scale))
                    img_scaled = img.resize(new_size, Image.LANCZOS)
                    scaled_array = np.array(img_scaled)
                    
                    # Center crop to keep original dimensions
                    new_h, new_w = scaled_array.shape[:2]
                    start_h = (new_h - h) // 2
                    start_w = (new_w - w) // 2
                    
                    cropped = scaled_array[start_h:start_h+h, start_w:start_w+w]
                    return cropped
                
                video = VideoClip(make_zoom_out_frame, duration=video.duration)  
            final = video.with_audio(audio)
        
        # Export
        final.write_videofile(final_output, fps=24, codec="libx264", audio_codec="aac")
        print(f"✅ Final video exported as {final_output}")


def burn_subtitles(video_file="final_video.mp4", srt_file="subtitles.srt", output_file="final_video_subtitled.mp4"):
    # Check files exist
    if not os.path.exists(video_file):
        print(f"❌ Video file not found: {video_file}")
        return
    if not os.path.exists(srt_file):
        print(f"❌ SRT file not found: {srt_file}")
        return

    # FFmpeg command
    cmd = f'ffmpeg -i "{video_file}" -vf "subtitles={srt_file}:force_style=\'FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF&\'" -c:a copy "{output_file}"'
    
    # Use shlex.split for safety on Unix/WSL
    process = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    
    if process.returncode == 0:
        print(f"✅ Subtitles burned successfully: {output_file}")
    else:
        print("❌ Error burning subtitles")
        print(process.stderr)

    def create_final_output(self, script_lines, video_file=None, final_audio="final_story.mp3", final_video="final_video.mp4"):
        output_dir = "output"
        self.generate_audio(script_lines, output_dir=output_dir)

        audio_files = [
            os.path.join(output_dir, f)
            for f in os.listdir(output_dir)
            if f.endswith((".mp3", ".wav"))
        ]
        self.merge_audio(audio_files, final_output=final_audio)

        if video_file:
            self.merge_visuals(video_file, final_audio, final_output=final_video)




    class Reviewer(Agent):
        """
        Reviews a script and provides constructive criticism using LLM.
        """
        def __init__(self):
            super().__init__()

        def review_script(self, script):
            """
            Takes in a script and uses LLM to review its storytelling.
            Returns constructive criticism.
            """
            prompt = f"""
            You are a professional script reviewer. Analyze the following script for its storytelling quality:
            
            Script:
            {json.dumps(script, indent=4)}
            
            Provide constructive criticism on the following aspects:
            1. Plot structure (beginning, middle, end).
            2. Character development and dialogue.
            3. Engagement and pacing.
            4. Suggestions for improvement.

            Your response should be clear and concise.
            """
            response = self.ask_llm(prompt)
            return response
        
def validate_step(output, regenerate_func=None, *args, **kwargs):
    print("\n--- Output Preview ---\n")
    print(output)
    print("\n----------------------\n")
    
    while True:
        choice = input("Accept (a), Regenerate (r), or Quit (q)? ").strip().lower()
        if choice == "a":
            return output
        elif choice == "r" and regenerate_func:
            output = regenerate_func(*args, **kwargs)
            print("\n--- Regenerated Output ---\n")
            print(output)
        elif choice == "q":
            exit()
        else:
            print("Invalid choice, try again.")


def save_to_csv(story_data, csv_file="youtube_story_tracking.csv"):
    """
    Save story idea specs and YouTube metrics to CSV.
    
    story_data: dict with keys:
        - format_name
        - style_name
        - length_duration
        - category_name
        - tone_name
        - viral_element
        - yt_views
        - yt_likes
        - yt_comments
        - yt_ctr
    """
    # Ensure all keys exist
    keys = ["timestamp", "format_name", "style_name", "length_duration",
            "category_name", "tone_name", "viral_element",
            "yt_views", "yt_likes", "yt_comments", "yt_ctr","id"]
    
    # Add timestamp
    story_data["timestamp"] = datetime.now().isoformat()
    
    # Check if CSV exists
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            existing = True
    except FileNotFoundError:
        existing = False
    
    # Write data
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        if not existing:
            writer.writeheader()
        writer.writerow({k: story_data.get(k, "") for k in keys})


def add_id_to_csv(csv_file=CSV_FILE, channel_id=CHANNEL_ID, api_key=API_KEY):
    # Initialize YouTube API client
    youtube = build("youtube", "v3", developerKey=api_key)
    
    # Get the uploads playlist ID for the channel
    res = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    
    uploads_playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    
    # Fetch the latest video from the uploads playlist
    playlist_items = youtube.playlistItems().list(
        part="snippet",
        playlistId=uploads_playlist_id,
        maxResults=1
    ).execute()
    
    latest_video = playlist_items["items"][0]["snippet"]
    video_id = latest_video["resourceId"]["videoId"]
    video_title = latest_video["title"]
    
    # Append to CSV
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=None)  # None will auto-use headers from first row
        writer.writerow({"id": video_id, "title": video_title})  # add other fields as needed
    
    print(f"Appended video '{video_title}' with ID {video_id} to CSV.")




# ---------------- USAGE EXAMPLE --------------------------------------------
if __name__ == "__main__":

    """ choice = input("Make Video (v) or Update csv (c)")
    if (choice.strip().lower() == "c"):
        add_id_to_csv()

    generator = IdeaGenerator()
    #generator.run()
    res_gen = generator.generate_prompt_from_selections()
    res_gen["yt_views"] = 0
    res_gen["yt_likes"] = 0
    res_gen["yt_comments"] = 0
    res_gen["yt_ctr"] = 0.0
    res_gen["id"] = 1

    """
    questions = [
        inquirer.List(
            'narration_type',
            message="Choose Narration type",
            choices=[
                ('Narration', 'narration'),
                ('Dialogue (Acted)', 'act'),
                ('Mixed', 'mix'),
                ('Campfire Long', 'campfire_long'),
                ('Business Psychology','biz')
            ]
        )
    ]
    answers = inquirer.prompt(questions)
    narration_type = answers['narration_type']


    """ save_to_csv(res_gen)

    prompt = res_gen["prompt"]
    genre = generator.ask_llm(prompt) """
    

    """ generator = IdeaGeneratorBiz()
    idea = validate_step(
        generator.generate_idea(),
        regenerate_func=generator.generate_idea()) """

    idea = """
    {
        "topic_title": "Why Airlines Overbook Flights They Know Will Be Full",
        "hook_angle": "Airlines intentionally sell more tickets than seats exist, creating guaranteed conflict and customer anger",
        "central_mystery": "Why would an industry built on customer satisfaction deliberately create situations that lead to public confrontations and forced compensation?",
        "key_examples": [
            "United Airlines Flight 3411 dragging incident (2017)",
            "Delta's systematic overbooking statistics",
            "Southwest's public overbooking disclosure reports"
        ],
        "psychological_principles": [
            "Statistical exploitation of no-show probability",
            "Cost-benefit analysis of angry customers vs empty seats",
            "Anchoring effect of base ticket price vs compensation cost",
            "Diffusion of responsibility in oversold situations"
        ],
        "viral_potential_score": 9,
        "why_it_works": "Nearly every adult has experienced flight overbooking, reveals brilliant statistical manipulation, creates immediate pattern recognition for travel, triggers strong emotional response about being treated as a statistic"
    }
    """

    idea = json.loads(idea)
    writer = Writer()
    """ script = validate_step(
        writer.generate_script(genre=story_genre,type="narration"),
        regenerate_func=writer.generate_script,
        genre=story_genre
    ) """

    script = writer.generate_script(genre=idea, type=narration_type)

    editor = Editor(VOICE_IDS)
    """ script_lines = validate_step(
        editor.analyze_script(script),
        regenerate_func=editor.analyze_script,
        script=script
    ) """

    script_lines = editor.analyze_script(script)
    print(f"SCRIPT LINES \n\n {script_lines} \n\n\n")

    """ audio_files = validate_step(
        editor.generate_audio(script_lines, output_dir="output"),
        regenerate_func=editor.generate_audio,
        script_lines=script_lines,
        output_dir="output"
    ) """

    audio_files = editor.generate_audio(script_lines, output_dir="output")

    merged_audio = editor.merge_audio(audio_files, final_output="multi_voice_story.mp3")
    validate_step(merged_audio)  # You could just check if it's OK

    director = Director()
    image_seq_file = validate_step(
        director.generate_image_seq_from_subtitles(),
        regenerate_func=director.generate_image_seq_from_subtitles
    )

    editor.merge_visuals_video(image_seq_file, merged_audio, final_output="final_video.mp4", zoom=False)
    burn_subtitles()