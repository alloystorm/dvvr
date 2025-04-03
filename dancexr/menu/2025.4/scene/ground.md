---
locale: en-rUS
layout: single
title: Ground
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/ground) | [繁中](/tw/dancexr/menu/2025.4/scene/ground) | [日本語](/jp/dancexr/menu/2025.4/scene/ground) | [한국어](/kr/dancexr/menu/2025.4/scene/ground) | [简中](/zh/dancexr/menu/2025.4/scene/ground)

[Environment](../menu#Environment) > Ground



| Setting | Value | Description |
| :--- | --- | :--- |
| Ground Height | [0] (-2 ~ 2) | 0/22/True
| Ground | OFF | 1/22/True
| Radius | [200] (2 ~ 100) | Size of the ground mesh.2/22/True
| Hide If Stage Present | ON | Hide ground when there are stage models.3/22/True
| **Surface** | | 4/22/True
| ├ Texture: [Tiles] || 0/13/True
| │ Texture | **[Tiles]** | [Sky Map], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| ├ **Tiling** | | 1/13/True
| │ ├ Tiling X | [1] (0.1 ~ 10) | 0/7/False
| │ ├ Tiling Y | [1] (0.1 ~ 10) | 1/7/False
| │ ├ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 2/7/False
| │ ├ Offset X | [0] (0 ~ 1) | 3/7/False
| │ ├ Offset Y | [0] (0 ~ 1) | 4/7/False
| │ ├ Rotation | [0] (0 ~ 360) | 5/7/False
| │ ├ Variation | [0.5] (0 ~ 1) | 6/7/False
| │ └ Fit Texture | OFF | 7/7/False
| ├ Gloss | [0.95] (0 ~ 1) | 2/13/True
| ├ Metallic | [0] (0 ~ 1) | 3/13/True
| ├ Bump | [0.2] (0 ~ 1) | 4/13/True
| ├ Glow | [0] (0 ~ 10) | 5/13/True
| ├ Ambient | [1] (0 ~ 1) | 6/13/True
| ├ Alpha | [1] (0 ~ 1) | 7/13/True
| ├ Clip | [0] (0 ~ 1) | 8/13/True
| ├ **Color** | | 9/13/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Blend Mode: Blend || 7/8/True
| │ │ Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├ Blend | [1] (0 ~ 1) | 8/8/True
| │ └ Presets | **Black** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├ **Toon Shader** | | 10/13/True
| │ ├ Enable Toon Shader | OFF | 0/10/True
| │ ├ Shading | [1] (0 ~ 1) | 1/10/True
| │ ├ Outline | [0.5] (0 ~ 1) | 2/10/True
| │ ├ Specular | [0.25] (0 ~ 1) | 3/10/True
| │ ├ Soft Specular | [0.1] (0 ~ 1) | 4/10/True
| │ ├ Highlight Area | [0.25] (0 ~ 1) | 5/10/True
| │ ├ Soft Highlight | [0.1] (0 ~ 1) | 6/10/True
| │ ├ Ambient | [0.75] (0 ~ 1) | 7/10/True
| │ ├ Shadow Area | [0.65] (0 ~ 1) | 8/10/True
| │ ├ Shadow | [0.75] (0 ~ 1) | 9/10/True
| │ ├ Soft Shadow | [0.1] (0 ~ 1) | 10/10/True
| │ └ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├ **Special Shader** | | 11/13/True
| │ ├ Mode: Off || 0/2/False
| │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| ├ Viewer Height | [1.5] (0.5 ~ 3) | Viewer height used when projecting the the texture on to the ground12/13/True
| ├ **LED Mode** | | 13/13/True
| │ ├ Enable LED Mode | OFF | 0/6/False
| │ ├ Density | [7] (4 ~ 10) | 1/6/False
| │ ├ Size | [0.8] (0 ~ 1) | 2/6/False
| │ ├ Soft Edge | [0.3] (0 ~ 1) | 3/6/False
| │ ├ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect4/6/False
| │ ├ Edge | [0.5] (0 ~ 1) | 5/6/False
| │ └ Reduce Moire | [0.1] (0 ~ 1) | 6/6/False
| └ Presets | **Black Gloss** | Sky Map, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Glow, Glass,  |
| **Shadow Only** | | 5/22/True
| ├ Shadow Color || 0/9/False
| ├ Presets: Black || 1/9/False
| │ Presets | **Black** | White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange, Preset 1,  |
| ├ Color Mode | RGB | RGB, HSV, 2/9/False
| ├ Hue | [0] (0 ~ 1) | 3/9/False
| ├ Satuation | [0] (0 ~ 1) | 4/9/False
| ├ Brightness | [0] (0 ~ 1) | 5/9/False
| ├ Red | [0] (0 ~ 1) | 6/9/False
| ├ Green | [0] (0 ~ 1) | 7/9/False
| ├ Blue | [0] (0 ~ 1) | 8/9/False
| └ Transparency | [0.5] (0 ~ 1) | 9/9/False
| Stage / Pool | OFF | 6/22/True
| Presets: Off || 7/22/True
| Presets | **Off** | Off, Runway, Pool, Room, Background Board, Projector Screen, LED Screen,  |
| Lift | [0.5] (-2 ~ 2) | Lift the stage up / down.8/22/True
| Front / Back Offset | [0] (-10 ~ 10) | 9/22/True
| **Shape** | | 10/22/True
| ├ Center Width | [8] (0 ~ 10) | Width of the center area.0/9/False
| ├ Center Depth | [5] (0 ~ 9) | Depth of the center area.1/9/False
| ├ Back Height | [0] (0 ~ 9) | Height of the background board.2/9/False
| ├ Side Extension | [0] (0 ~ 5) | Extension at left and right.3/9/False
| ├ Front Extension | [0] (0 ~ 10) | Extension at front.4/9/False
| ├ Back Extension | [0] (0 ~ 10) | Extension at back.5/9/False
| ├ Wall Height | [0.05] (0 ~ 5) | Height of the edge above ground.6/9/False
| ├ Wall Thickness | [0.1] (0 ~ 1) | Size of the edge.7/9/False
| ├ Window | [0] (0 ~ 1) | 8/9/False
| └ Floating | OFF | 9/9/False
| **Surface** | | 11/22/True
| ├ Texture: [Wood1] || 0/12/True
| │ Texture | **[Wood1]** | [Blank], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| ├ **Tiling** | | 1/12/True
| │ ├ Tiling X | [1] (0.1 ~ 10) | 0/7/False
| │ ├ Tiling Y | [1] (0.1 ~ 10) | 1/7/False
| │ ├ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 2/7/False
| │ ├ Offset X | [0] (0 ~ 1) | 3/7/False
| │ ├ Offset Y | [0] (0 ~ 1) | 4/7/False
| │ ├ Rotation | [0] (0 ~ 360) | 5/7/False
| │ ├ Variation | [0.5] (0 ~ 1) | 6/7/False
| │ └ Fit Texture | OFF | 7/7/False
| ├ Gloss | [0.95] (0 ~ 1) | 2/12/True
| ├ Metallic | [0] (0 ~ 1) | 3/12/True
| ├ Bump | [0.2] (0 ~ 1) | 4/12/True
| ├ Glow | [0] (0 ~ 10) | 5/12/True
| ├ Ambient | [1] (0 ~ 1) | 6/12/True
| ├ Alpha | [1] (0 ~ 1) | 7/12/True
| ├ Clip | [0] (0 ~ 1) | 8/12/True
| ├ **Color** | | 9/12/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Blend Mode: Blend || 7/8/True
| │ │ Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├ Blend | [1] (0 ~ 1) | 8/8/True
| │ └ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├ **Toon Shader** | | 10/12/True
| │ ├ Enable Toon Shader | OFF | 0/10/True
| │ ├ Shading | [1] (0 ~ 1) | 1/10/True
| │ ├ Outline | [0.5] (0 ~ 1) | 2/10/True
| │ ├ Specular | [0.25] (0 ~ 1) | 3/10/True
| │ ├ Soft Specular | [0.1] (0 ~ 1) | 4/10/True
| │ ├ Highlight Area | [0.25] (0 ~ 1) | 5/10/True
| │ ├ Soft Highlight | [0.1] (0 ~ 1) | 6/10/True
| │ ├ Ambient | [0.75] (0 ~ 1) | 7/10/True
| │ ├ Shadow Area | [0.65] (0 ~ 1) | 8/10/True
| │ ├ Shadow | [0.75] (0 ~ 1) | 9/10/True
| │ ├ Soft Shadow | [0.1] (0 ~ 1) | 10/10/True
| │ └ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├ **Special Shader** | | 11/12/True
| │ ├ Mode: Off || 0/2/False
| │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| ├ **LED Mode** | | 12/12/True
| │ ├ Enable LED Mode | OFF | 0/6/False
| │ ├ Density | [7] (4 ~ 10) | 1/6/False
| │ ├ Size | [0.8] (0 ~ 1) | 2/6/False
| │ ├ Soft Edge | [0.3] (0 ~ 1) | 3/6/False
| │ ├ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect4/6/False
| │ ├ Edge | [0.5] (0 ~ 1) | 5/6/False
| │ └ Reduce Moire | [0.1] (0 ~ 1) | 6/6/False
| └ Presets | **Wood** | Blank, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Glow, Glass,  |
| **Back Surface** | | 12/22/True
| ├ Texture: [Blank] || 0/12/True
| │ Texture | **[Blank]** | [Blank], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| ├ **Tiling** | | 1/12/True
| │ ├ Tiling X | [1] (0.1 ~ 10) | 0/7/False
| │ ├ Tiling Y | [1] (0.1 ~ 10) | 1/7/False
| │ ├ Wrap Mode | Repeat | Repeat, Mirror U, Mirror V, Mirror Both, 2/7/False
| │ ├ Offset X | [0] (0 ~ 1) | 3/7/False
| │ ├ Offset Y | [0] (0 ~ 1) | 4/7/False
| │ ├ Rotation | [0] (0 ~ 360) | 5/7/False
| │ ├ Variation | [0.5] (0 ~ 1) | 6/7/False
| │ └ Fit Texture | ON | 7/7/False
| ├ Gloss | [0.95] (0 ~ 1) | 2/12/True
| ├ Metallic | [0] (0 ~ 1) | 3/12/True
| ├ Bump | [0.2] (0 ~ 1) | 4/12/True
| ├ Glow | [0] (0 ~ 10) | 5/12/True
| ├ Ambient | [1] (0 ~ 1) | 6/12/True
| ├ Alpha | [1] (0 ~ 1) | 7/12/True
| ├ Clip | [0] (0 ~ 1) | 8/12/True
| ├ **Color** | | 9/12/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Blend Mode: Original || 7/8/True
| │ │ Blend Mode | **Original** | Original, Multiply, Blend, Color Shift,  |
| │ ├ Blend | [1] (0 ~ 1) | 8/8/True
| │ └ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├ **Toon Shader** | | 10/12/True
| │ ├ Enable Toon Shader | OFF | 0/10/True
| │ ├ Shading | [1] (0 ~ 1) | 1/10/True
| │ ├ Outline | [0.5] (0 ~ 1) | 2/10/True
| │ ├ Specular | [0.25] (0 ~ 1) | 3/10/True
| │ ├ Soft Specular | [0.1] (0 ~ 1) | 4/10/True
| │ ├ Highlight Area | [0.25] (0 ~ 1) | 5/10/True
| │ ├ Soft Highlight | [0.1] (0 ~ 1) | 6/10/True
| │ ├ Ambient | [0.75] (0 ~ 1) | 7/10/True
| │ ├ Shadow Area | [0.65] (0 ~ 1) | 8/10/True
| │ ├ Shadow | [0.75] (0 ~ 1) | 9/10/True
| │ ├ Soft Shadow | [0.1] (0 ~ 1) | 10/10/True
| │ └ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├ **Special Shader** | | 11/12/True
| │ ├ Mode: Off || 0/2/False
| │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| ├ **LED Mode** | | 12/12/True
| │ ├ Enable LED Mode | OFF | 0/6/False
| │ ├ Density | [7] (4 ~ 10) | 1/6/False
| │ ├ Size | [0.8] (0 ~ 1) | 2/6/False
| │ ├ Soft Edge | [0.3] (0 ~ 1) | 3/6/False
| │ ├ Viewing Angle | [1] (0 ~ 8) | Reduce brightness when viewed from an angle. 0 = perfect4/6/False
| │ ├ Edge | [0.5] (0 ~ 1) | 5/6/False
| │ └ Reduce Moire | [0.1] (0 ~ 1) | 6/6/False
| └ Presets | **Blank** | Blank, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Glow, Glass,  |
| Water System | OFF | 13/22/True
| Presets: Off || 14/22/True
| Presets | **Off** | Off, Pool, Still Water, Ocean,  |
| Type | Pool | Pool, River, Ocean, 15/22/True
| Height | [-0.1] (-2 ~ 2) | Height of water level.16/22/True
| Ripples | [3] (0 ~ 10) | Intensity of small wave17/22/True
| Large Wave | [30] (0 ~ 100) | Intensity of large wave18/22/True
| Refraction Max Distance | [0.35] (0 ~ 3.5) | Controls the maximum distance in meters used to clamp the under water refraction depth. Higher value increases the distortion amount.19/22/True
| Absorption Distance | [5] (1 ~ 10) | Max distance you can see in the water from above.20/22/True
| Caustics | [0.5] (0 ~ 1) | Caustics effect21/22/True
| Absorption Multiplier | [2] (0 ~ 5) | Multiplication applied to the Absorption Distance when viewing from below.22/22/True
| Presets | **Black Gloss** | Sky Map, Black Gloss, Stage, Pool, Ocean, Background Board, Projector Screen, Emissive Screen, Preset 1,  |
