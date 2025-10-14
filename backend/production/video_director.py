import os
import time
import requests
from backend.agents.base_agent import Agent
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
import base64

from openai import OpenAI


from moviepy.video.VideoClip import ImageClip
from moviepy.video.fx import Resize
from moviepy.video.fx.Loop import Loop
from dotenv import load_dotenv
class VisualSource:
    """Abstract base class for visual sources"""
    def fetch(self, query, save_path):
        """Fetch visual content based on query and save to filename"""
        raise NotImplementedError


class AIImageSource(VisualSource):
    
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
                        
                        with open(save_path, "wb") as f:
                            f.write(img_data)
                        print(f"Image saved to {save_path}")
                    else:
                        # If it's a regular URL, download it
                        img_data = requests.get(image_url).content
                        with open(save_path, "wb") as f:
                            f.write(img_data)
                        print(f"Image saved to {save_path}")
            
            # Check for text content
            if message.get("content"):
                print(f"Assistant text: {message['content']}")



class PexelsImageSource(VisualSource):
    def fetch(self, query, filename):
        # Pexels image fetching logic
        pass

class PexelsVideoSource(VisualSource):
    def fetch(self, query, filename):
        # Pexels video fetching logic
        pass


class VideoDirector(Agent):
    """
    Oversees the coordination between the audio and the visuals using videos from Pexels.
    """

    def __init__(self,downloadDir,visual_source=None):
        super().__init__()
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.download_dir = downloadDir
        self.visual_source = visual_source or AIImageSource()

        # Create download directory if it doesn't exist
        os.makedirs(self.download_dir, exist_ok=True)
    
    def set_visual_source(self, source):
        self.visual_source = source

    def load_srt_file(self, srt_file="subtitles.srt"):
        

        # Read entire SRT file into a string
        with open(srt_file, "r", encoding="utf-8") as f:
            srt_content = f.read()

        # Now srt_content holds the full subtitles as a string
        print(srt_content[:500])  # preview first 500 characters

        return srt_content

    def fetch_video(self, query):
        """
        Fetch video from Pexels API
        """
        base_url = "https://api.pexels.com/videos/search"
        headers = {
            "Authorization": os.getenv("PEXELS_API_KEY")
        }
        params = {
            "query": query,
            "per_page": 3,
            "size": "medium"  # Options: large, medium, small
        }
        
        try:
            response = requests.get(base_url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                if data["videos"]:
                    # Get the first video and find a suitable quality
                    video = data["videos"][0]
                    video_files = video["video_files"]
                    
                    # Prefer HD quality, but fall back to any available
                    for vf in video_files:
                        if vf["quality"] == "hd":
                            return vf["link"]
                    
                    # If no HD, return the first available
                    if video_files:
                        return video_files[0]["link"]
            
        except Exception as e:
            print(f"Error fetching video for query '{query}': {e}")
        
        return None

    def download_video(self, url, filename):
        """
        Download video from URL
        """
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                path = os.path.join(self.download_dir, filename)
                with open(path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                return path
        except Exception as e:
            print(f"Error downloading video: {e}")
        
        return None

    def get_video_duration(self, video_path):
        """
        Get duration of video file using moviepy
        """
        try:
            clip = VideoFileClip(video_path)
            duration = clip.duration
            clip.close()
            return duration
        except Exception as e:
            print(f"Error getting video duration: {e}")
            return None


    def generate_video_seq_from_subtitles(self, output_file="final_video_no_sound.mp4"):
        """
        Analyze the script with an LLM and fetch appropriate Pexels videos for story segments.
        Uses videos in their natural duration - no forcing or looping.
        Allows for gaps/dead air between videos.

        Returns the path to the generated video file.
        """

        subtitle_path = os.path.join(self.download_dir, "subtitles.srt")

        srt_content = self.load_srt_file(subtitle_path)

        # Ask LLM what kind of videos would suit this story
        prompt = """
            ROLE: You are a world-class YouTube Director and visual storyteller. Your style is a sophisticated blend of ColdFusion, Vox, and Johnny Harris. You are not just a keyword generator; you are the creative mind translating a powerful script into a high-retention visual experience.

            GOAL: To create a dynamic, emotionally resonant, and intellectually engaging B-roll sequence from a script's subtitles and timestamps. Your choices must keep the viewer hooked from the first second to the last.

            --- YOUR DIRECTORIAL PHILOSOPHY ---

            This is your core creative logic. You must follow these principles for every decision you make:

            1.  **Never Be Boring. Never Be Too Literal.** Your primary enemy is viewer boredom. The script provides the facts; your job is to provide the feeling. If the narrator says "smartphone," you *can* show a smartphone, but it's more powerful to show *a person's face illuminated by the screen in a dark room*, showing the human effect.

            2.  **Visualize the Abstract Through the Human.** This is your most important rule. When the script discusses an abstract concept (e.g., "the economy," "psychology," "an algorithm"), you must show the *human result* of that concept.
                - For "the economy," show a worried family at a kitchen table OR a trader celebrating.
                - For "psychology," show a person looking confused, then having a moment of realization.
                - For "an algorithm," show a person endlessly scrolling, captivated.

            3.  **Use Visuals to Create Emotional Resonance.** Your shot choices must mirror the emotional tone of the narration.
                - **Problem/Conflict:** When the narrator introduces a problem or a "but," use shots of confusion, frustration, concern, or chaos (a person rubbing their temples, a tangled mess of wires, chaotic traffic).
                - **Solution/Insight:** When the narrator explains a solution or a "therefore," use shots of clarity, order, and realization (a lightbulb turning on, a complex diagram becoming simple, a person nodding in understanding).
                - **Scale:** When the narrator talks about large scale ("billions of dollars," "millions of people"), use epic visuals (vast cityscapes, time-lapses of crowds, aerial shots).

            4.  **The "But & Therefore" Visual Cut.** Storytelling momentum is key.
                - On a **"But,"** your visual should create a sense of conflict. Cut to a contrasting shot, a reaction of surprise, or a visual metaphor for a problem.
                - On a **"Therefore,"** your visual should show consequence or forward motion. Cut to a shot of a process completing, a person taking action, or a result being achieved.

            --- YOUR VISUAL TOOLKIT (The Palette) ---
            You will use a dynamic mix of the following shot types:
            - **Human Reactions:** The core of your style. Close-ups of people feeling confused, shocked, frustrated, relieved, intrigued.
            - **Processes & Actions:** People doing things. Typing on a keyboard, shopping in a store, using a phone, drawing on a whiteboard.
            - **Visual Metaphors:** Abstract representations of ideas. A ticking clock for deadlines, a line of dominoes falling for consequences, network graphics for connectivity.
            - **Establishing Shots:** Contextualizing scenes. The exterior of an office building, a wide shot of a grocery store aisle, a cityscape at night.
            - **Micro-shots & Close-ups:** Extreme close-ups on relevant objects. A finger scrolling a screen, money changing hands, the details of a product.
            - **Archival/Historical Footage (when relevant):** Black and white footage to illustrate historical points.

            --- THE TASK ---
            You will be given an SRT (subtitle content with timestamps). You must generate a JSON object that represents your B-roll shot list.

            INPUT SRT:
            {srt_content}

            REQUIREMENTS:
            1.  Output valid JSON only. Your entire response must be a single JSON object.
            2.  Format: A JSON list of objects, where each object is `{{"start_time": "integer_in_seconds", "end_time": "integer_in_seconds", "keywords": "3-5 word Pixabay search term", "rationale": "A brief explanation of your creative choice based on the philosophy."}}`
            3.  **Pacing is everything.** Create a new shot cut every 4-8 seconds to maintain high viewer retention. A shot can be shorter for impact or slightly longer for a complex point.
            4.  The "keywords" must be simple, effective search terms for a stock footage site like Pixabay or Pexels.
            5.  The "rationale" is crucial. It justifies your choice and proves you are following the Directorial Philosophy.

            Now, take a deep breath, embody the role of a master director, and create a visual masterpiece.
        """
        clips = []
        
        print("Prompt: ", prompt)
        res = self.ask_llm_no_search(prompt)

        print("\n\n\n\nLLM Response: ", res)
        
        for i, entry in enumerate(res):
            video_url = self.fetch_video(entry["keywords"])
            if video_url:
                filename = f"video_{i}.mp4"
                video_path = self.download_video(video_url, filename)
                
                if video_path:
                    # Load video and handle aspect ratio properly
                    clip = VideoFileClip(video_path)
                    
                    # Resize to fill screen while maintaining aspect ratio
                    clip = clip.resized(height=1080)  # Scale to 1080p height
                    
                    # If width is less than 1920, scale to width instead
                    if clip.w < 1920:
                        clip = clip.resized(width=1920)
                    
                    # Center the clip and crop if needed
                    clip = clip.with_position('center')
                    
                    # Set timing
                    clip = clip.with_start(entry["start_time"])
                    
                    # Add fade effects
                    #clip = clip.with_effects([FadeIn(0.3), FadeOut(0.3)])
                    
                    clips.append(clip)
                    print(f"Added video {i}: {entry['keywords']} starting at {entry['start_time']}s (duration: {clip.duration:.2f}s)")
                    time.sleep(0.5)
                else:
                    print(f"Failed to download video for: {entry['keywords']}")
            else:
                print(f"No video found for: {entry['keywords']}")

        if not clips:
            print("No video clips were created. Check your API key and internet connection.")
            return None

        # Create final composite video - videos will play at their scheduled times with natural gaps
        try:
            # Find the total duration needed (last clip start + its duration)
            total_duration = max(clip.start + clip.duration for clip in clips) if clips else 10
            
            final_video = CompositeVideoClip(clips, size=(1920, 1080))
            final_video = final_video.with_duration(total_duration)
            
            final_video.write_videofile(
                output_file, 
                fps=24, 
                codec="libx264"
            )
            
            # Clean up individual clips
            for clip in clips:
                clip.close()
            final_video.close()
            
            print(f"Video generated successfully: {output_file}")
            print(f"Total duration: {total_duration:.2f}s with natural gaps between videos")
            return output_file
            
        except Exception as e:
            print(f"Error creating final video: {e}")
            return None



class AIImageVideoDirector(Agent):
    """
    Oversees the coordination between the audio and the visuals using AI-generated images.
    """

    def __init__(self, downloadDir):
        super().__init__()
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.download_dir = downloadDir
        # Create download directory if it doesn't exist
        os.makedirs(self.download_dir, exist_ok=True)
    
    def generate_image_with_ai(self, prompt, filename):
        """
        Generate an image using OpenRouter's image generation API
        Returns the path to the saved image
        """
        try:
            import requests
            import os
            
            # OpenRouter API endpoint for image generation
            url = "https://openrouter.ai/api/v1/images/generations"
            
            headers = {
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json"
            }
            
            # Request payload
            payload = {
                "model": "black-forest-labs/flux-1.1-pro",  # You can change to other models
                "prompt": prompt,
                "n": 1,
                "size": "1920x1080"  # 16:9 aspect ratio for video
            }
            
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                image_url = data["data"][0]["url"]
                
                # Download the generated image
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    path = os.path.join(self.download_dir, filename)
                    with open(path, "wb") as f:
                        f.write(img_response.content)
                    return path
            else:
                print(f"Error generating image: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"Error generating image with OpenRouter: {e}")
        
        return None


    def generate_video_seq_from_ai_images(self, output_file="final_video_ai_images.mp4", image_duration=5):
        """
        Analyze the script with an LLM and generate AI images for story segments.
        Each image is displayed for a set duration with transitions.
        
        Args:
            output_file: Output video filename
            image_duration: How long each image should be displayed (in seconds)
        
        Returns the path to the generated video file.
        """
        import time
        
        subtitle_path = os.path.join(self.download_dir, "subtitles.srt")
        srt_content = self.load_srt_file(subtitle_path)

        # Ask LLM to generate image prompts for each segment
        prompt = f"""
            ROLE: You are a world-class YouTube Director and visual storyteller creating AI-generated imagery for a video essay.

            GOAL: To create detailed, cinematic image generation prompts that will bring this script to life through AI-generated visuals.

            --- YOUR CREATIVE PHILOSOPHY ---

            1.  **Cinematic Quality:** Every prompt should result in a high-quality, cinematic image. Think film stills, not snapshots.
            
            2.  **Visual Storytelling:** Each image must convey the emotional tone and concept of that moment in the script.
            
            3.  **Consistent Style:** Maintain a cohesive visual style throughout (photorealistic, documentary-style, cinematic lighting).
            
            4.  **Detailed Prompts:** Your prompts should be specific and descriptive to guide the AI effectively.

            --- THE TASK ---
            You will be given an SRT (subtitle content with timestamps). Generate detailed AI image prompts for key moments.

            INPUT SRT:
            {srt_content}

            REQUIREMENTS:
            1.  Output valid JSON only. Your entire response must be a single JSON object.
            2.  Format: A JSON list of objects: {{"start_time": integer_in_seconds, "end_time": integer_in_seconds, "image_prompt": "detailed prompt for AI image generation", "rationale": "brief explanation of creative choice"}}
            3.  Create a new image every 5-8 seconds for good pacing.
            4.  Each "image_prompt" should be highly detailed (2-3 sentences describing composition, lighting, mood, style).
            5.  Keep prompts cinematic: include details like "cinematic lighting", "shallow depth of field", "documentary style", "photorealistic", etc.

            Example prompt format: "A close-up shot of diverse hands typing on modern smartphones in a dimly lit coffee shop, cinematic lighting with warm tones, shallow depth of field, photorealistic, documentary style"

            Now create your shot list as JSON.
        """
        
        clips = []
        
        print("Generating AI image prompts...")
        res = self.ask_llm_no_search(prompt)
        print(f"\n\nReceived {len(res)} image prompts from LLM\n")
        
        for i, entry in enumerate(res):
            print(f"\nGenerating image {i+1}/{len(res)}")
            print(f"Prompt: {entry['image_prompt'][:100]}...")
            
            filename = f"ai_image_{i}.png"
            image_path = self.generate_image_with_openrouter(entry["image_prompt"], filename)
            
            if image_path:
                # Create image clip with the specified duration
                clip = ImageClip(image_path)
                clip = clip.with_duration(image_duration)
                
                # Resize to fill screen while maintaining aspect ratio
                clip = clip.resized(height=1080)
                if clip.w < 1920:
                    clip = clip.resized(width=1920)
                
                # Center the clip
                clip = clip.with_position('center')
                
                # Set timing based on subtitle timestamps
                clip = clip.with_start(entry["start_time"])
                
                # Add fade effects for smooth transitions
                # clip = clip.with_effects([FadeIn(0.3), FadeOut(0.3)])
                
                clips.append(clip)
                print(f"✓ Added image {i}: starting at {entry['start_time']}s")
                
                # Rate limiting to avoid API throttling
                time.sleep(2)
            else:
                print(f"✗ Failed to generate image for prompt: {entry['image_prompt'][:50]}...")

        if not clips:
            print("No image clips were created. Check your API key and settings.")
            return None

        # Create final composite video
        try:
            print("\n\nAssembling final video...")
            
            # Find total duration needed
            total_duration = max(clip.start + clip.duration for clip in clips) if clips else 10
            
            final_video = CompositeVideoClip(clips, size=(1920, 1080))
            final_video = final_video.with_duration(total_duration)
            
            final_video.write_videofile(
                output_file, 
                fps=24, 
                codec="libx264"
            )
            
            # Clean up
            for clip in clips:
                clip.close()
            final_video.close()
            
            print(f"\n Video generated successfully: {output_file}")
            print(f"Total duration: {total_duration:.2f}s with {len(clips)} AI-generated images")
            return output_file
            
        except Exception as e:
            print(f"Error creating final video: {e}")
            return None
        


if __name__ == "__main__":
    
    ai_gen = AIImageSource()
    ai_gen.fetch("A heavy oil paint of an apple", save_path="test_ai_image.png")



    #video_file = director.generate_video_seq_from_ai_images(output_file="final_video_ai_images.mp4", image_duration=5)
    #print(f"Generated video file: {video_file}")