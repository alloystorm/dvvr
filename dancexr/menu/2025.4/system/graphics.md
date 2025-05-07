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



[Feature Page](/dancexr/features/graphics)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anti-Aliasing| **Deferred SMAA** | No AA, Deferred SMAA, Deferred TAA,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Raytracing</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Reflection| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Ambient Occlusion| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Global Illumination| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Shadow| [ON] | 
| ├─ □ Contact Shadow| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ray Length| [50] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Denoise| [ON] | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Super Sampling| **Off** | Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Reflection</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ ☑ Mode| Screen Space | Screen Space, Probe, 
| ├─ ☑ Quality| High | Low, Medium, High, 
| ├─ ☑ Algorithm| Approximation | Approximation, PBRAccumulation, <br/>Algorithm for screen space reflection.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Edge Fade Dist| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Object Thickness| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Fallback To Sky| [ON] | Fallback to sky color when raytracing has no hit.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Sky Reflection| [ON] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Fog</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volumetric Fog| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Base Height| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Height| [25] (10 ~ 100) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Distance| [5000] (0 ~ 10000) | 
|  □ <b>Ambient Occlusion</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Quality| High | Low, Medium, High, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [1] (0 ~ 1) | 
|  □ <b>Global Illumination</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Quality| Low | Low, Medium, High, 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Fallback To Sky| [ON] | 
|  □ <b>Depth Of Field</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Quality| Medium | Low, Medium, High, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [0.25] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Offset| [0.1] (-1 ~ 1) | 
|  □ <b>Motion Blur</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Quality| Medium | Low, Medium, High, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Bloom</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ ☑ Quality| High | Low, Medium, High, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Lens Flare</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Disable in VR| [ON] | This effect is not recommended for VR
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─ □ Use Stage Color| [OFF] | Use the color from the stage ring
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Flares| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Streaks| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Length| [0.5] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Chromatic Abberation| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Color Adjustment</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Post Exposure| [0] (-12 ~ 12) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Contrast| [1] (-100 ~ 100) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue Shift| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Saturation| [1] (-100 ~ 100) | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color Filter</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ Color Mode| HSV | RGB, HSV, 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow| [1] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **White** | White, Red, Green, Blue, Animated Hue, Glow w/ Music,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Color Curve</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Start Gradient| [1] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Start Position| [0] (0 ~ 0.5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Start Value| [0] (0 ~ 0.5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> End Gradient| [1] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> End Position| [1] (0.5 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> End Value| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>White Balance</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Temperature| [0] (-100 ~ 100) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tint| [0] (-100 ~ 100) | 
|  □ <b>Special Render</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Mode| Depth Output | Depth Output, Normal Output, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth Range| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth Scale| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Normal Scale| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Normal Blend| [0] (0 ~ 1) | 
| ☑ Tonemapping| Custom | None, Neutral, ACES, Custom, 
|  □ Actors Toon Shading| [OFF] | Use toon shading for all actors.
|  □ Stages Toon Shading| [OFF] | Use toon shading for stages and props.
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Options</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Transparent Prepass| [ON] | Enable transparent prepass. This will make obscured transparent materials invisible.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Screen Space Shadows| [ON] | 
| ├─ □ Contact Shadow| [OFF] | Shadow for small details.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump Map Shadow| [0.5] (0 ~ 1) | Enable shadows for bump map and detail map.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Stop NaN| [ON] | Prevent black screen when error happens during post processing. 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Compute Thickness| [ON] | Calculate thickness that can be used in skin effect.
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **High** | Performance, Medium, High, Indoor GI, Outdoor GI, Toon Effect,  |
