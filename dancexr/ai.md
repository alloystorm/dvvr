---
layout: release
title: AI in DanceXR
locale: en-US
toc: true
---

# AI in DanceXR

DanceXR has several AI-driven features. Most of them go through one local backend — **DanceXR Operator** — which runs on your hardware and bundles voice synthesis, large language model chat, and supporting services into a single process. This page is the overview; each feature has its own detailed page.

For terms (Operator, TTS, STT, persona, template), see [Concepts & glossary](/dancexr/concepts#ai-backends).

---

## The big picture

```
┌──────────────────────────────────────────────────────────┐
│  DanceXR (the game)                                      │
│                                                          │
│   AI Voice Chat ──┐                                      │
│   Discovery ──────┼─→ HTTP API (default :8110) ─→ Operator
│   (other)  ───────┘                                      │
│                                                          │
│   Auto Dance 3 ── runs in-process (no external backend)  │
└──────────────────────────────────────────────────────────┘
```

- **Operator** is the local AI backend. Runs as a separate process alongside DanceXR. See [DanceXR Operator](/dancexr/features/operator).
- **AI Voice Chat** is the user-facing chat experience that consumes Operator. See [AI Powered Voice Chat](/dancexr/features/ai_chat).
- **Discovery** is an AI-assisted asset acquisition tool. See [Discovery app](/dancexr/features/discovery).
- **Auto Dance 3** is procedural and runs inside DanceXR; no external AI needed. See [Auto Dance 3](/dancexr/features/autodance3).

Everything is local-first. After the initial model download, no internet connection is required.

---

## DanceXR Operator

[Operator](/dancexr/features/operator) is the dedicated local backend introduced in **2026.5**. It bundles:

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

<!-- TODO: minimum VRAM, RAM, OS, GPU requirements once confirmed. -->

---

## AI Voice Chat

[AI Voice Chat](/dancexr/features/ai_chat) is the conversational layer. With Operator running, you can:

- Talk to characters in natural language, with multi-turn memory.
- Hear them reply in synthesized voice, with automatic lip-sync.
- Use voice input — built-in Whisper handles speech-to-text.
- Configure characters with personas, templates, and personality descriptions.

Pro tier on the PC build; supported on Quest, Android, and iOS with platform-specific limits on voice features.

### Templates and personas

- **Templates** ([chat/templates](/dancexr/preparecontent)) — the prompt scaffold the LLM uses. Plain text, easy to modify.
- **Personas** ([chat/personas](/dancexr/preparecontent)) — personality descriptions applied to a character. Supports importing TavernAI-style PNG character cards.

### Legacy local backends

[AI Voice Chat](/dancexr/features/ai_chat) still supports OobaBooga, LM Studio, and Ollama for users who want a custom local LLM stack. These are alternatives to Operator, not the recommended path. New features (memory compression, scene awareness, session persistence) are tuned for Operator first.

<!-- TODO Phase 3: split ai_chat.md into "AI Chat (Operator)" as primary and "AI Chat (legacy backends)" so the recommended flow is not buried under setup instructions for older tools. -->

---

## Discovery app

[Discovery](/dancexr/features/discovery) is an AI-assisted asset acquisition tool — find, preview, and import models and motions without manually scouring sites. Added in 2025.6.

<!-- TODO: confirm whether Discovery uses Operator or a separate backend. -->

---

## Auto Dance — procedural, not LLM

The Auto Dance family generates procedural dance motion from a motion library. It is sometimes grouped with "AI features" because it is generative, but it does **not** use Operator or an LLM:

- [Auto Dance](/dancexr/features/autodance) — original generator.
- [Auto Dance 2](/dancexr/features/autodance2) — improved variation.
- [Auto Dance 3](/dancexr/features/autodance3) — current default; rhythm analysis, beat-aware transitions.

Use Auto Dance 3 unless you have a specific reason to pick an earlier generation.

Reads [music timing](/dancexr/features/music_timing) to sync to the beat.

---

## Setup paths

| You want | Do this |
|---|---|
| The recommended modern AI chat | Install [Operator](/dancexr/features/operator) next to DanceXR; enable AI Chat |
| Voice chat with your own LLM stack | Configure [AI Voice Chat](/dancexr/features/ai_chat) → Local WebUI; point at LM Studio / Ollama / OobaBooga |
| Procedural dancing | Enable [Auto Dance 3](/dancexr/features/autodance3) on the actor |
| To find and import assets | Use the [Discovery app](/dancexr/features/discovery) |

---

## Common problems

| Symptom | Where to look |
|---|---|
| AI Chat does not respond | Verify Operator is running (system tray icon); check the [Operator web interface](/dancexr/features/operator#web-interface) |
| Generation is very slow | LLM model is too large for your hardware — pick a smaller model in Operator's web UI |
| TTS produces silence on Quest / Android | Voice features are platform-limited; replies may be text-only |
| Voice recognition is slow on Quest | Use [Manual mode](/dancexr/features/ai_chat#manual-mode) instead of automatic |
| Wrong language voice | Configure [Language matching & fallback](/dancexr/features/ai_chat#language-matching--fallback) |

---

## Related pages

- [Concepts & glossary](/dancexr/concepts#ai-backends)
- [DanceXR Operator](/dancexr/features/operator)
- [AI Powered Voice Chat](/dancexr/features/ai_chat)
- [Discovery app](/dancexr/features/discovery)
- [Auto Dance 3](/dancexr/features/autodance3)
- [Motion system](/dancexr/motion) — Auto Dance is part of motion
