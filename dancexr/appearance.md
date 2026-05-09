---
layout: release
title: Appearance & Materials
locale: en-US
toc: true
---

# Appearance & Materials

DanceXR's material system is highly customizable, with multiple layers of settings that stack to create the final look of an actor or objects on stage. You can change the materials' properties, swap textures, apply body paint, toggle outfit pieces, and more.

For per-feature detail, follow the links to each dedicated page. For terms used here (material slot, dressing system, alternative textures, body paint), see [Concepts & glossary](/dancexr/concepts#materials-and-appearance).

---

## The control layers

A loaded model's materials are controlled in multiple layers, from bottom to top:

1. **Individual Materials** — you can access each material individually and change settings one by one.
2. **Material slots** — materials are grouped into slots by surface type (skin, hair, eyes, lips, opaque, transparent, custom). Each slot has its own settings that apply to all materials in that category on the actor when turned on.
3. **Global material settings** — Global overrides that apply to all materials for the actor, for quick change of properties that needs to be consistent across the whole model (e.g. toon shading and alpha cutoff threshold for all transparent materials).
4. **Overlays** — layers drawn on top of the base materials, like outfit and body paint, sweat effect, detail maps, and specular/mask maps.
5. **System-wide render properties** — settings that apply to the entire scene, like unlit mode, shadow quality, raytracing effects, and transparent prepass.

Keep in mind that when you have higher level control enabled, the individual material settings may not have any effect.

---

## Mesh & visibility — the dressing system

The [Dressing system](/dancexr/features/optionals) combines the morphs from PMX and optional meshes from XPS to provide a unified interface for toggling the visibility of parts of the model. Use it to turn outfit pieces on and off, switch to alternative shapes, or hide specific body parts.

- For **PMX** models, it works through *material morphs* defined by the model author. Toggling shows or hides specific submeshes.
- For **XPS** models, it works through *optional items* defined per-slot.

Same UI in both cases. Use this for outfit changes, removing accessories the model came with, swapping hair sub-pieces, hiding limbs for special effects.

PMX models also expose individual morphs through the [Morph list](/dancexr/features/morph_list) — useful when a morph is not surfaced as a dressing toggle.

---

## Texture Enhancement (Pro)

- [Custom detail map](/dancexr/features/custom_detail_map) — a custom detail normal map.
- [Hexagon detail map](/dancexr/features/hexagon_detail) — built-in hexagon pattern detail.
- [Generate normal map](/dancexr/features/generate_normal_map) — auto-derive a normal map from the diffuse texture.
- [Specular / mask map](/dancexr/features/specular_map) — specular and mask map configuration.

---
## Textures — alternative texture sets

[Alternative textures](/dancexr/features/alternative_textures) lets you swap entire texture sets at runtime without editing the model.

How it works: place additional textures with **the same filenames** as the model's originals, in a different folder (or elsewhere in the same zip). DanceXR detects them and exposes a picker. Common use: multiple skin tones, day/night versions, recolored outfits.

You can also use [Texture enhancement](/dancexr/features/texture_enhancement) (Pro) to AI-upscale and sharpen textures at load time.

---

## Materials — the slot system

DanceXR groups materials into **slots** by surface type. Each slot has its own settings; settings on a slot apply to every material in that category on the actor when turned on.

| Slot | Use it for | Page |
|---|---|---|
| Skin | Body, face | [Skin materials](/dancexr/features/material_skin) |
| Hair | Head hair, body hair | [Hair materials](/dancexr/features/material_hair) |
| Eyes | Iris, sclera, eye highlights | [Eye materials](/dancexr/features/material_eyes) |
| Lips | Lips and inner mouth | [Lips materials](/dancexr/features/material_lips) |
| Opaque | Anything solid that does not fit a body slot — outfits, props on the model | [Opaque materials](/dancexr/features/material_opaque) |
| Transparent | Anything see-through — glass, sheer fabric, particles, hair tips | [Transparent materials](/dancexr/features/material_transparent) |
| Custom | Up to two free-form slots for shaders that need their own settings | [Custom materials](/dancexr/features/material_custom1) |

How a material gets into a slot:

- **PMX**: based on the material's properties in the model file (transparency, name hints).
- **XPS**: based on the slot you assign in the dressing system / bone mapper.

If something looks wrong (skin appearing as opaque, hair appearing as skin), it is usually a slot assignment problem.

---

## Overlays

Layers drawn on top of the base materials:

- [Outfit & body paint](/dancexr/features/outfit) — outfit slots and image-based body paint, drawn from images in `texture/drawing`.
- [Sweat effect](/dancexr/features/sweat_effect) — procedural sweat overlay on skin.

---

## Shading style

[Toon shading](/dancexr/features/toon_shading) toggles cel / anime-style shading per actor. The toon path uses different math for light wrap, shadow ramps, and rim lighting than the default PBR-style path. Choose based on the look you want; mixing is OK.

[Raytracing effects](/dancexr/features/raytracing) is a separate, scene-level feature (PC, RT build only) that affects shadow and reflection quality regardless of shading style.

---

## Common problems

| Symptom | Likely fix |
|---|---|
| You can see through hair | Transparency depth prepass — see [FAQ](/dancexr/faq#i-can-see-through-hair-materials) |
| Texture missing, model is white | Filename or path mismatch — see [FAQ](/dancexr/faq#model-loads-but-everything-is-white) |
| Skin looks plastic / shiny | Adjust [skin materials](/dancexr/features/material_skin) — typically reduce specular |
| Outfit cannot be removed | The model author has to expose it as a morph (PMX) or optional (XPS); use [Dressing system](/dancexr/features/optionals) to find what is available |
| Texture looks low-res | Try [Texture enhancement](/dancexr/features/texture_enhancement), or place a higher-res alternative texture |
| Sky sphere looks pixelated / has holes | Multiple transparent sky spheres + transparency depth prepass; see [FAQ](/dancexr/faq) |

---

## Further reading

- [Concepts & glossary](/dancexr/concepts#materials-and-appearance)
- [Working with actors](/dancexr/actors)
- [Physics system](/dancexr/physics) — for cloth and hair motion (separate from cloth materials)
- [Content library](/dancexr/preparecontent) — `texture/`, `drawing/`, `mask/` folders
