---
layout: feature
title: "Softbody Physics"
locale: en-US
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


## Settings reference

<a id="settings-softbody-group"></a>
## Softbody group settings (Primary Group) {#primary-group}

Defines a softbody simulation group. Select bones via the
bone picker; child bones of selected roots become softbody
particles. Optional **Suspension** adds anchor joints to
root bones. **Anchor Along Axis** and **Anchor Offset**
control the softbody attachment point. Non-primary groups
can inherit the primary group's physics settings. The
nested XPBD panel defines particle stiffness, damping,
and collision parameters.

### Use Suspension {#use-suspension}

Adds a spring-damper suspension joint to a bone, anchoring
it to its parent with configurable **Anchor** position and
**Center Offset**. **Spring Force**, **Damping**, **Mass**,
and **Drag** control the joint dynamics. **Radius** sets
the collider size; **Rest Angle** adds a rotational bias.
**Rotation Limit** constrains swing and twist angles with
their own spring and damping. **Visualize Joints** renders
the constraint shape.

<a id="settings-shape-matching"></a>
### Shape matching (XPBD) {#xpbd}

Shape-matching softbody. Each selected bone becomes a surface particle
plus a locked inner anchor; overlapping clusters pull the surface back
toward its rest shape, allowing soft local deformation and jiggle.
**Depth** controls how far the inner anchors sit from the surface;
**Edge Depth** pulls edge anchors closer to the skeleton. **Stiffness**
sets how strongly the shape is restored each step (0 = floppy, 1 = rigid).

## Group 2 {#group-2}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-1"></a>
<a id="xpbd-1"></a>
## Group 3 {#group-3}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-2"></a>
<a id="xpbd-2"></a>
## Group 4 {#group-4}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-3"></a>
<a id="xpbd-3"></a>
## Group 5 {#group-5}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-4"></a>
<a id="xpbd-4"></a>
## Group 6 {#group-6}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-5"></a>
<a id="xpbd-5"></a>
## Group 7 {#group-7}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-6"></a>
<a id="xpbd-6"></a>
## Group 8 {#group-8}

See [Softbody group settings](#settings-softbody-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="use-suspension-7"></a>
<a id="xpbd-7"></a>
