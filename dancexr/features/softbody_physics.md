---
layout: feature
title: "Softbody Physics"
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

# Softbody Physics

Connects selected bones with XPBD particle-based softbody
simulation to simulate jiggly or deformable body parts like
butts, belly, or chest.


## Group Management

The **Primary Group** is always active and has full control
over simulation parameters. **Additional Groups** adds up
to 7 more groups, each with its own bone selection.
Non-primary groups can inherit the primary group's settings
via **Use Primary Group Settings** to keep configuration
consistent.


## Bone Selection

Each group has a bone picker to select root bones. Child
bones of selected roots become softbody particles.
**Use Suspension** adds spring-damper anchor joints to root
bones for additional support. **Anchor Along Axis** and
**Anchor Offset** control how the softbody attaches to its
parent.


## Softbody Particles

The XPBD panel defines particle mesh parameters including
depth, layers, subdivision, and constraint stiffness. See
the Softbody sub-panel for detailed particle settings.


## Visualization

**Visualize Bodies** renders collider shapes for softbody
physics bodies. **Visualize Joints** shows joint limits for
softbody physics joints.


# Sub-Components

## Primary Group

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 2

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 3

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 4

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 5

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 6

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 7

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

## Group 8

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

### XPBD

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

