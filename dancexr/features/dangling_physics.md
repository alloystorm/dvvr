---
layout: feature
title: "Dangling Physics"
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

# Dangling Physics

Applies chain physics to dangling parts of the model such as
ribbons, scarves, tails, and loose accessories. Works like hair
physics but tuned for heavier, slower movement with lower spring
stiffness for more exaggerated swinging.


## Bone Selection

Use **Select Bones** to pick root bones of dangling parts — the
system automatically traverses children to build the chain.
**Skip First X Bones** leaves root bones unattached for a firmer
base. **Max Levels** caps chain depth (0 = unlimited). Presets
let you save configurations across different models.


## Physics Mode

**Auto** follows the system-wide default. **PhysX** uses
joint-based rigid body physics with capsule or sphere colliders.
**XPBD** uses a particle-based simulation that can be more stable
for long chains and interacts with the scene collision layers.
The mode determines which settings panel is shown.


## PhysX Settings

Visible when using PhysX mode. **Spring Force** (logarithmic)
controls stiffness — lower values than hair physics give a looser,
more dramatic sway. **Damping** reduces oscillation. **Stiffness
Reduction** softens the spring at each chain level so tips flop
more freely than the base. **Twist Limit** constrains rotation
around the bone axis. **Limit Force** controls how hard the joint
pushes back against its constraints. **Mass** is higher than hair
by default for more momentum. **Drag** adds air resistance.
**Collider Radius** sets the collision sphere size; **Collider
Length** scales it along the bone as a capsule. **Anchor Position**
chooses where the joint attaches (0 = parent bone, 1 = child bone).


## XPBD Chain

Visible when using XPBD mode. Configures particle-based chain
simulation with **Rotation Compliance**, **Twist Compliance**,
**Stiffness Reduction**, **Mass Reduction**, and **Constraint
Damping**. **Particle Anchor** controls attachment position.
Collision layer is set to Cloth for interaction with the rest
of the scene.


## Visualization

**Visualize Bodies** renders collider shapes for physics bodies.
**Visualize Joints** shows joint limits and drive targets as
wireframe gizmos.


# Sub-Components

## XPBD

Configures particle-based chain or mesh simulation for hair,
cloth, and other dangling parts. **Rotation Compliance** controls
how much the chain bends at each joint (higher = more flexible).
**Twist Compliance** controls rotation around the bone axis.
For mesh mode, **Lateral Compliance** adds cross-connections
between adjacent chains.

**Stiffness Reduction** (power-of-10 scale) multiplies compliance
at each level — values above 1 make the chain progressively looser
toward the tip. **Mass Reduction** (power-of-2 scale) reduces mass
at each level. **Particle Anchor** positions the joint along the
segment. **Constraint Damping** smooths oscillation between solver
steps. **Inertia** adds resistance to movement changes.
**Particle Radius** sets the collider size in millimeters.
**Use Sphere Shape** replaces capsule particles with spheres for
debugging.

