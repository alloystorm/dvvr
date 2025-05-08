---
locale: en-rUS
layout: single
title: Playback Options
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/motion/motion_loader) | [繁中](/tw/dancexr/menu/2025.5/motion/motion_loader) | [日本語](/jp/dancexr/menu/2025.5/motion/motion_loader) | [한국어](/kr/dancexr/menu/2025.5/motion/motion_loader) | [简中](/zh/dancexr/menu/2025.5/motion/motion_loader)

[Audio / Motion](../menu#Audio / Motion) > Playback Options

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| ☐ Auto-Load Actors | [OFF] | Automatically load actors to match the number of motion tracks and assign different motion for each actor
| ☐ Auto-Assign Camera | [OFF] | Automatically assign camera motion if available
| > Playback Mode | **List Once** | List Once, Single, Loop List, Loop Single, Shuffle,  |
| > Remix Mode | **Synchronized** | Continue Next, Synchronized, Loop, Shuffle Next,  |
| ⊖ Speed | [1] (0.5 ~ 2) | Change speed of audio. This also affects motion and physics speed
| ☑ Pitch Shift | [ON] | Adjust audio to match the original pitch after changing speed
| > Auto Sync Mode | **Off** | Off, Move Audio, Move Motion,  |
| ⊖ Auto Sync Threshold | [0.05] (0 ~ 0.2) | Automatically sync motion and audio when time differences exceed this amount. In seconds.
| ☑ Timeline Fine Adjust | [ON] | Long press on the timeline to fine adjust playback time.
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Default Timing** | | 
| ├─⊖ Offset | [0] (Unlimited) | 
| ├─⊖ BPM | [120] (1 ~ 240) | Beats per minute
| ├─⊖ Beat Offset | [0] (0 ~ 1) | 
| ├─⊖ Beats Per Phrase | [8] (4 ~ 64) | 
| ├─⊖ Phrase Begin | [0] (0 ~ 32) | 
| ├─ Copy Auto BPM || Set BPM from automatically detected value.
| └─ Tap Beats || Set BPM by tapping while the music is playing
| ☑ **Audio Analysis** | | 
| ├─☑ Enable | [ON] | 
| ├─⊖ Processing Rate | [45] (1 ~ 90) | Rate of audio processing. Since the system only updates audio data at a fixed rate, usually no need to go above 45 FPS.
| ├─⊖ Band Selection | [0] (0 ~ 1) | Select the range of bands to calculate loudness level
| ├─⊖ Smooth | [0.25] (0 ~ 1) | Smooth output of loudness value
| └─⊖ Fade In Out | [0] (0 ~ 0.2) | Fade in and out audio level at the beginning and end of the audio.
| ☐ **Lip Sync** | | 
| ├─☐ Enable | [OFF] | 
| └─⊖ Lip Sync Smoothing | [0.05] (0 ~ 0.1) | 
| ☐ **Spatialize** | | 
| ├─☐ Enable | [OFF] | 
| ├─⊖ Spatial Blend | [0] (0 ~ 1) | Blend the 3D effect of the spatial audio
| ├─☐ Follow Actor | [OFF] | 
| └─> Select Actor |  |  |
