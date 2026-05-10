---
layout: release
title: Motion System
locale: en-US
toc: true
---

# Motion System

Motion in DanceXR comes from several sources, configured at several levels, and can stack. This page is the map: where motion comes from, where settings live, and how layers combine.

For terms (motion pass, override, dance set, remix, custom inherit), see [Concepts & glossary](concepts#motion-concepts).

---

## Motion sources

There are five places motion can come from:

1. **A motion file** (VMD or BVH) loaded from disk.
2. **A dance set** — one audio file plus one or more motions, automatically detected when grouped in a folder or zip.
3. **Procedural motion** — generated at runtime by Auto Dance, Idle Motion, Catwalk, Lifelike Motions, and Secondary Motion.
4. **Keyframe animation** — manually authored poses in DanceXR.
5. **Remix** — using motion data from one dance set with audio from another.

You can mix these. A typical scene plays a VMD-driven dance with a procedural [secondary motion](features/secondary_motion) layer on top, plus [eye contact](features/eyecontact) and breathing handled by their own systems.

---

## The dance set unit

A [dance set](features/dance_set) is the natural grouping for "a song". When you place a folder or zip in `motion/` containing one audio file and one or more matching VMD/BVH files, DanceXR groups them automatically. A loaded dance set:

- Plays the audio.
- Routes motions to actors (one motion per actor by default; reassignable).
- Optionally drives the camera if a camera VMD is included.
- Has a shared [music timing](features/music_timing) tied to the audio's BPM.

The set is the unit you load, save, share, and remix. Individual motions still have their own settings (per-motion speed, loop range, etc.), but the dance set keeps them coordinated.

[VMD2PNG](features/dance_set#vmd2png-v20263) (added in 2026.3) lets you load motion data from PNG files that encode VMD data — smaller, easier to share, includes a thumbnail.

---

## Settings hierarchy

Motion settings live at three levels. When the same parameter exists at multiple levels, the more specific level wins.

| Level | Page | Scope |
|---|---|---|
| System | [Motion settings](features/motion_settings) | Defaults for every motion in the scene |
| Per-actor | [Actor motion settings](features/motion_settings) | Overrides for one actor's motion |
| Per-motion | inside [Dance set](features/dance_set) | Per-motion tuning within the set |

[Playback options](features/playback_options) — speed, loop mode, range — applies at the playback level (the audio/motion timeline as a whole).

---

## Assigning motion

[Assigning motion](features/assign_motion) covers the actual mechanics: drag-drop a VMD onto the window, click *Assign To* in the audio/motion menu, or open the actor menu and pick from already-loaded motions.

Order matters when you have multiple actors. **Move Up / Move Down** in the actor [Tools menu](features/actor_tools#tools-menu) reorders actors, which changes which motion in the dance set they get when auto-assigned.

[Spectator mode](features/spectator_mode) excludes an actor from auto-assignment.

---

## Layering and override

When you want to combine or modify motions, four pages do related things — pick the right one for the job:

| Want | Use |
|---|---|
| Two motions playing on the same actor at once (e.g. a dance plus a hand wave) | [Motion passes](features/motion_passes) |
| Replace specific bones in a motion (fix arm clipping, swap face) | [Motion override](features/motion_override) |
| Author or modify the bone-following relationships PMX inherit-bones use | [Custom inherit motion](features/custom_inherit) |
| Pair motion from one dance set with audio from another | [Remix motion](features/remix) |

Motion passes layer; override masks per-bone; inherit motion changes what counts as following what; remix is a higher-level swap of audio under the same motion.

---

## Procedural motion

Generated at runtime, no source VMD needed:

- [Idle motion](features/idle_motion) — breathing and quiet poses when nothing else is playing.
- [Catwalk motion](features/catwalk) — procedural walk cycle.
- [Auto Dance 1](features/autodance), [Auto Dance 2](features/autodance2), [Auto Dance 3](features/autodance3) — procedural dance generators. Use **Auto Dance 3** unless you have a reason to pick an earlier generation; it has rhythm analysis and the strongest variation.
- [Lifelike motions](features/lifelike_motions) — micro-motions that make a paused or idle actor feel alive.
- [Secondary motion](features/secondary_motion) — procedural layer that runs on top of any motion (sway, breath, follow-through).
- [Keyframe animation](features/keyframe_animation) — author your own poses with manual keyframes.

[Idle motion](features/idle_motion), [Auto Dance](features/autodance), [Auto Dance 2](features/autodance2), and [Motion override](features/motion_override) all expose [gizmo cubes](controls#gizmo-cubes) for direct posing.

---

## Music timing

[Music timing](features/music_timing) detects (or lets you set) the BPM and beat offset of the loaded audio. Several systems consume this:

- [Auto Dance 3](features/autodance3) syncs motion changes to beats.
- [Auto camera](features/auto_cam) can sync shot transitions to beats and respond to audio sensitivity.
- [Auto update](features/autoupdate) can drive any setting from the beat signal.

If procedural dance feels off-tempo, fix music timing first.

---

## Character behavior — the always-on layer

Three systems run continuously, regardless of what motion is playing, to keep characters from looking robotic:

- [Blink, breathing & eye contact](features/eyecontact) — eyelid behavior, automatic gaze targeting, breath rise/fall.
- [Facial control](features/facial_control) — manual or automatic facial expression / morph blending.
- [Lifelike motions](features/lifelike_motions) — small idle adjustments.

These compose with whatever motion source you are using.

---

## Common problems

| Symptom | Likely fix |
|---|---|
| Loaded a motion but nothing happened | Motion was loaded but not assigned — see [Assigning motion](features/assign_motion) |
| Wrong actor got the dance | Reorder actors with Move Up / Down in [Tools menu](features/actor_tools#tools-menu) |
| Motion runs at wrong speed | Check [playback options](features/playback_options) and per-motion speed in [dance set](features/dance_set) |
| Procedural dance is off-beat | [Music timing](features/music_timing) — verify BPM and offset |
| Arm clips through body | [Motion override](features/motion_override) on the offending arm bones |
| Character looks dead between motions | Enable [idle motion](features/idle_motion), [eye contact](features/eyecontact), and [lifelike motions](features/lifelike_motions) |

---

## Related pages

- [Concepts & glossary](concepts#motion-concepts)
- [Working with actors](actors)
- [AI in DanceXR](ai) — Auto Dance and AI-driven motion
- [Cinematic camera](cameras) — Auto Cam reads music timing too
