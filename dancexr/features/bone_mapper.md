---
layout: release
title: XPS Bone Mapper
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

XPS (XNA Pose) models are widely used in the DanceXR community, but they don't ship with a standardised bone naming convention. Before DanceXR can animate an XPS model—applying motion data, physics, blinking, or eye contact—it needs to know which bone in the model corresponds to the head, the hips, the elbows, and so on. That's what the **XPS Bone Mapper** does: it lets you connect the model's bones to DanceXR's expected skeleton.

If you load a model and it stays frozen in the A-pose (or T-pose), unresponsive to animations and posing, this is the first thing to check.

{% include video id="g0VAfBHauXw" provider="youtube" %}

## The Mapping Status

DanceXR does a lot of the work automatically. When you open the bone mapper, most bones will already be mapped by the program's heuristic matching—it looks at bone names, hierarchy positions, and common conventions used by XPS creators. In most cases, you only need to fix a handful of critical bones that the auto-mapper couldn't identify.

The status of each bone is shown with a simple icon system:

- **Empty circle** — This bone is not mapped but is *non-critical*. The model will still animate and work without it. Examples include accessories, optional tail bones, or cosmetic joints.
- **Circle with dot** — The bone is already mapped. No action needed.
- **Circle with exclamation mark (!)** — This bone is not mapped and is *critical* for the model to function. These are the ones you need to fix. Common culprits are unusual bone names that didn't match DanceXR's internal lookup table.

When you see the "!" markers, click into each one and select the correct bone from the model's skeleton. Once the critical bones are assigned, the model should immediately become animated.

### How to Map a Bone

1. Select the bone with the "!" marker from the list.
2. In the model's bone hierarchy, find the correct matching bone. Bones are typically named something recognizable (e.g., `Head`, `Hips`, `LeftArm`, `RightFoot`).
3. Click to assign it. The icon should update to a dot.

If you're unsure which bone maps to what, a good rule of thumb is to follow the standard XPS naming convention: most creators name their bones in plain English, so `Hand_L` maps to `Left Hand`, `Hand_R` maps to `Right Hand`, and so on.

{% include video id="jtxQo5NYk2o" provider="youtube" %}

## Why Bone Mapping Matters

Proper bone mapping doesn't just enable basic animation—it's a prerequisite for almost every interactive feature in DanceXR:

- **Motion playback** — Imported dance motions won't apply to a model that can't find its hip and leg bones.
- **Physics and jiggle** — Breast, buttock, and other physics rely on knowing which bones to affect.
- **Lifelike Motion** — Eye contact, blinking, and breathing ([see related feature](/dancexr/features/eyecontact)) need to know where the head, eyes, and eyelids are.
- **Posing and morphs** — Manual posing requires the bone mapper to understand the model's joint structure.

In short, the bone mapper is the bridge between a static mesh and a fully interactive character.

### Dealing with Non-Standard Models

Some models use unconventional naming (Japanese terms, shortened names, or creator-specific labels). If auto-mapping leaves many "!" markers:

- Look for bones with similar *position* in the hierarchy rather than matching by name alone.
- Check the arms, legs, and spine first—those are the most critical.
- For FBX-to-XPS converted models, the names may carry over from the original format and can be more cryptic. The video below demonstrates converting an FBX model and mapping it step by step.

## More Demos

Here's a video demo of converting an FBX model into XPS format and then using the bone mapper to make it work in DanceXR:

{% include video id="YqX_uktVvQk" provider="youtube" %}
{% include video id="BV1CF411o7P2" provider="bilibili" %}

### Practical Tips

- **Save after mapping.** Once you've mapped the critical bones, the configuration is saved with the model profile—you won't need to redo it unless you reset the profile.
- **Batch similar models.** If you have several models from the same creator that use the same naming scheme, they'll often map identically. You can save time by cloning the profile.
- **Check character-specific props.** Some models carry weapons, wings, or tails that use custom bone names. The bone mapper handles these as optional ("empty circle") bones—they're nice to have mapped but not required for the model to dance.
