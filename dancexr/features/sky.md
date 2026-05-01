---
layout: release
title: "Sky"
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



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Skymap, Procedural, Indoor, <b>Thin Cloud</b>, Cloudy, </td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td>Selects the sky rendering mode: Color, Sky Map, or Procedural.</td></tr>
<tr><td><strong>Background</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Controls the brightness of the sky when it is rendered.</td></tr>
<tr><td><strong>Sky Ambient</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Controls how much the sky affects ambient lighting.</td></tr>
<tr><td><strong>Celestial</strong></td><td>Value</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>Sky Map</strong></td><td>Options</td><td>[Cloud], [Fantasy], [Day], [Studio]</td><td>[Fantasy]</td><td></td><td></td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td>Sets the rotation of the sky in degrees.</td></tr>
<tr><td><strong>Wind</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>Global wind speed affecting cloth simulation, particle dynamics, and clouds.</td></tr>
<tr><td><strong>Wind Direction</strong></td><td>Float</td><td>0 – 360</td><td>0</td><td></td><td>Sets the global wind direction in degrees.</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Wind Field</strong> — <em>Configures the wind field, including position, rotation, radius, and speed.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Position</strong> — <em>Sets the position of the wind field.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Rotation</strong> — <em>Sets the rotation of the wind field.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 10</td><td>5</td><td></td><td>Sets the distance of the wind field.</td></tr>
<tr><td><strong>Radius</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Sets the radius of the wind field.</td></tr>
<tr><td><strong>Speed</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>Sets the speed of the wind field.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><strong>Sky Ambient</strong></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Sky Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Sunset, Red, Yellow, Blue, Green, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Use Stage Color</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use the color from the stage ring</td></tr>
<tr><td><strong>Color Temp</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Middle Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Sunset, Red, Yellow, Blue, Green, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Use Stage Color</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use the color from the stage ring</td></tr>
<tr><td><strong>Color Temp</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ground Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>White</b>, Sunset, Red, Yellow, Blue, Green, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Use Stage Color</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use the color from the stage ring</td></tr>
<tr><td><strong>Color Temp</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Cloud</strong> — <em>Configures volumetric clouds, including shape, erosion, density, and wind effects.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enables or disables volumetric clouds.</td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Shape Scale</strong></td><td>Float</td><td>-1 – 2</td><td>1</td><td></td><td>Controls the scale of the cloud shapes.</td></tr>
<tr><td><strong>Shape Factor</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td>Adjusts the shape factor of the clouds.</td></tr>
<tr><td><strong>Erosion Scale</strong></td><td>Float</td><td>0 – 5</td><td>2</td><td></td><td>Controls the scale of cloud erosion.</td></tr>
<tr><td><strong>Erosion Factor</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td>Adjusts the erosion factor of the clouds.</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td>Sets the density multiplier for the clouds.</td></tr>
<tr><td><strong>Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enables or disables cloud shadows.</td></tr>
<tr><td><strong>Wind Multiplier</strong></td><td>Float</td><td>0 – 4</td><td>3</td><td></td><td>Sets the wind multiplier for cloud movement.</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

