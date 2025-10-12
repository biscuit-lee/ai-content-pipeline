from backend.agents.base_agent import Agent
import backend.prompts as prompts


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

