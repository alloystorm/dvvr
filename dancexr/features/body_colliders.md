---
layout: feature
title: "Body Colliders"
locale: en-US
---

# Body Colliders

Creates capsule and sphere collision shapes around the
actor's body for physics interaction — used by cloth, hair,
and other dynamic parts to bounce off the body instead of
clipping through.


## Global Size

**Size** is a master multiplier applied to all collider
radii. Adjust this first to match the model's overall scale
before fine-tuning individual regions.


## Body Regions

Individual sliders scale specific areas relative to the
global size: **Head Radius**, **Arm Radius**, **Forearms**,
**Chest Width**, **Waist Width**, **Hips Width**, **Leg
Radius**, **Butts Radius**, and **Belly Radius**. Values
above 1 enlarge the collider; below 1 shrinks it.

**Butts Position** and **Belly Position** shift those
colliders in 3D space to match the model's proportions.
**Thigh Fwd/Back** adjusts thigh collider placement;
**Thigh Start Position** controls where along the leg chain
colliders begin.


## Visualization

In wireframe physics mode, **Visualize** renders the
collider shapes as translucent gizmos for debugging.

