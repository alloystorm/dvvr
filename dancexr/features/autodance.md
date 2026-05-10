---
layout: release
title: Auto Dance
locale: en-US
toc: true
---

# Auto Dance

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

Auto Dance is the **first-generation** procedural dance generator. It produces dance moves on the fly from a built-in motion library, choosing and blending moves in response to the music's beats and volume.

Auto Dance is largely superseded by [Auto Dance 2](autodance2) and [Auto Dance 3](autodance3) — the newer versions have more variation, finer control, and better music sync. Use Auto Dance when you specifically want the original generator's behavior.

---

## How it works

- DanceXR analyzes the playing audio for **beats** (timing) and **volume** (energy).
- On each beat, the generator picks the next move from a library of short authored dance segments and blends from the previous move.
- Higher volume sections trigger bigger / more energetic moves.

You do not load a VMD file for Auto Dance — the moves are generated.

---

## Settings

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## When to choose Auto Dance vs newer versions

- **Auto Dance (this page)** — the original generator. Smaller move library, simpler music response.
- **[Auto Dance 2](autodance2)** — second generation, larger pool, more variation between moves.
- **[Auto Dance 3](autodance3)** — current default. Highly customizable; integrates with the [Sex Motion 3](sex_motion_3) shared motion-control system; uses the realtime audio analyzer with beat detection.

---

## Related pages

- [Auto Dance 2](autodance2)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)
