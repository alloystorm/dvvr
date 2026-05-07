---
layout: release
title: Display Settings
locale: en-US
---



## Overview
Display settings allows you to change configurations regarding UI, screen resolution, and framerate.

## UI Settings
* **UI Scale**: Changes the size of the UI. Useful when using a high-resolution screen where the UI appears too small.
* **UI Width**: Controls the width of the menu UI.
* **Max UI Height**: Controls the maximum height of menu panels.
* **Max Menu Levels**: Sets the maximum number of nested menu levels shown simultaneously.
* **Indentation**: Controls the size of indentation within menus.
* **Use Menu Pinning**: Allows parent menus to move out of view to make room for content behind the menu.
* **Hide UI When Sliding**: Hides the rest of the UI while a slider is being adjusted.
* **UI Uses Directional Input**: Enables d-pad or directional input for menu navigation, useful with gamepads.
* **Resume Menu After Loading**: Restores the last open menu after a scene finishes loading.
* **Toggle Root Menu**: Root menu buttons toggle the menu off when the menu is already visible.

## Screen Resolution
Controls the screen resolution and window mode. Switching between fullscreen and windowed mode is available here.

These settings are not applied automatically. Click the **Apply** button to apply changes.

## Framerate
Controls the target framerate and where the FPS counter is displayed.

The first two framerate options are special:
* **VSync**: Targets the monitor's refresh rate.
* **Max**: Renders as fast as possible without a cap.

## VR Specific Settings
These settings are only available in VR mode.
* **UI Always On Top**: Ensures the UI is always rendered on top even when obscured by other objects. On by default.
* **UI Auto Return**: When enabled, the UI gradually moves back into the field of view when it drifts out of sight.
* **UI Distance**: Controls how far the UI panel is from the viewer's head.
* **Mouse Mode in VR**: Use the mouse as a pointer in VR without requiring hand controllers.
* **Mouse Sensitivity**: Adjusts pointer sensitivity when using mouse mode in VR.

### Pointer
Calibrates the pointer ray used for VR interaction.
* **Direction**: Adjusts the direction angle of the pointer ray.
* **Orientation**: Adjusts the orientation offset of the pointer.
* **Offset**: Adjusts the positional offset of the pointer origin.
* **Update Pointer**: Applies the current pointer calibration settings.

## Foveated Rendering (v2025.12)
Foveated rendering reduces GPU load by rendering peripheral areas at lower resolution while keeping the center sharp.
* Supported on OpenXR-compatible PC VR headsets.
* Works on Quest Standalone in both AR and VR modes.
* **Level**: Controls how aggressively the edges of the view are rendered at lower resolution (0–1).