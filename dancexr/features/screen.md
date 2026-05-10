---
layout: release
title: Screen
locale: en-US
toc: true
---

# Screen

<!-- TODO: confirm exact settings. Drafted from release notes (2024.5 LED screen mode, props release notes). -->

Screen is a customizable prop that displays an image, a video, or the view from a scene camera on a flat surface. Use it for stage backgrounds, monitors, projector screens, or as a media surface inside a [room stage](room_stage).

In an earlier release the previous "Screen" prop was split into two: [Mirror](mirror) (reflective) and Screen (display). They share base placement and sizing, but their material and source settings differ.

---

## Source

Choose what the screen displays:

- **Camera** — a scene camera's view (use a second camera in the scene to see the actor on a stage screen).
- **Video** — a video file played via [Video Playback](video_playback). Place the video in the `videos/` folder of your [content library](../preparecontent).
- **Image** — a static texture.

---

## Surface modes

Added across 2024.4 / 2024.5:

- **Standard** — flat material; useful as a TV-style screen with adjustable reflectivity.
- **Emissive** — the screen surface emits light into the scene, no external lighting required.
- **LED screen** — simulates the look of on-stage LED panels, including pixel grid and bloom characteristics. Good for concert stages.
- **Projector** — paired with a light cookie; see [Lighting](lighting).

The actors will make eye contact with the camera attached to a Screen prop set in *Camera* mode (added with the prop split).

---

## Reflection

The screen surface can range from glossy (TV-style reflection of the room) to matte (projector-screen behavior). Adjust roughness in the surface settings.

---

## Visible camera model

When the screen source is a scene camera, a small camera model is rendered at the screen's location. Useful for staging shots in concert mode. Toggle visibility in the screen settings.

---

## Related pages

- [Video Playback](video_playback)
- [Mirror](mirror)
- [Props](props)
- [Room Stage](room_stage)
- [Lighting](lighting)
