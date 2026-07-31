---
layout: feature
title: DanceXR Native
locale: en-US
toc: true
---

# DanceXR Native

**DanceXR Native** is a separate, standalone Windows application that renders your characters with full **path tracing** on NVIDIA RTX hardware. It is not a build of DanceXR — it is a purpose-built companion app with its own installer, its own settings, and its own content folder.

Currently in **public preview** (2026.8). Expect rough edges.

Download: [github.com/alloystorm/dvvr/releases/tag/dxr-native](https://github.com/alloystorm/dvvr/releases/tag/dxr-native)

---

## What path tracing gives you

DanceXR's PC RT build offers raytraced effects layered onto a conventional renderer (see [Raytracing Effects](raytracing)). Native takes the other approach: the entire image is path traced, so lighting is simulated rather than approximated.

- **Real bounced light** — a wall lit by a lamp throws colored light onto a nearby face, with no probes or baking.
- **Soft shadows** with true penumbras that widen with distance from the caster.
- **True reflections** — surfaces reflect what is actually in the room, including things off-screen or behind the camera.
- **Volumetric fog and light shafts** — a haze layer built into the path tracer itself, so beams and god-rays come from real light transport.

Two render modes:

- **Realtime** — denoised and upscaled for interactive framerates. This is where you pose, frame, and play back.
- **Reference** — accumulates samples over several seconds for a clean, noise-free image. Use it for stills.

---

## Requirements

| | |
|---|---|
| OS | Windows |
| GPU | Ray-tracing capable (NVIDIA RTX recommended) |
| VR | **Not supported** — desktop only |

If your GPU can't run it, the app tells you why on launch instead of failing silently.

---

## Supported content

This is the most important thing to know before you download.

- **Models: XPS / XNALara** (`.xps`, `.mesh`, `.ascii`), loose or in a ZIP.
- **Motions: VMD** (MikuMikuDance), including camera motion.

**PMX models are not supported yet.** PMX is the next major chapter for Native — it brings morphs, append/inherit deforms, and PMX physics content with it — but it is not in this preview. If your library is entirely PMX, this release won't have much for you yet.

Facial morphs are likewise not yet available, since XPS has no morph data.

### Preview limits

The free preview renders **one character at a time**. Dropping a second model replaces the first, and the app shows a notice when it does.

---

## Using it

Drag and drop is the primary way in — drop a model, a motion, or a ZIP onto the window and it loads. The interface is organized into tabs: **Actors**, **Motion**, **Camera**, **Environment**, **Scene**, and **System**.

### Posing and motion

- VMD motion playback with audio, kept in sync on a shared clock.
- Procedural idle motion when no clip is playing, plus eye contact so the character can look at the camera.
- Leg IK and a feet-on-floor solver, so feet plant on the ground rather than floating or sinking.
- Hair physics and shape-matching soft-body simulation, with body colliders.

### Placing characters

Hover a character's feet to bring up the interaction disc: drag to move on the ground plane, scroll to rotate. The disc is real emissive geometry, so its glow actually lights the character.

### Scenes and rooms

A procedural room with real window openings, adjustable lighting, and volumetric fog serves as the default environment. Scenes can be saved and reloaded by name, preserving character placement, materials, and motion assignment.

### Materials

Per-material controls for roughness, metalness, anisotropy, and subsurface scattering, with name-group remapping so you can adjust every "hair" material at once.

---

## Reporting problems

Native writes a per-session log and a crash dump if it falls over. The **System** tab has **Report Issue**, **Copy Diagnostics**, and **Open Log** — please include the log when you report something.

---

## Related pages

- [Raytracing Effects](raytracing) — raytraced effects in the DanceXR PC RT build
- [Graphics](graphics)
- [Organizing Model Files](../preparecontent#3d-models)
