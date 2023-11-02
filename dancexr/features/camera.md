---
layout: single
title: Camera
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/camera) | [繁中](/tw/dancexr/features/camera) | [日本語](/jp/dancexr/features/camera) | [한국어](/kr/dancexr/features/camera) | [简中](/zh/dancexr/features/camera)


## Overview
We have 5 procedural camera motions available and you can also use camera motion from loaded dance motions if available.

### Procedural Camera Motions
* Freefly Camera: Familiar WASD control camera that allows you to go anywhere and view from any angle.
* Orbit Camera: Focus is alwasy on an actor or the center of a group of actors. Movement is limited to orbiting and distance change. 
* Auto Camera: The system automatically selects focus target and the camera motion. The movement matches the music beats.
* One-Shot Camera: Similar to Auto Camera but the movement is continuous. 
* Concert Mode Camera: Viewing angle and position are fixed so the stage stays constant.

### Target Select
Most of the procedural cameras provides "Lock On Target" options. These options provides controls on which actor is to be chosen as focus target and the zoom in option.
* Auto
* Selected
* Group
* Rotate
* Rotate + Gropu
* Stage Center

### Lock On Target
Lock On Target option in Freefly camera allows focusing on the current target while having the freedom to move the position of the camera.

### Auto Zoom
Auto Zoom controls field of view to maintain a fixed size for the subject regardless of its distance to the camera. 

## Recent Updates
### 1.4.3
* Auto cameras are updated with smarter view range control. When using auto or group mode, the cameras can now ensure all the actors on the stage are in the visual range.

{% include video id="csv6_H5_Q7k" provider="youtube" %}

* Added more camera tracking options. 

{% include video id="Gq_eRoZIrO4" provider="youtube" %}