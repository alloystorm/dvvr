---
layout: feature
title: "Physics"
locale: en-US
---

# Physics

Configures physics for PMX models that include built-in
rigidbody and joint definitions (hair, skirts, accessories).

**Physics Mode** selects the engine: *Auto* uses the system
default; *PhysX* runs Unity's joint-based physics; *XPBD*
uses a particle-based simulation; *Off* disables PMX physics
entirely and exposes the XPS physics tools (Hair Physics,
Cloth Physics, etc.) as replacements.

**Visualize Bodies** and **Visualize Joints** render the
physics shapes and joint constraints as wireframe gizmos.
The nested **Particle Props** panel defines global XPBD
settings like gravity, stiffness, and damping.

**Linear Motion** and **Angular Motion** tune the PhysX
joint drive response — how aggressively bodies follow their
animated targets. **Options** exposes advanced PhysX
parameters like solver iterations and substep count.
**Auto Reset Threshold** snaps bones back to their animated
position when velocity exceeds the limit, preventing physics
from spinning out of control.

Each **Group** section corresponds to a physics joint group
defined in the PMX file, with per-group enable/disable,
gravity, and collision settings.

The **XPS Tools** section provides quick links to the
alternative physics systems available when PMX physics is
turned off.

