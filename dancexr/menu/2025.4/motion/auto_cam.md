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



[Feature Page](/dancexr/features/auto_cam.md)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> Assign To Main</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> FOV</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Near</nobr>| [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance Far</nobr>| [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Orientation</nobr>| [ON] | Enable or disable alignment of the camera to the actor's orientation.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Seed</nobr>| [1234] (Unlimited) | Seed value for generating random camera motions.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Fade To Black</nobr>| [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B Probability</nobr>| [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Audio Sensitivity</nobr>| [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
|<nobr> <b>Target Selection</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Head</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's head.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Chest</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's chest.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Center</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's center.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Legs</nobr>| [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Feet</nobr>| [0] (0 ~ 1) | Probability of targeting the actor's feet.
|<nobr> <b>Distance Selection</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Close Up</nobr>| [1] (0 ~ 1) | Probability of a close-up camera distance.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Zoom In</nobr>| [0.25] (0 ~ 1) | Probability of zooming in.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Zoom Out</nobr>| [0.25] (0 ~ 1) | Probability of zooming out.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Middle</nobr>| [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Far</nobr>| [0.25] (0 ~ 1) | Probability of a far camera distance.
|<nobr> <b>Path Selection</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> High Angle</nobr>| [20] (0 ~ 30) | Maximum upward angle for the camera.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Low Angle</nobr>| [-20] (-30 ~ 0) | Maximum downward angle for the camera.
|<nobr> <b>Orientation</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Front Center</nobr>| [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Front 45</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Side 90</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Back 135</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Back 180</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1,  |
