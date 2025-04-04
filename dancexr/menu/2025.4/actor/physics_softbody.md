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

Drive additional control bones using particle dynamics.

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Simulation Settings</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable Dragging</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Simulate</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Reverse Even Substeps</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Two Step Solving</nobr>| [OFF] | 
|<nobr> <b>Primary Group</b></nobr>|| 
|<nobr> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Additional Groups</nobr>| [0] (0 ~ 7) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 2</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 3</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 4</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 5</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 6</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 7</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Group 8</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> Select Bones</nobr>|| Select bones
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Anchor Along Axis</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Anchor Offset</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Primary Group Settings</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Particle Dynamics</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>Joints</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Include Center</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Volume Constraint</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Internal Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Surface Constraint</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotation Constraint</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Edge Lock</nobr>| [0.85] (0.5 ~ 1) | Lock particles on the edge.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center Lock</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Visualize</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Angular Velocity</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Inertia</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Soften</nobr>| [0] (0 ~ 1) | Soften the particle constraints.
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Particle Radius</nobr>| [5] (1 ~ 20) | Size of particle in millimeters
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Gravity</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Friction</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ground Friction</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Air)</nobr>| [0] (0 ~ 2) | Air resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag (Underwater)</nobr>| [1] (0 ~ 2) | Underwater resistancy
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Buoyancy</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Wind</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Wind Influence</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Collide With</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Head</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Body</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Boobs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Butts</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Arms</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Legs</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Feet</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Player</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Boobs** | Boobs, Butts, Legs, tina, 预设1, 预设2,  |
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset),  |
