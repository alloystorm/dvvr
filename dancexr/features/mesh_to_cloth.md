---
layout: feature
title: "Mesh To Cloth"
locale: en-US
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---

# Mesh To Cloth

Mesh To Cloth converts any existing render mesh on an actor — such
as a jacket, skirt panel, or accessory — into a particle-based cloth
simulation. Instead of moving rigidly with the skeleton, the
converted mesh drapes, swings, and wrinkles dynamically in response
to motion, wind, and collision. This is the feature to use when a
garment looks stiff during animation and you want it to behave like
real fabric.

The feature works alongside the procedural [cloth
simulation](/dancexr/features/cloth_sim) system, but where cloth
sim generates entirely new meshes, Mesh To Cloth repurposes existing
geometry. This makes it ideal for character models that ship with
modelled clothing but lack simulation — you get physics without
rebuilding the garment from scratch.

Because each converted mesh runs its own simulation, performance
scales with the number of meshes and their vertex count. Convert only
the pieces that need dynamic behaviour (a long coat, loose sleeves)
and leave fitted items (tight pants, belts) as static meshes.


## Configuration

Every render mesh on the actor body gets its own config panel once
Mesh To Cloth is enabled. The panel contains the controls described
below. Meshes that are close-fitting or have very few vertices may
not simulate convincingly — favour meshes with loose geometry and
sufficient polygon density.

### Pinned Vertices

Pinned vertices are the points where the simulated mesh stays
attached to the skeleton. To anchor a coat's shoulders to the
character's collarbone bones, pin the vertices that lie over those
bones. The fewer vertices you pin, the more freely the cloth moves;
the more you pin, the closer the simulation stays to the original
rigid mesh.

The vertex selection is bone-driven: specify which bones anchor their
overlapping vertices. For a skirt, pin the waist bones and leave the
hem unpinned. If the entire mesh flies off or collapses, you have
too few pins. If it hardly moves at all, you have too many.

### Gradual Enable

**Gradual Enable** controls how many seconds the simulation takes to
fade in when you toggle it on. A value of 0 applies the simulation
instantly — the mesh may snap from its rigid pose to its simulated
rest state, causing a visible pop. A value of 1–3 seconds blends the
transition smoothly, which is the recommended approach for on-stage
equips or scene transitions.

This is especially useful when you enable Mesh To Cloth mid-scene
and don't want the audience to notice the simulation kicking in.

### Simulation Parameters

These properties live in the **Particle Props** sub-panel and apply
globally to all converted meshes:

- **Stiffness** — resistance to bending. High stiffness keeps the
  mesh rigid, close to its original form. Low stiffness lets it fold
  and drape like soft fabric. For a leather jacket keep stiffness
  high; for a silk scarf set it low.
- **Damping** — how quickly particle motion decays. Low damping
  produces lively, bouncy cloth that oscillates. High damping produces
  heavy, sluggish cloth that settles quickly. Start at 0.5 and adjust
  by feel.
- **Gravity Multiplier** — scales the force of gravity on the
  simulated particles. A value of 1.0 is standard gravity. Values
  below 1.0 produce floaty, zero-G behaviour (good for fantasy
  effects). Values above 1.0 make the cloth heavy and droopy.
- **Wind** — applies a directional force that pushes the cloth,
  useful for outdoor scenes or dramatic entrances. Pair with the
  [ground](/dancexr/features/ground) stage's environment settings
  for coherent wind direction across the whole scene.

Tuning these parameters interactively is the fastest path to a good
look — start with the fabric type you are going for (stiff for armour,
loose for silk) and then adjust damping and gravity to match the
desired weight and response speed.


## Workflow Tips

1. **Start with one mesh** — enable Mesh To Cloth on a single garment
   piece first, tune its parameters, then add more. This isolates
   performance and behaviour.
2. **Use Gradual Enable** when adding simulation to an already-visible
   mesh to avoid snapping.
3. **Pin conservatively** — start with 2–4 bone anchors and add more
   only if the mesh drifts off the body.
4. **Watch for intersections** — a too-stiff cloth pinned at too-few
   points may clip through the body. Increase stiffness or add more
   pins to resolve this.
5. **Combine with cloth simulation** — use Mesh To Cloth for the
   character's existing garments and [cloth sim](/dancexr/features/cloth_sim)
   to generate additional overlaid clothing like scarves or capes.
6. **Performance monitoring** — if frame rate drops after converting
   a mesh, reduce its particle resolution by checking whether a
   lower-poly version of the mesh is available, or increase damping
   to reduce computational cost per particle.
