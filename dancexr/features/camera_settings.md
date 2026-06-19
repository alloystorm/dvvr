---
layout: feature
title: "Main Camera"
locale: en-US
---

# Main Camera

Camera settings control the behavior and position of the camera rig, including height, field of view, and how motion data affects the camera.


## Settings

**Height Offset** (-5.0 to 5.0) adjusts the camera height relative to the motion's default position. Use this to raise or lower the camera independently of the motion data.

**FOV Scale** (0.25 to 2.0) scales the field of view of the camera. Values below 1 narrow the view (zoom in); values above 1 widen it (zoom out).

**Portrait Mode Zoom** (1.0 to 2.0) sets additional zoom applied when the display is in portrait orientation.

**Near Clip** (0.0 to 0.5) sets the near clipping plane distance. Lower values allow the camera to get closer to objects before they are clipped.

**Reset When Motion Change** resets the camera offset to default whenever the motion changes.

**Freeze in VR** freezes camera movements while the UI is visible in VR mode, preventing unwanted camera drift during menu interaction.


## Rotation filter

Controls how much of the camera rotation from motion data is applied.

* **No Rotation**: Motion camera rotation is ignored; the camera remains stationary in rotation.
* **Direction Only**: Only the horizontal facing direction from the motion is applied.
* **Full Rotation**: The full rotation from the motion data is applied.


## Actions

* **Reset Offset** resets the camera height offset to its default value.

