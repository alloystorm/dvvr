---
layout: release
title: Idle Motion
locale: en-US
toc: true
---

# Idle Motion

<!-- TODO: confirm UI labels. Drafted from release notes (2025.12) and the procedural-motion family. -->

Idle Motion is a procedural motion that plays when an actor has no other motion assigned. It simulates breathing, weight shifting, and small head and limb movements so the actor looks alive in the standing pose rather than frozen.

---

## When idle motion plays

- Before any motion is assigned to the actor.
- When a motion ends (and the actor is not part of a sequence).
- During pauses in a sequence.

If an explicit motion is playing, idle motion does not run. To layer subtle micro-movements on top of an active motion, see [Lifelike Motions](lifelike_motions) instead.

---

## Settings

<!-- TODO: confirm exact slider names and ranges. -->

- **Intensity** — overall amplitude of the idle movement.
- **Speed** — how quickly the breathing / weight-shift cycle runs.
- **Body sway, head movement** — per-region multipliers.

---

## New idle motion (v2025.12)

DanceXR 2025.12 introduced a more natural idle motion driven by the new procedural motion control system. The new version produces smoother, less repetitive idle animation than earlier builds. More improvements to procedural motion control are planned for future releases.

---

## Related pages

- [Lifelike Motions](lifelike_motions) — subtle micro-movements on top of any motion
- [Catwalk Motion](catwalk)
- [Auto Dance 3](autodance3)
- [Blink, Breathing & Eye Contact](eyecontact)
- [Motion Settings](motion_settings)
