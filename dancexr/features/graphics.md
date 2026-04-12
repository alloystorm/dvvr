---
locale: en-US
layout: single
title: Graphics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## Overview
The Graphics settings control the visual quality of the scene. These settings affect rendering performance, so balancing quality and performance to suit your hardware is recommended.

## Anti-Aliasing
Reduces jagged edges on rendered geometry. Available modes typically include None, FXAA, SMAA, and TAA depending on the render pipeline. Higher quality modes have greater performance cost.

## Bloom
Simulates the glow effect of bright light sources. When enabled, bright areas of the scene emit a soft glow. Intensity and threshold can be adjusted.

## Depth of Field (DOF)
Simulates camera focus by blurring objects outside the focal distance. Useful for cinematic rendering.

## Lens Flare
Adds optical lens flare effects when bright light sources are in view.

## Tonemapping
Controls how the rendered high-dynamic-range (HDR) image is mapped to the display. Affects the overall contrast and color response of the scene.

## Color Grading
Adjusts the final color appearance of the scene including brightness, contrast, saturation, and color balance.

## Reflections
Controls screen-space or baked reflections on reflective surfaces.

## Render Scale
Scales the internal rendering resolution relative to the display resolution. Values below 1.0 improve performance at the cost of sharpness. Values above 1.0 provide supersampling for higher quality.

## Fog
Adds distance-based atmospheric fog to the scene. Fog color, density, and start/end distances can be configured in [Sky Settings](/dancexr/features/sky_settings).

## Toon Shading
Applies a cel-shaded or toon rendering style to actors and objects in the scene. See also the dedicated [Toon Shading](/dancexr/features/toon_shading) feature page.

## Posterization
Reduces the number of distinct color levels in the rendered image, creating a stylized poster-like appearance.

## Additional notes

### Render Quality Improvements (v2025.10)
Improved shader for better skin effect and removed excessive sky reflection on skin & hair objects for LW & Android versions. Improved handling of detail & mask textures for better visual quality.

### Unity 6.3 upgrade and DLSS update (v2026.2)
DanceXR 2026.2 upgrades the underlying Unity engine to version 6.3, bringing performance enhancements, improved graphics capabilities, and access to the latest engine features. Unity 6.3 ships with DLSS version 310.4.0.0, further improving performance and visual quality on supported NVIDIA GPUs.

### Shader optimization (v2026.3)
Dedicated shader variants have been added for simpler scenarios — specifically when the **Outfit** and **Sweat Effect** advanced features are not in use. This results in a noticeable frame-rate increase, especially at high resolutions and in VR.

### Note on foveated rendering (v2026.3)
Foveated rendering on PC requires DX12 and disabling post-processing and shadows, which significantly limits its usefulness. Unity currently has no plan to broaden its availability on PC. On Quest standalone, foveated rendering works as expected.

