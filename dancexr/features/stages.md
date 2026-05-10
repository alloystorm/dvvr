---
layout: release
title: Stages
locale: en-US
toc: true
---

# Stages

<!-- TODO: confirm exact UI flow. Drafted from the actors / props / content-library structure. -->

A stage is the static environment your actors perform on — a club floor, a concert hall, a city street, a procedural [room](room_stage). DanceXR loads stages from your content library the same way it loads actors and motions, and applies its own lighting, physics, and camera systems on top.

---

## Loading a stage

Place stage models in your [content library](../preparecontent), tagged appropriately so they appear under the stage menu. PMX, XPS, and FBX models can all be used as stages.

From the scene menu, open the stage selector and pick the model to load. A stage replaces any previously loaded stage; only one stage is active at a time.

---

## Stage vs prop vs room

- **Stage** — the main environment. Loaded once, sets the floor, walls, scale of the scene.
- **[Props](props)** — additional models layered on top of (or independently from) the stage.
- **[Primitive shapes](primitive_shapes)** — built-in box / cylinder / sphere props.
- **[Room Stage](room_stage)** — a built-in procedural stage you can configure without an external model.
- **[Ground](ground)** — the rendered ground plane. The stage and ground coexist; the ground can be set to *shadow-only* mode (2024.3) to layer the model's shadow over a background or AR passthrough.

---

## Stage and motion

If the loaded motion includes a camera or a stage prop track, those tracks attach to the stage origin. Motion files authored for one stage may need [Scale & Offset](scale_offset) adjustments when loaded against a differently scaled stage.

---

## Sharing a stage

Save a complete scene (including the loaded stage and its settings) via [Save Scene](save_scene). To bundle the actual stage assets alongside the scene file so a recipient does not need to find the model themselves, use [Scene Bundle](scene_bundle).

---

## Related pages

- [Room Stage](room_stage)
- [Props](props)
- [Ground](ground)
- [Lighting](lighting)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)
