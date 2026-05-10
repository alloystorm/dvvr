---
layout: release
title: VMD2PNG
locale: en-US
toc: true
---

# VMD2PNG

<!-- TODO: confirm details against the actual tool. Drafted from the 2026.3 release notes. -->

**VMD2PNG** is a separate open-source tool that encodes a `.vmd` motion file into a `.png` image. DanceXR can load motion data directly from these PNG files, so you can use them anywhere a VMD motion would normally go.

Added in **2026.3**.

[GitHub: alloystorm/vmd2png](https://github.com/alloystorm/vmd2png)

---

## Why use it

- **Smaller file size** than the original VMD in many cases.
- **Easier to share** — a PNG is readable as an image on any platform, with no special metadata to strip.
- **Visualization** — the PNG itself is a visual representation of the motion data, so you can see at a glance how dense or sparse a motion is.
- <!-- TODO: confirm whether the PNG also serves as a thumbnail / preview in the DanceXR motion picker. -->

---

## Loading a VMD2PNG file

Two equivalent paths:

1. **Drag and drop** the `.png` file onto the running DanceXR window — it loads as a motion just like a VMD. (See [drag-and-drop loading notes in 2026.3](../releases/2026.3) for how drag-and-drop interacts with dance sets.)
2. **Content library** — keep `.png` motion files in your `motions/` folder alongside `.vmd` / `.bvh` / `.pose` / `.vpd` files. They appear in the motion picker like any other motion.

---

## Encoding your own

Use the [VMD2PNG](https://github.com/alloystorm/vmd2png) command-line tool to convert an existing `.vmd` to `.png`. The output PNG is portable — anyone with a recent DanceXR build can load it.

<!-- TODO: confirm:
- Is decoding lossless? Round-trip vmd → png → vmd identity?
- Are camera / morph tracks preserved or only bone tracks?
- Any size or frame-count limits? -->

---

## Limitations

<!-- TODO: confirm. Likely:
- DanceXR versions before 2026.3 cannot load these.
- The PNG must not be re-encoded by image tools that strip the relevant metadata. -->

---

## Related pages

- [Assigning Motion](assign_motion)
- [Motion Settings](motion_settings)
- [Pose Files (.pose / .vpd)](pose_files)
- [Content Library](../preparecontent)
