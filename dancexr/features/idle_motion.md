---
layout: release
title: Idle Motion
locale: en-US
toc: true
---

# Idle Motion

Idle Motion provides a configurable resting pose with weight shifts and small body movements. Select it as a procedural motion when an actor should stay present without performing a dance. Use [Lifelike Motions](lifelike_motions) for blink, breathing and gaze overlays on another motion.

## Make a resting pose

1. Select **Idle Motion** and open the actor's motion settings.
2. Start with **Stand**, **Sit** or **On Floor**. These presets also change hand poses and stance, so inspect the result on your model.
3. Adjust the hand poses, **Lift** and **Hip Bend** to settle the body at the intended height and bend.
4. Enable **Shifting** for changes of weight. **Shift Interval** controls the interval; **Random** varies that shifting behavior.
5. Compare **Micro Twist** and **Head Turn** on and off to decide how much background movement the shot needs.

For a still pose, disable the movement toggles rather than looking for a single intensity control. To dance instead, assign another motion to the actor. [Free Pose](free_pose) provides direct dragging and foot pinning when you want to place limbs interactively.

## Spectators

Spectator actors expose additional idle controls: **Follow Actor**, **Min Distance**, **Follow Speed**, **Walking** and **Turn To Speaker**. Start with walking and following disabled for a stationary audience member, then enable the behavior you need and check spacing around the other actors. These controls are specific to spectator behavior; they do not set the Catwalk motion's stride.

## Check the model

If the resting pose bends unexpectedly, inspect [Bone Mapper](bone_mapper) and [actor troubleshooting](troubleshooting). If the feet float or sink, check the actor's height and [Feet Adjustment](feet_adjustment) before adding more idle movement.
