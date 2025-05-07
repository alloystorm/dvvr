---
locale: en-rUS
layout: single
title: Dangling Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/stage/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/stage/cloth_physics)

[Stage](../menu#Stage) > Dangling Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|  Select Bones</nobr>|| Select bones
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Particle Dynamics</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
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
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps</nobr>| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations</nobr>| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Reverse Even Substeps</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size</nobr>| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size</nobr>| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Two Step Solving</nobr>| [OFF] | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring</nobr>| [0.5] (0 ~ 5) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Damp</nobr>| [0.01] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0.25] (0 ~ 1) | Reducing stiffness at each level
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Limit</nobr>| [5] (0 ~ 180) | Limit tiwsting rotation
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Force</nobr>| [3] (0 ~ 8) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.05] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.9] (0 ~ 1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
