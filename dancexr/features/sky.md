---
layout: release
title: "Sky"
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

# Sky

Controls everything overhead — the sky background that fills the
horizon, the ambient light it casts on the scene, and the global
wind that drives clouds, cloth, and particle systems. Presets
bundle these into named looks like *Skymap*, *Procedural*,
*Indoor*, *Thin Cloud*, and *Cloudy*.


## Mode

**Mode** picks one of three sky renderers and the rest of the
panel reshapes to match. *Color* paints a flat gradient sky
from the **Sky Color** / **Middle Color** / **Ground Color**
values and is the cheapest option. *Sky Map* wraps a 360°
panorama (built-in or imported) around the scene — use this
for outdoor or stylized backgrounds. *Procedural* renders a
physically-based sky and (on HDRP) is the only mode that
supports volumetric clouds.


## Sky Map and Orientation

When mode is *Sky Map*, **Sky Map** chooses the panorama from
the built-in set plus anything imported into the content
library. Loading large skymaps is asynchronous so the UI stays
responsive. **Orientation** rotates the sky in degrees around
the vertical axis — this also rotates the projection used for
the ground sky-dome material, so adjusting it shifts ground
reflections too.


## Background and Ambient

**Background** (HDRP) scales how bright the sky looks on
screen. **Sky Ambient** controls how much that sky bleeds
into the rest of the scene as ambient lighting — lower it
if a bright skymap is washing out actor shading. On URP the
same role is played by **Sky Exposure** and **Intensity**,
where Sky Exposure also feeds reflection probe brightness.


## Sky Colors

In *Color* mode, **Sky Color**, **Middle Color**, and
**Ground Color** define the top, horizon, and bottom of a
three-band gradient. They also drive trilight ambient
lighting (and on HDRP, the fog albedo), so changing them
tints what the scene picks up from the sky in addition to
the visible background.


## Wind

**Wind** sets a global wind speed that drives cloth
simulation, particle dynamics, and (on HDRP) volumetric
cloud movement. **Wind Direction** sets its compass heading.
Keep this modest — high wind speeds make hair and skirts
visibly thrash.


## Wind Field

A localized wind volume on top of the global wind, useful
for staged effects like a fan blowing on one actor. Toggle
it on, then position and orient the cylindrical field with
**Position** / **Rotation** (an interactive gizmo appears
while the menu is open). **Distance** is the cylinder's
length, **Radius** its width, and **Speed** its strength.
Affects cloth and particles inside the volume only.


## Clouds (HDRP)

Volumetric clouds, available only in *Procedural* mode. The
**Toggle** turns them on. **Shape Scale** and **Shape
Factor** control the large-scale silhouette; **Erosion
Scale** and **Erosion Factor** add the wispy edge detail;
**Density** controls overall coverage. **Shadow** projects
cloud shadows onto the scene — costly but adds a lot of
realism on outdoor stages. **Wind Multiplier** scales the
global wind for clouds only, so they can drift faster or
slower than the rest of the scene.

