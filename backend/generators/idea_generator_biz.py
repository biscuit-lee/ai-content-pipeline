import backend.prompts as prompts
from backend.agents.base_agent import Agent
import json
import os 

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

