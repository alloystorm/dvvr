---
layout: release
title: Auto Dance 3
locale: en-US
toc: true
---

# Auto Dance 3

<!-- TODO: confirm exact UI labels for the actor pose / motion sections. Drafted from release notes (2024.3, 2025.5, 2025.7) and the SM3 documentation. -->

Auto Dance 3 is the **current-generation** procedural dance generator. It shares its motion-control plumbing with [Sex Motion 3](sex_motion_3) but without the NSFW layers, and integrates with the realtime audio analyzer (beat detection added in 2025.5) so dance phrasing tracks the music in real time.

This is the default Auto Dance to use for new projects.

---

## What sets Auto Dance 3 apart

- **Highly customizable.** Hand pose, leg pose, body pose, and motion patterns can all be tuned individually.
- **Reproducible random.** Each generated sequence has a seed; save and share a seed (added 2024.3) to reproduce the exact same sequence.
- **Realtime beat reactive.** Uses the realtime audio analyzer with beat detection; you do not need precomputed BPM.
- **Spring / damping motion curves.** From 2025.7, motions are smoothed by simulated spring force and damping for a more natural feel.

---

## Actor pose

Set the actor's base pose before the procedural motion runs:

- **Hands** — pose for both hands (or per-hand if asymmetric).
- **Legs** — leg / feet pose.
- **Body** — torso pose, bend, and orientation.

The procedural motion is layered on top of this base pose, so a clean base produces cleaner-looking dance.

---

## Motion control

- **Pattern source** — random from built-in patterns, random from your saved presets, or fully manual curves.
- **Random seed** — fixes the random sequence so it can be reproduced.
- **Speed** — manual or driven by audio level.
- **Variety / transition** — controls how often the generator switches phrases and how smoothly it transitions.

---

## Pairing with audio

The most natural results come from setting [Music Timing](music_timing) on the dance set so the generator has a BPM to lock to. With BPM set, the generator can phrase moves at musically meaningful intervals (typically 4 / 8 / 16 beats) instead of drifting.

---

## Related pages

- [Auto Dance](autodance) — generation 1
- [Auto Dance 2](autodance2) — generation 2
- [Sex Motion 3](sex_motion_3) — shared motion control system, NSFW
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)
