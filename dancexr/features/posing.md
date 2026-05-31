---
layout: feature
title: "Interactive Posing"
locale: en-US
---

# Interactive Posing

Shape a character's pose directly by grabbing and dragging points on the body. Instead of editing bone values one at a time, you reach for a hand or a foot and move it where you want it, while a rebuilt full-body balance system keeps the character settled and natural underneath your edits.

Introduced in [2026.6](../releases/2026.6) as the **Free Pose** motion. It is an early, experimental feature — select it from the procedural motion list to switch the character into balance-driven posing.


## Drag to pose

With Free Pose active, you can grab a point on the body and drag to move that part directly. The draggable parts are:

- **Left and right hands** — reach the arms out and place the hands in 3D.
- **Left and right feet** — step, lift, and plant the legs.
- **Upper body** — grab the torso or head to lean and turn the upper body as one.

A marker shows the point you are moving, and the pose updates live as you drag, so you can rough in a stance quickly and then refine.

Depth is handled by the drag itself: the grab locks to a fixed distance along your aim ray, so moving the camera (or your VR hand) sweeps the point toward and away from you, and you can fine-tune that distance with the scroll wheel. This lets you position limbs in full 3D rather than only along the screen plane.


## Foot pinning (dwell to pin)

By default a foot you let go of will **drop to the ground** — the balance system lets it descend and take weight naturally. If you want a foot to stay exactly where you placed it, hold it still for a moment before releasing: while you dwell, the marker tints from red toward green to show the pin is arming. Release once it has turned green and the foot stays planted; release early, or keep moving, and it drops instead.

Hands behave differently — a hand stays where you release it, so you can leave an arm posed without dwelling. The upper body also keeps the lean and orientation you gave it after you let go.

To reset everything, use the **Reset** action in the Free Pose settings: it drops all pins and settles the character back to a neutral standing pose.


## Full-body balance

Underneath the dragging, a rebuilt balance solver keeps the character standing believably. Rather than holding a rigid shape, it tracks the center of mass over the supporting foot, shifts weight between the legs, bends the hips and knees to support the pose, and adds a small ongoing sway so a held pose never looks frozen.

The balance behavior is tunable in the Free Pose settings, including:

- **Sway Amplitude** — how much idle sway the character shows.
- **Support Radius** — how far the body can drift before the hips correct.
- **Leg and Stance Stiffness / Damping** — how springy or heavy the legs feel as weight shifts.
- **Shift Smoothing** and **Sim Gravity** — the pace and weightiness of weight transfer.


## VR hand control

Posing works in the headset too. You can point at a handle and drag it with the controller ray just like with a mouse, or reach out and physically grab a hand or foot — gripping a controller over the body tracks your hand position directly, so you can move a limb through real space and shape the pose by hand.
