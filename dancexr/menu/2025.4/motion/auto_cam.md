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
|<nobr>Assign To Main</nobr>|| 
|<nobr>Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>Distance Near</nobr>| [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
|<nobr>Distance Far</nobr>| [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
|<nobr>Use Actor Orientation</nobr>| [ON] | Enable or disable alignment of the camera to the actor's orientation.
|<nobr>Seed</nobr>| [1234] (Unlimited) | Seed value for generating random camera motions.
|<nobr>Fade To Black</nobr>| [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
|<nobr>F2B Probability</nobr>| [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|<nobr>Audio Sensitivity</nobr>| [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
|<nobr><b>Target Selection</b></nobr>|| 
|<nobr>Head</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's head.
|<nobr>Chest</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's chest.
|<nobr>Center</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's center.
|<nobr>Legs</nobr>| [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
|<nobr>Feet</nobr>| [0] (0 ~ 1) | Probability of targeting the actor's feet.
|<nobr><b>Distance Selection</b></nobr>|| 
|<nobr>Close Up</nobr>| [1] (0 ~ 1) | Probability of a close-up camera distance.
|<nobr>Zoom In</nobr>| [0.25] (0 ~ 1) | Probability of zooming in.
|<nobr>Zoom Out</nobr>| [0.25] (0 ~ 1) | Probability of zooming out.
|<nobr>Middle</nobr>| [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
|<nobr>Far</nobr>| [0.25] (0 ~ 1) | Probability of a far camera distance.
|<nobr><b>Path Selection</b></nobr>|| 
|<nobr>High Angle</nobr>| [20] (0 ~ 30) | Maximum upward angle for the camera.
|<nobr>Low Angle</nobr>| [-20] (-30 ~ 0) | Maximum downward angle for the camera.
|<nobr><b>Orientation</b></nobr>|| 
|<nobr>Front Center</nobr>| [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
|<nobr>Front 45</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
|<nobr>Side 90</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
|<nobr>Back 135</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
|<nobr>Back 180</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
|<nobr>Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1,  |
