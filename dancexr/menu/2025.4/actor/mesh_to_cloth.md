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
| Combine As One | OFF | 
| Gradual Enable | [2] (0 ~ 5) | 
| **Particle Properties** | | 
| ├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| ├&nbsp;Stickiness | [0] (0 ~ 1) | 
| ├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| ├&nbsp;Friction | [1] (0 ~ 2) | 
| ├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| ├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| ├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| ├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| ├&nbsp;**Wind** | | 
| │&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| ├&nbsp;**Collide With** | | 
| │&nbsp;├&nbsp;Head | ON | 
| │&nbsp;├&nbsp;Body | ON | 
| │&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;└&nbsp;Player | ON | 
| ├&nbsp;Enable Bending Constraints | ON | 
| ├&nbsp;Bending Compliance | [0] (0 ~ 1) | 
| ├&nbsp;Scale | [1] (0 ~ 2) | 
| ├&nbsp;Self Collision | OFF | 
| ├&nbsp;Grip Mass | [2] (0 ~ 4) | Mass of grip particles
| ├&nbsp;Grip Friction | [2] (-2 ~ 4) | Friction for grip particles
| ├&nbsp;Grip Stickiness | [0.25] (0 ~ 1) | Stickiness of grip particles
| ├&nbsp;Grip Drag | [0] (-2 ~ 2) | Air resistancy for grip particles
| ├&nbsp;Grip Scale | [1] (0 ~ 2) | 
| ├&nbsp;Enable Tearing | OFF | 
| ├&nbsp;Tear Threshold | [2] (1 ~ 10) | 
| └&nbsp;Limit Tearing Speed | [0] (0 ~ 25) | Cool down interval after tearing, in frames
| **Simulation Settings** | | 
| ├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| ├&nbsp;Enable Dragging | ON | 
| ├&nbsp;Reset Scale | [1] (1 ~ 5) | Transit from a larger scale for the cloth during reset to help with fitting.
| ├&nbsp;Simulate | ON | 
| ├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| ├&nbsp;Substeps | [4] (1 ~ 20) | 
| ├&nbsp;Iterations | [1] (0 ~ 10) | 
| ├&nbsp;Reverse Even Substeps | OFF | 
| ├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| ├&nbsp;Table Size | [6] (1 ~ 20) | 
| └&nbsp;Two Step Solving | OFF | 
