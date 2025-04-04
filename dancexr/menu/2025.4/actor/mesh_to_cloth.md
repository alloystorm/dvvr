---
locale: en-rUS
layout: single
title: Mesh To Cloth
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[Pro](../menu#Pro) > Mesh To Cloth



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) Combine As One</nobr>| [OFF] | 
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Gradual Enable</nobr>| [2] (0 ~ 5) | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Particle Properties</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Stickiness</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Bending Constraints</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Bending Compliance</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Self Collision</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Grip Scale</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable Tearing</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Tear Threshold</nobr>| [2] (1 ~ 10) | 
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Simulation Settings</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
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
