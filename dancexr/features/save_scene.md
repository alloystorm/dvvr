---
layout: release
title: Save Scene
locale: en-US
toc: true
---

# Save Scene

<!-- TODO: confirm exact UI flow. -->

A saved scene captures the **complete state** of your DanceXR session — loaded actors, motions, audio, stage, lights, camera, all per-actor settings, all environment settings — into a single file that can be reloaded later.

---

## What a scene contains

- All loaded **actors** with their per-actor configuration (materials, physics, dressing, motion overrides).
- The currently loaded **stage** and its settings.
- The active **dance set** (audio + motions) and assignment to each actor.
- **Environment** — sky, ground, lighting, weather, water.
- **Camera** mode and settings.
- **Formation** layout for multi-actor scenes.

What a scene does **not** contain:

- The actual model, motion, or music files. The scene file references them by their content-library identifier ([since 2024.9](../releases/2024.9), this is the immediate folder + filename, not the full path, so reorganizing your library no longer breaks scenes).
- Per-tier features the recipient does not have access to.

---

## Saving and loading

1. Configure your scene the way you want.
2. Open the scene menu and choose **Save Scene** — name the scene file.
3. To reload, open the scene menu and pick the saved scene by name.

Saved scenes live in your [content library](../preparecontent) and can be copied between machines.

---

## When the scene fails to load completely

If a scene references a model, motion, or music file that is not present in the recipient's library, that asset is skipped. The rest of the scene loads normally.

To **share a scene with all its assets bundled together**, use [Scene Bundle](scene_bundle) — that packs the model and motion files in alongside the scene file so a recipient does not have to track them down separately.

---

## Save Scene vs presets

| Format | Scope | Page |
|---|---|---|
| **Save Scene** | Everything in the scene | (this page) |
| **Scene Bundle** | Save Scene + the actual asset files | [Scene Bundle](scene_bundle) |
| **Actor Preset** | A single actor's settings only | [Actor Presets](actor_presets) |
| **System Preset** | Scene-wide environment / graphics settings only | [System Presets](system_presets) |

---

## Related pages

- [Scene Bundle](scene_bundle)
- [Actor Presets](actor_presets)
- [System Presets](system_presets)
- [Content Library](../preparecontent)
