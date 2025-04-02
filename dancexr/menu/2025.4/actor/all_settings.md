---
locale: en-rUS
layout: single
title: Settings
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/actor/all_settings) | [繁中](/tw/dancexr/menu/2025.4/actor/all_settings) | [日本語](/jp/dancexr/menu/2025.4/actor/all_settings) | [한국어](/kr/dancexr/menu/2025.4/actor/all_settings) | [简中](/zh/dancexr/menu/2025.4/actor/all_settings)

# Settings



| Setting | Value | Description |
| :--- | --- | :--- |
| Settings || 
|**Facial Control** | | 
| Mouth || 
| Use Lip Sync | OFF | 
| Eyebrows || 
| Eyelids || 
|
|**Scale & Offset** | | 
|- Model Scale | [0] (-3 ~ 3) | 
|- Ground Offset | [0] (-2 ~ 2) | 
| Uniform Height | ON | Set the default scale to average human size
|- Rotation | [0] (-180 ~ 180) | 
|- Offset X | [0] (-5 ~ 5) | 
|- Offset Z | [0] (-5 ~ 5) | 
|- Snapping | **0**, 0.1, 0.2, 0.5, 1, 2,  | 
| Presets | **Uniform Life Size**, Miniature, Giant, Original,  |  |
|
|**Lifelike Motions** | | 
| Eye Contact | ON | Enable eye contact, look at and turn head towards camera or other models when they are in visual range
| Stare Mode | OFF | Constantly looking at the closest target in range.
|- Look At Camera | [1] (0 ~ 1) | Priority of cameras as gaze target
|- Look At Peers | [0.5] (0 ~ 1) | Priority of other models as gaze target
|- Look At Body | [0.5] (0 ~ 1) | Priority of certain body parts as gaze target
|- Eye Contact Angle | [80] (0 ~ 180) | Angle of visual range, only objects within this angle can be gaze target
|- Eye Contact Head Turn | [0.7] (0 ~ 1) | Ratio of head turn when looking at target
| Cartoon Eyes | ON | Reduce eye rotation, useful for models with big cartoon eyes
|- Cartoon Eyes Limit | [0.4] (0 ~ 1) | How much rotation reduction in cartoon eyes mode
|- Smile Mouth | [1] (0 ~ 1) | 
|- Smile Eyebrow | [0.5] (0 ~ 1) | 
| Random Target | ON | 
| Blink | ON | Automatically blink eyes at random interval
| Breathing | ON | Breathing motion
|- Breath Rate | [0.3] (0 ~ 1) | 
| Micro Move | OFF | Add micro movements
|- Micro Move Extent | [0.25] (0 ~ 1) | 
|- Micro Move Cycle | [3] (1 ~ 10) | 
|
|**Troubleshooting** | | 
| Apply Body Rotation To Center | OFF | Apply rotation of hip and torso to the center bone
| Twist Correction | OFF | Reduce twisting of arms & legs at joints
|- Upper Arm Twist | [0] (0 ~ 1) | 
|- Lower Arm Twist | [0] (0 ~ 1) | 
|- Lower Arm Mode | From Upper Arm, **From Hand**,  | 
|- Leg Twist | [0] (0 ~ 1) | 
|- Clear Arm Twist | [0] (0 ~ 1) | 
|- Elbow Axis | [0] (-180 ~ 180) | Rotation axis of the elbow joints
| Ignore Diffuse Color | OFF | 
|- Hand Scale | [1] (0 ~ 1) | Set scale of the hands
|- BVH Thumb Motion | [0.5] (0 ~ 1) | Reduce thumb motion for BVH motions
|- Limit Neck Rotation | [0] (0 ~ 1) | Reduce rotation of neck bone
|- Limit Head Rotation | [0] (0 ~ 1) | Reduce rotation of head bone
| Reset Transition | OFF | When resetting physics, perform a transition from standard pose to the animated pose to allow physics components to settle properly.
|- Leg Pose During Reset | [30] (0 ~ 45) | 
| Skip Kinematic Updates | OFF | Not updating kinematic bones that are not animated.
|
|**Water Interaction**<sup>[PRO]</sup> | | 
| Ripple | OFF | 
|- Intensity | [1] (0 ~ 2) | 
|- Body | [1] (0.1 ~ 2) | 
|- Hands | [0.5] (0.1 ~ 2) | 
|- Feet | [0.5] (0.1 ~ 2) | 
| Water Drop || 
|- Sweat Drops | [0] (0 ~ 1) | 
|- Water Drop Glow | [5] (0 ~ 20) | 
|- Water Drop Gravity | [3] (0 ~ 10) | 
|- Drag | [2.5] (0 ~ 10) | 
|- Metallic | [0.25] (0 ~ 1) | 
|- Alpha | [0.25] (0 ~ 1) | 
|- Size | [0.003] (0 ~ 0.01) | 
|- Duration | [5] (0 ~ 10) | 
| Sweat Collision | OFF | 
|
|**Visualize Bones** | | 
| Enable Visualize Bones | OFF | 
| Virtual Bones | ON | 
| Bones | OFF | 
| IK | OFF | 
| Ragdoll | OFF | 
|
|**Motion Passes** | | 
| Reset Bones | ON | 
| Animation | ON | 
| Offset | ON | 
| IK | ON | 
| Virtual Bones | ON | 
| Morph Post Update | ON | 
| Inherit Bones | ON | 
| Post Transform | ON | 
| Post IK | ON | 
| Final Update | ON | 
|
