---
layout: feature
title: "Simulation"
locale: en-US
---

# Simulation

Generates and simulates clothing meshes on the actor model.
Supports two independent cloth layers with configurable
topology, anchoring, materials, and fluid particle effects.


## Cloth Layers

**Cloth 1** and **Cloth 2** each define a separate garment
with its own mesh topology, anchor points, and material.
Use **Rebuild Mesh** to regenerate the geometry after
changing shape parameters. Presets include skirts, tops,
and string configurations.


## Materials

Each cloth layer has a **Material** panel for surface
shading, texture selection, and detail mapping. Supports
transparent rendering and audio-reactive visualization
modes.


## Fluid Simulation

An experimental particle shower system that spawns fluid
droplets with configurable spawn position, auto-aim,
cohesion, and viscosity. See the Fluid sub-panel for
detailed particle behavior settings.


## Collision

**Geometry Colliders** creates SDF body shapes for cloth
to collide against. **Mesh Collider** generates tetrahedral
colliders from the actor's skinned mesh for more accurate
collision with arbitrary geometry.


# Sub-Components

## Cloth 1

Configures a procedurally generated cloth mesh. **Topology**
selects the particle grid layout — *Adaptive Hexagon*,
*Adaptive Rectangle*, *Horizontal/Vertical Layout*, or
*String* variants. **Inner Radius** sets the waist opening
size. **Slope** controls flare angle (0 = tube, 90 = flat
disc). **Arc** shapes the profile — positive for balloon,
negative for bell shape. **Length** sets garment length.

For horizontal layouts, **Arm Holes** and **Arm Hole Height**
carve openings. For vertical layouts, **Back Length** and
**Side Length** scale the mesh independently, and **Split
Interval** creates gaps in the mesh. **Horizontal** and
**Vertical Resolution** set particle spacing. **Distance
Compliance** controls stretchiness. **Damping** reduces
oscillation. **UV Mapping** selects texture projection mode.
**Particle Radius** sets collision size.

### Anchor

Configures how the cloth mesh attaches to the actor's
skeleton. **Top Anchor** and **Bottom Anchor** define the
upper and lower attachment points using bone-relative
positions and rotations. The cloth spans between these two
anchor rings, with attraction strength controlling how
tightly particles follow the anchor bones during simulation.

## C1 Material

Configures the surface appearance of a cloth mesh. Supports
solid color textures, detail maps, and transparent rendering.
**Audio Visualization** mode replaces surface settings with
reactive frequency/beat patterns that animate the material
properties in real-time.

**Surface** controls roughness and metalness. **Texture**
selects from ground pattern presets or solid color.
**Detail Map** adds secondary surface noise. **Transparent**
enables alpha blending for see-through garments.

## Cloth 2

Configures a procedurally generated cloth mesh. **Topology**
selects the particle grid layout — *Adaptive Hexagon*,
*Adaptive Rectangle*, *Horizontal/Vertical Layout*, or
*String* variants. **Inner Radius** sets the waist opening
size. **Slope** controls flare angle (0 = tube, 90 = flat
disc). **Arc** shapes the profile — positive for balloon,
negative for bell shape. **Length** sets garment length.

For horizontal layouts, **Arm Holes** and **Arm Hole Height**
carve openings. For vertical layouts, **Back Length** and
**Side Length** scale the mesh independently, and **Split
Interval** creates gaps in the mesh. **Horizontal** and
**Vertical Resolution** set particle spacing. **Distance
Compliance** controls stretchiness. **Damping** reduces
oscillation. **UV Mapping** selects texture projection mode.
**Particle Radius** sets collision size.

### Anchor

Configures how the cloth mesh attaches to the actor's
skeleton. **Top Anchor** and **Bottom Anchor** define the
upper and lower attachment points using bone-relative
positions and rotations. The cloth spans between these two
anchor rings, with attraction strength controlling how
tightly particles follow the anchor bones during simulation.

## C2 Material

Configures the surface appearance of a cloth mesh. Supports
solid color textures, detail maps, and transparent rendering.
**Audio Visualization** mode replaces surface settings with
reactive frequency/beat patterns that animate the material
properties in real-time.

**Surface** controls roughness and metalness. **Texture**
selects from ground pattern presets or solid color.
**Detail Map** adds secondary surface noise. **Transparent**
enables alpha blending for see-through garments.

## Fluid

An experimental particle-based fluid simulation system.
Spawns up to 1000 particles with configurable physics
including cohesion, viscosity, gravity, and surface
interaction. Particles can render as points or as scaled
droplets with PBR material properties.

### Spawn

Controls particle generation — fixed position, hand/mouse
aiming, or auto-tracking. Configure rate, speed, spread,
and lifetime.

### Fluid

Defines particle interaction physics: cohesion strength,
viscosity, stickiness, and target spacing. Presets include
water, viscous fluid, and sand-like granular behavior.

### Render

Toggles point cloud vs droplet mesh rendering. Droplet size
can scale with local fluid density. Material properties
include color, metallic, smoothness, glow, and transparency.

### Spawn

Configures where and how fluid particles are generated.
Supports three spawn modes: fixed position relative to the
actor, VR/mouse hand control, and auto-aim tracking.

**Position** and **Rotation** set the fixed spawn point.
**Spawn Radius** and **Spread** control particle dispersion.
**Spawn Rate** sets particles per second. **Speed** controls
initial velocity. **Max TTL** is the particle lifetime before
respawn. **TTL on Floor** is how long puddles persist.
**Smoothing** damps the auto-aim target tracking.

### Fluid

Defines particle interaction physics. **Cohesion** pulls
particles together into streams. **Cohesion Range** sets the
maximum distance for cohesion effects. **Target Distance**
is the minimum particle separation when cohesion is off.
**Viscosity** resists flow for thicker fluids. **Stick To
Surface** controls how strongly particles adhere to geometry.

Presets: *Water* (light, cohesive), *Viscous* (thick,
sticky), *Sand* (no cohesion, granular).

## Geometry Collider

Defines SDF (signed distance field) body capsule shapes that
cloth and physics systems collide against. Each body part
(head, neck, chest, ribs, waist, belly, butts, arms, legs,
etc.) is a configurable capsule with position, radius, and
curve parameters.

Shapes scale with actor morphs to maintain proper collision
geometry across body types. **Visible** toggle shows collider
wireframes in the scene. Organized into sections: head, body,
arms, and legs. NSFW builds include additional hole collider
configurations.

## Mesh Collider

Generates tetrahedral collision geometry from the actor's
skinned mesh renderers. Unlike SDF capsule colliders, mesh
colliders conform to arbitrary model geometry for accurate
collision with custom clothing, accessories, or props.

Select individual meshes to enable as colliders. Each mesh
has an **Exclusion** panel to disable specific bones from
contributing collision surfaces. **Depth** controls the
offset thickness of the collision shell. **Visualize**
renders the generated collider mesh in the scene.

