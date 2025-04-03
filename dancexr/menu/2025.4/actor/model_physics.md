---
locale: en-rUS
layout: single
title: Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/model_physics) | [繁中](/tw/dancexr/menu/2025.4/actor/model_physics) | [日本語](/jp/dancexr/menu/2025.4/actor/model_physics) | [한국어](/kr/dancexr/menu/2025.4/actor/model_physics) | [简中](/zh/dancexr/menu/2025.4/actor/model_physics)

[Actor](../menu#Actor) > Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| Disable PMX Physics | OFF | Disable PMX physics to use XPS tools instead0/17/True
| Reduced Constraints | ON | Use the experimental setup that reduces constraints to allow smoother simulation1/17/True
| **Collision** | | 2/17/True
| ├ Static Inclusive | ON | 0/3/False
| ├ Static Exclusive | ON | 1/3/False
| ├ Dynamic Inclusive | ON | 2/3/False
| └ Dynamic Exclusive | ON | 3/3/False
| **Linear Movement** | | Settings for linear movements3/17/True
| ├ Restriction | Auto | Auto, Limited, Locked, Free, 0/7/False
| ├ Lock 0 Limit | ON | 1/7/False
| ├ Min Spring Force | [5] (0 ~ 15) | 2/7/False
| ├ Max Limit | [0.05] (0.05 ~ 0.1) | 3/7/False
| ├ Bonciness | [0.5] (0 ~ 1) | 4/7/False
| ├ Contact Distance | [0.5] (0 ~ 1) | 5/7/False
| ├ Damping | [0.05] (0 ~ 1) | 6/7/False
| └ Drag | [0.15] (0 ~ 1) | 7/7/False
| **Angular Movement** | | Settings for angular movements4/17/True
| ├ Restriction | Auto | Auto, Limited, Locked, Free, 0/7/False
| ├ Lock 0 Limit | ON | 1/7/False
| ├ Min Spring Force | [5] (0 ~ 15) | 2/7/False
| ├ Max Limit | [90] (3 ~ 90) | 3/7/False
| ├ Bonciness | [0.5] (0 ~ 1) | 4/7/False
| ├ Contact Distance | [0.5] (0 ~ 1) | 5/7/False
| ├ Damping | [0.05] (0 ~ 1) | 6/7/False
| └ Drag | [0.15] (0 ~ 1) | 7/7/False
| **Linear Drive** | | Apply linear drive5/17/True
| ├ Enable Linear Drive | ON | 0/2/False
| ├ Spring Force | [3] (0 ~ 5) | 1/2/False
| └ Damping | [0.1] (0 ~ 1) | 2/2/False
| **Angular Drive** | | Apply angular drive6/17/True
| ├ Enable Angular Drive | ON | 0/2/False
| ├ Spring Force | [0.1] (0 ~ 5) | 1/2/False
| └ Damping | [0.1] (0 ~ 1) | 2/2/False
| **Linear Motion** | | Settings for linear motion7/17/True
| ├ Firmness | [0] (-1 ~ 1) | 0/8/False
| ├ Main Drive Force | [5] (0 ~ 8) | 1/8/False
| ├ Second Drive Force | [3] (0 ~ 8) | 2/8/False
| ├ Target Position | Zero | Zero, Center, Min, Max, 3/8/False
| ├ Lock When Possible | ON | 4/8/False
| ├ Acceleration Mode | ON | 5/8/False
| ├ Damping | [0.05] (0 ~ 1) | 6/8/False
| ├ Drag | [0.15] (0 ~ 1) | 7/8/False
| └ Ignore Limit | OFF | Further reducing constraints by ignoring joint limits8/8/False
| **Angular Motion** | | Settings for angular motion8/17/True
| ├ Firmness | [0] (-1 ~ 1) | 0/8/False
| ├ Main Drive Force | [5] (0 ~ 8) | 1/8/False
| ├ Second Drive Force | [5] (0 ~ 8) | 2/8/False
| ├ Target Position | Zero | Zero, Center, Min, Max, 3/8/False
| ├ Lock When Possible | OFF | 4/8/False
| ├ Acceleration Mode | ON | 5/8/False
| ├ Damping | [0.05] (0 ~ 1) | 6/8/False
| ├ Drag | [0.15] (0 ~ 1) | 7/8/False
| └ Ignore Limit | OFF | Further reducing constraints by ignoring joint limits8/8/False
| **Options** | | 9/17/True
| ├ Min Drag | [0] (0 ~ 1) | The min drag value in auto mode0/6/False
| ├ Drag Scale | [1] (0 ~ 5) | The scale applied to drag values in auto mode1/6/False
| ├ Min Mass | [0] (0 ~ 1) | The min mass value in auto mode2/6/False
| ├ Mass Scale | [1] (0 ~ 10) | The scale applied to mass values in auto mode3/6/False
| ├ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider4/6/False
| ├ Projection Dist | [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value5/6/False
| └ Projection Angle | [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value6/6/False
| Auto Reset Threshold | [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value10/17/True
| **Auto Reset** | | 11/17/True
| └ Threshold | [30] (0 ~ 50) | 0/0/False
| **Body Colliders** | | 12/17/True
| ├ Enable Body Colliders | ON | 0/19/True
| ├ Size | [0.5] (0 ~ 1) | 1/19/True
| ├ Head Radius | [1] (0 ~ 2) | 2/19/True
| ├ Arm Radius | [1] (0 ~ 2) | 3/19/True
| ├ Forearms | [1] (0 ~ 2) | 4/19/True
| ├ Chest Width | [1] (0 ~ 2) | 5/19/True
| ├ Waist Width | [0.5] (0 ~ 1) | 6/19/True
| ├ Hips Width | [0] (-1 ~ 1) | 7/19/True
| ├ Butts Radius | [1] (0 ~ 2) | 8/19/True
| ├ Butts Position || 9/19/True
| ├ X | [0] (-0.1 ~ 0.1) | 10/19/True
| ├ Y | [0] (-0.1 ~ 0.1) | 11/19/True
| ├ Z | [0] (-0.1 ~ 0.1) | 12/19/True
| ├ Belly Radius | [1] (0 ~ 2) | 13/19/True
| ├ Belly Position | [0] (-1 ~ 1) | 14/19/True
| ├ Leg Radius | [1] (0 ~ 2) | 15/19/True
| ├ Thigh Fwd/Back | [0] (-1 ~ 1) | 16/19/True
| ├ Thigh Start Position | [0] (0 ~ 1) | 17/19/True
| ├ Hand | [0] (0 ~ 1) | 18/19/True
| ├ Visualize | OFF | 19/19/True
| └ Presets | **Default (Reset)** | Default (Reset), amy, misaki,  |
| **Boobs Physics**<sup>[PRO]</sup> | | 13/17/True
| ├ Enable Boobs Physics | ON | 0/12/True
| ├ Select Bones || 1/12/True
| ├ Spring Force | [1.5] (0 ~ 5) | 2/12/True
| ├ Damping | [0.1] (0 ~ 1) | 3/12/True
| ├ Mass | [0.1] (0 ~ 1) | 4/12/True
| ├ Drag | [0.1] (0 ~ 10) | 5/12/True
| ├ Counter Gravity | [10] (0 ~ 45) | 6/12/True
| ├ **Rotation Limit** | | 7/12/True
| │ ├ Up Limit | [100] (0 ~ 120) | 0/6/False
| │ ├ Down Limit | [15] (0 ~ 45) | 1/6/False
| │ ├ Left / Right Limit | [15] (0 ~ 45) | 2/6/False
| │ ├ Spring Force | [1.25] (0 ~ 10) | Spring force when exceeding limit3/6/False
| │ ├ Damping | [1] (0 ~ 1) | 4/6/False
| │ ├ Contact Distance | [0.5] (0 ~ 1) | 5/6/False
| │ └ Bounce | [0.2] (0 ~ 1) | 6/6/False
| ├ **Anchor** | | 8/12/True
| │ ├ X | [-0.03] (-0.2 ~ 0.2) | 0/2/False
| │ ├ Y | [0.03] (-0.2 ~ 0.2) | 1/2/False
| │ └ Z | [0.08] (-0.2 ~ 0.2) | 2/2/False
| ├ **Center** | | 9/12/True
| │ ├ X | [0.02] (-0.2 ~ 0.2) | 0/2/False
| │ ├ Y | [-0.05] (-0.2 ~ 0.2) | 1/2/False
| │ └ Z | [0.025] (-0.2 ~ 0.2) | 2/2/False
| ├ **Collision** | | 10/12/True
| │ ├ Collide With Arms | OFF | 0/7/False
| │ ├ Collider Radius | [0.07] (0 ~ 0.1) | 1/7/False
| │ ├ Collider Length | [0.65] (0 ~ 1) | 2/7/False
| │ ├ Collider Curve | [2] (-2 ~ 2) | Works with cloth simulation.3/7/False
| │ ├ Visualize | OFF | 4/7/False
| │ ├ Enable Nipple | ON | Works with cloth simulation.5/7/False
| │ ├ **Nipple Position** | | 6/7/False
| │ │ ├ X | [-0.18] (-1 ~ 1) | 0/2/False
| │ │ ├ Y | [0.09] (-1 ~ 1) | 1/2/False
| │ │ └ Z | [0.2] (0 ~ 1) | 2/2/False
| │ └ Nipple Size | [0.1] (0 ~ 1) | 7/7/False
| ├ **Softbody** | | 11/12/True
| │ ├ Enable Softbody | ON | 0/24/True
| │ ├ Joints || 1/24/True
| │ ├ Depth | [0.4] (0 ~ 1) | 2/24/True
| │ ├ Include Center | ON | 3/24/True
| │ ├ Volume Constraint | [0.85] (0.5 ~ 1) | 4/24/True
| │ ├ Internal Constraint | [0.65] (0.5 ~ 1) | 5/24/True
| │ ├ Surface Constraint | [0.75] (0.5 ~ 1) | 6/24/True
| │ ├ Rotation Constraint | [0.65] (0.5 ~ 1) | 7/24/True
| │ ├ Edge Lock | [0.85] (0.5 ~ 1) | Lock particles on the edge.8/24/True
| │ ├ Center Lock | [1] (0.5 ~ 1) | 9/24/True
| │ ├ Damping | [15] (0 ~ 40) | 10/24/True
| │ ├ Visualize | OFF | 11/24/True
| │ ├ Max Angular Velocity | [2] (0 ~ 4) | 12/24/True
| │ ├ Inertia | [2] (1 ~ 5) | 13/24/True
| │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.14/24/True
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters15/24/True
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 16/24/True
| │ ├ Friction | [1] (0 ~ 2) | 17/24/True
| │ ├ Ground Friction | [1] (-2 ~ 2) | 18/24/True
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy19/24/True
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy20/24/True
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 21/24/True
| │ ├ **Wind** | | 22/24/True
| │ │ ├ Wind Influence | [0] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ ├ **Collide With** | | 23/24/True
| │ │ ├ Head | ON | 0/8/False
| │ │ ├ Body | OFF | 1/8/False
| │ │ ├ Boobs | OFF | 2/8/False
| │ │ ├ Butts | OFF | 3/8/False
| │ │ ├ Arms | ON | 4/8/False
| │ │ ├ Hands | ON | 5/8/False
| │ │ ├ Legs | OFF | 6/8/False
| │ │ ├ Feet | ON | 7/8/False
| │ │ └ Player | ON | 8/8/False
| │ ├ **Simulation Settings** | | 24/24/True
| │ │ ├ Use Global | ON | Find the global settings under Pro / Cloth Simulation0/10/False
| │ │ ├ Enable Dragging | ON | 1/10/False
| │ │ ├ Simulate | ON | 2/10/False
| │ │ ├ Simulation FPS: Dynamic || 3/10/False
| │ │ │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ │ ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
| │ │ ├ Substeps | [4] (1 ~ 20) | 5/10/False
| │ │ ├ Iterations | [1] (0 ~ 10) | 6/10/False
| │ │ ├ Reverse Even Substeps | OFF | 7/10/False
| │ │ ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
| │ │ ├ Table Size | [6] (1 ~ 20) | 9/10/False
| │ │ └ Two Step Solving | OFF | 10/10/False
| │ └ Presets | **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
| ├ Softbody Only | OFF | Disable physics joint and use softbody particles only.12/12/True
| └ Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, tina, 预设1, 预设2,  |
| **Skirt Physics**<sup>[PRO]</sup> | | 14/17/True
| ├ Enable Skirt Physics | ON | 0/20/True
| ├ Use Particle Dynamics | ON | 1/20/True
| ├ **Simulation Settings** | | 2/20/True
| │ ├ Use Global | ON | Find the global settings under Pro / Cloth Simulation0/10/False
| │ ├ Enable Dragging | ON | 1/10/False
| │ ├ Simulate | ON | 2/10/False
| │ ├ Simulation FPS: Dynamic || 3/10/False
| │ │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │ ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
| │ ├ Substeps | [4] (1 ~ 20) | 5/10/False
| │ ├ Iterations | [1] (0 ~ 10) | 6/10/False
| │ ├ Reverse Even Substeps | OFF | 7/10/False
| │ ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
| │ ├ Table Size | [6] (1 ~ 20) | 9/10/False
| │ └ Two Step Solving | OFF | 10/10/False
| ├ Primary Group || 3/20/True
| ├ Select Bones || 4/20/True
| ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.5/20/True
| │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├ Closed Loop | ON | Bones for closed loops at each level6/20/True
| ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels7/20/True
| ├ **Particle Dynamics** | | 8/20/True
| │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ ├ Visualize | OFF | 6/18/False
| │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ ├ **Wind** | | 17/18/False
| │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ └ **Collide With** | | 18/18/False
| │   ├ Head | ON | 0/8/False
| │   ├ Body | ON | 1/8/False
| │   ├ Boobs | ON | 2/8/False
| │   ├ Butts | ON | 3/8/False
| │   ├ Arms | ON | 4/8/False
| │   ├ Hands | ON | 5/8/False
| │   ├ Legs | ON | 6/8/False
| │   ├ Feet | ON | 7/8/False
| │   └ Player | ON | 8/8/False
| ├ **Physics Properties** | | Physics properties like mass, drag and friction9/20/True
| │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| ├ **Parent-Child Joint** | | 10/20/True
| │ ├ Visualize | OFF | 0/5/False
| │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| ├ **Lateral Joint** | | 11/20/True
| │ ├ Visualize | OFF | 0/6/False
| │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ ├ Lock Y | OFF | 5/6/False
| │ └ Lock Z | OFF | 6/6/False
| ├ **Collider** | | 12/20/True
| │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ ├ Collider Type: Box || 1/3/False
| │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| ├ Additional Groups | [0] (0 ~ 7) | 13/20/True
| ├ **Group 2** | | 14/20/True
| │ ├ Enable Group 2 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 3** | | 15/20/True
| │ ├ Enable Group 3 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 4** | | 16/20/True
| │ ├ Enable Group 4 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 5** | | 17/20/True
| │ ├ Enable Group 5 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 6** | | 18/20/True
| │ ├ Enable Group 6 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 7** | | 19/20/True
| │ ├ Enable Group 7 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| ├ **Group 8** | | 20/20/True
| │ ├ Enable Group 8 | OFF | 0/10/False
| │ ├ Select Bones || 1/10/False
| │ ├ Sorting: Shortest Path || Set sorting method used when making lateral connections.2/10/False
| │ │ Sorting | **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| │ ├ Closed Loop | ON | Bones for closed loops at each level3/10/False
| │ ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels4/10/False
| │ ├ **Particle Dynamics** | | 5/10/False
| │ │ ├ Swing Compliance | [0.25] (0 ~ 1) | 0/18/False
| │ │ ├ Twist Compliance | [0.75] (0 ~ 1) | 1/18/False
| │ │ ├ Particle Anchor | [0.5] (0 ~ 1) | 2/18/False
| │ │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level3/18/False
| │ │ ├ Lateral Compliance | [1] (0 ~ 1) | 4/18/False
| │ │ ├ Lateral Anchor | [0] (0 ~ 0.5) | 5/18/False
| │ │ ├ Visualize | OFF | 6/18/False
| │ │ ├ Max Angular Velocity | [2] (0 ~ 4) | 7/18/False
| │ │ ├ Inertia | [2] (1 ~ 5) | 8/18/False
| │ │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.9/18/False
| │ │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters10/18/False
| │ │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 11/18/False
| │ │ ├ Friction | [1] (0 ~ 2) | 12/18/False
| │ │ ├ Ground Friction | [1] (-2 ~ 2) | 13/18/False
| │ │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy14/18/False
| │ │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy15/18/False
| │ │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 16/18/False
| │ │ ├ **Wind** | | 17/18/False
| │ │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ │ └ **Collide With** | | 18/18/False
| │ │   ├ Head | ON | 0/8/False
| │ │   ├ Body | ON | 1/8/False
| │ │   ├ Boobs | ON | 2/8/False
| │ │   ├ Butts | ON | 3/8/False
| │ │   ├ Arms | ON | 4/8/False
| │ │   ├ Hands | ON | 5/8/False
| │ │   ├ Legs | ON | 6/8/False
| │ │   ├ Feet | ON | 7/8/False
| │ │   └ Player | ON | 8/8/False
| │ ├ **Physics Properties** | | Physics properties like mass, drag and friction6/10/False
| │ │ ├ Mass | [0.1] (0 ~ 1) | 0/6/False
| │ │ ├ Drag | [0] (0 ~ 10) | 1/6/False
| │ │ ├ Horizontal Overlap | [-0.2] (-1 ~ 1) | Overlap of colliders horizontally2/6/False
| │ │ ├ Mass Distribution | [0] (-1 ~ 1) | Reduce mass at each level3/6/False
| │ │ ├ Friction | [0] (0 ~ 1) | 4/6/False
| │ │ ├ Solver Iterations | [20] (1 ~ 150) | Number of iterations when solving collision5/6/False
| │ │ └ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider6/6/False
| │ ├ **Parent-Child Joint** | | 7/10/False
| │ │ ├ Visualize | OFF | 0/5/False
| │ │ ├ Swing Drive | [0] (0 ~ 10) | 1/5/False
| │ │ ├ Twist Drive | [5] (0 ~ 10) | 2/5/False
| │ │ ├ Drive Damping | [0.01] (0 ~ 1) | 3/5/False
| │ │ ├ Reduction Rate | [0.5] (0 ~ 1) | 4/5/False
| │ │ └ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone5/5/False
| │ ├ **Lateral Joint** | | 8/10/False
| │ │ ├ Visualize | OFF | 0/6/False
| │ │ ├ Linear Drive | [5] (0 ~ 10) | 1/6/False
| │ │ ├ Angular Drive | [0] (0 ~ 10) | 2/6/False
| │ │ ├ Drive Damping | [0.1] (0 ~ 1) | 3/6/False
| │ │ ├ Reduction Rate | [1] (0 ~ 1) | 4/6/False
| │ │ ├ Lock Y | OFF | 5/6/False
| │ │ └ Lock Z | OFF | 6/6/False
| │ ├ **Collider** | | 9/10/False
| │ │ ├ Collider Radius | [0.01] (0 ~ 0.1) | 0/3/False
| │ │ ├ Collider Type: Box || 1/3/False
| │ │ │ Collider Type | **Box** | Box, Capsule, Sphere,  |
| │ │ ├ Collider Length | [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.2/3/False
| │ │ └ First Collider Length | [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.3/3/False
| │ └ Use Primary Group Settings | ON | 10/10/False
| └ Presets | **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
| **Hair Physics** | | 15/17/True
| ├ Enable Hair Physics | ON | 0/13/True
| ├ Select Bones || Select bones1/13/True
| ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels2/13/True
| ├ **Particle Dynamics** | | 3/13/True
| │ ├ Enable Particle Dynamics | ON | 0/18/False
| │ ├ Swing Compliance | [0.25] (0 ~ 1) | 1/18/False
| │ ├ Twist Compliance | [0.75] (0 ~ 1) | 2/18/False
| │ ├ Particle Anchor | [0.5] (0 ~ 1) | 3/18/False
| │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level4/18/False
| │ ├ Visualize | OFF | 5/18/False
| │ ├ Max Angular Velocity | [2] (0 ~ 4) | 6/18/False
| │ ├ Inertia | [2] (1 ~ 5) | 7/18/False
| │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.8/18/False
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters9/18/False
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 10/18/False
| │ ├ Friction | [1] (0 ~ 2) | 11/18/False
| │ ├ Ground Friction | [1] (-2 ~ 2) | 12/18/False
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy13/18/False
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy14/18/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 15/18/False
| │ ├ **Wind** | | 16/18/False
| │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ ├ **Collide With** | | 17/18/False
| │ │ ├ Head | ON | 0/8/False
| │ │ ├ Body | ON | 1/8/False
| │ │ ├ Boobs | ON | 2/8/False
| │ │ ├ Butts | ON | 3/8/False
| │ │ ├ Arms | ON | 4/8/False
| │ │ ├ Hands | ON | 5/8/False
| │ │ ├ Legs | ON | 6/8/False
| │ │ ├ Feet | ON | 7/8/False
| │ │ └ Player | ON | 8/8/False
| │ └ **Simulation Settings** | | 18/18/False
| │   ├ Use Global | ON | Find the global settings under Pro / Cloth Simulation0/10/False
| │   ├ Enable Dragging | ON | 1/10/False
| │   ├ Simulate | ON | 2/10/False
| │   ├ Simulation FPS: Dynamic || 3/10/False
| │   │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │   ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
| │   ├ Substeps | [4] (1 ~ 20) | 5/10/False
| │   ├ Iterations | [1] (0 ~ 10) | 6/10/False
| │   ├ Reverse Even Substeps | OFF | 7/10/False
| │   ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
| │   ├ Table Size | [6] (1 ~ 20) | 9/10/False
| │   └ Two Step Solving | OFF | 10/10/False
| ├ Spring | [1.25] (0 ~ 5) | 4/13/True
| ├ Damp | [0.01] (0 ~ 0.1) | 5/13/True
| ├ Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level6/13/True
| ├ Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation7/13/True
| ├ Limit Force | [3] (0 ~ 8) | 8/13/True
| ├ Mass | [0.01] (0 ~ 0.1) | 9/13/True
| ├ Drag | [1] (0 ~ 10) | 10/13/True
| ├ Collider Radius | [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.11/13/True
| ├ Collider Length | [0.9] (0 ~ 1) | 12/13/True
| ├ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone13/13/True
| └ Presets | **Default (Reset)** | Default (Reset), momiji bob, Preset 1,  |
| **Dangling Physics** | | 16/17/True
| ├ Enable Dangling Physics | ON | 0/13/True
| ├ Select Bones || Select bones1/13/True
| ├ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels2/13/True
| ├ **Particle Dynamics** | | 3/13/True
| │ ├ Enable Particle Dynamics | ON | 0/18/False
| │ ├ Swing Compliance | [0.25] (0 ~ 1) | 1/18/False
| │ ├ Twist Compliance | [0.75] (0 ~ 1) | 2/18/False
| │ ├ Particle Anchor | [0.5] (0 ~ 1) | 3/18/False
| │ ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level4/18/False
| │ ├ Visualize | OFF | 5/18/False
| │ ├ Max Angular Velocity | [2] (0 ~ 4) | 6/18/False
| │ ├ Inertia | [2] (1 ~ 5) | 7/18/False
| │ ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.8/18/False
| │ ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters9/18/False
| │ ├ Gravity | [9.8] (-9.8 ~ 9.8) | 10/18/False
| │ ├ Friction | [1] (0 ~ 2) | 11/18/False
| │ ├ Ground Friction | [1] (-2 ~ 2) | 12/18/False
| │ ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy13/18/False
| │ ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy14/18/False
| │ ├ Buoyancy | [-0.1] (-1 ~ 1) | 15/18/False
| │ ├ **Wind** | | 16/18/False
| │ │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| │ ├ **Collide With** | | 17/18/False
| │ │ ├ Head | ON | 0/8/False
| │ │ ├ Body | ON | 1/8/False
| │ │ ├ Boobs | ON | 2/8/False
| │ │ ├ Butts | ON | 3/8/False
| │ │ ├ Arms | ON | 4/8/False
| │ │ ├ Hands | ON | 5/8/False
| │ │ ├ Legs | ON | 6/8/False
| │ │ ├ Feet | ON | 7/8/False
| │ │ └ Player | ON | 8/8/False
| │ └ **Simulation Settings** | | 18/18/False
| │   ├ Use Global | ON | Find the global settings under Pro / Cloth Simulation0/10/False
| │   ├ Enable Dragging | ON | 1/10/False
| │   ├ Simulate | ON | 2/10/False
| │   ├ Simulation FPS: Dynamic || 3/10/False
| │   │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │   ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
| │   ├ Substeps | [4] (1 ~ 20) | 5/10/False
| │   ├ Iterations | [1] (0 ~ 10) | 6/10/False
| │   ├ Reverse Even Substeps | OFF | 7/10/False
| │   ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
| │   ├ Table Size | [6] (1 ~ 20) | 9/10/False
| │   └ Two Step Solving | OFF | 10/10/False
| ├ Spring | [0.5] (0 ~ 5) | 4/13/True
| ├ Damp | [0.01] (0 ~ 0.1) | 5/13/True
| ├ Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level6/13/True
| ├ Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation7/13/True
| ├ Limit Force | [3] (0 ~ 8) | 8/13/True
| ├ Mass | [0.05] (0 ~ 0.1) | 9/13/True
| ├ Drag | [1] (0 ~ 10) | 10/13/True
| ├ Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.11/13/True
| ├ Collider Length | [0.9] (0 ~ 1) | 12/13/True
| ├ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone13/13/True
| └ Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
| **Detach Object** | | 17/17/True
| ├ Enable Detach Object | ON | 0/7/False
| ├ Select Bones || 1/7/False
| ├ Gravity | ON | 2/7/False
| ├ Mass | [0.1] (0 ~ 10) | 3/7/False
| ├ Damp | [0] (0 ~ 1) | 4/7/False
| ├ Collider | Sphere | None, Sphere, Capsule, 5/7/False
| ├ Collider Radius | [0.1] (0 ~ 1) | 6/7/False
| └ Collider Length | [0.3] (0 ~ 2) | 7/7/False
| Presets | **Default (Reset)** | Default (Reset),  |
