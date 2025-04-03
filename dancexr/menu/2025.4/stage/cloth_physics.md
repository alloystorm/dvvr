---
locale: en-rUS
layout: single
title: Dangling Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/stage/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/stage/cloth_physics)

[Stage](../menu#Stage) > Dangling Physics



| Setting | Value | Description |
| :--- | --- | :--- |
| Enable Dangling Physics | ON | 0/13/True
| Select Bones || Select bones1/13/True
| Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels2/13/True
| **Particle Dynamics** | | 3/13/True
| ├ Enable Particle Dynamics | ON | 0/18/False
| ├ Swing Compliance | [0.25] (0 ~ 1) | 1/18/False
| ├ Twist Compliance | [0.75] (0 ~ 1) | 2/18/False
| ├ Particle Anchor | [0.5] (0 ~ 1) | 3/18/False
| ├ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level4/18/False
| ├ Visualize | OFF | 5/18/False
| ├ Max Angular Velocity | [2] (0 ~ 4) | 6/18/False
| ├ Inertia | [2] (1 ~ 5) | 7/18/False
| ├ Soften | [0] (0 ~ 1) | Soften the particle constraints.8/18/False
| ├ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters9/18/False
| ├ Gravity | [9.8] (-9.8 ~ 9.8) | 10/18/False
| ├ Friction | [1] (0 ~ 2) | 11/18/False
| ├ Ground Friction | [1] (-2 ~ 2) | 12/18/False
| ├ Drag (Air) | [0] (0 ~ 2) | Air resistancy13/18/False
| ├ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy14/18/False
| ├ Buoyancy | [-0.1] (-1 ~ 1) | 15/18/False
| ├ **Wind** | | 16/18/False
| │ ├ Wind Influence | [0.25] (0 ~ 1) | 0/3/False
| │ ├ Turbulence Scale | [0] (-2 ~ 2) | 1/3/False
| │ ├ Turbulence Intensity | [1] (0 ~ 2) | 2/3/False
| │ └ Turbulence Time Scale | [0] (-4 ~ 4) | 3/3/False
| ├ **Collide With** | | 17/18/False
| │ ├ Head | ON | 0/8/False
| │ ├ Body | ON | 1/8/False
| │ ├ Boobs | ON | 2/8/False
| │ ├ Butts | ON | 3/8/False
| │ ├ Arms | ON | 4/8/False
| │ ├ Hands | ON | 5/8/False
| │ ├ Legs | ON | 6/8/False
| │ ├ Feet | ON | 7/8/False
| │ └ Player | ON | 8/8/False
| └ **Simulation Settings** | | 18/18/False
|   ├ Use Global | ON | Find the global settings under Pro / Cloth Simulation0/10/False
|   ├ Enable Dragging | ON | 1/10/False
|   ├ Simulate | ON | 2/10/False
|   ├ Simulation FPS: Dynamic || 3/10/False
|   │ Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
|   ├ Time Scale | [0.65] (0.1 ~ 1) | 4/10/False
|   ├ Substeps | [4] (1 ~ 20) | 5/10/False
|   ├ Iterations | [1] (0 ~ 10) | 6/10/False
|   ├ Reverse Even Substeps | OFF | 7/10/False
|   ├ Alternate Group Size | [0] (0 ~ 20) | 8/10/False
|   ├ Table Size | [6] (1 ~ 20) | 9/10/False
|   └ Two Step Solving | OFF | 10/10/False
| Spring | [0.5] (0 ~ 5) | 4/13/True
| Damp | [0.01] (0 ~ 0.1) | 5/13/True
| Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level6/13/True
| Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation7/13/True
| Limit Force | [3] (0 ~ 8) | 8/13/True
| Mass | [0.05] (0 ~ 0.1) | 9/13/True
| Drag | [1] (0 ~ 10) | 10/13/True
| Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.11/13/True
| Collider Length | [0.9] (0 ~ 1) | 12/13/True
| Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone13/13/True
| Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
