---
layout: release
title: Working with Actors
locale: en-US
toc: true
---

# Working with Actors

An actor is a character model loaded into the scene. DanceXR adapts the models' skeleton on-the-fly to fit the motion, and simulates movements of hair and clothes using the physics system.

You can customize the appearance of the model by changing materials, applying textures, or using the dressing system to toggle outfit pieces. You can also adjust the scale and position of the model, and fine-tune how it interacts with the stage and other actors.

For a glossary of terms used here (actor, selection disc, gizmo cube, dressing system), see [Concepts & glossary](concepts).

---

## Loading an actor

DanceXR reads three model formats:

- **PMX** — the MikuMikuDance format. Includes its own bone hierarchy, physics rig, and morph list out of the box.
- **XPS** — the XNALara / XPS format (`.xps`, `.mesh`, `.mesh.ascii`). Does **not** include physics or a standard skeleton, so you set those up in DanceXR.
- **FBX** *(preview, since 2025.9)* — broad-purpose 3D format. DanceXR currently loads the model only, not embedded animations or other FBX-specific features. Like XPS, FBX requires [bone mapping](features/bone_mapper) before motions will play correctly.

All three formats can also be packaged in a **ZIP**. See [ZIP format](features/zip_format) for filename rules and encoding.

### Two ways to load

- **Drag and drop** a model file (or zip) onto the DanceXR window. Fast for one-off loads.
- **Content library** — place models under `actors/` in your [content library](preparecontent). They appear in the actor menu's *Load Model* list.

### Replace vs add

By default, loading a model **replaces** the currently selected actor. Click the **+** icon next to a model name to add it as an additional actor instead. Multi-actor scenes require a paid build — see [Download & editions](download).

### Load options

[Loader options](features/loader_options) control how new actors come in: cache size, texture compression, transition effect, auto actor change.

---

## PMX vs XPS vs FBX — what differs

Most settings work the same across all three formats. The places they diverge are worth knowing:

| Topic | PMX | XPS | FBX (preview) |
|---|---|---|---|
| Skeleton | Standard bone names from the file | Mapped via [bone mapper](features/bone_mapper) | Mapped via [bone mapper](features/bone_mapper) |
| Physics rig | Built into the file ([PMX physics](features/pmx_physics)) | Configured in [XPS physics](features/xps_physics) | Configured in [XPS physics](features/xps_physics) |
| Morphs / blendshapes | [Morph list](features/morph_list) | None — use [Dressing system](features/optionals) instead | None |
| Outfit toggles | Material morphs (PMX) | Optional items (XPS) — same UI ([Dressing system](features/optionals)) | None |

If something in this guide says "PMX only" or "XPS only", that is why. FBX support is in preview as of 2025.9 — model geometry and materials load, but animations and other FBX features inside the file are ignored.

---

## The actor menu

Every actor has a yellow **selection disc** under its feet. Clicking it opens the actor menu — the central hub for everything per-actor. See [Actor menu & tools](features/actor_tools) for the full breakdown.

The menu is grouped into:

- **Motion** — assigned motion, [formation](features/formation) slot and model-specific motion settings.
- **Recently modified** — quick jumps to the dialogs you just changed. See [Recently modified settings](features/recently_modified).
- **Dressing & textures** — [dressing system](features/optionals), [bone mapper](features/bone_mapper) (XPS), [alternative textures](features/alternative_textures).
- **Materials** — per-slot settings: skin, hair, eyes, lips, opaque, transparent, custom. See [Appearance & materials](appearance) for how the slots fit together.
- **Settings** — physics, [feet adjustment](features/feet_adjustment), [facial control](features/facial_control), [eye contact](features/eyecontact), [troubleshooting](features/troubleshooting).
- **Pro** (paid builds) — [outfit & body paint](features/outfit), [accessory](features/accessory), [ragdoll](features/ragdoll), [motion override](features/motion_override), [light ball](features/light_ball), advanced physics, NSFW overlays.
- **Morph list** (PMX only) — [PMX blendshape morphs](features/morph_list).
- **Tools** (wrench-and-hammer icon) — favourite, tag, [spectator](features/spectator_mode), move up/down, reset, [duplicate](features/actor_tools#tools-menu), reload, [3D snapshot](features/snapshot_3d), remove.

---

## Multi-actor scenes

When you have more than one actor on stage, three features handle group behavior:

- [Formation](features/formation) — positions actors in patterns (line, grid, custom). Order is set by **Move Up** / **Move Down** in the Tools menu.
- [Actor playlist](features/actor_playlist) — cycles through a list of models over time, optionally synced to music.
- [Attach to actor](features/attach_to_actor) — parents one actor or accessory to another (held items, riders, paired motions).

Use [Spectator mode](features/spectator_mode) to keep a model on stage but exclude it from auto-assigned motions and formation slots.

[Global actor control](features/global_actor_control) applies a setting to every actor at once — useful when you want all loaded models to share the same physics tuning, dressing, or material.

---

## Snapshots and presets

Three ways to save what you have built:

- [3D snapshot](features/snapshot_3d) — exports the current pose as an OBJ for use in other 3D tools.
- [Actor presets](features/actor_presets) — saves the actor's settings (materials, physics, dressing) so you can apply the same look to the same model later, or to a similar one.
- [Save scene](features/save_scene) and [scene bundle](features/scene_bundle) — captures the entire scene including all actors, motion, stage, and configuration.

---

## When something looks wrong

Symptom-first troubleshooting:

| Symptom | Where to look |
|---|---|
| Model loads but everything is white | [FAQ → Model loads but everything is white](faq) |
| Model frozen in standard pose | [XPS bone mapper](features/bone_mapper), [Example bone structure](features/bones) |
| Floats, sinks, slides on the ground | [Feet adjustment](features/feet_adjustment) |
| Wrong size or position | [Scale & offset](features/scale_offset) |
| Hair / skirt / cloth not moving or jittering | [Physics system](physics) |
| Per-model weirdness | [Actor troubleshooting](features/troubleshooting) |
| App-level crash, won't launch | [Troubleshooting](troubleshooting), [FAQ](faq) |

---

## Related pages

- [Concepts & glossary](concepts)
- [Appearance & materials](appearance)
- [Physics system](physics)
- [Motion system](motion)
- [Actor menu & tools](features/actor_tools)
- [Content library](preparecontent)
