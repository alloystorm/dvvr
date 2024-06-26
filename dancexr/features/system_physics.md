---
locale: en-US
layout: single
title: System Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/system_physics) | [繁中](/tw/dancexr/features/system_physics) | [日本語](/jp/dancexr/features/system_physics) | [한국어](/kr/dancexr/features/system_physics) | [简中](/zh/dancexr/features/system_physics)


## System-wide physics settings

These are configurations for system-wide physics simulation. You can enable or disable physics simulation, adjust gravity, time scale, and other settings.

## Settings

- Enabled: Turn physics simulation on and off
- Engine: Select the physics engine to use. Currently, only the Physx engine is available.
- Gravity: Change gravity force. Setting it to negative will reverse the gravity direction.
- Time Scale: Change the time scale of physics simulation, creating slow motion or fast forward effect without affecting animation.
- Disable Collision: Disable collision between stationary and dynamic colliders.
- Subframe Motion: Enable subframe motion for smoother simulation.
- Steps per second: Number of physics simulation steps per second.

## Physics Frame Rate and Subframe Motion <a id="subframe"></a>

For the best result, physics simulation is calculated at a fixed interval, which means there can be multiple simulation steps per frame and the actual number of steps performed each frame can be different depending on the stability of your frame rate.

You can choose your desired physics frame rate by setting the "Steps per second" option. But do keep in mind that physics simulation takes CPU resources and setting it too high can slow down your frame rate, resulting in a worse experience. So it's best to find a sweet spot that doesn't hurt your frame rate too much while providing smooth simulation.

Subframe motion is a new feature that updates motion at the selected physics frame rate. This can reduce the amount of movement of each physics simulation step, resulting in smoother simulation and more stability. This is especially useful for fast-moving objects or when you want to achieve more realistic motion. However, this will also require more CPU resources, so only use it when you have CPU headroom to spare.

The following image shows the difference between subframe motion and normal motion.

![Subframe Demo](/images/subframe640.png)

Imagine an object with a chain attached to it moving from left to right. Without subframe motion, the physics simulation has a much greater gap to fill in the next frame, while with subframe motion, the gaps are much smaller, resulting in smoother motion.