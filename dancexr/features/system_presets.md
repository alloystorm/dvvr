---
layout: release
title: System Presets
locale: en-US
toc: true
---

# System Presets

<!-- TODO: confirm exact contents and UI flow. Drafted from the 2024.1 release notes. -->

System Presets save **scene-wide and environment settings** — graphics quality, lighting, sky, ground — into a single named preset that you can reapply later or share with others.

Added in **2024.1**. Presets are saved as individual JSON files in the [content library](../preparecontent).

---

## What a system preset contains

<!-- TODO: confirm the exact list of settings captured. The release notes call out: graphics quality, lighting, sky, ground. There are likely more. -->

A typical system preset captures:

- [Graphics settings](graphics) — render quality, post effects.
- [Lighting](lighting) — directional and ambient light setup, [light balls](light_ball).
- [Sky & cloud](skymap) and [Sky color](sky).
- [Ground](ground) — material, shadow-only mode, etc.
- <!-- TODO: confirm whether camera, weather, simulation, or audio settings are included. -->

What is **not** in a system preset:

- Per-actor settings — those live in [actor presets](actor_presets).
- Loaded actors, motions, music, or stage assets — that lives in a [saved scene](save_scene).

---

## Saving and loading

<!-- TODO: confirm exact UI path. -->

1. Configure your scene the way you want.
2. Open the relevant scene / system menu.
3. **Save preset** — give it a name. The preset is written as a JSON file under `presets/` (or the system-presets subfolder) in the content library.
4. **Load preset** — pick a saved preset by name to apply it.

Because each preset is a separate file, you can copy it between machines or share it with other users.

---

## System presets vs other preset types

| Preset | Scope | Typical contents | Page |
|---|---|---|---|
| **System preset** | Scene-wide | Graphics, lighting, sky, ground | (this page) |
| **Actor preset** | Per actor | Materials, physics, dressing | [Actor Presets](actor_presets) |
| **Saved scene** | Everything | Scene-wide + actors + motion + assignments | [Save Scene](save_scene) |
| **Scene bundle** | Everything + assets | Saved scene + the model / motion / music files it depends on | [Scene Bundle](scene_bundle) |

---

## Related pages

- [Actor Presets](actor_presets)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)
