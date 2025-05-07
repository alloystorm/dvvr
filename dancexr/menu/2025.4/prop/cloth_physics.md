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
|  ☑ Enable| [ON] | 
|  Select Bones|| Select bones
|  ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|  ☑ <b>Particle Dynamics</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| ├─ □ Visualize| [OFF] | 
| ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| ├─ ⊖ Friction| [1] (0 ~ 2) | 
| ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| ├─ ⚙️ <b>Wind</b>| | 
| │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| ├─ ⚙️ <b>Collide With</b>| | 
| │ ├─ ☑ Head| [ON] | 
| │ ├─ ☑ Body| [ON] | 
| │ ├─ ☑ Boobs| [ON] | 
| │ ├─ ☑ Butts| [ON] | 
| │ ├─ ☑ Arms| [ON] | 
| │ ├─ ☑ Hands| [ON] | 
| │ ├─ ☑ Legs| [ON] | 
| │ ├─ ☑ Feet| [ON] | 
| │ └─ ☑ Player| [ON] | 
| └─ ⚙️ <b>Simulation Settings</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| <img src="/images/icon/ic_space.png"/>├─ ☑ Enable Dragging| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ Simulate| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ > Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Time Scale| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Substeps| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Iterations| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Reverse Even Substeps| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Alternate Group Size| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─ ⊖ Table Size| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─ □ Two Step Solving| [OFF] | 
|  ⊖ Spring| [0.5] (0 ~ 5) | 
|  ⊖ Damp| [0.01] (0 ~ 0.1) | 
|  ⊖ Reduction Ratio| [0.25] (0 ~ 1) | Reducing stiffness at each level
|  ⊖ Twist Limit| [5] (0 ~ 180) | Limit tiwsting rotation
|  ⊖ Limit Force| [3] (0 ~ 8) | 
|  ⊖ Mass| [0.05] (0 ~ 0.1) | 
|  ⊖ Drag| [1] (0 ~ 10) | 
|  ⊖ Collider Radius| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
|  ⊖ Collider Length| [0.9] (0 ~ 1) | 
|  ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
