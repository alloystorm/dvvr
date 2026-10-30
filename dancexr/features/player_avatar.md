---
layout: feature
title: Player Avatar
locale: en-US
toc: true
---

# Player Avatar

The **Player Avatar** gives you a body in the scene. On the desktop you see it from a third-person over-the-shoulder view; in VR it is the body under your headset and controllers. Characters can look at it, and their hair, clothing, and soft bodies are pushed by it. It is a **Pro** feature in every edition.

Switch it on with **Camera > Player Avatar**.

---

## Choose a body

**Body** picks what you wear:

- **Dummy (male, upper body)**, the default.
- **Actor model**: any model you pick. Choose the selected actor, the built-in Dummy, or a model from your library, including one inside a zip pack. Recent and favorite models are kept in the picker.

**Avatar Scale** and **Fit to My Height** match the body to you.

## Standing and sitting

**Standing Pose** and **Seated Pose** are separate for desktop and VR.

- Standing: **Lean Forward**, **Lean Sideways**, **Weight Shift**, **Stance Width**, **Toe Out**, and **Arms** (where they rest). Switch on **Walk** and the avatar steps as you move.
- Seated: **Legs** (how they sit, with **Right Leg on Top** for crossed legs and ankles), **Arms**, and a **Chair** to sit on: a swivel chair that turns with you and rolls along when you move away. If the seat is too high for the floor, the legs hang.

## Over the shoulder (desktop)

The desktop view rides a boom behind and above the avatar's shoulder. In **Over the Shoulder**:

- **Distance**, **Shoulder Offset**, and **Height** place the camera.
- **Standing Height**: *Snap* stands the avatar up straight while the camera is near its standing height (within **Snap Range**) and crouches or rises beyond that, *Fixed* always stands it straight with its feet on the floor, and *Free* follows the camera exactly.
- **Look at Actors**: the avatar turns its head and eyes to the nearest actor in front of it.

Drag to turn the view around the avatar, drag with the right button to turn the avatar, and use the movement keys to walk it. The view needs the Free-fly camera without tracking.

## Seeing your own body

**Head Clearance** stands the body slightly behind you so its head stays out of your view without being hidden; it still appears in mirrors, reflections, and shadows. With **Camera Fade** on, the body is not drawn closer than **Clear Within** and fades back in out to **Fade Out To**, so you can look down without a head in the way.

## Hands

- On the desktop, use the [Pose tool](pose_tool) to drag the avatar's arms. A hand stays where you leave it and walks and turns with the body. **Lower Avatar Hands** in the Pose menu releases them.
- In VR, the controllers place the hands. **VR Fingers** curls the fingers with the trigger and grip, or follows tracked fingers on headsets that have hand tracking.

## Physics and contact

Hair, cloth, soft bodies, and PMX physics bodies are pushed by your avatar's body and hands. Switches in **System > Physics** control it:

- **Collide with Player** (on by default).
- **Collide with Other Actors** (off by default): every actor's body collides with every other actor's.

---

## Related pages

- [Pose Tool](pose_tool)
- [DanceXR Native](native)
