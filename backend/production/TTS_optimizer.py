from backend.prompts import *
from backend.agents.base_agent import Agent
from dotenv import load_dotenv

class TTS_optimizer(Agent):
    def __init__(self):
        super().__init__()
        load_dotenv()
    
    def optimize_tts_text(self, text: str) -> str:
        # Placeholder implementation for optimizing TTS text
        print("Optimizing TTS text...",     text)
        prompt = self.get_prompt().format(input_json=text)
        optimized_text = self.ask_llm_no_search(prompt)
        
        print("Optimized TTS text:", optimized_text)
        return optimized_text
    
    

    def get_prompt(self):
        prompt_podcast_enhancer = """
            You are an editor specializing in enhancing **two-person podcast scripts** using **ElevenLabs v3 audio tags**.

            Your goal is to take the following JSON podcast script, **preserve the characters and story**, and enhance it by:

            - Adding appropriate audio tags: [thoughtful], [serious], [curious], [sighs], [short pause], [long pause], [excited], [laughs], [chuckles], [groans]
            - Using ellipses (…) for hesitation or suspense
            - Adding subtle emphasis via CAPITALIZATION
            - Making the conversation feel **natural, emotional, and immersive**
            - Keeping the **same JSON structure** — do not rename, reorder, or remove lines.
            - Must be valid JSON, so use double quotes for strings and keys.
            Here is the input JSON:
            {input_json}

            Return the enhanced script in the same JSON format, with audio tags included. Example output:
            **JSON FORMAT:**
            {{
                "Characters": {{"HOST1": "WOMAN1", "HOST2": "MAN2"}},
                "story": [
                    {{"speaker": "HOST1", "line": "[thoughtful] Okay, I still get chills thinking about this — you remember that night I told you about?"}},
                    {{"speaker": "HOST2", "line": "Wait, the one with the knocking sound at 3 A.M.?"}},
                    {{"speaker": "HOST1", "line": "Yeah. Every night, same time. I even tried recording it once."}},
                    {{"speaker": "HOST2", "line": "And did you catch anything?"}},
                    {{"speaker": "HOST1", "line": "That’s the thing... I did. But not what you’d expect."}}
                ]
            }}
            """
        return prompt_podcast_enhancer


if __name__ == "__main__":
    load_dotenv()
    voice_ids = {
        "MAN1": "21m00Tcm4TlvDq8ikWAM",
        "MAN2": "AZnzlk1XvdvUeBnXmlld",
        "WOMAN1": "EXAVITQu4vr4xnSDxMaL",
        "WOMAN2": "ErXwobaYiN019PkySvjV",
    }
    model_id = "eleven_multilingual_v2"
    tts_optimizer = TTS_optimizer()
    
    sample_text = """
    [
        {"speaker": "MAN1", "text": "Hey, did you hear about the new AI that can write stories?"},
        {"speaker": "WOMAN1", "text": "Yeah, it's pretty amazing! I wonder if it can capture human creativity."},
        {"speaker": "MAN2", "text": "I think it can, but it still needs a human touch to make it truly special."},
        {"speaker": "WOMAN2", "text": "Absolutely! AI can assist, but the heart of storytelling is human emotion."}
    ]
    """
    optimized_text = tts_optimizer.optimize_tts_text(sample_text)
    print(optimized_text)