---
layout: release
title: "Graphics"
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

# Graphics

Controls all rendering quality settings for the HDRP (HD and RT)
versions of DanceXR. Choose a preset to get a balanced starting
point, then tune individual features to hit your performance and
visual targets.


## Presets

Six presets cover the common range: *Performance* disables
reflections and most screen-space effects; *Medium* adds fog and
screen-space shadows; *High* enables screen-space reflections;
*Indoor GI* and *Outdoor GI* activate global illumination without
or with sky contribution; *Dither + TAA* pairs temporal
anti-aliasing with dithered transparency for a clean look.


## Anti-Aliasing & Super Sampling

**Anti-Aliasing** selects the per-camera technique — no AA,
SMAA (deferred), or TAA. **Super Sampling** unlocks DLSS or FSR
upscaling when supported, which can boost frame rate at the cost
of a small sharpness trade-off.


## Reflection

Screen-space reflections or a planar reflection probe. Use
*Screen Space* mode for general surfaces; switch to *Probe* for
flat floors or mirrors. Quality, edge fade distance, and fallback
behaviour are tunable in the sub-section.


## Ambient Occlusion & Global Illumination

**Ambient Occlusion** adds contact shadows in crevices for
grounded depth. **Global Illumination** adds indirect bounce
light — enable *Fallback To Sky* for outdoor scenes so surfaces
facing away from lights still receive sky colour.


## Post-Process Effects

**Depth Of Field** blurs out-of-focus objects around the tracked
actor. **Motion Blur** adds velocity-based blur on fast movement.
**Bloom** makes bright highlights glow. **Lens Flare** adds
screen-space scattering around bright light sources — disable in
VR to avoid discomfort.


## Fog

Enable volumetric fog and set its height band and maximum render
distance. Fog density itself is driven by the **Fog** slider in
the Lighting panel.


## Color Adjustment

Tonemapping, exposure, contrast, hue shift, saturation, a color
filter, a two-point tone curve, and white balance all live here.
The **Color Curve** maps input luminance to output luminance;
useful for stylised looks or protecting highlights.


## Options

Miscellaneous rendering flags: **Transparent Prepass** hides
objects seen through transparent surfaces; **Toon Shading**
switches actors or stages to a flat cel look; **Dithering
Transparency** forces stippled blending for all transparent
materials; **Bump Map Shadow** adds micro-shadow from normal
maps; **Compute Thickness** enables subsurface skin effects.


## Posterization

A custom-pass effect that adds outlines, posterized
illumination, or a halftone screen over the final frame — useful
for anime or comic-strip aesthetics.

# Sub-Components

## Reflection

Configures screen-space reflections or a planar reflection probe.
*Screen Space* mode ray-marches the depth buffer to find
reflected surfaces — it works on any geometry but cannot reflect
objects outside the camera view. Switch to *Probe* mode for flat
surfaces such as floors or mirrors, which uses a planar capture
that is always complete but costs more performance.


### Algorithm

In *Screen Space* mode, *Approximation* is faster and suits most
surfaces; *PBR Accumulation* is more physically accurate for
rough materials but requires TAA to converge cleanly.
**Edge Fade Dist** fades reflections near screen borders to hide
artefacts; **Object Thickness** controls how deep the march
assumes surfaces to be.


### Sky Reflection & Fallback

**Sky Reflection** allows the camera sky to contribute to
reflections on upward-facing surfaces. **Fallback To Sky** fills
in reflection probe coverage for areas the screen-space pass
misses, at the cost of a slight accuracy trade-off.

## Posterization

A full-screen custom pass that applies stylised effects over the
final rendered image. Four built-in presets give a quick starting
point: *Outline*, *Black & White*, *Posterize*, and *Halftone*.


### Outline

Traces edges based on depth and normal discontinuities. Control
**Outline Thickness** and **Outline Intensity** to dial in the
weight. Works well combined with toon shading in the Options
panel for a cel-animated look.


### Quantize Illumination & Color

**Quantize Illumination** reduces the number of luminance steps
in the image; lower values (e.g. 4–8) produce a bold posterized
look. **Quantize Color** does the same for color channels
independently. Set both to 0 to disable quantization entirely
and use only the other effects.


### Dithering & Halftone

**Dithering** adds ordered noise that breaks up banding in
smooth gradients. **Halftone** overlays a dot-screen pattern;
increase **Halftone Size** and **Strength** for a vintage
print aesthetic.



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Performance, Medium, <b>High</b>, Indoor GI, Outdoor GI, Dither + TAA, </td></tr>
<tr><td><strong>Anti-Aliasing</strong></td><td>Options</td><td>No AA, Deferred SMAA, Deferred TAA</td><td>Deferred SMAA</td><td></td><td></td></tr>
<tr><td><strong>Super Sampling</strong></td><td>Options</td><td>Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%</td><td>Off</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Reflection</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Algorithm</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>Algorithm for screen space reflection.</td></tr>
<tr><td><strong>Edge Fade Dist</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Object Thickness</strong></td><td>Float</td><td>0 – 0.1</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong>Fallback To Sky</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Fallback to sky color when raytracing has no hit.</td></tr>
<tr><td><strong>Sky Reflection</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Fog</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Volumetric Fog</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Base Height</strong></td><td>Float</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Max Height</strong></td><td>Float</td><td>10 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Max Distance</strong></td><td>Float</td><td>0 – 10000</td><td>5000</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Ambient Occlusion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Global Illumination</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Fallback To Sky</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Depth Of Field</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion Blur</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Bloom</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Quality</strong></td><td>Integer</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Lens Flare</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Disable in VR</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>This effect is not recommended for VR</td></tr>
<tr><td><strong>Intensity</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
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
<tr><td><strong>Flares</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Streaks</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>Length</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Chromatic Abberation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color Adjustment</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Tonemapping</strong></td><td>Integer</td><td>0 – 3</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>Adjustment</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable color adjustment.</td></tr>
<tr><td><strong>Post Exposure</strong></td><td>Integer</td><td>-12 – 12</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Contrast</strong></td><td>Float</td><td>-100 – 100</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Hue Shift</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Saturation</strong></td><td>Float</td><td>-100 – 100</td><td>1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Color Filter</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Color Mode</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Hue</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Satuation</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Brightness</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Red</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Green</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blue</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Color Curve</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Start Gradient</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Start Position</strong></td><td>Float</td><td>0 – 0.5</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Start Value</strong></td><td>Float</td><td>0 – 0.5</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>End Gradient</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>End Position</strong></td><td>Float</td><td>0.5 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>End Value</strong></td><td>Float</td><td>0.5 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>White Balance</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Enable white balance.</td></tr>
<tr><td><strong>Temperature</strong></td><td>Float</td><td>-100 – 100</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Tint</strong></td><td>Float</td><td>-100 – 100</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Posterization</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Outline, Black & White, <b>Posterize</b>, Halftone, </td></tr>
<tr><td><strong>Outline Thickness</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Outline Intensity</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Quantize Illumination</strong></td><td>Integer</td><td>0 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Quantize Color</strong></td><td>Integer</td><td>0 – 64</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Dithering</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Halftone Size</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Halftone size</td></tr>
<tr><td><strong>Halftone Strength</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>Halftone strength</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Options</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Transparent Prepass</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable transparent prepass. This will make obscured transparent materials invisible.</td></tr>
<tr><td><strong>Screen Space Shadows</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Contact Shadow</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Shadow for small details.</td></tr>
<tr><td><strong>Bump Map Shadow</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Enable shadows for bump map and detail map.</td></tr>
<tr><td><strong>Stop NaN</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Prevent black screen when error happens during post processing. </td></tr>
<tr><td><strong>Compute Thickness</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Calculate thickness that can be used in skin effect.</td></tr>
<tr><td><strong>Actor Model Toon Shading</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use toon shading for all actors.</td></tr>
<tr><td><strong>Stage Model Toon Shading</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Use toon shading for stages and props.</td></tr>
<tr><td><strong>Dithering Transparency</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

