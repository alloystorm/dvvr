---
locale: en-rUS
layout: single
title: Physics
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.5/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.5/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.5/stage/model_physics) | [简中](/zh/dancexr/menu/2025.5/stage/model_physics)

[Stage](../menu#Stage) > Physics

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| ☐ Disable PMX Physics | [OFF] | Disable PMX physics to use XPS tools instead
| ☑ Reduced Constraints | [ON] | Use the experimental setup that reduces constraints to allow smoother simulation
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Collision** | | 
| ├─☑ Static Inclusive | [ON] | 
| ├─☑ Static Exclusive | [ON] | 
| ├─☑ Dynamic Inclusive | [ON] | 
| └─☑ Dynamic Exclusive | [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Linear Movement** | | Settings for linear movements
| ├─☑ Restriction | Auto | Auto, Limited, Locked, Free, 
| ├─☑ Lock 0 Limit | [ON] | 
| ├─⊖ Min Spring Force | [5] (0 ~ 15) | 
| ├─⊖ Max Limit | [0.05] (0.05 ~ 0.1) | 
| ├─⊖ Bounciness | [0.5] (0 ~ 1) | 
| ├─⊖ Contact Distance | [0.5] (0 ~ 1) | 
| ├─⊖ Damping | [0.05] (0 ~ 1) | 
| └─⊖ Drag | [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Angular Movement** | | Settings for angular movements
| ├─☑ Restriction | Auto | Auto, Limited, Locked, Free, 
| ├─☑ Lock 0 Limit | [ON] | 
| ├─⊖ Min Spring Force | [5] (0 ~ 15) | 
| ├─⊖ Max Limit | [90] (3 ~ 90) | 
| ├─⊖ Bounciness | [0.5] (0 ~ 1) | 
| ├─⊖ Contact Distance | [0.5] (0 ~ 1) | 
| ├─⊖ Damping | [0.05] (0 ~ 1) | 
| └─⊖ Drag | [0.15] (0 ~ 1) | 
| ☑ **Linear Drive** | | Apply linear drive
| ├─☑ Enable | [ON] | 
| ├─⊖ Spring Force | [3] (0 ~ 5) | 
| └─⊖ Damping | [0.1] (0 ~ 1) | 
| ☑ **Angular Drive** | | Apply angular drive
| ├─☑ Enable | [ON] | 
| ├─⊖ Spring Force | [0.1] (0 ~ 5) | 
| └─⊖ Damping | [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Linear Motion** | | Settings for linear motion
| ├─⊖ Firmness | [0] (-1 ~ 1) | 
| ├─⊖ Main Drive Force | [5] (0 ~ 8) | 
| ├─⊖ Second Drive Force | [3] (0 ~ 8) | 
| ├─☑ Target Position | Zero | Zero, Center, Min, Max, 
| ├─☑ Lock When Possible | [ON] | 
| ├─☑ Acceleration Mode | [ON] | 
| ├─⊖ Damping | [0.05] (0 ~ 1) | 
| ├─⊖ Drag | [0.15] (0 ~ 1) | 
| └─☐ Ignore Limit | [OFF] | Further reducing constraints by ignoring joint limits
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Angular Motion** | | Settings for angular motion
| ├─⊖ Firmness | [0] (-1 ~ 1) | 
| ├─⊖ Main Drive Force | [5] (0 ~ 8) | 
| ├─⊖ Second Drive Force | [5] (0 ~ 8) | 
| ├─☑ Target Position | Zero | Zero, Center, Min, Max, 
| ├─☐ Lock When Possible | [OFF] | 
| ├─☑ Acceleration Mode | [ON] | 
| ├─⊖ Damping | [0.05] (0 ~ 1) | 
| ├─⊖ Drag | [0.15] (0 ~ 1) | 
| └─☐ Ignore Limit | [OFF] | Further reducing constraints by ignoring joint limits
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Options** | | 
| ├─⊖ Min Drag | [0] (0 ~ 1) | The min drag value in auto mode
| ├─⊖ Drag Scale | [1] (0 ~ 5) | The scale applied to drag values in auto mode
| ├─⊖ Min Mass | [0] (0 ~ 1) | The min mass value in auto mode
| ├─⊖ Mass Scale | [1] (0 ~ 10) | The scale applied to mass values in auto mode
| ├─☑ Center Of Mass | Zero | Auto, Zero, <br/>Set center of mass at zero or automatically based on position and size of each collider
| ├─⊖ Projection Dist | [0.05] (0 ~ 0.1) | Force reset the joint when distance between objects relative to neutral exceed this value
| └─⊖ Projection Angle | [5] (0 ~ 60) | Force reset the joint when angle between the objects relative to neutral exceed this value
| ⊖ Auto Reset Threshold | [35] (0 ~ 100) | Automatically reset the bone and its children when the velocity exceed this value
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Auto Reset** | | 
| └─⊖ Threshold | [30] (0 ~ 50) | 
| ☑ **Body Colliders** | | 
| ├─☑ Enable | [ON] | 
| ├─⊖ Size | [0.5] (0 ~ 1) | 
| ├─⊖ Head Radius | [1] (0 ~ 2) | 
| ├─⊖ Arm Radius | [1] (0 ~ 2) | 
| ├─⊖ Forearms | [1] (0 ~ 2) | 
| ├─⊖ Chest Width | [1] (0 ~ 2) | 
| ├─⊖ Waist Width | [0.5] (0 ~ 1) | 
| ├─⊖ Hips Width | [0] (-1 ~ 1) | 
| ├─⊖ Butts Radius | [1] (0 ~ 2) | 
| ├─ **Butts Position** || 
| ├─⊖ X | [0] (-0.1 ~ 0.1) | 
| ├─⊖ Y | [0] (-0.1 ~ 0.1) | 
| ├─⊖ Z | [0] (-0.1 ~ 0.1) | 
| ├─⊖ Belly Radius | [1] (0 ~ 2) | 
| ├─⊖ Belly Position | [0] (-1 ~ 1) | 
| ├─⊖ Leg Radius | [1] (0 ~ 2) | 
| ├─⊖ Thigh Fwd/Back | [0] (-1 ~ 1) | 
| ├─⊖ Thigh Start Position | [0] (0 ~ 1) | 
| ├─⊖ Hand | [0] (0 ~ 1) | 
| ├─☐ Visualize | [OFF] | 
| └─≡ Presets | **Default (Reset)** | Default (Reset), amy, misaki,  |
| ☑ **Hair Physics** | | 
| ├─☑ Enable | [ON] | 
| ├─ Select Bones || Select bones
| ├─⊖ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─☑ **Particle Dynamics** | | 
| │ ├─☑ Enable | [ON] | 
| │ ├─⊖ Swing Compliance | [0.25] (0 ~ 1) | 
| │ ├─⊖ Twist Compliance | [0.75] (0 ~ 1) | 
| │ ├─⊖ Particle Anchor | [0.5] (0 ~ 1) | 
| │ ├─⊖ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │ ├─☐ Visualize | [OFF] | 
| │ ├─⊖ Max Angular Velocity | [2] (0 ~ 4) | 
| │ ├─⊖ Inertia | [2] (1 ~ 5) | 
| │ ├─⊖ Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─⊖ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─⊖ Gravity | [9.8] (-9.8 ~ 9.8) | 
| │ ├─⊖ Friction | [1] (0 ~ 2) | 
| │ ├─⊖ Ground Friction | [1] (-2 ~ 2) | 
| │ ├─⊖ Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │ ├─⊖ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │ ├─⊖ Buoyancy | [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Wind** | | 
| │ │ ├─⊖ Wind Influence | [0.25] (0 ~ 1) | 
| │ │ ├─⊖ Turbulence Scale | [0] (-2 ~ 2) | 
| │ │ ├─⊖ Turbulence Intensity | [1] (0 ~ 2) | 
| │ │ └─⊖ Turbulence Time Scale | [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Collide With** | | 
| │ │ ├─☑ Head | [ON] | 
| │ │ ├─☑ Body | [ON] | 
| │ │ ├─☑ Boobs | [ON] | 
| │ │ ├─☑ Butts | [ON] | 
| │ │ ├─☑ Arms | [ON] | 
| │ │ ├─☑ Hands | [ON] | 
| │ │ ├─☑ Legs | [ON] | 
| │ │ ├─☑ Feet | [ON] | 
| │ │ └─☑ Player | [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Simulation Settings** | | 
| │   ├─☑ Use Global | [ON] | Find the global settings under Pro / Cloth Simulation
| │   ├─☑ Enable Dragging | [ON] | 
| │   ├─☑ Simulate | [ON] | 
| │   ├─> Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │   ├─⊖ Time Scale | [0.65] (0.1 ~ 1) | 
| │   ├─⊖ Substeps | [4] (1 ~ 20) | 
| │   ├─⊖ Iterations | [1] (0 ~ 10) | 
| │   ├─☐ Reverse Even Substeps | [OFF] | 
| │   ├─⊖ Alternate Group Size | [0] (0 ~ 20) | 
| │   ├─⊖ Table Size | [6] (1 ~ 20) | 
| │   └─☐ Two Step Solving | [OFF] | 
| ├─⊖ Spring | [1.25] (0 ~ 5) | 
| ├─⊖ Damp | [0.01] (0 ~ 0.1) | 
| ├─⊖ Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├─⊖ Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
| ├─⊖ Limit Force | [3] (0 ~ 8) | 
| ├─⊖ Mass | [0.01] (0 ~ 0.1) | 
| ├─⊖ Drag | [1] (0 ~ 10) | 
| ├─⊖ Collider Radius | [0.005] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├─⊖ Collider Length | [0.9] (0 ~ 1) | 
| ├─⊖ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └─≡ Presets | **Default (Reset)** | Default (Reset), momiji bob, Preset 1,  |
| ☑ **Dangling Physics** | | 
| ├─☑ Enable | [ON] | 
| ├─ Select Bones || Select bones
| ├─⊖ Skip First X Bones | [0] (0 ~ 5) | Do not create physics connection for the first x number of levels
| ├─☑ **Particle Dynamics** | | 
| │ ├─☑ Enable | [ON] | 
| │ ├─⊖ Swing Compliance | [0.25] (0 ~ 1) | 
| │ ├─⊖ Twist Compliance | [0.75] (0 ~ 1) | 
| │ ├─⊖ Particle Anchor | [0.5] (0 ~ 1) | 
| │ ├─⊖ Reduction Ratio | [0] (0 ~ 1) | Reducing mass at each level
| │ ├─☐ Visualize | [OFF] | 
| │ ├─⊖ Max Angular Velocity | [2] (0 ~ 4) | 
| │ ├─⊖ Inertia | [2] (1 ~ 5) | 
| │ ├─⊖ Soften | [0] (0 ~ 1) | Soften the particle constraints.
| │ ├─⊖ Particle Radius | [5] (1 ~ 20) | Size of particle in millimeters
| │ ├─⊖ Gravity | [9.8] (-9.8 ~ 9.8) | 
| │ ├─⊖ Friction | [1] (0 ~ 2) | 
| │ ├─⊖ Ground Friction | [1] (-2 ~ 2) | 
| │ ├─⊖ Drag (Air) | [0] (0 ~ 2) | Air resistancy
| │ ├─⊖ Drag (Underwater) | [1] (0 ~ 2) | Underwater resistancy
| │ ├─⊖ Buoyancy | [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Wind** | | 
| │ │ ├─⊖ Wind Influence | [0.25] (0 ~ 1) | 
| │ │ ├─⊖ Turbulence Scale | [0] (-2 ~ 2) | 
| │ │ ├─⊖ Turbulence Intensity | [1] (0 ~ 2) | 
| │ │ └─⊖ Turbulence Time Scale | [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Collide With** | | 
| │ │ ├─☑ Head | [ON] | 
| │ │ ├─☑ Body | [ON] | 
| │ │ ├─☑ Boobs | [ON] | 
| │ │ ├─☑ Butts | [ON] | 
| │ │ ├─☑ Arms | [ON] | 
| │ │ ├─☑ Hands | [ON] | 
| │ │ ├─☑ Legs | [ON] | 
| │ │ ├─☑ Feet | [ON] | 
| │ │ └─☑ Player | [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Simulation Settings** | | 
| │   ├─☑ Use Global | [ON] | Find the global settings under Pro / Cloth Simulation
| │   ├─☑ Enable Dragging | [ON] | 
| │   ├─☑ Simulate | [ON] | 
| │   ├─> Simulation FPS | **Dynamic** | Dynamic, Fixed 30, Fixed 60, Fixed 90, Fixed 100, Fixed 120, Fixed 160, Fixed 175, Fixed 240,  |
| │   ├─⊖ Time Scale | [0.65] (0.1 ~ 1) | 
| │   ├─⊖ Substeps | [4] (1 ~ 20) | 
| │   ├─⊖ Iterations | [1] (0 ~ 10) | 
| │   ├─☐ Reverse Even Substeps | [OFF] | 
| │   ├─⊖ Alternate Group Size | [0] (0 ~ 20) | 
| │   ├─⊖ Table Size | [6] (1 ~ 20) | 
| │   └─☐ Two Step Solving | [OFF] | 
| ├─⊖ Spring | [0.5] (0 ~ 5) | 
| ├─⊖ Damp | [0.01] (0 ~ 0.1) | 
| ├─⊖ Reduction Ratio | [0.25] (0 ~ 1) | Reducing stiffness at each level
| ├─⊖ Twist Limit | [5] (0 ~ 180) | Limit tiwsting rotation
| ├─⊖ Limit Force | [3] (0 ~ 8) | 
| ├─⊖ Mass | [0.05] (0 ~ 0.1) | 
| ├─⊖ Drag | [1] (0 ~ 10) | 
| ├─⊖ Collider Radius | [0.01] (0 ~ 0.05) | Size of the particle used when solving collision.
| ├─⊖ Collider Length | [0.9] (0 ~ 1) | 
| ├─⊖ Anchor Position | [0] (0 ~ 1) | Choose anchor position when creating joints. 0 = anchor at the parent bone, 1 = anchor at the child bone
| └─≡ Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2,  |
| ☑ **Detach Object** | | 
| ├─☑ Enable | [ON] | 
| ├─ Select Bones || 
| ├─☑ Gravity | [ON] | 
| ├─⊖ Mass | [0.1] (0 ~ 10) | 
| ├─⊖ Damp | [0] (0 ~ 1) | 
| ├─☑ Collider | Sphere | None, Sphere, Capsule, 
| ├─⊖ Collider Radius | [0.1] (0 ~ 1) | 
| └─⊖ Collider Length | [0.3] (0 ~ 2) | 
| ≡ Presets | **Default (Reset)** | Default (Reset),  |
