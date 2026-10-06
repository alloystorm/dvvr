---
layout: release
title: Auto Dance
locale: en-US
toc: true
---

# Auto Dance: choosing a generator

Auto Dance creates motion procedurally from curves and poses, using music timing and optional audio response. You do not need to load a VMD dance file. The three generations have distinct settings; a value in one version does not configure the others.

| Generator | Use it for | Main controls |
|---|---|---|
| Auto Dance | The original procedural movement style | Extent, Curve, Motion Per Beat, hand poses and upper-body motion. |
| Auto Dance 2 | A different movement pattern with direct audio-response controls | Extent, motion speed, Audio Sensitivity, Audio Threshold and Body Twist. |
| [Auto Dance 3](autodance3) | Pattern-based motion with a configurable actor pose | Motion, Anchoring and Actor Pose. |

Start by selecting a generator from the procedural motion list, playing an audio track, and checking [Music Timing](music_timing). Open that motion's settings to adjust the generated movement; use the actor's motion settings for pose changes.

## Original Auto Dance {#auto-dance-1}

**Extent** changes movement amplitude. **Legs Open** and **Lower** set the stance; **Curve** changes the movement curve, and **Motion Per Beat** sets its relationship to the beat. **Upper Body Motion** scales upper-body movement. **Use Loudness For** enables the loudness-dependent behavior.

Choose left and right hand poses, or use symmetrical hands when they should match. Start with a small extent and a neutral stance, then increase the movement while checking foot placement and clothing physics. If the timing looks wrong, correct the audio timing before compensating with larger movements.

## Auto Dance 2 {#auto-dance-2}

The second generator exposes **Extent** and motion speed alongside **Audio Sensitivity**, **Audio Threshold** and **Body Twist**. Audio Sensitivity is an on/off control as well as a value: disable its audio response to compare the base motion with the music-reactive result.

Raise sensitivity when the motion responds too little to the track. Adjust the threshold when quiet passages trigger unwanted movement. **Lower** and the left/right hand pose settings configure the actor's stance. Change one control at a time so you can distinguish pose changes from audio response.

## Keeping a setup usable

Compare generators with the same actor and track. Their defaults and movement shapes differ, so an apparently stronger result may simply be a different stance or extent. For the pattern and pose workflow in the third generator, continue to [Auto Dance 3](autodance3).
