---
locale: en-rUS
layout: single
title: Camera
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[Environment](../menu#Environment) > Camera



| Setting | Value | Description |
| :--- | --- | :--- |
| [Freefly Cam] || 
| └&nbsp;**[Freefly Cam]** | | 
| &nbsp;&nbsp;├&nbsp;Target Select: Auto || 
| &nbsp;&nbsp;│&nbsp;Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| &nbsp;&nbsp;├&nbsp;Tracking Mode: Center || 
| &nbsp;&nbsp;│&nbsp;Tracking Mode | **Center** | Center, Head, Chest,  |
| &nbsp;&nbsp;├&nbsp;Target Smoothing | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| &nbsp;&nbsp;├&nbsp;Lock On Target | OFF | Automatically focus on target
| &nbsp;&nbsp;├&nbsp;Camera Shake | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Lock Rotation | OFF | Camera follows the rotation of the target
| &nbsp;&nbsp;├&nbsp;Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
| &nbsp;&nbsp;├&nbsp;Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
| &nbsp;&nbsp;├&nbsp;FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
| &nbsp;&nbsp;├&nbsp;Vertical Offset | [0] (-1 ~ 1) | Offset vertically
| &nbsp;&nbsp;├&nbsp;FOV | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;Beat Cycle | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;Use Orbit Move | OFF | Enable or disable orbit movement, allowing the camera to rotate around a central point.
| &nbsp;&nbsp;└&nbsp;Presets: Freefly || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **Freefly** | Freefly, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |
| [Orbit Cam] || 
| └&nbsp;**[Orbit Cam]** | | 
| &nbsp;&nbsp;├&nbsp;Target Select: Auto || 
| &nbsp;&nbsp;│&nbsp;Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| &nbsp;&nbsp;├&nbsp;Tracking Mode: Center || 
| &nbsp;&nbsp;│&nbsp;Tracking Mode | **Center** | Center, Head, Chest,  |
| &nbsp;&nbsp;├&nbsp;Target Smoothing | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| &nbsp;&nbsp;├&nbsp;FOV | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;Beat Cycle | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;Use Controller Input | OFF | 
| &nbsp;&nbsp;├&nbsp;Prevent Below Floor | ON | 
| &nbsp;&nbsp;├&nbsp;Retain Velocity | OFF | Maintain the rotation when there is no input
| &nbsp;&nbsp;├&nbsp;Max Speed | [15] (0 ~ 30) | Maximum rotation speed
| &nbsp;&nbsp;├&nbsp;Min Speed | [0] (0 ~ 30) | Minimum rotation speed
| &nbsp;&nbsp;├&nbsp;Auto Mode | OFF | 
| &nbsp;&nbsp;├&nbsp;Distance Min | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;Distance Max | [3] (1 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;Distance Cycle | [12] (Unlimited) | 
| &nbsp;&nbsp;├&nbsp;Pitch Min | [-15] (-45 ~ 0) | 
| &nbsp;&nbsp;├&nbsp;Pitch Max | [15] (0 ~ 45) | 
| &nbsp;&nbsp;├&nbsp;Pitch Cycle | [32] (Unlimited) | 
| &nbsp;&nbsp;├&nbsp;Height Min | [0] (-1 ~ 0) | 
| &nbsp;&nbsp;├&nbsp;Height Max | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Height Cycle | [32] (Unlimited) | 
| &nbsp;&nbsp;├&nbsp;Speed | [10] (0 ~ 90) | 
| &nbsp;&nbsp;└&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1,  |
| [Auto Cam] || 
| └&nbsp;**[Auto Cam]** | | 
| &nbsp;&nbsp;├&nbsp;Target Select: Auto || 
| &nbsp;&nbsp;│&nbsp;Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| &nbsp;&nbsp;├&nbsp;Tracking Mode: Center || 
| &nbsp;&nbsp;│&nbsp;Tracking Mode | **Center** | Center, Head, Chest,  |
| &nbsp;&nbsp;├&nbsp;Target Smoothing | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| &nbsp;&nbsp;├&nbsp;FOV | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;Beat Cycle | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;Distance Near | [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
| &nbsp;&nbsp;├&nbsp;Distance Far | [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
| &nbsp;&nbsp;├&nbsp;Use Actor Orientation | ON | Enable or disable alignment of the camera to the actor's orientation.
| &nbsp;&nbsp;├&nbsp;Seed | [1234] (Unlimited) | Seed value for generating random camera motions.
| &nbsp;&nbsp;├&nbsp;Fade To Black | [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
| &nbsp;&nbsp;├&nbsp;F2B Probability | [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
| &nbsp;&nbsp;├&nbsp;Audio Sensitivity | [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
| &nbsp;&nbsp;├&nbsp;Target Selection || 
| &nbsp;&nbsp;├&nbsp;Head | [1] (0 ~ 1) | Probability of targeting the actor's head.
| &nbsp;&nbsp;├&nbsp;Chest | [1] (0 ~ 1) | Probability of targeting the actor's chest.
| &nbsp;&nbsp;├&nbsp;Center | [1] (0 ~ 1) | Probability of targeting the actor's center.
| &nbsp;&nbsp;├&nbsp;Legs | [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
| &nbsp;&nbsp;├&nbsp;Feet | [0] (0 ~ 1) | Probability of targeting the actor's feet.
| &nbsp;&nbsp;├&nbsp;Distance Selection || 
| &nbsp;&nbsp;├&nbsp;Close Up | [1] (0 ~ 1) | Probability of a close-up camera distance.
| &nbsp;&nbsp;├&nbsp;Zoom In | [0.25] (0 ~ 1) | Probability of zooming in.
| &nbsp;&nbsp;├&nbsp;Zoom Out | [0.25] (0 ~ 1) | Probability of zooming out.
| &nbsp;&nbsp;├&nbsp;Middle | [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
| &nbsp;&nbsp;├&nbsp;Far | [0.25] (0 ~ 1) | Probability of a far camera distance.
| &nbsp;&nbsp;├&nbsp;Path Selection || 
| &nbsp;&nbsp;├&nbsp;High Angle | [20] (0 ~ 30) | Maximum upward angle for the camera.
| &nbsp;&nbsp;├&nbsp;Low Angle | [-20] (-30 ~ 0) | Maximum downward angle for the camera.
| &nbsp;&nbsp;├&nbsp;Orientation || 
| &nbsp;&nbsp;├&nbsp;Front Center | [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
| &nbsp;&nbsp;├&nbsp;Front 45 | [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
| &nbsp;&nbsp;├&nbsp;Side 90 | [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
| &nbsp;&nbsp;├&nbsp;Back 135 | [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
| &nbsp;&nbsp;├&nbsp;Back 180 | [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
| &nbsp;&nbsp;└&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1,  |
| [Long Take] || 
| └&nbsp;**[Long Take]** | | 
| &nbsp;&nbsp;├&nbsp;Target Select: Auto || 
| &nbsp;&nbsp;│&nbsp;Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| &nbsp;&nbsp;├&nbsp;Tracking Mode: Center || 
| &nbsp;&nbsp;│&nbsp;Tracking Mode | **Center** | Center, Head, Chest,  |
| &nbsp;&nbsp;├&nbsp;Target Smoothing | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| &nbsp;&nbsp;├&nbsp;FOV | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;Beat Cycle | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;Rotate Range | [60] (0 ~ 180) | Horizontal rotation range.
| &nbsp;&nbsp;├&nbsp;Distance | [0.5] (0.2 ~ 5) | 
| &nbsp;&nbsp;├&nbsp;Pitch Angle | [-15] (-90 ~ 90) | 
| &nbsp;&nbsp;├&nbsp;Curve | [0] (-1 ~ 1) | The ease curve used when changing motion
| &nbsp;&nbsp;├&nbsp;Prevent Below Floor | ON | 
| &nbsp;&nbsp;├&nbsp;Use Actor Orientation | ON | 
| &nbsp;&nbsp;├&nbsp;Raise Focus When Close | OFF | Move focus position up when distance gets smaller
| &nbsp;&nbsp;└&nbsp;Presets: Default (Reset) || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3,  |
| [First Person] || 
| └&nbsp;**[First Person]** | | 
| &nbsp;&nbsp;├&nbsp;Select Actor || 
| &nbsp;&nbsp;│&nbsp;Select Actor |  |  |
| &nbsp;&nbsp;├&nbsp;Field of View | [45] (30 ~ 100) | 
| &nbsp;&nbsp;├&nbsp;Near Clip Dist | [0.15] (0 ~ 0.3) | 
| &nbsp;&nbsp;├&nbsp;Control Actor Movement | ON | 
| &nbsp;&nbsp;├&nbsp;Control Hands in VR | ON | 
| &nbsp;&nbsp;├&nbsp;Remove Roll | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Stablizer | [5] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;Damping | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Disable Auto Return | OFF | 
| &nbsp;&nbsp;└&nbsp;Re-Center || 
| [Fixed Camera] || 
| └&nbsp;**[Fixed Camera]** | | 
| &nbsp;&nbsp;├&nbsp;Target Select: Auto || 
| &nbsp;&nbsp;│&nbsp;Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| &nbsp;&nbsp;├&nbsp;Tracking Mode: Center || 
| &nbsp;&nbsp;│&nbsp;Tracking Mode | **Center** | Center, Head, Chest,  |
| &nbsp;&nbsp;├&nbsp;Target Smoothing | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| &nbsp;&nbsp;├&nbsp;Lock On Target | OFF | Automatically focus on target
| &nbsp;&nbsp;├&nbsp;Camera Shake | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Lock Rotation | OFF | Camera follows the rotation of the target
| &nbsp;&nbsp;├&nbsp;Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
| &nbsp;&nbsp;├&nbsp;Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
| &nbsp;&nbsp;├&nbsp;FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
| &nbsp;&nbsp;├&nbsp;Vertical Offset | [0] (-1 ~ 1) | Offset vertically
| &nbsp;&nbsp;├&nbsp;FOV | [10] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;Beat Cycle | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;Size | [1] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Shift | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Target Center | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;Offset || 
| &nbsp;&nbsp;├&nbsp;X | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Y | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;Z | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;└&nbsp;Presets: Far || 
| &nbsp;&nbsp;&nbsp;&nbsp;Presets | **Far** | Near, Far,  |
| Config || 
| [Config Camera](config_camera) |
