---
layout: release
title: LipSync
locale: en-US
toc: true
---

# LipSync

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. May overlap with content already in facial_control.md — fold one into the other if appropriate. -->

LipSync drives an actor's mouth shapes from an audio signal in real time, so characters appear to speak or sing along with whatever audio is playing. Unlike the older lip-sync that lived inside [AI Voice Chat](ai_chat), this system is **available on all platforms**, including Android and Quest.

Added in **2024.9**.

---

## Enabling LipSync

<!-- TODO: confirm exact UI path. -->

1. Turn LipSync on globally in [Playback Options](playback_options).
2. For each actor that should move its mouth, open [Facial Control](facial_control) and enable **LipSync**.

Both toggles are required: the global toggle controls whether the audio is analyzed at all; the per-actor toggle controls which actors react to it.

---

## Pairing with Spatial Audio

LipSync pairs naturally with [Spatial Audio](spatial_audio) — anchor the audio to an actor's head and enable LipSync on that same actor, and the result reads as "this character is speaking."

---

## Pairing with AI Voice Chat

[AI Voice Chat](ai_chat) drives speech audio that the LipSync system can analyze the same way as music or video audio. <!-- TODO: confirm whether AI Voice Chat uses LipSync directly, or its own internal mouth driver, or both. -->

---

## Settings

<!-- TODO: list. Likely candidates: sensitivity / gain, smoothing, mouth-open intensity, which morph(s) drive what. -->

---

## Limitations

<!-- TODO: confirm. Areas to verify:
- Does it require specific blendshapes / morphs (a / i / u / e / o)? What if the model lacks them?
- Does it work with PMX, XPS, and FBX equally?
- Latency on Android / Quest. -->

---

## Related pages

- [Playback Options](playback_options)
- [Facial Control](facial_control)
- [Spatial Audio](spatial_audio)
- [AI Voice Chat](ai_chat)
- [Blink, Breathing & Eye Contact](eyecontact)
