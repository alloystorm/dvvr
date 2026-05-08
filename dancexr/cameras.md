---
layout: release
title: Cinematic Cameras
locale: en-US
toc: true
---

# Cinematic Cameras

DanceXR has six camera modes plus a shared settings page. They are not interchangeable — each is tuned for a different use. This page picks the right one for the job and points you at the detail page once you know.

For shared parameters (FOV, near / far clip, depth of field), see [Camera settings](/dancexr/features/camera_settings).

---

## Mode comparison

| Mode | Best for | Driven by | Page |
|---|---|---|---|
| Freefly | Hands-on free roaming, line-up shots | You (mouse / gamepad / VR) | [Freefly camera](/dancexr/features/freefly_cam) |
| Auto | Cinematic music videos, hands-off recording | Music beats + actor positions | [Auto camera](/dancexr/features/auto_cam) |
| Orbit | Turntable shots, model showcases | You (orbit input) around a target | [Orbit camera](/dancexr/features/orbit_cam) |
| One-shot (Long take) | A single uncut sweep through a scene | Pre-set path, runs once | [One-shot camera](/dancexr/features/one_shot_cam) |
| Concert (Fixed) | Concert / stage angle, single static framing | Pinned position; never moves | [Concert camera](/dancexr/features/concert_cam) |
| First Person | POV experience; the actor's view | <!-- TODO: confirm — actor head bone? --> | [Camera settings](/dancexr/features/camera_settings) <!-- TODO: separate page if/when one is added --> |

---

## When to pick which

**Freefly camera.** Default for desktop. You move the camera with WASD + mouse (or thumbstick + look). Use it whenever you want manual control — composing screenshots, moving through a scene, posing a shot before recording.

**Auto camera.** Hands-off cinematic. Picks targets (head, chest, center, legs), distances (close-up to far), and angles probabilistically, with optional fade-to-black cuts. Reads [music timing](/dancexr/features/music_timing) and music volume to sync transitions and pace. Best when you want a finished-looking music video without directing every shot. Re-roll the [seed](/dancexr/features/auto_cam#random-seed) until you like the take.

**Orbit camera.** Stays a fixed distance from a target and orbits around it. Use it for a model turntable, a slow showcase loop, or a controlled rotation around a posed actor.

**One-shot camera.** A single take that runs through a defined path or sequence and ends. Use it for an opener, an outro, or an uncut sweep where you want exactly one camera move.

**Concert camera (fixed).** The camera does not move. Useful for stage-position or audience-position framing where you want a stable angle for the duration of a song.

**First Person camera.** POV — the camera sees what the actor sees. <!-- TODO: confirm exact behavior. -->

---

## Recording considerations

The mode you pick affects what offline rendering captures:

- **Auto camera + Creator edition** is the most common combo for finished music videos. Auto Cam handles framing; Creator records frame-by-frame so you do not lose shots to FPS dips. See [Creator edition](/dancexr/creator).
- **Freefly + screen capture** is fine for shorter clips when real-time FPS is good.
- **One-shot** is the cleanest match for VR 180 / VR 360 recording — one camera path, one take, no cuts.
- **Concert** is your friend for static-angle reference shots, comparison videos, or anything that needs perfect repeatability across takes.
- **Orbit** records cleanly because the path is deterministic — useful for showcase reels.

The recording flow itself is the same regardless of mode; see [Creator edition → Recording menu](/dancexr/creator#recording-menu).

---

## VR considerations

In VR, the **headset** is effectively the camera. You can still use the cinematic camera modes for the desktop mirror window or for offline render output:

- The headset always shows the world in stereo VR.
- The cinematic camera applies to the mirror window and to recordings.
- **Block Desktop Window** in [VR settings → UI](/dancexr/features/vr_settings#ui) stops mirror rendering when you do not need it, freeing GPU.

For VR recording (3D SBS, VR 180), use Creator's recording mode regardless of which cinematic camera is active — see [Creator edition → Recording modes](/dancexr/creator#recording-modes).
