---
layout: release
title: "Outfit & Bodypaint"
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

# Outfit & Bodypaint

Outfit applies a procedural fabric/paint layer over the character's
skin material — used to add stockings, bodysuits, latex, hexagon
detail, freehand body paint, and dissolve transitions without
touching the underlying mesh or textures.


## Mode

**Mode** picks how the layer behaves. *Color Paint* turns the
character into a canvas you draw on directly with the cursor —
pick a brush color and paint freely. *Outfit* hides the painting
tools and instead drives the layer from the procedural
shape/pattern settings, so you get clean stockings or bodysuits
generated from parameters. *Outfit Paint* combines both: the
procedural shape defines the outfit area, and you paint on top
of it. The visibility rules in the panel collapse the unrelated
sub-sections automatically once the mode is set.


## Presets

Seven built-in presets cover the common cases — Body Paint,
Fullbody Latex, V-Shape Fishnet, two stocking variants, and two
bodysuits. They seed the mode, shape, and the three surface
presets in one click; treat them as starting points to tweak
rather than final looks.


## Body Paint

See the *Body Paint* sub-section. Brush size, rotation, color,
stamp texture, and save/load drawing live there. Visible only
in Color Paint and Outfit Paint modes.


## Shape & Pattern

See the *Shape* sub-section. Controls the procedural geometry of
the outfit — stocking heights, top lines, fishnet/maze/curve
line patterns, and bump effects along borders. Hidden in pure
Color Paint mode since there is no procedural outfit to shape.


## Surfaces

Three surface layers stack on the outfit: **Surface Base** is
the main fabric (latex, stocking, gold, etc.), **Surface
Pattern** drives the line/maze pattern fill, and **Surface
Border** controls the trim around shape edges. Each is a full
surface block (metallic, gloss, color, anisotropy, dissolve,
special shaders) so you can mix e.g. matte stockings with a
glowing border. Hidden in Color Paint mode.


## Hexagon Detail

See the *Hexagon Map* sub-section. Adds a procedural hex /
circle micro-pattern on top of the surface for fishnet-style
detail or sci-fi panels. Toggle off when you want a smooth
fabric.


## Dissolve

**Dissolve** is the master amount (0 – 1) that fades the outfit
away along the dissolve map — drive it with auto-update for
tearing/melting transitions synced to music or other data.
The *Dissolve Map* sub-section configures the map itself:
pattern frequency, edge width and bump on both sides of the
cutoff, X/Y offsets, and a hard cutout toggle. Hidden in pure
Color Paint mode.

# Sub-Components

## Body Paint

Freehand painting on the character's body. Drag the cursor (or
VR pointer) across the model to apply color or pattern strokes
directly onto the outfit canvas. The canvas persists across
frames so you can build up a drawing over time, save it as a
texture, and reload it later.


### Brush

**Brush Size** and **Brush Rotation** set the stroke shape;
rotation only matters when a stamp texture is selected.
**Texture** picks an optional stamp — when set, each click
stamps a single decal instead of drawing a continuous stroke,
which is the right choice for tattoos or logos. **Brush Type**
selects which channel you're painting (Base / Pattern / Edge /
Erase) when in *Outfit Paint* mode; in *Color Paint* mode the
channel is implicit and this is hidden.


### Color, Glow & Preserve

**Color** is the brush color in Color Paint mode. **Glow**
multiplies the painted color's intensity (above 1 it becomes
emissive). **Preserve Color** biases the glow boost so it
amplifies brightness without washing out the color's hue —
useful when you want a saturated neon look rather than a
bleached bright one. **Erase** flips the brush to clear instead
of paint.


### Paint Side

Restricts strokes to *Front*, *Back*, or *Both* sides of the
body. Pick a side when you want a design only on the chest or
only on the back without having to carefully avoid the other.


### Canvas Actions

**Clear Canvas** wipes the drawing. **Save Drawing** writes the
current canvas to disk as both an HDR and PNG so the full
colour/glow range survives a round-trip. **Load Drawing** picks
a previously saved drawing (or any drawing texture in the
library) as the canvas contents.

## Shape

Procedural geometry for the outfit layer — defines where the
outfit covers the body and what pattern fills it. Everything is
computed in shader, so changes are live and free of texture
authoring.


### Stocking & Top Lines

Outfits are bounded by up to three diagonal cuts: one stocking
line (the bottom of the leg cover) and two top lines (V-neck
style cuts on the torso). Each line has a **Height** (where it
crosses the centre) and an **Angle** (tilt away from
horizontal). Combine the three to draw stockings, V-shape
bodysuits, fishnet halters, etc. **Stocking Edge** and
**Top Edge** soften the cut into a gradient — small values give
a hard hem, larger values fade the outfit into skin.


### Line Pattern

**Line Pattern Type** picks the fill: *None* leaves the area
solid, *Grid* tiles a fishnet, *Maze* and *Maze Curve* generate
non-repeating maze lines, *Parallel* draws stripes.
**Line Pattern Density** sets the line spacing,
**Line Pattern Rotation** rotates the whole pattern,
**Line Pattern Symmetric** mirrors it across the body's centre
so left and right match. **Line Pattern Seed** reshuffles the
random maze without changing density. **Border Size In/Out**
control how thick the line is on each side of its centre — use
the asymmetry to suggest stitching or piping.


### Bump

**Inside / Outside Bump** raises or lowers the surface near the
line edges, with **Inside / Outside Distance** controlling how
far the bump bleeds. Subtle positive bump reads as raised
stitching; negative bump reads as a pressed seam.

## Hexagon Map

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

## Dissolve Map

Generates the noise map that drives the parent's *Dissolve*
slider. The map is built from two layered patterns and an edge
profile, so the same dissolve amount can read as cracking,
burning, melting, or a clean cut depending on these settings.


### Layer 1 & Layer 2

Two independent noise layers combine to break up the dissolve
front. **Pattern L1 / L2** pick a noise variant (different
values produce visibly different shapes). **Density L1 / L2**
control how fine each layer is — L1 is typically the broad
shape, L2 the small-scale detail. **Magnify Scale** zooms both
layers, **Curve** sharpens or softens the dissolve gradient.


### Edges

Where the outfit dissolves it leaves a transition band on each
side of the cutoff. **Edge Size** and **Edge Bump** shape the
band on the still-visible side; **Inverse Edge Size / Bump**
shape the band on the dissolved side. Negative bump indents
the surface (good for char/burn looks); positive bump raises
it. **Cutout** discards dissolved pixels entirely instead of
fading their alpha — pick this when you want the outfit to
vanish hole-by-hole rather than fade out.


### Offset

**Offset X / Y** slide the dissolve map across the body. Animate
them (via auto-update) to make the dissolve front sweep in a
direction rather than appear uniformly.



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Body Paint</b>, Fullbody Latex, V Shape Fishnet, Stockings, Stockings Fishnet, Bodysuit 1, Bodysuit 2, </td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Body Paint</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Paint Side</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Texture</strong></td><td>Options</td><td>[None], [Tattoo]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>Brush Size</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Brush Rotation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brush Type</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Erase</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
White, Black, Red, <b>Yellow</b>, Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Preserve Color</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Clear Canvas</strong></td><td>Action</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>Save Drawing</strong></td><td>Action</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>Load Drawing</strong></td><td>Options</td><td>[None]</td><td>[None]</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Shape &amp; Pattern</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Fullbody</b>, V Shape, Stockings, Fishnet Fullbody, Fishnet V Shape, Fishnet Stockings, Maze 1, Maze 2, Curve 1, Curve 2, </td></tr>
<tr><td><strong>Top Height1</strong></td><td>Float</td><td>0 – 3</td><td>3</td><td></td><td>Height of the first line at center</td></tr>
<tr><td><strong>Top Angle1</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>Angle of the first line</td></tr>
<tr><td><strong>Top Height2</strong></td><td>Float</td><td>0 – 3</td><td>3</td><td></td><td>Height of the second line at center</td></tr>
<tr><td><strong>Top Angle2</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>Angle of the second line</td></tr>
<tr><td><strong>Top Edge</strong></td><td>Float</td><td>0 – 0.2</td><td>0.05</td><td></td><td>Edge width for the first and second lines</td></tr>
<tr><td><strong>Stocking Height</strong></td><td>Float</td><td>0 – 3</td><td>1.45</td><td></td><td>Height of the stocking line at center</td></tr>
<tr><td><strong>Stocking Angle</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>Angle of the stocking line</td></tr>
<tr><td><strong>Stocking Edge</strong></td><td>Float</td><td>0 – 0.2</td><td>0.05</td><td></td><td>Edge width for the stocking line</td></tr>
<tr><td><strong>Pattern Type</strong></td><td>Integer</td><td>0 – 4</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pattern Symmetric</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Pattern Density</strong></td><td>Float</td><td>1 – 50</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>Pattern Rotation</strong></td><td>Float</td><td>0 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pattern Seed</strong></td><td>Float</td><td>10 – 50</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>Border Size In</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Border Size Out</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Outside Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Outside Distance</strong></td><td>Float</td><td>0 – 0.025</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong>Inside Bump</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Inside Distance</strong></td><td>Float</td><td>0 – 0.1</td><td>0.005</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hexagon Map</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Density</strong></td><td>Float</td><td>0 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Size</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>-1 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Noise</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Use Circle</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Soft Edge</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>UV Projection</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Projection Radius</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Rotation</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Surface Base</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Stocking Thin</b>, Stocking Thick, White Stocking, Latex, Clear Latex, Silver, Gold, Glow White, Original, </td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
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
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Blend</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Anisotropy</strong></td><td>Float</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>Stocking Effect</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Stocking Gradient</strong></td><td>Float</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Detail Density</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Enable Dissolve</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Surface Pattern</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Stocking Thin</b>, Stocking Thick, White Stocking, Latex, Clear Latex, Silver, Gold, Glow White, Original, </td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Metallic</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bump</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
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
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Blend</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Anisotropy</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Stocking Effect</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Stocking Gradient</strong></td><td>Float</td><td>-3 – 3</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Detail Density</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Enable Dissolve</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Surface Border</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Stocking Thin</b>, Stocking Thick, White Stocking, Latex, Clear Latex, Silver, Gold, Glow White, Original, </td></tr>
<tr><td><strong>Gloss</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
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
<tr><td><strong>Blend Mode</strong></td><td>Options</td><td>Original, Multiply, Blend, Color Shift</td><td>Blend</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Alpha</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Anisotropy</strong></td><td>Float</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>Stocking Effect</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Stocking Gradient</strong></td><td>Float</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Detail Density</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Enable Dissolve</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Dissolve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Dissolve Map</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Pattern L1</strong></td><td>Float</td><td>0 – 90</td><td>13</td><td></td><td>Change the level 1 pattern when generating the dissolve map</td></tr>
<tr><td><strong>Density L1</strong></td><td>Float</td><td>1 – 10</td><td>3.5</td><td></td><td>Density of level 1 pattern</td></tr>
<tr><td><strong>Pattern L2</strong></td><td>Float</td><td>0 – 90</td><td>31</td><td></td><td>Change the level 2 pattern when generating the dissolve map</td></tr>
<tr><td><strong>Density L2</strong></td><td>Float</td><td>10 – 100</td><td>50</td><td></td><td>Density of level 2 pattern</td></tr>
<tr><td><strong>Magnify Scale</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Edge Size</strong></td><td>Float</td><td>0 – 0.2</td><td>0.05</td><td></td><td>Width of the edge in the positive area</td></tr>
<tr><td><strong>Edge Bump</strong></td><td>Float</td><td>-1 – 1</td><td>-1</td><td></td><td>Bump effect of the edge area</td></tr>
<tr><td><strong>Inverse Edge Size</strong></td><td>Float</td><td>0 – 0.2</td><td>0.05</td><td></td><td>Width of the edge in the negative area</td></tr>
<tr><td><strong>Inverse Edge Bump</strong></td><td>Float</td><td>-1 – 1</td><td>-1</td><td></td><td>Bump effect of the edge area</td></tr>
<tr><td><strong>Offset X</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Offset the dissolve map in X direction</td></tr>
<tr><td><strong>Offset Y</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Offset the dissolve map in Y direction</td></tr>
<tr><td><strong>Cutout</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Make the dissolved area invisible</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Manual Selection</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Select Material</strong></td><td>Selection</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

