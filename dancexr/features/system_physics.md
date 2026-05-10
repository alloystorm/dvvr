---
layout: feature
title: "System Physics"
locale: en-US
---

# System Physics

Global physics engine selection, timestep settings, and gravity for the scene.


## Default Engines

**PMX Default** sets the physics engine used for PMX models with built-in rigidbodies and joints (hair, skirts, accessories). Choose *PhysX* for Unity's joint-based physics, *XPBD* for a particle-based simulation, or *Off* to disable and free those bones for the XPS custom physics tools.

**Custom Physics Default** sets the engine for the XPS tools (Hair Physics, Cloth Physics, Softbody, etc.). XPBD is more stable for cloth; PhysX may be faster on some hardware.


## PhysX Settings

**Gravity** sets the downward force applied to all rigidbodies. Set it to zero for a zero-gravity stage. **Disable Collision** prevents XPS particle systems from colliding with each other, which can reduce jitter when multiple soft bodies interact.


## XPBD Settings

Holds simulation parameters for the XPBD engine — see the XPBD Settings sub-data for details.


## Time

**Time Scale** slows or accelerates the physics simulation independently of animation playback speed. Lower values make particles and soft bodies move in slow motion. **Physics FPS** locks the simulation to a fixed timestep: lower values reduce CPU load, higher values improve stability at the cost of performance. *Flexible* lets the simulation run at the render framerate.


# Sub-Components

## XPBD Settings

Holds XPBD solver settings: substeps, iterations, collision interval, self-collision, body collision, ground friction, expand radius, and parallel solving.

