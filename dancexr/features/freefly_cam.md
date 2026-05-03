---
layout: release
title: "./motion/proc/free_cam"
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

# ./motion/proc/free_cam

A fully manual camera mode where you control position and
rotation directly. Move freely through the scene, orbit around
a point, or lock on to an actor for tracking.


## Movement

**Movement Damping** smooths camera position changes — lower
values make the camera more responsive, higher values add
inertia for cinematic ease-in/out.

**Use Orbit Move** switches from free-flight to orbit mode,
where the camera rotates around a point 1.5 m in front of it
instead of translating freely. Useful for circling a subject.

**Restrict Vertical Move** (VR platforms only) prevents
unintentional height changes by snapping small vertical offsets
back to ground level.


## Lock On Target

When **Lock On Target** is enabled the camera automatically
tracks the selected actor. **Tracking Mode** chooses which
body part to follow (center, head, or chest). **Target
Smoothing** and **Prediction** reduce lag and jitter in the
follow. **Auto Zoom** adjusts the field of view to keep the
target at a consistent screen size, with **FOV Height At
Target** controlling the desired apparent height. **Camera
Shake** adds subtle handheld-style motion scaled by tracking
lag. **Lock Rotation** makes the camera also follow the
target's orientation.


## Presets

Four built-in presets cover common setups: *Freefly* (full
manual control), *Lock On Actor* (track without zoom), *Lock +
Zoom Fullbody*, and *Lock + Zoom Upper Body* (tighter framing
on the torso).



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Freefly</b>, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body, </td></tr>
<tr><td><strong>Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td>Predict position of the target to reduce lag caused by smoothing</td></tr>
<tr><td><strong>Lock On Target</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Automatically focus on target</td></tr>
<tr><td><strong>Camera Shake</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Lock Rotation</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Camera follows the rotation of the target</td></tr>
<tr><td><strong>Auto Zoom</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Automatically zoom in and out to maintain the target size in view</td></tr>
<tr><td><strong>Zoom Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Time it takes to zoom to target FOV</td></tr>
<tr><td><strong>FOV Height At Target</strong></td><td>Float</td><td>0.2 – 2</td><td>1</td><td></td><td>Vertical height for the target when using auto zoom</td></tr>
<tr><td><strong>Vertical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Offset vertically</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Movement Damping</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Use Orbit Move</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable or disable orbit movement, allowing the camera to rotate around a central point.</td></tr>
</tbody>
</table>

