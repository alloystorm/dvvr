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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| ├─ □ Reverse Even Substeps| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| └─ □ Two Step Solving| [OFF] | 
|  <b>Primary Group</b>|| 
|  Select Bones|| Select bones
|  □ Anchor Along Axis| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| ├─ <b>Joints</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
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
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ ├─ □ Body| [OFF] | 
| │ ├─ □ Boobs| [OFF] | 
| │ ├─ □ Butts| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ ├─ □ Legs| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Additional Groups| [0] (0 ~ 7) | 
|  □ <b>Group 2</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 3</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 4</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 5</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 6</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 7</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|  □ <b>Group 8</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| Select bones
| ├─ □ Anchor Along Axis| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>Joints</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ Visualize| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Body| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Boobs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Butts| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ Legs| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
