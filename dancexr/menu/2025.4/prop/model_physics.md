---
locale: en-rUS
layout: single
title: Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[Prop](../menu#Prop) > Physics



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>Disable PMX Physics</nobr>| [OFF] | Disable PMX physics to use XPS tools instead
|<nobr>Reduced Constraints</nobr>| [ON] | Use the experimental setup that reduces constraints to allow smoother simulation
|<nobr>**Collision**</nobr>| | 
|<nobr>├&nbsp;Static Inclusive</nobr>| [ON] | 
|<nobr>├&nbsp;Static Exclusive</nobr>| [ON] | 
|<nobr>├&nbsp;Dynamic Inclusive</nobr>| [ON] | 
|<nobr>└&nbsp;Dynamic Exclusive</nobr>| [ON] | 
|<nobr>**Linear Movement**</nobr>| | Settings for linear movements
|<nobr>├&nbsp;Restriction</nobr>| Auto | Auto, Limited, Locked, Free, 
|<nobr>├&nbsp;Lock 0 Limit</nobr>| [ON] | 
|<nobr>├&nbsp;Min Spring Force</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;Max Limit</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp;Bonciness</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Contact Distance</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Damping</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;Drag</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**Angular Movement**</nobr>| | Settings for angular movements
|<nobr>├&nbsp;Restriction</nobr>| Auto | Auto, Limited, Locked, Free, 
|<nobr>├&nbsp;Lock 0 Limit</nobr>| [ON] | 
|<nobr>├&nbsp;Min Spring Force</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;Max Limit</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp;Bonciness</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Contact Distance</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Damping</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;Drag</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**Linear Drive**</nobr>| | Apply linear drive
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Spring Force</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp;Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**Angular Drive**</nobr>| | Apply angular drive
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Spring Force</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp;Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**Linear Motion**</nobr>| | Settings for linear motion
|<nobr>├&nbsp;Firmness</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;Main Drive Force</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;Second Drive Force</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;Target Position</nobr>| Zero | Zero, Center, Min, Max, 
|<nobr>├&nbsp;Lock When Possible</nobr>| [ON] | 
|<nobr>├&nbsp;Acceleration Mode</nobr>| [ON] | 
|<nobr>├&nbsp;Damping</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;Drag</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;Ignore Limit</nobr>| [OFF] | Further reducing constraints by ignoring joint limits
|<nobr>**Angular Motion**</nobr>| | Settings for angular motion
|<nobr>├&nbsp;Firmness</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;Main Drive Force</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;Second Drive Force</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;Target Position</nobr>| Zero | Zero, Center, Min, Max, 
|<nobr>├&nbsp;Lock When Possible</nobr>| [OFF] | 
|<nobr>├&nbsp;Acceleration Mode</nobr>| [ON] | 
|<nobr>├&nbsp;Damping</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;Drag</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;Ignore Limit</nobr>| [OFF] | Further reducing constraints by ignoring joint limits
|<nobr>**Options**</nobr>| | 
|<nobr>├&nbsp;Min Drag</nobr>| [0] (0 ~ 1) | The min drag value in auto mode
|<nobr>├&nbsp;Drag Scale</nobr>| [1] (0 ~ 5) | The scale applied to drag values in auto mode
|<nobr>├&nbsp;Min Mass</nobr>| [0] (0 ~ 1) | The min mass value in auto mode
|<nobr>├&nbsp;Mass Scale</nobr>| [1] (0 ~ 10) | The scale applied to mass values in auto mode
|<nobr>├&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;Projection Dist</nobr>| [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value
|<nobr>└&nbsp;Projection Angle</nobr>| [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value
|<nobr>Auto Reset Threshold</nobr>| [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value
|<nobr>**Auto Reset**</nobr>| | 
|<nobr>└&nbsp;Threshold</nobr>| [30] (0 ~ 50) | 
|<nobr>**Body Colliders**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Size</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Head Radius</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Arm Radius</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Forearms</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Chest Width</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Waist Width</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Hips Width</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;Butts Radius</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Butts Position</nobr>|| 
|<nobr>├&nbsp;X</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;Y</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;Z</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;Belly Radius</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Belly Position</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;Leg Radius</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Thigh Fwd/Back</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;Thigh Start Position</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Hand</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), amy, misaki,  |
|<nobr>**Boobs Physics**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Spring Force</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp;Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;Drag</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;Counter Gravity</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp;**Rotation Limit**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Up Limit</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp;Down Limit</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;Left / Right Limit</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;Spring Force</nobr>| [1.25] (0 ~ 10) | Spring force when exceeding limit
|<nobr>│&nbsp;├&nbsp;Damping</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Contact Distance</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Bounce</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;**Anchor**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**Center**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;X</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;Y</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;Z</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**Collision**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collide With Arms</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Collider Curve</nobr>| [2] (-2 ~ 2) | Works with cloth simulation.
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Enable Nipple</nobr>| [ON] | Works with cloth simulation.
|<nobr>│&nbsp;├&nbsp;**Nipple Position**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;X</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Nipple Size</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;**Softbody**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Joints</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Include Center</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>│&nbsp;├&nbsp;Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Body</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Boobs</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Butts</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Legs</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Simulation Settings**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>│&nbsp;│&nbsp;├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>├&nbsp;Softbody Only</nobr>| [OFF] | Disable physics joint and use softbody particles only.
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3, tina, 预设1, 预设2,  |
|<nobr>**Skirt Physics**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Use Particle Dynamics</nobr>| [ON] | 
|<nobr>├&nbsp;**Simulation Settings**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>│&nbsp;├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>│&nbsp;├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>├&nbsp;Primary Group</nobr>|| 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>├&nbsp;Additional Groups</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp;**Group 2**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 3**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 4**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 5**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 6**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 7**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>├&nbsp;**Group 8**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Select Bones</nobr>|| 
|<nobr>│&nbsp;├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>│&nbsp;├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>│&nbsp;├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>│&nbsp;├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**Physics Properties**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>│&nbsp;├&nbsp;**Parent-Child Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>│&nbsp;├&nbsp;**Lateral Joint**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**Collider**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
|<nobr>**Hair Physics**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;**Simulation Settings**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>├&nbsp;Spring</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp;Damp</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;Reduction Ratio</nobr>| [0.25] (0 ~ 1) | Reducing stiffness at each level
|<nobr>├&nbsp;Twist Limit</nobr>| [5] (0 ~ 180) | Limit tiwsting rotation
|<nobr>├&nbsp;Limit Force</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;Mass</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;Drag</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;Collider Radius</nobr>| [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.
|<nobr>├&nbsp;Collider Length</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), momiji bob, Preset 1,  |
|<nobr>**Dangling Physics**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;**Particle Dynamics**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;**Simulation Settings**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>├&nbsp;Spring</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp;Damp</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;Reduction Ratio</nobr>| [0.25] (0 ~ 1) | Reducing stiffness at each level
|<nobr>├&nbsp;Twist Limit</nobr>| [5] (0 ~ 180) | Limit tiwsting rotation
|<nobr>├&nbsp;Limit Force</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;Mass</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp;Drag</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
|<nobr>├&nbsp;Collider Length</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
|<nobr>**Detach Object**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Gravity</nobr>| [ON] | 
|<nobr>├&nbsp;Mass</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;Damp</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Collider</nobr>| Sphere | None, Sphere, Capsule, 
|<nobr>├&nbsp;Collider Radius</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp;Collider Length</nobr>| [0.3] (0 ~ 2) | 
|<nobr>Presets</nobr>| **Default (Reset)** | Default (Reset),  |
