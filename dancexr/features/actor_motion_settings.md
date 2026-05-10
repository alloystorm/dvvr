---
layout: release
title: Actor Motion Settings
locale: en-US
toc: true
---

# Actor Motion Settings

<!-- TODO: confirm exact UI labels. Drafted from release notes (2024.5, 2024.7, 2025.8, 2026.2) and from the per-actor menu structure. -->

Actor Motion Settings customize how a specific actor plays a motion. These are **per-actor** overrides — they take precedence over the dance-set-level [Motion Settings](motion_settings) and the global [Playback Options](playback_options).

Use them when one actor in a multi-actor scene needs different behavior from the others — for example, a slower playback speed, no IK, or a different pose-transition style.

---

## Common settings

- **Playback speed** — per-actor multiplier on top of the motion's nominal speed.
- **Loop / sequence** — per-actor override of how the motion advances.
- **Standard pose transition** — when switching motion or scrubbing the timeline, transition through the standard pose first so physics can settle (added in 2024.5).

---

## IK and inheritance toggles

Added in **2025.8** to support complex PMX models with custom inheritance and IK setups. You can toggle each independently:

- **Motion IK** — let the motion's authored IK targets drive the rig.
- **Model IK** — use the IK constraints baked into the model file.
- **Inheritance** — apply PMX inherit-bone relationships during playback.

Disable individual toggles when a model fights itself (twisted limbs, broken hands, locked feet).

---

## Twist and arm corrections

- **Twist correction** — reduces unnatural twist on shoulder / arm bones.
- **Arm twist correction** — added in 2024.7. Keeps arms straight when twist bones are animated incorrectly.
- See [Troubleshooting](troubleshooting) for the full list of per-actor corrections (Apply Body Rotation To Center, Hand Scale, Limit Neck/Head Rotation, etc.).

---

## Smoothing

The advanced motion smoothing introduced in **2026.2** can be tuned per actor — including per-joint smoothing parameters. The default is on; turn it off if a motion feels muted or laggy.

---

## Related pages

- [Motion Settings](motion_settings) — dance-set-level defaults
- [Playback Options](playback_options) — scene-wide defaults
- [Assigning Motion](assign_motion)
- [Motion Override](motion_override)
- [Troubleshooting](troubleshooting)
