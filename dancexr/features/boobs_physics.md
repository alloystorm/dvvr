---
layout: feature
title: "Boobs Physics"
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

# Boobs Physics

Adds physics simulation to breast bones on the model. Selected bones
are given suspension joints that allow them to bounce and sway with
movement, plus optional collision shapes that interact with arms
and the ground.


## Bone Selection

Use **Select Bones** to pick which bones receive physics. Opens a
bone picker dialog starting from the torso — select one or two bones
(left and right). Presets let you save and restore configurations
across different models.


## Suspension

Adds spring-damper joints that anchor each bone to its parent.
Controls bounce, sway, and rotation limits. See the Suspension
sub-panel for detailed joint settings.


## Collision

Enables SDF collider shapes (cone-like capsules) around each breast
bone so they interact with arms, clothing, and the ground.
**Collider Radius** and **Collider Length** set the overall size.
**Collider Curve** shapes the profile — negative values make it
more bulbous, positive values taper it toward the tip.
**Enable Nipple** adds a small spherical collider with adjustable
**Nipple Position** and **Nipple Size**. **Friction** controls how
surfaces slide against the collider. **Collide With Arms** assigns
the collider to a separate layer for arm-specific interactions.
**Visualize** renders the 3D collider meshes for debugging.

Both **Collider Curve** and **Enable Nipple** are designed to work
with cloth simulation, giving clothing something to slide against.


## Softbody

Overlays a particle-based XPBD softbody on the child bones of each
selected root, adding jiggle deformation on top of the rigid
suspension physics. See the Softbody sub-panel for particle
settings.


# Sub-Components

## Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

## Softbody

Defines a particle-based XPBD softbody mesh that deforms with
physics. Child bones of each selected root become simulation
particles arranged in layers extending outward. **Depth** controls
how far particles extend from the bone; **Edge Depth** pulls edge
particles closer to the skeleton for a tighter fit. **Layers**
and **Subdivision** increase mesh resolution at the cost of
performance. **Depth Distribution** shifts volume between inner
and outer layers.

The constraint sliders (**Volume**, **Edge**, **Rotation**) control
particle stiffness — higher values mean less deformation.
**Constraint Damping** smooths oscillation between solver steps.
**Inertia** adds resistance to rapid movement changes.
**Show Bones** renders the original skeleton bones alongside the
particle mesh for comparison.

