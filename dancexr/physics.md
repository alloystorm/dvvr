---
layout: release
title: Physics System
locale: en-US
toc: true
---

# Physics System

DanceXR has model format-specific physics systems for character models, plus a custom built XPBD (extended particle-based dynamics) system that can be used to simulate cloth, soft body and simplified rigid bodies. 

PMX models come with physics component definitions and it should work out of the box. You can customize and fine-tune the physics behavior for PMX models in the [PMX physics settings](features/pmx_physics). 

For XPS and FBX models, you need to set up physics from scratch using the provided physics tools tailered for common usecases. See below for the list of tools and their recommended use cases. 

By default the physics system uses the built-in Unity physics engine based on PhysX. We also have a custom made physics engine based on XPBD (Extended Position-Based Dynamics) which provides better control and stability especially for cloth and hair.

For terms (rigid body, joint, colliders, spring force, damping, projection distance, projection angle), see [Concepts & glossary](concepts#bones-physics-and-colliders).

---

## Physics Tools

The physics tools are a collection of tools that allow you to quickly set up physics for your models. Each individual tool focuses on a particular use case, minimizing the number of parameters you need to tweak to get a good result. Most of the time you only need to select the right bone to get the desired behavior. There are also presets to help you quickly find good settings and and visualization for understanding the effect of each parameter.

- [Body colliders](features/body_colliders) — capsule colliders along the actor's body, used so freely-moving parts (hair, cloth, skirt) collide with the body instead of clipping through.
- [Hair physics](features/hair_physics) — spring-bone simulation on a tree of bones rooted at the head. Set the root bones and DanceXR walks the children to build the rig.
- [Skirt physics](features/skirt_physics) — chain physics with horizontal connections (mesh-like), suited to skirts and hems.
- [Dangling physics](features/dangling_physics) — chain physics without horizontal connections, suited to ribbons, ties, ear chains, animal tails, anything that hangs.
- [Boobs physics](features/boobs_physics) — joint-based jiggle on breast bones, with counter-gravity to compensate for the constant downward pull. 
- [Soft body physics](features/softbody_physics) — connecting bones with a mesh of spring force constraints to simulate volumetric deformation on body parts like butts and thighs.
- [Detach object](features/detach_object) — release a bone or object so you can remove certain parts by making it drop off. Useful when they don't have separate materials to hide them with transparency.
- [Auto Reset](features/auto_reset) — automatically reset physics components when velocity reaches a certain threshold, to prevent explosions.

Demo video:
{% include video id="-IZTzHUpROs" provider="youtube" %}

---

## Simulation System

The simulation system is a custom built XPBD (extended particle-based dynamics) system that can be used to simulate cloth, soft body and fluid. 

- [Cloth simulation](features/cloth_simulation) — adding cloth to the model.
- [Mesh to cloth](features/mesh_to_cloth) — convert a mesh on the model into a cloth-simulated object.
- Fluid simulation — simulate simple fluid effect like viscosity with particles.
- [Tentacle simulation](features/tentacles) — simulating tentacles movement by connecting nodes with constraints and drive force.

---

## Settings

You can control the physics behavior with the following settings.

- [System-level physics settings](features/system_physics) — global settings that apply to all physics simulations in DanceXR, regardless of model format or rig type.
- [PMX physics settings](features/pmx_physics) — PMX-specific settings that override the physics definitions from the model file.
- Physics Tools:
    - [Body colliders](features/body_colliders) — size and position of the colliders along the body.
    - [Hair physics](features/hair_physics) — spring force, damping, collider radius, and bone selection for hair physics.
    - [Skirt physics](features/skirt_physics) — spring force, damping, collider radius, and bone selection for skirt physics.
    - [Dangling physics](features/dangling_physics) — spring force, damping, collider radius, and bone selection for dangling physics.
    - [Boobs physics](features/boobs_physics) — spring force, damping, collider radius, bone selection, and counter-gravity for boobs physics.
    - [Soft body physics](features/softbody_physics) — particle size, constraint compliance, and bone selection for soft body physics.
    - [Detach object](features/detach_object) — bone selection for detach object.
    - [Auto Reset](features/auto_reset) — velocity threshold for auto reset.
- [Cloth Simulation settings](features/cloth_simulation) — mesh creation parameters, simulation parameters, and collider adjustments for cloth simulation. It includes
    - Cloth Mesh 1
    - Cloth Mesh 2
    - Fluid Simulation
    - Mesh To Cloth
- [Tentacle Simulation settings](features/tentacles) — node count, spring force, damping, and collider radius for tentacle simulation.
- [Ragdoll settings](features/ragdoll) — joint limits, spring force, damping, and collider radius for ragdoll simulation.

---

## Further reading

- [Concepts & glossary](concepts#bones-physics-and-colliders)
- [Working with actors](actors)
- [Example bone structure](features/bones) — reference skeletons for bone selection

