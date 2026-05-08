---
layout: release
title: Motion System
locale: en-US
toc: true
---

# Motion System

Motion in DanceXR comes from several sources, configured at several levels, and can stack. This page is the map: where motion comes from, where settings live, and how layers combine.

For terms (motion pass, override, dance set, remix, custom inherit), see [Concepts & glossary](/dancexr/concepts#motion-concepts).

---

## Motion sources

There are five places motion can come from:

1. **A motion file** (VMD or BVH) loaded from disk.
2. **A dance set** — one audio file plus one or more motions, automatically detected when grouped in a folder or zip.
3. **Procedural motion** — generated at runtime by Auto Dance, Idle Motion, Catwalk, Lifelike Motions, and Secondary Motion.
4. **Keyframe animation** — manually authored poses in DanceXR.
5. **Remix** — using motion data from one dance set with audio from another.

You can mix these. A typical scene plays a VMD-driven dance with a procedural [secondary motion](/dancexr/features/secondary_motion) layer on top, plus [eye contact](/dancexr/features/eyecontact) and breathing handled by their own systems.

---

## The dance set unit

A [dance set](/dancexr/features/dance_set) is the natural grouping for "a song". When you place a folder or zip in `motion/` containing one audio file and one or more matching VMD/BVH files, DanceXR groups them automatically. A loaded dance set:

- Plays the audio.
- Routes motions to actors (one motion per actor by default; reassignable).
- Optionally drives the camera if a camera VMD is included.
- Has a shared [music timing](/dancexr/features/music_timing) tied to the audio's BPM.

The set is the unit you load, save, share, and remix. Individual motions still have their own settings (per-motion speed, loop range, etc.), but the dance set keeps them coordinated.

[VMD2PNG](/dancexr/features/dance_set#vmd2png-v20263) (added in 2026.3) lets you load motion data from PNG files that encode VMD data — smaller, easier to share, includes a thumbnail.

---

## Settings hierarchy

Motion settings live at three levels. When the same parameter exists at multiple levels, the more specific level wins.

| Level | Page | Scope |
|---|---|---|
| System | [Motion settings](/dancexr/features/motion_settings) | Defaults for every motion in the scene |
| Per-actor | [Actor motion settings](/dancexr/features/actor_motion_settings) | Overrides for one actor's motion |
| Per-motion | inside [Dance set](/dancexr/features/dance_set) | Per-motion tuning within the set |

[Playback options](/dancexr/features/playback_options) — speed, loop mode, range — applies at the playback level (the audio/motion timeline as a whole).

---

## Assigning motion

[Assigning motion](/dancexr/features/assign_motion) covers the actual mechanics: drag-drop a VMD onto the window, click *Assign To* in the audio/motion menu, or open the actor menu and pick from already-loaded motions.

Order matters when you have multiple actors. **Move Up / Move Down** in the actor [Tools menu](/dancexr/features/actor_tools#tools-menu) reorders actors, which changes which motion in the dance set they get when auto-assigned.

[Spectator mode](/dancexr/features/spectator_mode) excludes an actor from auto-assignment.

---

## Layering and override

When you want to combine or modify motions, four pages do related things — pick the right one for the job:

| Want | Use |
|---|---|
| Two motions playing on the same actor at once (e.g. a dance plus a hand wave) | [Motion passes](/dancexr/features/motion_passes) |
| Replace specific bones in a motion (fix arm clipping, swap face) | [Motion override](/dancexr/features/motion_override) |
| Author or modify the bone-following relationships PMX inherit-bones use | [Custom inherit motion](/dancexr/features/custom_inherit) |
| Pair motion from one dance set with audio from another | [Remix motion](/dancexr/features/remix) |

Motion passes layer; override masks per-bone; inherit motion changes what counts as following what; remix is a higher-level swap of audio under the same motion.

---

## Procedural motion

Generated at runtime, no source VMD needed:

- [Idle motion](/dancexr/features/idle_motion) — breathing and quiet poses when nothing else is playing.
- [Catwalk motion](/dancexr/features/catwalk) — procedural walk cycle.
- [Auto Dance 1](/dancexr/features/autodance), [Auto Dance 2](/dancexr/features/autodance2), [Auto Dance 3](/dancexr/features/autodance3) — procedural dance generators. Use **Auto Dance 3** unless you have a reason to pick an earlier generation; it has rhythm analysis and the strongest variation.
- [Lifelike motions](/dancexr/features/lifelike_motions) — micro-motions that make a paused or idle actor feel alive.
- [Secondary motion](/dancexr/features/secondary_motion) — procedural layer that runs on top of any motion (sway, breath, follow-through).
- [Keyframe animation](/dancexr/features/keyframe_animation) — author your own poses with manual keyframes.

[Idle motion](/dancexr/features/idle_motion), [Auto Dance](/dancexr/features/autodance), [Auto Dance 2](/dancexr/features/autodance2), and [Motion override](/dancexr/features/motion_override) all expose [gizmo cubes](/dancexr/features/controls#gizmo-cubes) for direct posing.

---

## Music timing

[Music timing](/dancexr/features/music_timing) detects (or lets you set) the BPM and beat offset of the loaded audio. Several systems consume this:

- [Auto Dance 3](/dancexr/features/autodance3) syncs motion changes to beats.
- [Auto camera](/dancexr/features/auto_cam) can sync shot transitions to beats and respond to audio sensitivity.
- [Auto update](/dancexr/features/autoupdate) can drive any setting from the beat signal.

If procedural dance feels off-tempo, fix music timing first.

---

## Character behavior — the always-on layer

Three systems run continuously, regardless of what motion is playing, to keep characters from looking robotic:

- [Blink, breathing & eye contact](/dancexr/features/eyecontact) — eyelid behavior, automatic gaze targeting, breath rise/fall.
- [Facial control](/dancexr/features/facial_control) — manual or automatic facial expression / morph blending.
- [Lifelike motions](/dancexr/features/lifelike_motions) — small idle adjustments.

These compose with whatever motion source you are using.

---

## Common problems

| Symptom | Likely fix |
|---|---|
| Loaded a motion but nothing happened | Motion was loaded but not assigned — see [Assigning motion](/dancexr/features/assign_motion) |
| Wrong actor got the dance | Reorder actors with Move Up / Down in [Tools menu](/dancexr/features/actor_tools#tools-menu) |
| Motion runs at wrong speed | Check [playback options](/dancexr/features/playback_options) and per-motion speed in [dance set](/dancexr/features/dance_set) |
| Procedural dance is off-beat | [Music timing](/dancexr/features/music_timing) — verify BPM and offset |
| Arm clips through body | [Motion override](/dancexr/features/motion_override) on the offending arm bones |
| Character looks dead between motions | Enable [idle motion](/dancexr/features/idle_motion), [eye contact](/dancexr/features/eyecontact), and [lifelike motions](/dancexr/features/lifelike_motions) |

---

## Related pages

- [Concepts & glossary](/dancexr/concepts#motion-concepts)
- [Working with actors](/dancexr/actors)
- [AI in DanceXR](/dancexr/ai) — Auto Dance and AI-driven motion
- [Cinematic camera](/dancexr/cameras) — Auto Cam reads music timing too
