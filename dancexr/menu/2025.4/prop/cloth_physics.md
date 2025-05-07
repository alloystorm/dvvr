---
locale: en-rUS
layout: single
title: Dangling Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[Prop](../menu#Prop) > Dangling Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
|  Select Bones|| Select bones
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Particle Dynamics</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| ├─ □ Visualize| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
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
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Reverse Even Substeps| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─ □ Two Step Solving| [OFF] | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring| [0.5] (0 ~ 5) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Damp| [0.01] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0.25] (0 ~ 1) | Reducing stiffness at each level
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Limit| [5] (0 ~ 180) | Limit tiwsting rotation
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Force| [3] (0 ~ 8) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.05] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.9] (0 ~ 1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
