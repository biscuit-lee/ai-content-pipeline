# Automated YouTube Story Generator

This project is a web application that automates the creation of YouTube-ready videos from a single prompt. It generates a script, synthesizes voice lines, and pairs them with AI-selected visuals, all optimized for engagement and retention.

## Features

- **Prompt-to-Video Pipeline:** Enter an idea or prompt, and the app generates a complete YouTube script.
- **Script Generation:** Uses advanced LLMs to write engaging, viral-ready scripts.
- **Voice Synthesis:** Converts script lines into realistic voiceovers using TTS APIs.
- **Visual Pairing:** Automatically selects and sequences AI-generated or stock visuals to match the narration.
- **Timeline Management:** Aligns audio and visuals for seamless video output.
- **Subtitles:** Supports subtitle generation and burning into final videos.
- **Self-Improvement:** Optionally analyzes uploads to improve future content.
- **Multi-Character Support:** Allows overlapping dialogue and multiple speakers.
- **Background Music & SFX:** Add music and sound effects for enhanced production value.
- **Flexible Visuals:** Supports various backgrounds (image sequences, gameplay, static effects, etc.).

## Installation (Linux)

Install dependencies:
```sh
sudo apt install ffmpeg
```
Other dependencies are managed via `requirements.txt` in the `backend/` folder.

## Usage

1. Clone the repository.
2. Set up environment variables in `backend/.env` for API keys (TTS, LLM, etc.).
3. Run the backend pipeline (`main.py`) to generate scripts, audio, and visuals.
4. Use the frontend to interactively generate and preview story ideas.
5. Final videos are saved in the `output/` directory.

## Roadmap / Planned Features

- Automated self-analysis and improvement after each upload.
- Enhanced background music and sound effects.
- Improved subtitle handling and visual diversity.
- Support for overlapping character dialogue.
- More flexible visual backgrounds.

## License

---

For more details, see [backend/main.py](backend/main.py) and [prompts.py](backend/prompts.py).


# INSTALL (LINUX)
sudo apt install ffmpeg



# Add features

 - Self analyizing, improving with  every upload
 - add bg music, bg sfx 
 - Multiple characters can overlap speaking  
 - maybe add better background pic        
 - SUBTITLES 
 - add multiple type of visuals ; (sequence of images, gameplay bg, static rain whateer bg)