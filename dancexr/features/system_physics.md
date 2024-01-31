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
You can locate the system-wide physics settings in Settings -> Options -> Physics. 

![System Physics](/images/system-physics.png)

Enabled
: Turn physics simulation on and off

Gravity
:  Change gravity force. Set it to negative will reverse the gravity direction. 

Disable Collision
:  Controls collision between model parts. There are 2 types of colliders in a model, type A are the ones that move with animation, like arms and legs, type B are the ones that move freely, usually they are connected to other parts by one or more joints. By default type B will collide with type A but if you turn "Disable Collision" on, then type B objects will no longer collide with type A objects and will penetrate through. 

Steps per second
:  Physics simulation are calculated with a certain interval between steps, and it works best if it is a fixed interval. This option controls how many simulation is performed within a second. The more the better but too many steps will slow down your FPS. It's best to match it with your FPS for smooth animation.
