---
locale: en-rUS
layout: single
title: Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/model_physics) | [简中](/zh/dancexr/menu/2025.4/stage/model_physics)

[Stage](../menu#Stage) > Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| Disable PMX Physics | OFF | Disable PMX physics to use XPS tools instead
| Reduced Constraints | ON | Use the experimental setup that reduces constraints to allow smoother simulation
|**Collision** | | 
| Static Inclusive | ON | 
| Static Exclusive | ON | 
| Dynamic Inclusive | ON | 
| Dynamic Exclusive | ON | 
|**Linear Movement** | | Settings for linear movements
|- Restriction | **Auto**, Limited, Locked, Free,  | 
| Lock 0 Limit | ON | 
|- Min Spring Force | [5] (0 ~ 15) | 
|- Max Limit | [0.05] (0.05 ~ 0.1) | 
|- Bonciness | [0.5] (0 ~ 1) | 
|- Contact Distance | [0.5] (0 ~ 1) | 
|- Damping | [0.05] (0 ~ 1) | 
|- Drag | [0.15] (0 ~ 1) | 
|**Angular Movement** | | Settings for angular movements
|- Restriction | **Auto**, Limited, Locked, Free,  | 
| Lock 0 Limit | ON | 
|- Min Spring Force | [5] (0 ~ 15) | 
|- Max Limit | [90] (3 ~ 90) | 
|- Bonciness | [0.5] (0 ~ 1) | 
|- Contact Distance | [0.5] (0 ~ 1) | 
|- Damping | [0.05] (0 ~ 1) | 
|- Drag | [0.15] (0 ~ 1) | 
|**Linear Drive** | | Apply linear drive
| Enable Linear Drive | ON | 
|- Spring Force | [3] (0 ~ 5) | 
|- Damping | [0.1] (0 ~ 1) | 
|**Angular Drive** | | Apply angular drive
| Enable Angular Drive | ON | 
|- Spring Force | [0.1] (0 ~ 5) | 
|- Damping | [0.1] (0 ~ 1) | 
|**Linear Motion** | | Settings for linear motion
|- Firmness | [0] (-1 ~ 1) | 
|- Main Drive Force | [5] (0 ~ 8) | 
|- Second Drive Force | [3] (0 ~ 8) | 
|- Target Position | **Zero**, Center, Min, Max,  | 
| Lock When Possible | ON | 
| Acceleration Mode | ON | 
|- Damping | [0.05] (0 ~ 1) | 
|- Drag | [0.15] (0 ~ 1) | 
| Ignore Limit | OFF | Further reducing constraints by ignoring joint limits
|**Angular Motion** | | Settings for angular motion
|- Firmness | [0] (-1 ~ 1) | 
|- Main Drive Force | [5] (0 ~ 8) | 
|- Second Drive Force | [5] (0 ~ 8) | 
|- Target Position | **Zero**, Center, Min, Max,  | 
| Lock When Possible | OFF | 
| Acceleration Mode | ON | 
|- Damping | [0.05] (0 ~ 1) | 
|- Drag | [0.15] (0 ~ 1) | 
| Ignore Limit | OFF | Further reducing constraints by ignoring joint limits
|**Options** | | 
|- Min Drag | [0] (0 ~ 1) | The min drag value in auto mode
|- Drag Scale | [1] (0 ~ 5) | The scale applied to drag values in auto mode
|- Min Mass | [0] (0 ~ 1) | The min mass value in auto mode
|- Mass Scale | [1] (0 ~ 10) | The scale applied to mass values in auto mode
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|- Projection Dist | [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value
|- Projection Angle | [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value
|- Auto Reset Threshold | [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value
|**Auto Reset** | | 
|- Threshold | [30] (0 ~ 50) | 
|**Body Colliders** | | 
| Enable Body Colliders | ON | 
|- Size | [0.5] (0 ~ 1) | 
|- Head Radius | [1] (0 ~ 2) | 
|- Arm Radius | [1] (0 ~ 2) | 
|- Forearms | [1] (0 ~ 2) | 
|- Chest Width | [1] (0 ~ 2) | 
|- Waist Width | [0.5] (0 ~ 1) | 
|- Hips Width | [0] (-1 ~ 1) | 
|- Butts Radius | [1] (0 ~ 2) | 
| Butts Position || 
|- X | [0] (-0.1 ~ 0.1) | 
|- Y | [0] (-0.1 ~ 0.1) | 
|- Z | [0] (-0.1 ~ 0.1) | 
|- Belly Radius | [1] (0 ~ 2) | 
|- Belly Position | [0] (-1 ~ 1) | 
|- Leg Radius | [1] (0 ~ 2) | 
|- Thigh Fwd/Back | [0] (-1 ~ 1) | 
|- Thigh Start Position | [0] (0 ~ 1) | 
|- Hand | [0] (0 ~ 1) | 
| Visualize | OFF | 
| Presets | **Default (Reset)**,  |  |
|**Boobs Physics**<sup>[PRO]</sup> | | 
| Enable Boobs Physics | ON | 
| Select Bones || 
|- Spring Force | [1.5] (0 ~ 5) | 
|- Damping | [0.1] (0 ~ 1) | 
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0.1] (0 ~ 10) | 
|- Counter Gravity | [10] (0 ~ 45) | 
|**Rotation Limit** | | 
|- Up Limit | [100] (0 ~ 120) | 
|- Down Limit | [15] (0 ~ 45) | 
|- Left / Right Limit | [15] (0 ~ 45) | 
|- Spring Force | [1.25] (0 ~ 10) | Spring force when exceeding limit
|- Damping | [1] (0 ~ 1) | 
|- Contact Distance | [0.5] (0 ~ 1) | 
|- Bounce | [0.2] (0 ~ 1) | 
|**Anchor** | | 
|- X | [-0.03] (-0.2 ~ 0.2) | 
|- Y | [0.03] (-0.2 ~ 0.2) | 
|- Z | [0.08] (-0.2 ~ 0.2) | 
|**Center** | | 
|- X | [0.02] (-0.2 ~ 0.2) | 
|- Y | [-0.05] (-0.2 ~ 0.2) | 
|- Z | [0.025] (-0.2 ~ 0.2) | 
|**Collision** | | 
| Collide With Arms | OFF | 
|- Collider Radius | [0.07] (0 ~ 0.1) | 
|- Collider Length | [0.65] (0 ~ 1) | 
|- Collider Curve | [2] (-2 ~ 2) | Works with cloth simulation.
| Visualize | OFF | 
| Enable Nipple | ON | Works with cloth simulation.
|**Nipple Position** | | 
|- X | [-0.18] (-1 ~ 1) | 
|- Y | [0.09] (-1 ~ 1) | 
|- Z | [0.2] (0 ~ 1) | 
|- Nipple Size | [0.1] (0 ~ 1) | 
|**Softbody** | | 
| Enable Softbody | ON | 
| Joints || 
|- Depth | [0.4] (0 ~ 1) | 
| Include Center | ON | 
|- Volume Constraint | [0.85] (0.5 ~ 1) | 
|- Internal Constraint | [0.65] (0.5 ~ 1) | 
|- Surface Constraint | [0.75] (0.5 ~ 1) | 
|- Rotation Constraint | [0.65] (0.5 ~ 1) | 
|- Edge Lock | [0.85] (0.5 ~ 1) | Lock particles on the edge.
|- Center Lock | [1] (0.5 ~ 1) | 
|- Damping | [15] (0 ~ 40) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | OFF | 
| Boobs | OFF | 
| Butts | OFF | 
| Arms | ON | 
| Hands | ON | 
| Legs | OFF | 
| Feet | ON | 
| Player | ON | 
|**Simulation Settings** | | 
| Use Global | ON | Find the global settings under Pro / Cloth Simulation
| Enable Dragging | ON | 
| Simulate | ON | 
| Simulation FPS | **Dynamic**, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |  |
|- Time Scale | [0.65] (0.1 ~ 1) | 
|- Substeps | [4] (1 ~ 20) | 
|- Iterations | [1] (0 ~ 10) | 
| Reverse Even Substeps | OFF | 
|- Alternate Group Size | [0] (0 ~ 20) | 
|- Table Size | [6] (1 ~ 20) | 
| Two Step Solving | OFF | 
| Presets | **Boobs**, Butts, Legs,  |  |
| Softbody Only | OFF | Disable physics joint and use softbody particles only.
| Presets | **Default (Reset)**,  |  |
|**Skirt Physics**<sup>[PRO]</sup> | | 
| Enable Skirt Physics | ON | 
| Use Particle Dynamics | ON | 
|**Simulation Settings** | | 
| Use Global | ON | Find the global settings under Pro / Cloth Simulation
| Enable Dragging | ON | 
| Simulate | ON | 
| Simulation FPS | **Dynamic**, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |  |
|- Time Scale | [0.65] (0.1 ~ 1) | 
|- Substeps | [4] (1 ~ 20) | 
|- Iterations | [1] (0 ~ 10) | 
| Reverse Even Substeps | OFF | 
|- Alternate Group Size | [0] (0 ~ 20) | 
|- Table Size | [6] (1 ~ 20) | 
| Two Step Solving | OFF | 
| Primary Group || 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- Additional Groups | [0] (0 ~ 7) | 
|**Group 2** | | 
| Enable Group 2 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 3** | | 
| Enable Group 3 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 4** | | 
| Enable Group 4 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 5** | | 
| Enable Group 5 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 6** | | 
| Enable Group 6 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 7** | | 
| Enable Group 7 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
|**Group 8** | | 
| Enable Group 8 | OFF | 
| Select Bones || 
| Sorting | **Shortest Path**, Circular, Linear, No Sorting,  | Set sorting method used when making lateral connections. |
| Closed Loop | ON | Bones for closed loops at each level
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
|- Lateral Compliance | [1] (0 ~ 1) | 
|- Lateral Anchor | [0] (0 ~ 0.5) | 
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Physics Properties** | | Physics properties like mass, drag and friction
|- Mass | [0.1] (0 ~ 1) | 
|- Drag | [0] (0 ~ 10) | 
|- Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|- Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level
|- Friction | [0] (0 ~ 1) | 
|- Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision
|- Center Of Mass | Auto, **Zero**,  | Set center of mass at zero or automatically based on position and size of each collider
|**Parent-Child Joint** | | 
| Visualize | OFF | 
|- Swing Drive | [0] (0 ~ 10) | 
|- Twist Drive | [5] (0 ~ 10) | 
|- Drive Damping | [0.01] (0 ~ 1) | 
|- Reduction Rate | [0.5] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|**Lateral Joint** | | 
| Visualize | OFF | 
|- Linear Drive | [5] (0 ~ 10) | 
|- Angular Drive | [0] (0 ~ 10) | 
|- Drive Damping | [0.1] (0 ~ 1) | 
|- Reduction Rate | [1] (0 ~ 1) | 
| Lock Y | OFF | 
| Lock Z | OFF | 
|**Collider** | | 
|- Collider Radius | [0.01] (0 ~ 0.1) | 
| Collider Type | **Box**, Capsule, Sphere,  |  |
|- Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|- First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| Use Primary Group Settings | ON | 
| Presets | **Default (Reset)**, test,  |  |
|**Hair Physics** | | 
| Enable Hair Physics | ON | 
| Select Bones || Select bones
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
| Enable Particle Dynamics | ON | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Simulation Settings** | | 
| Use Global | ON | Find the global settings under Pro / Cloth Simulation
| Enable Dragging | ON | 
| Simulate | ON | 
| Simulation FPS | **Dynamic**, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |  |
|- Time Scale | [0.65] (0.1 ~ 1) | 
|- Substeps | [4] (1 ~ 20) | 
|- Iterations | [1] (0 ~ 10) | 
| Reverse Even Substeps | OFF | 
|- Alternate Group Size | [0] (0 ~ 20) | 
|- Table Size | [6] (1 ~ 20) | 
| Two Step Solving | OFF | 
|- Spring | [1.25] (0 ~ 5) | 
|- Damp | [0.01] (0 ~ 0.1) | 
|- Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
|- Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
|- Limit Force | [3] (0 ~ 8) | 
|- Mass | [0.01] (0 ~ 0.1) | 
|- Drag | [1] (0 ~ 10) | 
|- Collider Radius | [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.
|- Collider Length | [0.9] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| Presets | **Default (Reset)**,  |  |
|**Dangling Physics** | | 
| Enable Dangling Physics | ON | 
| Select Bones || Select bones
|- Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|**Particle Dynamics** | | 
| Enable Particle Dynamics | ON | 
|- Swing Compliance | [0.25] (0 ~ 1) | 
|- Twist Compliance | [0.75] (0 ~ 1) | 
|- Particle Anchor | [0.5] (0 ~ 1) | 
|- Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| Visualize | OFF | 
|- Max Angular Velocity | [2] (0 ~ 4) | 
|- Inertia | [2] (1 ~ 5) | 
|- Soften | [0] (0 ~ 1) | Soften the particle constraints.
|- Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
|- Gravity | [9.8] (-9.8 ~ 9.8) | 
|- Friction | [1] (0 ~ 2) | 
|- Ground Friction | [1] (-2 ~ 2) | 
|- Drag (Air) | [0] (0 ~ 2) | Air resistancy
|- Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
|- Buoyancy | [-0.1] (-1 ~ 1) | 
|**Wind** | | 
|- Wind Influence | [0.25] (0 ~ 1) | 
|- Turbulence Scale | [0] (-2 ~ 2) | 
|- Turbulence Intensity | [1] (0 ~ 2) | 
|- Turbulence Time Scale | [0] (-4 ~ 4) | 
|**Collide With** | | 
| Head | ON | 
| Body | ON | 
| Boobs | ON | 
| Butts | ON | 
| Arms | ON | 
| Hands | ON | 
| Legs | ON | 
| Feet | ON | 
| Player | ON | 
|**Simulation Settings** | | 
| Use Global | ON | Find the global settings under Pro / Cloth Simulation
| Enable Dragging | ON | 
| Simulate | ON | 
| Simulation FPS | **Dynamic**, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |  |
|- Time Scale | [0.65] (0.1 ~ 1) | 
|- Substeps | [4] (1 ~ 20) | 
|- Iterations | [1] (0 ~ 10) | 
| Reverse Even Substeps | OFF | 
|- Alternate Group Size | [0] (0 ~ 20) | 
|- Table Size | [6] (1 ~ 20) | 
| Two Step Solving | OFF | 
|- Spring | [0.5] (0 ~ 5) | 
|- Damp | [0.01] (0 ~ 0.1) | 
|- Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
|- Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
|- Limit Force | [3] (0 ~ 8) | 
|- Mass | [0.05] (0 ~ 0.1) | 
|- Drag | [1] (0 ~ 10) | 
|- Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
|- Collider Length | [0.9] (0 ~ 1) | 
|- Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| Presets | **Default (Reset)**,  |  |
|**Detach Object** | | 
| Enable Detach Object | ON | 
| Select Bones || 
| Gravity | ON | 
|- Mass | [0.1] (0 ~ 10) | 
|- Damp | [0] (0 ~ 1) | 
|- Collider | None, **Sphere**, Capsule,  | 
|- Collider Radius | [0.1] (0 ~ 1) | 
|- Collider Length | [0.3] (0 ~ 2) | 
| Presets | **Default (Reset)**,  |  |
