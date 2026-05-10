---
layout: release
title: Raytracing Effects
locale: en-US
toc: true
---

# Raytracing Effects

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.2, 2025.1, 2025.4, 2025.5). -->

The **RT** build of DanceXR uses Unity HDRP's hardware-accelerated raytracing for a set of effects that go beyond what screen-space techniques can produce: indirect bounce light, accurate reflections, true contact shadows, and (experimentally) full pathtracing.

Available on **PC RT builds only**, with an RT-capable GPU. The HD build can use screen-space approximations of most of these effects; the LW / Android / Quest builds use simpler shaders.

---

## Reflection

Real-time raytraced reflections — the scene reflected in glossy and metallic surfaces is computed by tracing rays into the world rather than sampling a screen capture.

Settings:

- **Sky reflection control** (added 2025.4) — how much of the sky environment is mixed into the reflection. Turn this **down** for indoor scenes; turn it **up** outdoors.
- **Raytracing fallback to sky** (2025.4) — when a reflected ray finds nothing to hit, falls back to the sky color. Disable for indoor scenes so dark interiors don't get sky-tinted reflections.

Translucent objects also receive realistic shadows in RT builds (2025.1).

---

## Ambient occlusion

Raytraced AO computes contact darkening by tracing short rays from each shaded surface. Compared to screen-space AO, this captures occlusion that is off-screen, behind the camera, or hidden by depth.

---

## Global illumination

Indirect bounce light. A wall lit by sunlight bounces some of that light onto a face nearby; raytraced GI captures that bounce instead of relying on baked light or precomputed probes.

GI was tuned in **2025.4** with **GI Indoor** and **GI Outdoor** presets — start from those, then fine-tune.

---

## Shadow

Raytraced shadows produce sharp contact shadows and softer penumbras at distance. Translucent surfaces cast translucent (color-tinted) shadows.

---

## Contact shadow

Short-range contact shadows — the shadows in seams, corners, under buttons — are traced with an accurate technique that screen-space solutions struggle with at edges of the screen.

---

## Pathtracing (experimental, 2025.5+)

Full pathtracing for real-time preview and offline recording (Creator only). Pathtracing simulates the full transport of light — direct, indirect, refractions, glowing emissive objects illuminating the scene.

Pathtraced output is **noisy** by default. Reduce noise with:

- **Frame accumulation** — combine multiple frames; more frames = less noise but the image only stabilizes when the camera is still.
- **Lower max bounce depth** — fewer light bounces, less indirect noise, less realism.
- **Disable translucent skin** — skin scattering is a major noise source in pathtracing. Turn it off in [Skin Materials](material_skin).
- **Denoiser** — pick **Open Image Denoise** (slower, more accurate) or **Optix Denoiser** (faster, less detail-preserving).

This feature is experimental and may not perform well in every scene.

---

## Related pages

- [Graphics](graphics)
- [Lighting](lighting)
- [Material Settings](material_settings)
- [Skin Materials](material_skin)
- [Creator Edition](../creator) — for offline pathtraced recording
