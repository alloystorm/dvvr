---
layout: feature
title: "Playback Options"
locale: en-US
---

# Playback Options

Controls playback behavior, timing, audio analysis, and spatial audio for the scene.


## Auto Setup {#auto-setup}

**Auto-Load Actors** automatically loads enough actors to match the number of motion tracks, each driven by a different motion source. **Auto-Assign Camera** automatically uses camera motion when available — useful when switching tracks frequently.


## Playback Mode {#playback-mode}

Controls how the playlist or track list is traversed:
- *List Once* plays through the list once and stops.
- *Single* loops the current track indefinitely.
- *Loop List* repeats the entire list.
- *Loop Single* repeats the current track with remix behavior.
- *Shuffle* plays tracks in random order without repeating until all have played.

**Remix Mode** controls how remix tracks continue: *Continue Next* advances to the next remix track, *Synchronized* syncs with the primary playback, *Loop* restarts the current remix, and *Shuffle Next* picks a random remix track.


## Speed {#speed}

**Speed** scales playback rate without affecting pitch when *Pitch Shift* is enabled — useful for slower warm-ups or faster run-throughs. The motion timeline and physics simulation also respect this speed. **Smooth Audio Time** interpolates the motion time between audio updates, reducing jitter on playback; tune **Smooth Time Damping** and **Smooth Time Frequency** to balance smoothness against responsiveness. **Timeline Fine Adjust** enables long-press adjustment on the timeline for precise scrubbing.


## Timing {#timing}

Sets the default BPM, beat offset, and phrase structure used by the audio player. See *Base Timing* for details.


## Audio Analysis {#audio-analysis}

When enabled, the audio spectrum is processed at the configured **Processing Rate** (45 FPS is usually sufficient). **Band Selection** chooses the frequency range used for audio-reactive effects — narrow the range to focus on bass or treble. **Audio Level Rise** and **Audio Level Fall** control how quickly the level responds to increasing and decreasing audio energy; lower values create smoother, more sustained reactions, higher values track transients closely. **Audio Level Damping** adds overall damping to the signal. **Fade In Out** reduces level spikes at track start and end. **Spectrum Balance** shifts weight between low and high frequencies — lower values favor bass, higher values favor treble.


## Lip Sync {#lip-sync}

Enables mouth animation driven by audio. **Lip Sync Smoothing** controls how fast the animation reacts; lower values react more quickly, while higher values smooth changes over a longer time. See [LipSync](lipsync) for the playback and per-actor setup.


## Spatial Audio {#spatial-audio}

Enables 3D spatialization of the audio output. **Spatial Blend** blends between 2D playback and a 3D source; zero keeps playback 2D. Enable **Follow Actor** and choose **Select Actor** to move the source with that actor's head. See [Spatial Audio](spatial_audio) for a complete setup.


## Settings reference

## Default Timing {#default-timing}

Holds BPM, beat offset, phrase structure, loop range, and motion speed for an audio track. Designed to be reused wherever timing configuration is needed.

