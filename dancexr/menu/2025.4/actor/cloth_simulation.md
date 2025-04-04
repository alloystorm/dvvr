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
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr> Reset</nobr>|| 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Cloth 1</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Top Anchor</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Bottom Anchor</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C1 Material</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b></nobr>|| 
|<nobr>├&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Double Side</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Blend Mode</nobr>| **Blend** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Toon Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Special Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Detail Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Hexagon Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Cloth 2</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Top Anchor</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Bottom Anchor</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C2 Material</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>Surface</b></nobr>|| 
|<nobr>├&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Double Side</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Blend Mode</nobr>| **Multiply** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Toon Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Special Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Detail Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Hexagon Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Combine</nobr>| [OFF] | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Fluid (Experimental)</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Spawn</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Position</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [2.5] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Rotation</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spawn Radius</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spread</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spawn Rate</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Speed</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Mouse / Hand Control</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Auto Aim</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max TTL</nobr>| [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> TTL on Floor</nobr>| [0.1] (0 ~ 1) | Time to live after hitting floor.
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Smoothing</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Fluid</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cohesion</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Viscosity</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stick To Surface</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Density</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cohesion Range</nobr>| [20] (1 ~ 50) | Max distance for cohesion effect
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Distance</nobr>| [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Elevation</nobr>| [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Water** | Water, Viscous, Sand,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Render</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Render Particle</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Render Droplet</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Droplet Size</nobr>| [2] (0 ~ 50) | Droplet size in MM
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale By Density</nobr>| [0] (0 ~ 5) | Scale droplet size by density of the fluid
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Smoothness</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Transparency</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [-2] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [-2] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Player</nobr>| [OFF] | 
|<nobr>└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset),  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Geometry Collider</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visible</nobr>| [OFF] | 
|<nobr>├&nbsp; Export Shape</nobr>|| 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Head</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Neck</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Chest</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Ribs</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Waist</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Belly</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Butts</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shoulder</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Upper Arm</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Lower Arm</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Hand</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Hips</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Thigh</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shin</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position Middle</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius Middle</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve Middle</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Foot</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Radius To</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;<img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Mesh Collider</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Disable Geometry Colliders</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visulize</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Skip Edge</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Skip Point</nobr>| [ON] | 
|<nobr>└&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Single Collision</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b></nobr>| | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reset Scale</nobr>| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
|<nobr>├&nbsp;<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate</nobr>| [ON] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Two Step Solving</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset),  |
