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
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
| Use Orbit Move | OFF | 
| Presets | **Freefly**, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body,  |  |
| [Orbit Cam] || 
|**[Orbit Cam]** | | 
| Target Select | **Auto**, Selected, Group, Rotate, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
| Use Controller Input | OFF | 
| Prevent Below Floor | ON | 
| Retain Velocity | OFF | Maintain the rotation when there is no input
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
| Presets | **Default (Reset)**, Preset 1,  |  |
| [Auto Cam] || 
|**[Auto Cam]** | | 
| Target Select | **Auto**, Selected, Group, Rotate, Rotate + Group, Stage Center,  |  |
| Tracking Mode | **Center**, Head, Chest,  |  |
|- Target Smoothing | [0.5] (0 ~ 2) | 
|- Prediction | [1] (0 ~ 2) | Predict position of the target to reduce lag caused by smoothing
|- FOV | [30] (5 ~ 120) | 
|- Beat Cycle | [8] (1 ~ 16) | 
|- Distance Near | [1.5] (0.5 ~ 3) | 
|- Distance Far | [2.5] (0.5 ~ 3) | 
| Use Actor Orientation | ON | 
|- Seed | [1234] (Unlimited) | 
|- Fade To Black | [0] (0 ~ 0.25) | 
|- F2B Probability | [0.5] (0 ~ 1) | 
|- Audio Sensitivity | [1] (0 ~ 4) | 
| Target Selection || 
|- Head | [1] (0 ~ 1) | 
|- Chest | [1] (0 ~ 1) | 
|- Center | [1] (0 ~ 1) | 
|- Legs | [0.5] (0 ~ 1) | 
|- Feet | [0] (0 ~ 1) | 
| Distance Selection || 
|- Close Up | [1] (0 ~ 1) | 
|- Zoom In | [0.25] (0 ~ 1) | 
|- Zoom Out | [0.25] (0 ~ 1) | 
|- Middle | [0.25] (0 ~ 1) | 
|- Far | [0.25] (0 ~ 1) | 
| Path Selection || 
|- High Angle | [20] (0 ~ 30) | 
|- Low Angle | [-20] (-30 ~ 0) | 
| Orientation || 
|- Front Center | [1] (0 ~ 1) | 
|- Front 45 | [0] (0 ~ 1) | 
|- Side 90 | [0.25] (0 ~ 1) | 
|- Back 135 | [0] (0 ~ 1) | 
|- Back 180 | [0.25] (0 ~ 1) | 
| Presets | **Default (Reset)**, Preset 1,  |  |
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
| Presets | **Default (Reset)**, Preset 1, Preset 2, Preset 3,  |  |
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
