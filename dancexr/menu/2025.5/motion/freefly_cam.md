---
locale: en-rUS
layout: single
title: [Freefly Cam]
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/motion/freefly_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/freefly_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/freefly_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/freefly_cam) | [简中](/zh/dancexr/menu/2025.5/motion/freefly_cam)

[Procedural](../menu#Procedural) > [Freefly Cam]

Provides a free-fly camera mode where the user has full control over camera movement and rotation. The camera can move forward, backward, up, down, and rotate or tilt based on user input. Additional options include orbit movement and vertical movement restriction.

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> Assign To Main || 
| > Target Select | **Selected** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| > Tracking Mode | **Center** | Center, Head, Chest,  |
| ⊖ Target Smoothing | [0.5] (0 ~ 2) | 
| ⊖ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| ☐ Lock On Target | [OFF] | Automatically focus on target
| ☐ Camera Shake | [0.5] (0 ~ 1) | 
| ☐ Lock Rotation | [OFF] | Camera follows the rotation of the target
| ⊖ Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
| ⊖ Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
| ⊖ FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
| ⊖ Vertical Offset | [0] (-1 ~ 1) | Offset vertically
| ⊖ FOV | [30] (5 ~ 120) | 
| ⊖ Beat Cycle | [8] (1 ~ 16) | 
| ☐ Use Orbit Move | [OFF] | Enable or disable orbit movement, allowing the camera to rotate around a central point.
| ≡ Presets | **Freefly** | Freefly, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |
