---
layout: release
title: Hair Materials
locale: en-US
toc: true
---

# Hair Materials

Controls properties of the materials categorized as **hair**. Hair materials use a special shader with **anisotropic** highlights to produce the directional sheen that real hair has — a long stripe of specular along the hair flow rather than a circular highlight.

---

## What this category controls

- **Base color** and **smoothness** — the same controls as other material categories.
- **Anisotropic highlight** — the shape and intensity of the directional sheen.
- **Hair flow direction** — which way the highlight runs across the strand.
- <!-- TODO: confirm whether two-tone / tip-color / scatter parameters are exposed. -->

The hair shader received improvements over time. Notable releases:

- **2024.5** — improved procedural hair detail map.
- **2025.10** — better LW / Android skin and hair shaders, less excessive sky reflection on hair.

---

## Categorization

DanceXR auto-assigns materials whose names match common hair keywords to this category. If a model misclassifies its hair (or assigns hair material names to non-hair geometry), reassign manually from [Material Settings](material_settings).

[How materials are categorized](material_settings#material-category)

---

## Hair physics is separate

Hair **movement** — the bones swinging when the head turns or the actor walks — is configured in [Hair Physics](hair_physics) (or via [Particle Dynamics](particle_dynamics) on the new simulation system). The materials page only controls how hair surfaces render.

---

## Related pages

- [Material Settings](material_settings)
- [Skin Materials](material_skin)
- [Hair Physics](hair_physics)
- [Particle Dynamics](particle_dynamics)
- [Toon Shading](toon_shading)
