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
|  □ Combine As One| [OFF] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Gradual Enable| [2] (0 ~ 5) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Properties</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stickiness| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Bending Constraints| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bending Compliance| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale| [1] (0 ~ 2) | 
| ├─ □ Self Collision| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Grip Scale| [1] (0 ~ 2) | 
| ├─ □ Enable Tearing| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Tear Threshold| [2] (1 ~ 10) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
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
