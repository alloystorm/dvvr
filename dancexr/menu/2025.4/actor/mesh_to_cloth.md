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
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> Combine As One</nobr>| [OFF] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Gradual Enable</nobr>| [2] (0 ~ 5) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b></nobr>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness</nobr>| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance</nobr>| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale</nobr>| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Self Collision</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass</nobr>| [2] (0 ~ 4) | Mass of grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction</nobr>| [2] (-2 ~ 4) | Friction for grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness</nobr>| [0.25] (0 ~ 1) | Stickiness of grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag</nobr>| [0] (-2 ~ 2) | Air resistancy for grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale</nobr>| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable Tearing</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold</nobr>| [2] (1 ~ 10) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed</nobr>| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reset Scale</nobr>| [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps</nobr>| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations</nobr>| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Reverse Even Substeps</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size</nobr>| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size</nobr>| [6] (1 ~ 20) | 
| └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Two Step Solving</nobr>| [OFF] | 
