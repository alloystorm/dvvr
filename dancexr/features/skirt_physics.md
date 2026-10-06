---
layout: feature
title: "Skirt Physics"
locale: en-US
---

# Skirt Physics

Adds physics simulation to skirt or dress meshes on the
model. Supports up to 8 bone groups with configurable
joints, colliders, and particle-based mesh deformation.


## Group Management {#group-management}

The **Primary Group** is always active and defines the main
physics chain. **Additional Groups** adds up to 7 more
groups, each with its own bone selection. Non-primary
groups can inherit settings from the primary group or
override them via **Override Physics**.


## Bone Selection {#bone-selection}

Each group has a **Select Bones** picker to choose root
bones. **Sorting** organizes bones for lateral connections
— *Shortest Path*, *Circular*, *Linear*, or *No Sorting*.
**Closed Loop** connects the first and last bone at each
level for seamless ring structures. **Skip First X Bones**
excludes initial levels from physics, keeping the waist
area firm.


## Physics Mode {#physics-mode}

**Auto** follows the system-wide default. **PhysX** uses
joint-based rigid body physics with box, capsule, or sphere
colliders. **XPBD** uses a particle-based mesh simulation
for more stable, continuous deformation. The mode
determines which settings panel is shown.


## PhysX Settings {#physx-settings}

Visible when using PhysX mode. Contains nested panels for
**Physics Properties** (mass, drag, friction, solver
iterations), **Parent-Child Joint** (swing/twist drive),
**Lateral Joint** (linear/angular connections between
adjacent bones), and **Collider** parameters (type, radius,
length). **First Collider Length** is typically shorter to
avoid interference with body colliders.


## XPBD Settings {#xpbd-settings}

Visible when using XPBD mode. Configures particle-based
mesh simulation via the XPartMesh system with rotation,
twist, and lateral compliance values.


## Visualization {#visualization}

**Visualize Bodies** renders collider shapes for physics
bodies. **Visualize Joints** shows joint limits and drive
targets as wireframe gizmos.


## Settings reference

<a id="settings-skirt-group"></a>
## Skirt group settings (Primary Group) {#primary-group}

Nested config for a single skirt physics group. **Select
Bones** picks the root bone chain. **Sorting** organizes
bones for lateral connections. **Closed Loop** connects the
first and last bone at each level. **Skip First X Bones**
excludes initial levels from physics. **Physics Mode**
chooses PhysX or XPBD (primary group only). **Visualize
Bodies/Joints** shows debug geometry. Contains nested
**PhysX Settings** with Physics Properties, Parent-Child
Joint, Lateral Joint, and Collider sub-configs, or an
**XPBD Settings** particle mesh config.

### Physics Properties {#physics-properties}

Defines base physics parameters for rigid body simulation.
**Mass** and **Drag** control how bones respond to forces
and air resistance. In mesh mode, **Horizontal Overlap**
adjusts collider side-to-side coverage, and **Mass
Distribution** reduces mass at each successive level.
**Friction** affects surface sliding during collisions.
**Solver Iterations** controls collision resolution accuracy
— higher values are more stable but cost more performance.
**Center Of Mass** chooses between auto-calculated (based
on collider shapes) or zero-centered positioning.

### Parent-Child Joint {#parent-child-joint}

Configures the joint connecting each bone to its parent.
**Swing Drive** controls stiffness for bending away from
the rest pose; **Twist Drive** resists rotation around the
bone axis. **Drive Damping** (squared) reduces oscillation.
**Reduction Rate** multiplies stiffness at each chain level
— values below 1 make the chain progressively looser.
**Anchor Position** chooses where the joint attaches (0 =
parent bone, 1 = child bone).

### Lateral Joint {#lateral-joint}

Configures connections between adjacent bones at the same
chain level, creating mesh-like behavior. **Linear Drive**
resists positional separation; **Angular Drive** resists
rotational differences. **Drive Damping** (squared) smooths
oscillation. **Reduction Rate** multiplies stiffness at each
level. **Lock Y** and **Lock Z** constrain lateral movement
along specific axes for stiffer behavior.

### Collider {#collider}

Nested config for physics collider parameters. **Collider
Type** selects Box, Capsule, or Sphere shapes. **Collider
Radius** sets the size. **Collider Length** and **First
Collider Length** control elongation, with the first level
typically shorter to avoid body interference.

<a id="settings-particle-mesh"></a>
### XPBD mesh settings (XPBD Settings) {#xpbd-settings-1}

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

## Group 2 {#group-2}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-1"></a>
<a id="parent-child-joint-1"></a>
<a id="lateral-joint-1"></a>
<a id="collider-1"></a>
<a id="xpbd-settings-2"></a>
## Group 3 {#group-3}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-2"></a>
<a id="parent-child-joint-2"></a>
<a id="lateral-joint-2"></a>
<a id="collider-2"></a>
<a id="xpbd-settings-3"></a>
## Group 4 {#group-4}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-3"></a>
<a id="parent-child-joint-3"></a>
<a id="lateral-joint-3"></a>
<a id="collider-3"></a>
<a id="xpbd-settings-4"></a>
## Group 5 {#group-5}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-4"></a>
<a id="parent-child-joint-4"></a>
<a id="lateral-joint-4"></a>
<a id="collider-4"></a>
<a id="xpbd-settings-5"></a>
## Group 6 {#group-6}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-5"></a>
<a id="parent-child-joint-5"></a>
<a id="lateral-joint-5"></a>
<a id="collider-5"></a>
<a id="xpbd-settings-6"></a>
## Group 7 {#group-7}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-6"></a>
<a id="parent-child-joint-6"></a>
<a id="lateral-joint-6"></a>
<a id="collider-6"></a>
<a id="xpbd-settings-7"></a>
## Group 8 {#group-8}

See [Skirt group settings](#settings-skirt-group). Defaults and available controls for this instance are listed in Config Reference.

<a id="physics-properties-7"></a>
<a id="parent-child-joint-7"></a>
<a id="lateral-joint-7"></a>
<a id="collider-7"></a>
<a id="xpbd-settings-8"></a>
