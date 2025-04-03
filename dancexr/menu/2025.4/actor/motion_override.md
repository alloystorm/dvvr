---
locale: en-rUS
layout: single
title: Motion Override
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[Pro](../menu#Pro) > Motion Override



| Setting | Value | Description |
| :--- | --- | :--- |
| Enable Motion Override | OFF | 0/8/True
| **Body** | | 1/8/True
| ├ Position | Free | Free, Lock Horizontal, Lock Vertical, Lock Position, 0/13/False
| ├ Rotation | Free | Free, Lock Rotation, 1/13/False
| ├ Damping | [0.5] (0 ~ 1) | 2/13/False
| ├ Lean | [0] (-45 ~ 90) | 3/13/False
| ├ Bend | [0] (-150 ~ 150) | 4/13/False
| ├ Twist | [0] (-90 ~ 90) | 5/13/False
| ├ Head | [0] (-90 ~ 90) | 6/13/False
| ├ Height | [0] (-1 ~ 1) | 7/13/False
| ├ Forward / Back | [0] (-1 ~ 1) | 8/13/False
| ├ Distance | OFF | 9/13/False
| ├ Target Actor || 10/13/False
| │ Target Actor |  |  |
| ├ Detect Range | [2] (0 ~ 10) | 11/13/False
| ├ Min Distance | [0.5] (0 ~ 1) | 12/13/False
| └ Max Distance | [1] (0.5 ~ 2) | 13/13/False
| **Rocking Motion** | | 2/8/True
| ├ Enable Rocking Motion | ON | 0/8/False
| ├ **Speed** | | 1/8/False
| │ ├ Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 0/7/False
| │ ├ Moves Per Group | [8] (4 ~ 32) | 1/7/False
| │ ├ Phase | [0] (0 ~ 1) | 2/7/False
| │ ├ Curve | [0] (0 ~ 1) | 3/7/False
| │ ├ Variable Speed | OFF | 4/7/False
| │ ├ Mode | Gradual | Gradual, Random, Volume, 5/7/False
| │ ├ Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 6/7/False
| │ └ Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 7/7/False
| ├ Rocking Angle | [30] (0 ~ 60) | 2/8/False
| ├ Up / Down | [0.1] (0 ~ 0.3) | 3/8/False
| ├ Front / Back | [0.1] (0 ~ 0.3) | 4/8/False
| ├ Depth Change | [0.1] (0 ~ 0.3) | 5/8/False
| ├ Depth Max | [0.15] (0 ~ 0.3) | 6/8/False
| ├ Depth Extra | [0] (-0.1 ~ 0.1) | 7/8/False
| └ Feet Motion | [0] (-1 ~ 1) | 8/8/False
| **Head Pose** | | 3/8/True
| ├ Enable Head Pose | OFF | 0/3/False
| ├ Rotatoin X | [0] (-90 ~ 90) | 1/3/False
| ├ Rotatoin Y | [0] (-90 ~ 90) | 2/3/False
| └ Rotatoin Z | [0] (-90 ~ 90) | 3/3/False
| **Leg Pose** | | 4/8/True
| ├ Enable Leg Pose | ON | 0/5/True
| ├ Relative To Floor | ON | 1/5/True
| ├ Max Twist | [60] (0 ~ 90) | 2/5/True
| ├ Symmetrical | ON | 3/5/True
| ├ **Left** | | 4/5/True
| │ ├ Open | [0] (-90 ~ 90) | 0/7/False
| │ ├ Foot X | [0] (Unlimited) | 1/7/False
| │ ├ Foot Y | [0] (Unlimited) | 2/7/False
| │ ├ Foot Z | [0] (Unlimited) | 3/7/False
| │ ├ Foot Rotate X | [0] (Unlimited) | 4/7/False
| │ ├ Foot Rotate Y | [0] (Unlimited) | 5/7/False
| │ ├ Foot Rotate Z | [0] (Unlimited) | 6/7/False
| │ └ Toe | [0] (-180 ~ 180) | 7/7/False
| ├ **Right** | | 5/5/True
| │ ├ Open | [0] (-90 ~ 90) | 0/7/False
| │ ├ Foot X | [0] (Unlimited) | 1/7/False
| │ ├ Foot Y | [0] (Unlimited) | 2/7/False
| │ ├ Foot Z | [0] (Unlimited) | 3/7/False
| │ ├ Foot Rotate X | [0] (Unlimited) | 4/7/False
| │ ├ Foot Rotate Y | [0] (Unlimited) | 5/7/False
| │ ├ Foot Rotate Z | [0] (Unlimited) | 6/7/False
| │ └ Toe | [0] (-180 ~ 180) | 7/7/False
| └ Presets | **Ride** | Sit, Ride, Kneel, Stand,  |
| Hands Symmetrical | ON | 5/8/True
| **Left Hand** | | 6/8/True
| ├ Enable Left Hand | OFF | 0/19/True
| ├ Gesture: Fist || 1/19/True
| │ Gesture | **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├ **Hand Position** | | 2/19/True
| │ ├ X | [0] (Unlimited) | 0/2/False
| │ ├ Y | [0] (Unlimited) | 1/2/False
| │ └ Z | [0] (Unlimited) | 2/2/False
| ├ **Hand Rotation** | | 3/19/True
| │ ├ X | [0] (Unlimited) | 0/2/False
| │ ├ Y | [0] (Unlimited) | 1/2/False
| │ └ Z | [0] (Unlimited) | 2/2/False
| ├ Rotation Type | Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 4/19/True
| ├ Elbow Orientation | [0] (-180 ~ 180) | 5/19/True
| ├ Mirror Left/Right | OFF | 6/19/True
| ├ Reference Actor: Self || 7/19/True
| │ Reference Actor | **Self** | Self, Partner, Closest,  |
| ├ Reference Bone: None || 8/19/True
| │ Reference Bone | **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├ IK Mode | Auto | Auto, Normal, Cylinder, Sphere, Align, 9/19/True
| ├ Side Selection | Auto | Auto, Left, Right, 10/19/True
| ├ Blend Range | [0.75] (0 ~ 2) | 11/19/True
| ├ Symmetrical Offset | [0] (-1 ~ 1) | 12/19/True
| ├ Use Accessory Position | ON | 13/19/True
| ├ **Motion** | | 14/19/True
| │ ├ Enable Motion | OFF | 0/3/False
| │ ├ **Speed** | | 1/3/False
| │ │ ├ Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 0/7/False
| │ │ ├ Moves Per Group | [8] (4 ~ 32) | 1/7/False
| │ │ ├ Phase | [0] (0 ~ 1) | 2/7/False
| │ │ ├ Curve | [0] (0 ~ 1) | 3/7/False
| │ │ ├ Variable Speed | OFF | 4/7/False
| │ │ ├ Mode | Gradual | Gradual, Random, Volume, 5/7/False
| │ │ ├ Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 6/7/False
| │ │ └ Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 7/7/False
| │ ├ Distance | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ Angle | [0] (-60 ~ 60) | 3/3/False
| ├ **Custom Pose** | | 15/19/True
| │ ├ Enable Custom Pose | OFF | 0/10/False
| │ ├ Open | [0] (-1 ~ 1) | 1/10/False
| │ ├ Thumb Axis | [90] (-360 ~ 360) | 2/10/False
| │ ├ Thumb Fold | [0] (-1 ~ 1) | 3/10/False
| │ ├ Thumb Bend | [0] (-1 ~ 1) | 4/10/False
| │ ├ Index Bend | [0] (-1 ~ 1) | 5/10/False
| │ ├ Middle Bend | [0] (-1 ~ 1) | 6/10/False
| │ ├ Ring Bend | [0] (-1 ~ 1) | 7/10/False
| │ ├ Pinky Bend | [0] (-1 ~ 1) | 8/10/False
| │ ├ Propagate | [1] (0 ~ 1) | 9/10/False
| │ └ Blend | [1] (0 ~ 1) | 10/10/False
| ├ Pose Weight | [1] (0 ~ 1) | 16/19/True
| ├ Grab Distance | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ Grab Position | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ Grab Axis | [0] (-180 ~ 180) | 19/19/True
| └ Presets | **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
| **Right Hand** | | 7/8/True
| ├ Enable Right Hand | OFF | 0/19/True
| ├ Gesture: Fist || 1/19/True
| │ Gesture | **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├ **Hand Position** | | 2/19/True
| │ ├ X | [0] (Unlimited) | 0/2/False
| │ ├ Y | [0] (Unlimited) | 1/2/False
| │ └ Z | [0] (Unlimited) | 2/2/False
| ├ **Hand Rotation** | | 3/19/True
| │ ├ X | [0] (Unlimited) | 0/2/False
| │ ├ Y | [0] (Unlimited) | 1/2/False
| │ └ Z | [0] (Unlimited) | 2/2/False
| ├ Rotation Type | Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 4/19/True
| ├ Elbow Orientation | [0] (-180 ~ 180) | 5/19/True
| ├ Mirror Left/Right | OFF | 6/19/True
| ├ Reference Actor: Self || 7/19/True
| │ Reference Actor | **Self** | Self, Partner, Closest,  |
| ├ Reference Bone: None || 8/19/True
| │ Reference Bone | **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├ IK Mode | Auto | Auto, Normal, Cylinder, Sphere, Align, 9/19/True
| ├ Side Selection | Auto | Auto, Left, Right, 10/19/True
| ├ Blend Range | [0.75] (0 ~ 2) | 11/19/True
| ├ Symmetrical Offset | [0] (-1 ~ 1) | 12/19/True
| ├ Use Accessory Position | ON | 13/19/True
| ├ **Motion** | | 14/19/True
| │ ├ Enable Motion | OFF | 0/3/False
| │ ├ **Speed** | | 1/3/False
| │ │ ├ Moves Per Beat | 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 0/7/False
| │ │ ├ Moves Per Group | [8] (4 ~ 32) | 1/7/False
| │ │ ├ Phase | [0] (0 ~ 1) | 2/7/False
| │ │ ├ Curve | [0] (0 ~ 1) | 3/7/False
| │ │ ├ Variable Speed | OFF | 4/7/False
| │ │ ├ Mode | Gradual | Gradual, Random, Volume, 5/7/False
| │ │ ├ Min Speed | 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 6/7/False
| │ │ └ Max Speed | 3/2 | 1, 3/2, 2, 3, 4, 7/7/False
| │ ├ Distance | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ Angle | [0] (-60 ~ 60) | 3/3/False
| ├ **Custom Pose** | | 15/19/True
| │ ├ Enable Custom Pose | OFF | 0/10/False
| │ ├ Open | [0] (-1 ~ 1) | 1/10/False
| │ ├ Thumb Axis | [90] (-360 ~ 360) | 2/10/False
| │ ├ Thumb Fold | [0] (-1 ~ 1) | 3/10/False
| │ ├ Thumb Bend | [0] (-1 ~ 1) | 4/10/False
| │ ├ Index Bend | [0] (-1 ~ 1) | 5/10/False
| │ ├ Middle Bend | [0] (-1 ~ 1) | 6/10/False
| │ ├ Ring Bend | [0] (-1 ~ 1) | 7/10/False
| │ ├ Pinky Bend | [0] (-1 ~ 1) | 8/10/False
| │ ├ Propagate | [1] (0 ~ 1) | 9/10/False
| │ └ Blend | [1] (0 ~ 1) | 10/10/False
| ├ Pose Weight | [1] (0 ~ 1) | 16/19/True
| ├ Grab Distance | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ Grab Position | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ Grab Axis | [0] (-180 ~ 180) | 19/19/True
| └ Presets | **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
| **Ride Model** | | 8/8/True
| ├ Enable Ride Model | ON | 0/14/False
| ├ Model: [Hoverbike] || 1/14/False
| │ Model | **[Hoverbike]** | [Hoverbike], [Rocking Horse],  |
| ├ Acceleration | [10] (0 ~ 20) | 2/14/False
| ├ Drag | [0.05] (0 ~ 1) | 3/14/False
| ├ Tilt When Turning | [0.5] (0 ~ 1) | 4/14/False
| ├ Position || 5/14/False
| ├ X | [0] (-1 ~ 1) | 6/14/False
| ├ Y | [0] (-1 ~ 1) | 7/14/False
| ├ Z | [0] (-1 ~ 1) | 8/14/False
| ├ Rotation || 9/14/False
| ├ X | [0] (-90 ~ 90) | 10/14/False
| ├ Y | [0] (-90 ~ 90) | 11/14/False
| ├ Z | [0] (-90 ~ 90) | 12/14/False
| ├ Scale | [0] (-5 ~ 5) | 13/14/False
| └ Particle Effect | ON | 14/14/False
| Presets | **Free** | Free, Rocking Motion, Hoverbike, Rocking Horse, Pole Motion, Pole Blend,  |
