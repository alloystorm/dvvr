---
locale: en-US
layout: single
toc: true
title: Transparent Materials
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/material_transparent) | [繁中](/tw/dancexr/features/material_transparent) | [日本語](/jp/dancexr/features/material_transparent) | [한국어](/kr/dancexr/features/material_transparent) | [简中](/zh/dancexr/features/material_transparent)


## Transparent Materials
Transparent materials are materials that are transparent and not included in skin, hair, eyes, or lips materials.

This is off by default to allow individual control of the materials in the material list. If you would like to apply consistent settings to all transparent materials, you can enable it and make adjustments here.

## Categorization
The system automatically determine if a material is opaque or transparent based on the information from the mesh (for XPS models), or the texture format (for PMX models). This can be wrong sometimes, so you can manually assign materials to this category.

[How materials are categorized](material_settings.md#material-category)

## Texture Enhancement
You can enhance the textures of the materials in this category by utilizing the the specular map for certain effects, generating normal map from the base map or the specular map, and using a custom detail maps to improve the details of the materials.

* [Using specular / mask map](specular_map.md)
* [Generating normal map](generate_normal_map.md)
* [Using custom detail maps](custom_detail_map.md)