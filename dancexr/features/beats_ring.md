---
layout: release
title: Beats Ring
locale: en-US
---

# Beats Ring

<!-- TODO: full description. The Beats Ring is referenced as a tile on /dancexr/features under Stage & Props but no other page describes it. Likely an audio-reactive visualizer ring; confirm and fill in. -->

The Beats Ring is an audio-reactive visualizer prop that pulses with the music. It is one of the [auto-update](autoupdate) data sources, meaning other settings can drive themselves from its output.

---

## What it does

<!-- TODO: confirm shape (ring? particles? geometry?), where it is rendered (around the actor? on the stage?), how it scales with audio. -->

The Beats Ring takes the current audio signal and produces a beat-driven value that can be used to:

- Render a visible ring or pulse effect around the actor or stage.
- Drive other auto-update parameters (lighting intensity, material parameters, motion speed) in time with the music.

---

## Enabling it

<!-- TODO: confirm the menu path. Likely under environment menu or a per-actor setting. -->

---

## Settings

<!-- TODO: list. Possibly: visibility, color, scale, sensitivity threshold, smoothing. -->

---

## Related pages

- [Auto update](autoupdate) — using the beats ring as a data source for other settings
- [Music timing](music_timing) — synchronizing motion to music
- [Audio options](audio_options)
