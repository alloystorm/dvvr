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
|  ☑ Enable| [ON] | 
|  ☑ Use Particle Dynamics| [ON] | 
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
|  Select Bones|| 
|  > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|  ☑ Closed Loop| [ON] | Bones for closed loops at each level
|  ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|  ⚙️ <b>Particle Dynamics</b>| | 
| ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
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
| └─ ⚙️ <b>Collide With</b>| | 
|  ├─ ☑ Head| [ON] | 
|  ├─ ☑ Body| [ON] | 
|  ├─ ☑ Boobs| [ON] | 
|  ├─ ☑ Butts| [ON] | 
|  ├─ ☑ Arms| [ON] | 
|  ├─ ☑ Hands| [ON] | 
|  ├─ ☑ Legs| [ON] | 
|  ├─ ☑ Feet| [ON] | 
|  └─ ☑ Player| [ON] | 
|  ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| ├─ ⊖ Drag| [0] (0 ~ 10) | 
| ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| ├─ ⊖ Friction| [0] (0 ~ 1) | 
| ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|  ⚙️ <b>Parent-Child Joint</b>| | 
| ├─ □ Visualize| [OFF] | 
| ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|  ⚙️ <b>Lateral Joint</b>| | 
| ├─ □ Visualize| [OFF] | 
| ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| ├─ □ Lock Y| [OFF] | 
| └─ □ Lock Z| [OFF] | 
|  ⚙️ <b>Collider</b>| | 
| ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|  ⊖ Additional Groups| [0] (0 ~ 7) | 
|  □ <b>Group 2</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 3</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 4</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 5</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 6</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 7</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  □ <b>Group 8</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ Select Bones|| 
| ├─ > Sorting| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─ ☑ Closed Loop| [ON] | Bones for closed loops at each level
| ├─ ⊖ Skip First X Bones| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─ ⚙️ <b>Particle Dynamics</b>| | 
| │ ├─ ⊖ Swing Compliance| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ Twist Compliance| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ Particle Anchor| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Ratio| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─ ⊖ Lateral Compliance| [1] (0 ~ 1) | 
| │ ├─ ⊖ Lateral Anchor| [0] (0 ~ 0.5) | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Max Angular Velocity| [2] (0 ~ 4) | 
| │ ├─ ⊖ Inertia| [2] (1 ~ 5) | 
| │ ├─ ⊖ Soften| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─ ⊖ Particle Radius| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─ ⊖ Gravity| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ Friction| [1] (0 ~ 2) | 
| │ ├─ ⊖ Ground Friction| [1] (-2 ~ 2) | 
| │ ├─ ⊖ Drag (Air)| [0] (0 ~ 2) | Air resistancy
| │ ├─ ⊖ Drag (Underwater)| [1] (0 ~ 2) | Underwater resistancy
| │ ├─ ⊖ Buoyancy| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ <b>Wind</b>| | 
| │ │ ├─ ⊖ Wind Influence| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ Turbulence Scale| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ Turbulence Intensity| [1] (0 ~ 2) | 
| │ │ └─ ⊖ Turbulence Time Scale| [0] (-4 ~ 4) | 
| │ └─ ⚙️ <b>Collide With</b>| | 
| │  ├─ ☑ Head| [ON] | 
| │  ├─ ☑ Body| [ON] | 
| │  ├─ ☑ Boobs| [ON] | 
| │  ├─ ☑ Butts| [ON] | 
| │  ├─ ☑ Arms| [ON] | 
| │  ├─ ☑ Hands| [ON] | 
| │  ├─ ☑ Legs| [ON] | 
| │  ├─ ☑ Feet| [ON] | 
| │  └─ ☑ Player| [ON] | 
| ├─ ⚙️ <b>Physics Properties</b>| | Physics properties like mass, drag and friction
| │ ├─ ⊖ Mass| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Drag| [0] (0 ~ 10) | 
| │ ├─ ⊖ Horizontal Overlap| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─ ⊖ Mass Distribution| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─ ⊖ Friction| [0] (0 ~ 1) | 
| │ ├─ ⊖ Solver Iterations| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─ ☑ Center Of Mass| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─ ⚙️ <b>Parent-Child Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Swing Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Twist Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [0.5] (0 ~ 1) | 
| │ └─ ⊖ Anchor Position| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─ ⚙️ <b>Lateral Joint</b>| | 
| │ ├─ □ Visualize| [OFF] | 
| │ ├─ ⊖ Linear Drive| [5] (0 ~ 10) | 
| │ ├─ ⊖ Angular Drive| [0] (0 ~ 10) | 
| │ ├─ ⊖ Drive Damping| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ Reduction Rate| [1] (0 ~ 1) | 
| │ ├─ □ Lock Y| [OFF] | 
| │ └─ □ Lock Z| [OFF] | 
| ├─ ⚙️ <b>Collider</b>| | 
| │ ├─ ⊖ Collider Radius| [0.01] (0 ~ 0.1) | 
| │ ├─ > Collider Type| **Box** | Box, Capsule, Sphere,  |
| │ ├─ ⊖ Collider Length| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─ ⊖ First Collider Length| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─ ☑ Use Primary Group Settings| [ON] | 
|  ≡ Presets| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
