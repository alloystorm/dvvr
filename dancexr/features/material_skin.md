---
locale: en-US
layout: single
toc: true
title: Skin Materials
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/material_skin) | [繁中](/tw/dancexr/features/material_skin) | [日本語](/jp/dancexr/features/material_skin) | [한국어](/kr/dancexr/features/material_skin) | [简中](/zh/dancexr/features/material_skin)


## Skin Materials
Controls properties of the materials that are categorized as skin materials.

Skin materials uses a special skin shader that enables subsurface scattering and has a procedural detail map that simulates detail textures of human skin.

Subsurface scaterring conflicts with metallic effect so if you use metallic effect on top of skin materials, the subsurface scattering effect will be disabled.

## Categorization
The system automatically puts materials that are named with certain keywords into the skin category. However this can sometimes be wrong, so you can manually assign materials to this category.

[How materials are categorized](material_settings.md#material-category)

## Settings
* Thickness: Thickness of the skin. This controls how much light is scattered inside the skin.
* Subsurface Intensity: Intensity of the subsurface scattering effect.
* Gloss: Glossiness of the skin.
* Detail Size: Size of the detail texture.
* Detail Map Bump: Intensity of the normal map of the detail texture.
* Detail Map Smooth: Smoothness of the detail texture.
* Detail Map AO: Ambient occlusion of the detail texture.
