---
layout: feature
title: "Ragdoll"
locale: en-US
---

# Ragdoll

Replaces the actor's animated skeleton with a particle-based
ragdoll physics simulation. The body goes limp and reacts to
gravity and external forces.

**Spring Force** and **Damping** (both logarithmic) control
how aggressively the ragdoll tries to return to its animated
pose — low values make it floppy, high values keep it closer
to the animation. **Gravity** toggles gravitational pull on
the ragdoll.

**Lock Left/Right Foot**, **Lock Head**, and **Lock Left/Right
Hand** pin specific body parts to their animated positions so
they don't flop — useful for keeping feet planted while the
rest of the body goes limp.

**Fine Tune** sets per-bone force scales from 0 (fully floppy)
to 1 (fully rigid). Adjust individual body parts like legs,
knees, arms, shoulders, torso, neck, and head to create
localized stiffness — e.g. keep the torso firm while letting
limbs dangle.

