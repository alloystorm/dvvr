---
layout: release
title: "./motion/proc/concert_cam"
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

# ./motion/proc/concert_cam

Fixed camera positioned at a set location, always looking at the focused actor.

## Framing

**Size** controls how large the target actor appears in the camera view.
Lower values zoom in for a tighter frame; higher values show more of the
surrounding scene.

**Target Center** shifts the focal point up or down on the actor's body.
Negative values focus lower (legs/feet); positive values focus higher
(chest/head).

## Position

**Offset** moves the camera's fixed position in 3D space. Use this to
place the camera exactly where you want it relative to the scene origin.

**Shift** tilts the camera up or down while keeping its fixed position.
This changes the angle of view without moving the camera location.

## Field of View

**FOV** controls how wide the camera lens is. Lower values act like a
telephoto lens (narrow view, zoomed in); higher values act like a wide-angle
lens (broader view, more perspective distortion).



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Near, <b>Far</b>, </td></tr>
<tr><td><strong>Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Predict position of the target to reduce lag caused by smoothing</td></tr>
<tr><td><strong>Lock On Target</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Automatically focus on target</td></tr>
<tr><td><strong>Camera Shake</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Lock Rotation</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Camera follows the rotation of the target</td></tr>
<tr><td><strong>Auto Zoom</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Automatically zoom in and out to maintain the target size in view</td></tr>
<tr><td><strong>Zoom Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Time it takes to zoom to target FOV</td></tr>
<tr><td><strong>FOV Height At Target</strong></td><td>Float</td><td>0.2 – 2</td><td>1</td><td></td><td>Vertical height for the target when using auto zoom</td></tr>
<tr><td><strong>Vertical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Offset vertically</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Size of the target actor in the camera view.</td></tr>
<tr><td><strong>Shift</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Shift the camera position up or down.</td></tr>
<tr><td><strong>Target Center</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Center position of the focal point on the target actor.</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Offset</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

