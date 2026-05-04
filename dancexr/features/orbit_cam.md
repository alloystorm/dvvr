---
layout: release
title: "[Orbit Cam]"
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

# [Orbit Cam]

Manual and automatic orbit camera that rotates around the focused actor.

## Manual Control

When not in auto mode, drag to orbit the camera around the actor.
**Use Controller Input** enables gamepad/VR controller support for orbiting.
**Prevent Below Floor** stops the camera from moving beneath the ground plane.

**Retain Velocity** keeps the camera spinning after you release input, gradually
slowing down. **Min Speed** and **Max Speed** clamp the retained rotation speed —
raise *Max Speed* for long cinematic spins, or lower it for tighter control.

## Auto Mode

When enabled, the camera orbits automatically with configurable distance, pitch,
and height that cycle using sine waves.

**Distance Min** and **Distance Max** set the near/far range the camera moves
through each cycle. **Distance Cycle** is the period in seconds for a full
back-and-forth cycle.

**Pitch Min** and **Pitch Max** control the vertical angle range, and
**Pitch Cycle** sets how fast the camera tilts up and down.

**Height Min** and **Height Max** adjust the vertical offset of the camera target,
with **Height Cycle** controlling the oscillation period.

**Speed** sets how fast the camera orbits horizontally when auto mode is active.
Increase it for fast sweeping shots, or lower it for slow, deliberate circles.

