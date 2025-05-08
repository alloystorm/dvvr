---
locale: en-rUS
layout: single
title: Graphics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/system/graphics) | [繁中](/tw/dancexr/menu/2025.5/system/graphics) | [日本語](/jp/dancexr/menu/2025.5/system/graphics) | [한국어](/kr/dancexr/menu/2025.5/system/graphics) | [简中](/zh/dancexr/menu/2025.5/system/graphics)

[System](../menu#System) > Graphics


Settings for graphics quality for HD & RT versions.

## Presets
- Performance: No reflection, minimum effects, shadow map.
- Medium: Screenspace shadow, fog enabled.
- High: With reflections.
- Indoor GI: Global illumination without sky influences.
- Outdoor GI: Global illumination with sky.
- Toon Effect: Flat shading for actors and stages. All effects off.



## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| > Anti-Aliasing | **Deferred SMAA** | No AA, Deferred SMAA, Deferred TAA,  |
| ☑ **Raytracing** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Reflection | [ON] | 
| ├─☑ Ambient Occlusion | [ON] | 
| ├─☑ Global Illumination | [ON] | 
| ├─☑ Shadow | [ON] | 
| ├─☐ Contact Shadow | [OFF] | 
| ├─⊖ Ray Length | [50] (0 ~ 100) | 
| ├─☑ Denoise | [ON] | 
| └─⊖ Denoise Radius | [0.1] (0 ~ 1) | 
| ☐ **Path Tracing (Experimental)** | | 
| ├─☐ Enable | [OFF] | 
| ├─☑ Responsive Mode | [ON] | Disable accumulation and denoising when the UI is visible.
| ├─⊖ Max Samples | [5] (2 ~ 10) | 
| ├─⊖ Accumulate Frames | [1] (0 ~ 16) | 
| ├─⊖ Shutter Open | [0.25] (0 ~ 1) | 
| ├─⊖ Shutter Close | [0.75] (0 ~ 1) | 
| ├─☑ Denoise | None | None, Open Image, Optix, 
| ├─☑ Use AOVs | [ON] | 
| ├─☑ Temporal | [ON] | 
| ├─⊖ Min Depth | [1] (1 ~ 32) | 
| ├─⊖ Max Depth | [16] (1 ~ 32) | 
| ├─⊖ Max Intensity | [10] (0 ~ 100) | 
| ├─☑ Sky Sampling | HDRI Only | HDRI Only, On, Off, 
| └─≡ Presets | **Low (Single Sample)** | Low (Single Sample), Medium (Multi-Sampled), High (Denoised),  |
| > Super Sampling | **Off** | Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| ☑ **Reflection** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Mode | Screen Space | Screen Space, Probe, 
| ├─☑ Quality | High | Low, Medium, High, 
| ├─☑ Algorithm | Approximation | Approximation, PBRAccumulation, <br/>Algorithm for screen space reflection.
| ├─⊖ Edge Fade Dist | [0.1] (0 ~ 1) | 
| ├─⊖ Object Thickness | [0.01] (0 ~ 0.1) | 
| ├─☐ Fallback To Sky | [OFF] | Fallback to sky color when raytracing has no hit.
| └─☐ Sky Reflection | [OFF] | 
| ☑ **Fog** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Volumetric Fog | [ON] | 
| ├─⊖ Base Height | [0] (0 ~ 10) | 
| ├─⊖ Max Height | [25] (10 ~ 100) | 
| └─⊖ Max Distance | [5000] (0 ~ 10000) | 
| ☐ **Ambient Occlusion** | | 
| ├─☐ Enable | [OFF] | 
| ├─☑ Quality | High | Low, Medium, High, 
| └─⊖ Intensity | [1] (0 ~ 1) | 
| ☑ **Global Illumination** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Quality | Low | Low, Medium, High, 
| └─☐ Fallback To Sky | [OFF] | 
| ☐ **Depth Of Field** | | 
| ├─☐ Enable | [OFF] | 
| ├─☑ Quality | Medium | Low, Medium, High, 
| ├─⊖ Intensity | [0.25] (0 ~ 1) | 
| └─⊖ Offset | [0.1] (-1 ~ 1) | 
| ☐ **Motion Blur** | | 
| ├─☐ Enable | [OFF] | 
| ├─☑ Quality | Medium | Low, Medium, High, 
| └─⊖ Intensity | [0.25] (0 ~ 1) | 
| ☑ **Bloom** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Quality | High | Low, Medium, High, 
| └─⊖ Intensity | [0.25] (0 ~ 1) | 
| ☑ **Lens Flare** | | 
| ├─☑ Enable | [ON] | 
| ├─☑ Disable in VR | [ON] | This effect is not recommended for VR
| ├─⊖ Intensity | [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| │ ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| │ └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─⊖ Flares | [1] (0 ~ 1) | 
| ├─⊖ Streaks | [0.2] (0 ~ 1) | 
| ├─⊖ Length | [0.5] (0 ~ 1) | 
| └─⊖ Chromatic Abberation | [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color Adjustment** | | 
| ├─☑ Tonemapping | Neutral | None, Neutral, ACES, Custom, 
| ├─☑ Adjustment | [ON] | Enable color adjustment.
| ├─⊖ Post Exposure | [0] (-12 ~ 12) | 
| ├─⊖ Contrast | [1] (-100 ~ 100) | 
| ├─⊖ Hue Shift | [0] (-180 ~ 180) | 
| ├─⊖ Saturation | [1] (-100 ~ 100) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color Filter** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─⊖ Glow | [0] (0 ~ 100) | 
| │ └─≡ Presets | **White** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| ├─☑ Color Curve | [ON] | 
| ├─⊖ Start Gradient | [1] (0 ~ 4) | 
| ├─⊖ Start Position | [0] (0 ~ 0.5) | 
| ├─⊖ Start Value | [0] (0 ~ 0.5) | 
| ├─⊖ End Gradient | [1] (0 ~ 4) | 
| ├─⊖ End Position | [1] (0.5 ~ 1) | 
| ├─⊖ End Value | [1] (0.5 ~ 1) | 
| ├─☑ White Balance | [ON] | Enable white balance.
| ├─⊖ Temperature | [0] (-100 ~ 100) | 
| └─⊖ Tint | [0] (-100 ~ 100) | 
| ☐ **Posterization** | | 
| ├─☐ Enable | [OFF] | 
| ├─⊖ Outline Thickness | [0.1] (0 ~ 1) | 
| ├─⊖ Outline Intensity | [1] (0 ~ 1) | 
| ├─⊖ Quantize Illumination | [8] (0 ~ 16) | 
| ├─⊖ Quantize Color | [0] (0 ~ 64) | 
| ├─⊖ Dithering | [0.25] (0 ~ 1) | 
| ├─⊖ Halftone Size | [0.25] (0 ~ 1) | Halftone size
| ├─⊖ Halftone Strength | [0.1] (0 ~ 1) | Halftone strength
| └─≡ Presets | **Outline** | Outline, Black & White, Posterize, Halftone,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Options** | | 
| ├─☑ Transparent Prepass | [ON] | Enable transparent prepass. This will make obscured transparent materials invisible.
| ├─☑ Screen Space Shadows | [ON] | 
| ├─☐ Contact Shadow | [OFF] | Shadow for small details.
| ├─⊖ Bump Map Shadow | [0.5] (0 ~ 1) | Enable shadows for bump map and detail map.
| ├─☑ Stop NaN | [ON] | Prevent black screen when error happens during post processing. 
| ├─☑ Compute Thickness | [ON] | Calculate thickness that can be used in skin effect.
| ├─☐ Actor Model Toon Shading | [OFF] | Use toon shading for all actors.
| └─☐ Stage Model Toon Shading | [OFF] | Use toon shading for stages and props.
| ≡ Presets | **Indoor GI** | Performance, Medium, High, Indoor GI, Outdoor GI, Toon Effect,  |
