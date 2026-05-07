---
layout: feature
title: "Mesh To Cloth"
locale: en-US
---

# Mesh To Cloth

Converts any render mesh on the actor into a particle-based cloth
simulation. Each mesh gets its own config panel for selecting
pinned vertices (bones that anchor the cloth) and simulation
parameters.

**Gradual Enable** fades the simulation in over a set number of
seconds, preventing the mesh from snapping into place abruptly.
The nested **Particle Props** panel defines global physics
properties like stiffness, damping, and gravity multiplier that
apply to all converted meshes.

