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


## Settings reference

<a id="settings-special-shader"></a>
## Special shader (Special Shader) {#special-shader}

Overrides the shader type for all materials on the actor.

**Mode** selects the shader: *Off* uses the default shader;
*Refraction Thick/Thin* simulates glass with refractive
transparency; *Outline* renders only the outline edges;
*Unlit* disables all lighting; *Experiment* is a
placeholder for custom shader effects.

**Refraction** controls the index of refraction for glass
modes — higher values bend light more.

**Thickness** adjusts the perceived depth of thin glass
refraction.

## Hexagon Map {#hexagon-map}

A procedural hexagonal (or circular) micro-pattern overlaid on
the surface for fishnet, sci-fi panel, or studded looks. Toggle
it off whenever you want a smooth fabric.


### Density & Shape

**Density** sets how many hexagons fit across the surface
(snapped to powers of two for clean tiling). **Size** scales
each hex within its cell — smaller values leave gaps between
hexes, larger values pack them tight. **Use Circle** swaps the
hex shape for circles, useful for polka-dot or rivet looks.
**Soft Edge** controls the falloff at each cell's border;
values near zero give a crisp boundary, larger values blur the
pattern into the surrounding surface.


### Bump & Noise

**Bump** raises or lowers each cell relative to the surface
(negative values stamp inwards). **Noise** randomises per-cell
height so the pattern doesn't read as a perfect grid.


### UV Projection

For outfits the cells can either follow the model's UV layout
or be projected from a virtual cylinder around the body.
**UV Projection** enables the cylindrical mode — turn it on
when stretched or distorted UVs ruin the pattern.
**Projection Radius** scales the cylinder, and **Rotation**
tilts it so the hex grid runs diagonally instead of straight.

<a id="settings-glow-color"></a>
## Color and glow (Color) {#color}

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

