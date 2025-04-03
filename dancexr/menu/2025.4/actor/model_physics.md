---
locale: en-rUS
layout: single
title: Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/model_physics) | [繁中](/tw/dancexr/menu/2025.4/actor/model_physics) | [日本語](/jp/dancexr/menu/2025.4/actor/model_physics) | [한국어](/kr/dancexr/menu/2025.4/actor/model_physics) | [简中](/zh/dancexr/menu/2025.4/actor/model_physics)

[Actor](../menu#Actor) > Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| Disable PMX Physics | OFF | Disable PMX physics to use XPS tools instead
| Reduced Constraints | ON | Use the experimental setup that reduces constraints to allow smoother simulation
| **Collision** | | 
| ├&nbsp;Static Inclusive | ON | 
| ├&nbsp;Static Exclusive | ON | 
| ├&nbsp;Dynamic Inclusive | ON | 
| └&nbsp;Dynamic Exclusive | ON | 
| **Linear Movement** | | Settings for linear movements
| ├&nbsp;Restriction | Auto | Auto, Limited, Locked, Free, 
| ├&nbsp;Lock 0 Limit | ON | 
| ├&nbsp;Min Spring Force | [5] (0 ~ 15) | 
| ├&nbsp;Max Limit | [0.05] (0.05 ~ 0.1) | 
| ├&nbsp;Bonciness | [0.5] (0 ~ 1) | 
| ├&nbsp;Contact Distance | [0.5] (0 ~ 1) | 
| ├&nbsp;Damping | [0.05] (0 ~ 1) | 
| └&nbsp;Drag | [0.15] (0 ~ 1) | 
| **Angular Movement** | | Settings for angular movements
| ├&nbsp;Restriction | Auto | Auto, Limited, Locked, Free, 
| ├&nbsp;Lock 0 Limit | ON | 
| ├&nbsp;Min Spring Force | [5] (0 ~ 15) | 
| ├&nbsp;Max Limit | [90] (3 ~ 90) | 
| ├&nbsp;Bonciness | [0.5] (0 ~ 1) | 
| ├&nbsp;Contact Distance | [0.5] (0 ~ 1) | 
| ├&nbsp;Damping | [0.05] (0 ~ 1) | 
| └&nbsp;Drag | [0.15] (0 ~ 1) | 
| **Linear Drive** | | Apply linear drive
| ├&nbsp;Enable | ON | 
| ├&nbsp;Spring Force | [3] (0 ~ 5) | 
| └&nbsp;Damping | [0.1] (0 ~ 1) | 
| **Angular Drive** | | Apply angular drive
| ├&nbsp;Enable | ON | 
| ├&nbsp;Spring Force | [0.1] (0 ~ 5) | 
| └&nbsp;Damping | [0.1] (0 ~ 1) | 
| **Linear Motion** | | Settings for linear motion
| ├&nbsp;Firmness | [0] (-1 ~ 1) | 
| ├&nbsp;Main Drive Force | [5] (0 ~ 8) | 
| ├&nbsp;Second Drive Force | [3] (0 ~ 8) | 
| ├&nbsp;Target Position | Zero | Zero, Center, Min, Max, 
| ├&nbsp;Lock When Possible | ON | 
| ├&nbsp;Acceleration Mode | ON | 
| ├&nbsp;Damping | [0.05] (0 ~ 1) | 
| ├&nbsp;Drag | [0.15] (0 ~ 1) | 
| └&nbsp;Ignore Limit | OFF | Further reducing constraints by ignoring joint limits
| **Angular Motion** | | Settings for angular motion
| ├&nbsp;Firmness | [0] (-1 ~ 1) | 
| ├&nbsp;Main Drive Force | [5] (0 ~ 8) | 
| ├&nbsp;Second Drive Force | [5] (0 ~ 8) | 
| ├&nbsp;Target Position | Zero | Zero, Center, Min, Max, 
| ├&nbsp;Lock When Possible | OFF | 
| ├&nbsp;Acceleration Mode | ON | 
| ├&nbsp;Damping | [0.05] (0 ~ 1) | 
| ├&nbsp;Drag | [0.15] (0 ~ 1) | 
| └&nbsp;Ignore Limit | OFF | Further reducing constraints by ignoring joint limits
| **Options** | | 
| ├&nbsp;Min Drag | [0] (0 ~ 1) | The min drag value in auto mode
| ├&nbsp;Drag Scale | [1] (0 ~ 5) | The scale applied to drag values in auto mode
| ├&nbsp;Min Mass | [0] (0 ~ 1) | The min mass value in auto mode
| ├&nbsp;Mass Scale | [1] (0 ~ 10) | The scale applied to mass values in auto mode
| ├&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├&nbsp;Projection Dist | [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value
| └&nbsp;Projection Angle | [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value
| Auto Reset Threshold | [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value
| **Auto Reset** | | 
| └&nbsp;Threshold | [30] (0 ~ 50) | 
| **Body Colliders** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Size | [0.5] (0 ~ 1) | 
| ├&nbsp;Head Radius | [1] (0 ~ 2) | 
| ├&nbsp;Arm Radius | [1] (0 ~ 2) | 
| ├&nbsp;Forearms | [1] (0 ~ 2) | 
| ├&nbsp;Chest Width | [1] (0 ~ 2) | 
| ├&nbsp;Waist Width | [0.5] (0 ~ 1) | 
| ├&nbsp;Hips Width | [0] (-1 ~ 1) | 
| ├&nbsp;Butts Radius | [1] (0 ~ 2) | 
| ├&nbsp;Butts Position || 
| ├&nbsp;X | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;Y | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;Z | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;Belly Radius | [1] (0 ~ 2) | 
| ├&nbsp;Belly Position | [0] (-1 ~ 1) | 
| ├&nbsp;Leg Radius | [1] (0 ~ 2) | 
| ├&nbsp;Thigh Fwd/Back | [0] (-1 ~ 1) | 
| ├&nbsp;Thigh Start Position | [0] (0 ~ 1) | 
| ├&nbsp;Hand | [0] (0 ~ 1) | 
| ├&nbsp;Visualize | OFF | 
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), amy, misaki,  |
| **Boobs Physics**<sup>[PRO]</sup> | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Select Bones || 
| ├&nbsp;Spring Force | [1.5] (0 ~ 5) | 
| ├&nbsp;Damping | [0.1] (0 ~ 1) | 
| ├&nbsp;Mass | [0.1] (0 ~ 1) | 
| ├&nbsp;Drag | [0.1] (0 ~ 10) | 
| ├&nbsp;Counter Gravity | [10] (0 ~ 45) | 
| ├&nbsp;**Rotation Limit** | | 
| │&nbsp;├&nbsp;Up Limit | [100] (0 ~ 120) | 
| │&nbsp;├&nbsp;Down Limit | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;Left / Right Limit | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;Spring Force | [1.25] (0 ~ 10) | Spring force when exceeding limit
| │&nbsp;├&nbsp;Damping | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Contact Distance | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;Bounce | [0.2] (0 ~ 1) | 
| ├&nbsp;**Anchor** | | 
| │&nbsp;├&nbsp;X | [-0.03] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;Y | [0.03] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;Z | [0.08] (-0.2 ~ 0.2) | 
| ├&nbsp;**Center** | | 
| │&nbsp;├&nbsp;X | [0.02] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;Y | [-0.05] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;Z | [0.025] (-0.2 ~ 0.2) | 
| ├&nbsp;**Collision** | | 
| │&nbsp;├&nbsp;Collide With Arms | OFF | 
| │&nbsp;├&nbsp;Collider Radius | [0.07] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;Collider Length | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;Collider Curve | [2] (-2 ~ 2) | Works with cloth simulation.
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Enable Nipple | ON | Works with cloth simulation.
| │&nbsp;├&nbsp;**Nipple Position** | | 
| │&nbsp;│&nbsp;├&nbsp;X | [-0.18] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y | [0.09] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Z | [0.2] (0 ~ 1) | 
| │&nbsp;└&nbsp;Nipple Size | [0.1] (0 ~ 1) | 
| ├&nbsp;**Softbody** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Joints || 
| │&nbsp;├&nbsp;Depth | [0.4] (0 ~ 1) | 
| │&nbsp;├&nbsp;Include Center | ON | 
| │&nbsp;├&nbsp;Volume Constraint | [0.85] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;Internal Constraint | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;Surface Constraint | [0.75] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;Rotation Constraint | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;Edge Lock | [0.85] (0.5 ~ 1) | Lock particles on the edge.
| │&nbsp;├&nbsp;Center Lock | [1] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;Damping | [15] (0 ~ 40) | 
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;├&nbsp;Body | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Boobs | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Butts | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;├&nbsp;Legs | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Simulation Settings** | | 
| │&nbsp;│&nbsp;├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| │&nbsp;│&nbsp;├&nbsp;Enable Dragging | ON | 
| │&nbsp;│&nbsp;├&nbsp;Simulate | ON | 
| │&nbsp;│&nbsp;├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;│&nbsp;│&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │&nbsp;│&nbsp;├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Substeps | [4] (1 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;Iterations | [1] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Reverse Even Substeps | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;Table Size | [6] (1 ~ 20) | 
| │&nbsp;│&nbsp;└&nbsp;Two Step Solving | OFF | 
| │&nbsp;└&nbsp;Presets: Boobs || 
| │&nbsp;&nbsp;&nbsp;Presets | **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
| ├&nbsp;Softbody Only | OFF | Disable physics joint and use softbody particles only.
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, tina, 预设1, 预设2,  |
| **Skirt Physics**<sup>[PRO]</sup> | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Use Particle Dynamics | ON | 
| ├&nbsp;**Simulation Settings** | | 
| │&nbsp;├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| │&nbsp;├&nbsp;Enable Dragging | ON | 
| │&nbsp;├&nbsp;Simulate | ON | 
| │&nbsp;├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;│&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │&nbsp;├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| │&nbsp;├&nbsp;Substeps | [4] (1 ~ 20) | 
| │&nbsp;├&nbsp;Iterations | [1] (0 ~ 10) | 
| │&nbsp;├&nbsp;Reverse Even Substeps | OFF | 
| │&nbsp;├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| │&nbsp;├&nbsp;Table Size | [6] (1 ~ 20) | 
| │&nbsp;└&nbsp;Two Step Solving | OFF | 
| ├&nbsp;Primary Group || 
| ├&nbsp;Select Bones || 
| ├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| ├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├&nbsp;**Particle Dynamics** | | 
| │&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| ├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├&nbsp;**Lateral Joint** | | 
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;└&nbsp;Lock Z | OFF | 
| ├&nbsp;**Collider** | | 
| │&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| ├&nbsp;Additional Groups | [0] (0 ~ 7) | 
| ├&nbsp;**Group 2** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 3** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 4** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 5** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 6** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 7** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| ├&nbsp;**Group 8** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Select Bones || 
| │&nbsp;├&nbsp;Sorting: Shortest Path || Set sorting method used when making lateral connections.
| │&nbsp;│&nbsp;Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │&nbsp;├&nbsp;Closed Loop | ON | Bones for closed loops at each level
| │&nbsp;├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| │&nbsp;├&nbsp;**Particle Dynamics** | | 
| │&nbsp;│&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;│&nbsp;├&nbsp;Lateral Compliance | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lateral Anchor | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;│&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;│&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;│&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;│&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player | ON | 
| │&nbsp;├&nbsp;**Physics Properties** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;Mass | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Drag | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │&nbsp;│&nbsp;├&nbsp;Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
| │&nbsp;│&nbsp;├&nbsp;Friction | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
| │&nbsp;│&nbsp;└&nbsp;Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| │&nbsp;├&nbsp;**Parent-Child Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Swing Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Twist Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| │&nbsp;├&nbsp;**Lateral Joint** | | 
| │&nbsp;│&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Linear Drive | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Angular Drive | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;Drive Damping | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Reduction Rate | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Lock Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Lock Z | OFF | 
| │&nbsp;├&nbsp;**Collider** | | 
| │&nbsp;│&nbsp;├&nbsp;Collider Radius | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;Collider Type: Box || 
| │&nbsp;│&nbsp;│&nbsp;Collider Type | **Box** | Box, Capsule, Sphere,  |
| │&nbsp;│&nbsp;├&nbsp;Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;│&nbsp;└&nbsp;First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │&nbsp;└&nbsp;Use Primary Group Settings | ON | 
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
| **Hair Physics** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Select Bones || Select bones
| ├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├&nbsp;**Particle Dynamics** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;└&nbsp;Player | ON | 
| │&nbsp;└&nbsp;**Simulation Settings** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| │&nbsp;&nbsp;&nbsp;├&nbsp;Enable Dragging | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Simulate | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Substeps | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Iterations | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Reverse Even Substeps | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Table Size | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Two Step Solving | OFF | 
| ├&nbsp;Spring | [1.25] (0 ~ 5) | 
| ├&nbsp;Damp | [0.01] (0 ~ 0.1) | 
| ├&nbsp;Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├&nbsp;Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
| ├&nbsp;Limit Force | [3] (0 ~ 8) | 
| ├&nbsp;Mass | [0.01] (0 ~ 0.1) | 
| ├&nbsp;Drag | [1] (0 ~ 10) | 
| ├&nbsp;Collider Radius | [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├&nbsp;Collider Length | [0.9] (0 ~ 1) | 
| ├&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), momiji bob, Preset 1,  |
| **Dangling Physics** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Select Bones || Select bones
| ├&nbsp;Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├&nbsp;**Particle Dynamics** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │&nbsp;├&nbsp;Visualize | OFF | 
| │&nbsp;├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;Inertia | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │&nbsp;├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │&nbsp;├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;Friction | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │&nbsp;├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │&nbsp;├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**Wind** | | 
| │&nbsp;│&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**Collide With** | | 
| │&nbsp;│&nbsp;├&nbsp;Head | ON | 
| │&nbsp;│&nbsp;├&nbsp;Body | ON | 
| │&nbsp;│&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;│&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;│&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;│&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;│&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;│&nbsp;└&nbsp;Player | ON | 
| │&nbsp;└&nbsp;**Simulation Settings** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| │&nbsp;&nbsp;&nbsp;├&nbsp;Enable Dragging | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Simulate | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Simulation FPS: Dynamic || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Substeps | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Iterations | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Reverse Even Substeps | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;Table Size | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;Two Step Solving | OFF | 
| ├&nbsp;Spring | [0.5] (0 ~ 5) | 
| ├&nbsp;Damp | [0.01] (0 ~ 0.1) | 
| ├&nbsp;Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├&nbsp;Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
| ├&nbsp;Limit Force | [3] (0 ~ 8) | 
| ├&nbsp;Mass | [0.05] (0 ~ 0.1) | 
| ├&nbsp;Drag | [1] (0 ~ 10) | 
| ├&nbsp;Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├&nbsp;Collider Length | [0.9] (0 ~ 1) | 
| ├&nbsp;Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
| **Detach Object** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Select Bones || 
| ├&nbsp;Gravity | ON | 
| ├&nbsp;Mass | [0.1] (0 ~ 10) | 
| ├&nbsp;Damp | [0] (0 ~ 1) | 
| ├&nbsp;Collider | Sphere | None, Sphere, Capsule, 
| ├&nbsp;Collider Radius | [0.1] (0 ~ 1) | 
| └&nbsp;Collider Length | [0.3] (0 ~ 2) | 
| Presets: Default (Reset) || 
| Presets | **Default (Reset)** | Default (Reset),  |
