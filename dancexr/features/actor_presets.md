---
layout: release
title: Actor Presets
locale: en-US
toc: true
---

# Actor Presets

Actor presets save a snapshot of an actor's settings — physics, materials, dressing, motion preferences — so you can reapply the same configuration to the same model later, or to a different model with a similar build.

Added in **2024.1**. Stored under `presets/` in the [content library](../preparecontent), which means presets can be shared between users on the same DanceXR version.

---

## What a preset contains

<!-- TODO: confirm the exact list of settings included. -->

A typical actor preset captures:

- Per-actor [motion settings](motion_settings)
- [Dressing system](optionals) state (visible / hidden items)
- [Material settings](material_settings) per slot
- Physics configuration (PMX or XPS, including [hair](hair_physics), [skirt](skirt_physics), [boobs](boobs_physics), [body colliders](body_colliders))
- [Feet adjustment](feet_adjustment) and [scale & offset](scale_offset)

What is **not** in the preset:

- The model file itself (presets reference settings, not assets).
- System-wide settings — those live in [System presets](#system-presets).
- Scene composition (stage, lighting, camera) — that lives in a [scene](save_scene).

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

Across very different models, settings that depend on bone names — XPS physics rigs, [bone mapper](bone_mapper) overrides — may not transfer cleanly.

---

## System presets

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

System Presets save scene-wide settings (lighting, environment, camera, graphics) instead of per-actor settings. The save and apply flow is similar; system presets are stored separately.

---

## Related pages

- [Save scene](save_scene) — captures the entire scene rather than a single actor's settings
- [Scene bundle](scene_bundle) — packages a saved scene with the assets it depends on
- [Content library](../preparecontent) — `presets/` folder location
- [Actor menu & tools](actor_tools)
