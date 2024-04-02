---
locale: en-US
layout: single
toc: true
title: Hexagon Pattern Detail Map
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/hexagon_detail) | [繁中](/tw/dancexr/features/hexagon_detail) | [日本語](/jp/dancexr/features/hexagon_detail) | [한국어](/kr/dancexr/features/hexagon_detail) | [简中](/zh/dancexr/features/hexagon_detail)


## Hexagon Pattern Detail Map
This is a procedural detail map that is generated on the fly. It can be used in material categories that support detail maps and the Outfit effect.

## Settings
* Density: The density of the hexagons.
* Circle: Use a circle instead of a hexagon.
* Size: The size of the center area of the hexagon.
* Bump: Intensity of the bump effect on the hexagon sides. It can be negative to invert the bump direction.
* Noise: Add a random direction to the normal map for each hexagon cell.
* Soft edge: Soften the edge of the hexagon to allow it to blend into the normal texture.

## Typical usages
* Add a hexagon pattern bump effect for materials: Enable the detail map and the hexagon pattern, adjust the bump value for the desired effect.
* Add a glittering effect for materials: Enable the detail map and the hexagon pattern, increase density, increase the noise value, adjust smoothness and metallic values for the desired effect.

{% include video id="G9SSJQieO-E" provider="youtube" %}

{% include video id="BV1VD421W7YK" provider="bilibili" %}