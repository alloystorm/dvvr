---
layout: release
title: Camera Settings
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


## Overview
Camera settings control the behavior and position of the camera rig, including height, field of view, and how motion data affects the camera.

## Settings

* **Height Offset** (-5 to 5): Adjusts the camera height relative to the motion's default position. Use this to raise or lower the camera independently of the motion data.
* **FOV Scale** (0.25–2.0): Scales the field of view of the camera. Values below 1 narrow the view (zoom in); values above 1 widen it (zoom out).
* **Portrait Zoom** (1–2): Additional zoom applied when the display is in portrait orientation.
* **Near Clip Plane** (0–0.5): Sets the near clipping plane distance. Lower values allow the camera to get closer to objects before they are clipped.
* **Reset When Motion Changes**: When enabled, the camera offset is reset to default whenever the motion changes.
* **Freeze in VR**: When enabled, camera movements are frozen while the UI is visible in VR mode, preventing unwanted camera drift during menu interaction.

## Rotation filter
Controls how much of the camera rotation from motion data is applied.

* **No Rotation**: Motion camera rotation is ignored; the camera remains stationary in rotation.
* **Direction Only**: Only the horizontal facing direction from the motion is applied.
* **Full Rotation**: The full rotation from the motion data is applied.

## Actions

* **Reset Offset**: Resets the camera height offset to its default value.
