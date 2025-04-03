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
|<nobr>Enable</nobr>| [ON] | 
|<nobr>Reset</nobr>|| 
|<nobr>**Cloth 1**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;**Anchor**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;**Top Anchor**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Positoin</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Rotation</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;**Bottom Anchor**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Positoin</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Rotation</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;**Particle Properties**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;Presets</nobr>| **Top** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr>**C1 Material**</nobr>| | 
|<nobr>├&nbsp;Surface</nobr>|| 
|<nobr>├&nbsp;Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;Double Side</nobr>| [OFF] | 
|<nobr>├&nbsp;Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blend Mode</nobr>| **Blend** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;**Toon Shader**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;**Special Shader**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;**Detail Map**</nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;**Hexagon Map**</nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr>**Cloth 2**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Rebuild Mesh</nobr>|| Most parameters here requires rebuilding the mesh to take effect.
|<nobr>├&nbsp;Topology</nobr>| **Horizontal Layout** | Adaptive Hexagon, Adaptive Rectangle, Horizontal Layout, Horizontal Strings, Vertical Layout, Vertical Strings,  |
|<nobr>├&nbsp;String Connection</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;Inner Radius</nobr>| [0.08] (0 ~ 0.2) | Radius of inner circle in meters
|<nobr>├&nbsp;Slope</nobr>| [45] (0 ~ 90) | Angle to expand the mesh along the length. 0 = tube, 90 = flat circle.
|<nobr>├&nbsp;Arc</nobr>| [0] (-1 ~ 1) | Arc outwards or inwards along the length. Positive = balloon shape, Negative = bell shape
|<nobr>├&nbsp;Length</nobr>| [0.25] (0 ~ 0.75) | Length in meters
|<nobr>├&nbsp;Arm Holes</nobr>| [0.5] (0 ~ 1) | Size of arm holes in relation to circumference
|<nobr>├&nbsp;Arm Hole Height</nobr>| [0.25] (0 ~ 1) | Height of arm holes in relation to total length
|<nobr>├&nbsp;Back Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;Side Length</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;Horizontal Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;Vertical Resolution</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;Distance Compliance</nobr>| [0] (0 ~ 0.1) | Compliance of distance constraints between particles
|<nobr>├&nbsp;UV Mapping</nobr>| **Mirror Scaled** | Circular, Mirror Scaled, Mirror Actual, Wrap Scaled, Wrap Actual,  |
|<nobr>├&nbsp;**Anchor**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Top Layers</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;**Top Anchor**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Bone</nobr>| **Torso** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Positoin</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Anchor Rotation</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Bottom Layers</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;**Bottom Anchor**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Selection</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Selection Offset</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Bone</nobr>| **Waist** | Waist, Torso, Hip, Head, Thighs, Shins, Upper Arms, Lower Arms, Hands, Boobs,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Swap Side</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Lock Mode</nobr>| **None** | None, Lock, Lock Height, Sticky,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Positoin</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;X</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Y</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Z</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Anchor Rotation</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;X</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Y</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Z</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;**Particle Properties**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Enable Bending Constraints</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Self Collision</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>│&nbsp;├&nbsp;Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>│&nbsp;├&nbsp;Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>│&nbsp;├&nbsp;Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>│&nbsp;├&nbsp;Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Enable Tearing</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>└&nbsp;Presets</nobr>| **Skirt** | Skirt, Top, Tight Skirt, String Skirt, Hula Skirt,  |
|<nobr>**C2 Material**</nobr>| | 
|<nobr>├&nbsp;Surface</nobr>|| 
|<nobr>├&nbsp;Presets</nobr>| **Matt Gray** | Original, Matt Gray, Translucent, Glow, Silver, Solid Glass, Thin Glass, Outline, Preset 1, Preset 2, Preset 3,  |
|<nobr>├&nbsp;Glass Mode</nobr>| [OFF] | 
|<nobr>├&nbsp;Alpha As Gloss</nobr>| [OFF] | 
|<nobr>├&nbsp;Double Side</nobr>| [ON] | 
|<nobr>├&nbsp;Dim Back</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Cast Shadow</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Depth Prepass</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;Gloss</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Bump</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;Glow</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;Ambient</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Alpha</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Clip</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blend Mode</nobr>| **Multiply** | Original, Multiply, Blend, Color Shift,  |
|<nobr>│&nbsp;├&nbsp;Blend</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Gray** | Original, White, Black, Red, Yellow, Dark Gray, Blue, Skin, Gray, Orange,  |
|<nobr>├&nbsp;**Toon Shader**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Shading</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Outline</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Specular</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Specular</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Highlight Area</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Highlight</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Ambient</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Shadow Area</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Shadow</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Soft Shadow</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Sharp** | Sharp, Soft, Bright, Flat + Specular, Flat,  |
|<nobr>├&nbsp;**Special Shader**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| **Off** | Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment,  |
|<nobr>│&nbsp;├&nbsp;Refraction</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;Thickness</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Texture</nobr>| **[Solid Color]** | [Solid Color], [Wood1], [Wood2], [Tiles], [Concrete], [Video],  |
|<nobr>└&nbsp;**Detail Map**</nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;**Hexagon Map**</nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Density</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Size</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Bump</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Noise</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;Use Circle</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;Soft Edge</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Select Map</nobr>| **Fabric 3** | Carbon Fiber, Leather, Fabric 1, Fabric 2, Fabric 3, Wool 1, Wool 2, Metal Satin, Metal Brushed, Hair,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Rotation</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Scale</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Detail Map Bump</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect AO</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Smoothness</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Affect Color Blend</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Anisotropy</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIP Map Bias</nobr>| [0] (-5 ~ 5) | Adjust sharpness of detail texture.
|<nobr>Combine</nobr>| [OFF] | Combine Cloth 1 and 2 as a single simulation, this allows collision between the 2 but will be slower.
|<nobr>**Fluid (Experimental)**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;**Spawn**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;**Position**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [2.5] (Unlimited) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z</nobr>| [0] (Unlimited) | 
|<nobr>│&nbsp;├&nbsp;**Rotation**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;Spawn Radius</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Spread</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Spawn Rate</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;Speed</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Mouse / Hand Control</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Auto Aim</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Max TTL</nobr>| [10] (5 ~ 15) | Particles disappear and respawn after this amount of time.
|<nobr>│&nbsp;├&nbsp;TTL on Floor</nobr>| [0.1] (0 ~ 1) | Time to live after hitting floor.
|<nobr>│&nbsp;├&nbsp;Smoothing</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Sprinkler** | Shower, Fountain, Sprinkler, Handheld,  |
|<nobr>├&nbsp;**Fluid**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Cohesion</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Viscosity</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Stick To Surface</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Target Density</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Cohesion Range</nobr>| [20] (1 ~ 50) | Max distance for cohesion effect
|<nobr>│&nbsp;├&nbsp;Target Distance</nobr>| [10] (1 ~ 20) | Minimum distance between particles in MM when cohesion is off.
|<nobr>│&nbsp;├&nbsp;Elevation</nobr>| [0.25] (0 ~ 0.5) | Elevate particle in proportion of its size
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Water** | Water, Viscous, Sand,  |
|<nobr>├&nbsp;**Render**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Render Particle</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Render Droplet</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Droplet Size</nobr>| [2] (0 ~ 50) | Droplet size in MM
|<nobr>│&nbsp;├&nbsp;Scale By Density</nobr>| [0] (0 ~ 5) | Scale droplet size by density of the fluid
|<nobr>│&nbsp;├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Metallic</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Smoothness</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Glow</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Transparency</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;**Particle Properties**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [-2] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [-2] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [OFF] | 
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset),  |
|<nobr>**Geometry Collider**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Visible</nobr>| [OFF] | 
|<nobr>├&nbsp;Export Shape</nobr>|| 
|<nobr>├&nbsp;**Head**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Neck**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Chest**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;**Ribs**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Waist**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;**Belly**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;**Butts**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Shoulder**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Upper Arm**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Lower Arm**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Hand**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Hips**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Thigh**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Shin**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position Middle</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius Middle</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve Middle</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**Foot**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Position From</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius From</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Curve</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Position To</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Z</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;Radius To</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;Scale</nobr>|| 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, Preset 4, Preset 5,  |
|<nobr>**Mesh Collider**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Disable Geometry Colliders</nobr>| [ON] | 
|<nobr>├&nbsp;Visulize</nobr>| [OFF] | 
|<nobr>├&nbsp;Depth</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;Skip Edge</nobr>| [ON] | 
|<nobr>├&nbsp;Skip Point</nobr>| [ON] | 
|<nobr>└&nbsp;Single Collision</nobr>| [ON] | 
|<nobr>**Simulation Settings**</nobr>| | 
|<nobr>├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>├&nbsp;Reset Scale</nobr>| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
|<nobr>├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>Presets</nobr>| **Default (Reset)** | Default (Reset),  |
