---
locale: en-rUS
layout: single
title: Softbody Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/physics_softbody) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_softbody) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_softbody) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_softbody) | [简中](/zh/dancexr/menu/2025.4/actor/physics_softbody)

[Physics](../menu#Physics) > Softbody Physics



[Feature Page](/dancexr/features/physics_softbody)

| Setting | Value | Description |
| :--- | --- | :--- |
|  ☑ Enable| [ON] | 
|  ⚙️ <b>Simulation Settings</b>| | 
| ├─ ☑ Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| ├─ ☑ Enable Dragging| [ON] | 
| ├─ ☑ Simulate| [ON] | 
| ├─ > Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─ ⊖ Time Scale| [0.65] (0.1 ~ 1) | 
| ├─ ⊖ Substeps| [4] (1 ~ 20) | 
| ├─ ⊖ Iterations| [1] (0 ~ 10) | 
| ├─ □ Reverse Even Substeps| [OFF] | 
| ├─ ⊖ Alternate Group Size| [0] (0 ~ 20) | 
| ├─ ⊖ Table Size| [6] (1 ~ 20) | 
| └─ □ Two Step Solving| [OFF] | 
|  <b>Primary Group</b>|| 
|  Select Bones|| Select bones
|  □ Anchor Along Axis| [OFF] | 
|  ⚙️ <b>Anchor Offset</b>| | 
| ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
|  ⚙️ <b>Particle Dynamics</b>| | 
| ├─ <b>Joints</b>|| 
| ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
| ├─ ☑ Include Center| [ON] | 
| ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
| ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
| ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
| ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
| ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
| ├─ ⊖ Damping| [15] (0 ~ 40) | 
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
| │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
| │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| ├─ ⚙️ <b>Collide With</b>| | 
| │ ├─ ☑ Head| [ON] | 
| │ ├─ □ Body| [OFF] | 
| │ ├─ □ Boobs| [OFF] | 
| │ ├─ □ Butts| [OFF] | 
| │ ├─ ☑ Arms| [ON] | 
| │ ├─ ☑ Hands| [ON] | 
| │ ├─ □ Legs| [OFF] | 
| │ ├─ ☑ Feet| [ON] | 
| │ └─ ☑ Player| [ON] | 
| └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  ⊖ Additional Groups| [0] (0 ~ 7) | 
|  □ <b>Group 2</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 3</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 4</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 5</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 6</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 7</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 8</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─ ⚙️ <b>Anchor Offset</b>| | 
| │ ├─ ⊖ X| [0] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ Y| [0] (-0.2 ~ 0.2) | 
| │ └─ ⊖ Z| [0] (-0.2 ~ 0.2) | 
| ├─ ☑ Use Primary Group Settings| [ON] | 
| └─ ⚙️ <b>Particle Dynamics</b>| | 
|  ├─ <b>Joints</b>|| 
|  ├─ ⊖ Depth| [0.4] (0 ~ 1) | 
|  ├─ ☑ Include Center| [ON] | 
|  ├─ ☑ Volume Constraint| [0.85] (0.5 ~ 1) | 
|  ├─ ⊖ Internal Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ⊖ Surface Constraint| [0.75] (0.5 ~ 1) | 
|  ├─ ⊖ Rotation Constraint| [0.65] (0.5 ~ 1) | 
|  ├─ ☑ Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|  ├─ ⊖ Center Lock| [1] (0.5 ~ 1) | 
|  ├─ ⊖ Damping| [15] (0 ~ 40) | 
|  ├─ □ Visualize| [OFF] | 
|  ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
|  ├─ ⊖ Inertia| [2] (1 ~ 5) | 
|  ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
|  ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
|  ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
|  ├─ ⊖ Friction| [1] (0 ~ 2) | 
|  ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
|  ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
|  ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
|  ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
|  ├─ ⚙️ <b>Wind</b>| | 
|  │ ├─ ⊖ Wind Influence| [0] (0 ~ 1) | 
|  │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
|  │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
|  │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
|  ├─ ⚙️ <b>Collide With</b>| | 
|  │ ├─ ☑ Head| [ON] | 
|  │ ├─ □ Body| [OFF] | 
|  │ ├─ □ Boobs| [OFF] | 
|  │ ├─ □ Butts| [OFF] | 
|  │ ├─ ☑ Arms| [ON] | 
|  │ ├─ ☑ Hands| [ON] | 
|  │ ├─ □ Legs| [OFF] | 
|  │ ├─ ☑ Feet| [ON] | 
|  │ └─ ☑ Player| [ON] | 
|  └─ ≡ Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  ≡ Presets| **Default (Reset)** | Default (Reset),  |
