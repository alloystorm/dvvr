---
locale: en-rUS
layout: single
title: Skirt Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/physics_skirt) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_skirt) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_skirt) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_skirt) | [简中](/zh/dancexr/menu/2025.4/actor/physics_skirt)

[Physics](../menu#Physics) > Skirt Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Particle Dynamics| [ON] | 
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
|  Select Bones|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop| [ON] | Bones for closed loops at each level
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor| [0] (0 ~ 0.5) | 
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
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b>| | 
| ├─ □ Visualize| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.01] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [0.5] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b>| | 
| ├─ □ Visualize| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate| [1] (0 ~ 1) | 
| ├─ □ Lock Y| [OFF] | 
| └─ □ Lock Z| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type| **Box** | Box, Capsule, Sphere,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Additional Groups| [0] (0 ~ 7) | 
|  □ <b>Group 2</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 3</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 4</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 5</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 6</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 7</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
|  □ <b>Group 8</b>| | 
| ├─ □ Enable| [OFF] | 
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
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings| [ON] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
