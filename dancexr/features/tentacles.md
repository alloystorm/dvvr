---
layout: feature
title: "Tentacles"
locale: en-US
---

# Tentacles

Spawns and simulates procedural tentacle props attached to
the actor. Each tentacle is a segmented mesh driven by XPBD
physics with wiggle, coil, and attraction behaviors.

**Tentacle Count** and **Length** set the number and size.
The **Spawn** panel controls the cluster area: **Area Shape**
(Circle or Rectangle), **Area Size**, **Aspect Ratio**, and
**Length Distribution** for variation. **Radius**,
**Tapering**, and **Tip Radius** shape each tentacle's
thickness profile.

The **Behavior** panel drives animation: **Wiggle Speed**,
**Extent**, and **Lag** create organic sway; **Coil Extent**
and **Coil Fade** add spiral curling that fades toward the
tip. **Attraction** and **Attraction Offset** pull tentacle
tips toward a tracked body position. **Motion** syncs
movement to the sex motion system; **Motion Extent** scales
the response. **Back Out Distance** controls how far
tentacles retract.

**Material** and **X-Ray** sub-panels control appearance and
cross-section rendering. **Tentacle Props** defines global
physics parameters. Click **Rebuild Tentacles** after
changing count or spawn parameters to regenerate the mesh.

