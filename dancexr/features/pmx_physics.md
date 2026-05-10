---
layout: feature
title: "Physics"
locale: en-US
---

# Physics

Configures physics for PMX models that include built-in rigidbody
and joint definitions — typically used for hair, skirts, and accessories.


## Physics Mode

Selects the simulation engine. *Auto* uses the system default; *PhysX*
runs Unity's joint-based physics; *XPBD* uses a particle-based simulation
for more stable, elastic movement; *Off* disables PMX physics entirely and
exposes the XPS physics tools (Hair Physics, Cloth Physics, etc.) as
replacements.


## Particle Props

Available only in XPBD mode. Controls global XPBD parameters — particle
size, mass, damping, gravity response, and collision layers. **Scale**
auto-updates with the music for audio-reactive particle sizing.


## Linear / Angular Motion

Available only in PhysX mode. Tune how aggressively joints drive bodies
back toward their animated targets. **Main Drive Force** and **Second Drive
Force** set spring stiffness; **Damping** and **Drag** absorb energy;
**Lock When Possible** keeps joints fixed when motion is minimal;
**Acceleration Mode** uses acceleration-based drive for snappier response.


## Options

Available only in PhysX mode. Advanced solver parameters: **Min Mass**
and **Mass Scale** prevent bodies from becoming too light; **Min Drag**
and **Drag Scale** do the same for drag. **Center Of Mass** sets it to
zero or computes it from collider positions. **Projection Angle** and
**Projection Dist** force-reset joints that deviate beyond these thresholds,
preventing joints from stretching under fast motion.


## Groups

Each section corresponds to a physics joint group defined in the PMX file.
Enable or disable groups individually. When **Override Configs** is on,
per-group *Linear Motion* and *Angular Motion* override the global
Linear/Angular settings — useful to make a stiff skirt and soft hair coexist.
**Visualize Joints** and **Visualize Colliders** render that group's shapes.


## Auto Reset

When joint velocity exceeds **Auto Reset Threshold**, the bone and its
children snap back to their animated position — prevents physics from
spinning out of control on impact or extreme motion.


## XPS Tools

Links to alternative physics systems available when PMX physics is turned
off: Hair Physics, Cloth Physics, Boobs Physics, Skirt Physics, and more.


# Sub-Components

## Particle Properties

Holds particle size, mass, damping, gravity, friction, and collision layers for the XPBD physics system used in PMX physics mode.

## Linear Motion

Holds spring force, damping, drag, and drive mode for a PhysX joint axis. Used per-group to override global Linear/Angular motion settings.

## Angular Motion

Holds spring force, damping, drag, and drive mode for a PhysX joint axis. Used per-group to override global Linear/Angular motion settings.

## Options

Holds mass scaling, drag scaling, center of mass mode, and projection thresholds for the PhysX joint solver. Used to fine-tune joint stability and prevent stretching under fast motion.

