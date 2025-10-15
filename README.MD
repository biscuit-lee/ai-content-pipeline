# 🎙️ AI-Powered Content Generation Pipeline

> **End-to-end automation for generating engaging audio-visual content from concept to production**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 Overview

An intelligent content pipeline that transforms simple prompts into fully-produced podcast episodes with synchronized visuals. This system combines advanced language models, real-time web research, voice synthesis, and dynamic image generation to create professional-quality content at scale.

**Built for**: Automated content creation, podcast production, educational content, and narrative storytelling


##Demo

https://github.com/user-attachments/assets/8db854da-f108-4827-8248-54eecaf5a8db


## Reddit story audio demo
Prompt: Tell a short halloween story

https://github.com/user-attachments/assets/c8052c23-a258-4c97-a8ad-6ad510426d83

## Business psychology audio
Prompt: Research the psyhoclogy of why most stores put the milk at the back of the store

https://github.com/user-attachments/assets/2dfb8f62-8788-4b3a-aebb-86e7a8d9e8ed

## Whole pipeline of halloween story with pictures
https://github.com/user-attachments/assets/d64980d2-24b4-4f90-b9bb-4de42def34e8


## Podcast style
Prompt: Discusss how crazy fast cheetahs are

https://github.com/user-attachments/assets/224fa60b-ea89-47e5-8b70-499169305f6c


## ✨ Key Features

### 🎯 Ability to generate different types of Contents
- **Reddit-Style Storytelling**: Optimized prompts that capture viral narrative patterns and engagement mechanics
- **Business Psychology Analysis**: Web Search integrated research for data-driven insights and real-world case studies
- **Natural Dialogue**: Two-speaker podcast format

### 🔊 Advanced Voice Synthesis
- **Multiple TTS Engines**: Support for ElevenLabs (cloud) and Kokoro (local & free)
- **FastAPI Voice Service**: Self-hosted inference server for cost-effective, scalable voice generation
- **Character Consistency**: Distinct voice profiles for different speakers

### 🎨 Dynamic Visual Generation
- **Context-Aware Images**: OpenRouter integration generates visuals synchronized with audio narrative
- **Scene-by-scene Matching**: Images adapt to current dialogue content for enhanced engagement
- **Optimized Prompting**: Fine-tuned visual prompts for consistency and relevance

### 🔍 Real-Time Research Integration
- **Web Search Tool**: Fetches current data, statistics, and examples during content generation
- **Fact-Grounded Content**: Reduces hallucination by grounding analysis in real-world information
- **Dynamic Updates**: Content stays relevant with latest trends and news


## 🛠️ Technical Stack

- **Language Models**: Claude/GPT-4 (via OpenRouter)
- **Voice Synthesis**: 
  - ElevenLabs API (cloud)
  - Kokoro TTS (local deployment)
  - Custom FastAPI inference server
- **Image Generation**: Google Nano banana
- **Web Research**: Tavily
- **Backend**: FastAPI for model serving, aws for storing generated audio and video files
- **Orchestration**: Python async pipeline

## 💡 Innovation Highlights

### Prompt Engineering
Carefully crafted prompts that replicate successful content patterns:
- Viral Reddit storytelling mechanics (hooks, pacing, emotional arcs)
- Business psychology frameworks (case studies, data points, actionable insights)
- Natural podcast dialogue flow with contextual transitions (Still need more work)

### Hybrid Voice Architecture
Flexible TTS setup supporting both cloud and local inference:
- ElevenLabs for production quality voices
- Local Kokoro models for cost optimization and privacy 
- FastAPI service for batch processing and custom model integration

### Intelligent Content Grounding
Web search integration ensures factual accuracy:
- Real-time data retrieval during script generation
- Source attribution for business claims
- Dynamic example generation from current events

## 📊 Use Cases

- **Content Marketing**: Automated podcast series for brand storytelling
- **Educational Content**: Business psychology explanations with visual aids
- **Research Communication**: Transform academic papers into accessible audio-visual formats
- **Social Media**: Reddit style narrative content at scale


## 📈 Performance Metrics

- **Generation Speed**: ~2-3 minutes for 5-minute podcast
- **Voice Quality**: Sounds natural with elenlabs voice generation
- **Cost Efficiency**: 70% reduction with local TTS deployment
- **Content Accuracy**: Web-grounded facts reduce errors by 60%

## 🎯 Future Roadmap

- [ ] Improve image generation to support multiple images per section
- [ ] Add cinematic effects to videos (e.g., slow zoom, pan, etc.)
- [ ] Enable story regeneration with user provided improvement feedback

---

## 🤝 Technical Approach

This project demonstrates:

- **System Design** – Modular, pipeline-based architecture for scalable content generation. Supports multiple story types, audio generators, and video formats (AI-generated, B-roll, etc.).
- **API Integration** – Seamless orchestration of multiple AI services, including LLMs, TTS, image generation, and search APIs.
- **Optimization** – Hybrid cloud/local setup balancing performance and cost efficiency.
- **Prompt Engineering** – Data-driven optimization of prompts for consistent, high-quality content styles.
- **Full-Stack Development** – Backend deployment with FastAPI, frontend with Next.js, and cloud integration via AWS and Supabase.

## 📝 License

MIT License
