---
layout: release
title: Actor Presets
locale: en-US
toc: true
---

# Actor Presets

Actor presets save a snapshot of an actor's settings — physics, materials, dressing, motion preferences — so you can reapply the same configuration to the same model later, or to a different model with a similar build.

Added in **2024.1**. Stored under `presets/` in the [content library](/dancexr/preparecontent), which means presets can be shared between users on the same DanceXR version.

---

## What a preset contains

<!-- TODO: confirm the exact list of settings included. -->

A typical actor preset captures:

- Per-actor [motion settings](/dancexr/features/actor_motion_settings)
- [Dressing system](/dancexr/features/optionals) state (visible / hidden items)
- [Material settings](/dancexr/features/material_settings) per slot
- [Physics](/dancexr/features/physics) configuration (PMX or XPS, including [hair](/dancexr/features/hair_physics), [skirt](/dancexr/features/skirt_physics), [boobs](/dancexr/features/boobs_physics), [body colliders](/dancexr/features/body_colliders))
- [Feet adjustment](/dancexr/features/feet_adjustment) and [scale & offset](/dancexr/features/scale_offset)

What is **not** in the preset:

- The model file itself (presets reference settings, not assets).
- System-wide settings — those live in [System presets](#system-presets).
- Scene composition (stage, lighting, camera) — that lives in a [scene](/dancexr/features/save_scene).

---

## Saving and loading

<!-- TODO: confirm exact UI path and naming flow. -->

1. Configure an actor the way you want.
2. Open the actor menu, then the **Tools menu** (wrench-and-hammer icon).
3. Save preset; give it a name.
4. To apply, open the same Tools menu on any actor and select a saved preset by name.

Presets are saved under `presets/` in the content library. You can copy preset files between machines.

---

## When a preset is reusable across models

A preset is most reliable when applied to:

- The **same model** you saved it from.
- A **closely related model** (same source character, same skeleton).
- A **same-format model with similar build** (PMX-to-PMX, similar bone naming).

Across very different models, settings that depend on bone names — XPS physics rigs, [bone mapper](/dancexr/features/bone_mapper) overrides — may not transfer cleanly.

---

## System presets

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

System Presets save scene-wide settings (lighting, environment, camera, graphics) instead of per-actor settings. The save and apply flow is similar; system presets are stored separately.

---

## Related pages

- [Save scene](/dancexr/features/save_scene) — captures the entire scene rather than a single actor's settings
- [Scene bundle](/dancexr/features/scene_bundle) — packages a saved scene with the assets it depends on
- [Content library](/dancexr/preparecontent) — `presets/` folder location
- [Actor menu & tools](/dancexr/features/actor_tools)
