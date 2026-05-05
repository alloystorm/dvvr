---
layout: feature
title: "Motion Override"
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

# Motion Override

Advanced motion control system that overrides and enhances
actor movement through rigging adjustments. Useful for
limiting dance ranges, creating vehicle simulations, or
adding rhythmic animations like rocking motions.

## Presets

Quick-start configurations include **Free** (minimal
override), **Rocking Motion**, **Hoverbike**, **Rocking
Horse**, **Pole Motion**, and **Pole Blend**. Each preset
enables and configures relevant sub-panels automatically.

## Body Controls

**Position Lock** restricts movement along horizontal,
vertical, or both axes — useful for keeping actors in
frame. **Rotation Lock** prevents the torso from turning
with the dance. **Damping** smooths position changes
(higher = slower response). **Lean**, **Bend**, and
**Twist** rotate the torso, while **Height** and
**Forward/Back** shift the body. **Distance** mode
maintains a set range from a target actor.

## Rocking Motion

Simulates rhythmic movement with **Angle** (arc width),
**Up/Down** and **Front/Back** (translation amplitude),
and **Depth Change** (proximity oscillation). **Feet
Motion** blends foot movement with the rocking cycle.
Timing is controlled via the **Motion Speed** sub-config.

## Ride Model

Attaches a prop (hoverbike or saddle) with **Acceleration**
and **Drag** physics. **Tilt When Turning** leans the
prop during direction changes. Adjust **Position**,
**Rotation**, and **Scale** to fit the actor. Enable
**Particle Effect** for exhaust spark VFX trailing the
vehicle.

## Hand and Leg Poses

**Hand Poses** (left/right) offer gesture presets and
custom finger control with IK modes for grabbing or
pointing. **Legs Pose** adjusts foot placement with
symmetry support. **Head Pose** adds rotation offsets.


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

## Leg Pose

Nested config for leg and foot placement. **Left** and
**Right** sub-panels adjust **Foot X/Y/Z** positions,
**Foot Rotate X/Y/Z** angles, **Toe** bend, and **Open**
(leg spread). **Symmetrical** links both sides. **Relative
To Floor** bases foot offsets on the floor plane instead
of the hip. **Max Twist** limits how far the torso angle
can drift from the legs. Presets: *Sit*, *Ride*, *Kneel*,
*Stand*.

## Left Hand

Nested config for hand pose control. Choose a **Gesture**
preset or use **Custom Pose** to adjust individual
finger bends. **Position** and **Rotation** offset the
hand in space. **Rotation Type** sets the coordinate
frame (reference bone, self, absolute, or none).
**Reference Bone** and **Reference Actor** anchor the
hand to another body part or actor. **IK Mode**
switches between normal, cylinder, sphere, or align
IK solvers. **Blend Hand Motion** fades the pose
based on distance. **Symmetrical** links left/right
poses.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Right Hand

Nested config for hand pose control. Choose a **Gesture**
preset or use **Custom Pose** to adjust individual
finger bends. **Position** and **Rotation** offset the
hand in space. **Rotation Type** sets the coordinate
frame (reference bone, self, absolute, or none).
**Reference Bone** and **Reference Actor** anchor the
hand to another body part or actor. **IK Mode**
switches between normal, cylinder, sphere, or align
IK solvers. **Blend Hand Motion** fades the pose
based on distance. **Symmetrical** links left/right
poses.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Ride Model

Nested config for rideable prop models (hoverbike, saddle).
**Model** selects the prop type. **Acceleration** and
**Drag** control forward motion physics. **Tilt When
Turning** adds leaning during directional changes.
**Position**, **Rotation**, and **Scale** adjust the prop
attachment. **Particle Effect** enables exhaust spark VFX.
Computes velocity-based motion with drag and tilt filtering.

