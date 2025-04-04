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
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr> Reset</nobr>|| 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Cloth 1</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Top Anchor</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Bottom Anchor</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>C1 Material</b></nobr>| | 
|<nobr>├&nbsp;![texture icon](/images/icon/ic_texture.png) <b>Surface</b></nobr>|| 
|<nobr>├&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Double Side</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Blend Mode</nobr>| **Blend** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Toon Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Special Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Detail Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Hexagon Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Cloth 2</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Top Anchor</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Bottom Anchor</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Positoin</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>Anchor Rotation</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>C2 Material</b></nobr>| | 
|<nobr>├&nbsp;![texture icon](/images/icon/ic_texture.png) <b>Surface</b></nobr>|| 
|<nobr>├&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Double Side</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Blend Mode</nobr>| **Multiply** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Toon Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Special Shader</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Detail Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Hexagon Map</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr>![check_off icon](/images/icon/ic_check_off.png) Combine</nobr>| [OFF] | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Fluid (Experimental)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Spawn</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Position</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [2.5] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Rotation</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Spawn Radius</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Spread</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Spawn Rate</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Speed</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Mouse / Hand Control</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Auto Aim</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max TTL</nobr>| [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) TTL on Floor</nobr>| [0.1] (0 ~ 1) | Time to live after hitting floor.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Smoothing</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Fluid</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Cohesion</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Viscosity</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Stick To Surface</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Target Density</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Cohesion Range</nobr>| [20] (1 ~ 50) | Max distance for cohesion effect
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Target Distance</nobr>| [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Elevation</nobr>| [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Water** | Water, Viscous, Sand,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Render</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Render Particle</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Render Droplet</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Droplet Size</nobr>| [2] (0 ~ 50) | Droplet size in MM
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Scale By Density</nobr>| [0] (0 ~ 5) | Scale droplet size by density of the fluid
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Smoothness</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Glow</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Transparency</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Properties</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [-2] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [-2] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Player</nobr>| [OFF] | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset),  |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>Geometry Collider</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visible</nobr>| [OFF] | 
|<nobr>├&nbsp; Export Shape</nobr>|| 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Head</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Neck</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Chest</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Ribs</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Waist</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Belly</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Butts</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shoulder</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Upper Arm</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Lower Arm</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Hand</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Hips</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Thigh</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shin</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position Middle</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius Middle</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve Middle</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Foot</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>Position From</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>Position To</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Radius To</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>Scale</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>Mesh Collider</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Disable Geometry Colliders</nobr>| [ON] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visulize</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Skip Edge</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Skip Point</nobr>| [ON] | 
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Single Collision</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Simulation Settings</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Dragging</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Reset Scale</nobr>| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Simulate</nobr>| [ON] | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Two Step Solving</nobr>| [OFF] | 
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset),  |
