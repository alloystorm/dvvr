---
locale: en-rUS
layout: single
title: Dangling Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/stage/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/stage/cloth_physics)

[Stage](../menu#Stage) > Dangling Physics



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>Enable</nobr>| [ON] | 
|<nobr>Select Bones</nobr>|| Select bones
|<nobr>Skip First X Bones</nobr>| [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
|<nobr>**Particle Dynamics**</nobr>| | 
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Swing Compliance</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;Twist Compliance</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;Particle Anchor</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;Reduction Ratio</nobr>| [0] (0 ~ 1) | Reducing mass at each level
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
|<nobr>├&nbsp;**Wind**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Wind Influence</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Turbulence Scale</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Turbulence Intensity</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;Turbulence Time Scale</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;**Collide With**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Head</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Body</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Boobs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Butts</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Arms</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Hands</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Legs</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Feet</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;Player</nobr>| [ON] | 
|<nobr>└&nbsp;**Simulation Settings**</nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Use Global</nobr>| [ON] | Find the global settings under Pro / Cloth Simulation
|<nobr>&nbsp;&nbsp;├&nbsp;Enable Dragging</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Simulate</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Simulation FPS</nobr>| **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Time Scale</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Substeps</nobr>| [4] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Iterations</nobr>| [1] (0 ~ 10) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Reverse Even Substeps</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Alternate Group Size</nobr>| [0] (0 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Table Size</nobr>| [6] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;└&nbsp;Two Step Solving</nobr>| [OFF] | 
|<nobr>Spring</nobr>| [0.5] (0 ~ 5) | 
|<nobr>Damp</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>Reduction Ratio</nobr>| [0.25] (0 ~ 1) | Reducing stiffness at each level
|<nobr>Twist Limit</nobr>| [5] (0 ~ 180) | Limit tiwsting rotation
|<nobr>Limit Force</nobr>| [3] (0 ~ 8) | 
|<nobr>Mass</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>Drag</nobr>| [1] (0 ~ 10) | 
|<nobr>Collider Radius</nobr>| [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
|<nobr>Collider Length</nobr>| [0.9] (0 ~ 1) | 
|<nobr>Anchor Position</nobr>| [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
|<nobr>Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
