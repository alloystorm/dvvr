---
layout: release
title: Audio Options
locale: en-US
toc: true
---

# Audio Options

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.5, 2024.7, 2024.9, 2025.5, 2026.2). -->

Audio Options control how the audio track in the current [dance set](dance_set) plays back, including looping, volume, and how the audio source is positioned in the scene.

---

## Playback mode

Choose how the audio progresses through your loaded content:

- **Single** — play the current track once.
- **Loop** — repeat the current track. If a loop region is set (start / end time), only that region loops.
- **Shuffle** — randomly pick the next track from the queue.
- <!-- TODO: confirm whether "Sequential / next in folder" is also a separate mode. -->

Audio looping is independent of motion looping (added in 2024.5) — you can loop just the audio while letting the motion play through, or vice versa.

---

## Volume

Standard master volume slider for the audio track.

<!-- TODO: confirm whether per-actor / per-source volume controls live here or under Playback Options. -->

---

## Spatial audio

Anchor the audio to a 3D position in the scene rather than playing as a flat stereo mix. See [Spatial Audio](spatial_audio).

---

## Audio analysis

Music BPM detection, beat detection, and chorus-section data come from this layer. See:

- [Music Timing](music_timing) for setting BPM and beat offset.
- [Auto Update](autoupdate) for using audio level / beats as data sources for other settings.
- [Beats Ring](beats_ring) and the newer Audio Visualizer for visualizing the audio reactively.

The realtime audio analyzer was extended with beat detection in 2025.5, so procedural motions can react to live beats without precomputed timing.

---

## Audio / motion sync

When audio time and motion time drift apart, DanceXR can resync them automatically. Choose whether to sync **audio to motion** or **motion to audio** — see [Motion Settings](motion_settings).

Audio timing was further improved in 2026.2 to reduce stutter under variable frame rate, and 2026.3 fixed an oscillation issue when frame rate fluctuates significantly.

---

## Related pages

- [Playback Options](playback_options)
- [Music Timing](music_timing)
- [Dance Set](dance_set)
- [Spatial Audio](spatial_audio)
- [LipSync](lipsync)
