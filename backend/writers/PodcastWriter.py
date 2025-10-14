from backend.agents.base_agent import Agent
from backend.prompts import prompt_podcast_narration,prompt_podcast_joerogan
# import load env
import os
from dotenv import load_dotenv

class PodcastWriter(Agent):
    def generate_script(self, topic: str) -> str:
        # Placeholder implementation for generating a podcast script
        load_dotenv()
        prompt = prompt_podcast_narration.format(topic=topic)

        res = self.ask_llm_no_search(prompt)

        return res
    
if __name__ == "__main__":
    load_dotenv()

    writer = PodcastWriter()
    script = writer.generate_script("AI replacing humans creativity")
    print(script)