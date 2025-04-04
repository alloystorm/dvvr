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
|<nobr>Enable</nobr>| [ON] | 
|<nobr>Use Particle Dynamics</nobr>| [ON] | 
|<nobr><b>Simulation Settings</b></nobr>| | 
|<nobr>├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr><b>Primary Group</b></nobr>|| 
|<nobr>Select Bones</nobr>|| 
|<nobr>Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr><b>Particle Dynamics</b></nobr>| | 
|<nobr>├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>├&nbsp;Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp;Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp;Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>├&nbsp;Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>├&nbsp;Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>├&nbsp;Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>├&nbsp;Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr><b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr><b>Parent-Child Joint</b></nobr>| | 
|<nobr>├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr><b>Lateral Joint</b></nobr>| | 
|<nobr>├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr><b>Collider</b></nobr>| | 
|<nobr>├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>Additional Groups</nobr>| [0] (0 ~ 7) | 
|<nobr><b>Group 2</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 3</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 4</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 5</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 6</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 7</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr><b>Group 8</b></nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Select Bones</nobr>|| 
|<nobr>├&nbsp;Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;<b>Particle Dynamics</b></nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;<b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>├&nbsp;<b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;<b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;<b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;Use Primary Group Settings</nobr>| [ON] | 
|<nobr>Presets</nobr>| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
