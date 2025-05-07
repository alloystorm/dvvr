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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Particle Dynamics</nobr>| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps</nobr>| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations</nobr>| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Reverse Even Substeps</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size</nobr>| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size</nobr>| [6] (1 ~ 20) | 
| └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Two Step Solving</nobr>| [OFF] | 
|  <b>Primary Group</b></nobr>|| 
|  Select Bones</nobr>|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Additional Groups</nobr>| [0] (0 ~ 7) | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 2</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 3</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 4</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 5</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 6</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 7</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 8</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
| ├─ Select Bones</nobr>|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Sorting</nobr>| **Shortest Path** | Shortest Path, Circular, Linear, No Sorting, <br/>Set sorting method used when making lateral connections. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Closed Loop</nobr>| [ON] | Bones for closed loops at each level
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Compliance</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Lateral Anchor</nobr>| [0] (0 ~ 0.5) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Body</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Boobs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Butts</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Legs</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Physics Properties</b></nobr>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Horizontal Overlap</nobr>| [-0.2] (-1 ~ 1) | Overlap of colliders horizontally
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Mass Distribution</nobr>| [0] (-1 ~ 1) | Reduce mass at each level
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Solver Iterations</nobr>| [20] (1 ~ 150) | Number of iterations when solving collision
| │ └─<img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Center Of Mass</nobr>| Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Parent-Child Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Lateral Joint</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Linear Drive</nobr>| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angular Drive</nobr>| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Drive Damping</nobr>| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Reduction Rate</nobr>| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Y</nobr>| [OFF] | 
| │ └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lock Z</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collider</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Radius</nobr>| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Collider Type</nobr>| **Box** | Box, Capsule, Sphere,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Collider Length</nobr>| [0.8] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> First Collider Length</nobr>| [0.5] (0 ~ 1) | Reducing lenght of collider for the first level of bones to avoid interference from body colliders.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset), hurrah, nyotengu cheongsam, nyo birthday, Preset 1, Preset 2, Preset 3, Preset 4, Preset 5, Preset 6, 预设1,  |
