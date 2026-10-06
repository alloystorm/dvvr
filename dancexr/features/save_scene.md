---
layout: release
title: Save Scene
locale: en-US
toc: true
---

# Save Scene

A saved scene records the loaded content and its configuration so you can reopen the performance setup. It references models, motions and audio in the content library; it does not embed those source files.

## Save and reload

1. Arrange the actors, stage, props, motion assignments, environment and camera.
2. Open the **Scene** browser and use its save icon.
3. Enter a scene name and choose **Save**.
4. To restore it, open Scene again and select the saved name.

Before relying on a scene for a recording, reload it and check the actor assignments, playback and camera. This catches missing content or configuration differences while the source files are still easy to locate.

## Move a scene to another device

The destination library must contain the content referenced by the scene. DanceXR uses content identifiers rather than depending only on the full original filesystem path, but renaming files or removing their identifying folder can still prevent a match.

If part of a scene fails to load, confirm the corresponding actor, motion, audio or stage can be loaded directly from the destination library. Keep the asset files and required textures together. To transfer packaged content, use [Scene Bundle](scene_bundle).

## Scenes and presets

A scene captures composition and loaded-content references. [Actor Presets](actor_presets) reuse one actor's configuration, while [System Presets](system_presets) reuse application-level settings. Save a scene when you need the whole setup; use a preset for a narrower reusable adjustment.
