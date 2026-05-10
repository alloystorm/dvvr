---
layout: release
title: Catwalk Motion
locale: en-US
toc: true
---

# Catwalk Motion

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

Catwalk Motion is a procedural walking / runway motion. The actor walks toward a target with a fashion-show stride — hip sway, deliberate steps, head held — without needing a VMD walking motion file.

Use it for:

- Posing scenes where the actor enters from off-stage.
- Runway / fashion videos.
- Filling time before another motion starts.

---

## Behavior

- The actor walks forward along the scene Z axis (or toward a target — <!-- TODO: confirm whether target selection is exposed -->).
- Step cadence is procedural; if a music BPM is set ([Music Timing](music_timing)), the steps can sync to the beat.
- The motion loops; the actor walks until you stop it or assign a different motion.

---

## Settings

<!-- TODO: confirm exact slider names. Likely candidates:
- Walk speed
- Stride length
- Hip sway intensity
- Arm swing intensity
- Direction / target -->

---

## Pairing with other motions

Catwalk works well as a **secondary motion** layered under a face / facial-expression track ([Secondary Motion](secondary_motion), [Motion Passes](motion_passes)). Foot-on-floor adjustments from [Feet Adjustment](feet_adjustment) are recommended so the procedural footfalls plant correctly.

---

## Related pages

- [Idle Motion](idle_motion)
- [Auto Dance 3](autodance3)
- [Lifelike Motions](lifelike_motions)
- [Feet Adjustment](feet_adjustment)
- [Music Timing](music_timing)
