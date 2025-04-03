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
| [Freefly Cam] || 
|**[Freefly Cam]** | | 
| Target Select | Auto, Selected, Group, **Rotate**, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| Lock On Target | OFF | Automatically focus on target
|- Camera Shake | [0.5] (0 ~ 1) | 
| Lock Rotation | OFF | Camera follows the rotation of the target
|- Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
|- Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
|- FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
|- Vertical Offset | [0] (-1 ~ 1) | Offset vertically
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
| Use Orbit Move | OFF | Enable or disable orbit movement, allowing the camera to rotate around a central point.
| Presets | **Freefly**, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |  |
| [Orbit Cam] || 
|**[Orbit Cam]** | | 
| Target Select | Auto, Selected, Group, **Rotate**, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
| Use Controller Input | OFF | 
| Prevent Below Floor | ON | 
| Retain Velocity | ON | Maintain the rotation when there is no input
|- Max Speed | [15] (0 ~ 30) | Maximum rotation speed
|- Min Speed | [0] (0 ~ 30) | Minimum rotation speed
| Auto Mode | OFF | 
|- Distance Min | [1] (0 ~ 10) | 
|- Distance Max | [3] (1 ~ 10) | 
|- Distance Cycle | [12] (Unlimited) | 
|- Pitch Min | [-15] (-45 ~ 0) | 
|- Pitch Max | [15] (0 ~ 45) | 
|- Pitch Cycle | [32] (Unlimited) | 
|- Height Min | [0] (-1 ~ 0) | 
|- Height Max | [0.5] (0 ~ 1) | 
|- Height Cycle | [32] (Unlimited) | 
|- Speed | [10] (0 ~ 90) | 
| Presets | **Default (Reset)**,  |  |
| [Auto Cam] || 
|**[Auto Cam]** | | 
| Target Select | **Auto**, Selected, Group, Rotate, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
|- Distance Near | [1.5] (0.5 ~ 3) | Minimum distance of the camera from the target.
|- Distance Far | [2.5] (0.5 ~ 3) | Maximum distance of the camera from the target.
| Use Actor Orientation | ON | Enable or disable alignment of the camera to the actor's orientation.
|- Seed | [1234] (Unlimited) | Seed value for generating random camera motions.
|- Fade To Black | [0] (0 ~ 0.25) | Duration of the fade-to-black effect during transitions.
|- F2B Probability | [0.5] (0 ~ 1) | Probability of triggering the fade-to-black effect.
|- Audio Sensitivity | [1] (0 ~ 4) | Sensitivity of the camera motion to audio levels.
| Target Selection || 
|- Head | [1] (0 ~ 1) | Probability of targeting the actor's head.
|- Chest | [1] (0 ~ 1) | Probability of targeting the actor's chest.
|- Center | [1] (0 ~ 1) | Probability of targeting the actor's center.
|- Legs | [0.5] (0 ~ 1) | Probability of targeting the actor's legs.
|- Feet | [0] (0 ~ 1) | Probability of targeting the actor's feet.
| Distance Selection || 
|- Close Up | [1] (0 ~ 1) | Probability of a close-up camera distance.
|- Zoom In | [0.25] (0 ~ 1) | Probability of zooming in.
|- Zoom Out | [0.25] (0 ~ 1) | Probability of zooming out.
|- Middle | [0.25] (0 ~ 1) | Probability of a middle-range camera distance.
|- Far | [0.25] (0 ~ 1) | Probability of a far camera distance.
| Path Selection || 
|- High Angle | [20] (0 ~ 30) | Maximum upward angle for the camera.
|- Low Angle | [-20] (-30 ~ 0) | Maximum downward angle for the camera.
| Orientation || 
|- Front Center | [1] (0 ~ 1) | Probability of orienting the camera to the front center of the actor.
|- Front 45 | [0] (0 ~ 1) | Probability of orienting the camera to a 45-degree angle in front of the actor.
|- Side 90 | [0.25] (0 ~ 1) | Probability of orienting the camera to the actor's side at a 90-degree angle.
|- Back 135 | [0] (0 ~ 1) | Probability of orienting the camera to a 135-degree angle behind the actor.
|- Back 180 | [0.25] (0 ~ 1) | Probability of orienting the camera directly behind the actor.
| Presets | **Default (Reset)**,  |  |
| [Long Take] || 
|**[Long Take]** | | 
| Target Select | **Auto**, Selected, Group, Rotate, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
|- Rotate Range | [60] (0 ~ 180) | Horizontal rotation range.
|- Distance | [0.5] (0.2 ~ 5) | 
|- Pitch Angle | [-15] (-90 ~ 90) | 
|- Curve | [0] (-1 ~ 1) | The ease curve used when changing motion
| Prevent Below Floor | ON | 
| Use Actor Orientation | ON | 
| Raise Focus When Close | OFF | Move focus position up when distance gets smaller
| Presets | **Default (Reset)**,  |  |
| [First Person] || 
|**[First Person]** | | 
| Select Actor |  |  |
|- Field of View | [45] (30 ~ 100) | 
|- Near Clip Dist | [0.15] (0 ~ 0.3) | 
| Control Actor Movement | ON | 
| Control Hands in VR | ON | 
|- Remove Roll | [1] (0 ~ 1) | 
|- Stablizer | [5] (0 ~ 20) | 
|- Damping | [0.1] (0 ~ 1) | 
| Disable Auto Return | OFF | 
| Re-Center || 
| [Fixed Camera] || 
|**[Fixed Camera]** | | 
| Target Select | **Auto**, Selected, Group, Rotate, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
| Lock On Target | OFF | Automatically focus on target
|- Camera Shake | [0.5] (0 ~ 1) | 
| Lock Rotation | OFF | Camera follows the rotation of the target
|- Auto Zoom | [0] (0 ~ 1) | Automatically zoom in and out to maintain the target size in view
|- Zoom Speed | [0.5] (0 ~ 1) | Time it takes to zoom to target FOV
|- FOV Height At Target | [1] (0.2 ~ 2) | Vertical height for the target when using auto zoom
|- Vertical Offset | [0] (-1 ~ 1) | Offset vertically
|- FOV | [10] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
|- Size | [1] (0 ~ 2) | 
|- Shift | [0] (-1 ~ 1) | 
|- Target Center | [0] (-1 ~ 1) | 
| Offset || 
|- X | [0] (-2 ~ 2) | 
|- Y | [0] (-2 ~ 2) | 
|- Z | [0] (-2 ~ 2) | 
| Presets | Near, **Far**,  |  |
| Config || 
| [Config Camera](#config_camera) |


### **Config Camera**



| Setting | Value | Description |
| :--- | --- | :--- |
|- Height Offset | [0] (-5 ~ 5) | 
|- FOV Scale | [1] (0.25 ~ 2) | 
|- Portrait Mode Zoom | [1.2] (1 ~ 2) | 
|- Rotation Filter | No Rotation, Direction Only, **Full Rotation**,  | 
|- Near Clip | [0.01] (0 ~ 0.5) | 
| Reset When Motion Change | ON | 
| Reset Offset || 
