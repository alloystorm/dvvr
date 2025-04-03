---
locale: en-rUS
layout: single
title: [Auto Cam]
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[Procedural](../menu#Procedural) > [Auto Cam]



| Setting | Value | Description |
| :--- | --- | :--- |
| Assign To Main || 
| Target Select: Auto || 
| Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| Tracking Mode: Center || 
| Tracking Mode | **Center** | Center, Head, Chest,  |
| Target Smoothing | [0.5] (0 ~ 2) | 
| Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| FOV | [30] (5 ~ 120) | 
| Beat Cycle | [8] (1 ~ 16) | 
| Distance Near | [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
| Distance Far | [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
| Use Actor Orientation | ON | Enable or disable alignment of the camera to the actor's orientation.
| Seed | [1234] (Unlimited) | Seed value for generating random camera motions.
| Fade To Black | [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
| F2B Probability | [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
| Audio Sensitivity | [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
| Target Selection || 
| Head | [1] (0 ~ 1) | Probability of targeting the actor's head.
| Chest | [1] (0 ~ 1) | Probability of targeting the actor's chest.
| Center | [1] (0 ~ 1) | Probability of targeting the actor's center.
| Legs | [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
| Feet | [0] (0 ~ 1) | Probability of targeting the actor's feet.
| Distance Selection || 
| Close Up | [1] (0 ~ 1) | Probability of a close-up camera distance.
| Zoom In | [0.25] (0 ~ 1) | Probability of zooming in.
| Zoom Out | [0.25] (0 ~ 1) | Probability of zooming out.
| Middle | [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
| Far | [0.25] (0 ~ 1) | Probability of a far camera distance.
| Path Selection || 
| High Angle | [20] (0 ~ 30) | Maximum upward angle for the camera.
| Low Angle | [-20] (-30 ~ 0) | Maximum downward angle for the camera.
| Orientation || 
| Front Center | [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
| Front 45 | [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
| Side 90 | [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
| Back 135 | [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
| Back 180 | [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
| Presets: Default (Reset) || 
| Presets | **Default (Reset)** | Default (Reset), Preset 1,  |
