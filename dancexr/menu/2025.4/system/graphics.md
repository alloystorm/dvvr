---
locale: en-rUS
layout: single
title: Graphics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[System](../menu#System) > Graphics



| Setting | Value | Description |
| :--- | --- | :--- |
| Anti-Aliasing: Deferred SMAA || 
| Anti-Aliasing | **Deferred SMAA** | No AA, Deferred SMAA, Deferred TAA,  |
| **Raytracing** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Reflection | ON | 
| ├&nbsp;Ambient Occlusion | ON | 
| ├&nbsp;Global Illumination | ON | 
| ├&nbsp;Shadow | ON | 
| ├&nbsp;Contact Shadow | OFF | 
| ├&nbsp;Ray Length | [50] (0 ~ 100) | 
| ├&nbsp;Denoise | ON | 
| └&nbsp;Denoise Radius | [0.1] (0 ~ 1) | 
| Super Sampling: Off || 
| Super Sampling | **Off** | Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **Reflection** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Mode | Screen Space | Screen Space, Probe, 
| ├&nbsp;Quality | High | Low, Medium, High, 
| ├&nbsp;Algorithm | Approximation | Approximation, PBRAccumulation, <br/>Algorithm for screen space reflection.
| ├&nbsp;Edge Fade Dist | [0.1] (0 ~ 1) | 
| ├&nbsp;Object Thickness | [0.01] (0 ~ 0.1) | 
| ├&nbsp;Fallback To Sky | ON | Fallback to sky color when raytracing has no hit.
| └&nbsp;Sky Reflection | ON | 
| **Fog** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Volumetric Fog | ON | 
| ├&nbsp;Base Height | [0] (0 ~ 10) | 
| ├&nbsp;Max Height | [25] (10 ~ 100) | 
| └&nbsp;Max Distance | [5000] (0 ~ 10000) | 
| **Ambient Occlusion** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Quality | High | Low, Medium, High, 
| └&nbsp;Intensity | [1] (0 ~ 1) | 
| **Global Illumination** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Quality | Low | Low, Medium, High, 
| └&nbsp;Fallback To Sky | ON | 
| **Depth Of Field** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Quality | Medium | Low, Medium, High, 
| ├&nbsp;Intensity | [0.25] (0 ~ 1) | 
| └&nbsp;Offset | [0.1] (-1 ~ 1) | 
| **Motion Blur** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Quality | Medium | Low, Medium, High, 
| └&nbsp;Intensity | [0.25] (0 ~ 1) | 
| **Bloom** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Quality | High | Low, Medium, High, 
| └&nbsp;Intensity | [0.25] (0 ~ 1) | 
| **Lens Flare** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Disable in VR | ON | This effect is not recommended for VR
| ├&nbsp;Intensity | [0.1] (0 ~ 1) | 
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Use Stage Color | OFF | Use the color from the stage ring
| │&nbsp;├&nbsp;Color Temp | [6500] (3000 ~ 8000) | 
| │&nbsp;└&nbsp;Presets: White || 
| │&nbsp;&nbsp;&nbsp;Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├&nbsp;Flares | [1] (0 ~ 1) | 
| ├&nbsp;Streaks | [0.2] (0 ~ 1) | 
| ├&nbsp;Length | [0.5] (0 ~ 1) | 
| └&nbsp;Chromatic Abberation | [0.5] (0 ~ 1) | 
| **Color Adjustment** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Post Exposure | [0] (-12 ~ 12) | 
| ├&nbsp;Contrast | [1] (-100 ~ 100) | 
| ├&nbsp;Hue Shift | [0] (-180 ~ 180) | 
| ├&nbsp;Saturation | [1] (-100 ~ 100) | 
| └&nbsp;**Color Filter** | | 
| &nbsp;&nbsp;├&nbsp;Color Mode | HSV | RGB, HSV, 
| &nbsp;&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Glow | [1] (0 ~ 20) | 
| &nbsp;&nbsp;└&nbsp;Presets: White || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **White** | White, Red, Green, Blue, Animated Hue, Glow w/ Music,  |
| **Color Curve** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Start Gradient | [1] (0 ~ 4) | 
| ├&nbsp;Start Position | [0] (0 ~ 0.5) | 
| ├&nbsp;Start Value | [0] (0 ~ 0.5) | 
| ├&nbsp;End Gradient | [1] (0 ~ 4) | 
| ├&nbsp;End Position | [1] (0.5 ~ 1) | 
| └&nbsp;End Value | [1] (0.5 ~ 1) | 
| **White Balance** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Temperature | [0] (-100 ~ 100) | 
| └&nbsp;Tint | [0] (-100 ~ 100) | 
| **Special Render** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Mode | Depth Output | Depth Output, Normal Output, 
| ├&nbsp;Depth Range | [1] (0 ~ 1) | 
| ├&nbsp;Depth Scale | [0.25] (0 ~ 1) | 
| ├&nbsp;Normal Scale | [1] (0 ~ 1) | 
| └&nbsp;Normal Blend | [0] (0 ~ 1) | 
| Tonemapping | Custom | None, Neutral, ACES, Custom, 
| Actors Toon Shading | OFF | Use toon shading for all actors.
| Stages Toon Shading | OFF | Use toon shading for stages and props.
| **Options** | | 
| ├&nbsp;Transparent Prepass | ON | Enable transparent prepass. This will make obscured transparent materials invisible.
| ├&nbsp;Screen Space Shadows | ON | 
| ├&nbsp;Contact Shadow | OFF | Shadow for small details.
| ├&nbsp;Bump Map Shadow | [0.5] (0 ~ 1) | Enable shadows for bump map and detail map.
| ├&nbsp;Stop NaN | ON | Prevent black screen when error happens during post processing. 
| └&nbsp;Compute Thickness | ON | Calculate thickness that can be used in skin effect.
| Presets: High || 
| Presets | **High** | Performance, Medium, High, Indoor GI, Outdoor GI, Toon Effect,  |
