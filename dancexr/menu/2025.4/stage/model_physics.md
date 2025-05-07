---
locale: en-rUS
layout: single
title: Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/model_physics) | [简中](/zh/dancexr/menu/2025.4/stage/model_physics)

[Stage](../menu#Stage) > Physics



| Setting | Value | Description |
| :--- | --- | :--- |
|  □ Disable PMX Physics| [OFF] | Disable PMX physics to use XPS tools instead
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Reduced Constraints| [ON] | Use the experimental setup that reduces constraints to allow smoother simulation
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collision</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Static Inclusive| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Static Exclusive| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Dynamic Inclusive| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Dynamic Exclusive| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Linear Movement</b>| | Settings for linear movements
| ├─ ☑ Restriction| Auto | Auto, Limited, Locked, Free, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Lock 0 Limit| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Min Spring Force| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Limit| [0.05] (0.05 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bonciness| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Contact Distance| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Angular Movement</b>| | Settings for angular movements
| ├─ ☑ Restriction| Auto | Auto, Limited, Locked, Free, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Lock 0 Limit| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Min Spring Force| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Limit| [90] (3 ~ 90) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bonciness| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Contact Distance| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Linear Drive</b>| | Apply linear drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring Force| [3] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Angular Drive</b>| | Apply angular drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring Force| [0.1] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Linear Motion</b>| | Settings for linear motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Firmness| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Main Drive Force| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Second Drive Force| [3] (0 ~ 8) | 
| ├─ ☑ Target Position| Zero | Zero, Center, Min, Max, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Lock When Possible| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Acceleration Mode| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0.15] (0 ~ 1) | 
| └─ □ Ignore Limit| [OFF] | Further reducing constraints by ignoring joint limits
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Angular Motion</b>| | Settings for angular motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Firmness| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Main Drive Force| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Second Drive Force| [5] (0 ~ 8) | 
| ├─ ☑ Target Position| Zero | Zero, Center, Min, Max, 
| ├─ □ Lock When Possible| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Acceleration Mode| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0.15] (0 ~ 1) | 
| └─ □ Ignore Limit| [OFF] | Further reducing constraints by ignoring joint limits
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Options</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Min Drag| [0] (0 ~ 1) | The min drag value in auto mode
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag Scale| [1] (0 ~ 5) | The scale applied to drag values in auto mode
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Min Mass| [0] (0 ~ 1) | The min mass value in auto mode
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Scale| [1] (0 ~ 10) | The scale applied to mass values in auto mode
| ├─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Projection Dist| [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Projection Angle| [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Auto Reset Threshold| [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Auto Reset</b>| | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Threshold| [30] (0 ~ 50) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Body Colliders</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Head Radius| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Arm Radius| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Forearms| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Chest Width| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Waist Width| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hips Width| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Butts Radius| [1] (0 ~ 2) | 
| ├─ <b>Butts Position</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Belly Radius| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Belly Position| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Leg Radius| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thigh Fwd/Back| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Thigh Start Position| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hand| [0] (0 ~ 1) | 
| ├─ □ Visualize| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), amy, misaki,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Boobs Physics</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ Select Bones|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring Force| [1.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Counter Gravity| [10] (0 ~ 45) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Rotation Limit</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Up Limit| [100] (0 ~ 120) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Down Limit| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Left / Right Limit| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring Force| [1.25] (0 ~ 10) | Spring force when exceeding limit
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Contact Distance| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bounce| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [-0.03] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.03] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.08] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Center</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [0.02] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [-0.05] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.025] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collision</b>| | 
| │ ├─ □ Collide With Arms| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.07] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Curve| [2] (-2 ~ 2) | Works with cloth simulation.
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Nipple| [ON] | Works with cloth simulation.
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Nipple Position</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X| [-0.18] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y| [0.09] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Z| [0.2] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Nipple Size| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Softbody</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ <b>Joints</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth| [0.4] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint| [0.85] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint| [0.75] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock| [0.85] (0.5 ~ 1) | Lock particles on the edge.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock| [1] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping| [15] (0 ~ 40) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ ├─ □ Body| [OFF] | 
| │ │ ├─ □ Boobs| [OFF] | 
| │ │ ├─ □ Butts| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ ├─ □ Legs| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| │ │ ├─ □ Reverse Even Substeps| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| │ │ └─ □ Two Step Solving| [OFF] | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
| ├─ □ Softbody Only| [OFF] | Disable physics joint and use softbody particles only.
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, tina, 预设1, 预设2,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Skirt Physics</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Particle Dynamics| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| │ ├─ □ Reverse Even Substeps| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| │ └─ □ Two Step Solving| [OFF] | 
| ├─ <b>Primary Group</b>|| 
| ├─ Select Bones|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Additional Groups| [0] (0 ~ 7) | 
| ├─ □ <b>Group 2</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 3</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 4</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 5</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 6</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 7</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| ├─ □ <b>Group 8</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ Select Bones|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| │ │ ├─ □ Visualize| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| │ │ ├─ □ Lock Y| [OFF] | 
| │ │ └─ □ Lock Z| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Hair Physics</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ Select Bones|| Select bones
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Particle Dynamics</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| │ <img src="/images/icon/ic_space.png"/>├─ □ Reverse Even Substeps| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ Two Step Solving| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring| [1.25] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damp| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Limit| [5] (0 ~ 180) | Limit tiwsting rotation
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Force| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), momiji bob, Preset 1,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Dangling Physics</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ Select Bones|| Select bones
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Particle Dynamics</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ □ Visualize| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global| [ON] | Find the global settings under Pro / Cloth Simulation
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale| [0.65] (0.1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps| [4] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations| [1] (0 ~ 10) | 
| │ <img src="/images/icon/ic_space.png"/>├─ □ Reverse Even Substeps| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size| [0] (0 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size| [6] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ Two Step Solving| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spring| [0.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damp| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Limit| [5] (0 ~ 180) | Limit tiwsting rotation
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Limit Force| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.05] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Detach Object</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─ Select Bones|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Gravity| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Damp| [0] (0 ~ 1) | 
| ├─ ☑ Collider| Sphere | None, Sphere, Capsule, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.3] (0 ~ 2) | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset),  |
