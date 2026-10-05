---
layout: feature
title: "Sex Overlay & Dildo"
locale: en-US
---

# Sex Overlay & Dildo

Controls adult motion overlay and attachment props for an actor model.
This is a Pro-only feature and requires compatible skeletons.


## Pose

**Vertical Shift** raises or lowers the actor's root position — useful
for adjusting height relative to a partner or object. **Angle** sets
the forward/backward tilt of the motion axis, while **Random** adds
directional variance that fluctuates over time for organic feel.

**Arm IK Left** and **Arm IK Right** blend inverse-kinematics arm
correction so hands follow the body motion instead of floating in place.
Values above zero enable proportional IK influence.


## Motion

The motion subsystem drives rhythmic root offsets synced to the music
beat. Settings are managed by the nested Organic Motion panel, which
controls amplitude, frequency, and timing patterns.


## Attachment

The **Dildo** section configures a bone-attached prop with its own
model, surface material, and XRay cutaway. It can also drive hand
grab poses and leg IK when active.


## Settings reference

## Motion {#motion}

Reusable spring-driven thrust controller. A shaped driver curve
pushes one mass, a second mass trails behind it, and the gap
between them becomes the regulated travel used by paired motion
systems. This makes the cycle feel elastic rather than like a
raw sine wave.


### Tempo and Travel

**Extent** sets the maximum travel distance. **Auto Intensity**
can scale that travel from the current music level, while
**Auto BPM** and **Speed** control how quickly the cycle runs.
Use manual speed when you want consistent pacing; enable the
audio-driven controls when the motion should breathe with the
soundtrack instead.


### Driver Shape

**Top Duration**, **Bottom Duration**, and **Slope Balance**
shape the idealized cycle before the springs respond to it. A
longer top creates a held extension, a longer bottom creates a
more obvious reset, and slope balance shifts time between the
drive and return strokes. This is where you define whether the
motion feels punchy, even, or teasing.


### Spring Response

**Collision Distance** sets the resting separation between the
two spring masses. **Spring A**, **Damping A**, **Spring B**,
**Damping B**, and **Rest Spring** determine how tightly each
mass follows the driver and how much overshoot or softness is
left in the result. Stiffer values feel more mechanical; softer
values feel heavier but can get mushy if the cycle is fast.


### Visualization

**Visualize Curve** draws the target and spring responses in the
scene so you can tune the shape without guessing from the body
motion alone. It is a setup aid, not something you would keep on
during normal use.

<a id="settings-attachment"></a>
## Attachment settings (Dildo) {#dildo}

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

<a id="settings-anchor-offset"></a>
### Anchor offset (Anchor Offset) {#anchor-offset}

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

<a id="settings-accessory-alignment"></a>
### Size and alignment (Size & Alignment) {#size--alignment}

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

<a id="settings-toon-shading"></a>
### Toon shading (Toon Shader) {#toon-shader}

Overrides the actor's material with a global toon shader.

Enable the toggle to replace all materials with a unified toon
style. Adjust **Shading** and **Shadow** for the light/dark
balance, **Outline** for edge thickness, and **Ambient** for
the fill light level.

**Highlight Area** and **Soft Highlight** control how sharp
the bright areas are. **Shadow Area** and **Soft Shadow**
do the same for dark areas.

**Specular** and **Soft Specular** add shiny reflections
to lit surfaces.

**Receive Shadow** (non-HDRP only) lets the material
receive shadows from other objects.

<a id="settings-special-shader"></a>
### Special shader (Special Shader) {#special-shader}

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

<a id="settings-accessory-motion"></a>
### Attachment motion (Motion) {#motion-1}

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

<a id="settings-glow-color"></a>
### Color and glow (Color) {#color}

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

