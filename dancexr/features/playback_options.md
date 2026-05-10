---
layout: release
title: Playback Options
locale: en-US
toc: true
---

# Playback Options

<!-- TODO: confirm exact UI labels. Drafted from release notes (2024.5, 2024.9). -->

Playback Options control the global behavior of the timeline: how audio and motion advance, when LipSync and spatialization kick in, and how the scene transitions between motions.

---

## Play / pause / timeline

Standard transport controls live here. The timeline at the bottom of the screen ties into these settings — long-press the timeline (more than half a second) to enter fine-adjustment mode for precise scrubbing (added in 2025.3, useful when authoring [keyframes](keyframe_animation)).

---

## Loop and sequence

- **Loop** — repeat the current motion / audio. Audio and motion can be looped independently (see [Audio Options](audio_options) for audio looping).
- **Sequence / random sequence** — when you load a folder of motions or [pose files](pose_files), playback advances through the list in order or shuffled.
- **Motion sequence blending** — fade between motions as the sequence advances (improved in 2024.5).

---

## Standard pose transition

When switching motions or jumping the timeline, the actor can transition through the **standard pose** before settling into the new motion. This gives complex physics components (cloth, soft body, hair) time to settle from a known state instead of glitching from one pose directly to another.

---

## LipSync

Toggle the global [LipSync](lipsync) switch here. The feature also requires per-actor opt-in via [Facial Control](facial_control).

---

## Spatialize

Anchor the audio source to an actor's head for 3D positional sound — see [Spatial Audio](spatial_audio). When **Spatialize** is on, choose which actor is the source.

---

## Audio / motion auto-sync

When audio time and motion time drift, choose whether to sync audio to motion or motion to audio (added in 2024.7). See [Motion Settings](motion_settings) for the corresponding per-motion behavior.

---

## Related pages

- [Audio Options](audio_options)
- [Motion Settings](motion_settings)
- [Music Timing](music_timing)
- [LipSync](lipsync)
- [Spatial Audio](spatial_audio)
- [Keyframe Animation](keyframe_animation)
