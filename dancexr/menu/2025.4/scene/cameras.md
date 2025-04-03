---
locale: en-rUS
layout: single
title: Camera: [Freefly Cam]
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[Environment](../menu#Environment) > Camera: [Freefly Cam]



| Setting | Value | Description |
| :--- | --- | :--- |
| [Freefly Cam] || 0/7/False
| └ **[Freefly Cam]** | | 
| └ ├ Target Select: Auto || 0/13/True
| └ │ Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| └ ├ Tracking Mode: Center || 1/13/True
| └ │ Tracking Mode | **Center** | Center, Head, Chest,  |
| └ ├ Target Smoothing | [0.5] (0 ~ 2) | 2/13/True
| └ ├ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing3/13/True
| └ ├ Lock On Target | OFF | Automatically focus on target4/13/True
| └ ├ Camera Shake | [0.5] (0 ~ 1) | 5/13/True
| └ ├ Lock Rotation | OFF | Camera follows the rotation of the target6/13/True
| └ ├ Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view7/13/True
| └ ├ Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV8/13/True
| └ ├ FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom9/13/True
| └ ├ Vertical Offset | [0] (-1 ~ 1) | Offset vertically10/13/True
| └ ├ FOV | [30] (5 ~ 120) | 11/13/True
| └ ├ Beat Cycle | [8] (1 ~ 16) | 12/13/True
| └ ├ Use Orbit Move | OFF | Enable or disable orbit movement, allowing the camera to rotate around a central point.13/13/True
| └ └ Presets | **Freefly** | Freefly, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |
| [Orbit Cam] || 1/7/False
| └ **[Orbit Cam]** | | 
| └ ├ Target Select: Auto || 0/21/True
| └ │ Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| └ ├ Tracking Mode: Center || 1/21/True
| └ │ Tracking Mode | **Center** | Center, Head, Chest,  |
| └ ├ Target Smoothing | [0.5] (0 ~ 2) | 2/21/True
| └ ├ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing3/21/True
| └ ├ FOV | [30] (5 ~ 120) | 4/21/True
| └ ├ Beat Cycle | [8] (1 ~ 16) | 5/21/True
| └ ├ Use Controller Input | OFF | 6/21/True
| └ ├ Prevent Below Floor | ON | 7/21/True
| └ ├ Retain Velocity | OFF | Maintain the rotation when there is no input8/21/True
| └ ├ Max Speed | [15] (0 ~ 30) | Maximum rotation speed9/21/True
| └ ├ Min Speed | [0] (0 ~ 30) | Minimum rotation speed10/21/True
| └ ├ Auto Mode | OFF | 11/21/True
| └ ├ Distance Min | [1] (0 ~ 10) | 12/21/True
| └ ├ Distance Max | [3] (1 ~ 10) | 13/21/True
| └ ├ Distance Cycle | [12] (Unlimited) | 14/21/True
| └ ├ Pitch Min | [-15] (-45 ~ 0) | 15/21/True
| └ ├ Pitch Max | [15] (0 ~ 45) | 16/21/True
| └ ├ Pitch Cycle | [32] (Unlimited) | 17/21/True
| └ ├ Height Min | [0] (-1 ~ 0) | 18/21/True
| └ ├ Height Max | [0.5] (0 ~ 1) | 19/21/True
| └ ├ Height Cycle | [32] (Unlimited) | 20/21/True
| └ ├ Speed | [10] (0 ~ 90) | 21/21/True
| └ └ Presets | **Default (Reset)** | Default (Reset), Preset 1,  |
| [Auto Cam] || 2/7/False
| └ **[Auto Cam]** | | 
| └ ├ Target Select: Auto || 0/33/True
| └ │ Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| └ ├ Tracking Mode: Center || 1/33/True
| └ │ Tracking Mode | **Center** | Center, Head, Chest,  |
| └ ├ Target Smoothing | [0.5] (0 ~ 2) | 2/33/True
| └ ├ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing3/33/True
| └ ├ FOV | [30] (5 ~ 120) | 4/33/True
| └ ├ Beat Cycle | [8] (1 ~ 16) | 5/33/True
| └ ├ Distance Near | [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.6/33/True
| └ ├ Distance Far | [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.7/33/True
| └ ├ Use Actor Orientation | ON | Enable or disable alignment of the camera to the actor's orientation.8/33/True
| └ ├ Seed | [1234] (Unlimited) | Seed value for generating random camera motions.9/33/True
| └ ├ Fade To Black | [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.10/33/True
| └ ├ F2B Probability | [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.11/33/True
| └ ├ Audio Sensitivity | [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.12/33/True
| └ ├ Target Selection || 13/33/True
| └ ├ Head | [1] (0 ~ 1) | Probability of targeting the actor's head.14/33/True
| └ ├ Chest | [1] (0 ~ 1) | Probability of targeting the actor's chest.15/33/True
| └ ├ Center | [1] (0 ~ 1) | Probability of targeting the actor's center.16/33/True
| └ ├ Legs | [0.5] (0 ~ 1) | Probability of targeting the actor's legs.17/33/True
| └ ├ Feet | [0] (0 ~ 1) | Probability of targeting the actor's feet.18/33/True
| └ ├ Distance Selection || 19/33/True
| └ ├ Close Up | [1] (0 ~ 1) | Probability of a close-up camera distance.20/33/True
| └ ├ Zoom In | [0.25] (0 ~ 1) | Probability of zooming in.21/33/True
| └ ├ Zoom Out | [0.25] (0 ~ 1) | Probability of zooming out.22/33/True
| └ ├ Middle | [0.25] (0 ~ 1) | Probability of a middle-range camera distance.23/33/True
| └ ├ Far | [0.25] (0 ~ 1) | Probability of a far camera distance.24/33/True
| └ ├ Path Selection || 25/33/True
| └ ├ High Angle | [20] (0 ~ 30) | Maximum upward angle for the camera.26/33/True
| └ ├ Low Angle | [-20] (-30 ~ 0) | Maximum downward angle for the camera.27/33/True
| └ ├ Orientation || 28/33/True
| └ ├ Front Center | [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.29/33/True
| └ ├ Front 45 | [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.30/33/True
| └ ├ Side 90 | [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.31/33/True
| └ ├ Back 135 | [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.32/33/True
| └ ├ Back 180 | [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.33/33/True
| └ └ Presets | **Default (Reset)** | Default (Reset), Preset 1,  |
| [Long Take] || 3/7/False
| └ **[Long Take]** | | 
| └ ├ Target Select: Auto || 0/12/True
| └ │ Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| └ ├ Tracking Mode: Center || 1/12/True
| └ │ Tracking Mode | **Center** | Center, Head, Chest,  |
| └ ├ Target Smoothing | [0.5] (0 ~ 2) | 2/12/True
| └ ├ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing3/12/True
| └ ├ FOV | [30] (5 ~ 120) | 4/12/True
| └ ├ Beat Cycle | [8] (1 ~ 16) | 5/12/True
| └ ├ Rotate Range | [60] (0 ~ 180) | Horizontal rotation range.6/12/True
| └ ├ Distance | [0.5] (0.2 ~ 5) | 7/12/True
| └ ├ Pitch Angle | [-15] (-90 ~ 90) | 8/12/True
| └ ├ Curve | [0] (-1 ~ 1) | The ease curve used when changing motion9/12/True
| └ ├ Prevent Below Floor | ON | 10/12/True
| └ ├ Use Actor Orientation | ON | 11/12/True
| └ ├ Raise Focus When Close | OFF | Move focus position up when distance gets smaller12/12/True
| └ └ Presets | **Default (Reset)** | Default (Reset), Preset 1, Preset 2, Preset 3,  |
| [First Person] || 4/7/False
| └ **[First Person]** | | 
| └ ├ Select Actor || 0/9/False
| └ │ Select Actor |  |  |
| └ ├ Field of View | [45] (30 ~ 100) | 1/9/False
| └ ├ Near Clip Dist | [0.15] (0 ~ 0.3) | 2/9/False
| └ ├ Control Actor Movement | ON | 3/9/False
| └ ├ Control Hands in VR | ON | 4/9/False
| └ ├ Remove Roll | [1] (0 ~ 1) | 5/9/False
| └ ├ Stablizer | [5] (0 ~ 20) | 6/9/False
| └ ├ Damping | [0.1] (0 ~ 1) | 7/9/False
| └ ├ Disable Auto Return | OFF | 8/9/False
| └ └ Re-Center || 9/9/False
| [Fixed Camera] || 5/7/False
| └ **[Fixed Camera]** | | 
| └ ├ Target Select: Auto || 0/19/True
| └ │ Target Select | **Auto** | Auto, Selected, Group, Rotate, Rotate + Group, Stage Center,  |
| └ ├ Tracking Mode: Center || 1/19/True
| └ │ Tracking Mode | **Center** | Center, Head, Chest,  |
| └ ├ Target Smoothing | [0.5] (0 ~ 2) | 2/19/True
| └ ├ Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing3/19/True
| └ ├ Lock On Target | OFF | Automatically focus on target4/19/True
| └ ├ Camera Shake | [0.5] (0 ~ 1) | 5/19/True
| └ ├ Lock Rotation | OFF | Camera follows the rotation of the target6/19/True
| └ ├ Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view7/19/True
| └ ├ Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV8/19/True
| └ ├ FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom9/19/True
| └ ├ Vertical Offset | [0] (-1 ~ 1) | Offset vertically10/19/True
| └ ├ FOV | [10] (5 ~ 120) | 11/19/True
| └ ├ Beat Cycle | [8] (1 ~ 16) | 12/19/True
| └ ├ Size | [1] (0 ~ 2) | 13/19/True
| └ ├ Shift | [0] (-1 ~ 1) | 14/19/True
| └ ├ Target Center | [0] (-1 ~ 1) | 15/19/True
| └ ├ Offset || 16/19/True
| └ ├ X | [0] (-2 ~ 2) | 17/19/True
| └ ├ Y | [0] (-2 ~ 2) | 18/19/True
| └ ├ Z | [0] (-2 ~ 2) | 19/19/True
| └ └ Presets | **Far** | Near, Far,  |
| Config || 6/7/False
| [Config Camera](config_camera) |
