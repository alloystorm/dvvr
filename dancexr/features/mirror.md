---
layout: release
title: Mirror
locale: en-US
toc: true
---

# Mirror

<!-- TODO: confirm exact settings. Drafted from prop docs and release notes (2024.10). -->

A mirror prop reflects the scene from a planar surface — useful for choreography review (the actor can be seen from a second angle) and for stage scenes (reflective walls, dance studios).

Originally split out from the Screen prop in an earlier release. See [Props](props) for general prop placement.

---

## Placement and sizing

Place a mirror like any other [prop](props): position it on the stage, then resize and rotate. Standard placement gizmos apply.

---

## Reflection settings

<!-- TODO: confirm. Likely settings: reflection resolution, reflection clarity / blur, double-sided toggle, near-clip plane for the reflection camera. -->

The mirror renders the scene from the camera position reflected across its plane, so:

- Higher reflection resolution costs frame rate.
- The reflection respects existing lighting and shadows.
- Transparent or alpha-clipped objects in the reflection follow the same rules as the main view.

---

## VR support

From **2024.10**, the mirror works correctly in VR — both eyes get the right parallax so depth in the mirror feels physical instead of flat. This is what makes the mirror feel like a real surface in headset rather than a 2D screen.

---

## Limitations

<!-- TODO: confirm. Likely:
- Only one mirror at a time may be active, or N mirrors with each eating frame rate.
- Recursive reflection (mirror facing mirror) is bounded.
- Available render features inside the reflection (e.g. raytracing, pathtracing). -->

---

## Related pages

- [Props](props)
- [Screen](screen)
- [Primitive Shapes](primitive_shapes)
- [Room Stage](room_stage)
