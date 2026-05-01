---
layout: release
title: "Actor Options"
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

# Actor Options

Settings that control how actor models are loaded and replaced.


## Caching

Models are kept in an in-memory cache after first load so switching
between actors is near-instant. **Cache Size** sets how many models
are held at once — increase it if you switch frequently, lower it
to reduce RAM use.


## Texture Compression

Enabling *Compress Textures* converts textures to a GPU-compressed
format on load. This reduces VRAM significantly for complex models
but may introduce minor quality loss on some materials.


## Transition

Controls transition effects when adding, removing or replacing actor
models. 


## Auto Actor Change

When multiple models are in cache, the value of *Auto Actor Change* 
will automatically switch between them at runtime. 

With the auto update enabled for this value you can achieve automatic 
actor switching from music progress or any other data source you choose.

# Sub-Components

## Transition Effect

Reusable transition effect applied when actors or other optional
meshes are added, removed, or replaced. The effect dissolves the
mesh along a moving edge with optional particles, color, and
glow — a single configuration drives both the shader-side burn
and the VFX spawn.


### Edge Shape

**Direction** picks whether the edge sweeps *Up* or *Down* the
mesh. **V Shape** bends the edge from a flat horizontal line
(0) into an angled V — useful for less mechanical-looking
dissolves. **Transition Mode** selects the pattern that breaks
up the edge: *Cells* for a chunky cellular look, *Mosaic* for
square tiling, *Noise* for a soft organic dissolve. **Scale**
resizes that pattern (logarithmic) and **Width** widens the
band the dissolve spans, from a sharp line to a diffuse fade.


### Color and Glow

**Color** is the burn color drawn at the leading edge of the
dissolve. **Glow** boosts that edge to an emissive intensity
so it reads as a hot burn rather than a tint. **Blend**
controls how much that burn color overrides the mesh's own
color in the transition band — drop it to keep the original
material visible through the effect.


### Duration and Particles

**Transition Duration** is an on/off float — toggle it on to
use a custom duration, off to fall back to the system default.
On Quest builds the transition is force-disabled regardless.
**Particle Effect** sets the spawn rate (logarithmic — 0
disables particles entirely) and **Particle Duration** sets
how long they live. If particle duration exceeds the
transition duration, the transition is stretched to match so
particles do not get cut off mid-air.



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Cache Size</strong></td><td>Integer</td><td>0 – 20</td><td>10</td><td></td><td>How many actor models to keep in cache</td></tr>
<tr><td><strong>Retain Options</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Automatically applies the settings from the outgoing actor to the incoming actor when replacing actors.</td></tr>
<tr><td><strong>Compress Textures</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Compress textures to reduce VRAM use</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Transition Effect</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Direction</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>The direction of the animation.</td></tr>
<tr><td><strong>V Shape</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td>Controls the angle of the edge, 0 is flat.</td></tr>
<tr><td><strong>Transition Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Scale</strong></td><td>Float</td><td>-3 – 3</td><td>0</td><td></td><td>Scale of the pattern.</td></tr>
<tr><td><strong>Width</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>The size of the transition area.</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
White, Black, Red, <b>Yellow</b>, Gray, Blue, Skin, Flesh, Orange, </td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0.1667</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Glow</strong></td><td>Float</td><td>0 – 10</td><td>1</td><td></td><td>Brightness of the burn effect.</td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Blend between the original color and the burn color. </td></tr>
<tr><td><strong>Transition Duration</strong></td><td>Float</td><td>0 – 5</td><td>2</td><td></td><td>The duration of the animation.</td></tr>
<tr><td><strong>Particle Effect</strong></td><td>Float</td><td>0 – 10</td><td>2</td><td></td><td>Controls the amount of particles.</td></tr>
<tr><td><strong>Particle Duration</strong></td><td>Float</td><td>0 – 5</td><td>2.5</td><td></td><td>Controls the lifetime of the particles.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Auto Actor Change</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Automatically switch between actors in the cache based on the value</td></tr>
</tbody>
</table>

