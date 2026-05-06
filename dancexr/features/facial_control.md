---
layout: feature
title: "Facial Control"
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

# Facial Control

Facial Control gives you direct, per-expression sliders for the
face of XPS / FBX models — mouth shapes, eyebrow poses, and eyelid
positions — so you can craft any expression the model supports.
Whether you are triggering a quick smile for a photo, morphing
through vowel shapes for lip sync, or dialling in a subtle worried
brow for a dramatic scene, these sliders put every facial pose at
your fingertips.

The system works alongside [Auto Dance](/dancexr/features/autodance)
and motion playback — facial animation blends on top of body motion
automatically, so your character can walk, dance, and emote at the
same time.


## Mouth Shapes

The mouth shape sliders control the character's oral cavity and lip
positions, covering both the phoneme-based vowel shapes and common
emotional expressions:

- **A, I, U, E, O** — the five cardinal vowel phonemes, used
  primarily by the **Use Lip Sync** system (see below). Each shape
  matches the mouth position for that spoken vowel.
- **Grinning** — a wide, teeth-baring smile.
- **Smile 1, 2, 3** — increasingly intense smiles. Smile 1 is a
  subtle lip curl; Smile 3 is a full, open-mouthed smile.
- **Frown** — downturned mouth corners for sadness or displeasure.

Mix multiple shapes together — a Grinning and a Smile can compound
for extra width, or you can blend A with Frown for an asymmetrical
look. The sliders range from 0 (neutral) to 1 (full expression).


## Eyebrow Poses

Eyebrow sliders adjust the brow ridge position independently of the
mouth, giving you control over emotional valence and intent:

- **Smile** — raised inner brows, a warm expression that pairs well
  with Smile mouth shapes.
- **Upper** — both brows raised, indicating surprise or attention.
- **Lower** — brows lowered slightly, suggesting concentration or
  suspicion.
- **Worry** — inner brows raised and drawn together, for concern or
  anxiety.
- **Angry 1, 2** — brows pulled down and in, with Angry 2 being the
  more extreme version. Combine Angry with a Frown mouth for a full
  anger expression.

Because these are independent sliders, you can create nuanced
blends — Worry brows with a Smile mouth, for instance, reads as
nervous reassurance or bittersweetness. Experiment with non-obvious
combinations to find natural-looking, character-specific expressions.


## Eyelid Poses

Eyelid controls shape the eyes' opening and closure:

- **Blink** — a momentary full closure, typically triggered by a
  timer in motion playback.
- **Jito** — narrowing the eyes (also known as a squint or "side
  eye"), useful for suspicion or intensity.
- **Wink** — closing one eye while the other remains open. Works best
  paired with Smile or Grinning for a playful look.
- **Laugh** — strongly squinted, crinkled eyes that accompany a
  wide smile or open-mouthed laughter.
- **Narrow** — a general partial closure, less intense than Jito.
  Useful for bright-light or mild-concentration expressions.

Eyelid poses are independent per eye where the model supports it,
though most XPS models apply them symmetrically. Combine Narrow or
Jito with the [raytracing](/dancexr/features/raytracing) ambient
occlusion effect to add subtle shadow depth around the eye sockets.


## Use Lip Sync

The **Use Lip Sync** toggle switches from manual slider control to
automatic, audio-driven mouth animation. When enabled, the system
reads the frequency envelope of the currently playing audio (from
the music player or a video file) and maps the dominant phoneme onto
the A, I, U, E, O shapes in real time. This produces convincing
spoken-vowel shapes without keyframing.

Lip Sync works best when the character is close enough to the camera
for the mouth to be clearly visible. For distant or background
characters, manual expression presets are usually sufficient. The
mouth shape sliders are disabled while Lip Sync is active, but
eyebrow and eyelid controls remain available — use them to add
emotional context on top of the synced speech shapes.


## Disable and Extent

**Disable** turns off all facial animation — both the manual sliders
and any Lip Sync or motion-driven facial data. Use this when a
character's face should remain entirely neutral, such as for a
prop character or a static background figure.

**Extent** is a set of three independent multipliers that scale the
range of mouth, eyebrow, and eyelid movement respectively. The
default value of 1.0 corresponds to the model's authored range.
Some XPS models animate subtly; raising Extent to 1.5–2.0
exaggerates the motion for more readable expressions. Others animate
too broadly — lowering Extent to 0.5–0.7 reins them in without
disabling animation entirely.

These per-part Extent sliders are your first debugging tool when
facial animation looks wrong: if the mouth seems frozen, check the
mouth Extent isn't set to 0. If expressions look over-the-top,
dial all three Extents back proportionally.


## Practical Tips

- **Freeze a look for screenshots** — set the desired expression,
  then toggle **Disable** to lock it. The face won't change even if
  motion or audio continues.
- **Tune Extent before tweaking individual sliders** — it is much
  faster to adjust one multiplier than to rebalance five mouth
  shapes.
- **Pair Lip Sync with a [motion file](/dancexr/features/assign_motion)
  or [Auto Dance](/dancexr/features/autodance)** for characters that
  talk and move simultaneously — the two systems blend automatically.
- **Model-specific behaviour** — not all XPS/FBX models expose every
  shape listed. If a slider appears to do nothing, the model likely
  lacks that morph target. Check the model's documentation or try a
  different model.
