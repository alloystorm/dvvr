---
layout: release
title: "Sex Overlay & Dildo"
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

# Sex Overlay & Dildo

Controls adult motion overlay and attachment props for an actor model.
This is a Pro-only feature and requires compatible skeletons.


## Pose

**Vertical Shift** raises or lowers the actor's root position — useful
for adjusting height relative to a partner or object. **Angle** sets
the forward/backward tilt of the motion axis, while **Random** adds
directional variance that fluctuates over time for organic feel.

**Arm IK Left** and **Arm IK Right** blend inverse-kinematics arm
correction so hands follow the body motion instead of floating in place.
Values above zero enable proportional IK influence.


## Motion

The motion subsystem drives rhythmic root offsets synced to the music
beat. Settings are managed by the nested Organic Motion panel, which
controls amplitude, frequency, and timing patterns.


## Attachment

The **Dildo** section configures a bone-attached prop with its own
model, surface material, and XRay cutaway. It can also drive hand
grab poses and leg IK when active.

# Sub-Components

## Motion

Reusable spring-driven thrust controller. A shaped driver curve
pushes one mass, a second mass trails behind it, and the gap
between them becomes the regulated travel used by paired motion
systems. This makes the cycle feel elastic rather than like a
raw sine wave.


### Tempo and Travel

**Extent** sets the maximum travel distance. **Auto Intensity**
can scale that travel from the current music level, while
**Auto BPM** and **Speed** control how quickly the cycle runs.
Use manual speed when you want consistent pacing; enable the
audio-driven controls when the motion should breathe with the
soundtrack instead.


### Driver Shape

**Top Duration**, **Bottom Duration**, and **Slope Balance**
shape the idealized cycle before the springs respond to it. A
longer top creates a held extension, a longer bottom creates a
more obvious reset, and slope balance shifts time between the
drive and return strokes. This is where you define whether the
motion feels punchy, even, or teasing.


### Spring Response

**Collision Distance** sets the resting separation between the
two spring masses. **Spring A**, **Damping A**, **Spring B**,
**Damping B**, and **Rest Spring** determine how tightly each
mass follows the driver and how much overshoot or softness is
left in the result. Stiffer values feel more mechanical; softer
values feel heavier but can get mushy if the cycle is fast.


### Visualization

**Visualize Curve** draws the target and spring responses in the
scene so you can tune the shape without guessing from the body
motion alone. It is a setup aid, not something you would keep on
during normal use.

## Dildo

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

