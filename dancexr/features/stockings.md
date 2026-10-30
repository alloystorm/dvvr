---
layout: feature
title: Stockings
locale: en-US
toc: true
---

# Stockings

**Stockings** puts a sheer knit over a character's skin in DanceXR Native. It is not a garment mesh: the skin's own material is shaded as if a knit were stretched over it, so it works on any model and in both the path tracer and the raster renderer. The knit gets **thinner where the skin stretches** (bent knees) and **thicker where it relaxes**, following the body as it moves. It is a **Pro** feature in every edition.

Switch it on at **Actors > actor > Stockings**.

---

## Where it covers

- **Region** chooses how far it reaches: legs, legs and hips, the body, or the body and arms. Hands are never covered.
- **Height** sets the hem above the model's lowest point, **Angle** tilts it toward the sides (negative rises outward), and **Edge** softens it (0 is a hard line). The hem stays on the same place on the leg whatever the pose.

## Look

**Colour** and **Smoothness** (the fabric's gloss) set the knit's look. **Base Density** is how much of the skin the fabric hides head-on and unstretched: low is sheer, 1 is opaque. **Taper** adds more yarn toward the top so the thighs keep their color against the stretch, and **Fresnel Power** sets how fast the fabric thickens toward the limb's silhouette. **Live Update** re-measures the pose every frame so stretch and folds follow the body, and **Skin Only** keeps the fabric off clothing and shoes in the region.

### Welt and Edge

The band of heavier knit just inside the hem, the way a stocking's top is finished:

- **Welt Width** and **Welt Density**: the band itself and how much skin it hides.
- **Rim Width** and **Rim Bump**: the rolled rim of the welt rising at its edge.
- **Skin Width** and **Skin Bump**: the skin just outside the hem pressed in by it.

## Signals

The **Signals** submenu chooses what makes the knit thinner or thicker:

- **Relaxed Girth** and **Girth Strength**: the fabric's unstretched girth; wherever the body is thicker, the fabric is pulled thinner.
- **Pose Stretch Strength** and **Squeeze Strength**: how much the pose's stretch thins the fabric, and how much squeezing thickens it.
- **Crease Strength (Rest)** and **Crease Strength (Pose)**: thickening in folds the body has at rest, such as behind the knee, and in folds the pose creates.
- **Fold Tightness** and **Fold Smoothing**: which curvature counts in full, and how widely a fold is spread.
- **Minimum Density** and **Maximum Density**: the fabric never gets sheerer or more opaque than these, however stretched or folded.

## Presets

Built-in presets get you started; save your own from the row's alt-actions. Settings are saved with the model.

---

## Related pages

- [Body Paint and Spray](paint_and_spray)
- [DanceXR Native](native)
