---
locale: en-rUS
layout: single
title: Motion Override
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[Pro](../menu#Pro) > Motion Override



| Setting | Value | Description |
| :--- | --- | :--- |
| Enable | OFF | 
| **Body** | | 
| ├&nbsp;Position | Free | Free, Lock Horizontal, Lock Vertical, Lock Position, 
| ├&nbsp;Rotation | Free | Free, Lock Rotation, 
| ├&nbsp;Damping | [0.5] (0 ~ 1) | 
| ├&nbsp;Lean | [0] (-45 ~ 90) | 
| ├&nbsp;Bend | [0] (-150 ~ 150) | 
| ├&nbsp;Twist | [0] (-90 ~ 90) | 
| ├&nbsp;Head | [0] (-90 ~ 90) | 
| ├&nbsp;Height | [0] (-1 ~ 1) | 
| ├&nbsp;Forward / Back | [0] (-1 ~ 1) | 
| ├&nbsp;Distance | OFF | 
| ├&nbsp;Target Actor || 
| │&nbsp;Target Actor |  |  |
| ├&nbsp;Detect Range | [2] (0 ~ 10) | 
| ├&nbsp;Min Distance | [0.5] (0 ~ 1) | 
| └&nbsp;Max Distance | [1] (0.5 ~ 2) | 
| **Rocking Motion** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;**Speed** | | 
| │&nbsp;├&nbsp;Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │&nbsp;├&nbsp;Moves Per Group | [8] (4 ~ 32) | 
| │&nbsp;├&nbsp;Phase | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Curve | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Variable Speed | OFF | 
| │&nbsp;├&nbsp;Mode | Gradual | Gradual, Random, Volume, 
| │&nbsp;├&nbsp;Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │&nbsp;└&nbsp;Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 
| ├&nbsp;Rocking Angle | [30] (0 ~ 60) | 
| ├&nbsp;Up / Down | [0.1] (0 ~ 0.3) | 
| ├&nbsp;Front / Back | [0.1] (0 ~ 0.3) | 
| ├&nbsp;Depth Change | [0.1] (0 ~ 0.3) | 
| ├&nbsp;Depth Max | [0.15] (0 ~ 0.3) | 
| ├&nbsp;Depth Extra | [0] (-0.1 ~ 0.1) | 
| └&nbsp;Feet Motion | [0] (-1 ~ 1) | 
| **Head Pose** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Rotatoin X | [0] (-90 ~ 90) | 
| ├&nbsp;Rotatoin Y | [0] (-90 ~ 90) | 
| └&nbsp;Rotatoin Z | [0] (-90 ~ 90) | 
| **Leg Pose** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Relative To Floor | ON | 
| ├&nbsp;Max Twist | [60] (0 ~ 90) | 
| ├&nbsp;Symmetrical | ON | 
| ├&nbsp;**Left** | | 
| │&nbsp;├&nbsp;Open | [0] (-90 ~ 90) | 
| │&nbsp;├&nbsp;Foot X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Y | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Z | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate Y | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate Z | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Toe | [0] (-180 ~ 180) | 
| ├&nbsp;**Right** | | 
| │&nbsp;├&nbsp;Open | [0] (-90 ~ 90) | 
| │&nbsp;├&nbsp;Foot X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Y | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Z | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate Y | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Foot Rotate Z | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Toe | [0] (-180 ~ 180) | 
| └&nbsp;Presets: Ride || 
| &nbsp;&nbsp;Presets | **Ride** | Sit, Ride, Kneel, Stand,  |
| Hands Symmetrical | ON | 
| **Left Hand** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Gesture: Fist || 
| │&nbsp;Gesture | **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├&nbsp;**Hand Position** | | 
| │&nbsp;├&nbsp;X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Y | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Z | [0] (Unlimited) | 
| ├&nbsp;**Hand Rotation** | | 
| │&nbsp;├&nbsp;X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Y | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Z | [0] (Unlimited) | 
| ├&nbsp;Rotation Type | Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
| ├&nbsp;Elbow Orientation | [0] (-180 ~ 180) | 
| ├&nbsp;Mirror Left/Right | OFF | 
| ├&nbsp;Reference Actor: Self || 
| │&nbsp;Reference Actor | **Self** | Self, Partner, Closest,  |
| ├&nbsp;Reference Bone: None || 
| │&nbsp;Reference Bone | **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├&nbsp;IK Mode | Auto | Auto, Normal, Cylinder, Sphere, Align, 
| ├&nbsp;Side Selection | Auto | Auto, Left, Right, 
| ├&nbsp;Blend Range | [0.75] (0 ~ 2) | 
| ├&nbsp;Symmetrical Offset | [0] (-1 ~ 1) | 
| ├&nbsp;Use Accessory Position | ON | 
| ├&nbsp;**Motion** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;**Speed** | | 
| │&nbsp;│&nbsp;├&nbsp;Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │&nbsp;│&nbsp;├&nbsp;Moves Per Group | [8] (4 ~ 32) | 
| │&nbsp;│&nbsp;├&nbsp;Phase | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Curve | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Variable Speed | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Mode | Gradual | Gradual, Random, Volume, 
| │&nbsp;│&nbsp;├&nbsp;Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │&nbsp;│&nbsp;└&nbsp;Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 
| │&nbsp;├&nbsp;Distance | [0.1] (0 ~ 0.3) | 
| │&nbsp;└&nbsp;Angle | [0] (-60 ~ 60) | 
| ├&nbsp;**Custom Pose** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Open | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Thumb Axis | [90] (-360 ~ 360) | 
| │&nbsp;├&nbsp;Thumb Fold | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Thumb Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Index Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Middle Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Ring Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Pinky Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Propagate | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Blend | [1] (0 ~ 1) | 
| ├&nbsp;Pose Weight | [1] (0 ~ 1) | 
| ├&nbsp;Grab Distance | [0.015] (-0.1 ~ 0.1) | 
| ├&nbsp;Grab Position | [-0.05] (-0.1 ~ 0.1) | 
| ├&nbsp;Grab Axis | [0] (-180 ~ 180) | 
| └&nbsp;Presets: Rest || 
| &nbsp;&nbsp;Presets | **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
| **Right Hand** | | 
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Gesture: Fist || 
| │&nbsp;Gesture | **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├&nbsp;**Hand Position** | | 
| │&nbsp;├&nbsp;X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Y | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Z | [0] (Unlimited) | 
| ├&nbsp;**Hand Rotation** | | 
| │&nbsp;├&nbsp;X | [0] (Unlimited) | 
| │&nbsp;├&nbsp;Y | [0] (Unlimited) | 
| │&nbsp;└&nbsp;Z | [0] (Unlimited) | 
| ├&nbsp;Rotation Type | Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
| ├&nbsp;Elbow Orientation | [0] (-180 ~ 180) | 
| ├&nbsp;Mirror Left/Right | OFF | 
| ├&nbsp;Reference Actor: Self || 
| │&nbsp;Reference Actor | **Self** | Self, Partner, Closest,  |
| ├&nbsp;Reference Bone: None || 
| │&nbsp;Reference Bone | **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├&nbsp;IK Mode | Auto | Auto, Normal, Cylinder, Sphere, Align, 
| ├&nbsp;Side Selection | Auto | Auto, Left, Right, 
| ├&nbsp;Blend Range | [0.75] (0 ~ 2) | 
| ├&nbsp;Symmetrical Offset | [0] (-1 ~ 1) | 
| ├&nbsp;Use Accessory Position | ON | 
| ├&nbsp;**Motion** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;**Speed** | | 
| │&nbsp;│&nbsp;├&nbsp;Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │&nbsp;│&nbsp;├&nbsp;Moves Per Group | [8] (4 ~ 32) | 
| │&nbsp;│&nbsp;├&nbsp;Phase | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Curve | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Variable Speed | OFF | 
| │&nbsp;│&nbsp;├&nbsp;Mode | Gradual | Gradual, Random, Volume, 
| │&nbsp;│&nbsp;├&nbsp;Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │&nbsp;│&nbsp;└&nbsp;Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 
| │&nbsp;├&nbsp;Distance | [0.1] (0 ~ 0.3) | 
| │&nbsp;└&nbsp;Angle | [0] (-60 ~ 60) | 
| ├&nbsp;**Custom Pose** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Open | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Thumb Axis | [90] (-360 ~ 360) | 
| │&nbsp;├&nbsp;Thumb Fold | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Thumb Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Index Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Middle Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Ring Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Pinky Bend | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;Propagate | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;Blend | [1] (0 ~ 1) | 
| ├&nbsp;Pose Weight | [1] (0 ~ 1) | 
| ├&nbsp;Grab Distance | [0.015] (-0.1 ~ 0.1) | 
| ├&nbsp;Grab Position | [-0.05] (-0.1 ~ 0.1) | 
| ├&nbsp;Grab Axis | [0] (-180 ~ 180) | 
| └&nbsp;Presets: Rest || 
| &nbsp;&nbsp;Presets | **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
| **Ride Model** | | 
| ├&nbsp;Enable | ON | 
| ├&nbsp;Model: [Hoverbike] || 
| │&nbsp;Model | **[Hoverbike]** | [Hoverbike], [Rocking Horse],  |
| ├&nbsp;Acceleration | [10] (0 ~ 20) | 
| ├&nbsp;Drag | [0.05] (0 ~ 1) | 
| ├&nbsp;Tilt When Turning | [0.5] (0 ~ 1) | 
| ├&nbsp;Position || 
| ├&nbsp;X | [0] (-1 ~ 1) | 
| ├&nbsp;Y | [0] (-1 ~ 1) | 
| ├&nbsp;Z | [0] (-1 ~ 1) | 
| ├&nbsp;Rotation || 
| ├&nbsp;X | [0] (-90 ~ 90) | 
| ├&nbsp;Y | [0] (-90 ~ 90) | 
| ├&nbsp;Z | [0] (-90 ~ 90) | 
| ├&nbsp;Scale | [0] (-5 ~ 5) | 
| └&nbsp;Particle Effect | ON | 
| Presets: Free || 
| Presets | **Free** | Free, Rocking Motion, Hoverbike, Rocking Horse, Pole Motion, Pole Blend,  |
