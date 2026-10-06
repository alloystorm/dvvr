---
layout: release
title: Simulation
locale: en-US
---

# Simulation: choose the right tool

DanceXR uses particle simulation for cloth, bone-driven movement and soft bodies. Choose the tool by what the model already contains and what you want to move; their controls and anchoring requirements differ.

| Goal | Tool | Starting point |
|---|---|---|
| Run a PMX model's authored physics rig | [PMX Physics](pmx_physics) | Keep the authored bone, rigid-body and joint setup, then tune its simulation. |
| Add movement to a mapped bone chain | [Hair](hair_physics), [Dangling](dangling_physics) or [Skirt Physics](skirt_physics) | Select the relevant bones and inspect their connections. |
| Turn an existing garment mesh into simulated cloth | [Mesh to Cloth](mesh_to_cloth) | Select the mesh and choose the region that remains anchored. |
| Create a separate procedural cloth surface | [Cloth Simulation](cloth_simulation) | Choose shape, resolution, materials and anchors. |
| Deform a volume around control bones | [Softbody Physics](softbody_physics) or [Boobs Physics](boobs_physics) | Check particle layout and the supported body region. |
| Simulate flowing particles | Fluid simulation | Start small and tune cohesion, viscosity and collision. |

## Particle dynamics {#particle-dynamics}

Particle-based tools use constraints to keep particles connected. **Compliance** sets how readily a constraint yields: higher compliance gives a softer connection. Drag, inertia and particle properties influence movement, while anchors determine where the simulated structure is supported.

Bone-chain tools expose swing and twist compliance; skirts also use lateral connections. These are different from a legacy spring-and-damping setup, so do not copy numeric spring values directly into compliance controls. Use the detailed tool's reference for its units and ranges.

## Wind and collision {#wind-and-turbulence}

Global wind and per-group wind influence affect participating simulations. Turbulence adds variation; a wind field supplies localized forces. If the effect is too strong, reduce the individual group's wind influence before changing the whole scene.

Check [Body Colliders](body_colliders) when cloth passes through the actor. A misplaced or oversized collider can look like a cloth-stiffness problem. Review collider geometry and anchors before increasing simulation strength.

## Soft bodies {#softbody}

Volume constraints help preserve shape; distance constraints affect softness. Use visualization in the owning [softbody tool](softbody_physics) to inspect particle depth, layers and locked edges. Select appropriate control bones and test a small movement before tuning the entire region.

## A practical tuning order

1. Confirm the selected bones or mesh and the supported/anchored area.
2. Run a restrained motion with wind disabled and inspect collisions.
3. Adjust compliance and drag one control at a time.
4. Add wind or interaction after the basic shape behaves correctly.
5. Review [System Physics](system_physics) if several tools behave poorly together; reset physics after a large pose or setup change.

A stable solver does not guarantee a correct setup. Incorrect anchors, collisions or very dense meshes can still cause poor results or excessive cost.
