---
layout: feature
title: "Motion Settings"
locale: en-US
---

# Motion Settings

Controls how motion data (VMD, BVH, etc.) is applied to an actor
model, including scaling, timing offsets, IK handling, and pose
corrections.


## Motion Parameters

**Motion Scale** multiplies all positional movement from the motion
file — useful when animations are exaggerated or too subtle for the
model's proportions. **Vertical Pos Scale** independently scales the
center bone's up/down movement to reduce bouncing or hopping.

**Mirror** flips left and right motion data, primarily for VMD files
authored for opposite-side dominance. **Time Offset Percent** and
**Time Offset Seconds** shift when in the animation timeline the
actor starts playing — useful for syncing multiple actors or
compensating for motion lead-in.

**Leg Angle** adds a small rotation bias to leg bones, adjusting
stance width or toe-out angle across the entire animation.


## IK Settings

**Inherit Bones** respects the inherit-parent constraints defined in
the PMX file (e.g. hand bones following arm bones). **Motion Leg IK**
applies a generic two-bone leg IK pass during motion processing,
allowing foot planting to work even on models without dedicated IK
bones. **Model IK** uses the IK link chains defined in the PMX itself.
When Model IK conflicts with Motion IK, try disabling one or the other.


## Spectator

Marks the actor as a spectator — they are excluded from formation
patterns and lighting assignments, useful for audience members or
background characters.


## Pose Adjustment

Rotates the default T-pose bone angles before any motion is applied.
See the nested panel for per-bone-group rotation controls — this is
the primary way to fix models whose imported rest pose doesn't match
the animation's assumptions.


## Visualization

**Show Virtual Bones**, **Visualize Bones**, and **Visualize IK
Targets** render debug gizmos for the skeleton hierarchy and IK
target positions (PMX models only).


# Sub-Components

## sd_pose

Adjusts the default (zero-pose) rotation for every major bone group
on the actor. Values rotate the bone away from its imported T-pose
so you can fix models that stand with arms too wide, legs too close,
or fingers splayed incorrectly.

Each setting is a 3-axis rotation (X/Y/Z) in degrees. Left-side
bones are mirrored to the right side automatically. **Ring Finger**
and **Middle Finger** are scalar multipliers relative to Pinky and
Index respectively, keeping finger curls proportional.

