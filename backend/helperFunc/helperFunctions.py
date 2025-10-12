from openai import OpenAI
from langchain_openai import ChatOpenAI
import os

import dotenv

dotenv.load_dotenv()
import json


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


def add_emotions_to_text(text, emotion="neutral",model="deepseek/deepseek-chat-v3.1:free"):


    prompt = f"""
    You will be given a JSON object with a "story" field containing lines of dialogue spoken by the characters.  

    Example input:

    {{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Company example with source..."}},
        {{"speaker": "NARRATOR", "line": "Impressive number or trend with source..."}},
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact..."}}
    ]
    }}

    Your task is to:

    1. Add an emotional tone to each line based on the specified emotion: "{emotion}".  
    2. Reflect the emotional tone naturally in the wording of each line.  
    3. Add a "pause_after" field in seconds (use 1 second by default).  
    4. Keep the JSON **lean**, only including: "speaker", "line", "emotion", and "pause_after" for each story line.  
    5. Preserve the "Characters" mapping as-is.  

    Output example:

    {{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Company example with source...", "emotion": "{emotion}", "pause_after": 1}},
        {{"speaker": "NARRATOR", "line": "Impressive number or trend with source...", "emotion": "{emotion}", "pause_after": 1}},
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact...", "emotion": "{emotion}", "pause_after": 1}}
    ]
    }}
    """
    llm = ChatOpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            model=model,
            temperature=0.7,
            max_tokens=12000
        )
    

    res = llm.invoke([{"role": "user", "content": prompt}]).content
    dict_res = deserialize_response(res)

    """
    Adds emotional tone to the given text.
    """
    return f"{text}\n\nMake the above text sound more {emotion}."