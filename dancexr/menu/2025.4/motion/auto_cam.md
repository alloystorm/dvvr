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



[Feature Page](/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> Assign To Main|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Target Select| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Tracking Mode| **Center** | Center, Head, Chest,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Smoothing| [0.5] (0 ~ 2) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Prediction| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> FOV| [30] (5 ~ 120) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Beat Cycle| [8] (1 ~ 16) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Near| [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Far| [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Orientation| [ON] | Enable or disable alignment of the camera to the actor's orientation.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Seed| [1234] (Unlimited) | Seed value for generating random camera motions.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Fade To Black| [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B Probability| [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|  □ Audio Sensitivity| [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
|  <b>Target Selection</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Head| [1] (0 ~ 1) | Probability of targeting the actor's head.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Chest| [1] (0 ~ 1) | Probability of targeting the actor's chest.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Center| [1] (0 ~ 1) | Probability of targeting the actor's center.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Legs| [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Feet| [0] (0 ~ 1) | Probability of targeting the actor's feet.
|  <b>Distance Selection</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Close Up| [1] (0 ~ 1) | Probability of a close-up camera distance.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Zoom In| [0.25] (0 ~ 1) | Probability of zooming in.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Zoom Out| [0.25] (0 ~ 1) | Probability of zooming out.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Middle| [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Far| [0.25] (0 ~ 1) | Probability of a far camera distance.
|  <b>Path Selection</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> High Angle| [20] (0 ~ 30) | Maximum upward angle for the camera.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Low Angle| [-20] (-30 ~ 0) | Maximum downward angle for the camera.
|  <b>Orientation</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Front Center| [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Front 45| [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Side 90| [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Back 135| [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Back 180| [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Default (Reset)** | Default (Reset), Preset 1,  |
