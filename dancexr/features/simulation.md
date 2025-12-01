---
locale: en-US
layout: single
title: Simulation
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/simulation) | [繁中](/tw/dancexr/features/simulation) | [日本語](/jp/dancexr/features/simulation) | [한국어](/kr/dancexr/features/simulation) | [简中](/zh/dancexr/features/simulation)

## Simulation Overview

DanceXR's simulation system includes advanced particle dynamics, cloth simulation, and experimental fluid simulation, offering realistic and performant physics for various use cases.

---

### Particle Dynamics

The particle dynamics system replaces traditional physics for hair, clothing, and skirts, providing smoother and more stable results.

- **Key Configurations**:
  - Inertia
  - Swing compliance
  - Twist compliance
  - Reduction ratio
  - Particle anchor
  - Lateral compliance and anchor (for skirts)

- **Wind and Turbulence**:
  - Global wind settings for speed and direction
  - Turbulence forces for individual groups
  - Wind fields for localized effects like fans or tunnels

- **Improved Simulation (v2025.11)**:
  - Better line simulation
  - Vertical layout cloth that supports split strips
  - Enhanced cloth material properties with audio visualization support and transparency

---

### Cloth Simulation

The cloth simulation system supports XPS and PMX models with features like unbreakable stability and custom curved colliders.

- **Configurations**:
  - Mesh creation with adjustable radius, length, slope, and resolution
  - Anchoring to body parts
  - Interaction settings for dragging and tearing
  - Self-collision and physics properties
  - **Physics Improvements (v2025.10)**:
    - New shear and bend constraints for skirt physics
    - Improved stability of collision and friction solving
    - Support for complex colliders like holes

- **Performance Tips**:
  - Use a fixed frame rate for optimal simulation
  - Adjust collider shapes for model-specific tuning

- **Underwater Behavior**:
  - Buoyancy and drag settings for underwater simulations

---

### Fluid Simulation (Experimental)

The fluid simulation extends the particle system to simulate fluid behavior.

- **Attributes**:
  - Cohesion force
  - Viscosity
  - Stickiness

- **Rendering**:
  - Fluid particles rendered as points or spheres
  - Fluid shaders coming in future updates

- **Use Cases**:
  - Simulate scenarios like showers, fountains, or garden hoses

---

### Additional Features

- **Soft Body Simulation**:
  - Realistic soft body physics for body parts like boobs, butts, and legs
  - Volume and distance constraints for fine-tuning
  - Visualization tools for particle connections

- **LipSync and Spatial Audio**:
  - LipSync generates facial movements from audio
  - Spatial audio plays sound from actor positions in 3D space

For more details, refer to the [release notes](/dancexr/releases).
