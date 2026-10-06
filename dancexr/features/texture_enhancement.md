---
layout: release
title: Texture Enhancement
locale: en-US
---

# Texture Enhancement

Texture enhancement changes how an existing material responds to light. Start with one material, inspect its textures, and enable one effect at a time. Use the [material list](material_settings#material-list) for an individual change, or a category when several materials should share the result.

{% include video id="uk7QGK3rOQk" provider="youtube" %}

## Specular / mask map {#specular-mask-map}

A packed texture can control several properties through its red, green, blue and alpha channels. Open the texture preview to inspect those channels before assigning their purpose. Choose the channel for metallic, occlusion, smoothness or glow in the relevant map controls, then adjust its strength. For current texture types and channel assignments, see [Material Settings → Textures](material_settings#textures).

If a surface becomes unexpectedly dark or shiny, check the channel assignment before changing the entire material's color. A roughness map uses the inverse convention of smoothness; select the matching purpose rather than treating them as interchangeable.

## Generate normal map {#generate-normal-map}

Use **Generate Normal Map** when a material has useful detail in its base or specular map but no suitable bump texture.

1. Open the material or category's texture enhancement controls.
2. Enable **Generate Normal Map** and choose the base or specular source.
3. Start with a small intensity, then inspect the actor under angled lighting.
4. Compare with the effect disabled. Reduce intensity if printed colors or seams turn into excessive raised edges.

This estimates relief from an image; it cannot recover the original surface geometry. Use an authored normal map when one is available and gives a better result.

## Custom detail map {#custom-detail-map}

A detail map adds a repeating layer such as fabric grain or fine surface bumps. Choose a built-in map, or place your own image in the `textures` folder of the [content library](../preparecontent). Select the map in **Detail Map**, adjust its scale and rotation, then tune **Detail Map Bump** while viewing the model at its normal camera distance.

Keep the detail subtle enough that the base texture remains readable. If the pattern looks stretched, compare different parts of the model: texture coordinates and material scale affect the result.

## Hexagon pattern {#hexagon-pattern}

The procedural hexagon detail works in supported material detail maps and the [Outfit effect](outfit).

| Control | Result |
|---|---|
| Density | Changes how many cells cover the surface. |
| Circle | Uses circles instead of hexagons. |
| Size | Changes the center area of each cell. |
| Bump | Raises or inverts the cell edges; negative values reverse the relief. |
| Noise | Varies the normal direction between cells. |
| Soft Edge | Blends cell boundaries into the surface. |

For patterned relief, begin with low Bump and adjust Density to fit the garment. For glitter, increase Density and Noise, then tune the material's smoothness and metallic response under moving light.

{% include video id="G9SSJQieO-E" provider="youtube" %}
{% include video id="BV1VD421W7YK" provider="bilibili" %}

## Gradient control {#gradient-control}

Gradient controls vary material properties along a path. Set the start and end appearance, then inspect the transition on the model before combining it with detail or generated bump effects.

{% include video id="Yi2W_cwufNk" provider="youtube" %}
{% include video id="d8GP3G0wF3M" provider="youtube" %}
{% include video id="atIdSd2TIrA" provider="youtube" %}
