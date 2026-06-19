---
layout: feature
title: "VR Settings"
locale: en-US
---

# VR Settings

VR settings contain VR-specific configuration for hand controllers, UI behavior, pointer calibration, and performance options. These settings are only relevant when running in VR mode.


## Hand

Settings for virtual hand rendering.

* **Enable** toggles the display of virtual hands in VR.
* **Cast Shadow** controls whether the virtual hands cast shadows in the scene.
* **Left Hand Pose** selects the default pose for the left hand controller.
* **Right Hand Pose** selects the default pose for the right hand controller.


## UI

Settings for how the UI panel behaves in VR.

* **Block Desktop Window** blocks the desktop mirror window while in VR mode, reducing GPU load by not rendering the screen output to the desktop.
* **UI Auto Return** causes the UI panel to smoothly return to the field of view when it drifts out of sight.
* **UI Distance** (0.5 to 5.0m) controls how far the UI panel is positioned from the user.
* **Mouse Mode in VR** enables using the mouse as a pointer in VR without requiring hand controllers.
* **Mouse Sensitivity** adjusts pointer sensitivity when using mouse mode in VR.
* **Time and FPS** displays the current time and frame rate on the hand overlay.


## Pointer

Settings for calibrating the pointer ray used for VR interaction.

* **Direction** adjusts the direction angle of the pointer ray relative to the controller.
* **Orientation** adjusts the orientation offset of the pointer.
* **Offset** adjusts the positional offset of the pointer ray origin.
* **Update Pointer** applies the current pointer calibration settings.


## Foveated rendering

Foveated rendering reduces GPU load by rendering the peripheral areas of the view at lower resolution while keeping the center sharp. Only shown on supported hardware.

* **Enable** toggles foveated rendering on or off.
* **Level** (0 to 1) controls how aggressively the edges of the view are rendered at lower resolution. Higher values increase performance at the cost of peripheral image quality.

