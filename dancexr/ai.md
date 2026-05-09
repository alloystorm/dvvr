---
layout: release
title: AI in DanceXR
locale: en-US
toc: true
---

# AI in DanceXR

DanceXR has several AI-driven features. Most of them go through one local backend — **DanceXR Operator** — which runs on your hardware and bundles voice synthesis, large language model chat, and supporting services into a single process. This page is the overview; each feature has its own detailed page.

For terms (Operator, TTS, STT, persona, template), see [Concepts & glossary](concepts#ai-backends).

---

## The big picture

- **Operator** is the local AI backend. Runs as a separate process alongside DanceXR. See [DanceXR Operator](features/operator).
- **AI Voice Chat** is the user-facing chat experience that consumes Operator. See [AI Powered Voice Chat](features/ai_chat).


---

## DanceXR Operator

[Operator](features/operator) is the dedicated local backend introduced in **2026.5**. It bundles:

- **TTS** — Kokoro, for converting text replies to voice.
- **LLM** — llama.cpp, for chat generation.
- **HTTP API** — unified endpoint at `http://localhost:8110`.
- **Web interface** — model management, TTS preview, benchmarking.

Operator starts automatically when you enable AI Chat in DanceXR, and shuts down on its own after DanceXR exits. You can also start it manually from `Operator.exe`.

### Why Operator and not a cloud service

- Privacy — chat history never leaves your machine.
- No subscription or rate limits.
- Stable foundation for the longer, scene-aware roleplay sessions in 2026.5+.
- One install handles voice and chat together.

The trade-off is hardware: you need a gaming-class GPU and enough RAM/VRAM to run the chosen LLM model.

Recommended to have at least 16GB RAM and a GPU with 6GB+ VRAM for a good experience. You can choose smaller models in Operator's web UI for lower-end hardware, but performance will vary.
