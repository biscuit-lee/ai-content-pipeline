from backend.agents.base_agent import Agent

# Same as ideagenerator but let the llm choose the params in story experiment
class IdeaGeneratorLLM(Agent):
    """
    AI-driven story idea generator.
    User provides a prompt, and the LLM determines story parameters.
    Optional overrides can be provided to fix certain values.
    """

    def __init__(self):
        super().__init__()

        
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

        Choose these story parameters so that it best fits the prompt for an engaging YouTube story, You could also choose to create your own story category if none fit well with the prompt.:
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

