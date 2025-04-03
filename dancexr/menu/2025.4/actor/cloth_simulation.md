---
locale: en-rUS
layout: single
title: Simulation
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[Pro](../menu#Pro) > Simulation



| Setting | Value | Description |
| :--- | --- | :--- |
| Enable | ON | 
| Reset || 
| **Cloth 1** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Rebuild Mesh || Most parameters here requires rebuilding the mesh to take effect.
| ├&nbsp;Topology: Horizontal Layout || 
| │&nbsp;Topology | **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├&nbsp;String Connection | [4] (1 ~ 10) | 
| ├&nbsp;Inner Radius | [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├&nbsp;Slope | [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├&nbsp;Arc | [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├&nbsp;Length | [0.25] (0 ~ 0.75) | Length in meters
| ├&nbsp;Arm Holes | [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├&nbsp;Arm Hole Height | [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├&nbsp;Back Length | [1] (0.1 ~ 1.9) | 
| ├&nbsp;Side Length | [1] (0.1 ~ 1.9) | 
| ├&nbsp;Horizontal Resolution | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;Vertical Resolution | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;Distance Compliance | [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├&nbsp;UV Mapping: Mirror Scaled || 
| │&nbsp;UV Mapping | **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├&nbsp;**Anchor** | | 
| │&nbsp;├&nbsp;Top Layers | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**Top Anchor** | | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Selection | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Selection Offset | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Bone: Torso || 
| │&nbsp;│&nbsp;│&nbsp;Anchor Bone | **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │&nbsp;│&nbsp;├&nbsp;Lock Mode: None || 
| │&nbsp;│&nbsp;│&nbsp;Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │&nbsp;│&nbsp;├&nbsp;Anchor Positoin || 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Z | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Rotation || 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Z | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Bottom Layers | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**Bottom Anchor** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Selection | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Selection Offset | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Bone: Waist || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Anchor Bone | **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Swap Side | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Lock Mode: None || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Positoin || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;X | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Y | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Z | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Rotation || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;X | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Y | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Z | [0] (-1 ~ 1) | 
| ├&nbsp;**Particle Properties** | | 
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Stickiness | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;Enable Bending Constraints | ON | 
| │&nbsp;├&nbsp;Bending Compliance | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Scale | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Self Collision | OFF | 
| │&nbsp;├&nbsp;Grip Mass | [2] (0 ~ 4) | Mass of grip particles
| │&nbsp;├&nbsp;Grip Friction | [2] (-2 ~ 4) | Friction for grip particles
| │&nbsp;├&nbsp;Grip Stickiness | [0.25] (0 ~ 1) | Stickiness of grip particles
| │&nbsp;├&nbsp;Grip Drag | [0] (-2 ~ 2) | Air resistancy for grip particles
| │&nbsp;├&nbsp;Grip Scale | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Enable Tearing | OFF | 
| │&nbsp;├&nbsp;Tear Threshold | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;Limit Tearing Speed | [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └&nbsp;Presets: Top || 
| &nbsp;&nbsp;Presets | **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| **C1 Material** | | 
| ├&nbsp;Surface || 
| ├&nbsp;Presets: Matt Gray || 
| │&nbsp;Presets | **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├&nbsp;Glass Mode | OFF | 
| ├&nbsp;Alpha As Gloss | OFF | 
| ├&nbsp;Double Side | OFF | 
| ├&nbsp;Dim Back | [1] (0 ~ 1) | 
| ├&nbsp;Cast Shadow | [0.5] (0 ~ 1) | 
| ├&nbsp;Depth Prepass | [0.8] (0 ~ 1) | 
| ├&nbsp;Gloss | [0.3] (0 ~ 1) | 
| ├&nbsp;Metallic | [0] (0 ~ 1) | 
| ├&nbsp;Bump | [0.2] (0 ~ 1) | 
| ├&nbsp;Glow | [0] (0 ~ 10) | 
| ├&nbsp;Ambient | [1] (0 ~ 1) | 
| ├&nbsp;Alpha | [1] (0 ~ 1) | 
| ├&nbsp;Clip | [0] (0 ~ 1) | 
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blend Mode: Blend || 
| │&nbsp;│&nbsp;Blend Mode | **Blend** | Original, Multiply, Blend, Color Shift,  |
| │&nbsp;├&nbsp;Blend | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Presets: Gray || 
| │&nbsp;&nbsp;&nbsp;Presets | **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├&nbsp;**Toon Shader** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Shading | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Outline | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Specular | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Specular | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Highlight Area | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Highlight | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Ambient | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Shadow Area | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;Shadow | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Shadow | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Presets: Sharp || 
| │&nbsp;&nbsp;&nbsp;Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├&nbsp;**Special Shader** | | 
| │&nbsp;├&nbsp;Mode: Off || 
| │&nbsp;│&nbsp;Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │&nbsp;├&nbsp;Refraction | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;Thickness | [1] (0 ~ 1) | 
| ├&nbsp;Texture: [Solid Color] || 
| │&nbsp;Texture | **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └&nbsp;**Detail Map** | | 
| &nbsp;&nbsp;├&nbsp;Enable | ON | 
| &nbsp;&nbsp;├&nbsp;**Hexagon Map** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Enable | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Density | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Size | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Bump | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Noise | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Use Circle | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;Soft Edge | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Select Map: Fabric 3 || 
| &nbsp;&nbsp;│&nbsp;Select Map | **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| &nbsp;&nbsp;├&nbsp;Detail Map Rotation | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;Detail Map Scale | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;Detail Map Bump | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect AO | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Smoothness | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Metallic | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Color Blend | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Anisotropy | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP Map Bias | [0] (-5 ~ 5) | Adjust sharpness of detail texture.
| **Cloth 2** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Rebuild Mesh || Most parameters here requires rebuilding the mesh to take effect.
| ├&nbsp;Topology: Horizontal Layout || 
| │&nbsp;Topology | **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├&nbsp;String Connection | [4] (1 ~ 10) | 
| ├&nbsp;Inner Radius | [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├&nbsp;Slope | [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├&nbsp;Arc | [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├&nbsp;Length | [0.25] (0 ~ 0.75) | Length in meters
| ├&nbsp;Arm Holes | [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├&nbsp;Arm Hole Height | [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├&nbsp;Back Length | [1] (0.1 ~ 1.9) | 
| ├&nbsp;Side Length | [1] (0.1 ~ 1.9) | 
| ├&nbsp;Horizontal Resolution | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;Vertical Resolution | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;Distance Compliance | [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├&nbsp;UV Mapping: Mirror Scaled || 
| │&nbsp;UV Mapping | **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├&nbsp;**Anchor** | | 
| │&nbsp;├&nbsp;Top Layers | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**Top Anchor** | | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Selection | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Selection Offset | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Bone: Torso || 
| │&nbsp;│&nbsp;│&nbsp;Anchor Bone | **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │&nbsp;│&nbsp;├&nbsp;Lock Mode: None || 
| │&nbsp;│&nbsp;│&nbsp;Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │&nbsp;│&nbsp;├&nbsp;Anchor Positoin || 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Z | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Anchor Rotation || 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Z | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Bottom Layers | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**Bottom Anchor** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Selection | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Selection Offset | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Bone: Waist || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Anchor Bone | **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Swap Side | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Lock Mode: None || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Lock Mode | **None** | None, Lock, Lock Height, Sticky,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Positoin || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;X | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Y | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Z | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Rotation || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;X | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Y | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Z | [0] (-1 ~ 1) | 
| ├&nbsp;**Particle Properties** | | 
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Stickiness | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;Enable Bending Constraints | ON | 
| │&nbsp;├&nbsp;Bending Compliance | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Scale | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Self Collision | OFF | 
| │&nbsp;├&nbsp;Grip Mass | [2] (0 ~ 4) | Mass of grip particles
| │&nbsp;├&nbsp;Grip Friction | [2] (-2 ~ 4) | Friction for grip particles
| │&nbsp;├&nbsp;Grip Stickiness | [0.25] (0 ~ 1) | Stickiness of grip particles
| │&nbsp;├&nbsp;Grip Drag | [0] (-2 ~ 2) | Air resistancy for grip particles
| │&nbsp;├&nbsp;Grip Scale | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Enable Tearing | OFF | 
| │&nbsp;├&nbsp;Tear Threshold | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;Limit Tearing Speed | [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └&nbsp;Presets: Skirt || 
| &nbsp;&nbsp;Presets | **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| **C2 Material** | | 
| ├&nbsp;Surface || 
| ├&nbsp;Presets: Matt Gray || 
| │&nbsp;Presets | **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├&nbsp;Glass Mode | OFF | 
| ├&nbsp;Alpha As Gloss | OFF | 
| ├&nbsp;Double Side | ON | 
| ├&nbsp;Dim Back | [1] (0 ~ 1) | 
| ├&nbsp;Cast Shadow | [0.5] (0 ~ 1) | 
| ├&nbsp;Depth Prepass | [0.8] (0 ~ 1) | 
| ├&nbsp;Gloss | [0.3] (0 ~ 1) | 
| ├&nbsp;Metallic | [0] (0 ~ 1) | 
| ├&nbsp;Bump | [0.2] (0 ~ 1) | 
| ├&nbsp;Glow | [0] (0 ~ 10) | 
| ├&nbsp;Ambient | [1] (0 ~ 1) | 
| ├&nbsp;Alpha | [1] (0 ~ 1) | 
| ├&nbsp;Clip | [0] (0 ~ 1) | 
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blend Mode: Multiply || 
| │&nbsp;│&nbsp;Blend Mode | **Multiply** | Original, Multiply, Blend, Color Shift,  |
| │&nbsp;├&nbsp;Blend | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Presets: Gray || 
| │&nbsp;&nbsp;&nbsp;Presets | **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├&nbsp;**Toon Shader** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Shading | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Outline | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Specular | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Specular | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Highlight Area | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Highlight | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Ambient | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Shadow Area | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;Shadow | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Soft Shadow | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Presets: Sharp || 
| │&nbsp;&nbsp;&nbsp;Presets | **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├&nbsp;**Special Shader** | | 
| │&nbsp;├&nbsp;Mode: Off || 
| │&nbsp;│&nbsp;Mode | **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │&nbsp;├&nbsp;Refraction | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;Thickness | [1] (0 ~ 1) | 
| ├&nbsp;Texture: [Solid Color] || 
| │&nbsp;Texture | **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └&nbsp;**Detail Map** | | 
| &nbsp;&nbsp;├&nbsp;Enable | ON | 
| &nbsp;&nbsp;├&nbsp;**Hexagon Map** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Enable | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Density | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Size | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Bump | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Noise | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;Use Circle | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;Soft Edge | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Select Map: Fabric 3 || 
| &nbsp;&nbsp;│&nbsp;Select Map | **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| &nbsp;&nbsp;├&nbsp;Detail Map Rotation | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;Detail Map Scale | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;Detail Map Bump | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect AO | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Smoothness | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Metallic | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Affect Color Blend | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Anisotropy | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP Map Bias | [0] (-5 ~ 5) | Adjust sharpness of detail texture.
| Combine | OFF | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
| **Fluid (Experimental)** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;**Spawn** | | 
| │&nbsp;├&nbsp;**Position** | | 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (Unlimited) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [2.5] (Unlimited) | 
| │&nbsp;│&nbsp;└&nbsp;Z | [0] (Unlimited) | 
| │&nbsp;├&nbsp;**Rotation** | | 
| │&nbsp;│&nbsp;├&nbsp;X | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;└&nbsp;Z | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;Spawn Radius | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Spread | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Spawn Rate | [20] (0 ~ 20) | 
| │&nbsp;├&nbsp;Speed | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;Mouse / Hand Control | OFF | 
| │&nbsp;├&nbsp;Auto Aim | ON | 
| │&nbsp;├&nbsp;Max TTL | [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
| │&nbsp;├&nbsp;TTL on Floor | [0.1] (0 ~ 1) | Time to live after hitting floor.
| │&nbsp;├&nbsp;Smoothing | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;Presets: Sprinkler || 
| │&nbsp;&nbsp;&nbsp;Presets | **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
| ├&nbsp;**Fluid** | | 
| │&nbsp;├&nbsp;Cohesion | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Viscosity | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Stick To Surface | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Target Density | [2] (1 ~ 10) | 
| │&nbsp;├&nbsp;Cohesion Range | [20] (1 ~ 50) | Max distance for cohesion effect
| │&nbsp;├&nbsp;Target Distance | [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
| │&nbsp;├&nbsp;Elevation | [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
| │&nbsp;└&nbsp;Presets: Water || 
| │&nbsp;&nbsp;&nbsp;Presets | **Water** | Water, Viscous, Sand,  |
| ├&nbsp;**Render** | | 
| │&nbsp;├&nbsp;Render Particle | ON | 
| │&nbsp;├&nbsp;Render Droplet | OFF | 
| │&nbsp;├&nbsp;Droplet Size | [2] (0 ~ 50) | Droplet size in MM
| │&nbsp;├&nbsp;Scale By Density | [0] (0 ~ 5) | Scale droplet size by density of the fluid
| │&nbsp;├&nbsp;**Color** | | 
| │&nbsp;│&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;│&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Metallic | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Smoothness | [0.95] (0 ~ 1) | 
| │&nbsp;├&nbsp;Glow | [0] (0 ~ 1) | 
| │&nbsp;└&nbsp;Transparency | [0.1] (0 ~ 1) | 
| ├&nbsp;**Particle Properties** | | 
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [-2] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [-2] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Player | OFF | 
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset),  |
| **Geometry Collider** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Visible | OFF | 
| ├&nbsp;Export Shape || 
| ├&nbsp;**Head** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [-0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.04] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.5] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Neck** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.065] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Chest** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.023] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.04] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [0.88] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [0.7] (0 ~ 1) | 
| ├&nbsp;**Ribs** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0.075] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [-0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Waist** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.032] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [-0.3] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [0.8] (0 ~ 1) | 
| ├&nbsp;**Belly** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.013] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.073] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [0.65] (0 ~ 1) | 
| ├&nbsp;**Butts** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [-0.0425] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.105] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.012] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.09] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Shoulder** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [-0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.4] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Upper Arm** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.15] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.035] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Lower Arm** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.0445] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.44] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.01] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Hand** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.0315] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [-0.0316] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Hips** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [-0.027] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.1] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [-0.1] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.085] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Thigh** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.073] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.05599999] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Shin** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.05926838] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position Middle || 
| │&nbsp;├&nbsp;X | [0.009999919] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0.05999992] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.01666657] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius Middle | [0.06707321] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve Middle | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.03231711] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| ├&nbsp;**Foot** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Position From || 
| │&nbsp;├&nbsp;X | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [-0.03166673] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius From | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Curve | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Position To || 
| │&nbsp;├&nbsp;X | [0.028] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Y | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Z | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;Radius To | [0.0625] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;Scale || 
| │&nbsp;├&nbsp;X | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Z | [1] (0 ~ 1) | 
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
| **Mesh Collider** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Disable Geometry Colliders | ON | 
| ├&nbsp;Visulize | OFF | 
| ├&nbsp;Depth | [0.025] (0 ~ 0.1) | 
| ├&nbsp;Skip Edge | ON | 
| ├&nbsp;Skip Point | ON | 
| └&nbsp;Single Collision | ON | 
| **Simulation Settings** | | 
| ├&nbsp;Enable Dragging | ON | 
| ├&nbsp;Reset Scale | [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
| ├&nbsp;Simulate | ON | 
| ├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| ├&nbsp;Substeps | [4] (1 ~ 20) | 
| ├&nbsp;Iterations | [1] (0 ~ 10) | 
| ├&nbsp;Reverse Even Substeps | OFF | 
| ├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| ├&nbsp;Table Size | [6] (1 ~ 20) | 
| └&nbsp;Two Step Solving | OFF | 
| Presets: Default (Reset) || 
| Presets | **Default (Reset)** | Default (Reset),  |
