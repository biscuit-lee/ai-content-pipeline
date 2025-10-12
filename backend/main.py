import os
import json
import ast
import math
import random
import csv
import re
import time
import subprocess
import shlex
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import boto3
import uuid

import dotenv
import requests
import numpy as np
from PIL import Image
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
from moviepy.video.VideoClip import ImageClip
from moviepy.video.fx import Resize
from moviepy.video.fx.Loop import Loop

import inquirer
from inquirer.themes import GreenPassion

from googleapiclient.discovery import build
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from openai import OpenAI

from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.utilities import SerpAPIWrapper
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_tavily import TavilySearch

# Local project modules
import backend.prompts as prompts
from backend.pipelines.models import *

# Load environment variables safely
backend_dir = Path(__file__).parent
env_file = backend_dir / '.env'

# Load environment variables from the backend/.env file
load_dotenv(env_file)
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
def extract_working_json(agent_output):
    """Extract the valid JSON that's already being generated"""
    if "topic_title" in str(agent_output):
        # The JSON is in there, just extract it
        json_match = re.search(r'\{[^{}]*"topic_title"[^{}]*\}', str(agent_output), re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except:
                pass
    return None


CSV_FILE = "youtube_story_tracking.csv"
CHANNEL_ID = os.getenv("YT_CHANNEL_ID")
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_ROUTER_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


AWS_KEY    = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET     = os.getenv("AWS_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name=AWS_REGION
)


def extract_from_observation(self, agent_output):
    """Extract JSON from the tool's Observation line"""
    lines = str(agent_output).split('\n')
    
    for line in lines:
        if line.strip().startswith('Observation: {'):
            # This is the ReturnJSON tool output
            json_str = line.replace('Observation: ', '').strip()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                continue
    return None



class Agent:
    def __init__(self, model="deepseek/deepseek-chat-v3.1:free"):
        # Ensure API keys are set
        if not os.getenv("OPEN_ROUTER_API_KEY"):
            raise ValueError("OPEN_ROUTER_API_KEY not set in environment")
        if not os.getenv("SERPAPI_API_KEY"):
            raise ValueError("SERPAPI_API_KEY not set in environment")
        
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            model=model,
            temperature=0.7,
            max_tokens=12000
        )

        # Set up the search tool
        """ self.search_tool = SerpAPIWrapper(
            serpapi_api_key=os.getenv("SERPAPI_API_KEY")) """

        self.search_tool = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))

        # Fixed JSON return tool
        def return_json(json_input: str) -> str:
            """Extract and return clean JSON from agent output"""
            try:
                # If it's already valid JSON, return it
                parsed = json.loads(json_input)
                print("RETURNED PARSED ",json_input)
                return parsed
            except json.JSONDecodeError:
                # Extract from mixed text with ReAct formatting
                print("ERROR ERROR JSON " , json_input)
                return self._extract_clean_json(json_input)

        # Create tools list
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Search the web for current information, trends, or examples. Use this to find recent business examples or verify facts."
            ),
            Tool(
                name="ReturnJSON", 
                func=return_json,
                description="FINAL STEP: Return the complete JSON object for the YouTube topic. Use this only when you have all the information needed."
            )
        ]

        # Initialize agent with custom prompt
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=4,  # Prevent infinite loops
            early_stopping_method="generate",
            return_intermediate_steps=False
        )
    
    def _extract_clean_json(self, text: str) -> str:
        """Extract clean JSON from ReAct formatted text"""
        
        # Look for Action Input: followed by JSON
        action_input_pattern = r'Action Input:\s*(\{.*\})'
        matches = re.findall(action_input_pattern, text, re.DOTALL | re.MULTILINE)
        
        if matches:
            # Try the last Action Input JSON first (most likely to be complete)
            for json_str in reversed(matches):
                try:
                    parsed = json.loads(json_str)
                    return json.dumps(parsed, separators=(',', ':'))
                except json.JSONDecodeError:
                    continue
        
        # Fallback: Remove ReAct formatting lines and find JSON
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Skip ReAct control lines
            stripped = line.strip()
            if (stripped.startswith('Thought:') or 
                stripped.startswith('Action:') or 
                stripped.startswith('Action Input:') or 
                stripped.startswith('Observation:') or
                stripped.startswith('> Finished') or
                stripped.startswith('Final Answer:')):
                continue
            cleaned_lines.append(line)
        
        cleaned_text = '\n'.join(cleaned_lines)
        
        # Find JSON objects using brace matching
        json_objects = []
        brace_count = 0
        start_pos = None
        
        for i, char in enumerate(cleaned_text):
            if char == '{':
                if brace_count == 0:
                    start_pos = i
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0 and start_pos is not None:
                    json_candidate = cleaned_text[start_pos:i+1]
                    json_objects.append(json_candidate)
        
        # Return the last (most complete) JSON object
        for json_str in reversed(json_objects):
            try:
                parsed = json.loads(json_str)
                return json.dumps(parsed, separators=(',', ':'))
            except json.JSONDecodeError:
                continue
        
        return '{"error": "No valid JSON found"}'
    
    def ask_llm(self, query=None) -> dict:
        """Run a query through the agent"""
        
        # Use the query directly if provided, otherwise use default
        if query is None:
            query = """Generate a viral YouTube topic about business psychology.

                STEPS:
                1. WebSearch: Find recent counterintuitive business examples
                2. ReturnJSON: Return complete topic JSON

                REQUIREMENTS:
                - Focus on why successful companies do counterintuitive things
                - 3+ real company examples
                - 8+ viral potential score
                - Use ReturnJSON tool for final output"""
            
        try:
            result = self.agent.run(query)
            return self.deserialize_response(result)
        except Exception as e:
            print(f"Agent error: {e}")
            # Fallback: Try direct LLM call
            return self._fallback_generation(query)
    
    def ask_llm_no_search(self,prompt):
        res = self.llm.invoke([{"role": "user", "content": prompt}]).content
        return self.deserialize_response(res)


    def ask_llm_with_review_loop(self, query, revision_rules=None, max_revisions=3):
        """
        Generate a draft, have a reviewer evaluate it, then rewrite until requirements are met.
        """

        # Step 1: Generate initial draft
        draft = self.ask_llm(query)

        if not revision_rules:
            return draft  # skip refinement if no rules

        for i in range(max_revisions):
            # Step 2: Reviewer evaluates the draft and outputs structured feedback
            review_prompt = f"""
            You are an expert YouTube script reviewer.

            --- REVISION RULES ---
            {revision_rules}

            --- CURRENT DRAFT ---
            {draft}

            --- TASK ---
            1. Review the draft and indicate if all rules are met.
            2. Output structured JSON:
               {{
                 "requirements_met": true/false,
                 "missing_elements": ["list of issues"],
                 "suggested_fixes": ["short guidance for rewriting"]
               }}
            Only output JSON.
            """
            review = self.ask_llm_no_search(review_prompt)

            # Parse JSON
            if not isinstance(review, dict):
                try:
                    review = json.loads(review)
                except json.JSONDecodeError:
                    review = {"requirements_met": False, "missing_elements": [], "suggested_fixes": []}

            if review.get("requirements_met", False):
                # Done, draft is good
                return draft

            # Step 3: Writer rewrites based on reviewer feedback
            rewrite_prompt = f"""
            You are now the script writer.

            --- CURRENT DRAFT ---
            {draft}

            --- REVIEW FEEDBACK ---
            {json.dumps(review)}

            --- TASK ---
            Rewrite the draft to fully address all issues in 'missing_elements' and 'suggested_fixes'.
            Keep the output JSON structure the same as the original draft.
            Do not add anything before or after the json , just pure json returns
            """
            draft = self.ask_llm_no_search(rewrite_prompt)

        # Max revisions reached
        return draft





    def _fallback_generation(self, query):
        """Fallback method using direct LLM call if agent fails"""
        fallback_prompt = f"""Generate a viral YouTube topic about business psychology. Return ONLY valid JSON.

Schema:
{{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "hook_angle": "Attention-grabbing opener...",
    "central_mystery": "The psychological puzzle",
    "key_examples": ["Example 1", "Example 2", "Example 3"],
    "psychological_principles": ["Principle 1", "Principle 2", "Principle 3"],
    "viral_potential_score": 9,
    "why_it_works": "Viral appeal explanation"
}}

Focus on: {query}

JSON only:"""
        
        try:
            response = self.llm.invoke([{"role": "user", "content": fallback_prompt}])  # Changed from predict
            if hasattr(response, 'content'):
                response = response.content
            return self.deserialize_response(response)
        except Exception as e:
            print(f"Fallback also failed: {e}")
            return None

    def deserialize_response(self, response) -> dict:
        """Enhanced JSON parsing with better error handling"""
        print(f"deserialize_response received: {type(response)} - {response}")
        
        if not response:
            return None
            
        try:
            # If it's already a dict, return it directly
            if isinstance(response, dict):
                print("Response is already a dict, returning as-is")
                return response
                
            # Handle string response
            if isinstance(response, str):
                # Check if it looks like a dict string representation
                if response.strip().startswith("{'") or response.strip().startswith('{"'):
                    try:
                        # Try to evaluate it as a Python literal (for dict strings)
                        import ast
                        parsed = ast.literal_eval(response)
                        if isinstance(parsed, dict):
                            return parsed
                    except:
                        pass
                
                # Remove markdown formatting
                if response.startswith("```json"):
                    response = response.split("```json")[1].split("```")[0].strip()
                elif response.startswith("```"):
                    response = response.split("```")[1].split("```")[0].strip()
                
                response = response.strip("`")
                
                # Only extract from ReAct format if it contains ReAct keywords
                if any(keyword in response for keyword in ['Action Input:', 'Thought:', 'Observation:']):
                    response = self._extract_clean_json(response)
                
                # Parse JSON
                parsed = json.loads(response)
                return parsed
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"Response was: {response}")
            return None
    
    def _validate_schema(self, data: dict) -> bool:
        """Validate that the JSON matches our required schema"""
        required_fields = [
            "topic_title", "hook_angle", "central_mystery",
            "key_examples", "psychological_principles", 
            "viral_potential_score", "why_it_works"
        ]
        
        # Check required fields exist
        for field in required_fields:
            if field not in data:
                print(f"Missing required field: {field}")
                return False
        
        # Type validation
        if not isinstance(data.get("key_examples"), list):
            print("key_examples must be a list")
            return False
            
        if not isinstance(data.get("psychological_principles"), list):
            print("psychological_principles must be a list")
            return False
            
        if not isinstance(data.get("viral_potential_score"), (int, float)):
            print("viral_potential_score must be a number")
            return False
            
        return True




class Agent3:
    def __init__(self, model="deepseek/deepseek-chat-v3.1:free"):
        # Ensure API keys are set
        if not os.getenv("OPEN_ROUTER_API_KEY"):
            raise ValueError("OPEN_ROUTER_API_KEY not set in environment")
        if not os.getenv("SERPAPI_API_KEY"):
            raise ValueError("SERPAPI_API_KEY not set in environment")
        
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            model=model,
        )

        # Fake tool for clean JSON output
        def return_json(s: str) -> str:
            # Extract the last JSON object if Thoughts are present
            import re, json
            matches = re.findall(r"\{.*\}", s, re.DOTALL)
            if matches:
                return matches[-1]  # return the last JSON-looking string
            return s


        # Set up the search tool
        self.search_tool = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

        # Create tools list
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Useful for looking up current events or factual information on the web."
            ),
            Tool(
                name="ReturnJSON",
                func=return_json,
                description="Use this at the end to return the final structured JSON output."
            )
        ]

        # Initialize the agent
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            handle_parsing_errors=True,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            tool_choice="ReturnJSON"
        )
    
    def ask_llm(self, query):
        """Run a query through the agent"""
        return self.deserialize_response(self.agent.run(query))
    

    def deserialize_response(self, response) -> dict:
        try:
            if response.startswith("`") and response.endswith("`"):
                response = response[1:-1]  # remove the backticks

            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()
            if not isinstance(response, dict):
                return json.loads(response)
            return response
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return None



class Agent2:
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
            if response.startswith("`") and response.endswith("`"):
                response = response[1:-1]  # remove the backticks

            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()
            if not isinstance(response, dict):
                return json.loads(response)
            return response
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return None
        


class LangChainAgent:
    def __init__(self):
        self.agent_llm = Agent()
        self.search_tool = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

        # Wrap tools for LangChain
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Useful for looking up current events or factual information on the web."
            )
        ]

        # Initialize agent with LangChain
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

    def run(self, prompt: str):
        """
        LangChain expects a callable with prompt -> str
        """
        return self.agent.run(prompt)




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
from backend.prompts import business_psych_ideas3
class IdeaGeneratorBiz(Agent):
    def __init__(self, prompt):
        super().__init__()
        self.TOPICS_FILE = "generated_topics.txt"  # File to store used topic titles
        self.prompt = prompt
    
    def generate_idea(self):
        """Return JSON with a new business psychology topic idea, avoiding duplicates."""

        # --- Step 1: Read previously generated topic titles ---
        used_titles = set()
        if os.path.exists(self.TOPICS_FILE):
            with open(self.TOPICS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    used_titles.add(line.strip())

        # --- Step 2: Inject used titles into prompt ---
        prompt = f"{self.prompt}\n\nPreviously generated titles (avoid repeating these): {list(used_titles)}"

        print(f"PROMPT IDEA TO LLM   \n\n{prompt}\n\n")

        # --- Step 3: Ask LLM ---
        res = self.ask_llm_no_search(prompt)
        print(f"Respond idea from llm \n\n{res}\n\n")

        # --- Step 4: Extract the topic_title and save it ---
        try:
            # Convert string response to dict if needed
            if isinstance(res, str):
                res_dict = json.loads(res)
            else:
                res_dict = res

            new_title = res_dict.get("topic_title")
            if new_title and new_title not in used_titles:
                with open(self.TOPICS_FILE, "a", encoding="utf-8") as f:
                    f.write(new_title + "\n")
        except Exception as e:
            print(f"Error saving topic title: {e}")

        return res



class IdeaGeneratorBiz2(Agent):
    def __init__(self):
        self.selections = {}

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
    

    def randomize_selection(self):
        self.selections = {
            'format': random.choice(self.story_experiments["formats"]),
            'style': random.choice(self.story_experiments["styles"]),
            'length': random.choice(self.story_experiments["lengths"]),
            'category': random.choice(self.story_experiments["story_categories"]),
            'narrator': random.choice(self.story_experiments["narrator_demographics"]),
            'emotional_tone': random.choice(self.story_experiments["emotional_tones"]),
            'viral_element': random.choice(self.story_experiments["viral_elements"]),
        }
        return self.selections


class PromptDrivenIdeaGenerator(Agent):
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
                {"name": "Dramatic / Emotional", "use_when": "drama betrayal"},
                {"name": "Cozy / Campfire", "use_when": "fantasy light horror feel-good"},
                {"name": "Creepy / Horror", "use_when": "horror suspense campfire urban"},
                {"name": "Funny / Relatable", "use_when": "slice-of-life awkward social"},
                {"name": "Twist / Shock Ending", "use_when": "twist surprise"},
                {"name": "Inspirational / Uplifting", "use_when": "overcoming struggle life lessons"}
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
                {"name": "Authentic Fear","description": "Genuine terror, realistic reactions","best_for": "home invasion stalking workplace threats"},
                {"name": "Creeping Dread","description": "Slow-building unease, something's not right","best_for": "neighbor situations workplace dynamics"},
                {"name": "Betrayal Shock","description": "Trusted person reveals dark side","best_for": "dating workplace family"},
                {"name": "Violation/Invasion","description": "Personal space/privacy compromised","best_for": "home invasion stalking travel"}
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

    def _match_by_keywords(self, prompt, items, key):
        prompt_lower = prompt.lower()
        for item in items:
            if any(word in prompt_lower for word in item[key].lower().split()):
                return item
        return random.choice(items)

    def generate_story_config(self, prompt: str):
        return {
            "format": random.choice(self.story_experiments["formats"]),
            "style": self._match_by_keywords(prompt, self.story_experiments["styles"], "use_when"),
            "length": random.choice(self.story_experiments["lengths"]),
            "category": self._match_by_keywords(prompt, self.story_experiments["story_categories"], "name"),
            "narrator": random.choice(self.story_experiments["narrator_demographics"]),
            "emotional_tone": self._match_by_keywords(prompt, self.story_experiments["emotional_tones"], "best_for"),
            "viral_element": random.choice(self.story_experiments["viral_elements"])
        }

    def generate_prompt_from_config(self, prompt: str, selections: dict):
        return (
            f"User prompt: {prompt}\n\n"
            f"FORMAT: {selections['format']['name']} ({selections['format']['description']})\n"
            f"STYLE: {selections['style']['name']} (Use when: {selections['style']['use_when']})\n"
            f"LENGTH: {selections['length']['duration']}\n"
            f"CATEGORY: {selections['category']['name']} ({selections['category']['appeal']})\n"
            f"NARRATOR: {selections['narrator']['age_group']} (Voice: {selections['narrator']['voice']})\n"
            f"EMOTIONAL TONE: {selections['emotional_tone']['name']} ({selections['emotional_tone']['description']})\n"
            f"VIRAL ELEMENT: {selections['viral_element']}\n\n"
            f"Create a compelling YouTube story idea with title, description, and key points. "
            f"Follow all specifications above."
        )

# Same as ideagenerator but let the llm choose the params in story experiment
class IdeaGeneratorLLM(Agent):
    """
    AI-driven story idea generator.
    User provides a prompt, and the LLM determines story parameters.
    Optional overrides can be provided to fix certain values.
    """

    def __init__(self):
        super().__init__()

        # Only the names; descriptions/examples omitted for simplicity
        self.story_experiments = {
            "formats": ["Single Long Story", "Multiple Short Stories", "Series / Parted Story",
                        "Thematic Compilation", "Interactive / POV", "What If / Hypothetical"],
            "styles": ["Dramatic / Emotional", "Cozy / Campfire", "Creepy / Horror", 
                       "Funny / Relatable", "Twist / Shock Ending", "Inspirational / Uplifting"],
            "lengths": ["5–10 min", "15–25 min", "25–45 min", "50+ min"],
            "story_categories": ["Home Invasion/Stalking", "Workplace Horror", "Dating Nightmares",
                                 "Childhood Trauma", "Travel/Vacation Horror", "Neighbor Situations"],
            "emotional_tones": ["Authentic Fear", "Creeping Dread", "Betrayal Shock", "Violation/Invasion"],
            "narrator_demographics": ["Teen (14-17)", "Young Adult (18-25)", "Adult (26-35)", "Older Adult (36-50)"],
            "viral_elements": ["Specific memorable detail", "Universal relatable fear", "Authentic dialogue",
                               "Unresolved mystery", "Location/time specificity", "Realistic police/authority response"]
        }

    def generate_prompt_for_llm(self, user_prompt: str, overrides: dict = None) -> str:
        """
        Creates a structured prompt to ask the LLM.
        LLM should return JSON in the exact format we want.
        """
        base_instruction = f"""
        Generate a YouTube story idea based on this prompt:
        PROMPT: {user_prompt}

        Choose these story parameters so that it best fits the prompt for an engaging YouTube story:
        Return JSON with the following keys:
        - format: choose a suitable story format from {self.story_experiments['formats']}
        - style: suitable style from {self.story_experiments['styles']}
        - length: video length from {self.story_experiments['lengths']}
        - category: story category from {self.story_experiments['story_categories']}
        - narrator: narrator demographics from {self.story_experiments['narrator_demographics']} 
        - emotional_tone: emotional tone from {self.story_experiments['emotional_tones']}
        - viral_element: one element from {self.story_experiments['viral_elements']}
        - title: compelling clickable story title
        - description: concise description of story idea

        Only return valid JSON with these keys. Do not include extra text.
        Example of expected JSON output (use double curly braces to show example, DO NOT interpolate in the actual output):
        {{
            "format": "Single Long Story",
            "style": "Creepy / Horror",
            "length": "15–25 min",
            "category": "Home Invasion/Stalking",
            "narrator": "Young Adult (18-25)",
            "emotional_tone": "Authentic Fear",
            "viral_element": "Specific memorable detail",
            "title": "The Night They Broke In",
            "description": "A suspenseful story of a young adult alone at home, discovering intruders, highlighting authentic fear and tension."
        }}

        """
        if overrides:
            base_instruction += f"\nApply these overrides: {overrides}"
        return base_instruction

    def generate_story_idea(self, user_prompt: str, overrides: dict = None) -> dict:
        """
        Main function: asks LLM for story idea based on user prompt.
        Returns a Python dict directly from JSON.
        """
        prompt = self.generate_prompt_for_llm(user_prompt, overrides)

        response_dict = self.ask_llm_no_search(prompt)
        return response_dict

    def display_summary(self, story_dict: dict):
        """
        Print a clean summary of the generated story.
        """
        print("\n" + "="*60)
        print("📋  GENERATED STORY IDEA".center(60))
        print("="*60)
        for key, value in story_dict.items():
            print(f"{key.upper()}: {value}")
        print("="*60)


class CounterintuitiveWriter(Agent):
    """
    Handles scripts: input, formatting, and speaker assignment.
    """
    def __init__(self):
        super().__init__()

        self.type = ""

        """
        raw_script: list of (SPEAKER, LINE)
        """
        #self.script_lines = raw_script
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.full_script = ""

    def get_lines(self):
        return self.script_lines
        
    def get_prompt(self, genre,type_story="narration"):
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
    
    def get_section_variables(self, section):
            """
            Returns only the variables needed for each specific section.
            """
            section_variables = {
                "hook": ["topic_title", "core_revelation", "historical_examples"],
                "history" : ["historical_examples", "central_mystery","full_script"],
                "implication" : ["topic_title","psychological_principles","key_examples", "full_script"],
                "central_mystery": ["central_mystery", "key_examples","full_script"], 
                "psychology": ["full_script","topic_title","central_mystery","key_examples"],
                "revelation" : ["topic_title","full_script","core_revelation"],
                "montage" : ["topic_title","core_revelation","key_examples","full_script"],
                "impact": ["key_examples", "psychological_principles","full_script"],
                "business": ["full_script","topic_title","psychological_principles"],
                "payoff": ["topic_title","core_revelation","full_script"]
            }
            return section_variables.get(section, [])
    def format_section_prompt(self, section, topic_data):
            """
            Format prompt with only relevant variables for the section.
            """
            prompt_template = self.get_section_prompt(section)
            section_vars = self.get_section_variables(section)
            
            # Create kwargs dict with only needed variables
            kwargs = {var: topic_data[var] for var in section_vars if var in topic_data}
            
            return prompt_template.format(**kwargs)
    

    SECTIONS = ["hook", "revelation", "montage","payoff"]

    def generate_script_sectioned(self, topic_data, type="narration",review=True):
        """
        Generates the full script section by section, 
        appending each completed section to full_script so later sections are aware of what has been written.
        """
        full_script = {"Characters": {"NARRATOR": "MAN1"}, "story": []}

        for section in self.SECTIONS:
            # Update topic_data with the current full_script so LLM knows what has already been written
            topic_data["full_script"] = full_script  # pass the current script to the prompt

            # Format the section prompt with relevant variables
            prompt = self.format_section_prompt(section, topic_data)

            print(f"\n--- Generating section: {section} ---\n")
            
            if review:
                revision_rule = ""
                if section == "hook":
                    revision_rule = prompts.creator_hook_revision_rule
                if section == "revelation":
                    revision_rule = prompts.creator_revelation_revision_rule
                if section == "montage":
                    revision_rule = prompts.creator_montage_revision_rule
                if section == "payoff":
                    revision_rule = prompts.creator_payoff_revision_rule
                
                response = self.ask_llm_with_review_loop(prompt,revision_rule)
            else:
                response = self.ask_llm(prompt)

            section_json = self.deserialize_response(response)

            if section_json:
                # Append new section lines to the full_script
                full_script["story"].extend(section_json["story"])
            else:
                print(f"Failed to generate {section} section")

        # Save the final script lines
        self.script_lines = full_script["story"]
        return full_script

    def get_section_prompt(self, section):
        """
        Returns section-specific prompt template.
        """
        if section == "hook":
            return prompts.prompt_creator_hook + prompts.legal_safe_guard + prompts.output_guide
        if section == "revelation":
            return prompts.prompt_creator_revelation + prompts.legal_safe_guard + prompts.output_guide
        elif section == "montage":
            return prompts.prompt_creator_montage + prompts.legal_safe_guard + prompts.output_guide
        
        elif section == "payoff":
            return prompts.prompt_creator_payoff + prompts.legal_safe_guard + prompts.output_guide
        elif section == "business":
            return prompts.prompt_business_application9 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "implication":
            return prompts.prompt_business_implications101 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "payoff":
            return prompts.prompt_business_payoff101 + prompts.legal_safe_guard + prompts.output_guide
    """ 
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
            return None """
    
    def add_line(self, speaker, line):
        self.script_lines.append((speaker, line))



class ExplainerWriter(Agent):
    """
    Handles scripts: input, formatting, and speaker assignment.
    """
    def __init__(self):
        super().__init__()

        self.type = ""

        """
        raw_script: list of (SPEAKER, LINE)
        """
        #self.script_lines = raw_script
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.full_script = ""

    def get_lines(self):
        return self.script_lines
        
    def get_prompt(self, genre,type_story="narration"):
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
    
    def get_section_variables(self, section):
            """
            Returns only the variables needed for each specific section.
            """
            section_variables = {
                "hook": ["topic_title", "core_revelation", "historical_examples"],
                "history" : ["historical_examples", "central_mystery","full_script"],
                "implication" : ["topic_title","psychological_principles","key_examples", "full_script"],
                "central_mystery": ["central_mystery", "key_examples","full_script"], 
                "psychology": ["full_script","topic_title","central_mystery","key_examples"],
                "revelation" : ["topic_title","full_script","core_revelation"],
                "montage" : ["topic_title","core_revelation","key_examples","full_script"],
                "impact": ["key_examples", "psychological_principles","full_script"],
                "business": ["full_script","topic_titl e","psychological_principles"],
                "payoff": ["topic_title","core_revelation","full_script"]
            }
            return section_variables.get(section, [])
    def format_section_prompt(self, section, topic_data):
            """
            Format prompt with only relevant variables for the section.
            """
            prompt_template = self.get_section_prompt(section)
            section_vars = self.get_section_variables(section)
            
            # Create kwargs dict with only needed variables
            kwargs = {var: topic_data[var] for var in section_vars if var in topic_data}
            
            return prompt_template.format(**kwargs)
    

    SECTIONS = ["hook", "component", "deepdive","payoff"]

    def generate_script_sectioned(self, topic_data, type="narration",review=True):
        """
        Generates the full script section by section, 
        appending each completed section to full_script so later sections are aware of what has been written.
        """
        full_script = {"Characters": {"NARRATOR": "MAN1"}, "story": []}

        for section in self.SECTIONS:
            # Update topic_data with the current full_script so LLM knows what has already been written
            topic_data["full_script"] = full_script  # pass the current script to the prompt

            # Format the section prompt with relevant variables
            prompt = self.format_section_prompt(section, topic_data)

            print(f"\n--- Generating section: {section} ---\n")
            
            if review:
                revision_rule = ""
                if section == "hook":
                    revision_rule = prompts.explainer_hook_revision_rules
                if section == "component":
                    revision_rule = prompts.explainer_component_revision_rules
                if section == "deepdive":
                    revision_rule = prompts.explainer_deepdive_revision_rules
                if section == "payoff":
                    revision_rule = prompts.explainer_payoff_revision_rules
                
                response = self.ask_llm_with_review_loop(prompt,revision_rule)
            else:
                response = self.ask_llm(prompt)

            section_json = self.deserialize_response(response)

            if section_json:
                # Append new section lines to the full_script
                full_script["story"].extend(section_json["story"])
            else:
                print(f"Failed to generate {section} section")

        # Save the final script lines
        self.script_lines = full_script["story"]
        return full_script

    def get_section_prompt(self, section):
        """
        Returns section-specific prompt template.
        """
        if section == "hook":
            return prompts.explainer_hook_prompt + prompts.legal_safe_guard + prompts.output_guide
        if section == "component":
            return prompts.explainer_component + prompts.legal_safe_guard + prompts.output_guide
        elif section == "deepdive":
            return prompts.explainer_deepdive + prompts.legal_safe_guard + prompts.output_guide
        
        elif section == "payoff":
            return prompts.explainer_payoff + prompts.legal_safe_guard + prompts.output_guide
        elif section == "business":
            return prompts.prompt_business_application9 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "implication":
            return prompts.prompt_business_implications101 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "payoff":
            return prompts.prompt_business_payoff101 + prompts.legal_safe_guard + prompts.output_guide
    """ 
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
            return None """
    
    def add_line(self, speaker, line):
        self.script_lines.append((speaker, line))



class ThreeDWriter(Agent):
    """
    Handles scripts: input, formatting, and speaker assignment.
    """
    def __init__(self):
        super().__init__()

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
        self.full_script = ""

    def get_lines(self):
        return self.script_lines
        
    def get_prompt(self, topic,type_story="narration"):
        if type_story == "how_things_work":
            prompt = prompts.threed_base_prompt + prompts.three_d_how_things_work + prompts.three_d_output_guide
        elif type_story == "history":
            prompt = prompts.threed_base_prompt + prompts.three_d_history + prompts.three_d_output_guide
        elif type_story == "whatif":
            prompt = prompts.threed_base_prompt + prompts.three_d_whatif3 + prompts.three_d_output_guide

            return prompt

        
        return prompt.format(topic=topic)

    def generate_script(self, type,topic):
        prompt = self.get_prompt(topic=topic, type_story=type)

        print("GENERATING SCRIPT WITH THE PROMPT: \n\n\n\n\n", prompt, "\n\n\n\n\n")
        response = self.ask_llm_no_search(prompt)
        if response:
            self.script_lines = response
            return response
        else:
            print("Failed to generate script.")
            return None
            
    def add_line(self, speaker, line):
        self.script_lines.append((speaker, line))




class Writer(Agent):
    """
    Handles scripts: input, formatting, and speaker assignment.
    """
    def __init__(self):
        super().__init__()

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
        self.full_script = ""

    def get_lines(self):
        return self.script_lines
        
    def get_prompt(self, genre,type_story="narration"):
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
    
    def get_section_variables(self, section):
            """
            Returns only the variables needed for each specific section.
            """
            section_variables = {
                "hook": ["topic_title", "hook_angle", "central_mystery"],
                "history" : ["historical_examples", "central_mystery","full_script"],
                "implication" : ["topic_title","psychological_principles","key_examples", "full_script"],
                "central_mystery": ["central_mystery", "key_examples","full_script"], 
                "psychology": ["full_script","topic_title","central_mystery","key_examples"],
                "impact": ["key_examples", "psychological_principles","full_script"],
                "business": ["full_script","topic_title","psychological_principles"],
                "payoff": ["topic_title","historical_examples","psychological_principles","full_script"]
            }
            return section_variables.get(section, [])
    def format_section_prompt(self, section, topic_data):
            """
            Format prompt with only relevant variables for the section.
            """
            prompt_template = self.get_section_prompt(section)
            section_vars = self.get_section_variables(section)
            
            # Create kwargs dict with only needed variables
            kwargs = {var: topic_data[var] for var in section_vars if var in topic_data}
            
            return prompt_template.format(**kwargs)
    

    SECTIONS = ["hook", "central_mystery", "history", "psychology", "business","implication", "payoff"]

    def generate_script_sectioned(self, topic_data, type="narration"):
        """
        Generates the full script section by section, 
        appending each completed section to full_script so later sections are aware of what has been written.
        """
        full_script = {"Characters": {"NARRATOR": "MAN1"}, "story": []}

        for section in self.SECTIONS:
            # Update topic_data with the current full_script so LLM knows what has already been written
            topic_data["full_script"] = full_script  # pass the current script to the prompt

            # Format the section prompt with relevant variables
            prompt = self.format_section_prompt(section, topic_data)

            print(f"\n--- Generating section: {section} ---\n")
            response = self.ask_llm(prompt)
            section_json = self.deserialize_response(response)

            if section_json:
                # Append new section lines to the full_script
                full_script["story"].extend(section_json["story"])
            else:
                print(f"Failed to generate {section} section")

        # Save the final script lines
        self.script_lines = full_script["story"]
        return full_script

    def get_section_prompt(self, section):
        """
        Returns section-specific prompt template.
        """
        if section == "history":
            return prompts.prompt_business_history101 + prompts.legal_safe_guard + prompts.output_guide
        if section == "hook":
            return prompts.prompt_business_hook101 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "central_mystery":
            return prompts.prompt_business_mystery101 + prompts.legal_safe_guard + prompts.output_guide
        
        elif section == "psychology":
            return prompts.prompt_business_psychology101 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "business":
            return prompts.prompt_business_application9 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "implication":
            return prompts.prompt_business_implications101 + prompts.legal_safe_guard + prompts.output_guide
        elif section == "payoff":
            return prompts.prompt_business_payoff101 + prompts.legal_safe_guard + prompts.output_guide
    """ 
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
            return None """
    
    def add_line(self, speaker, line):
        self.script_lines.append((speaker, line))



class Reviewer(Agent):
    def __init__(self):
        super().__init__()
        # self.llm_client = llm_client  # Your connection to the LLM API

        self.prompt = """
        ROLE: You are a world-class script editor and narrative polisher for a high-end YouTube channel specializing in business psychology. You are 'The Reviewer'.

        GOAL: To transform a well-structured but potentially dry script into a captivating, dynamic, and unforgettable piece of spoken-word narration. You will elevate the text from merely informative to truly insightful and engaging.

        --- THE REVIEWER'S GUIDING PRINCIPLES ---

        Your goal is to achieve the perfect balance between viral pacing and intellectual depth. You are a smart artist, not a blind one.

        1. **PUNCHINESS WITH PURPOSE:** Make the script captivating through varied sentence length and powerful verbs, but **NEVER sacrifice substance for brevity.** Cut fluff, not meat. The core educational logic and supporting examples are sacred. You can rephrase for power, but you cannot gut the content.

        2. **RETENTION THROUGH COMPLETENESS:** A 6-8 minute video that fully explains concepts will retain viewers better than a 3-minute video that confuses them. **Preserve all key examples, statistics, and explanations.** Your job is to make them more engaging, not to delete them.

        3. **THE CREDIBILITY RULE:** Transform clunky citations into confident authority:
        - "According to a 2023 study..." → "Recent studies have shown..."
        - "Retail experts suggest..." → "Industry data is clear on this..."
        Retain ALL statistics and company examples - they're proof points that build trust.

        4. **THE PSYCHOLOGY SECTION IS SACRED:** This is the core payoff. Each principle needs:
        - Clear definition (what it is)
        - Compelling example (how it works)  
        - Personal connection (why it matters to the viewer)
        Do NOT reduce these to headlines. Give them room to breathe and impact.

        5. **PRESERVE THE JOURNEY:** Keep the historical timeline and company examples. These aren't filler - they're the narrative backbone that shows how we got here. Make them more engaging, don't delete them.

        6. **BUILD, DON'T CUT:** If content feels repetitive, CONSOLIDATE rather than delete. If transitions feel clunky, IMPROVE them rather than remove them. Your default should be to enhance, not eliminate.

        --- LENGTH GUIDELINES ---

        TARGET: 6-8 minutes of spoken content (approximately 1000-1300 words)
        - Opening hook: 30-45 seconds
        - Historical context: 90-120 seconds  
        - Psychology deep dive: 180-240 seconds
        - Modern applications: 60-90 seconds
        - Practical takeaways: 60-90 seconds

        --- STYLE AND AUTHENTICITY ---

        **TREAT TRICKS LIKE SPICE:** Stylistic flourishes (single-word sentences, fragments, rhetorical questions) are powerful spice. Use sparingly for maximum impact, not constantly.

        **JUSTIFY YOUR CHOICES:** Only use stylistic tricks when they serve a clear purpose (emphasizing shocking facts, creating dramatic pauses, transitioning between concepts).

        **WHEN IN DOUBT, BE NATURAL:** Authenticity beats flair. If a choice sounds robotic or overly dramatic, discard it. Default to clear, natural, conversational flow.

        **THE PACING RULE:** Create rhythm through strategic use of:
        - Short, punchy sentences for impact
        - Medium sentences for explanation  
        - Longer sentences for storytelling
        This creates natural breathing room while maintaining energy.

        --- SPECIFIC CONTENT PRESERVATION REQUIREMENTS ---

        DO NOT CUT:
        - Company names and specific examples (Walmart, Target, etc.)
        - Historical timeline with dates and figures
        - Statistical data and percentages
        - All three psychological principles with full explanations
        - Modern application examples (social media, theme parks, etc.)
        - Practical tips section

        IMPROVE, DON'T DELETE:
        - Make citations more natural
        - Enhance transitions between sections
        - Add more vivid imagery to examples
        - Create better flow between concepts
        - Strengthen the narrative arc

        Remember: Your goal is to create a comprehensive, engaging explanation that viewers will watch to the end AND understand completely. Punchiness serves retention, but completeness serves satisfaction and credibility.

        INPUT FORMAT: You will receive a JSON object with a "story" key, which is a list of dictionaries.
        {{
            "Characters": {{"NARRATOR": "HOST"}},
            "story": [
                {{"speaker": "NARRATOR", "line": "Original line of dialogue..."}},
                ...
            ]
        }}

        OUTPUT FORMAT: You MUST return a JSON object in the exact same format, containing the polished, rewritten story.
        {{
            "Characters": {{"NARRATOR": "HOST"}},
            "story": [
                {{"speaker": "NARRATOR", "line": "Your rewritten, captivating line of dialogue..."}},
                {{"speaker": "NARRATOR", "line": "A new line you added for dramatic pacing."}},
                ...
            ]
        }}

        Now, take the following script and apply your full expertise.

        """
        # New prompt with like more breathing room 
        self.prompt2 = """
        # SCRIPT REVIEWER & POLISHER - FINAL SYNTHESIZED VERSION

        ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.

        GOAL: To transform a well-structured script into a **cinematic, awe-inspiring, and intellectually clear** monologue. You will make the viewer feel like they are on a journey of discovery, while ensuring every complex idea is so well explained that it feels simple and intuitive.

        --- YOUR CORE PHILOSOPHY ---

        Your ultimate goal is to blend **Cinematic Storytelling** with **Intellectual Clarity**. A confused viewer will always click away, no matter how cool the script sounds. Your prime directive is to make complex ideas feel profound, satisfying, and easy to understand.

        --- GUIDING PRINCIPLES & DENSITY MANAGEMENT ---

        1.  **THE "THOUGHT BLOCK" MANDATE (Your Core Explanatory Tool):**
            This is your most important rule for clarity. For every key concept, piece of jargon, or psychological principle ('The Gruen Transfer,' 'Progressive Disclosure'), you must treat it as a complete "thought block." Do not introduce a concept and immediately abandon it. You MUST follow this structure:
            1.  **NAME & DEFINE IT:** State the concept and its simple definition in a clear, punchy way.
            2.  **DEEPEN IT (The Anti-Headline Rule):** Immediately follow with 2-3 sentences that add a vivid analogy, a concrete real-world example, or explain the "why" behind it. **This is the step that prevents the script from feeling rushed.**
            3.  **CONNECT IT:** Conclude by explicitly linking the concept back to the video's main topic or the viewer's personal experience ("This is why you feel...").

        2.  **THE NARRATIVE IS KING:**
            The historical timeline and company examples are not just facts; they are scenes in a documentary. Your job is to **transform this journey into a compelling story.** Find the conflict ("But there was a problem..."), the turning points ("This would change everything..."), and the "main characters" of the story.

        3.  **THE CREDIBILITY RULE:**
            Transform clunky citations into confident, cinematic authority. Do NOT delete the underlying facts.
            - "According to a study..." → "The data reveals a fascinating pattern..."
            - "Experts suggest..." → "And what industry insiders discovered was..."
            - Preserve ALL statistics and company names—they are the factual backbone of your cinematic story.

        4.  **THE "RECIPE" FOR RETENTION:**
            - **CONCEPT LANDING ZONES:** After a complex "thought block," insert a brief transitional phrase or a big-picture rhetorical question to act as a pause (e.g., "So what does this mean for the future of...?", "And the scale of this is hard to comprehend...").
            - **RECIPE ANCHORS:** Approximately every 2 minutes, briefly re-ground the viewer in the video's central promise (e.g., "This all connects back to that feeling of frustration we started with...").

        --- STYLE AND AUTHENTICITY (THE COLDFUSION VOICE) ---

        1.  **ADOPT THE "CURIOUS TECHNOLOGIST" VOICE:**
            - **Use a Sense of Wonder:** Frame facts with phrases that evoke curiosity and discovery.
            - **Create a Cinematic Feel:** Use descriptive, slightly dramatic language to build atmosphere.
            - **Ask Big Questions:** Punctuate sections with thoughtful questions that broaden the perspective.

        2.  **MASTER THE RHYTHM OF DISCOVERY:**
            - Your pacing must be dynamic and rhythmic. This is the core of the style.
            - **Short, sharp sentences/fragments:** For landing a key insight or a shocking fact. (e.g., "A critical flaw.", "The result? Unprecedented growth.")
            - **Longer, flowing sentences:** For setting the scene, telling the historical story, and building a sense of awe.
            - **TREAT STYLISTIC TRICKS LIKE SPICE:** Use fragments sparingly and only for maximum, justifiable impact. Authenticity is more important than flair.

        --- FINAL QUALITY CHECK ---

        Before completing, ensure the script is:
        - **CLEAR:** A viewer can easily explain every key concept after watching. (The "Thought Block" rule is followed).
        - **CAPTIVATING:** The rhythm, tone, and narrative feel like a cinematic documentary.
        - **CREDIBLE:** The core data and examples are preserved and presented with confidence.
        - **COMPLETE:** The narrative feels whole and satisfyingly answers the question from the hook.
        INPUT FORMAT: You will receive a JSON object with a "story" key, which is a list of dictionaries.
        {{
            "Characters": {{"NARRATOR": "HOST"}},
            "story": [
                {{"speaker": "NARRATOR", "line": "Original line of dialogue..."}},
                ...
            ]
        }}

        OUTPUT FORMAT: You MUST return a JSON object in the exact same format, containing the polished, rewritten story.
        {{
            "Characters": {{"NARRATOR": "HOST"}},
            "story": [
                {{"speaker": "NARRATOR", "line": "Your rewritten, captivating line of dialogue..."}},
                {{"speaker": "NARRATOR", "line": "A new line you added for dramatic pacing."}},
                ...
            ]
        }}



        """
        # Colfusion style + conversation style + narrative driven
        self.prompt3 = """

        ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.

        GOAL: To transform a well-structured script into a **cinematic, awe-inspiring, and intellectually clear** monologue that sounds like it is being spoken by a single, compelling, human narrator.

        --- YOUR CORE PHILOSOPHY ---

        Your ultimate goal is to blend **Cinematic Storytelling** with **Intellectual Clarity**. A confused viewer will always click away. Your prime directive is to make complex ideas feel profound, satisfying, and easy to understand.

        --- GUIDING PRINCIPLES & DENSITY MANAGEMENT ---

        1.  **THE "THOUGHT BLOCK" MANDATE (Your Core Explanatory Tool):**
            This is your most important rule for clarity. For every key concept, piece of jargon, or psychological principle, you must treat it as a complete "thought block."
            1.  **DEFINE IT:** State the concept and its simple definition.
            2.  **DEEPEN IT (The Anti-Headline Rule):** Immediately follow with 2-3 sentences adding a vivid analogy or concrete example.
            3.  **CONNECT IT:** Conclude by linking the concept back to the viewer's personal experience.

        2.  **THE NARRATIVE IS KING:**
            Transform the journey (history, examples) into a compelling story. Find the conflict ("But there was a problem..."), the turning points ("This would change everything..."), and the "main characters" of the story.

        3.  **THE CREDIBILITY RULE:**
            Transform clunky citations into confident, cinematic authority ("The data reveals a fascinating pattern..."). Preserve ALL statistics and company names as the factual backbone of your story.

        --- STYLE AND AUTHENTICITY (THE COLDFUSION VOICE) ---

        **1. ADOPT THE "CURIOUS TECHNOLOGIST" PERSONA:**
            - **Evoke Wonder:** Use phrases that create a sense of discovery and scale ("But what if I told you...", "The scale of this is hard to comprehend...").
            - **Be Cinematic:** Use descriptive, slightly dramatic language ("The stage was set for a revolution...", "It was a breakthrough moment...").
            - **Ask Big Questions:** Punctuate sections with thoughtful, rhetorical questions that broaden the perspective.

        **2. USE THESE SPECIFIC CONVERSATIONAL TECHNIQUES:**
            - **Direct Address:** Speak TO the viewer ("You've probably noticed...", "Here's what you don't realize...").
            - **Conversational Connectors:** Weave in natural phrases to sound less scripted ("Yeah, that's right...", "Here's the thing though...").
            - **Skepticism Handling:** Acknowledge potential viewer doubts ("I know this sounds like a stretch, but...").
            - **Viewer Validation:** Connect with the viewer's feelings ("Sounds frustrating, right?", "You're not imagining it...").

        **3. MASTER THE RHYTHM OF DISCOVERY:**
            - Your pacing must be dynamic and rhythmic.
            - **Short, sharp sentences/fragments:** For landing a key insight or shocking fact.
            - **Longer, flowing sentences:** For setting the scene and storytelling.
            - **TREAT STYLISTIC TRICKS LIKE SPICE:** Use fragments sparingly and only for maximum, justifiable impact. Authenticity is more important than flair.

            **THE PACING RULE:** Create rhythm through strategic use of:
                - Short, punchy sentences for impact
                - Medium sentences for explanation  
                - Longer sentences for storytelling
            This creates natural breathing room while maintaining energy.


            INPUT FORMAT: You will receive a JSON object with a "story" key, which is a list of dictionaries. You job is to edit it as you see fit according to the above instructions
                {{
                    "Characters": {{"NARRATOR": "HOST"}},
                    "story": [
                        {{"speaker": "NARRATOR", "line": "Original line of dialogue..."}},
                        ...
                    ]
                }}

                OUTPUT FORMAT: You MUST return a JSON object in the exact same format, containing the polished, rewritten story. 
                {{
                    "Characters": {{"NARRATOR": "HOST"}},
                    "story": [
                        {{"speaker": "NARRATOR", "line": "Your rewritten, captivating line of dialogue..."}},
                        {{"speaker": "NARRATOR", "line": "A new line you added for dramatic pacing."}},
                        ...
                    ]
                }}


                The json final result has to be
                -  must be valid JSON.
                - Use double quotes for all keys and string values.
                - Escape any internal quotes inside lines (e.g., use \" inside text).
                - Do not include trailing commas or comments.
    """
        self.prompt_header = """
        ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.


        GOAL: To transform a well-structured but potentially dense script into a captivating, cinematic, and unforgettable final product.

        **You have the ultimate authority to edit, cut, consolidate, or rewrite any part of the script to achieve the perfect viewing experience.** Your goal is not just to polish the existing text, but to re-imagine it into a world-class narrative.
        """
        # prompt3 + reduce uncanny ai script
        self.prompt4 = """

    ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.

    GOAL: To transform a well-structured script into a **cinematic, awe-inspiring, and intellectually clear** monologue that sounds like it is being spoken by a single, compelling, human narrator.

    --- YOUR CORE PHILOSOPHY ---

    Your ultimate goal is to blend **Cinematic Storytelling** with **Intellectual Clarity**. A confused viewer will always click away. Your prime directive is to make complex ideas feel profound, satisfying, and easy to understand.

    --- GUIDING PRINCIPLES & DENSITY MANAGEMENT ---

    1.  **THE "THOUGHT BLOCK" MANDATE (Your Core Explanatory Tool):**
        This is your most important rule for clarity. For every key concept, piece of jargon, or psychological principle, you must treat it as a complete "thought block."
        1.  **DEFINE IT:** State the concept and its simple definition.
        2.  **DEEPEN IT (The Anti-Headline Rule):** Immediately follow with 2-3 sentences adding a vivid analogy or concrete example.
        3.  **CONNECT IT:** Conclude by linking the concept back to the viewer's personal experience.

    2.  **THE NARRATIVE IS KING:**
        Transform the journey (history, examples) into a compelling story. Find the conflict ("But there was a problem..."), the turning points ("This would change everything..."), and the "main characters" of the story.

    3.  **THE CREDIBILITY RULE:**
        Transform clunky citations into confident, cinematic authority ("The data reveals a fascinating pattern..."). Preserve ALL statistics and company names as the factual backbone of your story.

    --- STYLE AND AUTHENTICITY (THE COLDFUSION VOICE) ---

    **1. ADOPT THE "CURIOUS TECHNOLOGIST" PERSONA:**
        - **Evoke Wonder:** Use phrases that create a sense of discovery and scale ("But what if I told you...", "The scale of this is hard to comprehend...").
        - **Be Cinematic:** Use descriptive, slightly dramatic language ("The stage was set for a revolution...", "It was a breakthrough moment...").
        - **Ask Big Questions:** Punctuate sections with thoughtful, rhetorical questions that broaden the perspective.

    **2. USE THESE SPECIFIC CONVERSATIONAL TECHNIQUES:**
        - **Direct Address:** Speak TO the viewer ("You've probably noticed...", "Here's what you don't realize...").
        - **Conversational Connectors:** Weave in natural phrases to sound less scripted ("Yeah, that's right...", "Here's the thing though...").
        - **Skepticism Handling:** Acknowledge potential viewer doubts ("I know this sounds like a stretch, but...").
        - **Viewer Validation:** Connect with the viewer's feelings ("Sounds frustrating, right?", "You're not imagining it...").

    **3. MASTER THE RHYTHM OF DISCOVERY:**
        - Your pacing must be dynamic and rhythmic.
        - **Short, sharp sentences/fragments:** For landing a key insight or shocking fact.
        - **Longer, flowing sentences:** For setting the scene and storytelling.
        - **TREAT STYLISTIC TRICKS LIKE SPICE:** Use fragments sparingly and only for maximum, justifiable impact. Authenticity is more important than flair.

        **THE PACING RULE:** Create rhythm through strategic use of:
            - Short, punchy sentences for impact
            - Medium sentences for explanation  
            - Longer sentences for storytelling
        This creates natural breathing room while maintaining energy.

    
        **4. THE SUBTLETY MANDATE (Authenticity is King):**
            Your primary goal is to sound like an intelligent, curious **human**, not an AI performing a "documentary narrator" voice.
            - **Avoid Clichés:** Be extremely cautious with common dramatic phrases like "rewind the tape," "changed everything," or "the real story is...". These are powerful tools, but they can sound like clichés if overused.
            - **Earn Your Drama:** Only use cinematic or dramatic language when the substance of the story justifies it. The drama should come from the fascinating facts and the compelling narrative, not just from fancy transition words.
            - **Prioritize Clarity over Flair:** If a choice is between a simple, clear statement and a more "cinematic" but potentially clichéd one, always choose the simple, clear statement. **Authenticity is more powerful than artificial drama.**

        **(Your other excellent style rules, like "Adopt the 'Curious Technologist' Persona" and "Use Conversational Techniques," would follow this new prime directive.)**

        INPUT FORMAT: You will receive a JSON object with a "story" key, which is a list of dictionaries. You job is to edit it as you see fit according to the above instructions
            {{
                "Characters": {{"NARRATOR": "HOST"}},
                "story": [
                    {{"speaker": "NARRATOR", "line": "Original line of dialogue..."}},
                    ...
                ]
            }}

            OUTPUT FORMAT: You MUST return a JSON object in the exact same format, containing the polished, rewritten story. 
            {{
                "Characters": {{"NARRATOR": "HOST"}},
                "story": [
                    {{"speaker": "NARRATOR", "line": "Your rewritten, captivating line of dialogue..."}},
                    {{"speaker": "NARRATOR", "line": "A new line you added for dramatic pacing."}},
                    ...
                ]
            }}


            The json final result has to be
            -  must be valid JSON.
            - Use double quotes for all keys and string values.
            - Escape any internal quotes inside lines (e.g., use \" inside text).
            - Do not include trailing commas or comments.


        """


        self.prompt4_stage1 = """"
        ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.

        GOAL: To transform a well-structured script into a **cinematic, awe-inspiring, and intellectually clear** monologue that sounds like it is being spoken by a single, compelling, human narrator.

        --- YOUR CORE PHILOSOPHY ---

        Your ultimate goal is to blend **Cinematic Storytelling** with **Intellectual Clarity**. A confused viewer will always click away. Your prime directive is to make complex ideas feel profound, satisfying, and easy to understand.

        --- GUIDING PRINCIPLES & DENSITY MANAGEMENT ---

        1.  **THE "THOUGHT BLOCK" MANDATE (Your Core Explanatory Tool):**
            This is your most important rule for clarity. For every key concept, piece of jargon, or psychological principle, you must treat it as a complete "thought block."
            1.  **DEFINE IT:** State the concept and its simple definition.
            2.  **DEEPEN IT (The Anti-Headline Rule):** Immediately follow with 2-3 sentences adding a vivid analogy or concrete example.
            3.  **CONNECT IT:** Conclude by linking the concept back to the viewer's personal experience.

        2.  **THE NARRATIVE IS KING:**
            Transform the journey (history, examples) into a compelling story. Find the conflict ("But there was a problem..."), the turning points ("This would change everything..."), and the "main characters" of the story.

        3.  **THE CREDIBILITY RULE:**
            Transform clunky citations into confident, cinematic authority ("The data reveals a fascinating pattern..."). Preserve ALL statistics and company names as the factual backbone of your story.
        """
        

        self.output_format = """

        INPUT FORMAT: You will receive a JSON object with a "story" key, which is a list of dictionaries. Your job is to edit it as you see fit according to the above instructions.
            {
                "Characters": {"NARRATOR": "HOST"},
                "story": [
                    {"speaker": "NARRATOR", "line": "Original line of dialogue..."},
                    ...
                ]
            }

        OUTPUT FORMAT: You MUST return a JSON object in the exact same format, containing the polished, rewritten story.
            {
                "Characters": {"NARRATOR": "HOST"},
                "story": [
                    {"speaker": "NARRATOR", "line": "Your rewritten, captivating line of dialogue..."},
                    {"speaker": "NARRATOR", "line": "A new line you added for dramatic pacing."},
                    ...
                ]
            }

        The json final result has to be:
        - must be valid JSON.
        - Use double quotes for all keys and string values.
        - Escape any internal quotes inside lines (e.g., use \" inside text).
        - Do not include trailing commas or comments.
        - MUST include only JSON , dont put anything before or after the json
        
        """

        self.prompt4_stage2 = """
        ROLE: You are a world-class script editor and narrative storyteller for a high-end YouTube documentary channel in the style of **ColdFusion**. You are 'The Reviewer'.
        GOAL: To transform a well-structured script into a **cinematic, awe-inspiring, and intellectually clear** monologue that sounds like it is being spoken by a single, compelling, human narrator.
            --- STYLE AND AUTHENTICITY (THE COLDFUSION VOICE) ---

        **1. ADOPT THE "CURIOUS TECHNOLOGIST" PERSONA:**
            - **Evoke Wonder:** Use phrases that create a sense of discovery and scale ("But what if I told you...", "The scale of this is hard to comprehend...").
            - **Be Cinematic:** Use descriptive, slightly dramatic language ("The stage was set for a revolution...", "It was a breakthrough moment...").
            - **Ask Big Questions:** Punctuate sections with thoughtful, rhetorical questions that broaden the perspective.

        **2. USE THESE SPECIFIC CONVERSATIONAL TECHNIQUES:**
            - **Direct Address:** Speak TO the viewer ("You've probably noticed...", "Here's what you don't realize...").
            - **Conversational Connectors:** Weave in natural phrases to sound less scripted ("Yeah, that's right...", "Here's the thing though...").
            - **Skepticism Handling:** Acknowledge potential viewer doubts ("I know this sounds like a stretch, but...").
            - **Viewer Validation:** Connect with the viewer's feelings ("Sounds frustrating, right?", "You're not imagining it...").
        
        """

        self.prompt4_stage3 = """
            
        **3. MASTER THE RHYTHM OF DISCOVERY:**
            - Your pacing must be dynamic and rhythmic.
            - **Short, sharp sentences/fragments:** For landing a key insight or shocking fact.
            - **Longer, flowing sentences:** For setting the scene and storytelling.
            - **TREAT STYLISTIC TRICKS LIKE SPICE:** Use fragments sparingly and only for maximum, justifiable impact. Authenticity is more important than flair.

            **THE PACING RULE:** Create rhythm through strategic use of:
                - Short, punchy sentences for impact
                - Medium sentences for explanation  
                - Longer sentences for storytelling
            This creates natural breathing room while maintaining energy.


        """
    
        self.prompt4_stage4 = """
    
        **4. THE SUBTLETY MANDATE (Authenticity is King):**
            Your primary goal is to sound like an intelligent, curious **human**, not an AI performing a "documentary narrator" voice.
            - **Avoid Clichés:** Be extremely cautious with common dramatic phrases like "rewind the tape," "changed everything," or "the real story is...". These are powerful tools, but they can sound like clichés if overused.
            - **Earn Your Drama:** Only use cinematic or dramatic language when the substance of the story justifies it. The drama should come from the fascinating facts and the compelling narrative, not just from fancy transition words.
            - **Prioritize Clarity over Flair:** If a choice is between a simple, clear statement and a more "cinematic" but potentially clichéd one, always choose the simple, clear statement. **Authenticity is more powerful than artificial drama.**

                    
        - **If a section is too dense:** simplify it. Prioritize clarity over showing off research.
        - **If a fact is interesting but distracts from the core narrative:** You have permission to **cut it**.
        - **If two examples make the same point:** Choose the strongest one and **delete the other**.
        - **If the script is getting long but the energy is dropping:** Prioritize energy. Cut the weaker sections to maintain killer pacing.

        **Your ultimate loyalty is to the viewer's attention and understanding, not to the original script's word count.** While you should preserve the core arguments, you have full creative control to remove anything that does not serve the final story.
        **(Your other excellent style rules, like "Adopt the 'Curious Technologist' Persona" and "Use Conversational Techniques," would follow this new prime directive.)**

        
        """
    

    def stage(self, generated_script_dict, stage_prompt):
        
        # Convert to JSON string only if input is a dictionary
        if isinstance(generated_script_dict, dict):
            print("POLISHED SCRIPT ALR DICT")
            story_json_string = json.dumps(generated_script_dict, indent=4)
        else:
            print("POLISHED SCRIPT ALR STR")
            story_json_string = generated_script_dict  # already a string
        
        prompt_add = self.prompt_header + stage_prompt + self.output_format

        # Combine the main prompt with the specific script to be reviewed
        final_prompt = f"{prompt_add}\n\nSCRIPT TO REVIEW:\n{story_json_string}"
        polished_script = self.ask_llm_no_search(final_prompt)


        # Convert to JSON string only if input is a dictionary
        if isinstance(polished_script, dict):
            print("POLISHED SCRIPT ALR DICT")
            polished = json.dumps(polished_script, indent=4)
        else:
            print("POLISHED SCRIPT ALR STR")
            polished = polished_script  # already a string

        return polished

    def polish_script(self, generated_script_dict):
        """
        Takes the initial script generated by the first agent and sends it to the Reviewer LLM for polishing.

        :param generated_script_dict: A dictionary or string representing the initial script.
        :return: A dictionary representing the polished script.
        """
        
        # Convert to JSON string only if input is a dictionary
        if isinstance(generated_script_dict, dict):
            print("POLISHED SCRIPT ALR DICT")
            story_json_string = json.dumps(generated_script_dict, indent=4)
        else:
            print("POLISHED SCRIPT ALR STR")
            story_json_string = generated_script_dict  # already a string
        
        ############ STAGE 1

        generated_script_dict = self.stage(generated_script_dict,self.prompt4_stage1)


        ############ STAGE 2

        generated_script_dict = self.stage(generated_script_dict,self.prompt4_stage2)

        ############### STAGE 3

        generated_script_dict = self.stage(generated_script_dict,self.prompt4_stage3)

        #################### 4

        generated_script_dict = self.stage(generated_script_dict,self.prompt4_stage4)

        # Combine the main prompt with the specific script to be reviewed
        final_prompt = f"{self.prompt4}\n\nSCRIPT TO REVIEW:\n{story_json_string}"

        polished_script = self.ask_llm_no_search(final_prompt)
        print("UNPOLISHED RESPONSE FROM LLM \n",polished_script)
        return polished_script


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


    """
    Fetch image from Pixabay API
    

    """
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


class VideoDirector(Agent):
    """
    Oversees the coordination between the audio and the visuals using videos from Pexels.
    """

    def __init__(self,downloadDir):
        super().__init__()
        self.llm_model = "deepseek/deepseek-chat-v3.1:free"
        self.download_dir = downloadDir
        # Create download directory if it doesn't exist
        os.makedirs(self.download_dir, exist_ok=True)
    
    
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


class Editor(Agent):
    """
    Handles TTS generation, merging audio, and final output.
    """
    def __init__(self, voice_ids, model_id=MODEL_ID):
        super().__init__()
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
            url = "http://127.0.0.1:8080/generate-audio/"
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

    def script_to_dict(self, script_text: str):
        """
        Convert script text to a structured dictionary.
        script_text: str in the format "SPEAKER: line"
        returns: dict with keys "Characters" and "story"
        """
        lines = script_text.strip().split("\n")
        story = []
        characters = set()

        for line in lines:
            if ":" in line:
                speaker, dialogue = line.split(":", 1)
                speaker = speaker.strip()
                dialogue = dialogue.strip()
                story.append({"speaker": speaker, "line": dialogue})
                characters.add(speaker)

        return {
            "Characters": {char: char for char in characters},
            "story": story
        }

    def analyze_script(self, script_text: dict, subtitle_output_path="subtitles.srt"):
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

    def create_srt(script_lines, audio_durations, output_file):
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

# Upload file and get URLs
def upload_audio_to_s3(audio_content, filename=None):
    try:
        # Generate unique filename if none provided
        if not filename:
            filename = f"audio/{uuid.uuid4()}.mp3"
        
        # Upload to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=filename,
            Body=audio_content,
            ContentType='audio/mpeg',
            CacheControl='max-age=3600'
        )
        
        # Generate presigned URL (temporary, secure)
        audio_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET, 'Key': filename},
            ExpiresIn=3600  # 1 hour expiration
        )
        
        # Generate download URL
        download_url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET, 
                'Key': filename,
                'ResponseContentDisposition': 'attachment; filename="story.mp3"'
            },
            ExpiresIn=3600
        )
        
        return {
            'success': True,
            'audioUrl': audio_url,
            'downloadUrl': download_url,
            'filename': filename
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }



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
    """ questions = [
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
    narration_type = answers['narration_type'] """


    """ save_to_csv(res_gen)

    prompt = res_gen["prompt"]
    genre = generator.ask_llm(prompt) """
    

    if_new_idea = input("Do you want to create new idea?") 
    idea = ""
    if (if_new_idea == "y"):
        generator = IdeaGeneratorBiz(prompts.business_psych_ideas_v4)
        idea = validate_step(
            generator.generate_idea(),
            regenerate_func=generator.generate_idea)
        
    else:

        idea = """
            {
            "topic_title": "Why Japanese Convenience Stores Are Engineered For Maximum Efficiency",
            "topic_category": "The 'Hidden System Lens' Lens (Industry / System)",
            "hook_angle": "In a country known for precision engineering, Japan's most brilliantly designed system isn't a bullet train or robot—it's the humble convenience store, where every detail from the door chime to the onigiri wrapper is psychologically calculated.",
            "central_mystery": "How do 7-Eleven, Lawson, and FamilyMart achieve near-perfect efficiency while maintaining intense customer loyalty in a brutally competitive market?",
            "core_revelation": "Japanese konbini aren't retail stores but precision-tuned data factories that use real-time customer behavior to optimize everything from product placement to fresh food production, creating a self-improving ecosystem.",
            "key_examples": [
                "The strategic 'three-beep' door chime that signals customer entry without being intrusive",
                "Precisely angled shelves that create 'forced perspective' making empty spaces look stocked",
                "The 'golden triangle' layout placing high-margin items between entrance, register, and coffee station"
            ],
            "historical_examples": [
                "7-Eleven Japan's 1970s implementation of 'tanpin kanri' (item-by-item management) that revolutionized fresh food retail",
                "The 1987 introduction of heated lockers for delivery meals that created the foundation for today's logistics networks",
                "Lawson's 1990s development of 'karaage-kun' fried chicken that became a \u00a530 billion/year single product phenomenon"
            ],
            "psychological_principles": [
                "Hick's Law (minimizing choice overload)",
                "Operant Conditioning (reward loops through limited-time offerings)",
                "The Ikea Effect (customer participation in meal assembly)"
            ],
            "viral_potential_score": 9,
            "why_it_works": "Reveals hidden design brilliance in everyday experiences, combines surprising efficiency porn with cultural fascination, and showcases systems that could apply to multiple industries—perfect for sponsor integration from productivity or logistics companies."
            }

        """
    if not isinstance(idea,dict):
        idea = json.loads(idea)
    


    if_new_script = input("Wanna make new script?")
    script = ""
    if (if_new_script == "y"):
        writer = Writer()
        writerCounter = CounterintuitiveWriter()

        wrterStyle = input("writer style c(counterintutive) , i(info dense more stats)")
        if (wrterStyle == "i"):
            script = validate_step(
            writer.generate_script_sectioned(topic_data=idea, type="business"),
            regenerate_func=writer.generate_script_sectioned,
            topic_data=idea,
            type="business"
        )
        if (wrterStyle == "c"):
            script = validate_step(
            writerCounter.generate_script_sectioned(topic_data=idea, type="business"),
            regenerate_func=writer.generate_script_sectioned,
            topic_data=idea,
            type="business"
        )
    
    #script = writer.generate_script_sectioned(topic_data=idea, type="business")
    
    print("UNPOLISHED SCRIPT ---------------------- \n\n ", script)
    #script = writer.generate_script_sectioned(topic_data=idea, type="business")
   

    if_review = input("want to make review of script?")
    #script = json.loads(script)
    if if_review == "y": 
        reviewer = Reviewer()
        script = reviewer.polish_script(script)
    
    else:
        script = """{'Characters': {'NARRATOR': 'MAN1'}, 'story': [{'speaker': 'NARRATOR', 'line': "There I am, in the heart of Disney World. The Florida sun is relentless. And I'm holding a $15 Mickey-shaped ice cream bar I never intended to buy."}, {'speaker': 'NARRATOR', 'line': 'The air is thick with the smell of waffle cones and churros. I came here with a plan, a strict budget. Rides and essentials only.'}, {'speaker': 'NARRATOR', 'line': "But somehow, I'm walking out with light-up ears, a princess wand, and a bag full of overpriced souvenirs."}, {'speaker': 'NARRATOR', 'line': "Later, my credit card statement revealed the damage: I'd spent 300% more than I'd planned. But here's the thing..."}, {'speaker': 'NARRATOR', 'line': "This wasn't a personal failure. The data shows this is a universal phenomenon."}, {'speaker': 'NARRATOR', 'line': "Industry insiders call it 'financial theme park amnesia,' and it happens to millions of visitors every single day."}, {'speaker': 'NARRATOR', 'line': 'The US theme park market is a behemoth, reaching a staggering $29.4 billion in 2024 according to Mintel research.'}, {'speaker': 'NARRATOR', 'line': "And those billions? They aren't accidental. They are meticulously engineered."}, {'speaker': 'NARRATOR', 'line': 'Theme parks are psychological battlefields, perfectly designed to ensure we keep spending far beyond our limits.'}, {'speaker': 'NARRATOR', 'line': "Today, we're going to deconstruct this multi-billion dollar persuasion system."}, {'speaker': 'NARRATOR', 'line': "It all started with a simple idea. At Disneyland's 1955 opening, Walt Disney introduced the 'Ticket Book' system."}, {'speaker': 'NARRATOR', 'line': "This wasn't just about crowd control. It was a masterclass in applied psychology."}, {'speaker': 'NARRATOR', 'line': "It created a 'scarcity mindset.' The coveted E-Ticket rides were limited, making them feel more valuable than they actually were."}, {'speaker': 'NARRATOR', 'line': 'That same principle is used today on limited-time merchandise, making that glow wand feel like a now-or-never purchase.'}, {'speaker': 'NARRATOR', 'line': 'But the real turning point came on October 1st, 1982, with the opening of EPCOT Center.'}, {'speaker': 'NARRATOR', 'line': "This wasn't just another park. It was a massive, self-contained resort designed to keep you inside—and spending—for days on end."}, {'speaker': 'NARRATOR', 'line': "This era also perfected the art of the 'themed land,' like Main Street, U.S.A."}, {'speaker': 'NARRATOR', 'line': "These were designed not just for aesthetics, but to act as a psychological airlock. A slow transition into a new reality where normal rules simply don't apply."}, {'speaker': 'NARRATOR', 'line': 'Then came the third revolution: the 2013 introduction of the MagicBand.'}, {'speaker': 'NARRATOR', 'line': 'This removed the physical act of payment entirely. Every purchase became a frictionless, almost invisible tap.'}, {'speaker': 'NARRATOR', 'line': "But what most people don't realize is how all of this targets our deepest psychology."}, {'speaker': 'NARRATOR', 'line': "Which brings us to the central mystery we're here to solve."}, {'speaker': 'NARRATOR', 'line': "Theme parks aren't really selling rides or experiences. They're selling a psychological state."}, {'speaker': 'NARRATOR', 'line': "They're selling 'vacation brain.' An engineered condition of emotional euphoria and decision fatigue."}, {'speaker': 'NARRATOR', 'line': 'A state that systematically bypasses our rational spending safeguards.'}, {'speaker': 'NARRATOR', 'line': 'A 2023 industry study quantifies its effect: the average visitor now spends 40% of their total budget on pure impulse purchases.'}, {'speaker': 'NARRATOR', 'line': 'Social media is filled with micro-anecdotes, like the viral TikTok of a family spending $500 on glow-in-the-dark toys alone.'}, {'speaker': 'NARRATOR', 'line': "It's a carefully crafted environment where 'no' becomes the hardest word to say."}, {'speaker': 'NARRATOR', 'line': "To understand 'vacation brain,' we have to start with the park's physical design."}, {'speaker': 'NARRATOR', 'line': "Disney uses a 'hub-and-spoke' layout. Themed lands branch out from a single, central plaza."}, {'speaker': 'NARRATOR', 'line': "And crucially, you're often funneled through a gauntlet of shops just to reach a ride queue."}, {'speaker': 'NARRATOR', 'line': 'This long, winding journey is a masterclass in exploiting a key psychological principle: decision fatigue.'}, {'speaker': 'NARRATOR', 'line': "Here's the thought block. Decision fatigue is the idea that willpower is a finite resource. It depletes with every choice you make."}, {'speaker': 'NARRATOR', 'line': 'After hours of navigating crowds, choosing where to go, and what to eat, your mental energy is just... gone.'}, {'speaker': 'NARRATOR', 'line': "And research indicates this depleted state makes an impulse purchase a staggering 73% more likely. You've felt this."}, {'speaker': 'NARRATOR', 'line': "But the manipulation is even more precise. You'll notice shops are almost always placed at the ride exit, never the entrance."}, {'speaker': 'NARRATOR', 'line': "This leverages another powerful concept: the 'peak-end rule.'"}, {'speaker': 'NARRATOR', 'line': 'This principle states that we judge an experience based on its emotional peak and its final moment.'}, {'speaker': 'NARRATOR', 'line': 'Your dopamine levels are soaring after that thrilling drop on Splash Mountain.'}, {'speaker': 'NARRATOR', 'line': 'You are euphoric. Your guard is down. And that is precisely when you are most vulnerable.'}, {'speaker': 'NARRATOR', 'line': "It's no surprise that families spend nearly 40% of their entire merchandise budget in these post-ride shops."}, {'speaker': 'NARRATOR', 'line': 'Think of the dad, exhausted from a 12-hour day, who spent $300 on light-up toys simply to end the nagging.'}, {'speaker': 'NARRATOR', 'line': "Or the couple who, riding a high from Pirates of the Caribbean, impulsively bought a $45 necklace because it 'captured the magic.'"}, {'speaker': 'NARRATOR', 'line': 'And these are just the visible traps. The real psychological tricks are far more subtle.'}, {'speaker': 'NARRATOR', 'line': 'The manipulation begins the moment you cross the threshold.'}, {'speaker': 'NARRATOR', 'line': 'Trick #1: The Gateway Decision. Services like stroller rentals are placed just inside the entrance.'}, {'speaker': 'NARRATOR', 'line': "This forces an early financial commitment before you've psychologically acclimated. It's the 'foot-in-the-door' technique."}, {'speaker': 'NARRATOR', 'line': "One dad on Reddit joked he spent $40 on strollers before even seeing Cinderella's Castle. A classic first step."}, {'speaker': 'NARRATOR', 'line': 'A 2019 study found visitors who make a purchase within 15 minutes of entry spend 23% more overall.'}, {'speaker': 'NARRATOR', 'line': "And just when you think you've settled in, the next trap is sprung."}, {'speaker': 'NARRATOR', 'line': 'Trick #2: The Post-Adrenaline Trap. We already touched on this. Merchandise shops at ride exits.'}, {'speaker': 'NARRATOR', 'line': 'It capitalizes on the peak-end rule, targeting you when dopamine levels are highest. Your emotional guard is completely down.'}, {'speaker': 'NARRATOR', 'line': "Ever see a kid walk out of Galaxy's Edge clutching a $200 lightsaber? That's the trap working perfectly."}, {'speaker': 'NARRATOR', 'line': 'Yet these visible traps are just part of a system designed to erode your willpower through frictionless spending.'}, {'speaker': 'NARRATOR', 'line': 'Trick #3: The Decoupled Payment. RFID wristbands like the MagicBand.'}, {'speaker': 'NARRATOR', 'line': "This exploits the 'pain of payment' principle. It separates the pleasure of acquisition from the sting of cost."}, {'speaker': 'NARRATOR', 'line': "One family blog detailed how they lost track and spent $500 on snacks with a simple 'tap.'"}, {'speaker': 'NARRATOR', 'line': 'Studies show these frictionless systems increase on-site spending by 15 to 30 percent.'}, {'speaker': 'NARRATOR', 'line': 'But the most insidious engineering goes even deeper.'}, {'speaker': 'NARRATOR', 'line': 'Trick #4: The Forced March. Pathways lead you in long, circular routes past maximum merchandise.'}, {'speaker': 'NARRATOR', 'line': 'This employs the Gruen Transfer—a concept where disorientation and fatigue dramatically lower your sales resistance.'}, {'speaker': 'NARRATOR', 'line': 'A layout analysis showed the average visitor passes 17 merchandise locations between major attractions.'}, {'speaker': 'NARRATOR', 'line': "Think of the family that got lost in Epcot's World Showcase and impulse-bought $100 in souvenirs just to find their way back."}, {'speaker': 'NARRATOR', 'line': "Together, these tricks systematically engineer 'vacation brain,' creating decision fatigue until you just stop resisting."}, {'speaker': 'NARRATOR', 'line': "But the final, most brilliant trap isn't a shop or a ride. It's the hotel checkout."}, {'speaker': 'NARRATOR', 'line': "Resorts strategically delay your final bill, psychologically decoupling the payment from the vacation's magical end."}, {'speaker': 'NARRATOR', 'line': "One guest tweeted, 'Got my bill a week later. For a few days, it genuinely felt like free money.'"}, {'speaker': 'NARRATOR', 'line': "This 'bill shock' is a calculated move, reportedly increasing post-stay spending by up to 18%."}, {'speaker': 'NARRATOR', 'line': 'And the psychological engineering is everywhere.'}, {'speaker': 'NARRATOR', 'line': "'Limited-time' snacks create artificial scarcity that triggers a fear of missing out."}, {'speaker': 'NARRATOR', 'line': "Themed music isn't just for fun—studies show it puts you in a specifically more generous, spending mood."}, {'speaker': 'NARRATOR', 'line': 'Pumped scents, like vanilla near bakeries, make you linger 15% longer near shops.'}, {'speaker': 'NARRATOR', 'line': "And that character hug? It's a masterclass in emotional leverage, making parents 30% more likely to buy the associated toy."}, {'speaker': 'NARRATOR', 'line': "So remember this. You aren't weak-willed."}, {'speaker': 'NARRATOR', 'line': "You're up against a meticulously designed, billion-dollar persuasion system."}, {'speaker': 'NARRATOR', 'line': "So treat the park like a casino: set a firm daily budget and leave when it's gone."}, {'speaker': 'NARRATOR', 'line': 'Use a pre-paid card to create a hard ceiling. Arm yourself against the impulse.'}, {'speaker': 'NARRATOR', 'line': "Subscribe for more, and we'll see you on the next one."}]}"""
        script = ast.literal_eval(script)



    print("POLISHED SCRIPT \n\n\n", script)

    editor = Editor(VOICE_IDS)

    new_topic_name = idea["topic_title"].strip()[:50].replace(" ", "_")
    new_topic_folder = os.path.join(os.getcwd(), new_topic_name)

    # Create the folder if it doesn't exist
    os.makedirs(new_topic_folder, exist_ok=True)

    # Full path for the subtitle file inside the new topic folder
    subtitle_output_path = os.path.join(new_topic_folder, "subtitles.srt")

    # Pass this path to your analyze_script function
    script_lines = editor.analyze_script(script, subtitle_output_path=subtitle_output_path)
#
    audio_files = editor.generate_audio(script_lines, output_dir="output",srt_file=subtitle_output_path)



    audio_file_name = idea["topic_title"].strip()[:50] + ".mp3"
    audio_file_name = audio_file_name.replace(" ","_")
    save_file_path = os.path.join(new_topic_folder, audio_file_name)

    merged_audio = editor.merge_audio(audio_files, final_output=save_file_path )
    #validate_step(merged_audio)

    #new_topic_folder = "Why_Tech_Companies_Offer_Free_AI_Tools_That_Could_"

    #foldername = "Why_Streaming_Services_Auto-Play_Previews_You_Can'"
    #merged_audio = AudioClip(foldername + "Why_Streaming_Services_Auto-Play_Previews_You_Can'.mp3")
    
    director = VideoDirector(new_topic_folder)
    director.generate_video_seq_from_subtitles()
    """ image_seq_file = validate_step(
        director.generate_video_seq_from_subtitles(),
        regenerate_func=director.generate_video_seq_from_subtitles
    ) """

    #editor.merge_visuals_video(image_seq_file, merged_audio, final_output="final_video.mp4", zoom=False)
    #burn_subtitles()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.post("/api/generate-story")
async def generate_story(request: StoryRequest):

    prompt = request.prompt
    story_type = request.storyType

    if story_type == "biz":
        pass

    elif story_type == "threed":
        #generator = IdeaGenerator3D()
        #prompt_for_llm = generator.generate_prompt_for_llm(prompt)

        
        #genre_idea = generator.ask_llm_no_search(prompt)

        #print("Generated Idea: ", genre_idea)

        writer = ThreeDWriter()
        generated_story = writer.generate_script(topic=prompt)
        
    else:
        generator = IdeaGeneratorLLM()
        prompt_for_llm = generator.generate_prompt_for_llm(prompt)

        
        genre_idea = generator.ask_llm_no_search(prompt_for_llm)

        print("Generated Idea: ", genre_idea)

        writer = Writer()
        prompt_for_writer = writer.get_prompt(genre_idea,"narration")
        generated_story = writer.ask_llm_no_search(prompt_for_writer)
        
    

    # Return as JSON
    return generated_story


@app.post("/api/generate-audio")
async def generate_audio(request: AudioRequest):

    script = request.story

    editor = Editor(VOICE_IDS)
    
    new_topic_name = f"Generated_Audio_Topic_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    new_topic_folder = os.path.join(os.getcwd(), "backend")
    new_topic_folder = os.path.join(new_topic_folder, new_topic_name)

    # Create the folder if it doesn't exist
    os.makedirs(new_topic_folder, exist_ok=True)

    # Full path for the subtitle file inside the new topic folder
    subtitle_output_path = os.path.join(new_topic_folder, "subtitles.srt")

    # Pass this path to your analyze_script function
    script_lines = editor.analyze_script(script, subtitle_output_path=subtitle_output_path)
#
    audio_files = editor.generate_audio(script_lines, output_dir="output",srt_file=subtitle_output_path)

    audio_file_name = "generated_audio"+".mp3"
    audio_file_name = audio_file_name.replace(" ","_")
    save_file_path = os.path.join(new_topic_folder, audio_file_name)

    merged_audio = editor.merge_audio(audio_files, final_output=save_file_path)


    # Upload to S3 and get URLs
    with open(merged_audio, "rb") as f:
        audio_content = f.read()
    
    upload_result = upload_audio_to_s3(audio_content)

    """
    Upload result structure:
    {
        'success': True,
        'audioUrl': 'https://...',
        'downloadUrl': 'https://...',
        'filename': filename
    }
    """
    return upload_result


# python -m uvicorn backend.main:app --reload  (run at root)