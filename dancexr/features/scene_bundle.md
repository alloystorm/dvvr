---
layout: release
title: Scene Bundle
locale: en-US
toc: true
---

# Scene Bundle

A scene bundle packages a scene and its content into a ZIP archive. Use it to transfer a performance setup when the destination device does not already have the same models and motions. [Save Scene](save_scene) stores references without packaging those files.

## Create and check a bundle

1. Load the scene you want to transfer and confirm its actors, stages, props, accessories and dance sets work.
2. Open the **Bundle** menu and use its save action to choose a bundle name.
3. Wait until the **Creating bundle...** progress message finishes before copying the archive.
4. Open the bundle on the destination device and check playback, materials and motion assignments.

The exporter packages the main and remix dance sets, loaded actor models and their accessories, and stage/prop content, then writes the scene and a bundle manifest. Built-in content is represented through the application's built-in identifiers rather than copied as an external model package.

## Transfer considerations

Bundles can be much larger than scene JSON files because model textures and playback content are included. Keep enough free storage on both devices. If a model is missing a texture before export, bundling it does not repair that source package.

Rendering features and licensed feature availability still depend on the destination build. Inspect the transferred scene there before recording or presenting it. Use [Actor Presets](actor_presets) or [System Presets](system_presets) when you only need settings and do not need to package the content.
