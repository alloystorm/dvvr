---
layout: release
title: Opaque Materials
locale: en-US
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



## Opaque Materials
Opaque materials are materials that are opaque and not included in skin, hair, eyes, or lips materials.

This is off by default to allow individual control of the materials in the material list. If you would like to apply consistent settings to all opaque materials, you can enable it and make adjustments here.

## Categorization
The system automatically determine if a material is opaque or transparent based on the information from the mesh (for XPS models), or the texture format (for PMX models). This can be wrong sometimes, so you can manually assign materials to this category.

[How materials are categorized](material_settings#material-category)

## Texture Enhancement
You can enhance the textures of the materials in this category by utilizing the the specular map for certain effects, generating normal map from the base map or the specular map, and using a custom detail maps to improve the details of the materials.

* [Using specular / mask map](specular_map)
* [Generating normal map](normal_map)
* [Using custom detail maps](custom_detail_map)