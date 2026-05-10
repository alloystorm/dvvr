---
layout: release
title: Scene Bundle
locale: en-US
toc: true
---

# Scene Bundle

<!-- TODO: confirm exact UI flow and bundle format. Drafted from release notes (2024.1, 2024.9). -->

A Scene Bundle is a [saved scene](save_scene) plus the actual model, motion, and music files it references — packaged together so a recipient can load the entire scene without first chasing down every asset.

Added (experimental) in **2024.1**.

---

## Save Scene vs Scene Bundle

- A **saved scene** is a small file that *references* assets by name. When you load it, DanceXR looks up each referenced asset in the recipient's content library. If the recipient is missing one of those models or motions, that part of the scene fails to load.
- A **scene bundle** wraps the saved scene **with** all the assets it depends on. The recipient can load the bundle directly — no missing-asset problem.

Use a scene bundle when sharing a scene; use a saved scene for your own use, where you already have all the assets.

---

## Creating a bundle

<!-- TODO: confirm UI path. -->

1. Set up the scene the way you want it.
2. Open the scene menu and choose **Save as Scene Bundle**.
3. DanceXR collects all referenced assets (models, motions, music) and packages them into a single bundle file.

The bundle includes everything the scene needs to load on another machine, in another country, without the recipient hunting down the same model packs.

---

## Loading a bundle

Treat a bundle file like any other content-library item — drop it into your library, or open it via the scene menu.

When loading, DanceXR extracts the assets into a temporary or per-bundle location and loads the scene from there. The assets are not merged into the recipient's main library by default <!-- TODO: confirm exact behavior here — extracted to a subfolder vs. merged. -->

---

## Limitations

<!-- TODO: confirm. Likely:
- Bundle size scales with the assets included; large stage models can produce very large bundles.
- Tier-locked features still require the recipient to have that tier.
- Personal / unauthorized model redistribution — the bundle does not strip licensing constraints. -->

Marked experimental in 2024.1; see release notes for the current state.

---

## Related pages

- [Save Scene](save_scene)
- [Content Library](../preparecontent)
- [Actor Presets](actor_presets)
- [System Presets](system_presets)
