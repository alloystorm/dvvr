---
layout: feature
title: "Ground"
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

