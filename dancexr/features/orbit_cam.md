---
layout: release
title: "./motion/proc/orbit_cam"
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

# ./motion/proc/orbit_cam

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
<tr><td><strong>Use Controller Input</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Prevent Below Floor</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Retain Velocity</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Maintain the rotation when there is no input</td></tr>
<tr><td><strong>Max Speed</strong></td><td>Float</td><td>0 – 30</td><td>15</td><td></td><td>Maximum rotation speed</td></tr>
<tr><td><strong>Min Speed</strong></td><td>Float</td><td>0 – 30</td><td>0</td><td></td><td>Minimum rotation speed</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Auto Mode</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Distance Min</strong></td><td>Float</td><td>0 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Distance Max</strong></td><td>Float</td><td>1 – 10</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>Distance Cycle</strong></td><td>Float</td><td></td><td>12</td><td></td><td></td></tr>
<tr><td><strong>Pitch Min</strong></td><td>Float</td><td>-45 – 0</td><td>-15</td><td></td><td></td></tr>
<tr><td><strong>Pitch Max</strong></td><td>Float</td><td>0 – 45</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>Pitch Cycle</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>Height Min</strong></td><td>Float</td><td>-1 – 0</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Height Max</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Height Cycle</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>Speed</strong></td><td>Float</td><td>0 – 90</td><td>10</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

