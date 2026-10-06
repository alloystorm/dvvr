---
layout: release
title: LipSync
locale: en-US
toc: true
---

# LipSync

LipSync analyzes playback audio and drives the actor's A, I, U, E and O mouth shapes. It can make an actor sing or speak along with the track without a separate mouth animation.

## Enable it

1. In [Playback Options](playback_options), enable the **Lip Sync** group.
2. In the actor's [Facial Control](facial_control), enable **Use Lip Sync**.
3. Play audio with a clear vocal part and watch the mouth. Adjust **Lip Sync Smoothing** in Playback Options if transitions are too abrupt or too slow.

The playback toggle enables the analyzer; the actor toggle applies its result to that actor. Several enabled actors can react to the same playback signal.

## If the mouth does not move

Check both toggles and confirm audio is playing. Then test the individual vowel expressions in Facial Control. If those do not work manually, the model's expression mapping needs attention: audio analysis cannot create missing mouth morphs or an unmapped facial rig. For XPS facial controls, also check the Disable switch and mouth extent.

Disable Use Lip Sync when arranging a manual mouth expression so the audio driver does not keep replacing the vowel values.

## Spatial audio and chat

[Spatial Audio](spatial_audio) moves the playback sound source to an actor when configured to follow it; it does not select which actors use lip sync. Set the two features independently.

[AI Voice Chat](ai_chat) uses a separate speech-audio lip-sync driver for the speaking actor. Playback audio settings should not be treated as the sole control for chat speech.
