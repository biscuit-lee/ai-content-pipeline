from backend.agents.base_agent import Agent
import inquirer
from inquirer.themes import GreenPassion
import random
import os
import json


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

