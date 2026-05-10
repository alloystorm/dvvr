---
layout: release
title: Dildo
locale: en-US
toc: true
---

# Dildo

<!-- TODO: confirm exact UI labels and configuration. Drafted from related Sex Overlay docs and the prop-attachment system. -->

Configures a dildo prop attached to an actor. Used standalone with a single actor or as the male side of paired motions when no male character is loaded.

---

## Setup

1. Enable the dildo on the relevant actor.
2. Choose attachment bone / position — typically pelvis-anchored.
3. Adjust size and offset.
4. Optional: configure animation behavior (thrust pattern) tied to a [sex motion](sex_motion_3) or to [Auto Update](autoupdate).

The detailed attachment configuration lives in [Sex Overlay & Dildo Config](smo_config).

---

## Settings

<!-- TODO: confirm exact controls. Likely:
- Size / scale
- Position offset
- Rotation
- Curve / bend
- Procedural motion driver (e.g., bound to Sex Motion 3, or driven by Auto Update) -->

---

## Pairing with motions

- With [Sex Motion 3](sex_motion_3) — the dildo can fill the male role in a paired motion. The motion's contact-frame system aligns the dildo to the female contact point.
- With [Auto Update](autoupdate) — drive the thrust pattern from audio level or beats for music-synced motion.

---

## Related pages

- [Sex Overlay & Dildo Config](smo_config)
- [Sex Motion 3](sex_motion_3)
- [Cowgirl Sex Motion](scg_motion)
- [Sex Motion 2](sfb_motion)
- [Auto Update](autoupdate)
