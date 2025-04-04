---
locale: en-rUS
layout: single
title: Softbody Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/physics_softbody) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_softbody) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_softbody) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_softbody) | [简中](/zh/dancexr/menu/2025.4/actor/physics_softbody)

[Physics](../menu#Physics) > Softbody Physics



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
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
|<nobr> Select Bones</nobr>|| Select bones
|<nobr>![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
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
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![slider icon](/images/icon/ic_slider.png) Additional Groups</nobr>| [0] (0 ~ 7) | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 2</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 3</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 4</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 5</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 6</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 7</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Group 8</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp; Select Bones</nobr>|| Select bones
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Anchor Along Axis</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Anchor Offset</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Primary Group Settings</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>Joints</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Include Center</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Damping</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Visualize</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Friction</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Wind</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Body</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Boobs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Butts</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Legs</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset),  |
