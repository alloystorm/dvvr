---
locale: en-US
layout: single
title: DanceXR Operator
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/operator) | [繁中](/tw/dancexr/features/operator) | [日本語](/jp/dancexr/features/operator) | [한국어](/kr/dancexr/features/operator) | [简中](/zh/dancexr/features/operator)

# DanceXR Operator
DanceXR Operator is the dedicated AI backend for DanceXR, providing advanced voice synthesis, large language model (LLM) chat, and dynamic roleplay features for the game.


## Overview
Operator runs as a local server, bundling Kokoro TTS and llama.cpp LLM behind a unified HTTP API, and is designed to work seamlessly alongside the DanceXR Unity client.

With Operator, you can generate lifelike character voices, enable in-game AI conversations, and manage custom roleplay scenarios using flexible prompt templates. The server supports multiple languages and voices, and includes tools for model management and benchmarking.

Operator is easy to set up and runs entirely on your own hardware—no internet connection required after initial model download. DanceXR Operator brings powerful AI-driven features to your DanceXR experience.


## Installation
Simply download and install next to your DanceXR folder.

Recommended folder structure:
```
DanceXR Root Folder
├─ content
├─ DanceXR HD Pro_WIN64
├─ DanceXR RT Pro_WIN64
├─ [other DanceXR versions]
└─ Operator
   ├─ Operator.exe
   └─ [other Operator files]
```

Download Link:
https://github.com/alloystorm/dvvr/releases/download/operator1.0/operator-install-lite-1.0.exe


## Usage

### Automatic Startup
When installed in the above structure, the Operator will automatically start when you enable AI Chat in DanceXR. 

A system tray icon will appear, allowing you to access Operator's web interface and monitor its status. 

It will then shut down itself after you exit the DanceXR for a while.


### Manual Startup
You can also start Operator manually by running `Operator.exe`. 

The system tray icon will appear, and you can access the web interface or shut it down by clicking on the icon.


### Web Interface
By default, Operator's web interface is accessible at `http://localhost:8110`. It has the following sections:

- **Model Management**: Download and switch LLM models
- **TTS Preview**: Preview TTS voices
- **Benchmarking**: Run performance benchmarks for LLM