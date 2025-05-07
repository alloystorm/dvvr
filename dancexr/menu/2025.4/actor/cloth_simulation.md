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
|  ☑ Enable| [ON] | 
|  Reset|| 
|  □ <b>Cloth 1</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Rebuild Mesh|| Most parameters here requires rebuilding the mesh to take effect.
| ├─ > Topology| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├─ ⊖ String Connection| [4] (1 ~ 10) | 
| ├─ ⊖ Inner Radius| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├─ ⊖ Slope| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├─ ⊖ Arc| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├─ ⊖ Length| [0.25] (0 ~ 0.75) | Length in meters
| ├─ ⊖ Arm Holes| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├─ ⊖ Arm Hole Height| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├─ ⊖ Back Length| [1] (0.1 ~ 1.9) | 
| ├─ ⊖ Side Length| [1] (0.1 ~ 1.9) | 
| ├─ ⊖ Horizontal Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─ ⊖ Vertical Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─ ⊖ Distance Compliance| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├─ > UV Mapping| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├─ ⚙️ <b>Anchor</b>| | 
| │ ├─ ⊖ Top Layers| [2] (0 ~ 10) | 
| │ ├─ ⚙️ <b>Top Anchor</b>| | 
| │ │ ├─ ⊖ Anchor Selection| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ Selection Offset| [0.5] (0 ~ 1) | 
| │ │ ├─ > Anchor Bone| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├─ > Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├─ <b>Anchor Positoin</b>|| 
| │ │ ├─ ⊖ X| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ ⊖ Y| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─ ⊖ Z| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>Anchor Rotation</b>|| 
| │ │ ├─ ⊖ X| [0] (-1 ~ 1) | 
| │ │ ├─ ⊖ Y| [0] (-1 ~ 1) | 
| │ │ └─ ⊖ Z| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Bottom Layers| [0] (0 ~ 10) | 
| │ └─ ⚙️ <b>Bottom Anchor</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Anchor Selection| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Selection Offset| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ > Anchor Bone| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ Swap Side| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─ > Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Positoin</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ X| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Y| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Z| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Rotation</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ X| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Y| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─ ⊖ Z| [0] (-1 ~ 1) | 
| ├─ ⚙️ <b>Particle Properties</b>| | 
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Stickiness| [0] (0 ~ 1) | 
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─ ⚙️ <b>Collide With</b>| | 
| │ │ ├─ ☑ Head| [ON] | 
| │ │ ├─ ☑ Body| [ON] | 
| │ │ ├─ ☑ Boobs| [ON] | 
| │ │ ├─ ☑ Butts| [ON] | 
| │ │ ├─ ☑ Arms| [ON] | 
| │ │ ├─ ☑ Hands| [ON] | 
| │ │ ├─ ☑ Legs| [ON] | 
| │ │ ├─ ☑ Feet| [ON] | 
| │ │ └─ ☑ Player| [ON] | 
| │ ├─ ☑ Enable Bending Constraints| [ON] | 
| │ ├─ ⊖ Bending Compliance| [0] (0 ~ 1) | 
| │ ├─ ⊖ Scale| [1] (0 ~ 2) | 
| │ ├─ □ Self Collision| [OFF] | 
| │ ├─ ⊖ Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| │ ├─ ⊖ Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| │ ├─ ⊖ Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| │ ├─ ⊖ Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| │ ├─ ⊖ Grip Scale| [1] (0 ~ 2) | 
| │ ├─ □ Enable Tearing| [OFF] | 
| │ ├─ ⊖ Tear Threshold| [2] (1 ~ 10) | 
| │ └─ ⊖ Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|  ⚙️ <b>C1 Material</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├─ □ Glass Mode| [OFF] | 
| ├─ □ Alpha As Gloss| [OFF] | 
| ├─ □ Double Side| [OFF] | 
| ├─ ⊖ Dim Back| [1] (0 ~ 1) | 
| ├─ ☑ Cast Shadow| [0.5] (0 ~ 1) | 
| ├─ □ Depth Prepass| [0.8] (0 ~ 1) | 
| ├─ ⊖ Gloss| [0.3] (0 ~ 1) | 
| ├─ ⊖ Metallic| [0] (0 ~ 1) | 
| ├─ ⊖ Bump| [0.2] (0 ~ 1) | 
| ├─ ⊖ Glow| [0] (0 ~ 10) | 
| ├─ ⊖ Ambient| [1] (0 ~ 1) | 
| ├─ ⊖ Alpha| [1] (0 ~ 1) | 
| ├─ ⊖ Clip| [0] (0 ~ 1) | 
| ├─ ⚙️ <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─ ⊖ Hue| [0] (0 ~ 1) | 
| │ ├─ ⊖ Satuation| [0] (0 ~ 1) | 
| │ ├─ ⊖ Brightness| [1] (0 ~ 1) | 
| │ ├─ ⊖ Red| [1] (0 ~ 1) | 
| │ ├─ ⊖ Green| [1] (0 ~ 1) | 
| │ ├─ ⊖ Blue| [1] (0 ~ 1) | 
| │ ├─ > Blend Mode| **Blend** | Original, Multiply, Blend, Color Shift,  |
| │ ├─ ⊖ Blend| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─ □ <b>Toon Shader</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⊖ Shading| [1] (0 ~ 1) | 
| │ ├─ ⊖ Outline| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Specular| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Soft Specular| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Highlight Area| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Soft Highlight| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Ambient| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Shadow Area| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ Shadow| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Soft Shadow| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─ ⚙️ <b>Special Shader</b>| | 
| │ ├─ > Mode| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─ ⊖ Refraction| [0.5] (1 ~ 3) | 
| │ └─ ⊖ Thickness| [1] (0 ~ 1) | 
| ├─ > Texture| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └─ ☑ <b>Detail Map</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ Enable| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>Hexagon Map</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Enable| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Density| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Size| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Bump| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Noise| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Use Circle| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─ ⊖ Soft Edge| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ > Select Map| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Rotation| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Scale| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Bump| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect AO| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Smoothness| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Metallic| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Color Blend| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Anisotropy| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─ ⊖ MIP Map Bias| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|  □ <b>Cloth 2</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Rebuild Mesh|| Most parameters here requires rebuilding the mesh to take effect.
| ├─ > Topology| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
| ├─ ⊖ String Connection| [4] (1 ~ 10) | 
| ├─ ⊖ Inner Radius| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
| ├─ ⊖ Slope| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
| ├─ ⊖ Arc| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
| ├─ ⊖ Length| [0.25] (0 ~ 0.75) | Length in meters
| ├─ ⊖ Arm Holes| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
| ├─ ⊖ Arm Hole Height| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
| ├─ ⊖ Back Length| [1] (0.1 ~ 1.9) | 
| ├─ ⊖ Side Length| [1] (0.1 ~ 1.9) | 
| ├─ ⊖ Horizontal Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─ ⊖ Vertical Resolution| [0.01] (0.005 ~ 0.025) | 
| ├─ ⊖ Distance Compliance| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
| ├─ > UV Mapping| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
| ├─ ⚙️ <b>Anchor</b>| | 
| │ ├─ ⊖ Top Layers| [2] (0 ~ 10) | 
| │ ├─ ⚙️ <b>Top Anchor</b>| | 
| │ │ ├─ ⊖ Anchor Selection| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ Selection Offset| [0.5] (0 ~ 1) | 
| │ │ ├─ > Anchor Bone| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ │ ├─ > Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ │ ├─ <b>Anchor Positoin</b>|| 
| │ │ ├─ ⊖ X| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ ⊖ Y| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─ ⊖ Z| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>Anchor Rotation</b>|| 
| │ │ ├─ ⊖ X| [0] (-1 ~ 1) | 
| │ │ ├─ ⊖ Y| [0] (-1 ~ 1) | 
| │ │ └─ ⊖ Z| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Bottom Layers| [0] (0 ~ 10) | 
| │ └─ ⚙️ <b>Bottom Anchor</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Anchor Selection| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Selection Offset| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ > Anchor Bone| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ Swap Side| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─ > Lock Mode| **None** | None, Lock, Lock Height, Sticky,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Positoin</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ X| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Y| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Z| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>Anchor Rotation</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ X| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─ ⊖ Y| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─ ⊖ Z| [0] (-1 ~ 1) | 
| ├─ ⚙️ <b>Particle Properties</b>| | 
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Stickiness| [0] (0 ~ 1) | 
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─ ⚙️ <b>Collide With</b>| | 
| │ │ ├─ ☑ Head| [ON] | 
| │ │ ├─ ☑ Body| [ON] | 
| │ │ ├─ ☑ Boobs| [ON] | 
| │ │ ├─ ☑ Butts| [ON] | 
| │ │ ├─ ☑ Arms| [ON] | 
| │ │ ├─ ☑ Hands| [ON] | 
| │ │ ├─ ☑ Legs| [ON] | 
| │ │ ├─ ☑ Feet| [ON] | 
| │ │ └─ ☑ Player| [ON] | 
| │ ├─ ☑ Enable Bending Constraints| [ON] | 
| │ ├─ ⊖ Bending Compliance| [0] (0 ~ 1) | 
| │ ├─ ⊖ Scale| [1] (0 ~ 2) | 
| │ ├─ □ Self Collision| [OFF] | 
| │ ├─ ⊖ Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| │ ├─ ⊖ Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| │ ├─ ⊖ Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| │ ├─ ⊖ Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| │ ├─ ⊖ Grip Scale| [1] (0 ~ 2) | 
| │ ├─ □ Enable Tearing| [OFF] | 
| │ ├─ ⊖ Tear Threshold| [2] (1 ~ 10) | 
| │ └─ ⊖ Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|  ⚙️ <b>C2 Material</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
| ├─ □ Glass Mode| [OFF] | 
| ├─ □ Alpha As Gloss| [OFF] | 
| ├─ ☑ Double Side| [ON] | 
| ├─ ⊖ Dim Back| [1] (0 ~ 1) | 
| ├─ ☑ Cast Shadow| [0.5] (0 ~ 1) | 
| ├─ □ Depth Prepass| [0.8] (0 ~ 1) | 
| ├─ ⊖ Gloss| [0.3] (0 ~ 1) | 
| ├─ ⊖ Metallic| [0] (0 ~ 1) | 
| ├─ ⊖ Bump| [0.2] (0 ~ 1) | 
| ├─ ⊖ Glow| [0] (0 ~ 10) | 
| ├─ ⊖ Ambient| [1] (0 ~ 1) | 
| ├─ ⊖ Alpha| [1] (0 ~ 1) | 
| ├─ ⊖ Clip| [0] (0 ~ 1) | 
| ├─ ⚙️ <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─ ⊖ Hue| [0] (0 ~ 1) | 
| │ ├─ ⊖ Satuation| [0] (0 ~ 1) | 
| │ ├─ ⊖ Brightness| [1] (0 ~ 1) | 
| │ ├─ ⊖ Red| [1] (0 ~ 1) | 
| │ ├─ ⊖ Green| [1] (0 ~ 1) | 
| │ ├─ ⊖ Blue| [1] (0 ~ 1) | 
| │ ├─ > Blend Mode| **Multiply** | Original, Multiply, Blend, Color Shift,  |
| │ ├─ ⊖ Blend| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
| ├─ □ <b>Toon Shader</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⊖ Shading| [1] (0 ~ 1) | 
| │ ├─ ⊖ Outline| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Specular| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Soft Specular| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Highlight Area| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Soft Highlight| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Ambient| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Shadow Area| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ Shadow| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Soft Shadow| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
| ├─ ⚙️ <b>Special Shader</b>| | 
| │ ├─ > Mode| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
| │ ├─ ⊖ Refraction| [0.5] (1 ~ 3) | 
| │ └─ ⊖ Thickness| [1] (0 ~ 1) | 
| ├─ > Texture| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
| └─ ☑ <b>Detail Map</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ Enable| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>Hexagon Map</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Enable| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Density| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Size| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Bump| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ ⊖ Noise| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Use Circle| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─ ⊖ Soft Edge| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ > Select Map| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Rotation| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Scale| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Detail Map Bump| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect AO| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Smoothness| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Metallic| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Affect Color Blend| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Anisotropy| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─ ⊖ MIP Map Bias| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|  □ Combine| [OFF] | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
|  □ <b>Fluid (Experimental)</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ⚙️ <b>Spawn</b>| | 
| │ ├─ ⚙️ <b>Position</b>| | 
| │ │ ├─ ⊖ X| [0] (Unlimited) | 
| │ │ ├─ ⊖ Y| [2.5] (Unlimited) | 
| │ │ └─ ⊖ Z| [0] (Unlimited) | 
| │ ├─ ⚙️ <b>Rotation</b>| | 
| │ │ ├─ ⊖ X| [0] (-180 ~ 180) | 
| │ │ ├─ ⊖ Y| [0] (-180 ~ 180) | 
| │ │ └─ ⊖ Z| [0] (-180 ~ 180) | 
| │ ├─ ⊖ Spawn Radius| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Spread| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Spawn Rate| [20] (0 ~ 20) | 
| │ ├─ ⊖ Speed| [5] (0 ~ 10) | 
| │ ├─ □ Mouse / Hand Control| [OFF] | 
| │ ├─ ☑ Auto Aim| [ON] | 
| │ ├─ ⊖ Max TTL| [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
| │ ├─ ⊖ TTL on Floor| [0.1] (0 ~ 1) | Time to live after hitting floor.
| │ ├─ ⊖ Smoothing| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
| ├─ ⚙️ <b>Fluid</b>| | 
| │ ├─ ⊖ Cohesion| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Viscosity| [0] (0 ~ 1) | 
| │ ├─ ⊖ Stick To Surface| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Target Density| [2] (1 ~ 10) | 
| │ ├─ ⊖ Cohesion Range| [20] (1 ~ 50) | Max distance for cohesion effect
| │ ├─ ⊖ Target Distance| [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
| │ ├─ ⊖ Elevation| [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Water** | Water, Viscous, Sand,  |
| ├─ ⚙️ <b>Render</b>| | 
| │ ├─ ☑ Render Particle| [ON] | 
| │ ├─ □ Render Droplet| [OFF] | 
| │ ├─ ⊖ Droplet Size| [2] (0 ~ 50) | Droplet size in MM
| │ ├─ ⊖ Scale By Density| [0] (0 ~ 5) | Scale droplet size by density of the fluid
| │ ├─ ⚙️ <b>Color</b>| | 
| │ │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ │ ├─ ⊖ Hue| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ Satuation| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ Brightness| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ Red| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ Green| [1] (0 ~ 1) | 
| │ │ └─ ⊖ Blue| [1] (0 ~ 1) | 
| │ ├─ ⊖ Metallic| [0] (0 ~ 1) | 
| │ ├─ ⊖ Smoothness| [0.95] (0 ~ 1) | 
| │ ├─ ⊖ Glow| [0] (0 ~ 1) | 
| │ └─ ⊖ Transparency| [0.1] (0 ~ 1) | 
| ├─ ⚙️ <b>Particle Properties</b>| | 
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [0] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [0] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [-2] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [-2] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Head| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Body| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Boobs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Butts| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Arms| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Hands| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Legs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─ ☑ Feet| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ Player| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
|  ☑ <b>Geometry Collider</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ □ Visible| [OFF] | 
| ├─ Export Shape|| 
| ├─ ☑ <b>Head</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [-0.05] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.04] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.5] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.08] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.11] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [0.8] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Neck</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.045] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.065] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.045] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Chest</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.08] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.023] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.15] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.05] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.04] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.15] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [0.88] (0 ~ 1) | 
| │ └─ ⊖ Z| [0.7] (0 ~ 1) | 
| ├─ ☑ <b>Ribs</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0.075] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.015] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [-0.015] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.05] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Waist</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.032] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.11] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [-0.3] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.05] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [0.8] (0 ~ 1) | 
| ├─ ☑ <b>Belly</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.013] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.15] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.073] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [0.65] (0 ~ 1) | 
| ├─ ☑ <b>Butts</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0.066] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [-0.0425] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.05] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.105] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0.066] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.012] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.09] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Shoulder</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [-0.02] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.02] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.05] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.4] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Upper Arm</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.053] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.15] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.035] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Lower Arm</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.0445] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.44] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.01] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Hand</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.0315] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [-0.0316] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Hips</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [-0.027] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.1] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.455] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [-0.1] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.085] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Thigh</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.073] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.455] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.05599999] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Shin</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.05926838] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0] (-2 ~ 2) | 
| │ ├─ <b>Position Middle</b>|| 
| │ ├─ ⊖ X| [0.009999919] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0.05999992] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.01666657] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius Middle| [0.06707321] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve Middle| [0] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.03231711] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| ├─ ☑ <b>Foot</b>| | 
| │ ├─ ☑ Enable| [ON] | 
| │ ├─ <b>Position From</b>|| 
| │ ├─ ⊖ X| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [-0.03166673] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0.015] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius From| [0.053] (0 ~ 0.15) | 
| │ ├─ ⊖ Curve| [0.1] (-2 ~ 2) | 
| │ ├─ <b>Position To</b>|| 
| │ ├─ ⊖ X| [0.028] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Y| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Z| [0] (-0.25 ~ 0.25) | 
| │ ├─ ⊖ Radius To| [0.0625] (0 ~ 0.15) | 
| │ ├─ <b>Scale</b>|| 
| │ ├─ ⊖ X| [1] (0 ~ 1) | 
| │ ├─ ⊖ Y| [1] (0 ~ 1) | 
| │ └─ ⊖ Z| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
|  ☑ <b>Mesh Collider</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ ☑ Disable Geometry Colliders| [ON] | 
| ├─ □ Visulize| [OFF] | 
| ├─ ⊖ Depth| [0.025] (0 ~ 0.1) | 
| ├─ ☑ Skip Edge| [ON] | 
| ├─ ☑ Skip Point| [ON] | 
| └─ ☑ Single Collision| [ON] | 
|  ⚙️ <b>Simulation Settings</b>| | 
| ├─ ☑ Enable Dragging| [ON] | 
| ├─ ⊖ Reset Scale| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
| ├─ ☑ Simulate| [ON] | 
| ├─ > Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─ ⊖ Time Scale| [0.65] (0.1 ~ 1) | 
| ├─ ⊖ Substeps| [4] (1 ~ 20) | 
| ├─ ⊖ Iterations| [1] (0 ~ 10) | 
| ├─ □ Reverse Even Substeps| [OFF] | 
| ├─ ⊖ Alternate Group Size| [0] (0 ~ 20) | 
| ├─ ⊖ Table Size| [6] (1 ~ 20) | 
| └─ □ Two Step Solving| [OFF] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
