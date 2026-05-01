---
layout: release
title: "Lighting"
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

# Lighting

Controls all scene lighting — a directional sun, up to three
independent light groups, and global brightness controls.
Built-in presets give a complete working look in one tap;
every parameter is then freely adjustable.


## Presets

The built-in presets — *Sunset*, *Daylight*, *Window*, *Stage*,
*Projector*, and others — establish a complete lighting setup in
one tap. Apply the closest preset and tune individual groups
from there.


## Overall Intensity & Sky Ambient

**Overall Intensity** scales every light group and the sun
together, letting you push or pull the whole scene brightness
with one slider. **Sky Ambient** controls indirect skylight;
raising it brightens shadowed areas and reduces harsh contrast,
especially in outdoor scenes.


## Sunlight

The **Celestial** sub-section controls the directional sun (and
moon on HDRP). Time of day, orientation, and ecliptic angle
determine where the sun sits in the sky and the resulting shadow
direction.


## Additional Light Groups

**Additional 1**, **2**, and **3** are independent, fully
configurable light groups — typically key, fill, and rim. Each
can be a spotlight, point light, area light, or projector, and
can track actors dynamically.


## Fog

Adds depth haze between the camera and the scene. Low values
give a subtle atmospheric cue; higher values can dramatically
shift the mood. Fog interacts with volumetric light cones for
dramatic beam effects.


## Light & Shadow Limits

**Light Limit** caps how many active lights are rendered
simultaneously. **Shadow Limit** caps the subset that cast
shadows — shadows are expensive, so keep this low (1–4)
unless performance allows more.


## Allocation

When light groups use *Follow Actor* or *Maintain Distance*
dynamics, **Allocation** controls how lights are spread across
multiple dancers. *By Distance* minimises total travel for a
natural look; *By Index (Fixed)* pins lights to specific actor
slots. **Refresh Interval** sets how many beats pass between
reallocations.

# Sub-Components

## Sunlight

Controls the directional sun (and, on HDRP, the moon and night
sky). The sun position is defined by Time of Day, Orientation,
and Ecliptic Angle, giving full creative control over shadow
direction and sky colour.


### Sun Position

**Time Of Day** moves the sun along its arc in hours (0–24).
**Orientation** sets the compass direction the sun rises toward.
**Ecliptic Angle** tilts the orbital plane — useful for matching
a specific location or season without precise sun tracking.


### Intensity & Color

**Sunlight Intensity** and **Color Temperature** control the raw
brightness and warmth of the directional light. Because sunlight
is very powerful, scenes with it enabled typically need a higher
exposure or lower Overall Intensity to avoid blow-out.


### Moon & Night Sky (HDRP)

On HDRP the same sub-section controls moon position, phase, and
earthshine, plus the brightness of stars and aurora. Disable the
sun and raise moonlight intensity for night scenes.


### Window Effect

The **Window** sub-section casts a grid of rectangular shadows
that simulate light streaming through window panes. Adjust
width, height, rows, and columns to fit an imagined room
interior. The *Sky Light* option adds a soft fill from the same
direction to complement the shadow.

## Additional 1

A configurable group of one or more lights, positioned relative
to the scene or an actor. Three groups are available in the
Lighting settings, typically used as key, fill, and rim lights,
but each is configured identically through this sub-section.


### Type & Cookie

**Type** selects the light shape: Spotlight, Point, Area,
Pyramid, or Box projector. **Cookie** maps project a pattern
through the beam (Window, Blinds, Spot, Tube, Video). Set
**Emitter Radius** to soften the cone or cookie edges, and
**Visible** to control how bright the light source itself
appears in the render.


### Position & Orientation

**Distance** and **Height** place the light relative to its
target, **Angle** tilts it downward, and **Orientation** rotates
it around the vertical axis. On spotlight types, **Size X / Y**
widens the beam cross-section; **Cone Length** controls the
volumetric scatter depth.


### Dynamics

**Dynamics** determines whether the light stays fixed
(*Stationary*), orbits the assigned actor (*Follow Actor* /
*Behind Actor*), or trails at a set radius (*Maintain Distance*).
Enable **Use Actor Position** to orient the light relative to
where the actor is facing. Actor assignment is handled by the
Allocation settings in the parent Lighting panel.


### Repeat (Array)

The **Repeat** sub-section multiplies the light into an array.
Choose *Circle* formation for a ring of stage beams or *Grid*
for a ceiling rig. Presets such as *4x Fan* or *8x Circle* set
the array up in one step.


### Suspension

Enable **Suspension** to hang the light from a virtual rigging
point, giving it a slow pendulum swing. **Segments** sets the
number of cable joints, **Suspension Distance** the drop length,
and **Swing Speed** how actively it maintains its swinging arc.


### Shadow

Each group has independent shadow controls. Leave mode at the
default to inherit the global scene quality, or override it to
force raytraced or screen-space shadows on this group.
**Shadow Dimmer** softens the shadow without fully disabling it.

## Additional 2

A configurable group of one or more lights, positioned relative
to the scene or an actor. Three groups are available in the
Lighting settings, typically used as key, fill, and rim lights,
but each is configured identically through this sub-section.


### Type & Cookie

**Type** selects the light shape: Spotlight, Point, Area,
Pyramid, or Box projector. **Cookie** maps project a pattern
through the beam (Window, Blinds, Spot, Tube, Video). Set
**Emitter Radius** to soften the cone or cookie edges, and
**Visible** to control how bright the light source itself
appears in the render.


### Position & Orientation

**Distance** and **Height** place the light relative to its
target, **Angle** tilts it downward, and **Orientation** rotates
it around the vertical axis. On spotlight types, **Size X / Y**
widens the beam cross-section; **Cone Length** controls the
volumetric scatter depth.


### Dynamics

**Dynamics** determines whether the light stays fixed
(*Stationary*), orbits the assigned actor (*Follow Actor* /
*Behind Actor*), or trails at a set radius (*Maintain Distance*).
Enable **Use Actor Position** to orient the light relative to
where the actor is facing. Actor assignment is handled by the
Allocation settings in the parent Lighting panel.


### Repeat (Array)

The **Repeat** sub-section multiplies the light into an array.
Choose *Circle* formation for a ring of stage beams or *Grid*
for a ceiling rig. Presets such as *4x Fan* or *8x Circle* set
the array up in one step.


### Suspension

Enable **Suspension** to hang the light from a virtual rigging
point, giving it a slow pendulum swing. **Segments** sets the
number of cable joints, **Suspension Distance** the drop length,
and **Swing Speed** how actively it maintains its swinging arc.


### Shadow

Each group has independent shadow controls. Leave mode at the
default to inherit the global scene quality, or override it to
force raytraced or screen-space shadows on this group.
**Shadow Dimmer** softens the shadow without fully disabling it.

## Additional 3

A configurable group of one or more lights, positioned relative
to the scene or an actor. Three groups are available in the
Lighting settings, typically used as key, fill, and rim lights,
but each is configured identically through this sub-section.


### Type & Cookie

**Type** selects the light shape: Spotlight, Point, Area,
Pyramid, or Box projector. **Cookie** maps project a pattern
through the beam (Window, Blinds, Spot, Tube, Video). Set
**Emitter Radius** to soften the cone or cookie edges, and
**Visible** to control how bright the light source itself
appears in the render.


### Position & Orientation

**Distance** and **Height** place the light relative to its
target, **Angle** tilts it downward, and **Orientation** rotates
it around the vertical axis. On spotlight types, **Size X / Y**
widens the beam cross-section; **Cone Length** controls the
volumetric scatter depth.


### Dynamics

**Dynamics** determines whether the light stays fixed
(*Stationary*), orbits the assigned actor (*Follow Actor* /
*Behind Actor*), or trails at a set radius (*Maintain Distance*).
Enable **Use Actor Position** to orient the light relative to
where the actor is facing. Actor assignment is handled by the
Allocation settings in the parent Lighting panel.


### Repeat (Array)

The **Repeat** sub-section multiplies the light into an array.
Choose *Circle* formation for a ring of stage beams or *Grid*
for a ceiling rig. Presets such as *4x Fan* or *8x Circle* set
the array up in one step.


### Suspension

Enable **Suspension** to hang the light from a virtual rigging
point, giving it a slow pendulum swing. **Segments** sets the
number of cable joints, **Suspension Distance** the drop length,
and **Swing Speed** how actively it maintains its swinging arc.


### Shadow

Each group has independent shadow controls. Leave mode at the
default to inherit the global scene quality, or override it to
force raytraced or screen-space shadows on this group.
**Shadow Dimmer** softens the shadow without fully disabling it.

## Auto Exposure

HDRP auto-exposure settings that control how the camera adapts
to changes in scene brightness. When disabled, the camera uses a
fixed exposure driven by the global dim slider; when enabled, it
adjusts continuously based on scene luminance.


### Metering Mode

Determines which part of the frame is sampled to measure
brightness. *Average* reads the whole frame uniformly; *Spot*
reads only the centre; *Center Weighted* emphasises the centre
while including the periphery. Use *Spot* or *Center Weighted*
when a bright background would otherwise cause the subject to
appear too dark.


### Compensation & Range

**Compensation** shifts the target exposure up or down in EV
steps. **Range** clamps the minimum and maximum allowed exposure
values, preventing the camera from going too dark in black scenes
or too bright in blown-out environments.


### Adaptation

Controls how quickly exposure changes when lighting conditions
shift. *Normal* gives a gradual, cinematic response; *Fast*
reacts quickly to sudden changes; *Instant* snaps to the new
exposure with no delay.



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Sunset, <b>Daylight</b>, Window, Stage, Silhouette, Projector, Area light, Point Light Array, </td></tr>
<tr><td colspan="6"><details>
<summary><strong>Sun / Moon / Time</strong> — <em>Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Ecliptic Angle</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td>The angle between the horizon and the plane the sun moves within.</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Time Of Day</strong></td><td>Float</td><td>0 – 24</td><td>9</td><td></td><td>Set sun angle at a certain time, in hours.</td></tr>
<tr><td><strong>Sun</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable or disable the sun.</td></tr>
<tr><td><strong>Sunlight Intensity</strong></td><td>Float</td><td>0 – 200</td><td>100</td><td></td><td>Brightness of the sun.</td></tr>
<tr><td><strong>Color Temperature</strong></td><td>Float</td><td>1000 – 20000</td><td>6500</td><td></td><td>Color temporature of the sunlight.</td></tr>
<tr><td><strong>Spot Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>This affects the size of the sun disc in procedural sky and the softness of the shadow.</td></tr>
<tr><td><strong>Volumetric Multiplier</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Moon</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable or disable the moon.</td></tr>
<tr><td><strong>Moonlight Intensity</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>The brightness of the moon.</td></tr>
<tr><td><strong>Moon Position</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>The position of the moon in the sky.</td></tr>
<tr><td><strong>Moon Phase</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>The phase of the moon, where 0 is new moon and 1 is full moon.</td></tr>
<tr><td><strong>Earthshine</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>The brightness of the earthshine on the moon.</td></tr>
<tr><td><strong>Phase Rotation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>The rotation of the moon phase.</td></tr>
<tr><td><strong>Stars</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>The brightness of the stars.</td></tr>
<tr><td><strong>Aurora</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>The brightness of the aurora.</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Window</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Width</strong></td><td>Float</td><td>0 – 16</td><td>8</td><td></td><td>The width of the window when cookie map is enabled.</td></tr>
<tr><td><strong>Height</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>The height of the window when cookie map is enabled.</td></tr>
<tr><td><strong>Bottom</strong></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>-2</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Rows</strong></td><td>Integer</td><td>0 – 8</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Columns</strong></td><td>Integer</td><td>0 – 8</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Space X</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>Space Y</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>Visible</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Show window in the scene.</td></tr>
<tr><td><strong>Origin</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Sky Light</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td>The brightness of the sky light.</td></tr>
<tr><td><strong>Sky Light Angle</strong></td><td>Float</td><td>0 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Sky Light Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable shadow for the sky light.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shadow</strong> — <em>Shadow settings.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Contact Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable shadows for small details.</td></tr>
<tr><td><strong>Sample Count</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>Sample count when using raytracing shadows. Higher = better result but worse performance.</td></tr>
<tr><td><strong>Denoise</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable denoising when using raytracing shadows.</td></tr>
<tr><td><strong>Denoise Radius</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Shadow Dimmer</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Reduce intensity of the shadow.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Lens Flare</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable lens flare</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Additional 1</strong> — <em>Configure light group 1</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Spotlight</b>, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, </td></tr>
<tr><td><strong>Volumetric Multiplier</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Type</strong></td><td>Options</td><td>Spotlight, Point light, Area light, Pyramid, Box</td><td>Spotlight</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
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
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Cookie</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Emitter Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>Size of the light source.</td></tr>
<tr><td><strong>Size X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Size Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Visible</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>Controls how bright the light source is when being renderred. Set to 0 to make it invisible.</td></tr>
<tr><td><strong>Cone Length</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>Length of the volumatric light cone.</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-90 – 180</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>Height</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>Height of light position.</td></tr>
<tr><td><strong>Dynamics</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>Max Follow Distance</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Suspension</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Suspension Segments</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>Enable suspension effect.</td></tr>
<tr><td><strong>Suspension Distance</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Swing Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Control speed to maintain swing motion</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Use Actor Position</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use actor's position and orientation when positioning the lights.</td></tr>
<tr><td><strong>Target Height</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Lens Flare</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Repeat</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Off</b>, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle, </td></tr>
<tr><td><strong>Number</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>How many lights in the array.</td></tr>
<tr><td><strong>Formation</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>Use grid or circle formation.</td></tr>
<tr><td><strong>Dist / Radius</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>Distance between the lights in grid mode.</td></tr>
<tr><td><strong>Range</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>The angle of the lights in circle mode.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shadow</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Contact Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable shadows for small details.</td></tr>
<tr><td><strong>Sample Count</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>Sample count when using raytracing shadows. Higher = better result but worse performance.</td></tr>
<tr><td><strong>Denoise</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable denoising when using raytracing shadows.</td></tr>
<tr><td><strong>Denoise Radius</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Shadow Dimmer</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Reduce intensity of the shadow.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Additional 2</strong> — <em>Configure light group 2</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Spotlight</b>, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, </td></tr>
<tr><td><strong>Volumetric Multiplier</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Type</strong></td><td>Options</td><td>Spotlight, Point light, Area light, Pyramid, Box</td><td>Spotlight</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
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
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Cookie</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Emitter Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>Size of the light source.</td></tr>
<tr><td><strong>Size X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Size Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Visible</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>Controls how bright the light source is when being renderred. Set to 0 to make it invisible.</td></tr>
<tr><td><strong>Cone Length</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>Length of the volumatric light cone.</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>Height</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>Height of light position.</td></tr>
<tr><td><strong>Dynamics</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>Max Follow Distance</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Suspension</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Suspension Segments</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>Enable suspension effect.</td></tr>
<tr><td><strong>Suspension Distance</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Swing Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Control speed to maintain swing motion</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Use Actor Position</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use actor's position and orientation when positioning the lights.</td></tr>
<tr><td><strong>Target Height</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Lens Flare</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Repeat</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Off</b>, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle, </td></tr>
<tr><td><strong>Number</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>How many lights in the array.</td></tr>
<tr><td><strong>Formation</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>Use grid or circle formation.</td></tr>
<tr><td><strong>Dist / Radius</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>Distance between the lights in grid mode.</td></tr>
<tr><td><strong>Range</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>The angle of the lights in circle mode.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shadow</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Contact Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable shadows for small details.</td></tr>
<tr><td><strong>Sample Count</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>Sample count when using raytracing shadows. Higher = better result but worse performance.</td></tr>
<tr><td><strong>Denoise</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable denoising when using raytracing shadows.</td></tr>
<tr><td><strong>Denoise Radius</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Shadow Dimmer</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Reduce intensity of the shadow.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Additional 3</strong> — <em>Configure light group 3</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Spotlight</b>, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, </td></tr>
<tr><td><strong>Volumetric Multiplier</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Type</strong></td><td>Options</td><td>Spotlight, Point light, Area light, Pyramid, Box</td><td>Spotlight</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
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
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Cookie</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Emitter Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>Size of the light source.</td></tr>
<tr><td><strong>Size X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Size Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>Visible</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>Controls how bright the light source is when being renderred. Set to 0 to make it invisible.</td></tr>
<tr><td><strong>Cone Length</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>Length of the volumatric light cone.</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>Height</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>Height of light position.</td></tr>
<tr><td><strong>Dynamics</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>Max Follow Distance</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Suspension</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Suspension Segments</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>Enable suspension effect.</td></tr>
<tr><td><strong>Suspension Distance</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Swing Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Control speed to maintain swing motion</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Use Actor Position</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use actor's position and orientation when positioning the lights.</td></tr>
<tr><td><strong>Target Height</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Lens Flare</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Repeat</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Off</b>, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle, </td></tr>
<tr><td><strong>Number</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>How many lights in the array.</td></tr>
<tr><td><strong>Formation</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>Use grid or circle formation.</td></tr>
<tr><td><strong>Dist / Radius</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>Distance between the lights in grid mode.</td></tr>
<tr><td><strong>Range</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>The angle of the lights in circle mode.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shadow</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Contact Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable shadows for small details.</td></tr>
<tr><td><strong>Sample Count</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>Sample count when using raytracing shadows. Higher = better result but worse performance.</td></tr>
<tr><td><strong>Denoise</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable denoising when using raytracing shadows.</td></tr>
<tr><td><strong>Denoise Radius</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Shadow Dimmer</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Reduce intensity of the shadow.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Overall Intensity</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Overall intensity of all the lights.</td></tr>
<tr><td><strong>Sky Ambient</strong></td><td>Float</td><td>0 – 14</td><td>1</td><td></td><td>Intensity of ambient lighting from sky.</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Auto Exposure</strong> — <em>Auto exposure settings.</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Metering Mode</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td>Choose metering mode.</td></tr>
<tr><td><strong>Compensation</strong></td><td>Integer</td><td>0 – 24</td><td>12</td><td></td><td></td></tr>
<tr><td><strong>Range</strong></td><td>Range</td><td>0 – 15</td><td></td><td></td><td></td></tr>
<tr><td><strong>Adaptation</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td>The speed of auto exposure level change when the lighting condition changes.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Fog</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Fog level</td></tr>
<tr><td><strong>Light Limit</strong></td><td>Integer</td><td>0 – 16</td><td>8</td><td></td><td>Set max number of lights available in the scene.</td></tr>
<tr><td><strong>Shadow Limit</strong></td><td>Integer</td><td>0 – 16</td><td>4</td><td></td><td>Set max number of lights that can have shadows.</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Allocation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Auto Allocate</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Refresh Interval</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>How often does it reassign lights. In beats.</td></tr>
<tr><td><strong>Manual Refresh</strong></td><td>Action</td><td></td><td></td><td></td><td>Force reassign lights.</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

