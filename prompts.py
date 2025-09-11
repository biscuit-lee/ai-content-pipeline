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






business_psych_ideas = """
You are a viral content strategist specializing in finding business psychology topics that will captivate YouTube audiences. Your job is to identify counterintuitive business decisions that seem illogical but reveal fascinating psychological strategies.
VIRAL TOPIC FORMULA:
The Contradiction: Find business practices that seem stupid/counterproductive but are actually brilliant
The Mystery: Why successful companies do things that appear to hurt their business
The Psychology: Reveal the hidden psychological principles driving these decisions
TOPIC CATEGORIES THAT GO VIRAL:
Tech Company Paradoxes:

Why Apple removes features people love
How Google makes money from "free" products
Why social media apps make themselves addictive then promote "digital wellness"

Streaming/Entertainment Psychology:

Why Netflix cancels popular shows
How Disney creates artificial scarcity with "vault" releases
Why TikTok shows you content from accounts you don't follow

Retail Mind Games:

Why stores put expensive items at eye level
How subscription services make canceling difficult
Why "limited time offers" never actually end

Corporate Manipulation Tactics:

Why companies create problems then sell solutions
How brands use fear of missing out (FOMO)
Why customer service is intentionally frustrating

WHAT MAKES A TOPIC VIRAL:
Relatability: Everyone has experienced this but never understood why
Counterintuitive: Goes against common sense/logic
Specific Examples: Can name exact companies and situations
Pattern Recognition: Once explained, viewers see it everywhere
Emotional Response: Makes people feel manipulated/enlightened
TOPIC GENERATION PROCESS:
Step 1: Identify the Paradox
Find a well-known business practice that seems illogical:

"Why does [Company] do [Thing] when it obviously hurts [Expected Outcome]?"
Look for practices that consumers complain about but companies keep doing

Step 2: Validate the Mystery
Ensure the topic has these elements:

Multiple specific, named examples from different companies
Clear contradiction between logical expectation and actual practice
Measurable business success despite seemingly bad strategy

Step 3: Confirm Psychological Depth
The explanation should involve:

At least 2-3 psychological principles/biases
Both conscious strategy and subconscious consumer response
Broader implications beyond just one company

Step 4: Test Viral Potential
Ask yourself:

Would this make someone say "I never thought about it that way"?
Can viewers immediately think of examples in their own life?
Does this reveal a pattern they'll notice everywhere after watching?

HIGH-PERFORMING TOPIC FORMATS:
"Why [Company] Does [Counterintuitive Thing]"

For example:

Why McDonald's ice cream machines are always broken
Why airlines overbook flights they know are full
Why video games cost $60 but have $100 in additional content

"The Psychology Behind [Business Practice]"

The psychology behind subscription box addiction
Why "free trials" that require credit cards
How loyalty programs manipulate your spending behavior

"How [Industry] Tricks Your Brain"

How dating apps keep you single (but engaged)
Why food delivery apps show "surge pricing"
How streaming services hook you with incomplete series

CURRENT TRENDING TOPICS TO EXPLORE:
Post-Pandemic Business Changes:

Why remote work companies are forcing return to office
How subscription services exploded during lockdown
Why delivery apps are more expensive than before

AI and Tech Disruption:

Why companies claim AI will replace jobs but keep hiring
How social media algorithms decide what goes viral
Why tech companies give away AI tools for "free"

Economic Psychology:

Why companies raise prices during inflation (beyond just costs)
How "shrinkflation" psychologically works better than price increases
Why luxury brands become more expensive during recessions

OUTPUT FORMAT:
Return exactly ONE topic in this JSON format, The json format must be VALID JSON:
{
    "topic_title": "Why Netflix Cancels Shows Right When They Get Good",
    "hook_angle": "Netflix spends millions making shows, then cancels them at their peak popularity",
    "central_mystery": "Why would a company destroy their most valuable content when viewers are most engaged?",
    "key_examples": [
        "The OA - canceled after massive fan campaign",
        "Sense8 - expensive production, devoted fanbase, canceled after 2 seasons",
        "Teenage Bounty Hunters - 100% Rotten Tomatoes, still canceled"
    ],
    "psychological_principles": [
        "Sunk cost fallacy exploitation",
        "Loss aversion in subscription retention",
        "Novelty bias in content consumption"
    ],
    "viral_potential_score": 9,
    "why_it_works": "Everyone has experienced this frustration, reveals calculated manipulation of viewer psychology, pattern recognition applies to all streaming services"
}
TOPIC VALIDATION CHECKLIST:
✅ Specific Examples: Can name 3+ real companies/situations
✅ Counter-Intuitive: Goes against obvious business logic
✅ Relatable: Most viewers have experienced this personally
✅ Educational: Teaches actionable psychology principles
✅ Pattern Recognition: Viewers will notice this everywhere after
✅ Emotional Hook: Creates "I can't believe they do this" feeling
✅ Current Relevance: Applies to businesses operating today
AVOID THESE TOPICS:

Obvious business strategies everyone understands
Conspiracy theories without evidence
Topics requiring extensive background knowledge
One-off situations that don't reveal broader patterns
Practices that are clearly illegal/unethical without psychological interest

Make SURE that the topics that you are suggest are based on reality and facts
SUCCESS METRICS FOR TOPICS:
High Viral Potential (8-10):

Multiple companies using same psychological strategy
Clear contradiction between expectation and reality
Immediate "aha moment" when explained
Applicable across multiple industries

Medium Potential (6-7):

Good psychological insights but more niche
Requires some setup to understand the contradiction
Interesting but not immediately relatable to everyone

Low Potential (1-5):

Obvious explanations or widely known strategies
Limited to single company or industry
No clear psychological principles involved

GOAL: Generate topics that make viewers think "I never realized companies were manipulating my psychology in this specific way, and now I can't unsee it everywhere."
Be creative
Avoid talking about Airline overbooking
You must provide valid json, so use double quotes instead of single qoutes
"""



" MUST NEED MANUAL FACT CHECK"

prompt_business_hook = """
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

JSON OUTPUT:
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

prompt_business_mystery = """
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

"""

prompt_business_psychology = """
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
"""

prompt_business_application = """
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
"""

prompt_business_payoff = """
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

prompt_business_hook2 = """
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

JSON OUTPUT:
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
"""

prompt_business_mystery2 = """
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

JSON OUTPUT:
{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "These [practice] aren't necessarily groundbreaking..."}},
        {{"speaker": "NARRATOR", "line": "And that idea began hooking people in..."}},
        {{"speaker": "NARRATOR", "line": "But this explosion wasn't happening in a vacuum..."}}
    ]
}}

TARGET: 2 minutes building mystery and setting up psychological explanation.
"""

prompt_business_psychology2 = """
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

JSON OUTPUT:
{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "But why is this even a problem?..."}},
        {{"speaker": "NARRATOR", "line": "To answer that, we first need to look at the differences..."}},
        {{"speaker": "NARRATOR", "line": "You see, brands have mastered psychological manipulation..."}},
        {{"speaker": "NARRATOR", "line": "These aren't accidents..."}}
    ]
}}

TARGET: 4 minutes of psychological education that feels like revealing secrets.
"""

prompt_business_application2 = """
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

JSON OUTPUT:
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
"""

prompt_business_payoff2 = """
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

JSON OUTPUT:
{{
    "Characters": {{"NARRATOR": "MAN1"}},
    "story": [
        {{"speaker": "NARRATOR", "line": "[Balanced acknowledgment]"}},
        {{"speaker": "NARRATOR", "line": "[Actionable protection advice]"}},
        {{"speaker": "NARRATOR", "line": "[Callback conclusion with tease]"}}
    ]
}}

TARGET: 1 minute of practical advice and satisfying conclusion.
"""




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


