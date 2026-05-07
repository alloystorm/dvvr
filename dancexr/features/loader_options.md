---
layout: feature
title: "Actor Options"
locale: en-US
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

