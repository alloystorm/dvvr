---
locale: en-US
layout: single
title: Sex Motion 3
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/sm3_motion) | [繁中](/tw/dancexr/features/sm3_motion) | [日本語](/jp/dancexr/features/sm3_motion) | [한국어](/kr/dancexr/features/sm3_motion) | [简中](/zh/dancexr/features/sm3_motion)


## Overview
This is the latest procedural NSFW motion that features highly customizable motion and the ability to be used on top of another motion to creat a mix of dance and sex motion.

## Female Pose
This shows up when you assign the motion to the actor and set their role as "Female". Configure position and rotation offset, hands and legs pose of the female actor assigned to the motion.

### Body
* Position X, Y, Z: Position offset
* Rotation X, Y, Z: Rotation
* Bend X, Y: Bend angles of the torso in both forward / back and left / right directions

When you have both male and female actors assigned to the motion, you might notice that when changing female actor position the male will follow. This is by design. If you want to change the relative position between the 2 actors, changes the body control for the male actor.

### Hands
Controls hands positions and poses. It can be toggled off when used of "Motion 2" to allow the original motion in "Motion 1" to be unchanged.

### Legs
Controls legs and feet positions and poses. Similar to hands control that this can be toggled off to preserve the motion from "Motion 1".


## Motion Control
The majority of the motion is on the female actor so the motion control is configured from the female actor.

Auto mode switch the motion pattern randomly within the built-in patterns.

Auto Preset mode will switch between your saved presets.

Manual mode allows you to create your own motion pattern by adjusting movements for each axis individually.

In Manual mode you can also use the "Override" value and "Auto Update" to control the motion with your controller input. Just turn on override and enable Auto Update and set it in the "Axis Input" mode.

### Sex motion
The sex motion cycle between these steps: 

Push -> Collide -> Bounce -> Return

You can adjust the following values to fine tune the motion:
* Distance: The distance it travels during push
* Overshoot: The distance it travels after collision
* Movement Allocation: The allocation of movements between male and female actors
* Bounce: How much male and female bounce away from each other in the bounce period
* Collision Allocation: Allocation between male and female for the bounce movement

It's hard to describe this in words, just have a play with those settings and you'll see what they do.


## Male Pose
This shows up when you assign the motion and set role to "Male". You can also change body, hands and legs control for male actor similar to the female part. 

### Penis Control
You can adjust how much it can curve.

