---
layout: release
title: Custom Inherit Motion
locale: en-US
toc: true
---

# Custom Inherit Motion

<!-- TODO: confirm exact UI flow. Drafted from PMX inheritance behavior and 2024.8 / 2025.8 release notes. -->

In PMX models, **inherit bones** are bones whose rotation or position is automatically derived from another bone, scaled by an inherit ratio. They are commonly used for:

- Skirt and hair physics helpers.
- Face / cheek bones tied to jaw rotation.
- Twist bones tied to upper-arm rotation for clean shoulder deformation.

Custom Inherit Motion lets you author **your own** inherit relationships — bones inheriting from other bones at user-chosen ratios — so you can create custom secondary motion without modifying the model file.

---

## When to use this

- A model lacks proper twist bones, and arms deform badly.
- You want a hair / accessory bone to follow the head with a damped offset.
- You want to retrofit physics-helper inherit chains onto an XPS / FBX model that has none.

---

## Authoring an inherit relationship

<!-- TODO: confirm exact UI. Drafted from typical setup. -->

1. Open the actor's inheritance settings.
2. Pick a **target bone** (the bone whose rotation will be derived).
3. Pick a **source bone** (the bone to inherit from).
4. Set the **inherit ratio** for rotation, and optionally for translation.
5. Optional: enable / disable specific inherit components (rotation only, position only, both).

The new inherit relationship is applied during motion playback alongside any inherit relationships that came from the PMX file itself.

---

## Compatibility with other systems

- **PMX inheritance toggles** — added in 2025.8, the inheritance behavior of a model can be turned off in [Actor Motion Settings](motion_settings) if a model fights itself. Custom inherit relationships are layered on top of that.
- **Motion override** — combine with [Motion Override](motion_override) to drive specific bones procedurally while using inheritance for everything downstream.

---

## Related pages

- [Bones (reference)](bones)
- [Bone Mapper](bone_mapper)
- [Motion Override](motion_override)
- [Actor Motion Settings](motion_settings)
