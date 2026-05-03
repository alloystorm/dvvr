---
layout: release
title: "[Long Take]"
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

# [Long Take]

Long-take camera that moves randomly each beat while following the actor.

## Movement

**Rotate Range** limits how far left or right the camera can orbit around
the actor. Wider ranges create sweeping shots; narrower ranges keep the
camera more front-facing.

The **Curve** value controls the easing when the camera moves to a new
random position each beat. Negative values start slow and speed up;
positive values start fast and slow down; *0* gives linear motion.

## Distance & Pitch

Sets the range for camera distance and vertical angle. The camera picks
a random position within these limits each beat.

**Distance** controls how far the camera is from the target — lower values
for close-ups, higher for wider shots.

**Pitch Angle** sets the vertical tilt range. Negative values look down
at the actor; positive values look up.

## Orientation

Enable **Use Actor Orientation** to align the camera with the actor's
facing direction, so the camera stays relative to where the actor is
looking.

Enable **Raise Focus When Close** to automatically move the focus point
upward as the camera gets nearer, keeping the actor's head in frame
for close-up shots.

**Prevent Below Floor** stops the camera from moving beneath the ground
plane.

