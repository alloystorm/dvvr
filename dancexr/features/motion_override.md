---
layout: release
title: "Motion Override"
locale: en-rUS
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

# Motion Override

Advanced tools to customize and enhance actor motion.
Integrates with the rigging system for precise control over
body, head, hand, and leg movements.

**Presets** include Free, Rocking Motion, Hoverbike, Rocking
Horse, Pole Motion, and Pole Blend. The **Body** panel
controls **Position** and **Rotation** locks, **Damping**,
**Lean**, **Bend**, **Height**, and **Forward/Back** offset.
**Rocking Motion** simulates rhythmic movement with
adjustable **Angle**, **Up/Down**, **Front/Back**, **Depth
Change**, and **Feet Motion** parameters.

The **Ride Model** panel spawns props like a hoverbike or
saddle with **Acceleration**, **Drag**, **Tilt When
Turning**, **Position**, **Rotation**, **Scale**, and
**Particle Effect** controls. **Head Pose** adds rotation
offsets to the neck and head. **Legs Pose** adjusts foot
placement dynamically. **Hand Poses** (left and right)
support presets and symmetric toggling.

Use cases include limiting dance motion range, creating
rocking horse animations, and converting dance into vehicle-
like motion with ride models and particle trails.

# Sub-Components

## Body

Nested config for body pose adjustments. **Position** and
**Rotation** switches lock specific axes. **Damping**
smoothes position tracking. **Lean**, **Bend**, **Twist**,
and **Head** rotate the torso and neck. **Height** and
**Forward/Back** translate the body. **Distance** mode
maintains proximity to a **Target Actor** within a
**Detect Range**, enforcing **Min** and **Max Distance**
bounds.

## Rocking Motion

Nested config for rhythmic rocking motion simulation.
**Rocking Angle** sets the arc, **Up/Down** and **Front/
Back** control translation amplitude. **Depth Change** and
**Depth Max** govern proximity oscillation. **Feet Motion**
blends foot movement with the rocking cycle. Includes a
**Motion Speed** sub-config for timing control.

## Head Pose

Nested config for head pose rotation offsets applied to the
neck and head bones. Controls **Rotation X**, **Y**, and
**Z** angles.

## Ride Model

Nested config for rideable prop models (hoverbike, saddle).
**Model** selects the prop type. **Acceleration** and
**Drag** control forward motion physics. **Tilt When
Turning** adds leaning during directional changes.
**Position**, **Rotation**, and **Scale** adjust the prop
attachment. **Particle Effect** enables exhaust spark VFX.
Computes velocity-based motion with drag and tilt filtering.

