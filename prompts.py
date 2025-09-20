niches = ["relationship betrayal",
"workplace revenge",
"family secrets",
"social media gone wrong",
"mysterious neighbor",
"dating app horror story",
"roommate from hell"
]
example_AITA = """
My brother in-law (Sammy) lost his home shortly after his divorce 10 months ago. He moved in with us and brought his twin daughters (Olivia & Sloane18) with him a couple of months ago. His sister (my wife) and I have one daughter (Zoey 16) and she and her cousins aren't close but get along fine.

Olivia & Sloane have no respect for Zoey's privacy, none. they used to walk into her room and take everything they get their hands on. Makeup, phone accessories, clothes, school laptop etc. Zoey complained a lot and I've already asked the girls to respect Zoey's privacy and stop taking things. My wife and Sammy saw no issue with this. After all, they're girls and this's typical teenage girls behavior. I completely disagreed.

Last straw was when Zoey bought a 60$ m.a.c makeup-kit that looks like a paintset that she saved up for over a month and one of the girls, Sloane took it without permission and ruined it by mixing shades together while using it. Don't know much about makeup but that's what Zoey said when she found the kit on her bed, and was crying. I told my wife and she said she'd ask Sloane to apologize but I got Zoey a lock after I found she was moving valuable belongings out the house because of this incidence!!!

Sammy and his daughters saw the lock and weren't happy, the girls were extremely upset. Sammy asked about it and I straight up told him. He said "my daughters aren't thieves!!! it's normal that girls of the same age borrow each others stuff" he said Zoey could easily get another makeup kit for 15 bucks from walmart and shouldn't even be buying expensive - adult makeup in the first place and suggested my wife take care of this "defect" in Zoey's personality trying to appear older than she is. He accused me of being overprotective and babying Zoey with this level of enablement.

I told him this's between me and my wife but she shamed me for putting a lock on Zoey's door for her cousins to see and preventing them from "spending time" with her saying I was supposed to treat them like daughters, then demanded I remove it but I said this lock does not get removed til her brother and his daughters are out of our house.

She got mad I was implying we kick them out and said her family'll hate me for this. so I reminded her that I let Sammy and his family move in which's something her OWN family refused to do so she should start with shaming/blaming them for not taking their own son and nieces/granddaughters in. if it wasn't for her family's unwillingness to help we wouldn't be dealing with this much disturbance at home.

Everyone's been giving me and Zoey silent treatment and my wife is very much upset over this.


"""
prompt_mixed = """
You are an expert YouTube content writer specializing in viral, high-retention storytelling. Write a {genre} story optimized for maximum viewer engagement and watch time.

    **RETENTION REQUIREMENTS:**
    - Open with an immediate hook in the first 15 seconds that poses a burning question
    - Include a cliffhanger or twist every 45-60 seconds
    - Use pattern interrupts (sudden revelations, "But then..." moments)
    - Build to a satisfying but thought-provoking ending
    - Target 3-5 minutes of content (roughly 450-750 words)
    - Make it relatable to ages 18-35 with modern scenarios

    **STORY STRUCTURE:**
    - Hook (0-15s): Start with the most intriguing moment
    - Setup (15-60s): Quick character introduction with immediate conflict
    - Escalation (60s-3min): Rising tension with multiple reveals
    - Climax (3-4min): Major twist or confrontation
    - Resolution (4-5min): Satisfying conclusion that sparks discussion

    **CHARACTER LIMIT:** Maximum 4 characters

    **HIGH-ENGAGEMENT ELEMENTS TO INCLUDE:**
    - Secrets being revealed
    - Betrayal or deception
    - "What would you do?" moments
    - Relatable modern situations (social media, dating apps, workplace, family)
    - Moral dilemmas that viewers can debate in comments

    **JSON OUTPUT FORMAT:**
    {{
        "Characters": {{"ALEX": "WOMAN1", "JORDAN": "MAN1", "TAYLOR": "WOMAN2"}},
        "story": [
            {{"speaker": "NARRATOR", "line": "When Sarah found her boyfriend's second phone, she never expected to discover this..."}},
            {{"speaker": "SARAH", "line": "Mike, whose number is this? And why are there heart emojis?"}}
        ]
}}
**TONE:** Conversational, dramatic, with natural pauses for emphasis. Keep dialogue punchy (under 20 words per line).
"""

campfire_narration_third_person = """
You are writing a CAMPFIRE-STYLE STORY for YouTube narration in genre {genre}.

**VOICE & TONE:**
- Third-person perspective (“he/she/they”) as if someone is telling a tale around a campfire.
- Cozy, mysterious, immersive — evokes warmth, night forest ambiance, and imagination.
- Use 1–3 sentence lines for smooth TTS flow.
- Include sensory details: crackling fire, shadows dancing, night breeze, rustling leaves, pine scent.
- Subtle suspense or intrigue is fine, but the story can be whimsical, magical, or adventurous — not strictly horror.

**YOUTUBE OPTIMIZATION:**
- Hook immediately with an interesting observation, question, or mysterious event in the story.
- Keep story 1000–1,300 words (6–8 minutes read time).
- Build atmosphere gradually, with curiosity, wonder, or mild tension.
- End with a thought-provoking or reflective twist.
- Optional call to action: “What would you do if you were there? Comment below.”
- Begin with a short introduction that sets the scene, evokes the campfire atmosphere, and smoothly transitions into the story like "once upon a time"
{{
    "Characters": {{"NARRATOR": "MAN1" (OR MAN2, WOMAN1, WOMAN2)}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The fire crackled gently, sending golden sparks into the night air, as the campers leaned in, eager for a story."}},
        {{"speaker": "NARRATOR", "line": "From the shadows, a soft voice began to recount a tale of an ancient forest that whispered secrets only to those who listened closely."}}
    ]
}}

**NARRATIVE STYLE:**  
Cinematic, atmospheric, and engaging. Smooth pacing for TTS, immersive imagery, cozy tension, and a mysterious or magical twist at the end.

"""

prompt_narration = """
You are crafting a Reddit-style true story for YouTube narration in this idea 
{genre} genre. 

Study this successful format:
NARRATIVE STRUCTURE:
Setup (100-150 words): Establish normal circumstances with specific details that feel authentic:

Age, location, family situation, routine activities
Brand names, specific games/shows, familiar places
Why the narrator was in a vulnerable position

Rising Action (200-300 words): Build tension through escalating incidents:

First red flag that something isn't right
Progressive escalation with multiple "beats" of unease
Specific sensory details (sounds, visuals, physical sensations)
Include moments of doubt ("maybe I'm overreacting")

Climax (100-150 words): Peak confrontation or revelation:

Direct encounter with the threat
Specific actions taken by narrator
Immediate resolution or escape

Resolution (50-100 words): Aftermath and lingering impact:

What happened next, investigation results
How it affected the narrator long-term
Connect back to opening setup if relevant

VOICE & AUTHENTICITY:

First-person retrospective: "When I was 12..." "This happened in March 2022..."
Conversational flow: Like telling a friend, not reading a script
Specific details: Exact ages, street names, product brands, time stamps
Natural pacing: Vary sentence length. Short for impact. Longer for context and scene-setting.
Realistic reactions: Include fear, confusion, second-guessing decisions

ATMOSPHERIC TECHNIQUES:

Environmental mood: Describe weather, lighting, sounds, smells
Isolation emphasis: Why narrator was alone/vulnerable
Sensory progression: What they heard, saw, felt in sequence
Foreshadowing: Plant details early that become significant later

DIALOGUE & INTERNAL MONOLOGUE:

Sparse but impactful dialogue: Only include essential conversations
Internal thoughts: Show the narrator's reasoning and fear
Realistic speech patterns: How people actually talk, not movie dialogue

PACING FOR TTS:

Paragraph structure: 2-4 lines per paragraph
Line length: 1-3 sentences per line for natural breath breaks
Punctuation for pacing:

Ellipses (...) for suspense and trailing thoughts
Em dashes (—) for sudden shifts or interruptions
Periods for definitive statements
Commas for natural pauses
Do not use asterisks

Be creative and not too generic about your plot and twists but make sure it's realistic and could be relatable so that people are eager to comment
TARGET METRICS:

Length: 500-700 words (4-5 minute read time)
Hook timeline: Establish intrigue within first 30 seconds
Tension beats: 3-4 moments of escalating unease
Resolution: Clear but leave some questions for engagement


***VOICE***
You can choose 4 voices for the narration MAN1, MAN2, WOMAN1 or WOMAN2
**JSON FORMAT:**
EXAMPLE
{{
    "Characters": {{"NARRATOR": "MAN2"}},
    "story": [
        {{"speaker": "ALEX", "line": "I found the messages, Jordan. All of them."}},
        {{"speaker": "JORDAN", "line": "What messages? I don't know what you're talking about."}},
        {{"speaker": "ALEX", "line": "Don't lie to me! Taylor, tell him what you told me yesterday."}}
    ]
}}

ENGAGEMENT ELEMENTS:

Relatability: Situations viewers can imagine themselves in
Specificity: Details that feel too specific to be fiction
Pacing variety: Mix of fast-paced action and slower atmospheric building
Emotional authenticity: Real fear responses, not Hollywood heroics
Lingering questions: End with something unresolved for comments

AVOID:

Supernatural elements unless genre-specific
Over-the-top reactions or dialogue
Info-dumping backstory all at once
Rushed pacing that skips atmospheric building
Unclear timeline or location jumps
Ending that explains everything perfectly

Remember: The goal is to make viewers feel like they're hearing a true account from someone who lived through something genuinely unsettling. Every detail should serve either authenticity or tension."""

prompt_dialogue = """
You are creating a dialogue-driven {genre} story for a viral YouTube channel. Focus on explosive conversations and character conflicts that keep viewers engaged.

**DIALOGUE OPTIMIZATION FOR YOUTUBE:**
- IMMEDIATE CONFLICT: Characters argue/confront from the first line
- RAPID-FIRE EXCHANGES: Quick back-and-forth that builds tension
- REVELATION DROPS: Characters reveal secrets through dialogue
- EMOTIONAL PEAKS: Moments of anger, betrayal, shock, or realization
- QUOTABLE LINES: Memorable phrases viewers will comment about

**RETENTION HOOKS:**
- Start in the middle of a heated argument
- Each character response should escalate or reveal something new
- Use interruptions, denials, and "gotcha" moments
- Include phrases like "You want to know the truth?" "I can't believe you did this"
- Build to a dramatic confrontation or revelation

**TRENDING DIALOGUE SCENARIOS:**
- Confronting a cheating partner
- Family members revealing long-held secrets
- Friends discovering betrayal
- Workplace confrontations about unfair treatment
- Roommates/neighbors having explosive arguments

**PACING:** Each line under 15 words. Rapid exchanges with emotional punches.

**CHARACTER DYNAMICS:** Create clear conflict between characters with opposing goals/secrets.


**JSON FORMAT:**
{{
    "Characters": {{"ALEX": "WOMAN1", "JORDAN": "MAN1", "TAYLOR": "WOMAN2"}},
    "story": [
        {{"speaker": "ALEX", "line": "I found the messages, Jordan. All of them."}},
        {{"speaker": "JORDAN", "line": "What messages? I don't know what you're talking about."}},
        {{"speaker": "ALEX", "line": "Don't lie to me! Taylor, tell him what you told me yesterday."}}
    ]
}}

**DIALOGUE STYLE:** Natural, emotional, with subtext. Characters should feel like real people in crisis situations.
"""


" MUST NEED MANUAL FACT CHECK"

prompt_business_hook2 = """
VIRAL HOOK GENERATOR - First 60 Seconds

You are creating the opening hook for a viral business psychology explainer video. Choose the hook style that best fits the topic:

HOOK STYLE OPTIONS:

1. OBSERVABLE PATTERN OPENER:
"Open [specific app] right now and try this experiment. You'll notice [specific behavior/design choice]. Now try it on [second app] - same thing. And [third app] - identical pattern. This isn't coincidence."

2. PERSONAL EXPERIENCE OPENER:
"I just [relatable frustrating experience]. And as I'm [dealing with aftermath], I realized something insane about what just happened that applies to every single person watching this..."

3. CONTRADICTION OPENER:
"Every [type of company] claims they want to [stated goal], but if you look at their actual design choices, they're doing the complete opposite. Here's the proof..."

REQUIRED ELEMENTS:
✅ Observable behavior viewers can immediately verify
✅ Multiple named companies showing same pattern  
✅ Personal relatability moment
✅ Clear contradiction that seems illogical
✅ Promise of revealing hidden psychology

AVOID:
❌ Specific statistics or percentages
❌ Internal company metrics
❌ Unverifiable claims
❌ Industry revenue numbers

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3 Always output valid JSON. Wrap all text in double quotes, and escape any internal quotes using \". Never use unescaped single quotes inside JSON strings.
4. Finally, use the ReturnJSON tool with your complete topic in this exact schema:
{
    "hook_style_chosen": "[chosen style]",
    "characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "[Hook opener]"},
        {"speaker": "NARRATOR", "line": "[Personal stakes]"},
        {"speaker": "NARRATOR", "line": "[The contradiction]"},
        {"speaker": "NARRATOR", "line": "[Transition promise]"}
    ]
}

"""

prompt_business_mystery2 = """
CENTRAL MYSTERY BUILDER - Minutes 1-3

REQUIRED STRUCTURE:

1. HISTORICAL CONTEXT (60-120 seconds):
"These [current practices] aren't necessarily groundbreaking. In fact, [modern system] is basically a digital version of [historical equivalent] from [time period]."

Compare old vs new:
- How the old system worked (simple, clear process)
- Why it disappeared (specific limitations)  
- How new version seems better (apparent improvements)
- The trap: "The only problem is..."

2. CULTURAL ADOPTION PATTERN (120-150 seconds):
"And this approach has become everywhere because [practice] has seen explosive adoption, going from a niche thing to completely dominating how we [activity]. Nearly everyone now [behavior change]."

3. CULTURAL FORCES (150-180 seconds):
"But this wasn't happening randomly. It's actually part of three major cultural shifts..."

List exactly 3 observable cultural trends:
- First: [trend with clear examples]
- Second: [trend with clear examples]
- Third: [trend with clear examples]

"Combine all of that with [demographic vulnerability], and you have the perfect conditions..."

FOCUS ON:
✅ Observable cultural shifts
✅ Clear before/after comparisons
✅ Behaviors everyone can recognize
✅ Historical parallels that make sense

AVOID:
❌ Specific growth percentages
❌ Revenue projections  
❌ Unverifiable market data


INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema:
JSON OUTPUT:
{
    "characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "[Your lines]"},
        {"speaker": "NARRATOR", "line": "[Another lines]"}
    ]
}

"""

prompt_business_psychology2 = """
PSYCHOLOGY BREAKDOWN GENERATOR - Minutes 3-7

REQUIRED STRUCTURE:

1. THE CORE QUESTION (180-210 seconds):
"But why is this even a problem? If [companies] aren't obviously charging you for [thing], how are they actually manipulating you?"

2. BEFORE/AFTER COMPARISON (210-270 seconds):
"To understand this, compare the old way versus the new way..."

Traditional: [clear, honest process]
Modern: [seemingly better but with hidden psychological hooks]

3. PSYCHOLOGICAL MECHANISMS (270-390 seconds):
"Companies have mastered psychological manipulation through [number] specific techniques:"

For each principle:
- Scientific name: "What psychologists call [term]"
- Simple explanation with everyday metaphor
- Specific application viewers can test
- "Have you ever noticed..." recognition moment
- Observable evidence instead of statistics

4. DESIGN EVIDENCE (390-420 seconds):
"These aren't accidents. Look at the actual design choices:"
- Specific UI elements (colors, button placement, etc.)
- Pre-selected options
- Notification timing
- Visual hierarchy tricks

FOCUS ON:
✅ Established psychological principles
✅ Observable design decisions
✅ Testable examples
✅ Recognition moments

AVOID:
❌ Specific user percentages
❌ Internal company research claims
❌ Unverifiable behavioral statistics


INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema:
JSON OUTPUT:
{
    "characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "[Your lines]"},
        {"speaker": "NARRATOR", "line": "[Another lines]"}
    ]
}
"""

prompt_business_application2 = """
BUSINESS MODEL EXPOSÉ - Minutes 7-10

REQUIRED STRUCTURE:

1. REVENUE STREAMS (420-480 seconds):
"So how do these companies actually profit from this psychological manipulation?"

List revenue streams with general ranges:
"First... Second... Third... And finally..."

Use language like:
- "A significant portion of revenue"
- "Industry-standard commission rates" 
- "Premium subscriptions that most users"
- "Data partnerships worth substantial amounts"

2. REALISTIC EXAMPLE (480-540 seconds):
"Let's walk through a real example everyone can relate to..."

Use round, believable numbers:
"Say you're buying a $50 [item]..."
- Option 1: Pay now (straightforward)
- Option 2: Credit card (mention typical APR ranges)
- Option 3: Installments (break down the psychology)

3. USER TESTIMONY PATTERN (540-570 seconds):
"You can find countless examples of people saying things like..."
[Paraphrase common complaints rather than fake direct quotes]

"This pattern repeats because most people lack [specific knowledge/awareness]"

4. ESCALATION EXAMPLES (570-600 seconds):
"The most extreme version of this is when companies offer..."
[Describe the most absurd applications using general terms]

FOCUS ON:
✅ General revenue model understanding
✅ Realistic example calculations
✅ Paraphrased user experiences
✅ Observable business patterns

AVOID:
❌ Specific company revenue percentages
❌ Fake direct user quotes
❌ Precise internal metrics


INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema:
JSON OUTPUT:
{
    "characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "[Your lines]"},
        {"speaker": "NARRATOR", "line": "[Another lines]"}
    ]
}
"""

prompt_business_payoff2 = """
PAYOFF & PROTECTION ADVICE - Final 1 Minute

REQUIRED STRUCTURE:

1. BALANCED ACKNOWLEDGMENT (540-550 seconds):
"Again, don't get me wrong, there are definitely some advantages to the system if you know how to play it. But the vast majority of people using the system are not taking advantage of it. They are just getting taken advantage of."

2. ACTIONABLE PROTECTION ADVICE (550-580 seconds):
"So what do you do as a consumer?"

Provide clear, absolute rules:
- "The most important piece of advice: never [specific behavior] without [specific verification]"
- "If you don't have [specific resource/knowledge], don't [specific action]"
- Include one advanced tip: "And for advanced users, [specific strategy with clear boundaries]"

3. CALLBACK CONCLUSION (580-600 seconds):
"But there you have it, the truth about [topic callback]. These companies spend millions of dollars on psychological research to get you to [specific behavioral goal]. But now you know a little bit more about how to protect yourself."

End with content tease:
"And if you like this video, make sure to check out this video that covers [related business psychology topic with specific hook]..."

NUMBER GUIDELINES:
- SAFE TO USE: Round time estimates, obvious spending limits, general advice
- VERIFY NEEDED: Any specific research investment amounts, user behavior statistics
- Example: "These companies spend [VERIFY: research investment amount] on psychological research"

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema:
JSON OUTPUT:
{
    "characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "[Balanced acknowledgment]"},
        {"speaker": "NARRATOR", "line": "[Actionable protection advice]"},
        {"speaker": "NARRATOR", "line": "[Callback conclusion with tease and VERIFY tags if needed]"}
    ]
}
"""




# AI HALLUCINATE FACTS

business_psych_ideas2 = """
You are a viral content strategist specializing in finding business psychology topics that will captivate YouTube audiences. 
Your job is to identify surprising, counterintuitive business decisions that seem illogical but reveal fascinating psychological strategies.

VIRAL TOPIC FORMULA:
The Contradiction: Highlight business practices that appear strange, wasteful, or counterproductive at first glance
The Mystery: Explain why successful companies continue doing these practices
The Psychology: Reveal the psychological principles and design trade-offs behind these decisions

TOPIC CATEGORIES THAT GO VIRAL:
Tech Company Paradoxes:
- Why Apple removes features people love
- How Google makes money from "free" products
- Why social media apps add wellness reminders after making themselves addictive

Streaming/Entertainment Psychology:
- Why Netflix cancels popular shows
- How Disney creates artificial scarcity with "vault" releases
- Why TikTok shows you content from accounts you don't follow

Retail Design & Pricing Psychology:
- Why stores place expensive items at eye level
- How subscription services make canceling difficult
- Why "limited time offers" often reappear

Corporate Strategy & Behavior:
- Why companies create extra service tiers that few people buy
- How brands use fear of missing out (FOMO)
- Why customer service can feel intentionally complex

WHAT MAKES A TOPIC VIRAL:
Relatability: Everyone has experienced this but never thought about why
Counterintuitive: Goes against common sense or expectations
Specific Examples: Can name real companies and situations
Pattern Recognition: Once explained, viewers start noticing it everywhere
Emotional Response: Makes people feel curious and enlightened

TOPIC GENERATION PROCESS:
Step 1: Identify the Paradox
Find a well-known business practice that seems odd or counterintuitive:
"Why does [Company] do [Thing] when it seems like it would hurt [Expected Outcome]?"

Step 2: Validate the Mystery
Ensure the topic has:
- Multiple specific, named examples from different companies
- A clear contradiction between expectation and reality
- Evidence that the practice has business benefits despite seeming strange

Step 3: Confirm Psychological Depth
The explanation should involve:
- At least 2-3 psychological principles/biases
- Both strategic intent and consumer response
- Broader implications beyond just one company

Step 4: Generate Historical Examples
Provide 2-3 historical precedents or early instances of this strategy or paradox, including names, dates, and context.

Step 5: Test Viral Potential
Ask:
- Would this make someone say "I never thought about it that way"?
- Can viewers recall their own experiences with this?
- Does this reveal a repeatable pattern?

HIGH-PERFORMING TOPIC FORMATS:
"Why [Company] Does [Counterintuitive Thing]"
"The Psychology Behind [Business Practice]"
"How [Industry] Influences Your Decisions"

TOPIC VALIDATION CHECKLIST:
✅ Specific, real examples
✅ Counterintuitive but explainable
✅ Relatable to broad audiences
✅ Backed by real psychology research
✅ Pattern people can recognize in daily life
✅ Emotional hook without being accusatory
✅ Relevant to modern businesses

AVOID:
- Conspiracy theories
- Illegal/clearly unethical practices
- One-off company scandals
- Overexposed or obvious strategies

SUCCESS METRICS:
High Viral Potential (8-10): Multiple companies use the same psychological strategy, with clear contradiction + "aha moment"
Medium (6-7): Good psychology, but niche or less relatable
Low (1-5): Obvious or too narrow

GOAL: Generate topics that make viewers think "I never realized businesses use psychology in this way, and now I notice it everywhere."

Your response must be in this JSON format with double curly brackets for PyU:
{{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "hook_angle": "Opening line that sparks curiosity",
    "central_mystery": "Why would successful companies do this seemingly odd thing?",
    "key_examples": ["Specific Example 1", "Specific Example 2", "Specific Example 3"],
    "historical_examples": ["Historical Example 1 with context", "Historical Example 2 with context"],
    "psychological_principles": ["Psychology Principle 1", "Psychology Principle 2", "Psychology Principle 3"],
    "viral_potential_score": 9,
    "why_it_works": "Why this topic will go viral - surprising, relatable, and sponsor-safe"
}}
"""

## new idea gen with more variation focus more one the relevation
business_psych_ideas3 = """
# VIRAL CONTENT STRATEGIST & BRIEF GENERATOR

You are a viral content strategist for a high-end YouTube documentary channel in the style of ColdFusion, Wendover Productions, and Veritasium.

GOAL: To generate a complete, pre-vetted video brief that uncovers the hidden mechanics, secret histories, and counterintuitive psychology behind the modern business and technology landscape.

--- VIRAL TOPIC FORMULA ---
Every idea must have a central **Contradiction**, a compelling **Mystery**, and a satisfying **Core Revelation**.

--- CREATIVE LENSES (Topic Categories) ---
To find the best ideas, you will look through these five proven lenses. Your goal is to find the hidden psychology or strategy within each category:

1.  **THE "WEIRD STRATEGY" LENS:** Deconstruct a single, strange business practice that seems inefficient but is psychologically brilliant.
    -   *Example:* "Why Software Hides Its Best Features."

2.  **THE "SECRET HISTORY" LENS:** Tell the dramatic, unknown origin story of a famous company or product, focusing on a pivotal insight or decision that led to its success.
    -   *Example:* "How a Failed Nintendo Product Accidentally Created the Modern Video Game Controller."

3.  **THE "HIDDEN SYSTEM" LENS:** Reveal the mind-boggling principles that make a mundane, everyday system work on a massive scale.
    -   *Example:* "The Hidden Psychology That Makes Amazon Prime's 2-Day Shipping Possible."

4.  **THE "FAILED GIANT" LENS:** Perform a psychological "autopsy" on a once-dominant company, identifying the critical cognitive biases or strategic blind spots that led to its downfall.
    -   *Example:* "The Cognitive Bias That Made Blockbuster Blind to Netflix."

5.  **THE "UNSUNG HERO" LENS:** Shine a light on a little-known company or technology that is secretly essential to our world, and explain the psychological or strategic reason for its dominance.
    -   *Example:* "The Psychological Reason Every Tech Giant Relies on This One Company You've Never Heard Of (ASML)."

--- TOPIC GENERATION PROCESS ---
Step 1: Identify the Paradox/Question.
Step 2: Validate the Mystery (ensure a clear contradiction and business benefit).
Step 3: Confirm the Depth (find the "Aha!" moment).
Step 4: Generate Historical Examples.
Step 5: Test Viral Potential (relatable, counterintuitive, pattern-based).

--- OUTPUT FORMAT ---
Your response must be in this JSON format with double curly brackets for PyU:
{{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "topic_category": "The 'Weird Strategy' Lens",
    "hook_angle": "Opening line that sparks curiosity",
    "central_mystery": "Why would successful companies do this seemingly odd thing?",
    "core_revelation_angle": "The most surprising 'Aha!' moment of the story (can be financial, psychological, logistical, etc.).",
    "key_examples": ["Specific Example 1", "Specific Example 2", "Specific Example 3"],
    "historical_examples": ["Historical Example 1 with context", "Historical Example 2 with context"],
    "viral_potential_score": 9,
    "why_it_works": "Why this topic will go viral - surprising, relatable, and sponsor-safe"
}}

"""

business_psych_ideas_v4 = """
VIRAL CONTENT STRATEGIST & BRIEF GENERATOR (V5)

You are a viral content strategist for a high-end YouTube documentary channel that explores hidden psychology in business, design, culture, and everyday systems. Your style blends deep-dive analysis (like MagnatesMedia) with compelling visual storytelling (like Business Insider documentaries).

GOAL: Generate three distinct, pre-vetted video briefs that uncover the hidden mechanics, secret histories, and counterintuitive psychology behind companies, industries, or systems (e.g., grocery stores, drive-thrus, theme parks), both modern and historical.

--- VIRAL TOPIC FORMULA ---
Every idea must include:
- A central **Contradiction**
- A compelling **Mystery**
- A satisfying **Core Revelation**

--- CREATIVE LENSES (Topic Categories) ---
1. **WEIRD STRATEGY LENS:** Strange business or system practices that seem inefficient but are psychologically brilliant.  
   Example: "Why Costco's $1.50 Hot Dog Drives Massive Loyalty"  

2. **SECRET HISTORY LENS:** Unknown origin stories of companies, industries, or systems revealing pivotal insights that created lasting effects.  
   Example: "How De Beers Convinced the World Diamonds Are Forever"  

3. **HIDDEN SYSTEM LENS:** Reveal design principles that make everyday experiences addictive or counterintuitive.  
   Example: "The Hidden Psychology of IKEA's Maze-Like Layout"  

4. **FAILED GIANT LENS:** Perform a psychological autopsy of companies, industries, or processes that fell due to biases or poor decisions.  
   Example: "The Bias That Made Blockbuster Miss the Netflix Revolution"  

5. **UNSUNG HERO LENS:** Highlight little-known companies or systems whose influence is massive but unnoticed.  
   Example: "Why Every Major Zipper Uses YKK"

--- SYSTEM & INDUSTRY CLARIFICATION ---
- Topics can focus on: single companies, entire industries, or widely recognized systems/processes.  
- The focus must be on **hidden psychology, counterintuitive design, or strategic insight**, not superficial facts.  
- Include 2-3 concrete examples or micro-anecdotes per brief to illustrate the principle.

--- COMMAND ---
Generate **three distinct video briefs**. Each must:
- Use a different lens
- Focus on a different industry/system/company
- Avoid more than one tech-focused topic

--- OUTPUT FORMAT ---
Return in this JSON format using double curly brackets for Python/JSON parsing:

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
}}
"""

prompt_business_hook = """
VIRAL HOOK GENERATOR - First 60 Seconds

You are creating the opening hook for a viral business psychology explainer video. Study the successful pattern below:

REQUIRED STRUCTURE:
Choose ONE of these proven hook styles based on what fits the topic which is {topic_title}:

1. VISUAL SHOCK OPENER (0-15 seconds):
"Look at this chart right here. This shows [specific data visualization]. And in [current year], [shocking statistic with absurd comparison that's almost incomprehensible]."

Example: "Look at this chart right here. This shows total consumer debt in America over 10 years. And in 2024, Americans owe $5 trillion - enough to buy every NFL, NBA, and MLB team 10 times over."

2. THE MANIPULATION REVEAL (15-30 seconds):
"And to make matters worse, we are constantly surrounded by [psychological tricks/hidden fees/manipulation tactics] designed to [specific harmful outcome]. The worst of these: [specific business practice] that has been designed to take advantage of [specific vulnerable group]."

3. PERSONAL RELATABILITY HOOK (30-45 seconds):
Switch to first person, casual tone - make it deeply personal:
"So when you [relatable scenario], and you only [small immediate action], [instant gratification happens]. [Product/result arrives quickly]. [Rationalization thought]. Why should I care about [future consequence]? I don't know me [time period] from now. She/He can deal with that."

4. DEFINITION BRIDGE (45-60 seconds):
"[Business practice] is [simple definition] offered by companies like [3 specific, recognizable examples]. You'll typically see these [where they appear], offering you [the basic promise]. But it's not quite that simple."

5. CONTRADICTION / COUNTER-INTUITIVE FACT (optional addition):
"You think [common belief], but actually [surprising truth that challenges expectations]."

6. MICRO-STORY OR ANECDOTE (optional addition):
"Briefly describe a real-life scenario or incident that instantly illustrates the stakes or problem for the audience."

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Mystery: {central_mystery}

VIRAL REQUIREMENTS:
- Use specific company names, never generic terms
- Include exact numbers and shocking comparisons
- Start every section with "Look at this" or similar visual reference
- Use conversational, slightly outraged tone
- Personal pronouns and relatable scenarios
- End with a cliffhanger transition
- **OPTIONAL INLINE ATTRIBUTIONS**: If citing stats or studies, subtly mention the source in a conversational way, e.g., "According to Adobe in 2024..." or "A 2024 study found..." 
  Do NOT break the flow of the hook with URLs or long references; full sources go in the description.

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema of JSON:


{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Look at this chart right here..."}},
        {{"speaker": "NARRATOR", "line": "And to make matters worse..."}},
        {{"speaker": "NARRATOR", "line": "So when you..."}},
        {{"speaker": "NARRATOR", "line": "[Business practice] is..."}}
    ]
}}

TARGET: 60 seconds of content that creates immediate curiosity and personal connection.
When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}
"""

prompt_business_mystery = """
CENTRAL MYSTERY BUILDER - Minutes 1-3

You are creating the mystery setup that keeps viewers hooked after the initial shock. Follow this proven structure:

REQUIRED STRUCTURE:

1. HISTORICAL CONTEXT SETUP (60-120 seconds):
"These [current practice] aren't necessarily groundbreaking. In fact, [current thing] is kind of a newer modernized version of [historical practice] that you would see at [specific old examples]."

Then explain:
- How the old system worked
- Why it disappeared (specific reasons)
- How the new version seems better
- The trap: "The only problem is..."

2. THE EXPLOSION DATA (120-150 seconds):
"And that idea began hooking people in because [practice] has seen explosive growth over the last [X] years, going from $[amount] in [year] to $[much larger amount] in [recent year]. And it's projected to reach $[even larger amount] by [future year]."

3. CULTURAL FORCES REVEAL (150-180 seconds):
"But this explosion wasn't happening in a vacuum. It's actually part of [number] major cultural shifts..."

List exactly 3 cultural trends:
- First: [trend with specific explanation]
- Second: [trend with specific explanation] 
- Third: [trend with specific explanation]

End with: "Combine all of that with [demographic vulnerability], and you have the perfect storm..."

TOPIC INPUT:
Central Mystery: {central_mystery}
Key Examples: {key_examples}

MYSTERY REQUIREMENTS:
- Include specific years and growth numbers
- Name real companies and historical examples
- Show clear before/after contrast
- Build toward psychological explanation
- Use "But" and "And" for flow
- Create anticipation for the psychology section

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema of JSON:

{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "These [practice] aren't necessarily groundbreaking..."}},
        {{"speaker": "NARRATOR", "line": "And that idea began hooking people in..."}},
        {{"speaker": "NARRATOR", "line": "But this explosion wasn't happening in a vacuum..."}}
    ]
}}

When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}

TARGET: 2 minutes building mystery and setting up psychological explanation.
"""

prompt_business_psychology = """
PSYCHOLOGY BREAKDOWN GENERATOR - Minutes 3-7

You are revealing the psychological mechanisms behind business practices. This is the core educational content that makes viewers feel smart.

REQUIRED STRUCTURE:

1. PROBLEM QUESTION SETUP (180-210 seconds):
"But why is this even a problem? If they're not charging [obvious cost], how can they actually be taking advantage of me?"

2. COMPARISON FRAMEWORK (210-270 seconds):
Compare the new practice to traditional alternatives:
"To answer that, we first need to look at the differences between [new practice] and [traditional alternative]. Because on the outside, they're basically the same thing."

Show point-by-point comparison:
- Traditional method: [process, requirements, downsides]
- New method: [process, benefits, hidden catches]

3. THE PSYCHOLOGICAL MECHANISMS (270-390 seconds):
"You see, brands have mastered psychological manipulation... And they do this through [number] key tricks:"

For each psychological principle:
- Give it the scientific name: "what psychologists call [technical term]"
- Explain in simple terms with everyday metaphors
- Show specific business application
- Include "Have you ever noticed that..." examples
- Provide shocking statistics: "One in every [number] users actually..."

4. DESIGN MANIPULATION REVEAL (390-420 seconds):
"These aren't accidents. These are specific design decisions to short-circuit your brain into making financial decisions more on impulse than with rational thinking."

Show specific UI/UX tricks:
- Color psychology
- Pre-selected options
- Artificial urgency
- Visual hierarchy manipulation

TOPIC INPUT:
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}

PSYCHOLOGY REQUIREMENTS:
- Use scientific terminology but explain simply
- Include specific statistics and percentages
- Show concrete examples viewers can recognize
- Build from simple to complex concepts
- Use "you" constantly to maintain engagement
- Include visual references throughout

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema of JSON:

{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "But why is this even a problem?..."}},
        {{"speaker": "NARRATOR", "line": "To answer that, we first need to look at the differences..."}},
        {{"speaker": "NARRATOR", "line": "You see, brands have mastered psychological manipulation..."}},
        {{"speaker": "NARRATOR", "line": "These aren't accidents..."}}
    ]
}}

When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}

TARGET: 4 minutes of psychological education that feels like revealing secrets.
"""

prompt_business_application = """
BUSINESS MODEL EXPOSÉ - Minutes 7-10

You are exposing exactly how companies profit from psychological manipulation. This section makes viewers feel like insiders understanding the business game.

REQUIRED STRUCTURE:

1. REVENUE MODEL BREAKDOWN (420-480 seconds):
"So let's look at how these companies actually make money beyond just [obvious revenue source]."

Number each revenue stream clearly:
"First... Second... Third... And finally..."

For each revenue stream:
- Specific percentages and dollar amounts
- Real company examples
- Shocking statistics about frequency
- Connect back to psychological principles

2. CONCRETE EXAMPLE WALKTHROUGH (480-540 seconds):
"So now let's look at buying a [specific expensive product everyone knows] for $[amount]."

Present exactly 3 options with specific numbers:
"When you reach the checkout page, you have three options..."
- Option 1: [full payment with benefits/simplicity]
- Option 2: [traditional credit with specific APR and total cost calculation]  
- Option 3: [new method with installment breakdown]

"Which sounds like the best deal to you?"

3. REAL VICTIM TESTIMONIALS (540-570 seconds):
Include direct quotes from real users:
"[Specific quote showing the real impact]"

Connect to broader patterns:
"This isn't necessarily a bad deal because... But to do so requires financial education. And sadly, [shocking statistic about financial literacy]."

4. EXTREME EXAMPLES (570-600 seconds):
Show the most absurd applications:
"A crazy story we recently saw is that [company] is now on [platform], which allows you to finance your $[small amount] [everyday item] over [number] payments..."

Explain loan stacking with specific statistics:
"In [year], [percentage] of [users] had more than one loan going at one time."

TOPIC INPUT:
Key Examples: {key_examples}

BUSINESS REQUIREMENTS:
- Include specific revenue percentages
- Show real calculation examples
- Use direct quotes from users
- Escalate to most extreme examples
- Connect business model to psychology
- Include demographic targeting data

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema of JSON:

{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "So let's look at how these companies actually make money..."}},
        {{"speaker": "NARRATOR", "line": "So now let's look at buying a..."}},
        {{"speaker": "NARRATOR", "line": "[Include real user quote]"}},
        {{"speaker": "NARRATOR", "line": "A crazy story we recently saw..."}}
    ]
}}

TARGET: 3 minutes exposing business model with specific numbers and examples.
When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}
"""

prompt_business_payoff = """
PAYOFF & PROTECTION ADVICE - Final 1 Minute

You are providing the satisfying conclusion that connects everything back and empowers viewers with protection strategies.

REQUIRED STRUCTURE:

1. BALANCED ACKNOWLEDGMENT (540-550 seconds):
"Again, don't get me wrong, there are definitely some advantages to the system if you know how to play it. But the vast majority of people using the system are not taking advantage of it. They are just getting taken advantage of."

2. ACTIONABLE PROTECTION ADVICE (550-580 seconds):
"So what do you do as a consumer?"

Provide clear, absolute rules:
- "The most important piece of advice: never spend more than you currently have"
- "If you don't have the cash in your bank, don't spend it"
- Include one conditional tip for advanced users

3. CALLBACK CONCLUSION (580-600 seconds):
"But there you have it, the truth about [topic]. These companies spend millions of dollars on psychological research to get you to spend more than you can actually afford. But now you know a little bit more about how to protect yourself."

End with content tease:
"And if you like this video, make sure to check out this video that covers [related business psychology topic]..."

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}

PAYOFF REQUIREMENTS:
- Balance acknowledgment of legitimate uses
- Provide absolute, memorable rules
- Connect back to opening hook
- End with empowerment and protection
- Tease related content for retention

INSTRUCTIONS:
1. First, use WebSearch to find current business examples and trends
2. Think through the viral topic formula to create your topic
3. Finally, use the ReturnJSON tool with your complete topic in this exact schema of JSON:

{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "[Balanced acknowledgment]"}},
        {{"speaker": "NARRATOR", "line": "[Actionable protection advice]"}},
        {{"speaker": "NARRATOR", "line": "[Callback conclusion with tease]"}}
    ]
}}

TARGET: 1 minute of practical advice and satisfying conclusion.

When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}
"""



output_guide = """
When you are ready to provide the final output:
1. Use the `ReturnJSON` tool with your complete JSON
2. After the tool returns the result, provide a Final Answer with the returned JSON

Example format:
Thought: I have all the information needed to create the mystery setup.
Action: ReturnJSON  
Action Input: {{your_json_here}}
Observation: {{tool_result}}
Thought: Perfect! I have the complete story structure.
Final Answer: {{the_json_result}}

The json final result has to be
-  must be valid JSON.
- Use double quotes for all keys and string values.
- Escape any internal quotes inside lines (e.g., use \" inside text).
- Do not include trailing commas or comments.
"""
legal_safe_guard = """
CRITICAL LEGAL SAFEGUARDS - READ FIRST
MANDATORY DISCLAIMER: All prompts below MUST include these legal protections:
FACT-CHECKING REQUIREMENTS:

ALL statistics must be from verifiable, recent sources (within 2 years)
Include source attribution: "According to [Source Name] in [Year]..."
Use phrases like "reportedly," "according to studies," "data suggests"
NEVER present estimates or projections as absolute facts

COMPANY REFERENCE RULES:

Use "companies like [Name]" instead of direct accusations
Focus on industry practices, not specific company wrongdoing
Use phrases like "some companies," "certain platforms," "industry reports suggest"
When naming companies, only reference publicly available, documented practices
Avoid making moral or legal accusations to any specific company 

LEGALLY SAFE LANGUAGE:

Replace "manipulation" with "persuasion techniques" or "influence strategies"
Use "designed to encourage" instead of "designed to trick"
Say "may lead to" instead of "causes"
Include "allegedly" or "reportedly" for unverified claims



"""




business_story_ideas4 = """
You are a content strategist for a YouTube channel that tells engaging, sponsor-friendly stories about business, psychology, and culture. 
Your job is to find surprising but reliable facts, trends, or business practices that audiences will find fascinating. 
The focus is NOT exposing or accusing companies, but instead highlighting interesting, research-backed insights.

TOPIC FORMULA:
- The Surprise: A fact, practice, or trend that seems unexpected or counterintuitive
- The Curiosity: Why this exists and what it reveals about psychology, culture, or business
- The Storytelling Angle: How to explain it through engaging narrative, real examples, and sourced research

TOPIC REQUIREMENTS:
✅ Must be fact-based and verifiable through reliable sources (news, research papers, company reports)
✅ Must feel relatable and spark curiosity
✅ Should avoid conspiracy tones, illegal claims, or unverified accusations
✅ Must be brand-safe and advertiser-friendly
✅ Use the Web search tool for any inspirations or fact checks
EXAMPLES:
- Why LEGO almost went bankrupt before becoming the world’s #1 toy brand
- How Starbucks accidentally created a secret menu
- Why some countries prefer cashless payments while others resist
- The psychology behind why we love limited-edition products
- Why Japan has vending machines for everything

OUTPUT FORMAT:
Return topics in this JSON format:
{{
    "topic_title": "Clear, engaging title",
    "hook_angle": "Opening idea that sparks curiosity",
    "central_mystery": "The surprising question at the heart of this topic",
    "key_examples": ["Example 1", "Example 2", "Example 3"],
    "reliable_sources": ["Source 1", "Source 2", "Source 3"],
    "why_it_works": "Why this story is engaging, relatable, and sponsor safe"
}}


"""
prompt_business_hook4 = """
VIRAL HOOK BUILDER - First 60 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
The goal is to spark curiosity immediately without being accusatory. Always keep tone engaging, conversational, and fact-driven. 

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}):
1. SHOCKING FACT: "Did you know [surprising fact]?" (cite reliable source)
2. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]" 
3. RELATABLE EXPERIENCE: "You’ve probably noticed [everyday example], but here’s the story behind it"
4. MICRO-STORY: A short, real-world anecdote that instantly draws people in

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline (e.g. “According to the BBC in 2024…”)
- End with a natural cliffhanger that transitions into the deeper story
- Tone: curious, not critical; sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question..."}}
    ]
}}
"""
prompt_business_mystery4 = """
MYSTERY BUILDER - Minutes 1-3

You are setting up the context that keeps viewers engaged. 
Instead of making companies look manipulative, focus on the surprising history and evolution of the practice.

STRUCTURE:
1. ORIGIN STORY: "This isn’t new. In fact, [current practice] actually started with [historical example]."
2. TRANSFORMATION: "Over time, it evolved into [modern practice], especially when [specific change happened]."
3. WHY IT MATTERS NOW: "Today, [companies/industries] use it in fascinating ways."

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}

REQUIREMENTS:
- Name real historical and modern examples
- Include at least one reliable data point with source
- Keep tone neutral, curious, and sponsor-friendly
- Build anticipation for the psychology or cultural explanation

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Historical context..."}},
        {{"speaker": "NARRATOR", "line": "Modern transformation..."}},
        {{"speaker": "NARRATOR", "line": "Why it matters today..."}}
    ]
}}
"""
prompt_business_psychology4 = """
PSYCHOLOGY INSIGHTS - Minutes 3-6

You are explaining the psychology behind the story. 
Tone should be educational, light, and accessible — not too academic, not accusatory. 
Think: "fun fact with science behind it."

STRUCTURE:
1. CENTRAL QUESTION: "But why does this work? The answer lies in psychology."
2. PSYCHOLOGICAL PRINCIPLES: Explain 2–3 principles that make this practice effective
   - Give scientific name AND simple explanation
   - Relate to everyday life ("Have you ever noticed when you…?")
   - Back with at least one reliable source
3. APPLICATION: Show how companies, cultures, or people use these principles in practice

TOPIC INPUT:
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up central question..."}},
        {{"speaker": "NARRATOR", "line": "Explain principle 1 with example + source..."}},
        {{"speaker": "NARRATOR", "line": "Explain principle 2 with example + source..."}},
        {{"speaker": "NARRATOR", "line": "Show how it applies in real life..."}}
    ]
}}
"""
prompt_business_application4 = """
APPLICATION & EXAMPLES - Minutes 6-8

You are showing how this practice works in the real world. 
Tone should be engaging, fact-driven, and sponsor-friendly.

STRUCTURE:
1. REAL EXAMPLES: Show 2–3 companies or industries that use this (include sources)
2. NUMBERS THAT WOW: Share a few data points (growth, usage, revenue) with citations
3. EVERYDAY IMPACT: Relate it back to viewers’ daily lives ("You’ve probably seen this when...")

TOPIC INPUT:
Key Examples: {key_examples}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Company example with source..."}},
        {{"speaker": "NARRATOR", "line": "Impressive number or trend with source..."}},
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact..."}}
    ]
}}
"""
prompt_business_payoff4 = """
CLOSING PAYOFF - Final 1 Minute

You are wrapping up the story in a way that feels satisfying, light, and sponsor-friendly. 
No warnings, no fear — just a fun conclusion and a gentle takeaway.

STRUCTURE:
1. RECAP: Briefly restate the central question and answer
2. TAKEAWAY: Share one interesting or empowering insight
3. CONTENT TEASE: Suggest a related video for the viewer to keep watching

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Brief recap of central story..."}},
        {{"speaker": "NARRATOR", "line": "Takeaway insight..."}},
        {{"speaker": "NARRATOR", "line": "Tease related content..."}}
    ]
}}
"""




""" business_story_ideas4 += output_guide
prompt_business_hook4 += legal_safe_guard + output_guide
prompt_business_mystery4 += legal_safe_guard + output_guide
prompt_business_psychology4 += legal_safe_guard + output_guide
prompt_business_application4 += legal_safe_guard + output_guide
prompt_business_payoff4 += legal_safe_guard + output_guide
 """


################################################# 5th
prompt_business_hook5 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
The goal is to spark curiosity immediately without being accusatory. Always keep tone engaging, conversational, and fact-driven. 

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}):
1. SHOCKING FACT: "Did you know [surprising fact]?" (cite reliable source)
2. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]" 
3. RELATABLE EXPERIENCE: "You’ve probably noticed [everyday example], but here’s the story behind it"
4. MICRO-STORY: A short, real-world anecdote that instantly draws people in

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline (e.g. “According to the BBC in 2024…”)
- End with a natural cliffhanger that transitions into the deeper story
- Expand the hook to include curiosity-building questions or mini-anecdotes
- Tone: curious, not critical; sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line..."}} ,
        {{"speaker": "NARRATOR", "line": "Supporting fact with source..."}} ,
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}} ,
        {{"speaker": "NARRATOR", "line": "Transition into central question..."}} 
    ]
}}
"""

prompt_business_mystery5 = """
MYSTERY BUILDER - Minutes 1-3

You are setting up the context that keeps viewers engaged. 
Instead of making companies look manipulative, focus on the surprising history and evolution of the practice.

STRUCTURE:
1. ORIGIN STORY: "This isn’t new. In fact, [current practice] actually started with [historical example]."
2. TRANSFORMATION: "Over time, it evolved into [modern practice], especially when [specific change happened]."
3. MODERN EXAMPLES: Expand to 3–4 examples for depth
4. WHY IT MATTERS NOW: "Today, [companies/industries] use it in fascinating ways."

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}

REQUIREMENTS:
- Name real historical and modern examples
- Include at least two reliable data points with sources
- Expand storytelling with mini-stories or anecdotes
- Keep tone neutral, curious, and sponsor-friendly
- Build anticipation for the psychology or cultural explanation

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Historical context with story..."}} ,
        {{"speaker": "NARRATOR", "line": "Transformation over time..."}} ,
        {{"speaker": "NARRATOR", "line": "Extra modern example for depth..."}} ,
        {{"speaker": "NARRATOR", "line": "Why it matters today..."}} 
    ]
}}
"""
prompt_business_psychology5 = """
PSYCHOLOGY INSIGHTS - Minutes 3-6

You are explaining the psychology behind the story. 
Tone should be educational, light, and accessible — not too academic, not accusatory. 
Think: "fun fact with science behind it."

STRUCTURE:
1. CENTRAL QUESTION: "But why does this work? The answer lies in psychology."
2. PSYCHOLOGICAL PRINCIPLES: Explain 3–4 principles that make this practice effective
   - Give scientific name AND simple explanation
   - Relate to everyday life ("Have you ever noticed when you…?")
   - Back with at least one reliable source each
3. ADDITIONAL MINI-CASE: Add a small, relatable story per principle to lengthen narrative
4. APPLICATION: Show how companies or people use these principles in practice

TOPIC INPUT:
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up central question..."}} ,
        {{"speaker": "NARRATOR", "line": "Explain principle 1 with example + source..."}} ,
        {{"speaker": "NARRATOR", "line": "Explain principle 2 with example + source..."}} ,
        {{"speaker": "NARRATOR", "line": "Explain principle 3 with example + source..."}} ,
        {{"speaker": "NARRATOR", "line": "Additional mini-case/example to illustrate effect..."}} ,
        {{"speaker": "NARRATOR", "line": "Show how it applies in real life..."}} 
    ]
}}
"""
prompt_business_application5 = """
APPLICATION & EXAMPLES - Minutes 6-8

You are showing how this practice works in the real world. 
Tone should be engaging, fact-driven, and sponsor-friendly.

STRUCTURE:
1. REAL EXAMPLES: Show 3–4 companies or industries that use this (include sources)
2. NUMBERS THAT WOW: Share multiple data points (growth, usage, revenue) with citations
3. MINI-STORY: Include a short story showing daily life impact
4. EVERYDAY IMPACT: Relate it back to viewers’ daily experiences ("You’ve probably seen this when...")

TOPIC INPUT:
Key Examples: {key_examples}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Company example with source..."}} ,
        {{"speaker": "NARRATOR", "line": "Impressive number or trend with source..."}} ,
        {{"speaker": "NARRATOR", "line": "Extra real-world example for depth..."}} ,
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact..."}} 
    ]
}}
"""
prompt_business_insight5 = """
CULTURAL OR INDUSTRY INSIGHT - Optional Section

This section explores a surprising, interesting, or counterintuitive angle about the industry, history, or societal impact.
Tone: engaging, sponsor-safe, slightly “mind-blowing” to keep retention high.

STRUCTURE:
1. SURPRISING CONNECTION: Show how the topic relates to culture, tech, or daily life
2. MINI-CASE OR STORY: Share a small story that’s memorable
3. IMPLICATION: What this means for viewers or the future

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Surprising cultural or industry connection..."}} ,
        {{"speaker": "NARRATOR", "line": "Mini-case/story that illustrates it..."}} ,
        {{"speaker": "NARRATOR", "line": "Implication for viewers or future..."}} 
    ]
}}
"""
prompt_business_payoff5 = """
CLOSING PAYOFF - Final 1 Minute

You are wrapping up the story in a way that feels satisfying, light, and sponsor-friendly. 
No warnings, no fear — just a fun conclusion and a gentle takeaway.

STRUCTURE:
1. RECAP: Briefly restate the central question and answer
2. TAKEAWAY: Share one interesting or empowering insight
3. CONTENT TEASE: Suggest a related video or next step for the viewer
4. CALL TO ACTION (optional): Invite engagement in a soft way

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Brief recap of central story..."}} ,
        {{"speaker": "NARRATOR", "line": "Takeaway insight..."}} ,
        {{"speaker": "NARRATOR", "line": "Tease related content..."}} ,
        {{"speaker": "NARRATOR", "line": "Optional soft call to action..."}} 
    ]
}}
"""

#####################################################7th
prompt_business_hook7 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}):
1. SHOCKING FACT: "Did you know [surprising fact]?" (cite source)
2. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]" 
3. RELATABLE EXPERIENCE: "You’ve probably noticed [everyday example], but here’s the story behind it"
4. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue..."}}
    ]
}}
"""
prompt_business_mystery7 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context, Do not fully recount the historical origins; just hint at them briefly or cite one example, save the detailed history for the HISTORICAL DEEP DIVE section...."}}
    ]
}}
"""
prompt_business_history7 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant and surprising.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section..."}}
    ]
}}
"""
prompt_business_revelation = """
# DEEP DIVE & REVELATION

ROLE: You are a master storyteller and investigative journalist.

GOAL: To uncover and explain the single most surprising and powerful "Aha!" moment behind the video's central mystery. This is the core payoff for the viewer. Do not just list facts; build a case and deliver a memorable revelation.

--- NARRATIVE STRUCTURE ---

1.  **THE TRANSITION & SETUP:** Create a smooth transition from the history section and pose a guiding question. (e.g., "But before we get into the psychology, we need to understand how these stores *actually* make their money...")

2.  **THE MISCONCEPTION:** State the common, but incorrect, assumption. (e.g., "Most of us would think that grocery stores make their money by selling products...")

3.  **THE CORE REVELATION (The "Aha!" Moment):** Deliver the single most shocking and counterintuitive truth. This is the central thesis of the video. It is not necessarily a psychological principle; it could be a financial model, a logistical strategy, or a historical quirk. (e.g., "But they already know that. That's why grocery stores are not in the food business. In fact, they're in the real estate business.")

4.  **THE EVIDENCE (The "How It Works"):** Systematically present the evidence to prove the Core Revelation. This is where you explain the mechanics. Use a "montage" of 3-4 key "tricks" or "mechanisms."
    -   **Trick #1:** Explain the first mechanism (e.g., The "front of shop" produce section).
    -   **Trick #2:** Explain the second mechanism (e.g., The "traffic builder" milk at the back).
    -   **Trick #3:** Explain the third, and most important, mechanism (e.g., "Slotting fees" and the "Golden Zone").

5.  **THE CONCLUSION & TRANSITION:** Summarize the revelation and transition to the broader implications or modern applications.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Full Script So Far: {full_script}

--- REQUIREMENTS ---
- **Find the REAL story:** Your primary job is to find the most compelling explanation, whether it's psychological, financial, or logistical. Do not be constrained to only psychology.
- **Build to a Climax:** Structure your explanation so that the most powerful piece of evidence (like the "slotting fees") is revealed last for maximum impact.
- **Use Vivid, Memorable Concepts:** Instead of abstract principles, use concrete, "sticky" ideas (e.g., "The Golden Zone").
- **Maintain a Storytelling Tone:** This is not an academic explanation; it is the solving of a mystery.
- **CRITICAL REQUIREMENT FOR NOVELTY:** This entire section must be new, revelatory information.

"""


prompt_business_application7 = """
MODERN APPLICATIONS & CASE STUDIES - Minutes 8-11

Show how this works in today’s world with multiple examples.

STRUCTURE:
1. INDUSTRY LEADER: Case study of major company
2. SURPRISING SECTOR: Unexpected industry example
3. STARTUP SUCCESS: Newer company leveraging strategy
4. GLOBAL PERSPECTIVE: Cultural/regional variations
5. NUMBERS THAT MATTER: Key metrics and growth

TOPIC INPUT:
Key Examples: {key_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include 4–5 company examples with sources
- Use specific metrics (growth %, usage, revenue)
- Generate 8–10 dialogue lines
- Expand each line to 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Industry leader case study with results..."}},
        {{"speaker": "NARRATOR", "line": "Specific metrics and numbers..."}},
        {{"speaker": "NARRATOR", "line": "Surprising sector example..."}},
        {{"speaker": "NARRATOR", "line": "Startup success story..."}},
        {{"speaker": "NARRATOR", "line": "Global/cultural variation explained..."}},
        {{"speaker": "NARRATOR", "line": "Compilation of key statistics..."}},
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact for viewers..."}},
        {{"speaker": "NARRATOR", "line": "Transition to insights/implications..."}}
    ]
}}
"""
prompt_business_payoff7 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}
Here are whats written before you: {full_script}


REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content..."}}
    ]
}}
"""


prompt_business_insight7 = """
CULTURAL OR INDUSTRY INSIGHT - Optional Section

Explore a surprising or counterintuitive angle to maintain attention.

STRUCTURE:
1. SURPRISING CONNECTION: How topic relates to culture, tech, or daily life
2. MINI-CASE OR STORY: Memorable anecdote
3. IMPLICATION: Meaning for viewers or future trends

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Generate 3 dialogue lines, each expanded to 2–3 sentences
- Keep tone engaging and sponsor-safe
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Surprising cultural or industry connection..."}},
        {{"speaker": "NARRATOR", "line": "Mini-case/story illustrating it..."}},
        {{"speaker": "NARRATOR", "line": "Implication for viewers/future..."}}
    ]
}}
"""

########################################################8th (Extended length from 7th)

prompt_business_hook8 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}):
1. SHOCKING FACT: "Did you know [surprising fact]?" (cite source)
2. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]" 
3. RELATABLE EXPERIENCE: "You’ve probably noticed [everyday example], but here’s the story behind it"
4. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Include a micro-story or anecdote for extra engagement
- Insert 1–2 curiosity hooks mid-story
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity and anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context including curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue and teaser..."}}
    ]
}}
"""
prompt_business_mystery8 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}

REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Add mini-stories or anecdotes for each example
- Insert micro-transitions for time jumps or context
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation with mini-story..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source and anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source, curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context and micro-transition..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained with intrigue..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context with teaser..."}}
    ]
}}
"""
prompt_business_history8 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant, surprising, and connected to modern examples.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates, anecdotes, and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- Add mini-stories or anecdotes to illustrate each point
- Insert curiosity hooks mid-history for engagement
- Generate 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Include subtle transitions to modern psychology

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics, micro-anecdote, and curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained with mini-story..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step with date, source, and anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step expanded with micro-transition..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment with context and intrigue..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples and teaser into psychology section..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section with curiosity hook..."}}
    ]
}}
"""
prompt_business_psychology8 = """
PSYCHOLOGY DEEP DIVE - Minutes 5-8

Explain psychological principles in depth with multiple examples.
Make science accessible, relatable, and tied to historical and modern cases.

STRUCTURE:
1. CENTRAL QUESTION: "Why does this work so effectively? It involves multiple psychological principles."
2. PRINCIPLE 1: Explanation + 2 real-world examples
3. PRINCIPLE 2: Different angle with studies + everyday applications
4. PRINCIPLE 3: Surprising research + implications
5. INTERACTION: "When these principles combine, the effect is amplified..."

TOPIC INPUT:
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}

REQUIREMENTS:
- Cover 3 distinct psychological principles
- Include at least 3 scientific sources
- Reference historical and modern company examples where relevant
- Generate 8–10 dialogue lines
- Expand each line to 2–3 sentences
- Use analogies viewers can relate to
- Insert curiosity hooks/questions for audience engagement

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up central question with teaser linking to history..."}},
        {{"speaker": "NARRATOR", "line": "Principle 1 introduction with science, example, and micro-story..."}},
        {{"speaker": "NARRATOR", "line": "Principle 1 additional context and curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Principle 2 explanation with research and real-world tie-in..."}},
        {{"speaker": "NARRATOR", "line": "Principle 2 everyday application with anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Principle 3 with surprising findings, source, and example..."}},
        {{"speaker": "NARRATOR", "line": "Interaction of principles explained with micro-transition..."}},
        {{"speaker": "NARRATOR", "line": "Transition to modern applications with curiosity hook..."}}
    ]
}}
"""
prompt_business_application8 = """
MODERN APPLICATIONS & CASE STUDIES - Minutes 8-11

Show how this works in today’s world with multiple examples.
Include mini-stories, metrics, and audience-facing questions for engagement.

STRUCTURE:
1. INDUSTRY LEADER: Case study of major company
2. SURPRISING SECTOR: Unexpected industry example
3. STARTUP SUCCESS: Newer company leveraging strategy
4. GLOBAL PERSPECTIVE: Cultural/regional variations
5. NUMBERS THAT MATTER: Key metrics and growth

TOPIC INPUT:
Key Examples: {key_examples}


REQUIREMENTS:
- Include 4–5 company examples with sources
- Add anecdotes or mini-stories for each
- Use specific metrics (growth %, usage, revenue)
- Include curiosity hooks and questions for audience
- Generate 8–10 dialogue lines
- Expand each line to 2–3 sentences

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Industry leader case study with results and mini-story..."}},
        {{"speaker": "NARRATOR", "line": "Specific metrics and numbers with curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Surprising sector example with anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Startup success story with engagement question..."}},
        {{"speaker": "NARRATOR", "line": "Global/cultural variation explained with micro-transition..."}},
        {{"speaker": "NARRATOR", "line": "Compilation of key statistics with viewer relevance..."}},
        {{"speaker": "NARRATOR", "line": "Relatable everyday impact for viewers..."}},
        {{"speaker": "NARRATOR", "line": "Transition to insights/implications with curiosity hook..."}}
    ]
}}
"""
prompt_business_insight8 = """
CULTURAL OR INDUSTRY INSIGHT - Optional Section

Explore a surprising or counterintuitive angle to maintain attention.
Include micro-stories and curiosity hooks.

STRUCTURE:
1. SURPRISING CONNECTION: How topic relates to culture, tech, or daily life
2. MINI-CASE OR STORY: Memorable anecdote
3. IMPLICATION: Meaning for viewers or future trends

TOPIC INPUT:
Topic Title: {topic_title}
Why It Works: {why_it_works}

REQUIREMENTS:
- Generate 3 dialogue lines, each expanded to 2–3 sentences
- Include curiosity hooks and mini-stories
- Keep tone engaging and sponsor-safe

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Surprising cultural or industry connection with anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Mini-case/story illustrating it with curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Implication for viewers/future with teaser..."}}
    ]
}}
"""
prompt_business_payoff8 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.
Use audience-facing questions and small stories for impact.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}

REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Insert micro-stories or examples to reinforce points
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap with mini-story..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice with curiosity hook..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development example..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message with anecdote..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection with micro-transition..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content with teaser..."}}
    ]
}}
"""


##############################################  9th ########################(7th but eliminate data dump)

business_psych_ideas = """
You are a viral content strategist specializing in finding business psychology topics that will captivate YouTube audiences. 
Your job is to identify surprising, counterintuitive business decisions that seem illogical but reveal fascinating psychological strategies.

VIRAL TOPIC FORMULA:
The Contradiction: Highlight business practices that appear strange, wasteful, or counterproductive at first glance
The Mystery: Explain why successful companies continue doing these practices
The Psychology: Reveal the psychological principles and design trade-offs behind these decisions

TOPIC CATEGORIES THAT GO VIRAL:
Tech Company Paradoxes:
- Why Apple removes features people love
- How Google makes money from "free" products
- Why social media apps add wellness reminders after making themselves addictive

Streaming/Entertainment Psychology:
- Why Netflix cancels popular shows
- How Disney creates artificial scarcity with "vault" releases
- Why TikTok shows you content from accounts you don't follow

Retail Design & Pricing Psychology:
- Why stores place expensive items at eye level
- How subscription services make canceling difficult
- Why "limited time offers" often reappear

Corporate Strategy & Behavior:
- Why companies create extra service tiers that few people buy
- How brands use fear of missing out (FOMO)
- Why customer service can feel intentionally complex

WHAT MAKES A TOPIC VIRAL:
Relatability: Everyone has experienced this but never thought about why
Counterintuitive: Goes against common sense or expectations
Specific Examples: Can name real companies and situations
Pattern Recognition: Once explained, viewers start noticing it everywhere
Emotional Response: Makes people feel curious and enlightened

TOPIC GENERATION PROCESS:
Step 1: Identify the Paradox
Find a well-known business practice that seems odd or counterintuitive:
"Why does [Company] do [Thing] when it seems like it would hurt [Expected Outcome]?"

Step 2: Validate the Mystery
Ensure the topic has:
- Multiple specific, named examples from different companies
- A clear contradiction between expectation and reality
- Evidence that the practice has business benefits despite seeming strange

Step 3: Confirm Psychological Depth
The explanation should involve:
- At least 2-3 psychological principles/biases
- Both strategic intent and consumer response
- Broader implications beyond just one company

Step 4: Test Viral Potential
Ask:
- Would this make someone say "I never thought about it that way"?
- Can viewers recall their own experiences with this?
- Does this reveal a repeatable pattern?

HIGH-PERFORMING TOPIC FORMATS:
"Why [Company] Does [Counterintuitive Thing]"
"The Psychology Behind [Business Practice]"
"How [Industry] Influences Your Decisions"

CURRENT TRENDING TOPICS TO EXPLORE:
Post-Pandemic Business Changes:
- Why remote-first companies call people back to the office
- How subscription services exploded during lockdown
- Why delivery apps feel more expensive than ever

AI and Tech Disruption:
- Why companies claim AI will replace jobs but still hire
- How social media algorithms decide what goes viral
- Why tech companies offer free AI tools

Economic Psychology:
- Why companies prefer shrinkflation over raising prices
- Why luxury brands increase prices in recessions
- How "anchoring" makes discounts feel bigger than they are

TOPIC VALIDATION CHECKLIST:
✅ Specific, real examples
✅ Counterintuitive but explainable
✅ Relatable to broad audiences
✅ Backed by real psychology research
✅ Pattern people can recognize in daily life
✅ Emotional hook without being accusatory
✅ Relevant to modern businesses

AVOID:
- Conspiracy theories
- Illegal/clearly unethical practices
- One-off company scandals
- Overexposed or obvious strategies

SUCCESS METRICS:
High Viral Potential (8-10): Multiple companies use the same psychological strategy, with clear contradiction + "aha moment"
Medium (6-7): Good psychology, but niche or less relatable
Low (1-5): Obvious or too narrow

GOAL: Generate topics that make viewers think "I never realized businesses use psychology in this way, and now I notice it everywhere."

Your response must be in this JSON format, no single quotes only double quotes:
{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "hook_angle": "Opening line that sparks curiosity",
    "central_mystery": "Why would successful companies do this seemingly odd thing?",
    "key_examples": ["Specific Example 1", "Specific Example 2", "Specific Example 3"],
    "psychological_principles": ["Psychology Principle 1", "Psychology Principle 2", "Psychology Principle 3"],
    "viral_potential_score": 9,
    "why_it_works": "Why this topic will go viral - surprising, relatable, and sponsor-safe"
}
"""


prompt_business_hook9 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}):
1. SHOCKING FACT: "Did you know [surprising fact]?" (cite source)
2. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]" 
3. RELATABLE EXPERIENCE: "You’ve probably noticed [everyday example], but here’s the story behind it"
4. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in

TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue..."}}
    ]
}}
"""
prompt_business_mystery9 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}


REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive
- CRITICAL REQUIREMENT FOR NOVELTY: Each section you generate must introduce NEW information, a NEW perspective, or a NEW layer of depth. Scrutinize the {full_script} input. Do not repeat core definitions, statistics, or explanations already established in previous sections. Your primary job is to ADVANCE the narrative, not summarize it.

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context, Do not fully recount the historical origins; just hint at them briefly or cite one example, save the detailed history for the HISTORICAL DEEP DIVE section...."}}
    ]
}}
"""
prompt_business_history9 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant and surprising.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Make good connections to the previous points in the sciprt
- CRITICAL REQUIREMENT FOR NOVELTY: Each section you generate must introduce NEW information, a NEW perspective, or a NEW layer of depth. Scrutinize the {full_script} input. Do not repeat core definitions, statistics, or explanations already established in previous sections. Your primary job is to ADVANCE the narrative, not summarize it.
- For each historical point, briefly connect it to an experience the viewer has in a store today (e.g., "This 'Golden Rule' layout is why you still have to walk the entire store perimeter...").
OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section..."}}
    ]
}}
"""
prompt_business_psychology9 = """
PSYCHOLOGY DEEP DIVE

GOAL: Explain complex psychological principles in an accessible, engaging, and non-repetitive way. Make the science relatable by using a diverse set of examples.

STRUCTURE:
1. CENTRAL QUESTION: "Why does this work so effectively? It involves multiple psychological principles."
2. PRINCIPLE 1: Explanation + a clear example directly related to the video's main topic ({topic_title}).
3. PRINCIPLE 2: Explanation + an analogous example from a completely different and unexpected domain.
4. PRINCIPLE 3: Explanation + a relatable example from a common, personal, everyday-life experience.
5. INTERACTION: "When these principles combine, the effect is amplified..."

TOPIC INPUT:
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}


REQUIREMENTS:
- Cover 3 distinct psychological principles.
- **CRITICAL REQUIREMENT FOR DIVERSITY:** To prevent repetition, you MUST use a variety of examples. The first example should connect to the main topic ({topic_title}). The subsequent examples for the other principles MUST be from different, unrelated contexts (e.g., if the topic is business, use an analogy from sports, art, or social dynamics). This demonstrates the universality of the principles.
- Include scientific sources where appropriate.
- Generate 8–10 dialogue lines, expanding each line for natural pacing.
- Use analogies and simple language to make complex ideas clear.
- Ensure the final transition smoothly connects these diverse principles back to the video's main topic.
- CRITICAL REQUIREMENT FOR NOVELTY: Each section you generate must introduce NEW information, a NEW perspective, or a NEW layer of depth. Scrutinize the {full_script} input. Do not repeat core definitions, statistics, or explanations already established in previous sections. Your primary job is to ADVANCE the narrative, not summarize it.

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up the central question about why this works..."}},
        {{"speaker": "NARRATOR", "line": "Principle 1 explained with a TOPIC-SPECIFIC example..."}},
        {{"speaker": "NARRATOR", "line": "Principle 2 explained with an ANALOGOUS example from a different domain..."}},
        {{"speaker": "NARRATOR", "line": "Principle 3 explained with a PERSONAL/EVERYDAY LIFE example..."}},
        {{"speaker": "NARRATOR", "line": "Explanation of how these principles interact and amplify each other..."}},
        {{"speaker": "NARRATOR", "line": "Transition that ties these universal principles back to the core subject of the video..."}}
    ]
}}
"""
prompt_business_application9 = """
EXTENSION & MODERN BATTLEFIELD - Minutes 8-11

Show how these psychological principles extend beyond the grocery store and into other areas of the viewer's life. Frame it as an evolution of these techniques.

STRUCTURE:
1. THE CORE IDEA REVISITED: "So it's not just about milk. This is about controlling your path to influence your decisions."
2. THE DIGITAL AISLE: "Now, think about how this works online..." (e.g., website layouts, infinite scroll, Amazon's 'Customers also bought').
3. BEYOND RETAIL: "You'll even see this where you least expect it..." (e.g., social media feed design, video game level layouts, theme park queues).
4. THE FUTURE OF INFLUENCE: "And it's getting even more sophisticated..." (e.g., AI personalizing store layouts in real-time, digital ads changing as you walk).

TOPIC INPUT:
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}

REQUIREMENTS:
- Directly connect each example back to the core psychological principles (Gruen Transfer, Mere Exposure, etc.).
- Use 3-4 relatable examples from digital life and physical spaces.
- Maintain a tone of discovery and empowerment, not just a list of facts.
- Generate 6-8 dialogue lines.
- Expand each line to 2-3 sentences.
- Ensure the focus remains on the viewer's experience.
- CRITICAL REQUIREMENT FOR NOVELTY: Each section you generate must introduce NEW information, a NEW perspective, or a NEW layer of depth. Scrutinize the {full_script} input. Do not repeat core definitions, statistics, or explanations already established in previous sections. Your primary job is to ADVANCE the narrative, not summarize it.


OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Reiterate the core psychological thesis..."}},
        {{"speaker": "NARRATOR", "line": "Example 1: The Digital Aisle (e.g., e-commerce)..."}},
        {{"speaker": "NARRATOR", "line": "Example 2: The Entertainment Maze (e.g., social media/streaming)..."}},
        {{"speaker": "NARRATOR", "line": "Example 3: Physical World, Non-Retail (e.g., airports, theme parks)..."}},
        {{"speaker": "NARRATOR", "line": "The Future: How AI and data are making this even more personal..."}},
        {{"speaker": "NARRATOR", "line": "Transition to the final payoff and actionable advice..."}}
    ]
}}
"""
prompt_business_implications9 = """
# BUSINESS IMPLICATIONS & STRATEGIC LANDSCAPE (HIGH-RPM MODULE)

ROLE: You are a sharp, insightful business analyst and industry strategist, in the style of ColdFusion or How Money Works.

GOAL: To create a new, high-value section for the script that explores the broader business ecosystem, financial stakes, and competitive landscape surrounding the video's central topic. This section is designed to attract a premium audience of entrepreneurs, marketers, and investors, and to be a magnet for high-RPM advertisers.

--- THE STRUCTURE OF THIS SECTION ---

1.  **THE PIVOT TO STRATEGY:** Begin with a clear transition that zooms out from the psychology to the business world. (e.g., "So we understand the psychology... but the real story is the multi-billion dollar industry built on top of it.")

2.  **THE MONEY BEHIND THE METHOD:** Provide concrete financial data. Discuss the size of the industry, the ROI companies see, and major investments made by key players. This establishes the high stakes.

3.  **THE ARMS RACE (Competitive Landscape):** Present compelling case studies of how different major companies compete using these psychological principles. Contrast the main strategy with a notable alternative (e.g., Apple's "town square" vs. traditional retail).

4.  **THE OPPORTUNITY FOR ENTREPRENEURS:** Directly address the business-minded viewer. Explain how small businesses can apply these principles, highlight any "opportunity gaps" that large companies miss, and explain why this knowledge is a competitive advantage.

5.  **THE FUTURE OF PERSUASION:** Look ahead. Discuss how emerging technologies like AI or VR will shape the future of this psychological strategy and what businesses need to prepare for.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Key Examples: {key_examples}
Full Script So Far: {full_script}

--- REQUIREMENTS ---
- **Target Audience:** Entrepreneurs, small business owners, marketing professionals, e-commerce owners.
- **High-Value Keywords:** Naturally integrate terms like "business strategy," "sales optimization," "customer behavior analytics," "competitive advantage," and "entrepreneurship."
- **Data-Driven:** Include specific (even if estimated) financial figures, percentages, and investment amounts to add credibility and scale.
- **Word Count:** Generate approximately 300-450 words to create a 2-3 minute section.
- **Confident, Analytical Tone:** Write with the authority of a seasoned industry analyst.
- **CRITICAL REQUIREMENT FOR NOVELTY:** This section must introduce new, strategic, and financial perspectives not previously discussed.

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The pivot: From psychology to the billion-dollar business behind it..."}},
        {{"speaker": "NARRATOR", "line": "The money: Hard numbers on the ROI and industry size..."}},
        {{"speaker": "NARRATOR", "line": "The Arms Race: A compelling case study of corporate competition..."}},
        {{"speaker": "NARRATOR", "line": "The Entrepreneur's Edge: Actionable insights for small businesses..."}},
        {{"speaker": "NARRATOR", "line": "The Future: What's next in the evolution of this strategy..."}}
    ]
}}"""
prompt_business_payoff9 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}
Here are whats written before you: {full_script}


REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences
- Make good connections to the previous points in the sciprt

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content..."}}
    ]
}}
"""


################################################# 10th ########### (Add better flow , might need more explaination in psychology section , and )



prompt_business_hook10 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}), Be creative:
1. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]"
2. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in
3. INVERTED EXPECTATION: "Most people believe [X], but the truth is [Y]"
4. HIDDEN COST/BENEFIT: "This tiny overlooked detail is why [company/product] is worth billions"
5. TIME MACHINE: "Back in [year], [X] failed. Today it’s the secret weapon of billion-dollar companies"
6. STAKES HOOK: "This single decision cost companies [X dollars/users]. Why does it keep happening?"


TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue..."}}
    ]
}}
"""
prompt_business_mystery10 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context, Do not fully recount the historical origins; just hint at them briefly or cite one example, save the detailed history for the HISTORICAL DEEP DIVE section...."}}
    ]
}}
"""
prompt_business_history10 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant and surprising.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive
- For each historical point, briefly connect it to an experience the viewer has in a store today (e.g., "This 'Golden Rule' layout is why you still have to walk the entire store perimeter...").
OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section..."}}
    ]
}}
"""
prompt_business_psychology10 = """
PSYCHOLOGY DEEP DIVE

GOAL: Explain complex psychological principles in an accessible, engaging, and non-repetitive way. Make the science relatable by using a diverse set of examples.

STRUCTURE:
1. CENTRAL QUESTION: "Why does this work so effectively? It involves multiple psychological principles."
2. PRINCIPLE 1: Explanation + a clear example directly related to the video's main topic ({topic_title}).
3. PRINCIPLE 2: Explanation + an analogous example from a completely different and unexpected domain.
4. PRINCIPLE 3: Explanation + a relatable example from a common, personal, everyday-life experience.
5. INTERACTION: "When these principles combine, the effect is amplified..."

TOPIC INPUT:
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Cover 3 distinct psychological principles.
- **CRITICAL REQUIREMENT FOR DIVERSITY:** To prevent repetition, you MUST use a variety of examples. The first example should connect to the main topic ({topic_title}). The subsequent examples for the other principles MUST be from different, unrelated contexts (e.g., if the topic is business, use an analogy from sports, art, or social dynamics). This demonstrates the universality of the principles.
- Include scientific sources where appropriate.
- Generate 8–10 dialogue lines, expanding each line for natural pacing.
- Use analogies and simple language to make complex ideas clear.
- Ensure the final transition smoothly connects these diverse principles back to the video's main topic.

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up the central question about why this works..."}},
        {{"speaker": "NARRATOR", "line": "Principle 1 explained with a TOPIC-SPECIFIC example..."}},
        {{"speaker": "NARRATOR", "line": "Principle 2 explained with an ANALOGOUS example from a different domain..."}},
        {{"speaker": "NARRATOR", "line": "Principle 3 explained with a PERSONAL/EVERYDAY LIFE example..."}},
        {{"speaker": "NARRATOR", "line": "Explanation of how these principles interact and amplify each other..."}},
        {{"speaker": "NARRATOR", "line": "Transition that ties these universal principles back to the core subject of the video..."}}
    ]
}}
"""
prompt_business_implications10 = """
# BUSINESS IMPLICATIONS & STRATEGIC LANDSCAPE (HIGH-RPM MODULE)

ROLE: You are a sharp, insightful business analyst and industry strategist, in the style of ColdFusion or How Money Works.

GOAL: To create a new, high-value section for the script that explores the broader business ecosystem, financial stakes, and competitive landscape surrounding the video's central topic. This section is designed to attract a premium audience of entrepreneurs, marketers, and investors, and to be a magnet for high-RPM advertisers.

--- THE STRUCTURE OF THIS SECTION ---

1.  **THE PIVOT TO STRATEGY:** Begin with a clear transition that zooms out from the psychology to the business world. (e.g., "So we understand the psychology... but the real story is the multi-billion dollar industry built on top of it.")

2.  **THE MONEY BEHIND THE METHOD:** Provide concrete financial data. Discuss the size of the industry, the ROI companies see, and major investments made by key players. This establishes the high stakes.

3.  **THE ARMS RACE (Competitive Landscape):** Present compelling case studies of how different major companies compete using these psychological principles. Contrast the main strategy with a notable alternative (e.g., Apple's "town square" vs. traditional retail).

4.  **THE OPPORTUNITY FOR ENTREPRENEURS:** Directly address the business-minded viewer. Explain how small businesses can apply these principles, highlight any "opportunity gaps" that large companies miss, and explain why this knowledge is a competitive advantage.

5.  **THE FUTURE OF PERSUASION:** Look ahead. Discuss how emerging technologies like AI or VR will shape the future of this psychological strategy and what businesses need to prepare for.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Key Examples: {key_examples}
Full Script So Far: {full_script}

--- REQUIREMENTS ---
- **Target Audience:** Entrepreneurs, small business owners, marketing professionals, e-commerce owners.
- **High-Value Keywords:** Naturally integrate terms like "business strategy," "sales optimization," "customer behavior analytics," "competitive advantage," and "entrepreneurship."
- **Data-Driven:** Include specific (even if estimated) financial figures, percentages, and investment amounts to add credibility and scale.
- **Word Count:** Generate approximately 300-450 words to create a 2-3 minute section.
- **Confident, Analytical Tone:** Write with the authority of a seasoned industry analyst.
- **CRITICAL REQUIREMENT FOR NOVELTY:** This section must introduce new, strategic, and financial perspectives not previously discussed.

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The pivot: From psychology to the billion-dollar business behind it..."}},
        {{"speaker": "NARRATOR", "line": "The money: Hard numbers on the ROI and industry size..."}},
        {{"speaker": "NARRATOR", "line": "The Arms Race: A compelling case study of corporate competition..."}},
        {{"speaker": "NARRATOR", "line": "The Entrepreneur's Edge: Actionable insights for small businesses..."}},
        {{"speaker": "NARRATOR", "line": "The Future: What's next in the evolution of this strategy..."}}
    ]
}}"""

prompt_business_payoff10 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}
Here are whats written before you: {full_script}


REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content..."}}
    ]
}}
"""


################################# 10.1 version IDENTICAL TO 10 BUT CHANGED STRUCTURE REPLACED PSYCHOLOGY WITH RELEVATION PROMPT (INSPIRED BY Zoufry) (But keep the name psychology cuz lady to change everythign)



prompt_business_hook101 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}), Be creative:
1. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]"
2. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in
3. INVERTED EXPECTATION: "Most people believe [X], but the truth is [Y]"
4. HIDDEN COST/BENEFIT: "This tiny overlooked detail is why [company/product] is worth billions"
5. TIME MACHINE: "Back in [year], [X] failed. Today it’s the secret weapon of billion-dollar companies"
6. STAKES HOOK: "This single decision cost companies [X dollars/users]. Why does it keep happening?"


TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue..."}}
    ]
}}
"""
prompt_business_mystery101 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context, Do not fully recount the historical origins; just hint at them briefly or cite one example, save the detailed history for the HISTORICAL DEEP DIVE section...."}}
    ]
}}
"""
prompt_business_history101 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant and surprising.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive
- For each historical point, briefly connect it to an experience the viewer has in a store today (e.g., "This 'Golden Rule' layout is why you still have to walk the entire store perimeter...").
OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section..."}}
    ]
}}
"""
prompt_business_psychology101 = """
# DEEP DIVE & REVELATION

ROLE: You are a master storyteller and investigative journalist.

GOAL: To uncover and explain the single most surprising and powerful "Aha!" moment behind the video's central mystery. This is the core payoff for the viewer. Do not just list facts; build a case and deliver a memorable revelation.

--- NARRATIVE STRUCTURE ---

1.  **THE TRANSITION & SETUP:** Create a smooth transition from the history section and pose a guiding question. (e.g., "But before we get into the psychology, we need to understand how these stores *actually* make their money...")

2.  **THE MISCONCEPTION:** State the common, but incorrect, assumption. (e.g., "Most of us would think that grocery stores make their money by selling products...")

3.  **THE CORE REVELATION (The "Aha!" Moment):** Deliver the single most shocking and counterintuitive truth. This is the central thesis of the video. It is not necessarily a psychological principle; it could be a financial model, a logistical strategy, or a historical quirk. (e.g., "But they already know that. That's why grocery stores are not in the food business. In fact, they're in the real estate business.")

4.  **THE EVIDENCE (The "How It Works"):** Systematically present the evidence to prove the Core Revelation. This is where you explain the mechanics. Use a "montage" of 3-4 key "tricks" or "mechanisms."
    -   **Trick #1:** Explain the first mechanism (e.g., The "front of shop" produce section).
    -   **Trick #2:** Explain the second mechanism (e.g., The "traffic builder" milk at the back).
    -   **Trick #3:** Explain the third, and most important, mechanism (e.g., "Slotting fees" and the "Golden Zone").

5.  **THE CONCLUSION & TRANSITION:** Summarize the revelation and transition to the broader implications or modern applications.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Full Script So Far: {full_script}

--- REQUIREMENTS ---
- **Find the REAL story:** Your primary job is to find the most compelling explanation, whether it's psychological, financial, or logistical. Do not be constrained to only psychology.
- **Build to a Climax:** Structure your explanation so that the most powerful piece of evidence (like the "slotting fees") is revealed last for maximum impact.
- **Use Vivid, Memorable Concepts:** Instead of abstract principles, use concrete, "sticky" ideas (e.g., "The Golden Zone").
- **Maintain a Storytelling Tone:** This is not an academic explanation; it is the solving of a mystery.
- **CRITICAL REQUIREMENT FOR NOVELTY:** This entire section must be new, revelatory information."""
prompt_business_implications101 = """
# BUSINESS IMPLICATIONS & STRATEGIC LANDSCAPE (HIGH-RPM MODULE)

ROLE: You are a sharp, insightful business analyst and industry strategist, in the style of ColdFusion or How Money Works.

GOAL: To create a new, high-value section for the script that explores the broader business ecosystem, financial stakes, and competitive landscape surrounding the video's central topic. This section is designed to attract a premium audience of entrepreneurs, marketers, and investors, and to be a magnet for high-RPM advertisers.

--- THE STRUCTURE OF THIS SECTION ---

1.  **THE PIVOT TO STRATEGY:** Begin with a clear transition that zooms out from the psychology to the business world. (e.g., "So we understand the psychology... but the real story is the multi-billion dollar industry built on top of it.")

2.  **THE MONEY BEHIND THE METHOD:** Provide concrete financial data. Discuss the size of the industry, the ROI companies see, and major investments made by key players. This establishes the high stakes.

3.  **THE ARMS RACE (Competitive Landscape):** Present compelling case studies of how different major companies compete using these psychological principles. Contrast the main strategy with a notable alternative (e.g., Apple's "town square" vs. traditional retail).

4.  **THE OPPORTUNITY FOR ENTREPRENEURS:** Directly address the business-minded viewer. Explain how small businesses can apply these principles, highlight any "opportunity gaps" that large companies miss, and explain why this knowledge is a competitive advantage.

5.  **THE FUTURE OF PERSUASION:** Look ahead. Discuss how emerging technologies like AI or VR will shape the future of this psychological strategy and what businesses need to prepare for.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Key Examples: {key_examples}
Full Script So Far: {full_script}

--- REQUIREMENTS ---
- **Target Audience:** Entrepreneurs, small business owners, marketing professionals, e-commerce owners.
- **High-Value Keywords:** Naturally integrate terms like "business strategy," "sales optimization," "customer behavior analytics," "competitive advantage," and "entrepreneurship."
- **Data-Driven:** Include specific (even if estimated) financial figures, percentages, and investment amounts to add credibility and scale.
- **Word Count:** Generate approximately 300-450 words to create a 2-3 minute section.
- **Confident, Analytical Tone:** Write with the authority of a seasoned industry analyst.
- **CRITICAL REQUIREMENT FOR NOVELTY:** This section must introduce new, strategic, and financial perspectives not previously discussed.

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The pivot: From psychology to the billion-dollar business behind it..."}},
        {{"speaker": "NARRATOR", "line": "The money: Hard numbers on the ROI and industry size..."}},
        {{"speaker": "NARRATOR", "line": "The Arms Race: A compelling case study of corporate competition..."}},
        {{"speaker": "NARRATOR", "line": "The Entrepreneur's Edge: Actionable insights for small businesses..."}},
        {{"speaker": "NARRATOR", "line": "The Future: What's next in the evolution of this strategy..."}}
    ]
}}"""

prompt_business_payoff101 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}
Here are whats written before you: {full_script}


REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content..."}}
    ]
}}
"""





########################################## 12 CLEAN SLATE (SIMPLIER, copy creator structure)


business_psych_ideas3 = """
You are a viral content strategist specializing in uncovering counterintuitive business psychology stories for YouTube audiences. 
Your job is to identify surprising, seemingly illogical business decisions that reveal deep psychological strategies and create a single, clear "aha" revelation for storytelling.

VIRAL TOPIC FORMULA:
The Contradiction: Highlight business practices that appear strange, wasteful, or counterproductive at first glance.
The Mystery: Ask why successful companies continue doing these practices.
The Core Revelation: Reveal the counterintuitive truth or hidden strategy that explains why it actually works.
The Psychology: Show the psychological principles, biases, or design trade-offs behind these decisions.

TOPIC CATEGORIES THAT GO VIRAL:
Tech & Platform Paradoxes:
- Why Apple removes features people love
- How Google monetizes "free" products
- Why social apps add wellness reminders after making themselves addictive

Streaming & Entertainment Psychology:
- Why Netflix cancels popular shows
- How Disney creates artificial scarcity with "vault" releases
- Why TikTok shows content from accounts you don’t follow

Retail Design & Pricing Psychology:
- Why stores place expensive items at eye level
- How subscription services make canceling difficult
- Why "limited time offers" often reappear

Corporate Strategy & Behavior:
- Why companies create extra service tiers that few people buy
- How brands exploit FOMO
- Why customer service can feel intentionally complex

WHAT MAKES A TOPIC VIRAL:
Relatability: Everyone has experienced this but never thought about why.
Counterintuitive: Goes against common sense or expectations.
Specific Examples: Real companies and situations.
Pattern Recognition: Viewers see the pattern everywhere once explained.
Emotional Response: Curiosity, surprise, and enlightenment.
Single Revelation: There should be one clear, story-ready insight around which the script can be built.

TOPIC GENERATION PROCESS:
Step 1: Identify the Paradox
"Why does [Company] do [Thing] when it seems it would hurt [Expected Outcome]?"
Step 2: Validate the Mystery
- Multiple real examples across companies or industries
- Clear contradiction between expectation and reality
- Evidence the practice benefits the company despite seeming odd
Step 3: Define the Core Revelation
- One sentence that solves the mystery
- Must be surprising, counterintuitive, and memorable
- Story-ready, can anchor micro-story, tricks, and payoff
Step 4: Confirm Psychological Depth
- At least 2-3 psychological principles or biases
- Include both company strategy and consumer behavior
- Highlight broader implications
Step 5: Generate Historical Examples
- Provide 2-3 early instances of this strategy or paradox
- Include names, dates, and context
Step 6: Test Viral Potential
- Would this make viewers say "I never thought of it that way"?
- Can viewers recognize it in their own life?
- Does it reveal a repeatable pattern?

HIGH-PERFORMING TOPIC FORMATS:
"Why [Company] Does [Counterintuitive Thing]"
"The Psychology Behind [Business Practice]"
"How [Industry] Influences Your Decisions"

TOPIC VALIDATION CHECKLIST:
✅ Real, specific examples
✅ Counterintuitive but explainable
✅ Relatable to broad audiences
✅ Backed by real psychology research
✅ Clear single revelation
✅ Emotional hook without being accusatory
✅ Relevant to modern business

AVOID:
- Conspiracy theories
- Illegal/clearly unethical practices
- One-off scandals
- Overexposed or obvious strategies

SUCCESS METRICS:
High Viral Potential (8-10): Multiple companies use the same psychological strategy, with a clear contradiction + strong core revelation
Medium (6-7): Good psychology, but niche or less relatable
Low (1-5): Obvious, too narrow, or lacks a single compelling insight

GOAL: Generate topics that make viewers think "I never realized businesses use psychology this way, and now I notice it everywhere."

Your response must be in this JSON format with double curly brackets for PyU:
{{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "hook_angle": "Opening line that sparks curiosity",
    "central_mystery": "Why would successful companies do this seemingly odd thing?",
    "core_revelation": "The surprising, counterintuitive truth that explains the strategy",
    "key_examples": ["Specific Example 1", "Specific Example 2", "Specific Example 3"],
    "historical_examples": ["Historical Example 1 with context", "Historical Example 2 with context"],
    "psychological_principles": ["Psychology Principle 1", "Psychology Principle 2", "Psychology Principle 3"],
    "viral_potential_score": 9,
    "why_it_works": "Why this topic will go viral - surprising, relatable, and sponsor-safe"
}}
"""
prompt_creator_hook = """
ROLE: You are a documentary storyteller setting the stage for a captivating investigation.

GOAL: Start with a personal, relatable micro-story, zoom out to reveal a larger system, and clearly introduce the central, counterintuitive `core_revelation`.

--- NARRATIVE STRUCTURE ---
1. **THE MICRO-STORY:** Short, punchy first-person anecdote about a frustrating or surprising experience everyone can relate to.
2. **THE UNIVERSAL CONNECTION:** Show that this experience is not unique and is intentionally designed.
3. **THE PROMISE & SCOPE:** Tease the secrets behind this system and hint at its scale.
4. **THE BRIEF HISTORY:** Give 2–3 mini-stories from different decades, industries, or companies, with dates, names, and outcomes to anchor the timeline.
5. **THE CENTRAL MYSTERY / CORE REVELATION:** Introduce the single, counterintuitive insight the video will explain. Make it memorable and story-ready.

--- PACING & STYLE ---
- Hook sentences: 10–15 words max, punchy and relatable.
- Micro-story should emotionally engage (frustration, surprise, curiosity).
- Word count: approx. 250–350 words (~2–3 minutes runtime).
- Where possible, add short micro-anecdotes (e.g., viral tweets, media coverage).
- Integrate at least one verifiable statistic, research finding, or case study. Numbers should never stand alone — weave them into the story naturally.
- Tone: personal, curious, slightly conspiratorial.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Core Revelation: {core_revelation}
Historical Examples: {historical_examples}

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Personal micro-story opening..."}},
        {{"speaker": "NARRATOR", "line": "Connect personal story to a universal, engineered experience..."}},
        {{"speaker": "NARRATOR", "line": "Reveal the existence of the hidden multi-billion dollar system..."}},
        {{"speaker": "NARRATOR", "line": "Promise to deconstruct the '§design' and show how it works..."}},
        {{"speaker": "NARRATOR", "line": "Brief historical context with 2–3 anchored mini-stories..."}},
        {{"speaker": "NARRATOR", "line": "Pivot to the central mystery / core revelation..."}}
    ]
}}



This is an example of an effective hook, inspire from it, but be creative, copy their style of writing pacing DO NOT COPY WORD BY WORD BE CREATIVE!!!! AND ENGAGING

{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "This is me pulling up to Walmart on a Sunday morning to get some milk and dog food for Zuy, my 3-year-old German Shepherd."}},
        {{"speaker": "NARRATOR", "line": "I walk in, go directly to the back of the store for the milk, and then pass by the Pet Foods aisle to grab dog food."}},
        {{"speaker": "NARRATOR", "line": "As I was on my way out, something stupid starts to happen."}},
        {{"speaker": "NARRATOR", "line": "Something I hate, but keeps happening whenever I come into a grocery store."}},
        {{"speaker": "NARRATOR", "line": "I start wandering around the store with absolutely no clear intentions."}},
        {{"speaker": "NARRATOR", "line": "From one aisle to the other, I keep putting stuff in my cart that I don't even need."}},
        {{"speaker": "NARRATOR", "line": "I walked in to get two items but somehow ended up with 13."}},
        {{"speaker": "NARRATOR", "line": "But it seems like I'm not the only one who does this."}},
        {{"speaker": "NARRATOR", "line": "It turns out grocery stores are perfectly designed to ensure that this keeps happening to millions of visitors every single day."}},
        {{"speaker": "NARRATOR", "line": "They use every trick in the book to make us buy things we never intended on buying."}},
        {{"speaker": "NARRATOR", "line": "We modeled the entire thing to show you the evil design of grocery stores."}},
        {{"speaker": "NARRATOR", "line": "The grocery store as we know it began to take shape in the early 20th century."}},
        {{"speaker": "NARRATOR", "line": "The first self-service grocery store, Piggly Wiggly, opened in 1916 in Memphis, Tennessee, revolutionizing the shopping experience by allowing customers to browse and select their own items."}},
        {{"speaker": "NARRATOR", "line": "This concept quickly gained popularity, leading to the rise of Supermarket chains."}},
        {{"speaker": "NARRATOR", "line": "As a result, notable chains like Kroger and A&P emerged, expanding across the United States and setting the stage for modern grocery retailing."}},
        {{"speaker": "NARRATOR", "line": "Today, the grocery industry is a massive sector in the US economy."}},
        {{"speaker": "NARRATOR", "line": "In 2023, retail and Food Service sales in the United States exceeded $8 trillion."}},
        {{"speaker": "NARRATOR", "line": "On average, Shoppers spend about $174 per trip to the grocery store, a 12% increase from previous years."}},
        {{"speaker": "NARRATOR", "line": "The industry comprises approximately 61,000 grocery stores, employing around 1.4 million people."}},
        {{"speaker": "NARRATOR", "line": "These numbers clearly show that these companies are making money, and a lot of it."}},
        {{"speaker": "NARRATOR", "line": "But before grocery stores looked the way we know today, they were designed way different."}},
        {{"speaker": "NARRATOR", "line": "Back then, before self-service models emerged, grocery shopping typically involved customers requesting items from behind a counter."}},
        {{"speaker": "NARRATOR", "line": "However, with the introduction of self-service in 1916, the layout and design of grocery stores began to evolve dramatically."}},
        {{"speaker": "NARRATOR", "line": "Piggly Wiggly turned things around."}},
        {{"speaker": "NARRATOR", "line": "I don't know why anyone would name a company as such, but to their credit, they changed grocery stores forever."}},
        {{"speaker": "NARRATOR", "line": "The open layout, the organized aisles, the directional lighting—these were all new additions to the grocery store design at the time."}}
    ]
}}
"""

prompt_creator_revelation = """
ROLE: You are an expert guide revealing the hidden system behind the core revelation.

GOAL: Explain the foundational, non-obvious mechanics of how the business or system works. Build the stage for the tricks while reinforcing the `core_revelation`.

--- NARRATIVE STRUCTURE ---
1. **THE FOUNDATION:** Explain the system’s design principles (e.g., layout, structure, rules).
2. **THE PIVOT TO THE TRICKS:** Transition from general mechanics to the specific manipulations, always linking to `core_revelation`.

--- PACING & STYLE ---
- Sentences: 15–25 words max, clear and engaging.
- Word count: approx. 200–300 words (~2 minutes runtime).
- Introduce **novel information** not mentioned in the hook.
- Integrate at least one verifiable statistic or credible case study to anchor the explanation.
- Where possible, add short micro-anecdotes (user complaints, viral posts).
- Tone: explanatory but conversational.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Full Script So Far: {full_script}
Core Revelation: {core_revelation}

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Transition into the explanation of the system's layout or design..."}},
        {{"speaker": "NARRATOR", "line": "Explanation of the first foundational mechanic and its connection to the core revelation..."}},
        {{"speaker": "NARRATOR", "line": "Explanation of the second foundational mechanic, with a statistic or case study..."}},
        {{"speaker": "NARRATOR", "line": "Pivot line that leads into the specific tricks, with breathing room for transition..."}}
    ]
}}




This is an example of an effective hook, inspire from it, but be creative, copy their style of writing pacing 


{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "But before we go into the nitty-gritty of the numerous tricks they use to influence your purchasing decisions, we must establish how grocery stores actually make money."}},
        {{"speaker": "NARRATOR", "line": "Most of us would think that grocery stores make their money by selling products. Although that's not quite wrong, they make the most of their revenue from something else."}},
        {{"speaker": "NARRATOR", "line": "Grocery stores don't really make as much profit as you think. Their margins are as thin as 1 to 3%."}},
        {{"speaker": "NARRATOR", "line": "Which means if you spend $100 at a grocery store, they're going to end up making $1 to $3 at most."}},
        {{"speaker": "NARRATOR", "line": "Considering the tremendous amount of capital it takes to run a grocery store, it's almost impossible for companies to survive on such low profit margins."}},
        {{"speaker": "NARRATOR", "line": "But they already know that. That's why grocery stores are not in the Food business... in fact, they're in the real estate business."}},
        {{"speaker": "NARRATOR", "line": "Let's first establish how the typical grocery store layout works."}},
        {{"speaker": "NARRATOR", "line": "One of the common grocery store layouts is the grid. Your retail fixtures are arranged in Long rows."}},
        {{"speaker": "NARRATOR", "line": "They're also typically placed at right angles throughout your store, making it easier for customers to get a preview of what's in the aisle without having to go through it."}},
        {{"speaker": "NARRATOR", "line": "From the width of the passages to the shelves' dimensions, every square inch of the store is utilized to its fullest capacity."}},
        {{"speaker": "NARRATOR", "line": "The grid layout also uses the loop concept, meaning the flow coming from the entrance should never cross paths with customers exiting,"}},
        {{"speaker": "NARRATOR", "line": "making the whole shopping experience an actual Loop where the customer is guided in and out of the store seamlessly."}},
        {{"speaker": "NARRATOR", "line": "But one could argue all of these design strategies are present in many commercial establishments, not just grocery stores."}},
        {{"speaker": "NARRATOR", "line": "So where does the trickery actually begin?"}}
    ]
}}

"""

prompt_creator_montage = """
ROLE: You are an insider revealing industry secrets.

GOAL: Deconstruct the 3–5 key "tricks" used by the company/system. Each trick should be a mini-chapter that reinforces the `core_revelation`.

--- NARRATIVE STRUCTURE ---
For each trick:
1. Name the trick.
2. Explain what it is.
3. Show why it’s effective and its purpose.
4. Add data, examples, or context (integrate at least one verifiable statistic, research finding, or case study).
5. Name and explain one psychological principle or bias that powers the trick (e.g., FOMO, sunk cost, scarcity).
6. Link clearly to the core revelation.
7. Include a short anecdote if possible (user experience, viral tweet, media coverage).
8. Write smooth transition sentences between tricks (“But that was just the beginning…”).

--- PACING & STYLE ---
- Sentences: 20–40 words for explanations; punchy transitions between tricks.
- Each trick must have a unique psychological insight — avoid repetition.
- Word count: approx. 600–800 words (~4–5 minutes runtime).
- Tone: revelatory, insider, slightly conspiratorial.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Core Revelation: {core_revelation}
Key Examples / Tricks: {key_examples}
Full Script So Far: {full_script}

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Transition into the deconstruction, starting with Trick #1..."}},
        {{"speaker": "NARRATOR", "line": "Detailed explanation of Trick #1 with stat, anecdote, and psychological principle..."}},
        {{"speaker": "NARRATOR", "line": "Breathing room transition into Trick #2..."}},
        {{"speaker": "NARRATOR", "line": "Detailed explanation of Trick #2 with stat, anecdote, and psychological principle..."}},
        {{"speaker": "NARRATOR", "line": "Breathing room transition into Trick #3..."}},
        {{"speaker": "NARRATOR", "line": "Detailed explanation of Trick #3 with stat, anecdote, and psychological principle..."}},
        {{"speaker": "NARRATOR", "line": "Concluding line summarizing the power of these tricks in reinforcing the core revelation..."}}
    ]
}}



This is an example of an effective montage section, inspire from it, but be creative, copy their style of writing pacing, note their storytelling 
Do not copy too much use your own creativity to tie to our own topic of {topic_title} better, use variations of the same word, use different sentence structure so basically not just copy
Notice how long each sections are, how indept they  went it
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The manipulation starts the second you step inside the store."}},
        {{"speaker": "NARRATOR", "line": "The first thing most Shoppers typically encounter when they walk into a grocery store is what's called 'front of shop,' in which you'd find the produce section as well as the flower section."}},
        {{"speaker": "NARRATOR", "line": "This isn't mere coincidence; it's by universal design. A store's produce section plays a large role in how much consumers will spend."}},
        {{"speaker": "NARRATOR", "line": "Not only that, grocery stores use very specific directional lights aimed at fruits and vegetables to make their colors pop."}},
        {{"speaker": "NARRATOR", "line": "Now, once your visual appetite is satisfied, stores have to make sure you don't just pick some fruits and bounce."}},
        {{"speaker": "NARRATOR", "line": "They need you to walk by as many items as possible. This is when the 'traffic builder' method comes into play."}},
        {{"speaker": "NARRATOR", "line": "Ever wondered why milk and bread are always way at the back of the store?"}},
        {{"speaker": "NARRATOR", "line": "This tactic is designed to increase the likelihood of impulse purchases along the way."}},
        {{"speaker": "NARRATOR", "line": "Since milk is a staple item, putting it at the back ensures that Shoppers will pass by various other products, which means more impulse buys."}},
        {{"speaker": "NARRATOR", "line": "That's also why some of the best deals are typically way at the back."}},
        {{"speaker": "NARRATOR", "line": "Now once they get you in the central section of the store, this is when they make the real money off of you."}},
        {{"speaker": "NARRATOR", "line": "At the beginning of the video, I told you grocery stores are in the real estate business. This is what I mean."}},
        {{"speaker": "NARRATOR", "line": "50 to 75 procent of grocery stores' profit is from slotting fees."}},
        {{"speaker": "NARRATOR", "line": "Food companies and brands spend a tremendous amount of money to place their products at a certain location inside stores."}},
        {{"speaker": "NARRATOR", "line": "One product could spend between $10,000 to $100,000 to a million dollars to get just one product on a certain shelf right in front of your eyeballs."}},
        {{"speaker": "NARRATOR", "line": "And that specific sweet spot on a certain shelf is called the Golden Zone."}},
        {{"speaker": "NARRATOR", "line": "Products placed in the golden Zone can sell eight times more than if they're on a different shelf."}},
        {{"speaker": "NARRATOR", "line": "But what is exactly this golden Zone?"}},
        {{"speaker": "NARRATOR", "line": "The golden Zone in grocery store design refers to the area at 4 to 5 ft above the floor, which corresponds to the average Shopper's eye level."}},
        {{"speaker": "NARRATOR", "line": "To perfectly place the money-making shelves, grocery store designers use the average height of the local population as a reference point."}},
        {{"speaker": "NARRATOR", "line": "At this height, most Shoppers' eyes naturally fall, making it the ideal spot for placing high-demand or high-margin products."}},
        {{"speaker": "NARRATOR", "line": "The Shelf design in itself is intentional. Shelves in the golden zone are typically 12 to 18 inches deep. This depth allows for easy access and visibility of products without overwhelming The Shopper."}},
        {{"speaker": "NARRATOR", "line": "But this golden zone changes according to aisles. For example, the golden zone for cereal is at around 3 ft from the ground."}},
        {{"speaker": "NARRATOR", "line": "That's because the real customers in the cereal aisle are children."}},
        {{"speaker": "NARRATOR", "line": "But the golden Zone trick is definitely not the last. They also kind of tailor-make things to people who are right-handed."}},
        {{"speaker": "NARRATOR", "line": "That's because 80 procent of the population is right-handed. According to research, right-handed people tend to look more on their right side than the left when shopping."}},
        {{"speaker": "NARRATOR", "line": "That's why most of the products with higher profit margins are usually placed on the right side of the aisle."}},
        {{"speaker": "NARRATOR", "line": "Also, more resistant floor textures that slow you down are placed next to products they want to push more."}}
    ]
}}


"""

prompt_creator_payoff = """
ROLE: You are the narrator delivering the final twist and actionable insight.

GOAL: Reveal the final trick or psychological manipulation and provide a punchy takeaway that reinforces the `core_revelation`.

--- NARRATIVE STRUCTURE ---
1. **THE FINAL TRICK:** Show last area of manipulation (checkout, interface, etc.).
2. **THE LIGHTNING ROUND:** Quick mentions of other minor tricks.
3. **THE ACTIONABLE TAKEAWAY:** One clear, memorable insight the viewer can apply.
4. **THE OUTRO:** Standard channel outro.

--- PACING & STYLE ---
- Sentences: 15–25 words; concise and punchy.
- Word count: approx. 150–250 words (~1 minute runtime).
- Introduce at least one novel fact not previously mentioned.
- Integrate at least one statistic, research finding, or credible anecdote.
- Tone: cynical, empowering, story-tying.

--- TOPIC INPUT ---
Topic Title: {topic_title}
Full Script So Far: {full_script}
Core Revelation: {core_revelation}

--- OUTPUT FORMAT ---
{{
    "Characters": {{"NARRATOR": "HOST"}} ,
    "story": [
        {{"speaker": "NARRATOR", "line": "Transition to final area of manipulation..."}},
        {{"speaker": "NARRATOR", "line": "Detailed explanation of the final trick with a novel fact and stat..."}},
        {{"speaker": "NARRATOR", "line": "Quick 'lightning round' of other minor tricks with smooth transition..."}},
        {{"speaker": "NARRATOR", "line": "Deliver the actionable takeaway, reinforcing the core revelation..."}},
        {{"speaker": "NARRATOR", "line": "Channel outro ('Subscribe and we'll see you...')..."}}
    ]
}}


This is example of an effective pay off ,inspire from it, but be creative, copy their style of writing pacing 

{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Now once you put way more products in your cart than you intended to, you head out to the checkout line."}},
        {{"speaker": "NARRATOR", "line": "But as soon as you may think you're safe, that's when you screw up even more."}},
        {{"speaker": "NARRATOR", "line": "Grocery stores have found out that for every second a person has to wait before they get checked out, an impulse purchase increases by 4%."}},
        {{"speaker": "NARRATOR", "line": "16 procent of total sales are made in the front area, and 87% of those impulse buys are made 3 seconds before a customer gets checked out."}},
        {{"speaker": "NARRATOR", "line": "In modern grocery stores, the checkout aisle became a maze to fuel impulse purchases, especially during the holiday season."}},
        {{"speaker": "NARRATOR", "line": "You're led through a winding corridor full of tempting small items for you to pick up along the way."}},
        {{"speaker": "NARRATOR", "line": "Some stores intentionally leave out a couple of lines without a cashier, increasing the waiting time in checkout lines."}},
        {{"speaker": "NARRATOR", "line": "All of this without mentioning the price tactics like the 99 cent trick, which increases sales by 24%..."}},
        {{"speaker": "NARRATOR", "line": "...the flashy reduction signs, the pumping of fruity smells to enhance the overall experience... and the list goes on."}},
        {{"speaker": "NARRATOR", "line": "Next time you stop by the grocery store, treat it as if you were walking into a casino."}},
        {{"speaker": "NARRATOR", "line": "Grab the stuff from your list and get the hell out."}},
        {{"speaker": "NARRATOR", "line": "Subscribe and we'll see you on the next one."}}
    ]
}}

"""


creator_hook_revision_rule = """

Rules for Revising Hook Section:

1. Word count: 250–350 words total.
2. Begin with a short, personal, relatable micro-story (1–3 lines) that draws the viewer in.
3. Include 2–3 historical mini-stories with dates, companies, or events to anchor context.
4. Integrate at least one verifiable statistic, research finding, or industry fact. Numbers must be woven naturally into the story.
5. Include smooth transitional sentences between micro-story, universal insight, and core revelation (e.g., 'But that’s not even the worst part…').
6. Tone: curious, slightly conspiratorial, emotionally engaging (frustration, surprise).
7. Hook sentences: max 10–15 words each.
8. Highlight at least one psychological principle if relevant (e.g., FOMO, sunk cost, scarcity) and connect it to the story.
9. Optional: add micro-anecdotes (tweets, user experiences, media coverage) to illustrate the trick.
10. **Do not copy any lines verbatim from the example.** Rewrite all content creatively while maintaining pacing, sentence length, and story flow.

Use this viral example purely for inspiration — style, sentence rhythm, JSON structure. The SCRIPT SHOULD **Focus on rewriting, not copying:**
Give advice accordingly


{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "This is me pulling up to Walmart on a Sunday morning to get some milk and dog food for Zuy, my 3-year-old German Shepherd."}},
        {{"speaker": "NARRATOR", "line": "I walk in, go directly to the back of the store for the milk, and then pass by the Pet Foods aisle to grab dog food."}},
        {{"speaker": "NARRATOR", "line": "As I was on my way out, something stupid starts to happen."}},
        {{"speaker": "NARRATOR", "line": "Something I hate, but keeps happening whenever I come into a grocery store."}},
        {{"speaker": "NARRATOR", "line": "I start wandering around the store with absolutely no clear intentions."}},
        {{"speaker": "NARRATOR", "line": "From one aisle to the other, I keep putting stuff in my cart that I don't even need."}},
        {{"speaker": "NARRATOR", "line": "I walked in to get two items but somehow ended up with 13."}},
        {{"speaker": "NARRATOR", "line": "But it seems like I'm not the only one who does this."}},
        {{"speaker": "NARRATOR", "line": "It turns out grocery stores are perfectly designed to ensure that this keeps happening to millions of visitors every single day."}},
        {{"speaker": "NARRATOR", "line": "They use every trick in the book to make us buy things we never intended on buying."}},
        {{"speaker": "NARRATOR", "line": "We modeled the entire thing to show you the evil design of grocery stores."}},
        {{"speaker": "NARRATOR", "line": "The grocery store as we know it began to take shape in the early 20th century."}},
        {{"speaker": "NARRATOR", "line": "The first self-service grocery store, Piggly Wiggly, opened in 1916 in Memphis, Tennessee, revolutionizing the shopping experience by allowing customers to browse and select their own items."}},
        {{"speaker": "NARRATOR", "line": "This concept quickly gained popularity, leading to the rise of Supermarket chains."}},
        {{"speaker": "NARRATOR", "line": "As a result, notable chains like Kroger and A&P emerged, expanding across the United States and setting the stage for modern grocery retailing."}},
        {{"speaker": "NARRATOR", "line": "Today, the grocery industry is a massive sector in the US economy."}},
        {{"speaker": "NARRATOR", "line": "In 2023, retail and Food Service sales in the United States exceeded $8 trillion."}},
        {{"speaker": "NARRATOR", "line": "On average, Shoppers spend about $174 per trip to the grocery store, a 12% increase from previous years."}},
        {{"speaker": "NARRATOR", "line": "The industry comprises approximately 61,000 grocery stores, employing around 1.4 million people."}},
        {{"speaker": "NARRATOR", "line": "These numbers clearly show that these companies are making money, and a lot of it."}},
        {{"speaker": "NARRATOR", "line": "But before grocery stores looked the way we know today, they were designed way different."}},
        {{"speaker": "NARRATOR", "line": "Back then, before self-service models emerged, grocery shopping typically involved customers requesting items from behind a counter."}},
        {{"speaker": "NARRATOR", "line": "However, with the introduction of self-service in 1916, the layout and design of grocery stores began to evolve dramatically."}},
        {{"speaker": "NARRATOR", "line": "Piggly Wiggly turned things around."}},
        {{"speaker": "NARRATOR", "line": "I don't know why anyone would name a company as such, but to their credit, they changed grocery stores forever."}},
        {{"speaker": "NARRATOR", "line": "The open layout, the organized aisles, the directional lighting—these were all new additions to the grocery store design at the time."}}
    ]
}}

The draft should follow closely this format and...

"""

creator_revelation_revision_rule = """

Revision Rules for the Revelation Section:

The draft should follow these rules:

1. Word count: 200–300 words (~2 minutes of spoken script).
2. Explain 1–2 foundational mechanics of the system behind the core revelation, in a clear and logical order.
3. Integrate at least one **verifiable statistic, case study, or research finding**, naturally woven into the explanation.
4. Include 1–2 short micro-anecdotes (e.g., user complaints, viral posts, news coverage) to make the explanation relatable.
5. Add smooth transition sentences between mechanics and pivoting toward the tricks (e.g., 'But the real manipulations begin when…') to give viewers breathing room.
6. Highlight at least one psychological principle or bias (e.g., FOMO, sunk cost, scarcity) and connect it directly to the mechanics.
7. Maintain sentences between 15–25 words, with a conversational, explanatory tone.
8. **Do not copy any lines verbatim from the example.** The draft should be creative, original, and maintain the pacing, sentence rhythm, and narrative flow inspired by the example.
9. Preserve the JSON structure exactly for easy parsing.

Here is a viral sample purely for inspiration — use it to guide style, pacing, and flow, not content:

{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "But before we go into the nitty-gritty of the numerous tricks they use to influence your purchasing decisions, we must establish how grocery stores actually make money."}},
        {{"speaker": "NARRATOR", "line": "Most of us would think that grocery stores make their money by selling products. Although that's not quite wrong, they make the most of their revenue from something else."}},
        {{"speaker": "NARRATOR", "line": "Grocery stores don't really make as much profit as you think. Their margins are as thin as 1 to 3%."}},
        {{"speaker": "NARRATOR", "line": "Which means if you spend $100 at a grocery store, they're going to end up making $1 to $3 at most."}},
        {{"speaker": "NARRATOR", "line": "Considering the tremendous amount of capital it takes to run a grocery store, it's almost impossible for companies to survive on such low profit margins."}},
        {{"speaker": "NARRATOR", "line": "But they already know that. That's why grocery stores are not in the Food business... in fact, they're in the real estate business."}},
        {{"speaker": "NARRATOR", "line": "Let's first establish how the typical grocery store layout works."}},
        {{"speaker": "NARRATOR", "line": "One of the common grocery store layouts is the grid. Your retail fixtures are arranged in Long rows."}},
        {{"speaker": "NARRATOR", "line": "They're also typically placed at right angles throughout your store, making it easier for customers to get a preview of what's in the aisle without having to go through it."}},
        {{"speaker": "NARRATOR", "line": "From the width of the passages to the shelves' dimensions, every square inch of the store is utilized to its fullest capacity."}},
        {{"speaker": "NARRATOR", "line": "The grid layout also uses the loop concept, meaning the flow coming from the entrance should never cross paths with customers exiting,"}},
        {{"speaker": "NARRATOR", "line": "making the whole shopping experience an actual Loop where the customer is guided in and out of the store seamlessly."}},
        {{"speaker": "NARRATOR", "line": "But one could argue all of these design strategies are present in many commercial establishments, not just grocery stores."}},
        {{"speaker": "NARRATOR", "line": "So where does the trickery actually begin?"}}
    ]
}}


"""

creator_montage_revision_rule = """
The draft should follow these rules:

1. Word count: approx. 400–500 words (~4–5 minutes of spoken script).
2. Deconstruct 3–5 key tricks used by the company/system.
   - For each trick:
     a) Name the trick.
     b) Explain how it works.
     c) Show why it’s effective and its purpose.
     d) Integrate at least one **verifiable statistic, study, or credible example**.
     e) Add 1–2 short micro-anecdotes (e.g., user experiences, viral posts) where possible.
     f) Highlight at least one **psychological principle or bias** (e.g., FOMO, scarcity, sunk cost) and connect it directly to the trick.
3. Write smooth **transition sentences** between tricks to give viewers breathing room (e.g., "But that was just the beginning…" or "The next trick takes it even further…").
4. Maintain sentences between 20–40 words for explanations; keep transitions punchy.
5. Integrate **novel information** not mentioned in the hook or revelation sections.
6. Ensure the narrative reinforces the **core revelation** throughout.
7. **Do not copy lines verbatim** from the viral sample. Use it for pacing, storytelling, and tone inspiration only.
8. Preserve the **JSON structure** exactly for easy parsing.

Here is a viral sample purely for inspiration — use it to guide style, pacing, and flow, not content:

{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "The manipulation starts the second you step inside the store."}},
        {{"speaker": "NARRATOR", "line": "The first thing most Shoppers typically encounter when they walk into a grocery store is what's called 'front of shop,' in which you'd find the produce section as well as the flower section."}},
        {{"speaker": "NARRATOR", "line": "This isn't mere coincidence; it's by universal design. A store's produce section plays a large role in how much consumers will spend."}},
        {{"speaker": "NARRATOR", "line": "Not only that, grocery stores use very specific directional lights aimed at fruits and vegetables to make their colors pop."}},
        {{"speaker": "NARRATOR", "line": "Now, once your visual appetite is satisfied, stores have to make sure you don't just pick some fruits and bounce."}},
        {{"speaker": "NARRATOR", "line": "They need you to walk by as many items as possible. This is when the 'traffic builder' method comes into play."}},
        {{"speaker": "NARRATOR", "line": "Ever wondered why milk and bread are always way at the back of the store?"}},
        {{"speaker": "NARRATOR", "line": "This tactic is designed to increase the likelihood of impulse purchases along the way."}},
        {{"speaker": "NARRATOR", "line": "Since milk is a staple item, putting it at the back ensures that Shoppers will pass by various other products, which means more impulse buys."}},
        {{"speaker": "NARRATOR", "line": "That's also why some of the best deals are typically way at the back."}},
        {{"speaker": "NARRATOR", "line": "Now once they get you in the central section of the store, this is when they make the real money off of you."}},
        {{"speaker": "NARRATOR", "line": "At the beginning of the video, I told you grocery stores are in the real estate business. This is what I mean."}},
        {{"speaker": "NARRATOR", "line": "50 to 75 procent of grocery stores' profit is from slotting fees."}},
        {{"speaker": "NARRATOR", "line": "Food companies and brands spend a tremendous amount of money to place their products at a certain location inside stores."}},
        {{"speaker": "NARRATOR", "line": "One product could spend between $10,000 to $100,000 to a million dollars to get just one product on a certain shelf right in front of your eyeballs."}},
        {{"speaker": "NARRATOR", "line": "And that specific sweet spot on a certain shelf is called the Golden Zone."}},
        {{"speaker": "NARRATOR", "line": "Products placed in the golden Zone can sell eight times more than if they're on a different shelf."}},
        {{"speaker": "NARRATOR", "line": "But what is exactly this golden Zone?"}},
        {{"speaker": "NARRATOR", "line": "The golden Zone in grocery store design refers to the area at 4 to 5 ft above the floor, which corresponds to the average Shopper's eye level."}},
        {{"speaker": "NARRATOR", "line": "To perfectly place the money-making shelves, grocery store designers use the average height of the local population as a reference point."}},
        {{"speaker": "NARRATOR", "line": "At this height, most Shoppers' eyes naturally fall, making it the ideal spot for placing high-demand or high-margin products."}},
        {{"speaker": "NARRATOR", "line": "The Shelf design in itself is intentional. Shelves in the golden zone are typically 12 to 18 inches deep. This depth allows for easy access and visibility of products without overwhelming The Shopper."}},
        {{"speaker": "NARRATOR", "line": "But this golden zone changes according to aisles. For example, the golden zone for cereal is at around 3 ft from the ground."}},
        {{"speaker": "NARRATOR", "line": "That's because the real customers in the cereal aisle are children."}},
        {{"speaker": "NARRATOR", "line": "But the golden Zone trick is definitely not the last. They also kind of tailor-make things to people who are right-handed."}},
        {{"speaker": "NARRATOR", "line": "That's because 80 procent of the population is right-handed. According to research, right-handed people tend to look more on their right side than the left when shopping."}},
        {{"speaker": "NARRATOR", "line": "That's why most of the products with higher profit margins are usually placed on the right side of the aisle."}},
        {{"speaker": "NARRATOR", "line": "Also, more resistant floor textures that slow you down are placed next to products they want to push more."}}
    ]
}}


"""

creator_payoff_revision_rule = """

Rules

The draft for the Payoff section should follow these requirements:

- Deliver the final twist, psychological insight, and actionable takeaway, tying back to the core revelation.
- Include a “lightning round” of minor tricks or insights for added depth.
- Sentences should be **15–25 words max**, concise and punchy.
- Word count: approx. **150–200 words** (~1 minute spoken).
- Integrate at least **one novel statistic, case study, or user anecdote** not mentioned previously.
- Where possible, include short micro-anecdotes (user experiences, viral posts) to illustrate points.
- Tone: cynical, empowering, story-tying, keeping the viewer engaged until the outro.
- The draft should follow the **JSON story format** with double curly braces and maintain the structure of previous sections.
- Avoid copying the example too closely — mimic style, pacing, and flow, but be creative and original.

Here’s a **sample inspiration** (do not copy verbatim, use it to guide tone and pacing):


{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Now once you put way more products in your cart than you intended to, you head out to the checkout line."}},
        {{"speaker": "NARRATOR", "line": "But as soon as you may think you're safe, that's when you screw up even more."}},
        {{"speaker": "NARRATOR", "line": "Grocery stores have found out that for every second a person has to wait before they get checked out, an impulse purchase increases by 4%."}},
        {{"speaker": "NARRATOR", "line": "16 procent of total sales are made in the front area, and 87% of those impulse buys are made 3 seconds before a customer gets checked out."}},
        {{"speaker": "NARRATOR", "line": "In modern grocery stores, the checkout aisle became a maze to fuel impulse purchases, especially during the holiday season."}},
        {{"speaker": "NARRATOR", "line": "You're led through a winding corridor full of tempting small items for you to pick up along the way."}},
        {{"speaker": "NARRATOR", "line": "Some stores intentionally leave out a couple of lines without a cashier, increasing the waiting time in checkout lines."}},
        {{"speaker": "NARRATOR", "line": "All of this without mentioning the price tactics like the 99 cent trick, which increases sales by 24%..."}},
        {{"speaker": "NARRATOR", "line": "...the flashy reduction signs, the pumping of fruity smells to enhance the overall experience... and the list goes on."}},
        {{"speaker": "NARRATOR", "line": "Next time you stop by the grocery store, treat it as if you were walking into a casino."}},
        {{"speaker": "NARRATOR", "line": "Grab the stuff from your list and get the hell out."}},
        {{"speaker": "NARRATOR", "line": "Subscribe and we'll see you on the next one."}}
    ]
}}

"""


final_guide = """

You are the reviewer of a viral, engaging youtube script explainer. Your job is to ensure that these requirements are met
You are allow to make changes edit delete and rewrite sentences so that all these requirements are met



# Tone
Tone must be curious, slightly conspiratorial, and admire the brilliance of the system.
Hook and ending should have punchy, viral-ready lines.

# Pacing & Timing
Lines with dense statistics or multiple concepts may be too long; break up or simplify.
Micro-anecdotes should be short and digestible to maintain rhythm.
Ensure word count matches spoken timing.

# Repetition
Avoid repeating the same psychological concept or stat too often (e.g., decision fatigue, peak-end rule, % spending on impulse).
Reinforce ideas creatively rather than verbatim.

# Clarity & Accessibility
Explain terms like 'Gruen Transfer,' 'peak-end rule,' 'decoupled payment' clearly but concisely.
Avoid jargon overload; use analogies or visuals if needed.
Simplify complex phrases (e.g., 'psychological state' → 'engineered euphoria and decision fatigue').


# Flow & Transitions
Trick sections should be linked with smooth transitions.
Ensure hotel checkout and later examples tie back to previous points.

# Fact-Checking & Credibility
Check numbers and sources (e.g., market size, percentage spending on impulse, scent/music effects).
If uncertain, reword as anecdotal or approximate.
"""


#################################################### EXPLAINER

explainer_idea_generator = """
You are a viral educational content strategist who identifies fascinating systems, innovations, and "how it actually works" stories that make viewers say "I never knew that's how it worked!"

VIRAL EXPLAINER FORMULA:
The Curiosity Gap: Highlight impressive outcomes or systems that seem almost magical
The Investigation: Deep dive into the mechanics that make it possible  
The Revelation: Show the brilliant engineering/thinking behind it
The Appreciation: Leave viewers amazed at human ingenuity

TOPIC CATEGORIES THAT GO VIRAL:
Engineering Marvels:
- How Singapore built the world's most efficient airport
- Why Japanese trains are never late
- How Amazon delivers packages so fast

Business System Mastery:
- How Costco makes money selling everything cheap
- Why McDonald's is actually a real estate company
- How Netflix knows what you want to watch

Hidden Complexity:
- Why airplane food tastes different
- How your GPS actually works
- Why shipping containers revolutionized everything

Scale and Coordination:
- How 2 billion people use WhatsApp daily
- Why the internet doesn't crash
- How global supply chains coordinate

WHAT MAKES EXPLAINER CONTENT VIRAL:
Mind-Blowing Factor: "I never realized it was that complex/clever"
System Appreciation: Celebrates human problem-solving and engineering
Relatability: Everyone uses/experiences this but never understood how
Educational Satisfaction: Viewers feel genuinely smarter
Pattern Recognition: "Now I understand why other systems work this way"
Verifiable Claims: Uses real data and documented processes

TOPIC GENERATION PROCESS:
Step 1: Identify the Impressive System
"How does [Company/System] achieve [Seemingly Impossible Outcome]?"

Step 2: Validate the Complexity
- Multiple interconnected components
- Non-obvious solutions to real problems
- Impressive scale or efficiency metrics
- Documented business/engineering practices

Step 3: Define the Core Insight  
- One sentence explaining the fundamental principle
- Must be surprising but logical once explained
- Should reveal broader patterns about how complex systems work

Step 4: Confirm Educational Depth
- At least 3-4 major system components to explain
- Real data, case studies, and documented practices
- Historical context showing evolution
- Broader implications viewers can apply

SUCCESS METRICS:
High Viral Potential (8-10): Complex system with documented practices, impressive scale, broad relatability
Medium (6-7): Interesting but niche, or less complex than it appears
Low (1-5): Obvious once explained, limited educational value

GOAL: Generate topics that make viewers think "That's incredible - I use this every day but never understood the genius behind it"

Your response must be in this JSON format:
{
    "topic_title": "How [Company/System] Achieves [Impressive Outcome]",
    "hook_angle": "Opening that highlights the impressive outcome",
    "central_mystery": "How is this seemingly impossible thing actually achieved?",
    "core_revelation": "The fundamental principle or insight that makes it work",  
    "key_components": ["System Component 1", "System Component 2", "System Component 3"],
    "historical_context": ["Historical Development 1", "Historical Development 2"],
    "scale_metrics": ["Impressive Scale Fact 1", "Impressive Scale Fact 2"],
    "viral_potential_score": 9,
    "why_it_works": "Why this will fascinate viewers and teach them something valuable"
}

"""

explainer_hook_prompt = """
ROLE: You are a storyteller highlighting human achievement and engineering brilliance.

GOAL: Start with genuine amazement at an impressive system, then promise to explain how it actually works.

STRUCTURE:
1. THE MOMENT OF REALIZATION: Personal experience that made you notice this system's brilliance
2. THE SCALE: Show the impressive numbers/scope that most people don't realize  
3. THE MYSTERY: "How is this even possible?"
4. THE HISTORICAL CONTEXT: 2-3 key innovations that made this system possible
5. THE PROMISE: "Let's break down this incredible achievement"

TONE: Curious, genuinely impressed, educational

EXAMPLE LANGUAGE:
- "This system processes X per second without anyone noticing"
- "The engineering behind this is absolutely brilliant"
- "Most people have no idea how complex this actually is"
- "Let's break down one of humanity's most impressive achievements"

Word Count: 300-400 words
Sentences: 12-18 words max, punchy and clear
Include: 2-3 verifiable statistics naturally woven in, use the search feature and provide reliable sources

"""

explainer_component = """
GOAL: Explain the 2-3 foundational elements that make the system work

STRUCTURE:
1. THE CORE PRINCIPLE: The main insight that makes everything possible
2. THE KEY COMPONENTS: 2-3 major system elements with real examples
3. THE INTEGRATION: How these components work together seamlessly
4. THE TRANSITION: "But the real genius is in the details..."

TONE: Educational but accessible, appreciative of clever solutions

REQUIREMENTS:
- Include 1-2 verifiable statistics or case studies
- Use concrete examples from real operations  
- Explain WHY each component is necessary
- Connect back to the impressive outcome from the hook

Word Count: 250-350 words
Focus: System architecture and core principles

"""

explainer_deepdive ="""

GOAL: Break down 3-4 specific innovations or clever solutions within the system

For each innovation:
1. Name the specific solution/innovation
2. Explain what problem it solves  
3. Show how it works with real examples
4. Include data showing its effectiveness
5. Connect to broader engineering/business principles
6. Add transition to next innovation

TONE: "This is brilliant because..." - appreciative and educational

REQUIREMENTS:
- Each innovation should teach a broader principle
- Use specific, verifiable examples and data
- Include real company names and documented practices
- Show evolution of solutions over time
- Connect innovations to user experience

Word Count: 500-700 words  
Structure: 3-4 innovations, smooth transitions between each
Focus: Specific clever solutions with real-world impact
"""

explainer_payoff = """
GOAL: Tie everything together and show broader implications

STRUCTURE:
1. THE SCALE REVEAL: Final impressive metric that shows system's true scope
2. THE PRINCIPLES: What other industries can learn from this approach
3. THE FUTURE: Where this type of innovation is heading
4. THE APPRECIATION: Why this represents human achievement at its best
5. THE OUTRO: Standard channel closing

TONE: Inspiring, educational, forward-looking

REQUIREMENTS:
- Include one final "wow" statistic  
- Connect to broader patterns in technology/business
- Leave viewers feeling smarter and more appreciative
- End on a note of human achievement and ingenuity

Word Count: 200-300 words
Focus: Broader implications and appreciation for human problem-solving
"""

explainer_hook_revision_rules ="""
1. Word count: 300-400 words total
2. Start with specific, relatable moment of system interaction
3. Include 2-3 historical developments with dates and context
4. Integrate 2-3 verifiable statistics naturally into narrative
5. Build genuine curiosity about "how is this possible?"
6. Tone: Impressed and curious, not conspiratorial
7. Max sentence length: 18 words
8. Include smooth transitions between personal story and system scale
9. Promise educational value, not exposé  
10. Use concrete, specific examples throughout

AVOID: Conspiracy language, manipulation framing, unverifiable claims
USE: Appreciation language, engineering marvels, documented achievements

"""

explainer_component_revision_rules = """
1. Word count: 250-350 words  
2. Explain 2-3 core system principles clearly
3. Include 1-2 verifiable statistics or documented case studies
4. Use concrete examples from real operations
5. Connect each principle to the impressive outcome
6. Smooth transitions between principles
7. Set up the detailed breakdown to follow
8. Educational tone throughout - "Here's how this brilliant system works"

FOCUS: System architecture, core innovations, foundational principles
AVOID: Speculation, unverified claims, manipulation framing

"""

explainer_deepdive_revision_rules = """
1. Word count: 500-700 words
2. Break down 3-4 specific innovations/solutions
3. Each innovation must include:
   - Real problem it solves
   - How the solution works  
   - Verifiable data showing effectiveness
   - Connection to broader principles
4. Use documented business practices and real company examples
5. Include evolution/development of solutions over time
6. Smooth transitions between innovations
7. Educational appreciation throughout - "This solution is brilliant because..."

QUALITY CONTROL:
- Every claim must be verifiable
- Use real company names and documented practices  
- Focus on genuine innovations, not ordinary business
- Connect to broader patterns in engineering/business

"""

explainer_payoff_revision_rules = """
1. Word count: 200-300 words
2. Include final impressive scale metric
3. Connect system to broader innovation patterns
4. Show what other industries can learn
5. End with appreciation for human achievement
6. Include brief forward-looking perspective
7. Avoid manipulation warnings - end on educational high note
8. Standard outro for channel branding

TONE: Inspiring, educational, appreciative of human ingenuity
FOCUS: Broader implications and systems thinking principles

"""





############################################################## EXPALINER SIMPLE WITH STOCK FOOTAGE

simExplain_idea= """

"""

##################################################### 11th (Claude suggest with hmw style)



prompt_business_hook11 = """
VIRAL HOOK BUILDER - First 60-90 Seconds

You are writing the opening hook for a sponsor-safe, storytelling YouTube video. 
Goal: spark curiosity immediately, never accusatory. Always engaging, conversational, and fact-driven.

HOOK STYLES TO CHOOSE FROM (pick what best fits {topic_title}), Be creative:
1. CURIOUS CONTRADICTION: "It doesn’t make sense that [X], but actually [Y]"
2. MICRO-STORY: A short, real-world anecdote that instantly draws viewers in
3. INVERTED EXPECTATION: "Most people believe [X], but the truth is [Y]"
4. HIDDEN COST/BENEFIT: "This tiny overlooked detail is why [company/product] is worth billions"
5. TIME MACHINE: "Back in [year], [X] failed. Today it’s the secret weapon of billion-dollar companies"
6. STAKES HOOK: "This single decision cost companies [X dollars/users]. Why does it keep happening?"


TOPIC INPUT:
Hook Angle: {hook_angle}
Central Question: {central_mystery}

REQUIREMENTS:
- Use real companies, products, or historical facts
- Cite at least one reliable source inline
- End with a cliffhanger
- Generate 4–6 dialogue lines
- Expand each line to 2–3 sentences for fuller engagement
- Tone: curious, sponsor-friendly

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Opening hook line with expanded curiosity..."}},
        {{"speaker": "NARRATOR", "line": "Supporting fact with source and extra context..."}},
        {{"speaker": "NARRATOR", "line": "Additional curiosity-building micro-story or question..."}},
        {{"speaker": "NARRATOR", "line": "Transition into central question with intrigue..."}}
    ]
}}
"""
prompt_business_mystery11 = """
CONTEXT & SETUP - Minutes 1-3

Provide background that makes the story compelling.
Focus on "why this matters" before revealing the mystery.

STRUCTURE:
1. SCOPE: "This affects [number] people/companies/industries worldwide"
2. CURRENT STATE: "Right now, [current situation with examples]"
3. HIDDEN COMPLEXITY: "But most people don't realize [surprising complexity]"
4. STAKES: "Understanding this could change how you think about [area]"

TOPIC INPUT:
Central Question: {central_mystery}
Key Examples: {key_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include 2–3 real company examples with sources
- Include one surprising statistic
- Generate 5–7 dialogue lines
- Expand each line to 2–3 sentences
- Keep curiosity high without revealing full answer
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Scope and scale explanation..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 1 with source..."}},
        {{"speaker": "NARRATOR", "line": "Current situation example 2 with source..."}},
        {{"speaker": "NARRATOR", "line": "Hidden complexity reveal with extra context..."}},
        {{"speaker": "NARRATOR", "line": "Stakes and importance explained..."}},
        {{"speaker": "NARRATOR", "line": "Transition to historical context, Do not fully recount the historical origins; just hint at them briefly or cite one example, save the detailed history for the HISTORICAL DEEP DIVE section...."}}
    ]
}}
"""
prompt_business_history11 = """
HISTORICAL DEEP DIVE - Minutes 3-5

Explore the origin and evolution of this practice.
Make history feel relevant and surprising.

STRUCTURE:
1. ORIGIN STORY: "This began in [time period] with [person/company/event]"
2. KEY TURNING POINTS: "Then [event] changed everything because [reason]"
3. EVOLUTION CHAIN: 2–3 major evolutionary steps with dates and sources
4. MODERN EMERGENCE: "By [recent year], it became what we see today"

TOPIC INPUT:
Central Question: {central_mystery}
Historical Context: {historical_examples}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Include specific names, dates, companies
- At least 2 reliable historical sources
- 6–8 dialogue lines
- Expand lines to 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive
- For each historical point, briefly connect it to an experience the viewer has in a store today (e.g., "This 'Golden Rule' layout is why you still have to walk the entire store perimeter...").
OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Origin story with specifics..."}},
        {{"speaker": "NARRATOR", "line": "First major turning point explained..."}},
        {{"speaker": "NARRATOR", "line": "Second evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Third evolution step..."}},
        {{"speaker": "NARRATOR", "line": "Key breakthrough moment..."}},
        {{"speaker": "NARRATOR", "line": "Modern emergence with examples..."}},
        {{"speaker": "NARRATOR", "line": "Transition to psychology section..."}}
    ]
}}
"""
prompt_business_psychology11 = """
PSYCHOLOGY DEEP DIVE

GOAL: Explain complex psychological principles in an accessible, engaging, and non-repetitive way. Make the science relatable by using a diverse set of examples.

STRUCTURE:
1. CENTRAL QUESTION: "Why does this work so effectively? It involves multiple psychological principles."
2. PRINCIPLE 1: Explanation + a clear example directly related to the video's main topic ({topic_title}).
3. PRINCIPLE 2: Explanation + an analogous example from a completely different and unexpected domain.
4. PRINCIPLE 3: Explanation + a relatable example from a common, personal, everyday-life experience.
5. INTERACTION: "When these principles combine, the effect is amplified..."

TOPIC INPUT:
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Cover 3 distinct psychological principles.
- **CRITICAL REQUIREMENT FOR DIVERSITY:** To prevent repetition, you MUST use a variety of examples. The first example should connect to the main topic ({topic_title}). The subsequent examples for the other principles MUST be from different, unrelated contexts (e.g., if the topic is business, use an analogy from sports, art, or social dynamics). This demonstrates the universality of the principles.
- Include scientific sources where appropriate.
- Generate 8–10 dialogue lines, expanding each line for natural pacing.
- Use analogies and simple language to make complex ideas clear.
- Ensure the final transition smoothly connects these diverse principles back to the video's main topic.

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Set up the central question about why this works..."}},
        {{"speaker": "NARRATOR", "line": "Principle 1 explained with a TOPIC-SPECIFIC example..."}},
        {{"speaker": "NARRATOR", "line": "Principle 2 explained with an ANALOGOUS example from a different domain..."}},
        {{"speaker": "NARRATOR", "line": "Principle 3 explained with a PERSONAL/EVERYDAY LIFE example..."}},
        {{"speaker": "NARRATOR", "line": "Explanation of how these principles interact and amplify each other..."}},
        {{"speaker": "NARRATOR", "line": "Transition that ties these universal principles back to the core subject of the video..."}}
    ]
}}
"""
prompt_business_application11 = """
EXTENSION & MODERN BATTLEFIELD - Minutes 8-11

Show how these psychological principles extend beyond the grocery store and into other areas of the viewer's life. Frame it as an evolution of these techniques.

STRUCTURE:
1. THE CORE IDEA REVISITED: "So it's not just about milk. This is about controlling your path to influence your decisions."
2. THE DIGITAL AISLE: "Now, think about how this works online..." (e.g., website layouts, infinite scroll, Amazon's 'Customers also bought').
3. BEYOND RETAIL: "You'll even see this where you least expect it..." (e.g., social media feed design, video game level layouts, theme park queues).
4. THE FUTURE OF INFLUENCE: "And it's getting even more sophisticated..." (e.g., AI personalizing store layouts in real-time, digital ads changing as you walk).

TOPIC INPUT:
Topic Title: {topic_title}
Psychological Principles: {psychological_principles}
Here are whats written before you: {full_script}

REQUIREMENTS:
- Directly connect each example back to the core psychological principles (Gruen Transfer, Mere Exposure, etc.).
- Use 3-4 relatable examples from digital life and physical spaces.
- Maintain a tone of discovery and empowerment, not just a list of facts.
- Generate 6-8 dialogue lines.
- Expand each line to 2-3 sentences.
- Ensure the focus remains on the viewer's experience.

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Reiterate the core psychological thesis..."}},
        {{"speaker": "NARRATOR", "line": "Example 1: The Digital Aisle (e.g., e-commerce)..."}},
        {{"speaker": "NARRATOR", "line": "Example 2: The Entertainment Maze (e.g., social media/streaming)..."}},
        {{"speaker": "NARRATOR", "line": "Example 3: Physical World, Non-Retail (e.g., airports, theme parks)..."}},
        {{"speaker": "NARRATOR", "line": "The Future: How AI and data are making this even more personal..."}},
        {{"speaker": "NARRATOR", "line": "Transition to the final payoff and actionable advice..."}}
    ]
}}
"""
prompt_business_payoff11 = """
ACTIONABLE INSIGHTS & PAYOFF - Minutes 13-15

Provide practical takeaways and satisfying conclusion.

STRUCTURE:
1. KEY INSIGHT RECAP
2. PERSONAL APPLICATION
3. RECOGNITION SKILLS: "Now you'll notice when..."
4. EMPOWERMENT
5. BROADER PERSPECTIVE
6. CONTENT BRIDGE: transition to related video

TOPIC INPUT:
Topic Title: {topic_title}
Historical examples: {historical_examples}
psychological principles {psychological_principles}
Here are whats written before you: {full_script}


REQUIREMENTS:
- 2–3 actionable takeaways
- Include one "now you'll notice" observation
- Generate 6–7 dialogue lines
- Expand each line 2–3 sentences
- Make good connections to the previous points in the sciprt
- Make sure not to repeat any points too many times that is repetitive

OUTPUT FORMAT:
{{
    "Characters": {{"NARRATOR": "HOST"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Key insight recap..."}},
        {{"speaker": "NARRATOR", "line": "Personal application advice..."}},
        {{"speaker": "NARRATOR", "line": "Recognition skills development..."}},
        {{"speaker": "NARRATOR", "line": "Empowerment message..."}},
        {{"speaker": "NARRATOR", "line": "Broader perspective connection..."}},
        {{"speaker": "NARRATOR", "line": "Natural bridge to related content..."}}
    ]
}}
"""



tone_prompt = """
CONVERSATIONAL VOICE REQUIREMENTS:
- Use direct address: "You've probably noticed..." "Here's what you don't realize..."
- Include conversational connectors: "Yeah, that's right..." "I know, I know..." "Here's the thing though..."
- Add skepticism handling: "I know this sounds crazy, but..." "Before you think this is conspiracy theory..."
- Use natural speech patterns: contractions, incomplete sentences for emphasis
- Include viewer validation: "Sounds frustrating, right?" "You're not imagining it..."


"""

prompt_business_hook11 += tone_prompt
prompt_business_mystery11 += tone_prompt
prompt_business_history11 += tone_prompt
prompt_business_psychology11 += tone_prompt
prompt_business_application11 += tone_prompt
prompt_business_payoff11 += tone_prompt



######################################################

prompt_business_hook3 = """
PROMPT 1: VIRAL HOOK GENERATOR (0-30 seconds)
HOOK GENERATOR - RESEARCH-BACKED STORYTELLING
You are creating an opening hook for a business psychology education video that feels like discovering hidden truths with scientific backing.
MANDATORY PRE-WRITING STEP:

Use web_search to find recent studies, industry reports, and verified data about your topic
Verify all statistics and claims through multiple credible sources
Ensure all company examples reference only documented, publicly available practices

FLEXIBLE HOOK STYLES (Choose what fits the topic best):
RELATABLE DISCOVERY HOOK (Best for consumer psychology topics):
"You know that moment when you [specific relatable scenario]? Research suggests that feeling isn't random - it appears to be the result of [psychological principle] that companies like [Name] reportedly use in their design strategies..."
PATTERN RECOGNITION HOOK (Best for industry-wide practices):
"Industry analysis reveals something interesting: [observable pattern across platforms]. Once you understand the psychology behind it, you'll notice this everywhere..."
RESEARCH REVELATION HOOK (Best for data-heavy topics):
"A 2024 [Institution] study found something surprising: [research finding]. This suggests that what feels like [common experience] may actually be [psychological explanation]..."
COUNTERINTUITIVE FACT HOOK (Best for myth-busting topics):
"Most people think [common belief], but recent research indicates [surprising truth]. Here's what behavioral scientists have discovered about why this happens..."
HOOK REQUIREMENTS:

Complete within 15-30 seconds maximum (modern attention spans)
Lead with universal human experience
Support immediately with credible research
Create curiosity about psychological explanation
End with promise of practical understanding
Include proper source attribution
Use legally safe language throughout

TARGET: Create immediate emotional connection while establishing scientific credibility.


"""
prompt_business_mystery3 = """
PROMPT 2: FLEXIBLE MYSTERY BUILDER (30 seconds - 3 minutes)
ADAPTIVE STORY DEVELOPMENT
You are building intrigue around why psychological principles become business strategies. Structure should serve the story, not constrain it.
MANDATORY RESEARCH STEP:
Use web_search to find:

Historical context for the practice
Growth data and industry trends
Academic research on underlying psychology
Multiple company examples and case studies

FLEXIBLE BUILDING BLOCKS (Use what serves your story):
HISTORICAL CONTEXT BLOCK (When relevant):
"This approach reportedly has roots in [historical practice/research]. Back in [era], [context]. But the modern version appears to leverage [psychological insight] in ways that weren't possible before..."
SCALE AND IMPACT BLOCK (Always include):
"Industry reports suggest this approach has grown from [amount] in [year] to [amount] in [recent year]. According to [Source], that represents [meaningful comparison]..."
PSYCHOLOGY FOUNDATION BLOCK (Core element):
"But why does this work so effectively? Research in behavioral psychology suggests it's because [psychological principle]. Studies indicate that [human behavior pattern]..."
BUSINESS APPLICATION BLOCK (Connect psychology to practice):
"Companies reportedly apply this by [specific techniques]. Industry analysis shows this approach appears designed to [psychological outcome]..."
CULTURAL CONTEXT BLOCK (When applicable):
"This trend seems to coincide with [cultural shifts]. Researchers note that [demographic/behavioral changes] may make consumers particularly susceptible to [psychological technique]..."
STORY REQUIREMENTS:

Build anticipation for psychological explanation
Include verified data and proper attribution
Show pattern across multiple companies/industries
Use legally safe language throughout
Create "aha moment" setup for next section
Maintain conversational, accessible tone

TARGET: Make viewers feel like they're uncovering a fascinating pattern backed by real research.

"""
prompt_business_psychology3 = """
PROMPT 3: PSYCHOLOGY EDUCATION SECTION (3-6 minutes)
RESEARCH-BACKED BEHAVIOR EXPLANATION
You are explaining psychological principles that drive business strategies. Make complex concepts accessible while maintaining scientific accuracy.
MANDATORY RESEARCH REQUIREMENTS:

Cite specific studies and researchers
Include publication years and institutions
Cross-reference claims with multiple academic sources
Verify all psychological terminology and definitions

EDUCATIONAL STRUCTURE:
SETUP QUESTION (3:00-3:15):
"So why do these techniques appear to be so effective? To understand this, we need to look at what behavioral researchers have discovered about [human behavior area]..."
PSYCHOLOGY EXPLANATION (3:15-5:00):
For each psychological principle:

Scientific name: "What researchers call [technical term]"
Accessible definition: "In simple terms, this means [everyday explanation]"
Research backing: "Studies by [Institution/Researcher] found that [specific finding]"
Business application: "Companies reportedly leverage this by [specific technique]"
Recognizable example: "You might notice this when [common experience]"

DESIGN PSYCHOLOGY REVEAL (5:00-5:45):
"Industry analysis suggests these aren't accidental design choices. Research indicates that elements like [specific UI/UX features] appear to be based on psychological principles such as [scientific concepts]..."
REALITY CHECK (5:45-6:00):
"It's important to note that many of these techniques have legitimate uses and can genuinely improve user experience. The key is understanding how they work so you can make informed decisions..."
REQUIREMENTS:

Use proper scientific terminology with accessible explanations
Include specific study citations and years
Show both psychological mechanism and business application
Maintain educational tone, not accusatory
Help viewers recognize patterns in their own experience
Present balanced perspective on business practices

TARGET: Make viewers feel educated about psychology while understanding business applications.

"""
prompt_business_application3 = """
PROMPT 4: BUSINESS MODEL ANALYSIS (6-8 minutes)
INDUSTRY ECONOMICS EDUCATION
You are explaining how psychological insights translate into business value. Focus on understanding economics, not villainizing companies.
RESEARCH REQUIREMENTS:

Find verified revenue data and business metrics
Reference industry reports and financial analyses
Include academic research on business psychology applications
Verify all financial claims through credible business sources

ANALYSIS STRUCTURE:
BUSINESS CONTEXT (6:00-6:30):
"To understand why companies use these approaches, let's look at the business economics involved. Industry reports suggest that [practice] can impact key metrics like [specific business outcomes]..."
REVENUE IMPACT BREAKDOWN (6:30-7:15):
"According to [Business Source], companies reportedly see [specific improvements] when implementing these techniques:

First: [metric] improvement of [percentage] according to [source]
Second: [metric] impact of [amount] based on [research]
Third: [outcome] resulting in [business benefit] per [study]"

PRACTICAL EXAMPLE (7:15-7:45):
"Here's how this might work in practice: [hypothetical but realistic scenario based on documented practices]. Industry analysis suggests this approach could potentially [business outcome] while users experience [user experience]..."
BROADER IMPLICATIONS (7:45-8:00):
"Research indicates this represents a broader trend where [psychological insight] becomes [business strategy]. Understanding these patterns can help consumers make more informed decisions..."
REQUIREMENTS:

Focus on business understanding, not accusation
Include specific, verified financial data
Show connection between psychology and business outcomes
Use industry reports and academic business research
Present information as education, not exposé
Maintain balanced perspective on business practices

TARGET: Help viewers understand business motivations while maintaining objectivity.

"""
prompt_business_payoff3 = """
PROMPT 5: EMPOWERMENT CONCLUSION (8-10 minutes)
PRACTICAL APPLICATION AND PROTECTION
You are providing actionable advice based on psychological research while empowering informed decision-making.
RESEARCH BASIS:

Reference consumer protection research
Include studies on effective decision-making strategies
Find expert recommendations from behavioral economists
Verify advice through academic consumer psychology research

CONCLUSION STRUCTURE:
BALANCED PERSPECTIVE (8:00-8:30):
"It's worth noting that many of these techniques serve legitimate business purposes and can genuinely improve user experience. The goal isn't to avoid all influence, but to understand it. Research suggests that awareness itself can improve decision-making..."
EVIDENCE-BASED PROTECTION STRATEGIES (8:30-9:15):
"Based on behavioral research, here are strategies that studies suggest can help with informed decision-making:

[Strategy 1] - According to [Research], this approach can [specific benefit]
[Strategy 2] - Studies indicate this reduces [specific bias] by [amount]
[Strategy 3] - Research shows this improves [decision outcome]"

PRACTICAL APPLICATION (9:15-9:45):
"The next time you encounter [common scenario], remember that [psychological principle] might be at play. Being aware of this can help you [specific action] based on your actual preferences rather than automatic responses..."
EDUCATIONAL WRAP-UP (9:45-10:00):
"Understanding these psychological principles isn't about becoming cynical - it's about making more informed choices. Now that you know how [topic] works, you can decide what approach works best for your situation. For more insights into business psychology, check out our video on [related topic]..."
REQUIREMENTS:

Base all advice on academic research
Avoid fear-mongering or anti-business sentiment
Emphasize informed choice over avoidance
Include specific, actionable strategies
Reference studies supporting recommendations
End with empowerment, not victimization
Provide logical content continuation

TARGET: Leave viewers feeling educated, empowered, and capable of making informed decisions.

"""
legal_safe_guard3 = """
Before finalizing any script, verify:
RESEARCH VERIFICATION:

 Used web_search to verify all major claims
 Included at least 3 credible sources per major section
 Checked publication dates (all within 2 years)
 Cross-referenced statistics through multiple sources
 Verified all company examples are publicly documented

LEGAL SAFETY:

 No direct accusations against specific companies
 Used qualifying language ("reportedly," "appears to," "suggests")
 Focused on industry patterns, not individual wrongdoing
 Included professional advice disclaimers
 Framed as education, not expose

RETENTION OPTIMIZATION:

 Hook completes within 30 seconds
 Each section builds logically on previous
 Includes relatable examples throughout
 Maintains curiosity gaps between sections
 Ends with clear value and next steps

EDUCATIONAL VALUE:

 Explains psychology concepts accessibly
 Provides practical, actionable advice
 Maintains balanced perspective
 Empowers rather than victimizes viewers
 Connects individual experience to broader patterns

CONTENT AUTHENTICITY:

 Structure serves the story, not formula
 Topic feels unique and engaging
 Scientific concepts explained conversationally
 Maintains credibility throughout
 Provides genuine value to viewers

FINAL PRINCIPLE: Create content that educates consumers about business psychology while maintaining respect for both viewers and businesses, backed by solid research and delivered through engaging storytelling.
"""


prompt_business_hook3 += legal_safe_guard3
prompt_business_mystery3 += legal_safe_guard3
prompt_business_psychology3 += legal_safe_guard3
prompt_business_application3 += legal_safe_guard3
prompt_business_payoff3 += legal_safe_guard3



business_psych_prompt ="""
Viral Business Psychology Explainer Video Prompt
You are creating highly engaging YouTube explainer videos that reveal the psychology behind major business decisions. Study this viral formula that hooks viewers and keeps them watching.
TOPIC INPUT:
Use the following topic generated by the Topic Generator:
[TOPIC_INPUT]

Topic Title: {topic_title}
Hook Angle: {hook_angle}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
[/TOPIC_INPUT]

Your job is to transform this topic into a viral 8-10 minute script using the structure below.
VIRAL HOOK FORMULA:
Contradictory Setup (First 15 seconds):
Start with a PARADOX that doesn't make sense:

"Netflix cancels their most popular shows... unless you understand this twisted psychology"
"Apple makes their old phones slower... but it's actually genius marketing"
"McDonald's ice cream machines are broken 25% of the time... and that's exactly what they want"

Statistical Credibility (15-30 seconds):
Hit them with shocking, specific numbers:

"According to internal leaked documents..."
"Data from 2.3 million customers shows..."
"Since 2019, this strategy has increased profits by 340%..."

The Mystery Statement (30-45 seconds):
Present the central puzzle with specific examples:

"There's a great mystery about why [Company X] does [Seemingly Stupid Thing]"
"Some companies succeed with [obvious strategy], others with [different strategy], but [Company] does something completely different..."
Use specific, named examples that viewers recognize

SCRIPT STRUCTURE:
Hook (45-60 seconds):
"[Shocking contradictory statement about well-known company]

According to [specific source], [shocking statistic that proves the contradiction]

There's a great mystery about [the business practice]. Some companies [do obvious thing], others [do different obvious thing], but [focus company] does something that seems completely insane...

[Specific example that seems to make no business sense]

But [focus company] is making [specific amount] doing this, and here's the psychology that explains everything..."
The Central Mystery (60-90 seconds):

Present 2-3 specific examples that seem illogical
Use exact numbers, dates, and company names
Build the "this makes no sense" feeling
Tease the psychological explanation coming

The Psychology Breakdown (3-4 minutes):
Reveal 3 key psychological principles with this structure:

The Hidden Psychology

"The reason? [Specific psychological bias/principle]"
Explain it simply with everyday examples
Show how it works in the viewer's own life


The Business Application

"Here's how [Company] weaponizes this psychology..."
Specific tactics with concrete examples
Internal data or leaked strategies if available


The Deeper Strategy

"But it gets even more calculated..."
Secondary psychological effects
Why competitors can't easily copy this


The Industry Pattern

"Once you see this, you'll notice it everywhere..."
How other companies use the same psychology
Examples viewers can immediately recognize



The Payoff (30-45 seconds):

Connect back to the opening paradox
Show why the "illogical" strategy is actually brilliant
Leave with actionable insight viewers can use

ENGAGEMENT TECHNIQUES FROM VIRAL CONTENT:
Specific, Named Examples: Never say "a streaming company" - say "Netflix." Use real people, real numbers, real situations
Visual Metaphors: Compare business strategies to things everyone understands (like the sitcom door entrance example)
Pattern Recognition: "Once you see this pattern, you'll notice it in [list 3-4 other places]"
Insider Knowledge: "What most people don't realize is..." / "According to leaked internal documents..."
Contradiction Resolution: Set up something that seems stupid, then reveal why it's genius
TONE & PACING:
Conversational Authority: Sound like someone who has inside knowledge
Rapid Information Delivery: Pack facts and insights densely
Confident Assertions: Don't hedge - make bold claims backed by evidence
Relatable Comparisons: Connect complex business concepts to everyday experiences
PSYCHOLOGICAL HOOKS:
Curiosity Gap: Create questions that MUST be answered
Social Proof: "Millions of people fall for this without realizing..."
Loss Aversion: "Companies are manipulating your fear of missing out..."
Pattern Completion: "There are three reasons this works... first..."
VOICE OPTIONS:
Choose from: MAN1
JSON FORMAT:
{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "Netflix cancels shows right when they get good. But this isn't stupidity—it's calculated psychology."}},
        {{"speaker": "NARRATOR", "line": "According to leaked Netflix data, shows cost 30% more after season three, but viewership only increases 12%."}},
        {{"speaker": "NARRATOR", "line": "There's a great mystery about streaming success. Some platforms keep shows forever, others reboot constantly, but Netflix does something that seems completely insane..."}},
        {{"speaker": "NARRATOR", "line": "They're not trying to finish stories. They're trying to hack your brain's reward system."}}
    ]
}}
VIRAL TOPIC FORMATS:
"The [Company] Strategy That Makes No Sense"
"Why [Company] Does [Counterintuitive Thing] (It's Genius)"
"The Psychology Behind [Seemingly Stupid Business Practice]"
"How [Company] Tricks Your Brain Into [Specific Behavior]"
SPECIFIC EXAMPLE STARTERS:

"Tesla doesn't advertise... but sells more cars than companies that spend billions on ads"
"Costco loses money on rotisserie chicken... and that's exactly the point"
"TikTok shows you videos you don't follow... because they understand addiction better than drug dealers"
"Disney keeps their movies in 'the vault'... exploiting a psychological principle from the 1940s"

AVOID:

Generic statements without specific examples
Slow builds - hook immediately
Academic language over conversational explanation
Apologetic or uncertain tone
Obvious insights everyone already knows

GOAL: Create the "I can't stop watching this" feeling by revealing counterintuitive business strategies that seem crazy until you understand the psychology. Every 30 seconds should deliver a new "wait, what?" moment."""


# Deepseek
business_psych_prompt2 = """
Viral Business Psychology Explainer Video Prompt (Enhanced)

You are creating highly engaging YouTube explainer videos that reveal the psychology behind major business decisions. Your goal is to replicate the structure, flow, and retention strategies of highly viral explainer videos. Study this viral style carefully:

VIRAL STYLE FEATURES:
1. Sentence Flow & Pacing:
   - Use a mix of short, punchy sentences and medium-length explanatory sentences.
   - Start with shocking statements that create instant curiosity.
   - Repeat key numbers, names, and examples for emphasis.
   - Use rhetorical questions to create suspense and curiosity gaps.
   - Occasionally summarize before moving to the next point to reinforce understanding.

2. Retention & Engagement Tactics:
   - Layered explanation: explain concepts in simple terms first, then dive deeper.
   - "Wait, what?" moments every 20-30 seconds using surprising stats, contradictions, or counterintuitive facts.
   - Concrete examples: use real companies, real products, and real numbers.
   - Pattern recognition: show how a principle repeats across multiple companies or industries.
   - Psychological hooks: curiosity gap, loss aversion, social proof, instant gratification, and pattern completion.
   - Conversational tone: make it feel like the narrator is speaking directly to the viewer, with humor, authority, and insider knowledge.

3. Story Structure:
   - Hook (0-60s): Contradictory or shocking statement + statistic + central mystery
   - Central Mystery (60-120s): Present multiple examples that seem illogical, tease the psychological explanation
   - Psychology Breakdown (3-4min): Reveal 3 main psychological principles, explain in simple everyday terms, then show how companies exploit them
   - Business Application (1-2min): Show the specific tactics and numbers used by companies
   - Industry Pattern & Payoff (1-2min): Show how this principle repeats across industries, connect back to opening paradox, leave actionable insight

4. Voice & Style:
   - Conversational Authority: confident, engaging, slightly dramatic
   - Rapid but digestible info delivery
   - Use analogies and comparisons to everyday life
   - Bold statements backed by facts or examples
   - Questions for curiosity: "Have you ever noticed…?" / "Why would they…?"

TOPIC INPUT:
Use the following topic generated by the Topic Generator:
[TOPIC_INPUT]

Topic Title: {topic_title}
Hook Angle: {hook_angle}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
[/TOPIC_INPUT]

Your task:
Transform this topic into a viral 8-10 minute YouTube script that mirrors the sentence flow, pacing, and retention tactics of the viral example provided. Include:
- Short, punchy sentences for hooks
- Layered explanations (start simple, go deeper)
- Surprising statistics or facts every 20-30 seconds
- Real company/product names and numbers
- Analogies and metaphors for complex ideas
- Teasing psychological explanations before revealing them
- Questions that engage viewers’ curiosity
- Connect back to opening paradox at the end

Output in JSON format:
{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "[Opening hook sentence]"}},
        {{"speaker": "NARRATOR", "line": "[Supporting statistic or example]"}},
        ...
    ]
}}

GOAL:
Create the “I can’t stop watching this” effect, keeping viewers engaged from start to finish, using the same sentence flow, pacing, retention tactics, and layered explanations as the viral Buy Now Pay Later video example.
"""

# Claude 3.7 sonnet
business_psych_prompt3 = """
Viral Business Psychology Explainer Video Prompt

You are creating a highly engaging YouTube explainer video that reveals the hidden psychology behind major business decisions. Your script should feel like a friend revealing insider secrets about how companies manipulate consumers.

TOPIC INPUT:
Use the following topic:
[TOPIC_INPUT]
Topic Title: {topic_title}
Hook Angle: {hook_angle}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
[/TOPIC_INPUT]

VIRAL SCRIPT STRUCTURE:

1. VISUAL HOOK (0:00-0:15)
   Start with a reference to something viewers can see:
   "Look at this chart right here..."
   "See this product everyone loves? It's designed to trick you..."
   MUST include a specific, shocking number with comparison (e.g., "$5 trillion, enough to buy every NFL, NBA, and MLB team 10 times over")

2. PROBLEM STATEMENT (0:15-0:45)
   Immediately name the specific problem/trick/manipulation:
   "And to make matters worse, we are constantly surrounded by [specific psychological trick]."
   Use personal, conversational language with a first-person perspective:
   "When you buy a $100 pair of shoes and only pay $25 today... I don't know me 2 months from now. She can deal with that."

3. EXPLANATION WITH SPECIFICS (0:45-2:00)
   - Define the concept using REAL company names (never generic)
   - Include EXACT numbers/statistics/growth figures
   - Use simple, everyday language
   - Present clear comparisons between alternatives

4. CULTURAL CONTEXT (2:00-3:00)
   Name 3 specific cultural trends that make this psychological trick effective:
   "This explosion wasn't happening in a vacuum. It's actually part of three major cultural shifts..."
   Connect to viewers' everyday experiences.

5. THE PSYCHOLOGICAL BREAKDOWN (3:00-5:00)
   - Compare options using exact dollar amounts
   - Break down the psychology in simple terms ("pain of paying", "temporal discounting")
   - Use visual metaphors: "It's almost like they're targeting people that..."
   - Include 4 specific psychological tricks with real examples

6. RELATABLE CONSEQUENCES (5:00-7:00)
   - Include a direct quote/testimonial showing real impact
   - Show extreme examples that create "I can't believe that" moments
   - Use specific statistics about who gets affected most
   - Short, punchy sentences for emphasis

7. ACTIONABLE SOLUTION (7:00-8:00)
   - Provide clear, specific advice 
   - Address different scenarios for different viewers
   - Empower with simple, memorable guidelines
   - End with a tease to another video

KEY WRITING TECHNIQUES:
- Use short paragraphs (1-3 sentences maximum)
- Mix very short sentences (5-7 words) with medium ones
- Use casual phrases ("crap," "crazy," "chokehold")
- Ask direct questions: "Have you ever noticed...?"
- Create mini-cliffhangers between sections
- Use "and" to start sentences for flow
- Include phrases like "Don't get me wrong..." to create balance
- Reference visual elements throughout ("look at this," "as you can see")

TONE:
- Like a knowledgeable friend revealing insider secrets
- Confident but conversational
- Slightly outraged but ultimately empowering
- Never academic or overly formal

AVOID:
- Complex vocabulary when simple words work
- Long, winding sentences
- Hedging language ("perhaps," "maybe")
- Generic examples without specific names/numbers
- Slow buildup - deliver new information every 15-30 seconds

JSON FORMAT:
{
    "Characters": {"NARRATOR": "MAN1"},
    "story": [
        {"speaker": "NARRATOR", "line": "Look at this chart right here. [Company X] made $X billion last year using this one psychological trick."},
        {"speaker": "NARRATOR", "line": "And in 2024, they're using it more than ever before. The worst part? You're falling for it every single day."},
        {"speaker": "NARRATOR", "line": "When you [specific common action], you're actually triggering a psychological response that [Company X] has studied for years."}
    ]
}

Your script should make viewers feel like they've discovered hidden knowledge that explains why businesses behave in seemingly irrational ways.

"""

# Claude 4
business_psych_prompt4 = """
VIRAL BUSINESS PSYCHOLOGY SCRIPT GENERATOR
You are creating highly engaging YouTube explainer videos that reveal the psychology behind major business decisions using the proven viral formula below.

TOPIC INPUT:
[TOPIC_INPUT]
Topic Title: {topic_title}
Hook Angle: {hook_angle}
Central Mystery: {central_mystery}
Key Examples: {key_examples}
Psychological Principles: {psychological_principles}
Why It Works: {why_it_works}
[/TOPIC_INPUT]

VIRAL OPENING FORMULA (First 60 seconds):

SHOCK STATISTIC OPENER (0-15 seconds):
Start with a visual reference + overwhelming statistic:
"Look at this chart right here. [Shocking visual statistic that's almost incomprehensible]"
"This shows [specific data] over the last [timeframe]. And in [current year], [shocking number that's so big you need a crazy comparison]"

Example: "This shows total consumer debt in America over 10 years. In 2024, Americans owe $5 trillion - enough to buy every NFL, NBA, and MLB team 10 times over."

THE CONSPIRACY REVEAL (15-30 seconds):
Immediately pivot to the manipulation angle:
"And to make matters worse, we are constantly surrounded by psychological tricks and hidden fees designed to [specific harmful outcome]"
"The worst of these tricks: [specific business practice] that has been designed to take advantage of [specific vulnerable group]"

THE PERSONAL RELATABILITY HOOK (30-45 seconds):
Switch to first person, casual tone - make it personal:
"So when you [common scenario], and you only have to [small action], [immediate gratification happens]. [Product] shows up in 3 days later, [rationalization]. Why do I care if [future consequence]? I don't know me [time period] from now. She can deal with that."

THE DEFINITION BRIDGE (45-60 seconds):
Now explain what you're actually talking about:
"[Business practice] is a [type of system] offered by companies like [3 specific examples]. You'll typically see these [where they appear], offering you [the basic promise]."

CORE STRUCTURE (8-10 minutes total):

SECTION 1: THE HISTORICAL CONTEXT (1-2 minutes)
"These [current practice] aren't necessarily groundbreaking. In fact, [current thing] is kind of a newer modernized version of [old thing] that you would see at [specific old examples]."
- Explain the old way
- Why it disappeared  
- How the new version seems better
- The trap: "The only problem is..."

SECTION 2: THE EXPLOSION DATA (2-3 minutes)
"And that idea began hooking people in because [practice] has seen explosive growth..."
- Specific growth numbers with years
- "Going from $X in [year] to $Y in [recent year]"
- "Projected to reach $Z by [future year]"
- Then reveal the three cultural forces driving this

SECTION 3: THE PSYCHOLOGY BREAKDOWN (3-4 minutes)
"But why is this even a problem? If they're not charging [obvious cost], how can they actually be taking advantage of me?"

Use this pattern for each psychological principle:
- First acknowledge it seems harmless
- Then reveal the hidden mechanism
- Use specific numbers and percentages
- Include shocking statistics: "One in every three users actually ends up..."

SECTION 4: THE BUSINESS MODEL EXPOSE (4-5 minutes)
"So let's look at how these companies actually make money..."
Number each revenue stream clearly:
"First... Second... Third... And finally..."
Include specific percentages and dollar amounts for everything

SECTION 5: THE REAL-WORLD EXAMPLE (5-6 minutes)
Use a specific product everyone knows:
"So now let's look at buying a [specific expensive item] for $[amount]"
Present exactly three options with specific numbers
"Which sounds like the best deal to you?"

SECTION 6: THE MANIPULATION TACTICS (6-7 minutes)
"You see, brands have mastered psychological manipulation... And they do this through four key tricks:"
- Name each psychological principle clearly
- Give the scientific term: "what psychologists call..."
- Provide immediate real-world examples
- Use second person: "Have you ever noticed that..."

SECTION 7: THE PERSONAL STORIES (7-8 minutes)
Include real user testimonials or quotes:
"[Quote from real person about their experience]"
Connect to broader patterns with specific statistics

SECTION 8: THE PROTECTIVE ADVICE (8-9 minutes)
"So what do you do as a consumer?"
Provide clear, actionable rules
Use absolute language: "never spend more than you currently have"
Give specific scenarios: "If you start financing weekly expenses like..."

SECTION 9: THE CALLBACK CLOSER (9-10 minutes)
"But there you have it, the truth about [topic]"
Connect back to opening statistic
End with protection angle: "now you know how to protect yourself"

VIRAL RETENTION MECHANICS:

SENTENCE STRUCTURE:
- Short, punchy sentences mixed with longer explanatory ones
- Start many sentences with "And" or "But" for conversational flow
- Use specific numbers in almost every sentence
- Include parenthetical asides: "(which sounds great, but...)"

PACING TECHNIQUES:
- Layer information: basic concept → shocking truth → psychological mechanism → business model
- Use "But" and "And" transitions to maintain momentum
- Include micro-cliffhangers: "And it gets even worse..."
- Regular pattern breaks with personal anecdotes

SPECIFIC LANGUAGE PATTERNS:
- "Look at this..." (visual references)
- "And to make matters worse..." (escalation)
- "You see..." (explanation transitions)
- "In fact..." (contradiction reveals)
- "The only problem is..." (trap reveals)
- "And that's exactly what they want you to think because..."

ENGAGEMENT MULTIPLIERS:
- Use "you" constantly - make it personal
- Include specific brand names, not generic terms
- Give exact percentages and dollar amounts
- Reference specific time periods and dates
- Include relatable personal scenarios
- Use comparison metaphors everyone understands

JSON FORMAT:
{
"Characters": {"NARRATOR": "MAN1"},
"story": [
{"speaker": "NARRATOR", "line": "Look at this chart right here. This shows [specific data visualization]. And in 2024, [shocking statistic with absurd comparison]."},
{"speaker": "NARRATOR", "line": "And to make matters worse, we are constantly surrounded by psychological tricks designed to [specific harm]. The worst of these: [specific practice] designed to target [vulnerable group]."},
{"speaker": "NARRATOR", "line": "So when you [relatable scenario], and you only pay [small amount], [immediate gratification]. Why should I care about [future consequence]? I don't know me two months from now. She can deal with that."},
{"speaker": "NARRATOR", "line": "[Business practice] is [definition] offered by companies like [three specific examples]. But it's not quite that simple..."}
]
}

TARGET LENGTH: 8-10 minutes (approximately 1,200-1,500 words)

AVOID:
- Academic language - keep it conversational
- Slow builds - hook immediately with shocking data
- Generic examples - use specific brands and numbers
- Hedging language - make confident assertions
- Long paragraphs - break into digestible chunks
"""


