# 🎙️ AI-Powered Content Generation Pipeline

## 🚀 Overview
  
A personal project exploring AI agents for autonomous content creation. Built to experiment with how AI can coordinate multiple tools—language models, text to speech, image generation, and web search to complete multi-step creative tasks with minimal guidance.

Focus Areas: Agent orchestration, multi-step reasoning, tool selection, and building pipelines where AI decides which tool to use and when.

##Demo

https://github.com/user-attachments/assets/8db854da-f108-4827-8248-54eecaf5a8db


## Reddit story audio demo
Prompt: Tell a short halloween story

https://github.com/user-attachments/assets/5b19c703-97da-40ab-8cb4-5c238306f54e


## Business psychology audio
Prompt: Research the psyhoclogy of why most stores put the milk at the back of the store

https://github.com/user-attachments/assets/2dfb8f62-8788-4b3a-aebb-86e7a8d9e8ed


## Podcast style
Prompt: Discusss how crazy fast cheetahs are

https://github.com/user-attachments/assets/224fa60b-ea89-47e5-8b70-499169305f6c

## Whole pipeline of halloween story with pictures
https://github.com/user-attachments/assets/d64980d2-24b4-4f90-b9bb-4de42def34e8



## ✨ Key Features

- **Storytelling:** Viral Reddit-style narratives with hooks and emotional arcs  
- **Dialogue Simulation:** Natural two-speaker podcast conversations  
- **Voice Synthesis:** Supports cloud (ElevenLabs) and local (Kokoro) TTS with FastAPI inference  
- **Dynamic Visuals:** Context-aware images synchronized to the audio  
- **Fact-Grounded Content:** Real-time web search integration for accuracy  

---

## 🛠️ Tech Stack

- **Language Models:** Claude / GPT-4 via OpenRouter  
- **Voice Synthesis:** ElevenLabs, Kokoro, FastAPI server  
- **Image Generation:** Google Nano Banana  
- **Web Research:** Tavily API  
- **Backend:** FastAPI + AWS S3 storage  
- **Pipeline Orchestration:** Python async workflows  

---

## 💡 Highlights

- **Prompt Engineering:** Optimized prompts for storytelling, research, and natural dialogue  
- **Hybrid TTS Architecture:** Combines cloud & local solutions for quality, cost, and privacy  
- **Modular Design:** Easy to extend to new story types, text-to-speech providers or audio-visual formats



## 🎯 Future Roadmap

- [ ] Improve image generation to support multiple images per section
- [ ] Add cinematic effects to videos (e.g., slow zoom, pan, etc.)
- [ ] Enable story regeneration with user provided improvement feedback

---

## 🤝 Technical Approach

This project demonstrates:

- **Agentic System Design** – Modular agent architecture where autonomous reasoning guides multi-step content generation workflows. The agent decides which tools to invoke, when to perform web research, and how to adapt the pipeline based on content type.  
- **Tool Orchestration** – Seamless integration of multiple AI services (LLMs, TTS, image generation, search APIs) as agent tools, with context-aware decision-making about which tools to use at each stage.  
- **Multi-Step Reasoning** – Agent breaks down complex prompts into executable sub-tasks (research → scripting → audio synthesis → visual generation), maintaining semantic context throughout the pipeline.  
- **Prompt Engineering for Agents** – Iterative optimization of system prompts to guide agent behavior while preserving flexibility. Designed prompts that enable consistent outputs across storytelling, educational, and conversational formats.  
- **Full-Stack Development** – Backend deployment with FastAPI for async task orchestration, Next.js frontend for agent interaction, and cloud integration via AWS and Supabase for state management.  

## 📝 License

MIT License
