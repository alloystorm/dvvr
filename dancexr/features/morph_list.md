---
layout: release
title: PMX Blendshape Morphs
locale: en-US
toc: true
---

# PMX Blendshape Morphs

PMX models ship with a list of named **morphs** (blendshapes) that the model author defined — facial expressions, mouth shapes, outfit toggles, body adjustments. The Morph List in DanceXR is where you browse and apply them.

The Morph List appears in the actor menu of any loaded **PMX** model. XPS models use the [Dressing system](optionals) instead.

---

## What a morph is

A morph is a stored deformation of the model — vertex positions, bone offsets, material parameters, or sub-mesh visibility — that can be blended in or out by a 0–1 value. PMX models commonly include:

- **Facial morphs** — happy, angry, sad, surprised, eye open/close, mouth shapes (a/i/u/e/o)
- **Bone morphs** — small skeleton tweaks
- **Material morphs** — color or transparency shifts (used by the [dressing system](optionals))
- **Vertex morphs** — direct mesh deformation
- **Group morphs** — combinations of the above

DanceXR reads these directly from the PMX file; you do not author them in DanceXR.

---

## Using the morph list

1. Open the actor menu (click the actor's selection disc).
2. Open the PMX model’s morph controls in the actor menu.
3. Enable **Override Value** for the PMX morph you want to adjust.
4. Change its value. With the override off, the normal motion-driven value is used. These controls require an edition with the feature unlocked.

Morphs stay applied until you change them or reload the model. Some morphs (like facial expressions) will be overridden by [Facial control](facial_control) and [Blink, breathing & eye contact](lifelike_motions#eye-contact) when those are active.

---

## Tips

- **Morph names depend on the author**. Japanese model authors usually name facial morphs in Japanese (まばたき, あ, い…). English models often use English names.
- **Material morphs** showing up here are typically the same ones surfaced by the [Dressing system](optionals); applying from either place has the same effect.
- For a long list, scroll through the author-defined names. Use **Application Settings → Use Translated Names** to compare translated and original labels; reload the model if needed.

---

## Related pages

- [Dressing system](optionals)
- [Facial control](facial_control)
- [Blink, breathing & eye contact](lifelike_motions#eye-contact)
- [Concepts & glossary](../concepts)
