---
layout: release
title: Physics System
locale: en-US
toc: true
---

# Physics System

DanceXR has a physics page for almost every body part — hair, skirt, breast, dangling, cloth, soft body, ragdoll, particle. They are not redundant: each handles a different kind of motion, and several of them stack. This page is the map.

For terms (rigid body, joint, type A/B colliders, projection distance), see [Concepts & glossary](/dancexr/concepts#bones-physics-and-colliders).

> The detailed parameter reference for the system-wide physics dialog and the per-PMX-model dialog lives at [Physics (settings reference)](/dancexr/features/physics).

---

## The two paths: PMX vs XPS

The biggest decision branch is the model format.

| | PMX | XPS |
|---|---|---|
| Has a physics rig? | Yes — built into the file | No — set up in DanceXR |
| Default behavior | Works out of the box | Nothing moves until configured |
| Where you tune | [PMX physics](/dancexr/features/pmx_physics) (per-actor) | [XPS physics](/dancexr/features/xps_physics) (per-actor) |
| Common gotcha | Joint stiffness from the model author may need overriding | You have to **select bones** for hair, breast, skirt before they do anything |

Both paths share the system-level dialog (gravity, simulation steps) and the same family of specialized rigs below.

---

## System-level settings

Two pages set the rules for the whole simulation, regardless of model format:

- [System physics](/dancexr/features/system_physics) — engine-level configuration, performance bounds.
- [Simulation](/dancexr/features/simulation) — global gravity, simulation steps per second, master enable.

Steps per second matters more than people expect: too few steps and joints jitter; too many and FPS tanks. Match it roughly to your target frame rate.

---

## The rig family

These are the per-body-part physics rigs. Most of them work on both PMX and XPS, but some are XPS-specific because PMX models already include their own rigid bodies for the same parts.

### Body shape

[Body colliders](/dancexr/features/body_colliders) — capsule colliders along the actor's body, used so freely-moving parts (hair, cloth, skirt) collide with the body instead of clipping through.

### Hair

[Hair physics](/dancexr/features/hair_physics) — spring-bone simulation on a tree of bones rooted at the head. Set the root bones and DanceXR walks the children to build the rig.

### Skirt and dangling

- [Skirt physics](/dancexr/features/skirt_physics) — chain physics with horizontal connections (mesh-like), suited to skirts and hems.
- [Dangling physics](/dancexr/features/dangling_physics) — chain physics without horizontal connections, suited to ribbons, ties, ear chains, animal tails, anything that hangs.

The difference is whether nearby chains are linked horizontally. Skirts collapse without those links; ribbons hang awkwardly with them.

### Breast

[Boobs physics](/dancexr/features/boobs_physics) — joint-based jiggle on breast bones, with counter-gravity to compensate for the constant downward pull. XPS-relevant because PMX models usually have their own breast joints in-file.

### Cloth (mesh-based)

- [Cloth simulation](/dancexr/features/cloth_simulation) — Unity cloth-style simulation on garment meshes.
- [Mesh to cloth](/dancexr/features/mesh_to_cloth) — convert a mesh on the model into a cloth-simulated object.

These differ from skirt/dangling chain physics: cloth simulates the whole mesh, not a small set of control bones. Heavier; better for dramatic, full-garment motion.

### Soft body

- [Soft body physics](/dancexr/features/softbody_physics) — volumetric deformation. <!-- TODO: confirm primary use cases. -->
- [Particle dynamics](/dancexr/features/particle_dynamics) — particle-based secondary motion.

### Whole-body

- [Ragdoll](/dancexr/features/ragdoll) — physics takes over the whole skeleton; the actor goes limp.
- [Detach object](/dancexr/features/detach_object) — release a bone or object so physics drives it independently.
- [Secondary motion](/dancexr/features/secondary_motion) — procedural layer that adds breath, sway, and follow-through on top of an existing motion.

---

## Choosing what to use

| Want | Reach for |
|---|---|
| Hair to swing | [Hair physics](/dancexr/features/hair_physics) — set root bones |
| Skirt to flare | [Skirt physics](/dancexr/features/skirt_physics) (XPS), or [PMX physics](/dancexr/features/pmx_physics) (PMX) |
| A ribbon, tail, or tie to hang | [Dangling physics](/dancexr/features/dangling_physics) |
| Breast jiggle on XPS | [Boobs physics](/dancexr/features/boobs_physics) — assign bones |
| A whole garment to sim like fabric | [Cloth simulation](/dancexr/features/cloth_simulation) |
| Body parts to feel volumetric | [Soft body physics](/dancexr/features/softbody_physics) |
| Actor to fall over | [Ragdoll](/dancexr/features/ragdoll) |
| To remove a body part dynamically | [Detach object](/dancexr/features/detach_object) |
| A subtle alive feel on top of any motion | [Secondary motion](/dancexr/features/secondary_motion) |
| Hair / cloth to actually collide with the body | [Body colliders](/dancexr/features/body_colliders) |

---

## Common problems

| Symptom | Likely cause |
|---|---|
| Hair / cloth clips through the body | [Body colliders](/dancexr/features/body_colliders) not set up, or *Disable Collision* is on in [physics settings](/dancexr/features/physics) |
| Hair selected but nothing moves | Selected bones may not be roots; check [Example bone structure](/dancexr/features/bones) |
| Boobs do not move | The boobs physics toggle is on but bones are not assigned — see [boobs physics](/dancexr/features/boobs_physics) |
| Bones drift away over time | Reduce *Projection distance* / *Projection angle*, or enable *Reset on change* in [physics settings](/dancexr/features/physics) |
| Jitter at high FPS | Increase steps per second in [simulation](/dancexr/features/simulation) |
| FPS drops when physics is on | Reduce steps per second; turn off heavy rigs (cloth, soft body) you do not need |
| Skirt looks like a stiff cone | You have dangling rather than skirt physics; switch ([skirt](/dancexr/features/skirt_physics) vs [dangling](/dancexr/features/dangling_physics)) |

---

## Related pages

- [Concepts & glossary](/dancexr/concepts#bones-physics-and-colliders)
- [Working with actors](/dancexr/actors)
- [Physics (settings reference)](/dancexr/features/physics) — system-wide and PMX-specific dialog parameters
- [XPS physics](/dancexr/features/xps_physics) — XPS rig configuration
- [Example bone structure](/dancexr/features/bones) — reference skeletons for bone selection

<!-- TODO Phase 3: resolve duplicate pages — cloth_sim.md vs cloth_simulation.md, physics_softbody.md vs softbody_physics.md, transparency.md vs material_transparent.md. Also consider renaming features/physics.md to features/pmx_physics_settings.md to make this hub the canonical "Physics" entry. -->
