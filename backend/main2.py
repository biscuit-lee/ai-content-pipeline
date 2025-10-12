import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.agents.base_agent import Agent
from backend.generators.idea_generator_biz import IdeaGeneratorBiz
from backend.generators.idea_generator_llm import IdeaGeneratorLLM
from backend.writers.counterintuitive_writer import CounterintuitiveWriter
from backend.writers.explainer_writer import ExplainerWriter
from backend.writers.threed_writer import ThreeDWriter
from backend.production.reviewer import Reviewer
from backend.production.editor import Editor
from backend.production.video_director import VideoDirector
from backend.writers.RedditWriter import RedditWriter

import backend.prompts as prompts
from backend.pipelines.models import *
from backend.utils import *


# Load environment variables
backend_dir = Path(__file__).parent
env_file = backend_dir / '.env'
load_dotenv(env_file)

# Configuration
CSV_FILE = "youtube_story_tracking.csv"
CHANNEL_ID = os.getenv("YT_CHANNEL_ID")
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_ROUTER_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Voice IDs for TTS
VOICE_IDS = {
    "MAN1": "JBFqnCBsd6RMkjVDRZzb",
    "MAN2": "JBFqnCBsd6RMkjVDRZzb",
    "WOMAN1": "si0svtk05vPEuvwAW93c",
    "WOMAN2": "si0svtk05vPEuvwAW93c",
    "NARRATOR": "JBFqnCBsd6RMkjVDRZzb"
}

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate-story")
async def generate_story(request: StoryRequest):
    prompt = request.prompt
    story_type = request.storyType
    generated_story = ""

    print(f"Generating story for prompt: {prompt} with type: {story_type}")
    if story_type == "biz":
        # Business psychology story
        generator = IdeaGeneratorBiz(prompts.business_psych_ideas_v4)

        expand_prompt = f"""Expand this user prompt into a detailed story idea with in these format 
        {{
        "topic_title": "Why [Company/Industry/System] Does [Counterintuitive Thing]",
        "topic_category": "The '[Lens Name]' Lens (Company / Industry / System)",
        "hook_angle": "Opening line that sparks curiosity and introduces the core contradiction",
        "central_mystery": "The core question the video will answer. Why does this seemingly illogical thing exist?",
        "core_revelation": "The single, surprising sentence that solves the mystery. This is the 'Aha!' moment",
        "key_examples": ["Specific Example 1", "Specific Example 2", "Specific Example 3"],
        "historical_examples": ["Historical Example 1 with context", "Historical Example 2 with context"],
        "psychological_principles": ["Cognitive Bias 1", "Behavioral Principle 2", "Marketing Tactic 3"],
        "viral_potential_score": 9,
        "why_it_works": "Why this topic will go viral - surprising, relatable, reveals hidden patterns, and is sponsor-safe"
        }}"""
        idea = generator.ask_llm_no_search(expand_prompt)

        writer = CounterintuitiveWriter()
        generated_story = writer.generate_script_sectioned(topic_data=idea, type="business")
        
    elif story_type == "threed":
        # 3D animated story
        writer = ThreeDWriter()
        generated_story = writer.generate_script(topic=prompt, type="whatif")
        
    elif story_type == "reddit":
        # General story with LLM-driven idea generation
        generator = IdeaGeneratorLLM()
        prompt_for_llm = generator.generate_prompt_for_llm(prompt)
        genre_idea = generator.ask_llm_no_search(prompt_for_llm)
        
        print("Generated story idea:", genre_idea)
        print("prompt for LLM:", prompt_for_llm)
        writer = RedditWriter()
        generated_story = writer.generate_reddit_script(genre=genre_idea)

        print("Generated story idea:", genre_idea)
        print("Generated script:", generated_story)
    
    return generated_story


@app.post("/api/generate-audio")
async def generate_audio(request: AudioRequest):
    script = request.story
    tts_provider = request.ttsProvider

    print("Received script for audio generation:", script)
    #script_chunks = split_texts_by_paragraph(script)
    editor = Editor(VOICE_IDS)
    
    # Create unique folder for this generation
    new_topic_name = f"Generated_Audio_Topic_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    new_topic_folder = os.path.join(os.getcwd(), "backend", new_topic_name)
    os.makedirs(new_topic_folder, exist_ok=True)

    # Generate subtitles and audio
    subtitle_output_path = os.path.join(new_topic_folder, "subtitles.srt")
    script_lines = editor.analyze_script(script, subtitle_output_path=subtitle_output_path)
    audio_files = editor.generate_audio(script_lines, output_dir="output", srt_file=subtitle_output_path)

    # Merge audio files
    audio_file_name = "generated_audio.mp3"
    save_file_path = os.path.join(new_topic_folder, audio_file_name)
    merged_audio = editor.merge_audio(audio_files, final_output=save_file_path)

    print(f"✅ Audio generation complete! File saved to: {merged_audio}")
    # Upload to S3
    with open(merged_audio, "rb") as f:
        audio_content = f.read()
    
    upload_result = upload_audio_to_s3(audio_content)

    print("Audio generation and upload complete:", upload_result)


    return upload_result

@app.post("/api/regenerate-script")
async def regenerate_script(request: RegenerateRequest):
    existing_script = request.existingScript
    user_critique = request.userCritique

    prompt = "Regenerate the following script based on this critique: " + user_critique + "\n\n" + str(existing_script) + "Keep the same tone, theme and style but the requested changes. Reply with only the new text nothing before or after"

    writer = Agent()
    new_script = writer.ask_llm_no_search(prompt)


    return new_script



# Main execution (when running as script)
if __name__ == "__main__":
    # Example usage
    print(" CONTENT GENERATION PIPELINE \n")
    
        # Upload to S3
    with open("/home/grognak/personalpjk/automatedRedditStoryGen/backend/Generated_Audio_Topic_20251009_141741/generated_audio.mp3", "rb") as f:
        audio_content = f.read()
    
    upload_result = upload_audio_to_s3(audio_content)

    print("Audio generation and upload complete:", upload_result)


    # 1. Generate idea
    if_new_idea = input("Do you want to create new idea? (y/n): ")
    
    if if_new_idea.lower() == "y":
        generator = IdeaGeneratorBiz(prompts.business_psych_ideas_v4)
        idea = generator.generate_idea()
    else:
        # Use existing idea (example)
        idea = {
            "topic_title": "Why Japanese Convenience Stores Are Engineered For Maximum Efficiency",
            "core_revelation": "Japanese konbini aren't retail stores but precision-tuned data factories",
            "key_examples": ["The three-beep door chime", "Angled shelves creating forced perspective"],
            "historical_examples": ["7-Eleven's 1970s tanpin kanri implementation"],
            "psychological_principles": ["Hick's Law", "Operant Conditioning"]
        }
    
    # 2. Generate script
    if_new_script = input("Want to make new script? (y/n): ")
    
    if if_new_script.lower() == "y":
        writer_style = input("Writer style - c(counterintuitive) or i(info dense): ")
        
        if writer_style == "c":
            writer = CounterintuitiveWriter()
        else:
            writer = ExplainerWriter()
        
        script = writer.generate_script_sectioned(topic_data=idea, type="business", review=True)
        print("\nUNPOLISHED SCRIPT:\n", script)
    else:
        # Use example script
        script = {"Characters": {"NARRATOR": "MAN1"}, "story": []}
    
    # 3. Review script
    if_review = input("Want to review/polish the script? (y/n): ")
    
    if if_review.lower() == "y":
        reviewer = Reviewer()
        script = reviewer.polish_script(script)
        print("\nPOLISHED SCRIPT:\n", script)
    
    # 4. Generate audio
    editor = Editor(VOICE_IDS)
    
    new_topic_name = idea["topic_title"].strip()[:50].replace(" ", "_")
    new_topic_folder = os.path.join(os.getcwd(), new_topic_name)
    os.makedirs(new_topic_folder, exist_ok=True)
    
    subtitle_output_path = os.path.join(new_topic_folder, "subtitles.srt")
    script_lines = editor.analyze_script(script, subtitle_output_path=subtitle_output_path)
    
    audio_files = editor.generate_audio(script_lines, output_dir="output", srt_file=subtitle_output_path)
    
    audio_file_name = idea["topic_title"].strip()[:50].replace(" ", "_") + ".mp3"
    save_file_path = os.path.join(new_topic_folder, audio_file_name)
    merged_audio = editor.merge_audio(audio_files, final_output=save_file_path)
    
    # 5. Generate video
    director = VideoDirector(new_topic_folder)
    director.generate_video_seq_from_subtitles()
    
    print("\n✅ Pipeline complete!")
    print(f"📁 Output folder: {new_topic_folder}")



#  ./backend/venv/bin/python -m uvicorn backend.main2:app --reload