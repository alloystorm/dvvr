---
locale: en-rUS
layout: single
title: Graphics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

Render quality settings.

## Configurations

For detailed explaination of the configurations, please visit the following page:

[Graphics v2025.4](/dancexr/menu/2025.4/system/graphics)

### Render Quality Improvements (v2025.10)
Improved shader for better skin effect and removed excessive sky reflection on skin & hair objects for LW & Android versions.
Improved handling of detail & mask textures for better visual quality.

### Unity 6.3 upgrade and DLSS update (v2026.2)
DanceXR 2026.2 upgrades the underlying Unity engine to version 6.3, bringing performance enhancements, improved graphics capabilities, and access to the latest engine features. Unity 6.3 ships with DLSS version 310.4.0.0, further improving performance and visual quality on supported NVIDIA GPUs.

### Shader optimization (v2026.3)
Dedicated shader variants have been added for simpler scenarios — specifically when the **Outfit** and **Sweat Effect** advanced features are not in use. This results in a noticeable frame-rate increase, especially at high resolutions and in VR.

### Note on foveated rendering (v2026.3)
Foveated rendering on PC requires DX12 and disabling post-processing and shadows, which significantly limits its usefulness. Unity currently has no plan to broaden its availability on PC. On Quest standalone, foveated rendering works as expected.

