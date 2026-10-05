---
layout: feature
title: "Tentacles"
locale: en-US
---

# Tentacles

Spawns and simulates procedural tentacle props attached to
the actor. Each tentacle is a segmented mesh driven by XPBD
physics with wiggle, coil, and attraction behaviors.

**Tentacle Count** and **Length** set the number and size.
The **Spawn** panel controls the cluster area: **Area Shape**
(Circle or Rectangle), **Area Size**, **Aspect Ratio**, and
**Length Distribution** for variation. **Radius**,
**Tapering**, and **Tip Radius** shape each tentacle's
thickness profile.

The **Behavior** panel drives animation: **Wiggle Speed**,
**Extent**, and **Lag** create organic sway; **Coil Extent**
and **Coil Fade** add spiral curling that fades toward the
tip. **Attraction** and **Attraction Offset** pull tentacle
tips toward a tracked body position. **Motion** syncs
movement to the sex motion system; **Motion Extent** scales
the response. **Back Out Distance** controls how far
tentacles retract.

**Material** and **X-Ray** sub-panels control appearance and
cross-section rendering. **Tentacle Props** defines global
physics parameters. Click **Rebuild Tentacles** after
changing count or spawn parameters to regenerate the mesh.


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

