---
layout: release
title: Spatial Audio
locale: en-US
toc: true
---

# Spatial Audio

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. -->

Spatial Audio plays scene audio from a position in 3D space rather than as a flat stereo mix. Anchoring audio to an actor's head makes the sound move with that actor, which adds a strong sense of presence in VR and on multi-actor stages.

Added in **2024.9**.

---

## Enabling spatial audio

<!-- TODO: confirm exact menu path. Drafted from the release notes which name the option as "Spatialize" under Playback Options. -->

1. Open [Playback Options](playback_options).
2. Turn on **Spatialize**.
3. Choose an actor from the dropdown — that actor's **head position** becomes the audio source.

Audio then attenuates with distance and pans correctly relative to the camera or VR headset.

---

## Behavior

- The audio source follows the chosen actor's head bone as the actor moves.
- In VR, the effect uses head tracking, so turning your head changes left / right balance naturally.
- <!-- TODO: confirm whether stereo is preserved or audio is downmixed to mono at the source. -->
- <!-- TODO: confirm distance attenuation curve and whether it is configurable. -->

---

## Pairing with LipSync

Spatial Audio pairs naturally with the [audio-driven lip sync](lipsync) introduced in the same release: anchoring audio to an actor's head and driving that actor's mouth from the same audio gives a consistent "this actor is the one talking" effect.

---

## Limitations

<!-- TODO: confirm. Likely areas to verify: which audio types this applies to (music vs voice chat vs video), behavior with multiple actors, behavior on Android / Quest, behavior in AR mode. -->

---

## Related pages

- [Playback Options](playback_options)
- [Audio Options](audio_options)
- [LipSync](lipsync)
- [AI Voice Chat](ai_chat)
