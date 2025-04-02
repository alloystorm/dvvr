---
locale: en-rUS
layout: single
title: Graphics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/system/graphics.md) | [繁中](/tw/dancexr/menu/2025.4/system/graphics.md) | [日本語](/jp/dancexr/menu/2025.4/system/graphics.md) | [한국어](/kr/dancexr/menu/2025.4/system/graphics.md) | [简中](/zh/dancexr/menu/2025.4/system/graphics.md)
# Graphics
## 
| Setting | Value | Description |
| :--- | --- | :--- |
|**Graphics** | | 
| Anti-Aliasing |  No AA,  **Deferred SMAA**,  Deferred TAA,  |  |
|**Raytracing** | | 
| Enable Raytracing | ON | 
| Reflection | ON | 
| Ambient Occlusion | ON | 
| Global Illumination | ON | 
| Shadow | ON | 
| Contact Shadow | OFF | 
|- Ray Length| [50] (0 ~ 100) | 
| Denoise | ON | 
|- Denoise Radius| [0.1] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
| Super Sampling |  **Off**,  DLSS Performance,  DLSS Balance,  DLSS Quality,  DLSS Ultra Performance,  FSR 50%,  FSR 66%,  FSR 75%,  FSR 100%,  |  |
|**Reflection** | | 
| Enable Reflection | ON | 
|- Mode|  **Screen Space**,  | 
|- Quality|  Low,  Medium,  **High**,  | 
|- Algorithm|  **Approximation**,  | Algorithm for screen space reflection.
|- Edge Fade Dist| [0.1] (0 ~ 1) | 
|- Object Thickness| [0.01] (0 ~ 0.1) | 
| Fallback To Sky | ON | Fallback to sky color when raytracing has no hit.
| Sky Reflection | ON | 
| Reset || 
| Confirm Reset || 
|
|**Fog** | | 
| Enable Fog | ON | 
| Volumetric Fog | ON | 
|- Base Height| [0] (0 ~ 10) | 
|- Max Height| [25] (10 ~ 100) | 
|- Max Distance| [5000] (0 ~ 10000) | 
| Reset || 
| Confirm Reset || 
|
|**Ambient Occlusion** | | 
| Enable Ambient Occlusion | OFF | 
|- Quality|  Low,  Medium,  **High**,  | 
|- Intensity| [1] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Global Illumination** | | 
| Enable Global Illumination | OFF | 
|- Quality|  **Low**,  | 
| Fallback To Sky | ON | 
| Reset || 
| Confirm Reset || 
|
|**Depth Of Field** | | 
| Enable Depth Of Field | OFF | 
|- Quality|  Low,  **Medium**,  | 
|- Intensity| [0.25] (0 ~ 1) | 
|- Offset| [0.1] (-1 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Motion Blur** | | 
| Enable Motion Blur | OFF | 
|- Quality|  Low,  **Medium**,  | 
|- Intensity| [0.25] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Bloom** | | 
| Enable Bloom | ON | 
|- Quality|  Low,  Medium,  **High**,  | 
|- Intensity| [0.25] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Lens Flare** | | 
| Enable Lens Flare | ON | 
| Disable in VR | ON | This effect is not recommended for VR
|- Intensity| [0.1] (0 ~ 1) | 
|**Color** | | 
|- Color Mode|  **RGB**,  | 
|- Hue| [0] (0 ~ 1) | 
|- Satuation| [0] (0 ~ 1) | 
|- Brightness| [1] (0 ~ 1) | 
|- Red| [1] (0 ~ 1) | 
|- Green| [1] (0 ~ 1) | 
|- Blue| [1] (0 ~ 1) | 
| Use Stage Color | OFF | Use the color from the stage ring
|- Color Temp| [6500] (3000 ~ 8000) | 
| Presets |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- Flares| [1] (0 ~ 1) | 
|- Streaks| [0.2] (0 ~ 1) | 
|- Length| [0.5] (0 ~ 1) | 
|- Chromatic Abberation| [0.5] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Color Adjustment** | | 
| Enable Color Adjustment | ON | 
|- Post Exposure| [0] (-12 ~ 12) | 
|- Contrast| [1] (-100 ~ 100) | 
|- Hue Shift| [0] (-180 ~ 180) | 
|- Saturation| [1] (-100 ~ 100) | 
|**Color Filter** | | 
|- Color Mode|  RGB,  **HSV**,  | 
|- Hue| [0] (0 ~ 1) | 
|- Satuation| [0] (0 ~ 1) | 
|- Brightness| [1] (0 ~ 1) | 
|- Red| [1] (0 ~ 1) | 
|- Green| [1] (0 ~ 1) | 
|- Blue| [1] (0 ~ 1) | 
|- Glow| [1] (0 ~ 20) | 
| Presets |  **White**,  Red,  Green,  Blue,  Animated Hue,  Glow w/ Music,  |  |
|
| Reset || 
| Confirm Reset || 
|
|**Color Curve** | | 
| Enable Color Curve | ON | 
|- Start Gradient| [1] (0 ~ 4) | 
|- Start Position| [0] (0 ~ 0.5) | 
|- Start Value| [0] (0 ~ 0.5) | 
|- End Gradient| [1] (0 ~ 4) | 
|- End Position| [1] (0.5 ~ 1) | 
|- End Value| [1] (0.5 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**White Balance** | | 
| Enable White Balance | ON | 
|- Temperature| [0] (-100 ~ 100) | 
|- Tint| [0] (-100 ~ 100) | 
| Reset || 
| Confirm Reset || 
|
|**Special Render** | | 
| Enable Special Render | OFF | 
|- Mode|  **Depth Output**,  | 
|- Depth Range| [1] (0 ~ 1) | 
|- Depth Scale| [0.25] (0 ~ 1) | 
|- Normal Scale| [1] (0 ~ 1) | 
|- Normal Blend| [0] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|- Tonemapping|  None,  Neutral,  ACES,  **Custom**,  | 
| Actors Toon Shading | OFF | Use toon shading for all actors.
| Stages Toon Shading | OFF | Use toon shading for stages and props.
|**Options** | | 
| Transparent Prepass | ON | Enable transparent prepass. This will make obscured transparent materials invisible.
| Screen Space Shadows | ON | 
| Contact Shadow | OFF | Shadow for small details.
|- Bump Map Shadow| [0.5] (0 ~ 1) | Enable shadows for bump map and detail map.
| Stop NaN | ON | Prevent black screen when error happens during post processing. 
| Compute Thickness | ON | Calculate thickness that can be used in skin effect.
| Reset || 
| Confirm Reset || 
|
| Presets |  Performance,  Medium,  **High**,  Indoor GI,  Outdoor GI,  Toon Effect,  |  |
|
