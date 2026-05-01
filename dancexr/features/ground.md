---
layout: release
title: "Ground"
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

# Ground

Controls the floor and surrounding stage that the scene sits on —
ground surface, procedural stage and pool geometry, and (on HDRP)
the water system. A set of presets bundles these sub-features into
one-click looks like *Wood*, *Stage*, *Pool*, *Ocean* and
*Audio Visualizer*.


## Ground Height

Vertical offset for the stage center, in meters. Use this to
line the floor up with a tracked play area or a captured set so
actors do not sink into or float above the ground. Other anchors
(lights, cameras attached to the stage) follow this offset.


## Ground Settings

Sub-group that defines the floor disc itself — its surface
material, radius, and stage-aware visibility. See the
*Ground* group below for details.


## Stage Geometry

Procedural stage, runway, walls, and inner pool well that
surround the ground disc. See the *Stage / Pool* group
below for details. Stage geometry composes with the ground
disc — both can be visible at once.


## Water (HDRP)

HDRP-only water surface anchored to the stage center, used
by ocean and pool presets. See the *Water System* group
below for details. Re-applies whenever the stage geometry
changes so the water tracks the pool well. Not available
on URP — the water shader globals are cleared instead.


## Presets

The preset list combines the sub-features into named looks.
Picking a preset toggles the ground on or off, selects a floor
surface, and chooses a stage-geometry and water variant in one
step. Presets are the fastest way to switch between a plain
floor, a runway stage, a pool, an ocean, an audio visualizer
floor, a projector screen, or an LED box.

# Sub-Components

## Ground

The flat ground disc that the scene sits on. Toggling it off
hides the ground entirely (useful when a stage prop or AR
passthrough should take over). **Radius** sets the size of
the disc — large enough to fill the visible horizon for
outdoor looks, smaller for tighter indoor scenes. **Hide If
Stage Present** automatically suppresses the ground whenever
an actor with the *Stage* purpose is loaded, so a physical
stage model does not stack on top of the procedural disc.
The **Surface** sub-group picks the floor material —
textured tiles, sky-projected dome, or solid color — and
also shares its preset list with the parent's preset
bundles.

## Stage / Pool

Procedural stage built from a runway slab plus optional
outer walls, inner well, and back wall — used for runways,
pools, rooms, projector screens, and LED boxes. Built-in
presets cover the common shapes; the fields below let you
tune them.


### Position

**Lift** raises the stage above the ground or sinks it
below; a negative lift carves a hole through the ground
disc so the inner well can hold water. **Front / Back
Offset** shifts the whole stage forward or back along the
Z axis, useful for aligning with a tracked play area.


### Geometry

The **Geometry** sub-group sizes the slab. **Center Width**
/ **Center Depth** define the main rectangle; **Side /
Front / Back Extension** add runway sections beyond it.
**Wall Height** and **Wall Thickness** control the rim that
wraps around — set Wall Height to 0 for a flush platform.
**Back Height** raises a vertical board behind the stage,
used for backdrops and projector screens. **Floating**
detaches the slab from the ground geometry so it can sit on
water without z-fighting.


### Surfaces

Three independent floor surfaces — *Top*, *Sides*, and
*Background* — each with their own texture, tiling, and
color. This lets the stage top, the wrap-around rim, and
the back board read as different materials (e.g. wood top
with metal sides).


### Custom Hole

By default the carved hole follows the stage outline. Toggle
**Custom Hole** to override the bounds explicitly with the
**Left** / **Right** / **Front** / **Back** / **Top** /
**Bottom** values — handy for non-rectangular cutouts or
aligning the hole with an imported set.

## Water System

HDRP water surface anchored to the stage center. Pro-only.
Used for pools sitting in the stage's inner well, still
lakes, and infinite oceans. Presets bundle the common looks.


### Type and Height

**Type** picks the water geometry. *Pool* sizes the surface
to the stage's runway dimensions and is the right choice
when the stage has a carved well. *River* is a finite quad
covering the ground disc. *Ocean* is infinite — use it for
horizon-filling water unbounded by the stage.

**Height** is the water level relative to the stage center.
Negative values sit the water below the floor (matching a
pool well dug by a negative stage *Lift*).


### Waves

**Ripples** drives the small wind-chop wavelets — keep
this low for still water. **Large Wave** drives the broad
swell that defines the look of an ocean; set it to 0 for
glass-still surfaces. **Wave Range** controls how high
the wet effect reaches up onto materials touching the
water.


### Optical Properties

**Absorption Distance** is how far you can see through the
water from above; lower it for murky water, raise it for
clear. **Absorption Multiplier** scales that distance when
viewing from below the surface. **Refraction Max Distance**
clamps under-water refraction depth — higher values
exaggerate distortion. **Caustics** sets the brightness of
the projected caustic patterns on submerged geometry.



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Sky Map, <b>Wood</b>, Stage, Pool, Ocean, Audio Visualizer, Projector Screen, LED Box, </td></tr>
<tr><td><strong>Ground Height</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ground</strong> — <em>Ground Settings.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>2 – 100</td><td>200</td><td></td><td>Size of the ground mesh.</td></tr>
<tr><td><strong>Hide If Stage Present</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Hide ground when there are stage models.</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Surface</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Sky Map, <b>Wood</b>, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glow White, </td></tr>
<tr><td><strong>Texture</strong></td><td>Options</td><td>[Sky Map], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[Wood1]</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Tiling</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Tiling X</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Tiling Y</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Wrap Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset X</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset Y</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Rotation</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Fit Texture</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.95</td><td></td><td></td></tr>
<tr><td><strong>Metallic</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Reduction</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Curve</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Clip</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Original, <b>White</b>, Black, Red, Yellow, Dark Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Multiply</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Toon Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Sharp</b>, Soft, Bright, Flat + Specular, Flat, </td></tr>
<tr><td><strong>Shading</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Outline</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Highlight Area</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Highlight</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Shadow Area</strong></td><td>Float</td><td>0 – 1</td><td>0.65</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Soft Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Special Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment</td><td>Off</td><td></td><td></td></tr>
<tr><td><strong>Refraction</strong></td><td>Float</td><td>1 – 3</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Thickness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Viewer Height</strong></td><td>Float</td><td>0.5 – 3</td><td>1.5</td><td></td><td>Viewer height used when projecting the the texture on to the ground</td></tr>
<tr><td colspan="6"><details>
<summary><strong>LED Mode</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>4 – 10</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Soft Edge</strong></td><td>Float</td><td>0 – 1</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong>Viewing Angle</strong></td><td>Float</td><td>0 – 8</td><td>1</td><td></td><td>Reduce brightness when viewed from an angle. 0 = perfect</td></tr>
<tr><td><strong>Edge</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Reduce Moire</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Audio Visualizer</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Layout</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Transparent</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Ring Size</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Data Scale</strong></td><td>Float</td><td>-2 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Color Transition</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Align</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Gap</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Shape Shift</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Beat Clock</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ring Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>20</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Background Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Background Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Background Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Foreground Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Foreground Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[DanceXR]</td><td></td><td></td></tr>
<tr><td><strong>Foreground Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Foreground Scale</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Auto BPM</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use real-time automatically detected BPM instead of the set BPM.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shadow Only</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Shadow Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
White, Black, Red, <b>Yellow</b>, Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Transparency</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Stage Geometry</strong> — <em>Procedural stage &amp; pool geometry.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>None</b>, Runway, Pool, Room, Background Board, Projector Screen, LED Box, </td></tr>
<tr><td><strong>Lift</strong></td><td>Float</td><td>-5 – 5</td><td>0.5</td><td></td><td>Lift the stage up / down.</td></tr>
<tr><td><strong>Front / Back Offset</strong></td><td>Float</td><td>-10 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Geometry</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Center Width</strong></td><td>Float</td><td>0 – 10</td><td>8</td><td></td><td>Width of the center area.</td></tr>
<tr><td><strong>Center Depth</strong></td><td>Float</td><td>0 – 9</td><td>5</td><td></td><td>Depth of the center area.</td></tr>
<tr><td><strong>Back Height</strong></td><td>Float</td><td>0 – 9</td><td>0</td><td></td><td>Height of the background board.</td></tr>
<tr><td><strong>Side Extension</strong></td><td>Float</td><td>0 – 5</td><td>0</td><td></td><td>Extension at left and right.</td></tr>
<tr><td><strong>Front Extension</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td>Extension at front.</td></tr>
<tr><td><strong>Back Extension</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td>Extension at back.</td></tr>
<tr><td><strong>Wall Height</strong></td><td>Float</td><td>0 – 5</td><td>0.05</td><td></td><td>Height of the edge above ground.</td></tr>
<tr><td><strong>Wall Thickness</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>Size of the edge.</td></tr>
<tr><td><strong>Window</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Floating</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Top Surface</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Blank</b>, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glow White, </td></tr>
<tr><td><strong>Texture</strong></td><td>Options</td><td>[Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[Blank]</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Tiling</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Tiling X</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Tiling Y</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Wrap Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset X</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset Y</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Rotation</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Fit Texture</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.95</td><td></td><td></td></tr>
<tr><td><strong>Metallic</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Reduction</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Curve</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Clip</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Original, <b>White</b>, Black, Red, Yellow, Dark Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Multiply</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Toon Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Sharp</b>, Soft, Bright, Flat + Specular, Flat, </td></tr>
<tr><td><strong>Shading</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Outline</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Highlight Area</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Highlight</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Shadow Area</strong></td><td>Float</td><td>0 – 1</td><td>0.65</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Soft Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Special Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment</td><td>Off</td><td></td><td></td></tr>
<tr><td><strong>Refraction</strong></td><td>Float</td><td>1 – 3</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Thickness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>LED Mode</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>4 – 10</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Soft Edge</strong></td><td>Float</td><td>0 – 1</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong>Viewing Angle</strong></td><td>Float</td><td>0 – 8</td><td>1</td><td></td><td>Reduce brightness when viewed from an angle. 0 = perfect</td></tr>
<tr><td><strong>Edge</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Reduce Moire</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Audio Visualizer</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Layout</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Transparent</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Ring Size</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Data Scale</strong></td><td>Float</td><td>-2 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Color Transition</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Align</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Gap</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Shape Shift</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Beat Clock</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ring Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>20</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Background Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Background Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Background Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Foreground Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Foreground Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[DanceXR]</td><td></td><td></td></tr>
<tr><td><strong>Foreground Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Foreground Scale</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Auto BPM</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use real-time automatically detected BPM instead of the set BPM.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Side Surface</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Blank</b>, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glow White, </td></tr>
<tr><td><strong>Texture</strong></td><td>Options</td><td>[Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[Blank]</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Tiling</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Tiling X</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Tiling Y</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Wrap Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset X</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset Y</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Rotation</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Fit Texture</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.95</td><td></td><td></td></tr>
<tr><td><strong>Metallic</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Reduction</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Curve</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Clip</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Original, <b>White</b>, Black, Red, Yellow, Dark Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Multiply</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Toon Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Sharp</b>, Soft, Bright, Flat + Specular, Flat, </td></tr>
<tr><td><strong>Shading</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Outline</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Highlight Area</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Highlight</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Shadow Area</strong></td><td>Float</td><td>0 – 1</td><td>0.65</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Soft Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Special Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment</td><td>Off</td><td></td><td></td></tr>
<tr><td><strong>Refraction</strong></td><td>Float</td><td>1 – 3</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Thickness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>LED Mode</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>4 – 10</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Soft Edge</strong></td><td>Float</td><td>0 – 1</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong>Viewing Angle</strong></td><td>Float</td><td>0 – 8</td><td>1</td><td></td><td>Reduce brightness when viewed from an angle. 0 = perfect</td></tr>
<tr><td><strong>Edge</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Reduce Moire</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Audio Visualizer</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Layout</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Transparent</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Ring Size</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Data Scale</strong></td><td>Float</td><td>-2 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Color Transition</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Align</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Gap</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Shape Shift</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Beat Clock</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ring Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>20</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Background Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Background Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Background Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Foreground Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Foreground Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[DanceXR]</td><td></td><td></td></tr>
<tr><td><strong>Foreground Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Foreground Scale</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Auto BPM</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use real-time automatically detected BPM instead of the set BPM.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Back Surface</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Blank</b>, Wood, Concrete, Blue Tiles, Projector Screen, Emissive Screen, LED Screen, Black Gloss, Audio Visualizer, Glow White, </td></tr>
<tr><td><strong>Texture</strong></td><td>Options</td><td>[Blank], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[Blank]</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Tiling</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Tiling X</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Tiling Y</strong></td><td>Float</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Wrap Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset X</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Offset Y</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Rotation</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Fit Texture</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.95</td><td></td><td></td></tr>
<tr><td><strong>Metallic</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Reduction</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha Curve</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Clip</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Original, <b>White</b>, Black, Red, Yellow, Dark Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Multiply</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Toon Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Sharp</b>, Soft, Bright, Flat + Specular, Flat, </td></tr>
<tr><td><strong>Shading</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Outline</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Specular</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Highlight Area</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Soft Highlight</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Ambient</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Shadow Area</strong></td><td>Float</td><td>0 – 1</td><td>0.65</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Soft Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Special Shader</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Off, Refraction Thick, Refraction Thin, Outline, Unlit, Experiment</td><td>Off</td><td></td><td></td></tr>
<tr><td><strong>Refraction</strong></td><td>Float</td><td>1 – 3</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Thickness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>LED Mode</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>4 – 10</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Soft Edge</strong></td><td>Float</td><td>0 – 1</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong>Viewing Angle</strong></td><td>Float</td><td>0 – 8</td><td>1</td><td></td><td>Reduce brightness when viewed from an angle. 0 = perfect</td></tr>
<tr><td><strong>Edge</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Reduce Moire</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Audio Visualizer</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Layout</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Transparent</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Ring Size</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Data Scale</strong></td><td>Float</td><td>-2 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Color Transition</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Align</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Gap</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Shape Shift</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Beat Clock</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ring Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>20</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Background Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Background Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Background Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Foreground Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Black, Yellow, Blue, Animated Hue, Glow w/ Music, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Foreground Image</strong></td><td>Options</td><td>[None], [Wood1], [DanceXR], [Tiles], [Concrete], [Video]</td><td>[DanceXR]</td><td></td><td></td></tr>
<tr><td><strong>Foreground Vibration</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Foreground Scale</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Auto BPM</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use real-time automatically detected BPM instead of the set BPM.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Custom Hole</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use custom hole.</td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Left</strong></td><td>Float</td><td></td><td>-1</td><td></td><td></td></tr>
<tr><td><strong>Right</strong></td><td>Float</td><td></td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Front</strong></td><td>Float</td><td></td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Back</strong></td><td>Float</td><td></td><td>-1</td><td></td><td></td></tr>
<tr><td><strong>Top</strong></td><td>Float</td><td></td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Bottom</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Water System</strong> — <em>Water System</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Off</b>, Pool, Still Water, Ocean, </td></tr>
<tr><td><strong>Type</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Height</strong></td><td>Float</td><td>-2 – 2</td><td>-0.1</td><td></td><td>Height of water level.</td></tr>
<tr><td><strong>Ripples</strong></td><td>Float</td><td>0 – 10</td><td>3</td><td></td><td>Intensity of small wave</td></tr>
<tr><td><strong>Large Wave</strong></td><td>Float</td><td>0 – 100</td><td>30</td><td></td><td>Intensity of large wave</td></tr>
<tr><td><strong>Refraction Max Distance</strong></td><td>Float</td><td>0 – 3.5</td><td>0.35</td><td></td><td>Controls the maximum distance in meters used to clamp the under water refraction depth. Higher value increases the distortion amount.</td></tr>
<tr><td><strong>Absorption Distance</strong></td><td>Float</td><td>1 – 10</td><td>5</td><td></td><td>Max distance you can see in the water from above.</td></tr>
<tr><td><strong>Caustics</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Caustics effect</td></tr>
<tr><td><strong>Absorption Multiplier</strong></td><td>Float</td><td>0 – 5</td><td>2</td><td></td><td>Multiplication applied to the Absorption Distance when viewing from below.</td></tr>
<tr><td><strong>Wave Range</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>Height of wet effect on materials.</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

