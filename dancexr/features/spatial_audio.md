---
layout: release
title: Spatial Audio
locale: en-US
toc: true
---

# Spatial Audio

Spatial audio gives playback sound a position in the scene. Use it when the track should sound as though it comes from a character, especially while viewing the scene in VR.

## Follow an actor

1. Open the **Spatialize** group in [Playback Options](playback_options) and enable it.
2. Increase **Spatial Blend** to introduce the 3D effect. At zero, the source remains a 2D mix even when the group is enabled.
3. Enable **Follow Actor**, then use **Select Actor** to choose the source actor.
4. Play the track and move the camera or headset around that actor to compare the result.

Follow Actor updates the source position from the selected actor's tracked head. Selecting an actor alone does not enable following. After removing or reordering actors, check that the selector still points to the actor you intend.

## Combine with mouth movement

Enable [LipSync](lipsync) on the actor that should appear to sing or speak. Spatialize and LipSync are independent: one positions sound, while the other applies mouth expressions. Choosing a spatial source does not automatically turn other actors' lip sync off.

For music that should fill the scene rather than come from one character, lower Spatial Blend or disable Spatialize. Compare from your normal viewing position before saving the setup.

[AI Voice Chat](ai_chat) has its own speech source and spatial voice configuration. These playback settings configure the playback AudioPlayer; use the chat settings for conversational speech.
