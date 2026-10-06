---
layout: release
title: System Presets
locale: en-US
toc: true
---

# System Presets

System presets save the application setting manager's configuration so you can restore a scene-wide setup. They store settings rather than model, motion or music files. Use [Save Scene](save_scene) for loaded content and actor assignments.

## Save and apply

1. Configure the application settings you want to keep, such as graphics, lighting, sky and ground.
2. Open **System Presets** in the environment menu and use its save action.
3. Enter a name and choose **Save**. The preset is written as JSON under `presets/system/` in the [content library](../preparecontent).
4. Open System Presets again and select the saved name to apply it.

**Reload Saved** restores the application's saved settings. **Reset All** resets application settings; these actions are different from loading one named preset.

## Scope and reuse

System presets capture settings registered with the application setting manager. The exact collection depends on the build and available features, so compare the resulting settings after applying a preset on another platform. A preset cannot make an unavailable rendering feature appear.

Per-actor configuration belongs in [Actor Presets](actor_presets). A [saved scene](save_scene) records content references and scene composition; a [Scene Bundle](scene_bundle) includes packaged content files. Choose the smallest scope that matches what you want to reuse.
