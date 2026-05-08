---
layout: release
title: Working with Actors
locale: en-US
toc: true
---

# Working with Actors

An actor is a character model loaded into the scene. Working with one in DanceXR follows a consistent lifecycle — **load → configure → animate → refine** — and most settings hang off the same actor menu. This page is the map of that lifecycle, with links to the dedicated pages for each step.

For a glossary of terms used here (actor, selection disc, gizmo cube, dressing system), see [Concepts & glossary](/dancexr/concepts).

---

## The actor lifecycle at a glance

| Step | What you do | Primary pages |
|---|---|---|
| 1. Load | Drag a model file in, or pick from the content library | [Loading an actor](#loading-an-actor) |
| 2. Place | Position, rotate, scale, ground-snap | [Scale & offset](/dancexr/features/scale_offset), [Feet adjustment](/dancexr/features/feet_adjustment) |
| 3. Look | Materials, dressing, accessories | [Appearance & materials](/dancexr/appearance) |
| 4. Move | Assign motion or use procedural motion | [Motion system](/dancexr/motion) |
| 5. Simulate | Hair, cloth, breast, ragdoll, soft body | [Physics system](/dancexr/physics) |
| 6. Behave | Idle, blink, breathing, gaze, facial control | [Lifelike motions](/dancexr/features/lifelike_motions), [Eye contact](/dancexr/features/eyecontact) |
| 7. Save | Export pose, save preset, save scene | [Snapshots & presets](#snapshots-and-presets) |

---

## Loading an actor

DanceXR reads two model formats:

- **PMX** — the MikuMikuDance format. Includes its own bone hierarchy, physics rig, and morph list out of the box.
- **XPS** — the XNALara / XPS format (`.xps`, `.mesh`, `.mesh.ascii`). Does **not** include physics or a standard skeleton, so you set those up in DanceXR.

Both formats can also be packaged in a **ZIP**. See [ZIP format](/dancexr/features/zip_format) for filename rules and encoding.

### Three ways to load

- **Drag and drop** a model file (or zip) onto the DanceXR window. Fast for one-off loads.
- **Content library** — place models under `actors/` in your [content library](/dancexr/preparecontent). They appear in the actor menu's *Load Model* list.
- **Google Drive** — share a Drive folder URL and DanceXR can pull missing files. See [Google Drive integration](/dancexr/features/googledrive).

### Replace vs add

By default, loading a model **replaces** the currently selected actor. Click the **+** icon next to a model name to add it as an additional actor instead. Multi-actor scenes require a paid build — see [Download & editions](/dancexr/download).

### Load options

[Actor options](/dancexr/features/loader_options) (sometimes called Loader Options) control how new actors come in: cache size, texture compression, transition effect, auto actor change.

---

## PMX vs XPS — what differs

Most settings work the same on both formats. The places they diverge are worth knowing:

| Topic | PMX | XPS |
|---|---|---|
| Skeleton | Standard bone names from the file | Mapped via [XPS bone mapper](/dancexr/features/bone_mapper) |
| Physics rig | Built into the file ([PMX physics](/dancexr/features/pmx_physics)) | Configured in [XPS physics](/dancexr/features/xps_physics) |
| Morphs / blendshapes | [Morph list](/dancexr/features/morph_list) | None — use [Dressing system](/dancexr/features/optionals) instead |
| Outfit toggles | Material morphs (PMX) | Optional items (XPS) — same UI ([Dressing system](/dancexr/features/optionals)) |

If something in this guide says "PMX only" or "XPS only", that is why.

---

## The actor menu

Every actor has a yellow **selection disc** under its feet. Clicking it opens the actor menu — the central hub for everything per-actor. See [Actor menu & tools](/dancexr/features/actor_tools) for the full breakdown.

The menu is grouped into:

- **Tools** (wrench-and-hammer icon) — favourite, tag, [spectator](/dancexr/features/spectator_mode), move up/down, reset, [duplicate](/dancexr/features/actor_tools#tools-menu), reload, [3D snapshot](/dancexr/features/snapshot_3d), remove.
- **Recently modified** — quick jumps to the dialogs you just changed. See [Recently modified settings](/dancexr/features/recently_modified).
- **Dressing & textures** — [dressing system](/dancexr/features/optionals), [bone mapper](/dancexr/features/bone_mapper) (XPS), [alternative textures](/dancexr/features/alternative_textures).
- **Materials** — per-slot settings: skin, hair, eyes, lips, opaque, transparent, custom. See [Appearance & materials](/dancexr/appearance) for how the slots fit together.
- **Settings** — physics, [feet adjustment](/dancexr/features/feet_adjustment), [facial control](/dancexr/features/facial_control), [eye contact](/dancexr/features/eyecontact), [troubleshooting](/dancexr/features/troubleshooting).
- **Pro** (paid builds) — [outfit & body paint](/dancexr/features/outfit), [accessory](/dancexr/features/accessory), [ragdoll](/dancexr/features/ragdoll), [motion override](/dancexr/features/motion_override), [light ball](/dancexr/features/light_ball), advanced physics, NSFW overlays.
- **Morph list** (PMX only) — [PMX blendshape morphs](/dancexr/features/morph_list).

---

## Multi-actor scenes

When you have more than one actor on stage, three features handle group behavior:

- [Formation](/dancexr/features/formation) — positions actors in patterns (line, grid, custom). Order is set by **Move Up** / **Move Down** in the Tools menu.
- [Actor playlist](/dancexr/features/actor_playlist) — cycles through a list of models over time, optionally synced to music.
- [Attach to actor](/dancexr/features/attach_to_actor) — parents one actor or accessory to another (held items, riders, paired motions).

Use [Spectator mode](/dancexr/features/spectator_mode) to keep a model on stage but exclude it from auto-assigned motions and formation slots.

[Global actor control](/dancexr/features/global_actor_control) applies a setting to every actor at once — useful when you want all loaded models to share the same physics tuning, dressing, or material.

---

## Snapshots and presets

Three ways to save what you have built:

- [3D snapshot](/dancexr/features/snapshot_3d) — exports the current pose as an OBJ for use in other 3D tools.
- [Actor presets](/dancexr/features/actor_presets) — saves the actor's settings (materials, physics, dressing) so you can apply the same look to the same model later, or to a similar one.
- [Save scene](/dancexr/features/save_scene) and [scene bundle](/dancexr/features/scene_bundle) — captures the entire scene including all actors, motion, stage, and configuration.

---

## When something looks wrong

Symptom-first troubleshooting:

| Symptom | Where to look |
|---|---|
| Model loads but everything is white | [FAQ → Model loads but everything is white](/dancexr/faq) |
| Floats, sinks, slides on the ground | [Feet adjustment](/dancexr/features/feet_adjustment) |
| Wrong size or position | [Scale & offset](/dancexr/features/scale_offset) |
| Bones look broken (XPS) | [XPS bone mapper](/dancexr/features/bone_mapper), [Example bone structure](/dancexr/features/bones) |
| Hair / skirt / cloth not moving or jittering | [Physics system](/dancexr/physics) |
| Per-model weirdness | [Actor troubleshooting](/dancexr/features/troubleshooting) |
| App-level crash, won't launch | [Troubleshooting](/dancexr/troubleshooting), [FAQ](/dancexr/faq) |

---

## Related pages

- [Concepts & glossary](/dancexr/concepts)
- [Appearance & materials](/dancexr/appearance)
- [Physics system](/dancexr/physics)
- [Motion system](/dancexr/motion)
- [Actor menu & tools](/dancexr/features/actor_tools)
- [Content library](/dancexr/preparecontent)
