---
layout: release
title: 3D Snapshot
locale: en-US
toc: true
---

# 3D Snapshot

3D Snapshot exports the current pose of an actor to an OBJ-format 3D model file. Whatever pose, morph, and dressing state the actor is in at the moment of capture is baked into the exported geometry.

Output files land in the `export/` folder of your [content library](../preparecontent).

---

## When to use it

- Capture a specific pose for use in another 3D tool (Blender, ZBrush, Unity).
- Export a snapshot of a dressed-up character for printing or sharing.
- Bake a procedural dance pose into a static asset.
- Produce a still-life model where you do not need rig or animation data.

OBJ format only carries mesh and material references — bones, animation, morph data, and physics rigs are **not** exported. If you need a fully rigged export, use the original PMX/XPS source instead.

---

## Taking a snapshot

1. Pose the actor exactly the way you want — apply motion, then pause; or use [Keyframe animation](keyframe_animation) for a specific frame; or pose by hand with [Motion override](motion_override).
2. Click the actor's selection disc to open the actor menu.
3. Open the **Tools menu** (wrench-and-hammer icon next to the actor name).
4. Click **3D Snapshot**.
5. The exported OBJ and its texture references appear in the `export/` folder.

---

## What gets baked into the OBJ

- Final mesh deformation from the current pose, morphs, and any active physics state.
- Material references — texture filenames are written into the OBJ's MTL file.
- Submesh visibility — items hidden by [Dressing system](optionals) are excluded.

What is **not** included:

- Skeleton / bones.
- Animation curves.
- Morph targets (already baked in).
- Physics rigs.
- Shader-driven effects (toon shading, sweat, body paint overlays).

---

## Tips

- **Pause first.** A moving target is hard to capture. Pause playback, then snapshot.
- **Decide on dressing first.** Whatever is hidden via the dressing system at capture time is excluded from the OBJ. Toggle items on/off before snapping.
- **Watch texture paths.** OBJ files reference textures by relative path. If you move the OBJ to a new machine, copy the textures alongside it or point the MTL to the new location.

---

## Related pages

- [Actor menu & tools](actor_tools)
- [Content library](../preparecontent) — see the `export/` folder
- [Keyframe animation](keyframe_animation)
- [Motion override](motion_override)
