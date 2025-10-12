from backend.agents.base_agent import Agent
import backend.prompts as prompts

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
