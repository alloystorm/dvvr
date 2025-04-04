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
|<nobr>![videocam icon](/images/icon/ic_videocam.png) Assign To Main</nobr>|| 
|<nobr>![chevron icon](/images/icon/ic_chevron.png) Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>![chevron icon](/images/icon/ic_chevron.png) Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>![slider icon](/images/icon/ic_slider.png) Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>![slider icon](/images/icon/ic_slider.png) FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) Distance Near</nobr>| [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
|<nobr>![slider icon](/images/icon/ic_slider.png) Distance Far</nobr>| [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
|<nobr>![check_on icon](/images/icon/ic_check_on.png) Use Actor Orientation</nobr>| [ON] | Enable or disable alignment of the camera to the actor's orientation.
|<nobr>![slider icon](/images/icon/ic_slider.png) Seed</nobr>| [1234] (Unlimited) | Seed value for generating random camera motions.
|<nobr>![slider icon](/images/icon/ic_slider.png) Fade To Black</nobr>| [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
|<nobr>![slider icon](/images/icon/ic_slider.png) F2B Probability</nobr>| [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|<nobr>![check_off icon](/images/icon/ic_check_off.png) Audio Sensitivity</nobr>| [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
|<nobr> <b>Target Selection</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) Head</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's head.
|<nobr>![slider icon](/images/icon/ic_slider.png) Chest</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's chest.
|<nobr>![slider icon](/images/icon/ic_slider.png) Center</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's center.
|<nobr>![slider icon](/images/icon/ic_slider.png) Legs</nobr>| [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
|<nobr>![slider icon](/images/icon/ic_slider.png) Feet</nobr>| [0] (0 ~ 1) | Probability of targeting the actor's feet.
|<nobr> <b>Distance Selection</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) Close Up</nobr>| [1] (0 ~ 1) | Probability of a close-up camera distance.
|<nobr>![slider icon](/images/icon/ic_slider.png) Zoom In</nobr>| [0.25] (0 ~ 1) | Probability of zooming in.
|<nobr>![slider icon](/images/icon/ic_slider.png) Zoom Out</nobr>| [0.25] (0 ~ 1) | Probability of zooming out.
|<nobr>![slider icon](/images/icon/ic_slider.png) Middle</nobr>| [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
|<nobr>![slider icon](/images/icon/ic_slider.png) Far</nobr>| [0.25] (0 ~ 1) | Probability of a far camera distance.
|<nobr> <b>Path Selection</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) High Angle</nobr>| [20] (0 ~ 30) | Maximum upward angle for the camera.
|<nobr>![slider icon](/images/icon/ic_slider.png) Low Angle</nobr>| [-20] (-30 ~ 0) | Maximum downward angle for the camera.
|<nobr> <b>Orientation</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) Front Center</nobr>| [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
|<nobr>![slider icon](/images/icon/ic_slider.png) Front 45</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
|<nobr>![slider icon](/images/icon/ic_slider.png) Side 90</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
|<nobr>![slider icon](/images/icon/ic_slider.png) Back 135</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
|<nobr>![slider icon](/images/icon/ic_slider.png) Back 180</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1,  |
