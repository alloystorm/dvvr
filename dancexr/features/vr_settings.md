---
layout: release
title: VR Settings
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
VR settings contain VR-specific configuration for hand controllers, UI behavior, pointer calibration, and performance options. These settings are only relevant when running in VR mode.

## Hand
Settings for virtual hand rendering.

* **Enable**: Toggles the display of virtual hands in VR.
* **Cast Shadow**: Controls whether the virtual hands cast shadows in the scene.
* **Left Hand Pose**: Selects the default pose for the left hand controller.
* **Right Hand Pose**: Selects the default pose for the right hand controller.

## UI
Settings for how the UI panel behaves in VR.

* **Block Desktop Window**: Blocks the desktop mirror window while in VR mode, reducing GPU load by not rendering the screen output to the desktop.
* **UI Auto Return**: When enabled, the UI panel smoothly returns to the field of view when it drifts out of sight.
* **UI Distance** (0.5–5m): Controls how far the UI panel is positioned from the user.
* **Mouse Mode in VR**: Enables using the mouse as a pointer in VR without requiring hand controllers.
* **Mouse Sensitivity**: Adjusts pointer sensitivity when using mouse mode in VR.
* **Time and FPS**: Displays the current time and frame rate on the hand overlay.

## Pointer
Settings for calibrating the pointer ray used for VR interaction.

* **Direction**: Adjusts the direction angle of the pointer ray relative to the controller.
* **Orientation**: Adjusts the orientation offset of the pointer.
* **Offset**: Adjusts the positional offset of the pointer ray origin.
* **Update Pointer**: Applies the current pointer calibration settings.

## Foveated rendering
Foveated rendering reduces GPU load by rendering the peripheral areas of the view at lower resolution while keeping the center sharp. Only shown on supported hardware.

* **Enable**: Toggles foveated rendering on or off.
* **Level** (0–1): Controls how aggressively the edges of the view are rendered at lower resolution. Higher values increase performance at the cost of peripheral image quality.
