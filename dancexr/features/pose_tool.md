---
layout: feature
title: Pose Tool
locale: en-US
toc: true
---

# Pose Tool

The **Pose tool** lets you grab a hand, foot, or the body of any actor in DanceXR Native and move it, **over any motion that is playing**. The first drag detaches that actor from its dance at the pose it is in, and the other actors keep dancing. A balance solver keeps the posed character standing, shifting its weight, or sitting as you pull, so you are posing a body with weight rather than moving a gizmo.

The Pose tool is free in every edition. It works on XPS, PMX, FBX, and VRM models, and in VR.

---

## Start posing

1. Open the **Pointer Tool** menu from the tool button on the bar, or right-click empty space, and choose **Pose**. **Next Tool** is also a button you can bind to cycle through the tools.
2. Drag a limb, the chest or head, or the hips of any actor.

Until you touch a leg or the hips, the actor holds the pose it was detached in exactly. The Pose menu header shows how many actors are posed.

## Pulling, pinning, and sitting

- **Hands** stay where you leave them.
- **Feet** lock in the air if you hold still until the marker turns green; a green ring with a cross shows what is pinned. Let go early and the leg is released and stands.
- **Hips**: drag the hips and hold still to sit. A quick drag and release stands up.
- **Reach**: the mouse wheel changes how far the held limb reaches. **Alt+wheel** rolls a held hand about its forearm.
- A posed actor keeps responding, and its hair keeps moving, even while the scene is paused.

In VR, point with a controller to grab, and use the stick for reach and tilt.

## Pose menu

| Item | What it does |
|---|---|
| **Scene Paused** | Holds every actor and the music still so you can pick the moment. |
| **Freeze All** | Detaches every actor at the pose it is in, ready to be posed. |
| **Unpin and Stand** | Lets go of every pinned foot and the hip seat, so the legs stand straight under the hips. |
| **Undo Edits** | Puts every posed actor back to the pose it was detached at; it stays held. |
| **Resume All** | Blends every posed actor back into its motion at the current time. |
| **Lower Avatar Hands** | Releases your [player avatar's](player_avatar) hands. |

### Balance

The **Balance** submenu tunes how the body behaves while posed:

- **Shift Smoothing**: how long the body takes to move its weight from one foot to the other.
- **Sway**: a small quiet-stance drift so a standing pose does not look frozen. Zero is dead still.
- **Gravity**, **Leg Stiffness**, and **Leg Damping**: how the legs bend and settle under the body.
- **Stance Stiffness**: how quickly the hips follow the base of support.
- **Relax Rate**: how quickly a released foot eases down to the floor.

## Good to know

- A held pose lasts for the session. It is not saved with the scene.
- With the **Pose tool** selected, you can also drag your player avatar's arms on the desktop. The hand stays where you leave it and walks and turns with the avatar.

---

## Related pages

- [Player Avatar](player_avatar)
- [DanceXR Native](native)
- [Interactive Pose](interactive_pose) in the DanceXR Unity apps
