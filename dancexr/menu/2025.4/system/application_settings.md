---
locale: en-rUS
layout: single
title: Application Settings
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/system/application_settings) | [繁中](/tw/dancexr/menu/2025.4/system/application_settings) | [日本語](/jp/dancexr/menu/2025.4/system/application_settings) | [한국어](/kr/dancexr/menu/2025.4/system/application_settings) | [简中](/zh/dancexr/menu/2025.4/system/application_settings)

[System](../menu#System) > Application Settings



| Setting | Value | Description |
| :--- | --- | :--- |
| Load Previous Scene | OFF | Automatically load the last scene on start0/7/False
| Block desktop window in VR | ON | Blocks desktop window in VR mode1/7/False
| Recover Tags From Save | OFF | Attempts to recover tags from saved settings in case your content cache is rebuilt or broken2/7/False
| Flip DDS Compressed | ON | Flip compressed DDS texture3/7/False
| Flip DDS Uncompressed | OFF | Flip uncomrpessed DDS texture4/7/False
| **VR Hands** | | 5/7/False
| ├ Hand Visible | ON | 0/7/False
| ├ Cast Shadow | OFF | 1/7/False
| ├ Time And FPS | ON | 2/7/False
| ├ **Hand Orientation** | | 3/7/False
| │ ├ Offset || 0/5/False
| │ ├ X | [0] (-0.1 ~ 0.1) | 1/5/False
| │ ├ Y | [0] (-0.1 ~ 0.1) | 2/5/False
| │ ├ Z | [0] (-0.1 ~ 0.1) | 3/5/False
| │ ├ Rotation | [45] (-90 ~ 90) | 4/5/False
| │ └ Update Pointer || 5/5/False
| ├ Left Hand Pose: Auto || 4/7/False
| │ Left Hand Pose | **Auto** | Auto, Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├ **Left Hand Accessory** | | 5/7/False
| │ ├ Enable Left Hand Accessory | OFF | 0/24/False
| │ ├ Model: [Pole] || 1/24/False
| │ │ Model | **[Pole]** | [Pole],  |
| │ ├ **Anchor Offset** | | Set the anchor position for the attachment to attach to2/24/False
| │ │ ├ Position || 0/7/False
| │ │ ├ X | [0] (-1 ~ 1) | 1/7/False
| │ │ ├ Y | [0] (-1 ~ 1) | 2/7/False
| │ │ ├ Z | [0] (-1 ~ 1) | 3/7/False
| │ │ ├ Rotation || 4/7/False
| │ │ ├ X | [0] (-90 ~ 90) | 5/7/False
| │ │ ├ Y | [0] (-90 ~ 90) | 6/7/False
| │ │ └ Z | [0] (-90 ~ 90) | 7/7/False
| │ ├ Size & Alignment || 3/24/False
| │ ├ Object Radius | [0.02] (0.01 ~ 0.05) | 4/24/False
| │ ├ Object Length | [0.2] (0 ~ 5) | 5/24/False
| │ ├ Scale | [0] (-5 ~ 5) | 6/24/False
| │ ├ Orientation | Y Up | Y Up, Y Down, X Up, X Down, Z Up, Z Down, 7/24/False
| │ ├ Offset || 8/24/False
| │ ├ X | [0] (-2 ~ 2) | 9/24/False
| │ ├ Y | [0] (-2 ~ 2) | 10/24/False
| │ ├ Z | [0] (-2 ~ 2) | 11/24/False
| │ ├ Rotation || 12/24/False
| │ ├ X | [0] (-180 ~ 180) | 13/24/False
| │ ├ Y | [0] (-180 ~ 180) | 14/24/False
| │ ├ Z | [0] (-180 ~ 180) | 15/24/False
| │ ├ Guitar Mode | OFF | 16/24/False
| │ ├ **Motion** | | Apply up / down motion to the attachment model17/24/False
| │ │ ├ Enable Motion | OFF | 0/3/False
| │ │ ├ **Speed** | | 1/3/False
| │ │ │ ├ Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 0/7/False
| │ │ │ ├ Moves Per Group | [8] (4 ~ 32) | 1/7/False
| │ │ │ ├ Phase | [0] (0 ~ 1) | 2/7/False
| │ │ │ ├ Curve | [0] (0 ~ 1) | 3/7/False
| │ │ │ ├ Variable Speed | OFF | 4/7/False
| │ │ │ ├ Mode | Gradual | Gradual, Random, Volume, 5/7/False
| │ │ │ ├ Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 6/7/False
| │ │ │ └ Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 7/7/False
| │ │ ├ Distance | [0.1] (0 ~ 0.3) | 2/3/False
| │ │ └ Angle | [0] (-60 ~ 60) | 3/3/False
| │ ├ Animation: None || Select loaded motion to use for the attachment model18/24/False
| │ │ Animation | **None** | None, <br/>Select loaded motion to use for the attachment model |
| │ ├ **Surface** | | 19/24/False
| │ │ ├ Gloss | [0.9] (0 ~ 1) | 0/9/True
| │ │ ├ Metallic | [1] (0 ~ 1) | 1/9/True
| │ │ ├ Bump | [0.2] (0 ~ 1) | 2/9/True
| │ │ ├ Glow | [0] (0 ~ 10) | 3/9/True
| │ │ ├ Ambient | [1] (0 ~ 1) | 4/9/True
| │ │ ├ Alpha | [1] (0 ~ 1) | 5/9/True
| │ │ ├ Clip | [0] (0 ~ 1) | 6/9/True
| │ │ ├ **Color** | | 7/9/True
| │ │ │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ │ │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ │ │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ │ │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ │ │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ │ │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ │ │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ │ │ ├ Blend Mode: Blend || 7/8/True
| │ │ │ │ Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ │ │ ├ Blend | [1] (0 ~ 1) | 8/8/True
| │ │ │ └ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| │ │ ├ **Toon Shader** | | 8/9/True
| │ │ │ ├ Enable Toon Shader | OFF | 0/10/True
| │ │ │ ├ Shading | [1] (0 ~ 1) | 1/10/True
| │ │ │ ├ Outline | [0.5] (0 ~ 1) | 2/10/True
| │ │ │ ├ Specular | [0.25] (0 ~ 1) | 3/10/True
| │ │ │ ├ Soft Specular | [0.1] (0 ~ 1) | 4/10/True
| │ │ │ ├ Highlight Area | [0.25] (0 ~ 1) | 5/10/True
| │ │ │ ├ Soft Highlight | [0.1] (0 ~ 1) | 6/10/True
| │ │ │ ├ Ambient | [0.75] (0 ~ 1) | 7/10/True
| │ │ │ ├ Shadow Area | [0.65] (0 ~ 1) | 8/10/True
| │ │ │ ├ Shadow | [0.75] (0 ~ 1) | 9/10/True
| │ │ │ ├ Soft Shadow | [0.1] (0 ~ 1) | 10/10/True
| │ │ │ └ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| │ │ ├ **Special Shader** | | 9/9/True
| │ │ │ ├ Mode: Off || 0/2/False
| │ │ │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ │ │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ │ │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| │ │ └ Presets | **Chrome** | White Gloss, Red Gloss, Chrome, Black Gloss, Gold, Solid Glass, Thin Glass,  |
| │ ├ XRay | [0] (0 ~ 1) | 20/24/False
| │ ├ Alpha | [1] (0 ~ 1) | 21/24/False
| │ ├ Pull Hands | [0.1] (0 ~ 0.5) | Pulling hands towards the attachment when they are close enough22/24/False
| │ ├ Grab Pose | ON | Automatically change hand pose to grab when they are on the attachment23/24/False
| │ └ Hand Motion | [0] (-1 ~ 1) | Move hands relative to the attachment motion24/24/False
| ├ Right Hand Pose: Auto || 6/7/False
| │ Right Hand Pose | **Auto** | Auto, Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| └ **Right Hand Accessory** | | 7/7/False
|   ├ Enable Right Hand Accessory | OFF | 0/24/False
|   ├ Model: [Pole] || 1/24/False
|   │ Model | **[Pole]** | [Pole],  |
|   ├ **Anchor Offset** | | Set the anchor position for the attachment to attach to2/24/False
|   │ ├ Position || 0/7/False
|   │ ├ X | [0] (-1 ~ 1) | 1/7/False
|   │ ├ Y | [0] (-1 ~ 1) | 2/7/False
|   │ ├ Z | [0] (-1 ~ 1) | 3/7/False
|   │ ├ Rotation || 4/7/False
|   │ ├ X | [0] (-90 ~ 90) | 5/7/False
|   │ ├ Y | [0] (-90 ~ 90) | 6/7/False
|   │ └ Z | [0] (-90 ~ 90) | 7/7/False
|   ├ Size & Alignment || 3/24/False
|   ├ Object Radius | [0.02] (0.01 ~ 0.05) | 4/24/False
|   ├ Object Length | [0.2] (0 ~ 5) | 5/24/False
|   ├ Scale | [0] (-5 ~ 5) | 6/24/False
|   ├ Orientation | Y Up | Y Up, Y Down, X Up, X Down, Z Up, Z Down, 7/24/False
|   ├ Offset || 8/24/False
|   ├ X | [0] (-2 ~ 2) | 9/24/False
|   ├ Y | [0] (-2 ~ 2) | 10/24/False
|   ├ Z | [0] (-2 ~ 2) | 11/24/False
|   ├ Rotation || 12/24/False
|   ├ X | [0] (-180 ~ 180) | 13/24/False
|   ├ Y | [0] (-180 ~ 180) | 14/24/False
|   ├ Z | [0] (-180 ~ 180) | 15/24/False
|   ├ Guitar Mode | OFF | 16/24/False
|   ├ **Motion** | | Apply up / down motion to the attachment model17/24/False
|   │ ├ Enable Motion | OFF | 0/3/False
|   │ ├ **Speed** | | 1/3/False
|   │ │ ├ Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 0/7/False
|   │ │ ├ Moves Per Group | [8] (4 ~ 32) | 1/7/False
|   │ │ ├ Phase | [0] (0 ~ 1) | 2/7/False
|   │ │ ├ Curve | [0] (0 ~ 1) | 3/7/False
|   │ │ ├ Variable Speed | OFF | 4/7/False
|   │ │ ├ Mode | Gradual | Gradual, Random, Volume, 5/7/False
|   │ │ ├ Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 6/7/False
|   │ │ └ Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 7/7/False
|   │ ├ Distance | [0.1] (0 ~ 0.3) | 2/3/False
|   │ └ Angle | [0] (-60 ~ 60) | 3/3/False
|   ├ Animation: None || Select loaded motion to use for the attachment model18/24/False
|   │ Animation | **None** | None, <br/>Select loaded motion to use for the attachment model |
|   ├ **Surface** | | 19/24/False
|   │ ├ Gloss | [0.9] (0 ~ 1) | 0/9/True
|   │ ├ Metallic | [1] (0 ~ 1) | 1/9/True
|   │ ├ Bump | [0.2] (0 ~ 1) | 2/9/True
|   │ ├ Glow | [0] (0 ~ 10) | 3/9/True
|   │ ├ Ambient | [1] (0 ~ 1) | 4/9/True
|   │ ├ Alpha | [1] (0 ~ 1) | 5/9/True
|   │ ├ Clip | [0] (0 ~ 1) | 6/9/True
|   │ ├ **Color** | | 7/9/True
|   │ │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
|   │ │ ├ Hue | [0] (0 ~ 1) | 1/8/True
|   │ │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
|   │ │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
|   │ │ ├ Red | [1] (0 ~ 1) | 4/8/True
|   │ │ ├ Green | [1] (0 ~ 1) | 5/8/True
|   │ │ ├ Blue | [1] (0 ~ 1) | 6/8/True
|   │ │ ├ Blend Mode: Blend || 7/8/True
|   │ │ │ Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
|   │ │ ├ Blend | [1] (0 ~ 1) | 8/8/True
|   │ │ └ Presets | **White** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|   │ ├ **Toon Shader** | | 8/9/True
|   │ │ ├ Enable Toon Shader | OFF | 0/10/True
|   │ │ ├ Shading | [1] (0 ~ 1) | 1/10/True
|   │ │ ├ Outline | [0.5] (0 ~ 1) | 2/10/True
|   │ │ ├ Specular | [0.25] (0 ~ 1) | 3/10/True
|   │ │ ├ Soft Specular | [0.1] (0 ~ 1) | 4/10/True
|   │ │ ├ Highlight Area | [0.25] (0 ~ 1) | 5/10/True
|   │ │ ├ Soft Highlight | [0.1] (0 ~ 1) | 6/10/True
|   │ │ ├ Ambient | [0.75] (0 ~ 1) | 7/10/True
|   │ │ ├ Shadow Area | [0.65] (0 ~ 1) | 8/10/True
|   │ │ ├ Shadow | [0.75] (0 ~ 1) | 9/10/True
|   │ │ ├ Soft Shadow | [0.1] (0 ~ 1) | 10/10/True
|   │ │ └ Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|   │ ├ **Special Shader** | | 9/9/True
|   │ │ ├ Mode: Off || 0/2/False
|   │ │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|   │ │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
|   │ │ └ Thickness | [1] (0 ~ 1) | 2/2/False
|   │ └ Presets | **Chrome** | White Gloss, Red Gloss, Chrome, Black Gloss, Gold, Solid Glass, Thin Glass,  |
|   ├ XRay | [0] (0 ~ 1) | 20/24/False
|   ├ Alpha | [1] (0 ~ 1) | 21/24/False
|   ├ Pull Hands | [0.1] (0 ~ 0.5) | Pulling hands towards the attachment when they are close enough22/24/False
|   ├ Grab Pose | ON | Automatically change hand pose to grab when they are on the attachment23/24/False
|   └ Hand Motion | [0] (-1 ~ 1) | Move hands relative to the attachment motion24/24/False
| Gizmo 3rd Axis: Rotation || 6/7/False
| Gizmo 3rd Axis | **Rotation** | Rotation, Depth,  |
| Use Translated Names | ON | 7/7/False
