---
locale: en-rUS
layout: single
title: Dangling Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[Prop](../menu#Prop) > Dangling Physics



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr> Select Bones</nobr>|| Select bones
|<nobr>![slider icon](/images/icon/ic_slider.png) Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>Particle Dynamics</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
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
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Collide With</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Head</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Body</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Butts</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Arms</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Hands</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Legs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Feet</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Player</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Simulation Settings</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable Dragging</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Simulate</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) Two Step Solving</nobr>| [OFF] | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Spring</nobr>| [0.5] (0 ~ 5) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Damp</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Reduction Ratio</nobr>| [0.25] (0 ~ 1) | Reducing stiffness at each level
|<nobr>![slider icon](/images/icon/ic_slider.png) Twist Limit</nobr>| [5] (0 ~ 180) | Limit tiwsting rotation
|<nobr>![slider icon](/images/icon/ic_slider.png) Limit Force</nobr>| [3] (0 ~ 8) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Mass</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Drag</nobr>| [1] (0 ~ 10) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Collider Radius</nobr>| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
|<nobr>![slider icon](/images/icon/ic_slider.png) Collider Length</nobr>| [0.9] (0 ~ 1) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
