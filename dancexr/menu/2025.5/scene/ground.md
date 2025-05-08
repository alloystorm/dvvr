---
locale: en-rUS
layout: single
title: Ground
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/scene/ground) | [繁中](/tw/dancexr/menu/2025.5/scene/ground) | [日本語](/jp/dancexr/menu/2025.5/scene/ground) | [한국어](/kr/dancexr/menu/2025.5/scene/ground) | [简中](/zh/dancexr/menu/2025.5/scene/ground)

[Environment](../menu#Environment) > Ground

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| ⊖ Ground Height | [0] (-2 ~ 2) | 
| ☑ **Ground** | | Ground Settings.
| ├─☑ Enable | [ON] | 
| ├─⊖ Radius | [200] (2 ~ 100) | Size of the ground mesh.
| ├─☑ Hide If Stage Present | [ON] | Hide ground when there are stage models.
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Surface** | | 
| │ ├─> Texture | **[Concrete]** | [Sky Map], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Tiling** | | 
| │ │ ├─⊖ Tiling X | [1] (0.1 ~ 10) | 
| │ │ ├─⊖ Tiling Y | [1] (0.1 ~ 10) | 
| │ │ ├─☑ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 
| │ │ ├─⊖ Offset X | [0] (0 ~ 1) | 
| │ │ ├─⊖ Offset Y | [0] (0 ~ 1) | 
| │ │ ├─⊖ Rotation | [0] (0 ~ 360) | 
| │ │ ├─⊖ Variation | [0.5] (0 ~ 1) | 
| │ │ └─☐ Fit Texture | [OFF] | 
| │ ├─⊖ Gloss | [0.95] (0 ~ 1) | 
| │ ├─⊖ Metallic | [0] (0 ~ 1) | 
| │ ├─⊖ Bump | [0.2] (0 ~ 1) | 
| │ ├─⊖ Glow | [0] (0 ~ 10) | 
| │ ├─⊖ Ambient | [1] (0 ~ 1) | 
| │ ├─⊖ Alpha | [1] (0 ~ 1) | 
| │ ├─⊖ Clip | [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ │ ├─> Blend Mode | **Multiply** | Original, Multiply, Blend, Color Shift,  |
| │ │ ├─⊖ Blend | [1] (0 ~ 1) | 
| │ │ └─≡ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| │ ├─☐ **Toon Shader** | | 
| │ │ ├─☐ Enable | [OFF] | 
| │ │ ├─⊖ Shading | [1] (0 ~ 1) | 
| │ │ ├─⊖ Outline | [0.5] (0 ~ 1) | 
| │ │ ├─⊖ Specular | [0.25] (0 ~ 1) | 
| │ │ ├─⊖ Soft Specular | [0.1] (0 ~ 1) | 
| │ │ ├─⊖ Highlight Area | [0.25] (0 ~ 1) | 
| │ │ ├─⊖ Soft Highlight | [0.1] (0 ~ 1) | 
| │ │ ├─⊖ Ambient | [0.75] (0 ~ 1) | 
| │ │ ├─⊖ Shadow Area | [0.65] (0 ~ 1) | 
| │ │ ├─⊖ Shadow | [0.75] (0 ~ 1) | 
| │ │ ├─⊖ Soft Shadow | [0.1] (0 ~ 1) | 
| │ │ └─≡ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Special Shader** | | 
| │ │ ├─> Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ │ ├─⊖ Refraction | [0.5] (1 ~ 3) | 
| │ │ └─⊖ Thickness | [1] (0 ~ 1) | 
| │ ├─⊖ Viewer Height | [1.5] (0.5 ~ 3) | Viewer height used when projecting the the texture on to the ground
| │ ├─☐ **LED Mode** | | 
| │ │ ├─☐ Enable | [OFF] | 
| │ │ ├─⊖ Density | [5] (4 ~ 10) | 
| │ │ ├─⊖ Size | [0.8] (0 ~ 1) | 
| │ │ ├─⊖ Soft Edge | [0.3] (0 ~ 1) | 
| │ │ ├─⊖ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect
| │ │ ├─⊖ Edge | [0] (0 ~ 1) | 
| │ │ └─⊖ Reduce Moire | [0.1] (0 ~ 1) | 
| │ ├─☐ **Audio Visualizer** | | 
| │ │ ├─☐ Enable | [OFF] | 
| │ │ ├─☑ Layout | Circle | Horizontal, Vertical, Circle, 
| │ │ ├─⊖ Radius | [0.5] (0 ~ 1) | 
| │ │ ├─⊖ Align | [0] (0 ~ 1) | 
| │ │ ├─⊖ Gap | [0.25] (0 ~ 1) | 
| │ │ ├─⊖ Shape Shift | [0.5] (0 ~ 1) | 
| │ │ ├─☐ Beat Clock | [OFF] | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Ring Color** | | 
| │ │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ │ │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ │ │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ │ │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ │ │ ├─⊖ Glow | [20] (0 ~ 100) | 
| │ │ │ └─≡ Presets | **White** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Background Color** | | 
| │ │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ │ ├─> Background Image | **[None]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ │ ├─⊖ Background Vibration | [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Foreground Color** | | 
| │ │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ │ ├─> Foreground Image | **[DanceXR]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ │ ├─⊖ Foreground Vibration | [0.5] (0 ~ 1) | 
| │ │ ├─⊖ Foreground Scale | [1] (0 ~ 2) | 
| │ │ └─☐ Auto BPM | [OFF] | Use real-time automatically detected BPM instead of the set BPM.
| │ └─≡ Presets | **Concrete** | Sky Map, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glass,  |
| └─☐ **Shadow Only** | | 
|   ├─ **Shadow Color** || 
|   ├─≡ Presets | **Black** | White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange, Preset 1,  |
|   ├─☑ Color Mode | RGB | RGB, HSV, 
|   ├─⊖ Hue | [0] (0 ~ 1) | 
|   ├─⊖ Satuation | [0] (0 ~ 1) | 
|   ├─⊖ Brightness | [0] (0 ~ 1) | 
|   ├─⊖ Red | [0] (0 ~ 1) | 
|   ├─⊖ Green | [0] (0 ~ 1) | 
|   ├─⊖ Blue | [0] (0 ~ 1) | 
|   └─⊖ Transparency | [0.5] (0 ~ 1) | 
| ☑ Stage Geometry | [OFF] | 
| ≡ Presets | **Projector Screen** | None, Runway, Pool, Room, Background Board, Projector Screen, LED Box,  |
| ⊖ Lift | [0.5] (-5 ~ 5) | Lift the stage up / down.
| ⊖ Front / Back Offset | [0] (-10 ~ 10) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Geometry** | | 
| ├─⊖ Center Width | [8] (0 ~ 10) | Width of the center area.
| ├─⊖ Center Depth | [5] (0 ~ 9) | Depth of the center area.
| ├─⊖ Back Height | [0] (0 ~ 9) | Height of the background board.
| ├─⊖ Side Extension | [0] (0 ~ 5) | Extension at left and right.
| ├─⊖ Front Extension | [0] (0 ~ 10) | Extension at front.
| ├─⊖ Back Extension | [0] (0 ~ 10) | Extension at back.
| ├─⊖ Wall Height | [0.05] (0 ~ 5) | Height of the edge above ground.
| ├─⊖ Wall Thickness | [0.1] (0 ~ 1) | Size of the edge.
| ├─⊖ Window | [0] (0 ~ 1) | 
| └─☐ Floating | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Surface: Top** | | 
| ├─> Texture | **[Tiles]** | [Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Tiling** | | 
| │ ├─⊖ Tiling X | [1] (0.1 ~ 10) | 
| │ ├─⊖ Tiling Y | [1] (0.1 ~ 10) | 
| │ ├─☑ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 
| │ ├─⊖ Offset X | [0] (0 ~ 1) | 
| │ ├─⊖ Offset Y | [0] (0 ~ 1) | 
| │ ├─⊖ Rotation | [0] (0 ~ 360) | 
| │ ├─⊖ Variation | [0.5] (0 ~ 1) | 
| │ └─☐ Fit Texture | [OFF] | 
| ├─⊖ Gloss | [0.95] (0 ~ 1) | 
| ├─⊖ Metallic | [0] (0 ~ 1) | 
| ├─⊖ Bump | [0.2] (0 ~ 1) | 
| ├─⊖ Glow | [0] (0 ~ 10) | 
| ├─⊖ Ambient | [1] (0 ~ 1) | 
| ├─⊖ Alpha | [1] (0 ~ 1) | 
| ├─⊖ Clip | [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─> Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├─⊖ Blend | [1] (0 ~ 1) | 
| │ └─≡ Presets | **Black** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─☐ **Toon Shader** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Shading | [1] (0 ~ 1) | 
| │ ├─⊖ Outline | [0.5] (0 ~ 1) | 
| │ ├─⊖ Specular | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Specular | [0.1] (0 ~ 1) | 
| │ ├─⊖ Highlight Area | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Highlight | [0.1] (0 ~ 1) | 
| │ ├─⊖ Ambient | [0.75] (0 ~ 1) | 
| │ ├─⊖ Shadow Area | [0.65] (0 ~ 1) | 
| │ ├─⊖ Shadow | [0.75] (0 ~ 1) | 
| │ ├─⊖ Soft Shadow | [0.1] (0 ~ 1) | 
| │ └─≡ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Special Shader** | | 
| │ ├─> Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─⊖ Refraction | [0.5] (1 ~ 3) | 
| │ └─⊖ Thickness | [1] (0 ~ 1) | 
| ├─☐ **LED Mode** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Density | [5] (4 ~ 10) | 
| │ ├─⊖ Size | [0.8] (0 ~ 1) | 
| │ ├─⊖ Soft Edge | [0.3] (0 ~ 1) | 
| │ ├─⊖ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect
| │ ├─⊖ Edge | [0] (0 ~ 1) | 
| │ └─⊖ Reduce Moire | [0.1] (0 ~ 1) | 
| ├─☐ **Audio Visualizer** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─☑ Layout | Circle | Horizontal, Vertical, Circle, 
| │ ├─⊖ Radius | [0.5] (0 ~ 1) | 
| │ ├─⊖ Align | [0] (0 ~ 1) | 
| │ ├─⊖ Gap | [0.25] (0 ~ 1) | 
| │ ├─⊖ Shape Shift | [0.5] (0 ~ 1) | 
| │ ├─☐ Beat Clock | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Ring Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [20] (0 ~ 100) | 
| │ │ └─≡ Presets | **White** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Background Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Background Image | **[None]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Background Vibration | [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Foreground Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Foreground Image | **[DanceXR]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Foreground Vibration | [0.5] (0 ~ 1) | 
| │ ├─⊖ Foreground Scale | [1] (0 ~ 2) | 
| │ └─☐ Auto BPM | [OFF] | Use real-time automatically detected BPM instead of the set BPM.
| └─≡ Presets | **Black Gloss** | Blank, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glass, Preset 1,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Surface: Sides** | | 
| ├─> Texture | **[Tiles]** | [Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Tiling** | | 
| │ ├─⊖ Tiling X | [1] (0.1 ~ 10) | 
| │ ├─⊖ Tiling Y | [1] (0.1 ~ 10) | 
| │ ├─☑ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 
| │ ├─⊖ Offset X | [0] (0 ~ 1) | 
| │ ├─⊖ Offset Y | [0] (0 ~ 1) | 
| │ ├─⊖ Rotation | [0] (0 ~ 360) | 
| │ ├─⊖ Variation | [0.5] (0 ~ 1) | 
| │ └─☐ Fit Texture | [OFF] | 
| ├─⊖ Gloss | [0.95] (0 ~ 1) | 
| ├─⊖ Metallic | [0] (0 ~ 1) | 
| ├─⊖ Bump | [0.2] (0 ~ 1) | 
| ├─⊖ Glow | [0] (0 ~ 10) | 
| ├─⊖ Ambient | [1] (0 ~ 1) | 
| ├─⊖ Alpha | [1] (0 ~ 1) | 
| ├─⊖ Clip | [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─> Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├─⊖ Blend | [1] (0 ~ 1) | 
| │ └─≡ Presets | **Black** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─☐ **Toon Shader** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Shading | [1] (0 ~ 1) | 
| │ ├─⊖ Outline | [0.5] (0 ~ 1) | 
| │ ├─⊖ Specular | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Specular | [0.1] (0 ~ 1) | 
| │ ├─⊖ Highlight Area | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Highlight | [0.1] (0 ~ 1) | 
| │ ├─⊖ Ambient | [0.75] (0 ~ 1) | 
| │ ├─⊖ Shadow Area | [0.65] (0 ~ 1) | 
| │ ├─⊖ Shadow | [0.75] (0 ~ 1) | 
| │ ├─⊖ Soft Shadow | [0.1] (0 ~ 1) | 
| │ └─≡ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Special Shader** | | 
| │ ├─> Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─⊖ Refraction | [0.5] (1 ~ 3) | 
| │ └─⊖ Thickness | [1] (0 ~ 1) | 
| ├─☐ **LED Mode** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Density | [5] (4 ~ 10) | 
| │ ├─⊖ Size | [0.8] (0 ~ 1) | 
| │ ├─⊖ Soft Edge | [0.3] (0 ~ 1) | 
| │ ├─⊖ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect
| │ ├─⊖ Edge | [0] (0 ~ 1) | 
| │ └─⊖ Reduce Moire | [0.1] (0 ~ 1) | 
| ├─☐ **Audio Visualizer** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─☑ Layout | Circle | Horizontal, Vertical, Circle, 
| │ ├─⊖ Radius | [0.5] (0 ~ 1) | 
| │ ├─⊖ Align | [0] (0 ~ 1) | 
| │ ├─⊖ Gap | [0.25] (0 ~ 1) | 
| │ ├─⊖ Shape Shift | [0.5] (0 ~ 1) | 
| │ ├─☐ Beat Clock | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Ring Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [20] (0 ~ 100) | 
| │ │ └─≡ Presets | **White** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Background Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Background Image | **[None]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Background Vibration | [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Foreground Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Foreground Image | **[DanceXR]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Foreground Vibration | [0.5] (0 ~ 1) | 
| │ ├─⊖ Foreground Scale | [1] (0 ~ 2) | 
| │ └─☐ Auto BPM | [OFF] | Use real-time automatically detected BPM instead of the set BPM.
| └─≡ Presets | **Black Gloss** | Blank, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glass, Preset 1,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Surface: Background** | | 
| ├─> Texture | **[Tiles]** | [Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Tiling** | | 
| │ ├─⊖ Tiling X | [1] (0.1 ~ 10) | 
| │ ├─⊖ Tiling Y | [1] (0.1 ~ 10) | 
| │ ├─☑ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 
| │ ├─⊖ Offset X | [0] (0 ~ 1) | 
| │ ├─⊖ Offset Y | [0] (0 ~ 1) | 
| │ ├─⊖ Rotation | [0] (0 ~ 360) | 
| │ ├─⊖ Variation | [0.5] (0 ~ 1) | 
| │ └─☐ Fit Texture | [OFF] | 
| ├─⊖ Gloss | [0.95] (0 ~ 1) | 
| ├─⊖ Metallic | [0] (0 ~ 1) | 
| ├─⊖ Bump | [0.2] (0 ~ 1) | 
| ├─⊖ Glow | [0] (0 ~ 10) | 
| ├─⊖ Ambient | [1] (0 ~ 1) | 
| ├─⊖ Alpha | [1] (0 ~ 1) | 
| ├─⊖ Clip | [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─> Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├─⊖ Blend | [1] (0 ~ 1) | 
| │ └─≡ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─☐ **Toon Shader** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Shading | [1] (0 ~ 1) | 
| │ ├─⊖ Outline | [0.5] (0 ~ 1) | 
| │ ├─⊖ Specular | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Specular | [0.1] (0 ~ 1) | 
| │ ├─⊖ Highlight Area | [0.25] (0 ~ 1) | 
| │ ├─⊖ Soft Highlight | [0.1] (0 ~ 1) | 
| │ ├─⊖ Ambient | [0.75] (0 ~ 1) | 
| │ ├─⊖ Shadow Area | [0.65] (0 ~ 1) | 
| │ ├─⊖ Shadow | [0.75] (0 ~ 1) | 
| │ ├─⊖ Soft Shadow | [0.1] (0 ~ 1) | 
| │ └─≡ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Special Shader** | | 
| │ ├─> Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─⊖ Refraction | [0.5] (1 ~ 3) | 
| │ └─⊖ Thickness | [1] (0 ~ 1) | 
| ├─☐ **LED Mode** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Density | [5] (4 ~ 10) | 
| │ ├─⊖ Size | [0.8] (0 ~ 1) | 
| │ ├─⊖ Soft Edge | [0.3] (0 ~ 1) | 
| │ ├─⊖ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect
| │ ├─⊖ Edge | [0] (0 ~ 1) | 
| │ └─⊖ Reduce Moire | [0.1] (0 ~ 1) | 
| ├─☐ **Audio Visualizer** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─☑ Layout | Circle | Horizontal, Vertical, Circle, 
| │ ├─⊖ Radius | [0.5] (0 ~ 1) | 
| │ ├─⊖ Align | [0] (0 ~ 1) | 
| │ ├─⊖ Gap | [0.25] (0 ~ 1) | 
| │ ├─⊖ Shape Shift | [0.5] (0 ~ 1) | 
| │ ├─☐ Beat Clock | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Ring Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [20] (0 ~ 100) | 
| │ │ └─≡ Presets | **White** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Background Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Background Image | **[None]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Background Vibration | [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Foreground Color** | | 
| │ │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ │ ├─⊖ Brightness | [0] (0 ~ 1) | 
| │ │ ├─⊖ Red | [0] (0 ~ 1) | 
| │ │ ├─⊖ Green | [0] (0 ~ 1) | 
| │ │ ├─⊖ Blue | [0] (0 ~ 1) | 
| │ │ ├─⊖ Glow | [1] (0 ~ 100) | 
| │ │ └─≡ Presets | **Black** | White, Black, Yellow, Blue, Animated Hue, Glow w/ Music,  |
| │ ├─> Foreground Image | **[DanceXR]** | [None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video], 00004-4218936958, 00005-943778646, 00006-1780167286, 00007-337258668, 00095-4033100436, 30off, 30percentoff, 51bg, 9784551_192946924108_2, discount70, freevector-clothing-pattern, istockphoto-2034974965-2048x2048, istockphoto-472294061-2048x2048, promo_ads, splash_black, test2, pattern 01, pattern 03, Wooden floor 01, Wooden floor 03,  |
| │ ├─⊖ Foreground Vibration | [0.5] (0 ~ 1) | 
| │ ├─⊖ Foreground Scale | [1] (0 ~ 2) | 
| │ └─☐ Auto BPM | [OFF] | Use real-time automatically detected BPM instead of the set BPM.
| └─≡ Presets | **Projector Screen** | Blank, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glass, Preset 1,  |
| ☐ **Custom Hole** | | 
| ├─☐ Enable | [OFF] | Use custom hole.
| ├─⊖ Left | [-1] (Unlimited) | 
| ├─⊖ Right | [1] (Unlimited) | 
| ├─⊖ Front | [1] (Unlimited) | 
| ├─⊖ Back | [-1] (Unlimited) | 
| ├─⊖ Top | [1] (Unlimited) | 
| └─⊖ Bottom | [0] (Unlimited) | 
| ≡ Presets | **Projector Screen** | Sky Map, Black Gloss, Stage, Pool, Ocean, Audio Visualizer, Projector Screen, LED Box, Preset 1,  |
