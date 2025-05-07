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
|  ☑ Gradual Enable| [2] (0 ~ 5) | 
|  ⚙️ **Particle Properties**| | 
| ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| ├─ ⊖ Stickiness| [0] (0 ~ 1) | 
| ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| ├─ ⊖ Friction| [1] (0 ~ 2) | 
| ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| ├─ ⚙️ **Wind**| | 
| │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| ├─ ⚙️ **Collide With**| | 
| │ ├─ ☑ Head| [ON] | 
| │ ├─ ☑ Body| [ON] | 
| │ ├─ ☑ Boobs| [ON] | 
| │ ├─ ☑ Butts| [ON] | 
| │ ├─ ☑ Arms| [ON] | 
| │ ├─ ☑ Hands| [ON] | 
| │ ├─ ☑ Legs| [ON] | 
| │ ├─ ☑ Feet| [ON] | 
| │ └─ ☑ Player| [ON] | 
| ├─ ☑ Enable Bending Constraints| [ON] | 
| ├─ ⊖ Bending Compliance| [0] (0 ~ 1) | 
| ├─ ⊖ Scale| [1] (0 ~ 2) | 
| ├─ □ Self Collision| [OFF] | 
| ├─ ⊖ Grip Mass| [2] (0 ~ 4) | Mass of grip particles
| ├─ ⊖ Grip Friction| [2] (-2 ~ 4) | Friction for grip particles
| ├─ ⊖ Grip Stickiness| [0.25] (0 ~ 1) | Stickiness of grip particles
| ├─ ⊖ Grip Drag| [0] (-2 ~ 2) | Air resistancy for grip particles
| ├─ ⊖ Grip Scale| [1] (0 ~ 2) | 
| ├─ □ Enable Tearing| [OFF] | 
| ├─ ⊖ Tear Threshold| [2] (1 ~ 10) | 
| └─ ⊖ Limit Tearing Speed| [0] (0 ~ 25) | Cool down interval after tearing, in frames
|  ⚙️ **Simulation Settings**| | 
| ├─ ☑ Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
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
