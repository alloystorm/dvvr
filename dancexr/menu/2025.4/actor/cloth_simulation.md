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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
|  Reset|| 
|  □ <b>Cloth 1</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Rebuild Mesh|| Most parameters here requires rebuilding the mesh to take effect.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Topology| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> String Connection| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inner Radius| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Slope| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arc| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Length| [0.25] (0 ~ 0.75) | Length in meters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Holes| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Hole Height| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Back Length| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Side Length| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Vertical Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Compliance| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV Mapping| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Top Layers| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Top Anchor</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├─ <b>Anchor Positoin</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>Anchor Rotation</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom Layers| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Bottom Anchor</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ Swap Side| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Positoin</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Rotation</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale| [1] (0 ~ 2) | 
| │ ├─ □ Self Collision| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale| [1] (0 ~ 2) | 
| │ ├─ □ Enable Tearing| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C1 Material</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├─ □ Glass Mode| [OFF] | 
| ├─ □ Alpha As Gloss| [OFF] | 
| ├─ □ Double Side| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dim Back| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Cast Shadow| [0.5] (0 ~ 1) | 
| ├─ □ Depth Prepass| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gloss| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alpha| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Clip| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Blend Mode| **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─ □ <b>Toon Shader</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shading| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Outline| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Specular| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Specular| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Highlight Area| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Highlight| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Area| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Shadow| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Special Shader</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Mode| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Refraction| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thickness| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Texture| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Detail Map</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>Hexagon Map</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Enable| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Density| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Noise| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Use Circle| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Edge| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Select Map| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Rotation| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Scale| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Bump| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect AO| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Smoothness| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Metallic| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Color Blend| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anisotropy| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP Map Bias| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|  □ <b>Cloth 2</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Rebuild Mesh|| Most parameters here requires rebuilding the mesh to take effect.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Topology| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> String Connection| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inner Radius| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Slope| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arc| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Length| [0.25] (0 ~ 0.75) | Length in meters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Holes| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Hole Height| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Back Length| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Side Length| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Vertical Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Compliance| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV Mapping| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Top Layers| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Top Anchor</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├─ <b>Anchor Positoin</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>Anchor Rotation</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom Layers| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Bottom Anchor</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ Swap Side| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Positoin</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Rotation</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale| [1] (0 ~ 2) | 
| │ ├─ □ Self Collision| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale| [1] (0 ~ 2) | 
| │ ├─ □ Enable Tearing| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C2 Material</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├─ □ Glass Mode| [OFF] | 
| ├─ □ Alpha As Gloss| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Double Side| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dim Back| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Cast Shadow| [0.5] (0 ~ 1) | 
| ├─ □ Depth Prepass| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gloss| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alpha| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Clip| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Blend Mode| **Multiply** | Original, Multiply, Blend, Color Shift,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─ □ <b>Toon Shader</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shading| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Outline| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Specular| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Specular| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Highlight Area| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Highlight| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Area| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Shadow| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Special Shader</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Mode| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Refraction| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thickness| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Texture| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Detail Map</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>Hexagon Map</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Enable| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Density| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Noise| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Use Circle| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Edge| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Select Map| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Rotation| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Scale| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Bump| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect AO| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Smoothness| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Metallic| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Color Blend| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anisotropy| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP Map Bias| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|  □ Combine| [OFF] | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
|  □ <b>Fluid (Experimental)</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Spawn</b>| | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Position</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (Unlimited) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [2.5] (Unlimited) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (Unlimited) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Rotation</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-180 ~ 180) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-180 ~ 180) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-180 ~ 180) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spawn Radius| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spread| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spawn Rate| [20] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Speed| [5] (0 ~ 10) | 
| │ ├─ □ Mouse / Hand Control| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Auto Aim| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max TTL| [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> TTL on Floor| [0.1] (0 ~ 1) | Time to live after hitting floor.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Smoothing| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Fluid</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cohesion| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Viscosity| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stick To Surface| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Density| [2] (1 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cohesion Range| [20] (1 ~ 50) | Max distance for cohesion effect
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Distance| [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Elevation| [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Water** | Water, Viscous, Sand,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Render</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Render Particle| [ON] | 
| │ ├─ □ Render Droplet| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Droplet Size| [2] (0 ~ 50) | Droplet size in MM
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale By Density| [0] (0 ~ 5) | Scale droplet size by density of the fluid
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Smoothness| [0.95] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow| [0] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Transparency| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [-2] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [-2] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ Player| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Geometry Collider</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ □ Visible| [OFF] | 
| ├─ Export Shape|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Head</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [-0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.04] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.5] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.11] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.8] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Neck</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.045] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.065] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.045] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Chest</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.023] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.04] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.15] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.88] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.7] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Ribs</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.075] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [-0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Waist</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.032] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.11] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [-0.3] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Belly</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.013] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.073] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.65] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Butts</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [-0.0425] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.105] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.012] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.09] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shoulder</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [-0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.4] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Upper Arm</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.15] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.035] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Lower Arm</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.0445] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.44] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.01] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Hand</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.0315] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [-0.0316] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Hips</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [-0.027] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.1] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.455] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [-0.1] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.085] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Thigh</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.073] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.455] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.05599999] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shin</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.05926838] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0] (-2 ~ 2) | 
| │ ├─ <b>Position Middle</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.009999919] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.05999992] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.01666657] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius Middle| [0.06707321] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve Middle| [0] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.03231711] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Foot</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [-0.03166673] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.028] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To| [0.0625] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Mesh Collider</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Disable Geometry Colliders| [ON] | 
| ├─ □ Visulize| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.025] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Skip Edge| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Skip Point| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Single Collision| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reset Scale| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| ├─ □ Reverse Even Substeps| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| └─ □ Two Step Solving| [OFF] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
