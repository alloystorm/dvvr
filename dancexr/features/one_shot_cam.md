---
layout: release
title: One-Shot Cam
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

# One-Shot Cam

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



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Predict position of the target to reduce lag caused by smoothing</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Rotate Range</strong></td><td>Float</td><td>0 – 180</td><td>60</td><td></td><td>Horizontal rotation range.</td></tr>
<tr><td><strong>Distance</strong></td><td>Range</td><td>0.2 – 5</td><td></td><td></td><td></td></tr>
<tr><td><strong>Pitch Angle</strong></td><td>Range</td><td>-90 – 90</td><td></td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>The ease curve used when changing motion</td></tr>
<tr><td><strong>Prevent Below Floor</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Use Actor Orientation</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Raise Focus When Close</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Move focus position up when distance gets smaller</td></tr>
</tbody>
</table>

