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
| Enable | ON | 
| Select Bones || Select bones
| Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| **Particle Dynamics** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Swing Compliance | [0.25] (0 ~ 1) | 
| ├&nbsp;Twist Compliance | [0.75] (0 ~ 1) | 
| ├&nbsp;Particle Anchor | [0.5] (0 ~ 1) | 
| ├&nbsp;Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| ├&nbsp;Visualize | OFF | 
| ├&nbsp;Max Angular Velocity | [2] (0 ~ 4) | 
| ├&nbsp;Inertia | [2] (1 ~ 5) | 
| ├&nbsp;Soften | [0] (0 ~ 1) | Soften the particle constraints.
| ├&nbsp;Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| ├&nbsp;Gravity | [9.8] (-9.8 ~ 9.8) | 
| ├&nbsp;Friction | [1] (0 ~ 2) | 
| ├&nbsp;Ground Friction | [1] (-2 ~ 2) | 
| ├&nbsp;Drag (Air) | [0] (0 ~ 2) | Air resistancy
| ├&nbsp;Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| ├&nbsp;Buoyancy | [-0.1] (-1 ~ 1) | 
| ├&nbsp;**Wind** | | 
| │&nbsp;├&nbsp;Wind Influence | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;Turbulence Scale | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;Turbulence Intensity | [1] (0 ~ 2) | 
| │&nbsp;└&nbsp;Turbulence Time Scale | [0] (-4 ~ 4) | 
| ├&nbsp;**Collide With** | | 
| │&nbsp;├&nbsp;Head | ON | 
| │&nbsp;├&nbsp;Body | ON | 
| │&nbsp;├&nbsp;Boobs | ON | 
| │&nbsp;├&nbsp;Butts | ON | 
| │&nbsp;├&nbsp;Arms | ON | 
| │&nbsp;├&nbsp;Hands | ON | 
| │&nbsp;├&nbsp;Legs | ON | 
| │&nbsp;├&nbsp;Feet | ON | 
| │&nbsp;└&nbsp;Player | ON | 
| └&nbsp;**Simulation Settings** | | 
| &nbsp;&nbsp;├&nbsp;Use Global | ON | Find the global settings under Pro / Cloth Simulation
| &nbsp;&nbsp;├&nbsp;Enable Dragging | ON | 
| &nbsp;&nbsp;├&nbsp;Simulate | ON | 
| &nbsp;&nbsp;├&nbsp;Simulation FPS: Dynamic || 
| &nbsp;&nbsp;│&nbsp;Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| &nbsp;&nbsp;├&nbsp;Time Scale | [0.65] (0.1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Substeps | [4] (1 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;Iterations | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;Reverse Even Substeps | OFF | 
| &nbsp;&nbsp;├&nbsp;Alternate Group Size | [0] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;Table Size | [6] (1 ~ 20) | 
| &nbsp;&nbsp;└&nbsp;Two Step Solving | OFF | 
| Spring | [0.5] (0 ~ 5) | 
| Damp | [0.01] (0 ~ 0.1) | 
| Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
| Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
| Limit Force | [3] (0 ~ 8) | 
| Mass | [0.05] (0 ~ 0.1) | 
| Drag | [1] (0 ~ 10) | 
| Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| Collider Length | [0.9] (0 ~ 1) | 
| Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| Presets: Default (Reset) || 
| Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
