---
layout: release
title: Generate Normal Map
locale: en-US
toc: true
---

# Generate Normal Map

DanceXR can synthesize a normal map for a material that does not ship one, using the **base map** or the **specular map** as the source. This adds surface relief without requiring you to author or supply a separate normal map.

---

## When to use this

- A model's base texture has visible detail (fabric weave, scales, embroidery) but no separate normal map.
- A model's specular / mask map encodes detail you want as bump rather than as gloss.
- You want a quick, procedural detail layer on a flat material.

---

## How to enable it

1. Open the material settings for the relevant category — typically [Skin](material_skin), [Hair](material_hair), [Opaque](material_opaque), or [Custom](material_custom1).
2. Enable **Generate Normal Map**.
3. Choose the source: **base map** or **specular map**.
4. Adjust the strength.

The generated normal map is computed once and used at render time. There is no real-time per-frame cost beyond a normal-mapped material.

---

## Combining with other texture enhancements

Generate Normal Map sits in the same texture-enhancement family as:

- [Specular / Mask Map](specular_map) — using one source map for multiple PBR channels.
- [Custom Detail Map](custom_detail_map) — overlaying a tiling detail texture.
- [Hexagon Detail Map](hexagon_detail) — procedural hexagon pattern detail.

You can combine them — for example, a generated normal from the base map + a hexagon detail bump on top.

---

## Related pages

- [Specular / Mask Map](specular_map)
- [Custom Detail Map](custom_detail_map)
- [Hexagon Detail Map](hexagon_detail)
- [Material Settings](material_settings)
