---
locale: en-rUS
layout: single
title: Graphics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[System](../menu#System) > Graphics



| Setting | Value | Description |
| :--- | --- | :--- |
| Anti-Aliasing: Deferred SMAA || 0/18/True
| Anti-Aliasing | **Deferred SMAA** | No AA, Deferred SMAA, Deferred TAA,  |
| **Raytracing** | | 1/18/True
| ├ Enable Raytracing | ON | 0/8/False
| ├ Reflection | ON | 1/8/False
| ├ Ambient Occlusion | ON | 2/8/False
| ├ Global Illumination | ON | 3/8/False
| ├ Shadow | ON | 4/8/False
| ├ Contact Shadow | OFF | 5/8/False
| ├ Ray Length | [50] (0 ~ 100) | 6/8/False
| ├ Denoise | ON | 7/8/False
| └ Denoise Radius | [0.1] (0 ~ 1) | 8/8/False
| Super Sampling: Off || 2/18/True
| Super Sampling | **Off** | Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **Reflection** | | 3/18/True
| ├ Enable Reflection | ON | 0/7/False
| ├ Mode | Screen Space | Screen Space, Probe, 1/7/False
| ├ Quality | High | Low, Medium, High, 2/7/False
| ├ Algorithm | Approximation | Approximation, PBRAccumulation, <br/>Algorithm for screen space reflection.3/7/False
| ├ Edge Fade Dist | [0.1] (0 ~ 1) | 4/7/False
| ├ Object Thickness | [0.01] (0 ~ 0.1) | 5/7/False
| ├ Fallback To Sky | ON | Fallback to sky color when raytracing has no hit.6/7/False
| └ Sky Reflection | ON | 7/7/False
| **Fog** | | 4/18/True
| ├ Enable Fog | ON | 0/4/False
| ├ Volumetric Fog | ON | 1/4/False
| ├ Base Height | [0] (0 ~ 10) | 2/4/False
| ├ Max Height | [25] (10 ~ 100) | 3/4/False
| └ Max Distance | [5000] (0 ~ 10000) | 4/4/False
| **Ambient Occlusion** | | 5/18/True
| ├ Enable Ambient Occlusion | OFF | 0/2/False
| ├ Quality | High | Low, Medium, High, 1/2/False
| └ Intensity | [1] (0 ~ 1) | 2/2/False
| **Global Illumination** | | 6/18/True
| ├ Enable Global Illumination | OFF | 0/2/False
| ├ Quality | Low | Low, Medium, High, 1/2/False
| └ Fallback To Sky | ON | 2/2/False
| **Depth Of Field** | | 7/18/True
| ├ Enable Depth Of Field | OFF | 0/3/False
| ├ Quality | Medium | Low, Medium, High, 1/3/False
| ├ Intensity | [0.25] (0 ~ 1) | 2/3/False
| └ Offset | [0.1] (-1 ~ 1) | 3/3/False
| **Motion Blur** | | 8/18/True
| ├ Enable Motion Blur | OFF | 0/2/False
| ├ Quality | Medium | Low, Medium, High, 1/2/False
| └ Intensity | [0.25] (0 ~ 1) | 2/2/False
| **Bloom** | | 9/18/True
| ├ Enable Bloom | ON | 0/2/False
| ├ Quality | High | Low, Medium, High, 1/2/False
| └ Intensity | [0.25] (0 ~ 1) | 2/2/False
| **Lens Flare** | | 10/18/True
| ├ Enable Lens Flare | ON | 0/7/False
| ├ Disable in VR | ON | This effect is not recommended for VR1/7/False
| ├ Intensity | [0.1] (0 ~ 1) | 2/7/False
| ├ **Color** | | 3/7/False
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Use Stage Color | OFF | Use the color from the stage ring7/8/True
| │ ├ Color Temp | [6500] (3000 ~ 8000) | 8/8/True
| │ └ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├ Flares | [1] (0 ~ 1) | 4/7/False
| ├ Streaks | [0.2] (0 ~ 1) | 5/7/False
| ├ Length | [0.5] (0 ~ 1) | 6/7/False
| └ Chromatic Abberation | [0.5] (0 ~ 1) | 7/7/False
| **Color Adjustment** | | 11/18/True
| ├ Enable Color Adjustment | ON | 0/5/False
| ├ Post Exposure | [0] (-12 ~ 12) | 1/5/False
| ├ Contrast | [1] (-100 ~ 100) | 2/5/False
| ├ Hue Shift | [0] (-180 ~ 180) | 3/5/False
| ├ Saturation | [1] (-100 ~ 100) | 4/5/False
| └ **Color Filter** | | 5/5/False
|   ├ Color Mode | HSV | RGB, HSV, 0/7/True
|   ├ Hue | [0] (0 ~ 1) | 1/7/True
|   ├ Satuation | [0] (0 ~ 1) | 2/7/True
|   ├ Brightness | [1] (0 ~ 1) | 3/7/True
|   ├ Red | [1] (0 ~ 1) | 4/7/True
|   ├ Green | [1] (0 ~ 1) | 5/7/True
|   ├ Blue | [1] (0 ~ 1) | 6/7/True
|   ├ Glow | [1] (0 ~ 20) | 7/7/True
|   └ Presets | **White** | White, Red, Green, Blue, Animated Hue, Glow w/ Music,  |
| **Color Curve** | | 12/18/True
| ├ Enable Color Curve | ON | 0/6/False
| ├ Start Gradient | [1] (0 ~ 4) | 1/6/False
| ├ Start Position | [0] (0 ~ 0.5) | 2/6/False
| ├ Start Value | [0] (0 ~ 0.5) | 3/6/False
| ├ End Gradient | [1] (0 ~ 4) | 4/6/False
| ├ End Position | [1] (0.5 ~ 1) | 5/6/False
| └ End Value | [1] (0.5 ~ 1) | 6/6/False
| **White Balance** | | 13/18/True
| ├ Enable White Balance | ON | 0/2/False
| ├ Temperature | [0] (-100 ~ 100) | 1/2/False
| └ Tint | [0] (-100 ~ 100) | 2/2/False
| **Special Render** | | 14/18/True
| ├ Enable Special Render | OFF | 0/5/False
| ├ Mode | Depth Output | Depth Output, Normal Output, 1/5/False
| ├ Depth Range | [1] (0 ~ 1) | 2/5/False
| ├ Depth Scale | [0.25] (0 ~ 1) | 3/5/False
| ├ Normal Scale | [1] (0 ~ 1) | 4/5/False
| └ Normal Blend | [0] (0 ~ 1) | 5/5/False
| Tonemapping | Custom | None, Neutral, ACES, Custom, 15/18/True
| Actors Toon Shading | OFF | Use toon shading for all actors.16/18/True
| Stages Toon Shading | OFF | Use toon shading for stages and props.17/18/True
| **Options** | | 18/18/True
| ├ Transparent Prepass | ON | Enable transparent prepass. This will make obscured transparent materials invisible.0/5/False
| ├ Screen Space Shadows | ON | 1/5/False
| ├ Contact Shadow | OFF | Shadow for small details.2/5/False
| ├ Bump Map Shadow | [0.5] (0 ~ 1) | Enable shadows for bump map and detail map.3/5/False
| ├ Stop NaN | ON | Prevent black screen when error happens during post processing. 4/5/False
| └ Compute Thickness | ON | Calculate thickness that can be used in skin effect.5/5/False
| Presets | **High** | Performance, Medium, High, Indoor GI, Outdoor GI, Toon Effect,  |
