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


# Motion Override

## Overview
The Motion Override feature provides advanced tools to customize and enhance the motion of actors. It integrates seamlessly with the actor's rigging system, enabling precise control over body, head, hand, and leg movements. This feature is ideal for creating dynamic and synchronized animations.

## Key Features
- **Motion Presets**: Choose from a variety of motion styles, including rocking motions, ride models, and body poses.
- **Audio-Driven Motion**: Synchronize animations with audio beats for immersive experiences.
- **Body Pose Adjustments**: Control lean, height, forward/backward position, and rotation.
- **Ride Models**: Integrate ride models like hoverbikes or rocking horses with configurable properties such as acceleration and drag.
- **Rocking Motion Simulation**: Simulate rocking motions with adjustable depth, angle, and feet motion.
- **Symmetric Hand Poses**: Enable or disable symmetric hand movements.
- **Dynamic Leg Motion**: Adjust leg motion dynamically based on presets and configurations.
- **Particle Effects**: Add particle effects to enhance visual feedback during motion.
- **Customizable Configurations**: Fine-tune various parameters to achieve the desired motion effects.

## Example Use Cases
- **Limit Movements of a Dance Motion**: Use the Motion Override feature to restrict certain movements of a dance motion, ensuring that the actor's performance remains within desired limits.
    - Set position and rotation locks to control the actor's movement range.
    - Adjust the lean and height to create a more grounded appearance.
    - Optionally apply arms and legs poses to suit your needs.
- **Create a Rocking Horse Animation**: Utilize the rocking motion simulation to create a rocking horse animation.
    - Select the Rocking Horse preset from the motion presets.
    - Adjust the rocking angle and depth to achieve the desired rocking effect.
    - Choose the appropriate ride model to match the rocking horse theme.
- **Turning dance into vehecle motion**: Transform a dance animation into a vehicle-like motion.
    - Enable the ride model and configure the acceleration and drag settings.
    - Adjust the body pose to create a more dynamic and engaging performance.
    - Use the rocking motion simulation to add depth and realism to the animation.
    - Optionally, add particle effects to enhance the visual impact of the motion.



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Body</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Position</nobr>| Free | Free, Lock Horizontal, Lock Vertical, Lock Position, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Rotation</nobr>| Free | Free, Lock Rotation, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Damping</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Lean</nobr>| [0] (-45 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Bend</nobr>| [0] (-150 ~ 150) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Twist</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Head</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Height</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Forward / Back</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Distance</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Target Actor</nobr>|  |  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Detect Range</nobr>| [2] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Min Distance</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Distance</nobr>| [1] (0.5 ~ 2) | 
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Rocking Motion</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Speed</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Moves Per Beat</nobr>| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Moves Per Group</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Phase</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Variable Speed</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Gradual | Gradual, Random, Volume, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Min Speed</nobr>| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Max Speed</nobr>| 3/2 | 1, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rocking Angle</nobr>| [30] (0 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Up / Down</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Front / Back</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth Change</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth Max</nobr>| [0.15] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Depth Extra</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Feet Motion</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Head Pose</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotatoin X</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotatoin Y</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rotatoin Z</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Leg Pose</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Relative To Floor</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Twist</nobr>| [60] (0 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Symmetrical</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Left</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Open</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Toe</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Right</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Open</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Foot Rotate Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Toe</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Ride** | Sit, Ride, Kneel, Stand,  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Hands Symmetrical</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Left Hand</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Gesture</nobr>| **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Hand Position</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Hand Rotation</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Rotation Type</nobr>| Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Elbow Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Mirror Left/Right</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Reference Actor</nobr>| **Self** | Self, Partner, Closest,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Reference Bone</nobr>| **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> IK Mode</nobr>| Auto | Auto, Normal, Cylinder, Sphere, Align, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Side Selection</nobr>| Auto | Auto, Left, Right, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend Range</nobr>| [0.75] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Symmetrical Offset</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Accessory Position</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Motion</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Speed</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Moves Per Beat</nobr>| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Moves Per Group</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Phase</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Variable Speed</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Gradual | Gradual, Random, Volume, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Min Speed</nobr>| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Max Speed</nobr>| 3/2 | 1, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle</nobr>| [0] (-60 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Custom Pose</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Open</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Axis</nobr>| [90] (-360 ~ 360) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Fold</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Index Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Middle Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ring Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Pinky Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Propagate</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Pose Weight</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Distance</nobr>| [0.015] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Position</nobr>| [-0.05] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Axis</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Right Hand</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Gesture</nobr>| **Fist** | Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Hand Position</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Hand Rotation</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Rotation Type</nobr>| Relative to Reference Bone | Relative to Reference Bone, Relative to Self, Absolute Rotation, No Rotation, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Elbow Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Mirror Left/Right</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Reference Actor</nobr>| **Self** | Self, Partner, Closest,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Reference Bone</nobr>| **None** | None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> IK Mode</nobr>| Auto | Auto, Normal, Cylinder, Sphere, Align, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Side Selection</nobr>| Auto | Auto, Left, Right, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend Range</nobr>| [0.75] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Symmetrical Offset</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Accessory Position</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Motion</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Speed</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Moves Per Beat</nobr>| 1 | 1/4, 1/3, 1/2, 2/3, 1, 4/3, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Moves Per Group</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Phase</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Curve</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Variable Speed</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Gradual | Gradual, Random, Volume, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Min Speed</nobr>| 1/2 | 1/4, 1/3, 1/2, 2/3, 1, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Max Speed</nobr>| 3/2 | 1, 3/2, 2, 3, 4, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle</nobr>| [0] (-60 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Custom Pose</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Open</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Axis</nobr>| [90] (-360 ~ 360) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Fold</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Thumb Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Index Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Middle Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ring Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Pinky Bend</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Propagate</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blend</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Pose Weight</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Distance</nobr>| [0.015] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Position</nobr>| [-0.05] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Grab Axis</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Rest** | Rest, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, chest, Preset 1, Preset 2, Preset 3,  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Ride Model</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Model</nobr>| **[Hoverbike]** | [Hoverbike], [Rocking Horse],  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Acceleration</nobr>| [10] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Drag</nobr>| [0.05] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Tilt When Turning</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>Position</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>Rotation</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Scale</nobr>| [0] (-5 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Particle Effect</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Free** | Free, Rocking Motion, Hoverbike, Rocking Horse, Pole Motion, Pole Blend,  |
