---
layout: feature
title: "./motion/proc/free_pose"
locale: en-US
---

# ./motion/proc/free_pose

Free Pose turns the actor into a self-balancing puppet you pose
by hand. Nothing is animating — the balance solver owns the whole
pose. Grab any limb, the torso, or the head and drag it; the
solver keeps the character balanced over its feet while standing,
or over a locked seat while sitting. Pins are remembered, so a
released limb stays where you leave it.


## Posing & Pinning

Drag a hand/arm or foot/leg to move that limb; the grab rides the
pointer ray at a fixed depth, so moving the camera (or scrolling)
sweeps it nearer and farther. The target is clamped to the limb's
natural reach, so it can't collapse into the joint or lock dead
straight. Hands stay put where you release them. Feet use
*dwell-to-pin*: hold the drag still until the marker tints green to
lock the foot in the air, or release while it is still red to let
the leg drop and settle to the floor. The **Reset** action drops
every pin and returns the actor to a neutral stand.


## Weight Shift & Sway

**Shift Smoothing** is the time the body takes to transfer weight
from one foot to the other — larger feels slower and heavier.
**Sway Amplitude** adds a small idle quiet-stance drift so a
standing pose doesn't look frozen; set it to *0* for a dead-still
hold.


## Support & Solver

**Support Radius** is a slack disk around the weighted stance: COM
excursion inside it counts as balanced and draws no hip correction,
so a larger radius gives a looser, lazier-looking balance.
**Solve Iterations** is how many passes the pose solver runs each
frame — raise it for tighter limbs at a small cost, lower it to
save time.


## Leg Springs

The body is a single mass at the pelvis, held up by each grounded
leg acting as a spring; the knee bend, the catch on landing, and
the standing wobble all emerge from these. **Sim Gravity** is the
downward pull that compresses the legs. **Leg Stiffness** sets how
firmly a leg resists that compression (softer legs sink into a
deeper crouch), and **Leg Damping** is the landing give that keeps
a planted foot from bouncing.


## Stance Control

**Stance Stiffness** and **Stance Damping** are the horizontal
controller that holds the pelvis over the base of support —
stiffer reacts faster but can feel rigid, more damping keeps quiet
stance from jittering. **Relax Rate** is how quickly a released leg
eases back toward its resting pose.


## Sitting

Drag the torso (waist) and hold still to lock it as a seat: the
body then rests on it like a stool, and both feet are free to lift
and dangle without bearing weight. A quick drag-and-release of the
torso, or **Reset**, stands back up. Because a seated pelvis can't
slide to chase balance the way a standing one does, balance is kept
by *tilting the upper body* opposite the legs. **Seat Radius** is
the support disk around the seat inside which no tilt is applied.
**Seat Lean Gain** sets how hard the upper body leans to counter a
leg that's been moved, and **Seat Lean Max** caps that angle — turn
the gain up for a stronger, more visible counterbalance, down if it
overshoots. **Seat Stiffness** and **Seat Damping** tune the spring
that settles the pelvis onto the seat after you release the drag.

