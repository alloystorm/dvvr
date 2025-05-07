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



[Feature Page](/dancexr/features/motion_override)

| Setting | Value | Description |
| :--- | --- | :--- |
|  □ Enable| [OFF] | 
|  ⚙️ <b>Body</b>| | 
| ├─ ☑ Position| Free | Free, Lock Horizontal, Lock Vertical, Lock Position, 
| ├─ ☑ Rotation| Free | Free, Lock Rotation, 
| ├─ ⊖ Damping| [0.5] (0 ~ 1) | 
| ├─ ⊖ Lean| [0] (-45 ~ 90) | 
| ├─ ⊖ Bend| [0] (-150 ~ 150) | 
| ├─ ⊖ Twist| [0] (-90 ~ 90) | 
| ├─ ⊖ Head| [0] (-90 ~ 90) | 
| ├─ ⊖ Height| [0] (-1 ~ 1) | 
| ├─ ⊖ Forward / Back| [0] (-1 ~ 1) | 
| ├─ □ Distance| [OFF] | 
| ├─ > Target Actor|  |  |
| ├─ ⊖ Detect Range| [2] (0 ~ 10) | 
| ├─ ⊖ Min Distance| [0.5] (0 ~ 1) | 
| └─ ⊖ Max Distance| [1] (0.5 ~ 2) | 
|  ☑ <b>Rocking Motion</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ ⚙️ <b>Speed</b>| | 
| │ ├─ ☑ Moves Per Beat| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │ ├─ ⊖ Moves Per Group| [8] (4 ~ 32) | 
| │ ├─ ⊖ Phase| [0] (0 ~ 1) | 
| │ ├─ ⊖ Curve| [0] (0 ~ 1) | 
| │ ├─ □ Variable Speed| [OFF] | 
| │ ├─ ☑ Mode| Gradual | Gradual, Random, Volume, 
| │ ├─ ☑ Min Speed| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │ └─ ☑ Max Speed| 3/2 | 1, 3/2, 2, 3, 4, 
| ├─ ⊖ Rocking Angle| [30] (0 ~ 60) | 
| ├─ ⊖ Up / Down| [0.1] (0 ~ 0.3) | 
| ├─ ⊖ Front / Back| [0.1] (0 ~ 0.3) | 
| ├─ ⊖ Depth Change| [0.1] (0 ~ 0.3) | 
| ├─ ⊖ Depth Max| [0.15] (0 ~ 0.3) | 
| ├─ ⊖ Depth Extra| [0] (-0.1 ~ 0.1) | 
| └─ ⊖ Feet Motion| [0] (-1 ~ 1) | 
|  □ <b>Head Pose</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ ⊖ Rotatoin X| [0] (-90 ~ 90) | 
| ├─ ⊖ Rotatoin Y| [0] (-90 ~ 90) | 
| └─ ⊖ Rotatoin Z| [0] (-90 ~ 90) | 
|  ☑ <b>Leg Pose</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ ☑ Relative To Floor| [ON] | 
| ├─ ⊖ Max Twist| [60] (0 ~ 90) | 
| ├─ ☑ Symmetrical| [ON] | 
| ├─ ⚙️ <b>Left</b>| | 
| │ ├─ ⊖ Open| [0] (-90 ~ 90) | 
| │ ├─ ⊖ Foot X| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Y| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Z| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate X| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate Y| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate Z| [0] (Unlimited) | 
| │ └─ ⊖ Toe| [0] (-180 ~ 180) | 
| ├─ ⚙️ <b>Right</b>| | 
| │ ├─ ⊖ Open| [0] (-90 ~ 90) | 
| │ ├─ ⊖ Foot X| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Y| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Z| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate X| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate Y| [0] (Unlimited) | 
| │ ├─ ⊖ Foot Rotate Z| [0] (Unlimited) | 
| │ └─ ⊖ Toe| [0] (-180 ~ 180) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Ride** | Sit, Ride, Kneel, Stand,  |
|  ☑ Hands Symmetrical| [ON] | 
|  □ <b>Left Hand</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ > Gesture| **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├─ ⚙️ <b>Hand Position</b>| | 
| │ ├─ ⊖ X| [0] (Unlimited) | 
| │ ├─ ⊖ Y| [0] (Unlimited) | 
| │ └─ ⊖ Z| [0] (Unlimited) | 
| ├─ ⚙️ <b>Hand Rotation</b>| | 
| │ ├─ ⊖ X| [0] (Unlimited) | 
| │ ├─ ⊖ Y| [0] (Unlimited) | 
| │ └─ ⊖ Z| [0] (Unlimited) | 
| ├─ ☑ Rotation Type| Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
| ├─ ⊖ Elbow Orientation| [0] (-180 ~ 180) | 
| ├─ □ Mirror Left/Right| [OFF] | 
| ├─ > Reference Actor| **Self** | Self, Partner, Closest,  |
| ├─ > Reference Bone| **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├─ ☑ IK Mode| Auto | Auto, Normal, Cylinder, Sphere, Align, 
| ├─ ☑ Side Selection| Auto | Auto, Left, Right, 
| ├─ ⊖ Blend Range| [0.75] (0 ~ 2) | 
| ├─ ⊖ Symmetrical Offset| [0] (-1 ~ 1) | 
| ├─ ☑ Use Accessory Position| [ON] | 
| ├─ □ <b>Motion</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⚙️ <b>Speed</b>| | 
| │ │ ├─ ☑ Moves Per Beat| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │ │ ├─ ⊖ Moves Per Group| [8] (4 ~ 32) | 
| │ │ ├─ ⊖ Phase| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ Curve| [0] (0 ~ 1) | 
| │ │ ├─ □ Variable Speed| [OFF] | 
| │ │ ├─ ☑ Mode| Gradual | Gradual, Random, Volume, 
| │ │ ├─ ☑ Min Speed| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │ │ └─ ☑ Max Speed| 3/2 | 1, 3/2, 2, 3, 4, 
| │ ├─ ⊖ Distance| [0.1] (0 ~ 0.3) | 
| │ └─ ⊖ Angle| [0] (-60 ~ 60) | 
| ├─ □ <b>Custom Pose</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⊖ Open| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Thumb Axis| [90] (-360 ~ 360) | 
| │ ├─ ⊖ Thumb Fold| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Thumb Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Index Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Middle Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Ring Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Pinky Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Propagate| [1] (0 ~ 1) | 
| │ └─ ⊖ Blend| [1] (0 ~ 1) | 
| ├─ ⊖ Pose Weight| [1] (0 ~ 1) | 
| ├─ ⊖ Grab Distance| [0.015] (-0.1 ~ 0.1) | 
| ├─ ⊖ Grab Position| [-0.05] (-0.1 ~ 0.1) | 
| ├─ ⊖ Grab Axis| [0] (-180 ~ 180) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
|  □ <b>Right Hand</b>| | 
| ├─ □ Enable| [OFF] | 
| ├─ > Gesture| **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
| ├─ ⚙️ <b>Hand Position</b>| | 
| │ ├─ ⊖ X| [0] (Unlimited) | 
| │ ├─ ⊖ Y| [0] (Unlimited) | 
| │ └─ ⊖ Z| [0] (Unlimited) | 
| ├─ ⚙️ <b>Hand Rotation</b>| | 
| │ ├─ ⊖ X| [0] (Unlimited) | 
| │ ├─ ⊖ Y| [0] (Unlimited) | 
| │ └─ ⊖ Z| [0] (Unlimited) | 
| ├─ ☑ Rotation Type| Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
| ├─ ⊖ Elbow Orientation| [0] (-180 ~ 180) | 
| ├─ □ Mirror Left/Right| [OFF] | 
| ├─ > Reference Actor| **Self** | Self, Partner, Closest,  |
| ├─ > Reference Bone| **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
| ├─ ☑ IK Mode| Auto | Auto, Normal, Cylinder, Sphere, Align, 
| ├─ ☑ Side Selection| Auto | Auto, Left, Right, 
| ├─ ⊖ Blend Range| [0.75] (0 ~ 2) | 
| ├─ ⊖ Symmetrical Offset| [0] (-1 ~ 1) | 
| ├─ ☑ Use Accessory Position| [ON] | 
| ├─ □ <b>Motion</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⚙️ <b>Speed</b>| | 
| │ │ ├─ ☑ Moves Per Beat| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
| │ │ ├─ ⊖ Moves Per Group| [8] (4 ~ 32) | 
| │ │ ├─ ⊖ Phase| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ Curve| [0] (0 ~ 1) | 
| │ │ ├─ □ Variable Speed| [OFF] | 
| │ │ ├─ ☑ Mode| Gradual | Gradual, Random, Volume, 
| │ │ ├─ ☑ Min Speed| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
| │ │ └─ ☑ Max Speed| 3/2 | 1, 3/2, 2, 3, 4, 
| │ ├─ ⊖ Distance| [0.1] (0 ~ 0.3) | 
| │ └─ ⊖ Angle| [0] (-60 ~ 60) | 
| ├─ □ <b>Custom Pose</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─ ⊖ Open| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Thumb Axis| [90] (-360 ~ 360) | 
| │ ├─ ⊖ Thumb Fold| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Thumb Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Index Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Middle Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Ring Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Pinky Bend| [0] (-1 ~ 1) | 
| │ ├─ ⊖ Propagate| [1] (0 ~ 1) | 
| │ └─ ⊖ Blend| [1] (0 ~ 1) | 
| ├─ ⊖ Pose Weight| [1] (0 ~ 1) | 
| ├─ ⊖ Grab Distance| [0.015] (-0.1 ~ 0.1) | 
| ├─ ⊖ Grab Position| [-0.05] (-0.1 ~ 0.1) | 
| ├─ ⊖ Grab Axis| [0] (-180 ~ 180) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
|  ☑ <b>Ride Model</b>| | 
| ├─ ☑ Enable| [ON] | 
| ├─ > Model| **[Hoverbike]** | [Hoverbike], [Rocking Horse],  |
| ├─ ⊖ Acceleration| [10] (0 ~ 20) | 
| ├─ ⊖ Drag| [0.05] (0 ~ 1) | 
| ├─ ⊖ Tilt When Turning| [0.5] (0 ~ 1) | 
| ├─ <b>Position</b>|| 
| ├─ ⊖ X| [0] (-1 ~ 1) | 
| ├─ ⊖ Y| [0] (-1 ~ 1) | 
| ├─ ⊖ Z| [0] (-1 ~ 1) | 
| ├─ <b>Rotation</b>|| 
| ├─ ⊖ X| [0] (-90 ~ 90) | 
| ├─ ⊖ Y| [0] (-90 ~ 90) | 
| ├─ ⊖ Z| [0] (-90 ~ 90) | 
| ├─ ⊖ Scale| [0] (-5 ~ 5) | 
| └─ ☑ Particle Effect| [ON] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Free** | Free, Rocking Motion, Hoverbike, Rocking Horse, Pole Motion, Pole Blend,  |
