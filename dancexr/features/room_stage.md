---
layout: feature
title: "Room Stage Settings"
locale: en-US
---

# Room Stage Settings

Creates a procedural room around the scene. Choose a preset first, then adjust its shape and surfaces. This is an enclosed environment; Ground's Stage / Pool controls instead create a platform or pool, and [Stages](stages) describes imported stage models.

## Build a simple room

1. Open **Room Stage Settings** and select **Wood Seamless** for a starting room, or **Glow Box** for a box-shaped scene.
2. Open **Shape** and choose **Box** or **Circle**. Set **Radius** and **Height** so the actors have room to move.
3. Use **Offset X** and **Offset Z** to align the room with the performance area. **Rotation** turns the entire room around the vertical axis.
4. Adjust **Ceiling**, **Walls** and **Floor** independently. **Back** and **Edge** have their own surface settings as well.
5. Set the [lighting](lighting) after the geometry and surfaces are in place. For an indoor look, reduce sky ambient lighting if it washes out the room.

## Shape and appearance

**Edge Radius** rounds the room edges and **Edge Steps** controls their subdivisions. **Gap** adds spacing between elements. The five surfaces each expose their own material/texture settings so the floor and walls do not have to share a look.

The preset list also includes **Projector Screen Far**, **Projector Screen Near**, **Emissive Screen** and **Gloss Circle**. Presets set both geometry and surface appearance; fine-tune them after selection. [Screen](screen) describes a separate media prop, while [Video Player](video_player) controls playback.

Save the finished arrangement with [Save Scene](save_scene) when you want to restore the complete performance setup.


## Settings reference

<a id="settings-toon-shading"></a>
## Toon shading (Toon Shader) {#toon-shader}

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

## Audio Visualizer {#audio-visualizer}

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

<a id="settings-glow-color"></a>
### Color and glow (Ring Color) {#ring-color}

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

### Background Color {#background-color}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Foreground Color {#foreground-color}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

## Toon Shader {#toon-shader-1}

See [Toon shading](#settings-toon-shading). Defaults and available controls for this instance are listed in Config Reference.

## Special Shader {#special-shader-1}

See [Special shader](#settings-special-shader). Defaults and available controls for this instance are listed in Config Reference.

## Audio Visualizer {#audio-visualizer-1}

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

### Ring Color {#ring-color-1}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Background Color {#background-color-1}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Foreground Color {#foreground-color-1}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

## Toon Shader {#toon-shader-2}

See [Toon shading](#settings-toon-shading). Defaults and available controls for this instance are listed in Config Reference.

## Special Shader {#special-shader-2}

See [Special shader](#settings-special-shader). Defaults and available controls for this instance are listed in Config Reference.

## Audio Visualizer {#audio-visualizer-2}

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

### Ring Color {#ring-color-2}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Background Color {#background-color-2}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Foreground Color {#foreground-color-2}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

## Toon Shader {#toon-shader-3}

See [Toon shading](#settings-toon-shading). Defaults and available controls for this instance are listed in Config Reference.

## Special Shader {#special-shader-3}

See [Special shader](#settings-special-shader). Defaults and available controls for this instance are listed in Config Reference.

## Audio Visualizer {#audio-visualizer-3}

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

### Ring Color {#ring-color-3}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Background Color {#background-color-3}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Foreground Color {#foreground-color-3}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

## Toon Shader {#toon-shader-4}

See [Toon shading](#settings-toon-shading). Defaults and available controls for this instance are listed in Config Reference.

## Special Shader {#special-shader-4}

See [Special shader](#settings-special-shader). Defaults and available controls for this instance are listed in Config Reference.

## Audio Visualizer {#audio-visualizer-4}

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

### Ring Color {#ring-color-4}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Background Color {#background-color-4}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

### Foreground Color {#foreground-color-4}

See [Color and glow](#settings-glow-color). Defaults and available controls for this instance are listed in Config Reference.

## Shape {#shape}

Nested config for room geometry. **Shape** selects Box or
Circle. **Radius** and **Height** set room size. **Edge
Radius** rounds corners. **Edge Steps** controls edge mesh
subdivision. **Offset X/Z** shifts the room. **Gap** adds
spacing between surfaces. **Wall/Edge/Ceiling Shadow**
toggles shadow casting per surface.

