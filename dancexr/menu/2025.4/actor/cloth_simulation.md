---
locale: en-rUS
layout: single
title: Simulation
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[Pro](../menu#Pro) > Simulation



| Setting | Value | Description |
| :--- | --- | :--- |
| Enable Simulation | ON | 0/10/True
| Reset || 1/10/True
| **Cloth 1** | | 2/10/True
| ├ Enable Cloth 1 | OFF | 0/17/True
| ├ Rebuild Mesh || Most parameters here requires rebuilding the mesh to take effect.1/17/True
| ├ Topology: Horizontal Layout || 2/17/True
| │ Topology | **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├ String Connection | [4] (1 ~ 10) | 3/17/True
| ├ Inner Radius | [0.08] (0 ~ 0.2) | Radius of inner circle in meters4/17/True
| ├ Slope | [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.5/17/True
| ├ Arc | [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape6/17/True
| ├ Length | [0.25] (0 ~ 0.75) | Length in meters7/17/True
| ├ Arm Holes | [0.5] (0 ~ 1) | Size of arm holes in relation to circumference8/17/True
| ├ Arm Hole Height | [0.25] (0 ~ 1) | Height of arm holes in relation to total length9/17/True
| ├ Back Length | [1] (0.1 ~ 1.9) | 10/17/True
| ├ Side Length | [1] (0.1 ~ 1.9) | 11/17/True
| ├ Horizontal Resolution | [0.01] (0.005 ~ 0.025) | 12/17/True
| ├ Vertical Resolution | [0.01] (0.005 ~ 0.025) | 13/17/True
| ├ Distance Compliance | [0] (0 ~ 0.1) | Compliance of distance constraints between particles14/17/True
| ├ UV Mapping: Mirror Scaled || 15/17/True
| │ UV Mapping | **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├ **Anchor** | | 16/17/True
| │ ├ Top Layers | [2] (0 ~ 10) | 0/3/False
| │ ├ **Top Anchor** | | 1/3/False
| │ │ ├ Anchor Selection | [1] (0 ~ 1) | 0/11/False
| │ │ ├ Selection Offset | [0.5] (0 ~ 1) | 1/11/False
| │ │ ├ Anchor Bone: Torso || 2/11/False
| │ │ │ Anchor Bone | **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├ Lock Mode: None || 3/11/False
| │ │ │ Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├ Anchor Positoin || 4/11/False
| │ │ ├ X | [0] (-0.5 ~ 0.5) | 5/11/False
| │ │ ├ Y | [0.2] (-0.5 ~ 0.5) | 6/11/False
| │ │ ├ Z | [0] (-0.5 ~ 0.5) | 7/11/False
| │ │ ├ Anchor Rotation || 8/11/False
| │ │ ├ X | [0] (-1 ~ 1) | 9/11/False
| │ │ ├ Y | [0] (-1 ~ 1) | 10/11/False
| │ │ └ Z | [0] (-1 ~ 1) | 11/11/False
| │ ├ Bottom Layers | [0] (0 ~ 10) | 2/3/False
| │ └ **Bottom Anchor** | | 3/3/False
| │   ├ Anchor Selection | [1] (0 ~ 1) | 0/12/False
| │   ├ Selection Offset | [0.5] (0 ~ 1) | 1/12/False
| │   ├ Anchor Bone: Waist || 2/12/False
| │   │ Anchor Bone | **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │   ├ Swap Side | OFF | 3/12/False
| │   ├ Lock Mode: None || 4/12/False
| │   │ Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │   ├ Anchor Positoin || 5/12/False
| │   ├ X | [0] (-0.5 ~ 0.5) | 6/12/False
| │   ├ Y | [0] (-0.5 ~ 0.5) | 7/12/False
| │   ├ Z | [0] (-0.5 ~ 0.5) | 8/12/False
| │   ├ Anchor Rotation || 9/12/False
| │   ├ X | [0] (-1 ~ 1) | 10/12/False
| │   ├ Y | [0] (-1 ~ 1) | 11/12/False
| │   └ Z | [0] (-1 ~ 1) | 12/12/False
| ├ **Particle Properties** | | 17/17/True
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters0/21/False
| │ ├ Stickiness | [0] (0 ~ 1) | 1/21/False
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 2/21/False
| │ ├ Friction | [1] (0 ~ 2) | 3/21/False
| │ ├ Ground Friction | [1] (-2 ~ 2) | 4/21/False
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy5/21/False
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy6/21/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 7/21/False
| │ ├ **Wind** | | 8/21/False
| │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ ├ **Collide With** | | 9/21/False
| │ │ ├ Head | ON | 0/8/False
| │ │ ├ Body | ON | 1/8/False
| │ │ ├ Boobs | ON | 2/8/False
| │ │ ├ Butts | ON | 3/8/False
| │ │ ├ Arms | ON | 4/8/False
| │ │ ├ Hands | ON | 5/8/False
| │ │ ├ Legs | ON | 6/8/False
| │ │ ├ Feet | ON | 7/8/False
| │ │ └ Player | ON | 8/8/False
| │ ├ Enable Bending Constraints | ON | 10/21/False
| │ ├ Bending Compliance | [0] (0 ~ 1) | 11/21/False
| │ ├ Scale | [1] (0 ~ 2) | 12/21/False
| │ ├ Self Collision | OFF | 13/21/False
| │ ├ Grip Mass | [2] (0 ~ 4) | Mass of grip particles14/21/False
| │ ├ Grip Friction | [2] (-2 ~ 4) | Friction for grip particles15/21/False
| │ ├ Grip Stickiness | [0.25] (0 ~ 1) | Stickiness of grip particles16/21/False
| │ ├ Grip Drag | [0] (-2 ~ 2) | Air resistancy for grip particles17/21/False
| │ ├ Grip Scale | [1] (0 ~ 2) | 18/21/False
| │ ├ Enable Tearing | OFF | 19/21/False
| │ ├ Tear Threshold | [2] (1 ~ 10) | 20/21/False
| │ └ Limit Tearing Speed | [0] (0 ~ 25) | Cool down interval after tearing, in frames21/21/False
| └ Presets | **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| **C1 Material** | | 3/10/True
| ├ Surface || 0/19/False
| ├ Presets: Matt Gray || 1/19/False
| │ Presets | **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├ Glass Mode | OFF | 2/19/False
| ├ Alpha As Gloss | OFF | 3/19/False
| ├ Double Side | OFF | 4/19/False
| ├ Dim Back | [1] (0 ~ 1) | 5/19/False
| ├ Cast Shadow | [0.5] (0 ~ 1) | 6/19/False
| ├ Depth Prepass | [0.8] (0 ~ 1) | 7/19/False
| ├ Gloss | [0.3] (0 ~ 1) | 8/19/False
| ├ Metallic | [0] (0 ~ 1) | 9/19/False
| ├ Bump | [0.2] (0 ~ 1) | 10/19/False
| ├ Glow | [0] (0 ~ 10) | 11/19/False
| ├ Ambient | [1] (0 ~ 1) | 12/19/False
| ├ Alpha | [1] (0 ~ 1) | 13/19/False
| ├ Clip | [0] (0 ~ 1) | 14/19/False
| ├ **Color** | | 15/19/False
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
| │ └ Presets | **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├ **Toon Shader** | | 16/19/False
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
| ├ **Special Shader** | | 17/19/False
| │ ├ Mode: Off || 0/2/False
| │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| ├ Texture: [Solid Color] || 18/19/False
| │ Texture | **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └ **Detail Map** | | 19/19/False
|   ├ Enable Detail Map | ON | 0/11/False
|   ├ **Hexagon Map** | | 1/11/False
|   │ ├ Enable Hexagon Map | OFF | 0/6/False
|   │ ├ Density | [2] (0 ~ 8) | 1/6/False
|   │ ├ Size | [1] (0 ~ 1) | 2/6/False
|   │ ├ Bump | [0.5] (-1 ~ 1) | 3/6/False
|   │ ├ Noise | [0.2] (0 ~ 1) | 4/6/False
|   │ ├ Use Circle | OFF | 5/6/False
|   │ └ Soft Edge | [0.1] (0 ~ 1) | 6/6/False
|   ├ Select Map: Fabric 3 || 2/11/False
|   │ Select Map | **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|   ├ Detail Map Rotation | [0] (-180 ~ 180) | 3/11/False
|   ├ Detail Map Scale | [6] (0 ~ 8) | 4/11/False
|   ├ Detail Map Bump | [0.5] (0 ~ 1) | 5/11/False
|   ├ Affect AO | [0] (0 ~ 1) | 6/11/False
|   ├ Affect Smoothness | [0] (0 ~ 1) | 7/11/False
|   ├ Affect Metallic | [0] (0 ~ 1) | 8/11/False
|   ├ Affect Color Blend | [0] (0 ~ 1) | 9/11/False
|   ├ Anisotropy | [0] (-1 ~ 1) | 10/11/False
|   └ MIP Map Bias | [0] (-5 ~ 5) | Adjust sharpness of detail texture.11/11/False
| **Cloth 2** | | 4/10/True
| ├ Enable Cloth 2 | OFF | 0/17/True
| ├ Rebuild Mesh || Most parameters here requires rebuilding the mesh to take effect.1/17/True
| ├ Topology: Horizontal Layout || 2/17/True
| │ Topology | **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├ String Connection | [4] (1 ~ 10) | 3/17/True
| ├ Inner Radius | [0.08] (0 ~ 0.2) | Radius of inner circle in meters4/17/True
| ├ Slope | [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.5/17/True
| ├ Arc | [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape6/17/True
| ├ Length | [0.25] (0 ~ 0.75) | Length in meters7/17/True
| ├ Arm Holes | [0.5] (0 ~ 1) | Size of arm holes in relation to circumference8/17/True
| ├ Arm Hole Height | [0.25] (0 ~ 1) | Height of arm holes in relation to total length9/17/True
| ├ Back Length | [1] (0.1 ~ 1.9) | 10/17/True
| ├ Side Length | [1] (0.1 ~ 1.9) | 11/17/True
| ├ Horizontal Resolution | [0.01] (0.005 ~ 0.025) | 12/17/True
| ├ Vertical Resolution | [0.01] (0.005 ~ 0.025) | 13/17/True
| ├ Distance Compliance | [0] (0 ~ 0.1) | Compliance of distance constraints between particles14/17/True
| ├ UV Mapping: Mirror Scaled || 15/17/True
| │ UV Mapping | **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├ **Anchor** | | 16/17/True
| │ ├ Top Layers | [2] (0 ~ 10) | 0/3/False
| │ ├ **Top Anchor** | | 1/3/False
| │ │ ├ Anchor Selection | [1] (0 ~ 1) | 0/11/False
| │ │ ├ Selection Offset | [0.5] (0 ~ 1) | 1/11/False
| │ │ ├ Anchor Bone: Torso || 2/11/False
| │ │ │ Anchor Bone | **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├ Lock Mode: None || 3/11/False
| │ │ │ Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├ Anchor Positoin || 4/11/False
| │ │ ├ X | [0] (-0.5 ~ 0.5) | 5/11/False
| │ │ ├ Y | [0.2] (-0.5 ~ 0.5) | 6/11/False
| │ │ ├ Z | [0] (-0.5 ~ 0.5) | 7/11/False
| │ │ ├ Anchor Rotation || 8/11/False
| │ │ ├ X | [0] (-1 ~ 1) | 9/11/False
| │ │ ├ Y | [0] (-1 ~ 1) | 10/11/False
| │ │ └ Z | [0] (-1 ~ 1) | 11/11/False
| │ ├ Bottom Layers | [0] (0 ~ 10) | 2/3/False
| │ └ **Bottom Anchor** | | 3/3/False
| │   ├ Anchor Selection | [1] (0 ~ 1) | 0/12/False
| │   ├ Selection Offset | [0.5] (0 ~ 1) | 1/12/False
| │   ├ Anchor Bone: Waist || 2/12/False
| │   │ Anchor Bone | **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │   ├ Swap Side | OFF | 3/12/False
| │   ├ Lock Mode: None || 4/12/False
| │   │ Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │   ├ Anchor Positoin || 5/12/False
| │   ├ X | [0] (-0.5 ~ 0.5) | 6/12/False
| │   ├ Y | [0] (-0.5 ~ 0.5) | 7/12/False
| │   ├ Z | [0] (-0.5 ~ 0.5) | 8/12/False
| │   ├ Anchor Rotation || 9/12/False
| │   ├ X | [0] (-1 ~ 1) | 10/12/False
| │   ├ Y | [0] (-1 ~ 1) | 11/12/False
| │   └ Z | [0] (-1 ~ 1) | 12/12/False
| ├ **Particle Properties** | | 17/17/True
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters0/21/False
| │ ├ Stickiness | [0] (0 ~ 1) | 1/21/False
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 2/21/False
| │ ├ Friction | [1] (0 ~ 2) | 3/21/False
| │ ├ Ground Friction | [1] (-2 ~ 2) | 4/21/False
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy5/21/False
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy6/21/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 7/21/False
| │ ├ **Wind** | | 8/21/False
| │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ ├ **Collide With** | | 9/21/False
| │ │ ├ Head | ON | 0/8/False
| │ │ ├ Body | ON | 1/8/False
| │ │ ├ Boobs | ON | 2/8/False
| │ │ ├ Butts | ON | 3/8/False
| │ │ ├ Arms | ON | 4/8/False
| │ │ ├ Hands | ON | 5/8/False
| │ │ ├ Legs | ON | 6/8/False
| │ │ ├ Feet | ON | 7/8/False
| │ │ └ Player | ON | 8/8/False
| │ ├ Enable Bending Constraints | ON | 10/21/False
| │ ├ Bending Compliance | [0] (0 ~ 1) | 11/21/False
| │ ├ Scale | [1] (0 ~ 2) | 12/21/False
| │ ├ Self Collision | OFF | 13/21/False
| │ ├ Grip Mass | [2] (0 ~ 4) | Mass of grip particles14/21/False
| │ ├ Grip Friction | [2] (-2 ~ 4) | Friction for grip particles15/21/False
| │ ├ Grip Stickiness | [0.25] (0 ~ 1) | Stickiness of grip particles16/21/False
| │ ├ Grip Drag | [0] (-2 ~ 2) | Air resistancy for grip particles17/21/False
| │ ├ Grip Scale | [1] (0 ~ 2) | 18/21/False
| │ ├ Enable Tearing | OFF | 19/21/False
| │ ├ Tear Threshold | [2] (1 ~ 10) | 20/21/False
| │ └ Limit Tearing Speed | [0] (0 ~ 25) | Cool down interval after tearing, in frames21/21/False
| └ Presets | **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| **C2 Material** | | 5/10/True
| ├ Surface || 0/19/False
| ├ Presets: Matt Gray || 1/19/False
| │ Presets | **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├ Glass Mode | OFF | 2/19/False
| ├ Alpha As Gloss | OFF | 3/19/False
| ├ Double Side | ON | 4/19/False
| ├ Dim Back | [1] (0 ~ 1) | 5/19/False
| ├ Cast Shadow | [0.5] (0 ~ 1) | 6/19/False
| ├ Depth Prepass | [0.8] (0 ~ 1) | 7/19/False
| ├ Gloss | [0.3] (0 ~ 1) | 8/19/False
| ├ Metallic | [0] (0 ~ 1) | 9/19/False
| ├ Bump | [0.2] (0 ~ 1) | 10/19/False
| ├ Glow | [0] (0 ~ 10) | 11/19/False
| ├ Ambient | [1] (0 ~ 1) | 12/19/False
| ├ Alpha | [1] (0 ~ 1) | 13/19/False
| ├ Clip | [0] (0 ~ 1) | 14/19/False
| ├ **Color** | | 15/19/False
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Blend Mode: Multiply || 7/8/True
| │ │ Blend Mode | **Multiply** | Original, Multiply, Blend, Color Shift,  |
| │ ├ Blend | [1] (0 ~ 1) | 8/8/True
| │ └ Presets | **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├ **Toon Shader** | | 16/19/False
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
| ├ **Special Shader** | | 17/19/False
| │ ├ Mode: Off || 0/2/False
| │ │ Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├ Refraction | [0.5] (1 ~ 3) | 1/2/False
| │ └ Thickness | [1] (0 ~ 1) | 2/2/False
| ├ Texture: [Solid Color] || 18/19/False
| │ Texture | **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └ **Detail Map** | | 19/19/False
|   ├ Enable Detail Map | ON | 0/11/False
|   ├ **Hexagon Map** | | 1/11/False
|   │ ├ Enable Hexagon Map | OFF | 0/6/False
|   │ ├ Density | [2] (0 ~ 8) | 1/6/False
|   │ ├ Size | [1] (0 ~ 1) | 2/6/False
|   │ ├ Bump | [0.5] (-1 ~ 1) | 3/6/False
|   │ ├ Noise | [0.2] (0 ~ 1) | 4/6/False
|   │ ├ Use Circle | OFF | 5/6/False
|   │ └ Soft Edge | [0.1] (0 ~ 1) | 6/6/False
|   ├ Select Map: Fabric 3 || 2/11/False
|   │ Select Map | **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|   ├ Detail Map Rotation | [0] (-180 ~ 180) | 3/11/False
|   ├ Detail Map Scale | [6] (0 ~ 8) | 4/11/False
|   ├ Detail Map Bump | [0.5] (0 ~ 1) | 5/11/False
|   ├ Affect AO | [0] (0 ~ 1) | 6/11/False
|   ├ Affect Smoothness | [0] (0 ~ 1) | 7/11/False
|   ├ Affect Metallic | [0] (0 ~ 1) | 8/11/False
|   ├ Affect Color Blend | [0] (0 ~ 1) | 9/11/False
|   ├ Anisotropy | [0] (-1 ~ 1) | 10/11/False
|   └ MIP Map Bias | [0] (-5 ~ 5) | Adjust sharpness of detail texture.11/11/False
| Combine | OFF | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.6/10/True
| **Fluid (Experimental)** | | 7/10/True
| ├ Enable Fluid (Experimental) | OFF | 0/4/True
| ├ **Spawn** | | 1/4/True
| │ ├ **Position** | | 0/10/True
| │ │ ├ X | [0] (Unlimited) | 0/2/False
| │ │ ├ Y | [2.5] (Unlimited) | 1/2/False
| │ │ └ Z | [0] (Unlimited) | 2/2/False
| │ ├ **Rotation** | | 1/10/True
| │ │ ├ X | [0] (-180 ~ 180) | 0/2/False
| │ │ ├ Y | [0] (-180 ~ 180) | 1/2/False
| │ │ └ Z | [0] (-180 ~ 180) | 2/2/False
| │ ├ Spawn Radius | [0.1] (0 ~ 1) | 2/10/True
| │ ├ Spread | [0.1] (0 ~ 1) | 3/10/True
| │ ├ Spawn Rate | [20] (0 ~ 20) | 4/10/True
| │ ├ Speed | [5] (0 ~ 10) | 5/10/True
| │ ├ Mouse / Hand Control | OFF | 6/10/True
| │ ├ Auto Aim | ON | 7/10/True
| │ ├ Max TTL | [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.8/10/True
| │ ├ TTL on Floor | [0.1] (0 ~ 1) | Time to live after hitting floor.9/10/True
| │ ├ Smoothing | [0.5] (0 ~ 1) | 10/10/True
| │ └ Presets | **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
| ├ **Fluid** | | 2/4/True
| │ ├ Cohesion | [0.5] (0 ~ 1) | 0/6/True
| │ ├ Viscosity | [0] (0 ~ 1) | 1/6/True
| │ ├ Stick To Surface | [0.1] (0 ~ 1) | 2/6/True
| │ ├ Target Density | [2] (1 ~ 10) | 3/6/True
| │ ├ Cohesion Range | [20] (1 ~ 50) | Max distance for cohesion effect4/6/True
| │ ├ Target Distance | [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.5/6/True
| │ ├ Elevation | [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size6/6/True
| │ └ Presets | **Water** | Water, Viscous, Sand,  |
| ├ **Render** | | 3/4/True
| │ ├ Render Particle | ON | 0/8/False
| │ ├ Render Droplet | OFF | 1/8/False
| │ ├ Droplet Size | [2] (0 ~ 50) | Droplet size in MM2/8/False
| │ ├ Scale By Density | [0] (0 ~ 5) | Scale droplet size by density of the fluid3/8/False
| │ ├ **Color** | | 4/8/False
| │ │ ├ Color Mode | RGB | RGB, HSV, 0/6/False
| │ │ ├ Hue | [0] (0 ~ 1) | 1/6/False
| │ │ ├ Satuation | [0] (0 ~ 1) | 2/6/False
| │ │ ├ Brightness | [1] (0 ~ 1) | 3/6/False
| │ │ ├ Red | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Green | [1] (0 ~ 1) | 5/6/False
| │ │ └ Blue | [1] (0 ~ 1) | 6/6/False
| │ ├ Metallic | [0] (0 ~ 1) | 5/8/False
| │ ├ Smoothness | [0.95] (0 ~ 1) | 6/8/False
| │ ├ Glow | [0] (0 ~ 1) | 7/8/False
| │ └ Transparency | [0.1] (0 ~ 1) | 8/8/False
| ├ **Particle Properties** | | 4/4/True
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 0/7/False
| │ ├ Friction | [0] (0 ~ 2) | 1/7/False
| │ ├ Ground Friction | [0] (-2 ~ 2) | 2/7/False
| │ ├ Drag (Air) | [-2] (0 ~ 2) | Air resistancy3/7/False
| │ ├ Drag (Underwater) | [-2] (0 ~ 2) | Underwater resistancy4/7/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 5/7/False
| │ ├ **Wind** | | 6/7/False
| │ │ ├ Wind Influence | [0] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ └ **Collide With** | | 7/7/False
| │   ├ Head | ON | 0/8/False
| │   ├ Body | ON | 1/8/False
| │   ├ Boobs | ON | 2/8/False
| │   ├ Butts | ON | 3/8/False
| │   ├ Arms | ON | 4/8/False
| │   ├ Hands | ON | 5/8/False
| │   ├ Legs | ON | 6/8/False
| │   ├ Feet | ON | 7/8/False
| │   └ Player | OFF | 8/8/False
| └ Presets | **Default (Reset)** | Default (Reset),  |
| **Geometry Collider** | | 8/10/True
| ├ Enable Geometry Collider | ON | 0/17/True
| ├ Visible | OFF | 1/17/True
| ├ Export Shape || 2/17/True
| ├ **Head** | | 3/17/True
| │ ├ Enable Head | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [-0.05] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.04] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.5] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.08] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.11] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [0.8] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Neck** | | 4/17/True
| │ ├ Enable Neck | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.045] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.065] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.045] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Chest** | | 5/17/True
| │ ├ Enable Chest | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0.08] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.023] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.15] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.05] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0.04] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.15] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [0.88] (0 ~ 1) | 14/15/False
| │ └ Z | [0.7] (0 ~ 1) | 15/15/False
| ├ **Ribs** | | 6/17/True
| │ ├ Enable Ribs | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0.075] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0.015] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [-0.015] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.05] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.05] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Waist** | | 7/17/True
| │ ├ Enable Waist | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0.032] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [-0.01] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.11] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [-0.3] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.05] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.125] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [0.8] (0 ~ 1) | 15/15/False
| ├ **Belly** | | 8/17/True
| │ ├ Enable Belly | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0.013] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.15] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.073] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [-0.01] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.125] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [0.65] (0 ~ 1) | 15/15/False
| ├ **Butts** | | 9/17/True
| │ ├ Enable Butts | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0.066] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [-0.0425] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.05] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.105] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0.066] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0.012] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.09] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Shoulder** | | 10/17/True
| │ ├ Enable Shoulder | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [-0.02] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0.02] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.01] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.05] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.4] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [-0.01] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.05] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Upper Arm** | | 11/17/True
| │ ├ Enable Upper Arm | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.01] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.053] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.15] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.035] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Lower Arm** | | 12/17/True
| │ ├ Enable Lower Arm | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.01] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.0445] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.44] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.01] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Hand** | | 13/17/True
| │ ├ Enable Hand | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.0315] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [-0.0316] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.05] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Hips** | | 14/17/True
| │ ├ Enable Hips | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0.01] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [-0.027] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.1] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.455] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0.01] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [-0.1] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.085] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Thigh** | | 15/17/True
| │ ├ Enable Thigh | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0.01] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.073] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.455] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [-0.01] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.05599999] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| ├ **Shin** | | 16/17/True
| │ ├ Enable Shin | ON | 0/21/False
| │ ├ Position From || 1/21/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/21/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 3/21/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 4/21/False
| │ ├ Radius From | [0.05926838] (0 ~ 0.15) | 5/21/False
| │ ├ Curve | [0] (-2 ~ 2) | 6/21/False
| │ ├ Position Middle || 7/21/False
| │ ├ X | [0.009999919] (-0.25 ~ 0.25) | 8/21/False
| │ ├ Y | [0.05999992] (-0.25 ~ 0.25) | 9/21/False
| │ ├ Z | [0.01666657] (-0.25 ~ 0.25) | 10/21/False
| │ ├ Radius Middle | [0.06707321] (0 ~ 0.15) | 11/21/False
| │ ├ Curve Middle | [0] (-2 ~ 2) | 12/21/False
| │ ├ Position To || 13/21/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 14/21/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 15/21/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 16/21/False
| │ ├ Radius To | [0.03231711] (0 ~ 0.15) | 17/21/False
| │ ├ Scale || 18/21/False
| │ ├ X | [1] (0 ~ 1) | 19/21/False
| │ ├ Y | [1] (0 ~ 1) | 20/21/False
| │ └ Z | [1] (0 ~ 1) | 21/21/False
| ├ **Foot** | | 17/17/True
| │ ├ Enable Foot | ON | 0/15/False
| │ ├ Position From || 1/15/False
| │ ├ X | [0] (-0.25 ~ 0.25) | 2/15/False
| │ ├ Y | [-0.03166673] (-0.25 ~ 0.25) | 3/15/False
| │ ├ Z | [0.015] (-0.25 ~ 0.25) | 4/15/False
| │ ├ Radius From | [0.053] (0 ~ 0.15) | 5/15/False
| │ ├ Curve | [0.1] (-2 ~ 2) | 6/15/False
| │ ├ Position To || 7/15/False
| │ ├ X | [0.028] (-0.25 ~ 0.25) | 8/15/False
| │ ├ Y | [0] (-0.25 ~ 0.25) | 9/15/False
| │ ├ Z | [0] (-0.25 ~ 0.25) | 10/15/False
| │ ├ Radius To | [0.0625] (0 ~ 0.15) | 11/15/False
| │ ├ Scale || 12/15/False
| │ ├ X | [1] (0 ~ 1) | 13/15/False
| │ ├ Y | [1] (0 ~ 1) | 14/15/False
| │ └ Z | [1] (0 ~ 1) | 15/15/False
| └ Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
| **Mesh Collider** | | 9/10/True
| ├ Enable Mesh Collider | ON | 0/6/False
| ├ Disable Geometry Colliders | ON | 1/6/False
| ├ Visulize | OFF | 2/6/False
| ├ Depth | [0.025] (0 ~ 0.1) | 3/6/False
| ├ Skip Edge | ON | 4/6/False
| ├ Skip Point | ON | 5/6/False
| └ Single Collision | ON | 6/6/False
| **Simulation Settings** | | 10/10/True
| ├ Enable Dragging | ON | 0/10/False
| ├ Reset Scale | [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.1/10/False
| ├ Simulate | ON | 2/10/False
| ├ Simulation FPS: Dynamic || 3/10/False
| │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
| ├ Substeps | [4] (1 ~ 20) | 5/10/False
| ├ Iterations | [1] (0 ~ 10) | 6/10/False
| ├ Reverse Even Substeps | OFF | 7/10/False
| ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
| ├ Table Size | [6] (1 ~ 20) | 9/10/False
| └ Two Step Solving | OFF | 10/10/False
| Presets | **Default (Reset)** | Default (Reset),  |
