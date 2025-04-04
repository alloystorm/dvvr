---
locale: en-rUS
layout: single
title: Camera
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[Environment](../menu#Environment) > Camera



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>[Freefly Cam]</nobr>|| 
|<nobr>└&nbsp;<b>[Freefly Cam]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>&nbsp;&nbsp;├&nbsp;Lock On Target</nobr>| [OFF] | Automatically focus on target
|<nobr>&nbsp;&nbsp;├&nbsp;Camera Shake</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Lock Rotation</nobr>| [OFF] | Camera follows the rotation of the target
|<nobr>&nbsp;&nbsp;├&nbsp;Auto Zoom</nobr>| [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
|<nobr>&nbsp;&nbsp;├&nbsp;Zoom Speed</nobr>| [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
|<nobr>&nbsp;&nbsp;├&nbsp;FOV Height At Target</nobr>| [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
|<nobr>&nbsp;&nbsp;├&nbsp;Vertical Offset</nobr>| [0] (-1 ~ 1) | Offset vertically
|<nobr>&nbsp;&nbsp;├&nbsp;FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Use Orbit Move</nobr>| [OFF] | Enable or disable orbit movement, allowing the camera to rotate around a central point.
|<nobr>&nbsp;&nbsp;└&nbsp;Presets</nobr>| **Freefly** | Freefly, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |
|<nobr>[Orbit Cam]</nobr>|| 
|<nobr>└&nbsp;<b>[Orbit Cam]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>&nbsp;&nbsp;├&nbsp;FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Use Controller Input</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prevent Below Floor</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Retain Velocity</nobr>| [OFF] | Maintain the rotation when there is no input
|<nobr>&nbsp;&nbsp;├&nbsp;Max Speed</nobr>| [15] (0 ~ 30) | Maximum rotation speed
|<nobr>&nbsp;&nbsp;├&nbsp;Min Speed</nobr>| [0] (0 ~ 30) | Minimum rotation speed
|<nobr>&nbsp;&nbsp;├&nbsp;Auto Mode</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Distance Min</nobr>| [1] (0 ~ 10) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Distance Max</nobr>| [3] (1 ~ 10) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Distance Cycle</nobr>| [12] (Unlimited) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Pitch Min</nobr>| [-15] (-45 ~ 0) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Pitch Max</nobr>| [15] (0 ~ 45) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Pitch Cycle</nobr>| [32] (Unlimited) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Height Min</nobr>| [0] (-1 ~ 0) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Height Max</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Height Cycle</nobr>| [32] (Unlimited) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Speed</nobr>| [10] (0 ~ 90) | 
|<nobr>&nbsp;&nbsp;└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1,  |
|<nobr>[Auto Cam]</nobr>|| 
|<nobr>└&nbsp;<b>[Auto Cam]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>&nbsp;&nbsp;├&nbsp;FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Distance Near</nobr>| [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
|<nobr>&nbsp;&nbsp;├&nbsp;Distance Far</nobr>| [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
|<nobr>&nbsp;&nbsp;├&nbsp;Use Actor Orientation</nobr>| [ON] | Enable or disable alignment of the camera to the actor's orientation.
|<nobr>&nbsp;&nbsp;├&nbsp;Seed</nobr>| [1234] (Unlimited) | Seed value for generating random camera motions.
|<nobr>&nbsp;&nbsp;├&nbsp;Fade To Black</nobr>| [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
|<nobr>&nbsp;&nbsp;├&nbsp;F2B Probability</nobr>| [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|<nobr>&nbsp;&nbsp;├&nbsp;Audio Sensitivity</nobr>| [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
|<nobr>&nbsp;&nbsp;├&nbsp;<b>Target Selection</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;Head</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's head.
|<nobr>&nbsp;&nbsp;├&nbsp;Chest</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's chest.
|<nobr>&nbsp;&nbsp;├&nbsp;Center</nobr>| [1] (0 ~ 1) | Probability of targeting the actor's center.
|<nobr>&nbsp;&nbsp;├&nbsp;Legs</nobr>| [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
|<nobr>&nbsp;&nbsp;├&nbsp;Feet</nobr>| [0] (0 ~ 1) | Probability of targeting the actor's feet.
|<nobr>&nbsp;&nbsp;├&nbsp;<b>Distance Selection</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;Close Up</nobr>| [1] (0 ~ 1) | Probability of a close-up camera distance.
|<nobr>&nbsp;&nbsp;├&nbsp;Zoom In</nobr>| [0.25] (0 ~ 1) | Probability of zooming in.
|<nobr>&nbsp;&nbsp;├&nbsp;Zoom Out</nobr>| [0.25] (0 ~ 1) | Probability of zooming out.
|<nobr>&nbsp;&nbsp;├&nbsp;Middle</nobr>| [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
|<nobr>&nbsp;&nbsp;├&nbsp;Far</nobr>| [0.25] (0 ~ 1) | Probability of a far camera distance.
|<nobr>&nbsp;&nbsp;├&nbsp;<b>Path Selection</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;High Angle</nobr>| [20] (0 ~ 30) | Maximum upward angle for the camera.
|<nobr>&nbsp;&nbsp;├&nbsp;Low Angle</nobr>| [-20] (-30 ~ 0) | Maximum downward angle for the camera.
|<nobr>&nbsp;&nbsp;├&nbsp;<b>Orientation</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;Front Center</nobr>| [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
|<nobr>&nbsp;&nbsp;├&nbsp;Front 45</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
|<nobr>&nbsp;&nbsp;├&nbsp;Side 90</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
|<nobr>&nbsp;&nbsp;├&nbsp;Back 135</nobr>| [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
|<nobr>&nbsp;&nbsp;├&nbsp;Back 180</nobr>| [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
|<nobr>&nbsp;&nbsp;└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1,  |
|<nobr>[Long Take]</nobr>|| 
|<nobr>└&nbsp;<b>[Long Take]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>&nbsp;&nbsp;├&nbsp;FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Rotate Range</nobr>| [60] (0 ~ 180) | Horizontal rotation range.
|<nobr>&nbsp;&nbsp;├&nbsp;Distance</nobr>| [0.5] (0.2 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Pitch Angle</nobr>| [-15] (-90 ~ 90) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Curve</nobr>| [0] (-1 ~ 1) | The ease curve used when changing motion
|<nobr>&nbsp;&nbsp;├&nbsp;Prevent Below Floor</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Use Actor Orientation</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Raise Focus When Close</nobr>| [OFF] | Move focus position up when distance gets smaller
|<nobr>&nbsp;&nbsp;└&nbsp;Presets</nobr>| **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3,  |
|<nobr>[First Person]</nobr>|| 
|<nobr>└&nbsp;<b>[First Person]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Select Actor</nobr>|  |  |
|<nobr>&nbsp;&nbsp;├&nbsp;Field of View</nobr>| [45] (30 ~ 100) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Near Clip Dist</nobr>| [0.15] (0 ~ 0.3) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Control Actor Movement</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Control Hands in VR</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;Remove Roll</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Stablizer</nobr>| [5] (0 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Damping</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Disable Auto Return</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;└&nbsp;Re-Center</nobr>|| 
|<nobr>[Fixed Camera]</nobr>|| 
|<nobr>└&nbsp;<b>[Fixed Camera]</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Select</nobr>| **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Tracking Mode</nobr>| **Center** | Center, Head, Chest,  |
|<nobr>&nbsp;&nbsp;├&nbsp;Target Smoothing</nobr>| [0.5] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Prediction</nobr>| [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|<nobr>&nbsp;&nbsp;├&nbsp;Lock On Target</nobr>| [OFF] | Automatically focus on target
|<nobr>&nbsp;&nbsp;├&nbsp;Camera Shake</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Lock Rotation</nobr>| [OFF] | Camera follows the rotation of the target
|<nobr>&nbsp;&nbsp;├&nbsp;Auto Zoom</nobr>| [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
|<nobr>&nbsp;&nbsp;├&nbsp;Zoom Speed</nobr>| [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
|<nobr>&nbsp;&nbsp;├&nbsp;FOV Height At Target</nobr>| [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
|<nobr>&nbsp;&nbsp;├&nbsp;Vertical Offset</nobr>| [0] (-1 ~ 1) | Offset vertically
|<nobr>&nbsp;&nbsp;├&nbsp;FOV</nobr>| [10] (5 ~ 120) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Beat Cycle</nobr>| [8] (1 ~ 16) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Size</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Shift</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Target Center</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>Offset</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;X</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Y</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;Z</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;└&nbsp;Presets</nobr>| **Far** | Near, Far,  |
|<nobr><b>Config</b></nobr>|| 
| [Config Camera](config_camera) |
