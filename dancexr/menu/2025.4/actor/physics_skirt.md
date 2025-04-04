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
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Use Particle Dynamics</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Simulation Settings</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Dragging</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Simulate</nobr>| [ON] | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Two Step Solving</nobr>| [OFF] | 
|<nobr> <b>Primary Group</b></nobr>|| 
|<nobr> Select Bones</nobr>|| 
|<nobr>![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>![slider icon](/images/icon/ic_slider.png) Additional Groups</nobr>| [0] (0 ~ 7) | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 2</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 3</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 4</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 5</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 6</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 7</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 8</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Closed Loop</nobr>| [ON] | Bones for closed loops at each level
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Compliance</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Parent-Child Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Lateral Joint</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Linear Drive</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Angular Drive</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drive Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Rate</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lock Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collider</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
