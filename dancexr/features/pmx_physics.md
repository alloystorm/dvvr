---
locale: en-US
layout: single
title: PMX Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/pmx_physics) | [繁中](/tw/dancexr/features/pmx_physics) | [日本語](/jp/dancexr/features/pmx_physics) | [한국어](/kr/dancexr/features/pmx_physics) | [简中](/zh/dancexr/features/pmx_physics)


## PMX Model physics settings

* Use XPS Tools: Enable this option if you want to use the XPS tools to adjust the physics settings. This will disable the built-in physics settings and use the XPS tools instead.
* Reduce Constraints: This uses a simplified physics model that reduces the number of constraints to improve stability and smoothness. Previously named "Experimental Setup".
* Linear Motion: Configures parameters for linear motion of joints.
* Angular Motion: Configures parameters for angular motion of joints.
* Options: Configures rigidbody parameters like mass, drag, and center of mass.
* Auto Reset Threshold: If the velocity of the bone exceeds the threshold value, it will be reset to its original position. This can prevent the explosion of the physics simulation.

## Groups

Joints and colliders are automatically grouped based on how they are connected together.

For each group, a separate setting is available to fine-tune the physics simulation for different body parts.

The number of groups varies depending on the model, and the program does not know which group is for which body part. So we added a label configuration for each group to help you label the group for your convenience.

## Group Settings

* Visualize joints: Toggle to show the joints in the group.
* Visualize colliders: Toggle to show the colliders in the group.
* Override Configs: Toggle to override physics settings for the group. Once enabled, the following configs will appear.
* Parent-child Linear: Configures linear motion settings for parent-child joints.
* Parent-child Angular: Configures angular motion settings for parent-child joints.
* Lateral Linear: Configures linear motion settings for lateral joints.
* Lateral Angular: Configures angular motion settings for lateral joints.

## Linear / Angular Motion Settings

For each of the linear and angular motion settings mentioned above, the following options are available:

* Firmness: Overall multiplier applied to the spring force of all joints.
* Main Drive Force: Spring force for linear and angular movements on the main axis.
* Second Drive Force: Spring force for linear and angular movements on the secondary axis.
* Target Position: The neutral position for the joint.
* Lock When Possible: Lock the joint based on the PMX definition of the joint.
* Acceleration Mode: Use acceleration mode that ignores the mass of the object.
* Damping: Damping of the spring force.
* Drag: Drag of the object.

## XPS Tools

If you turn on the "Use XPS Tools" option, the physics components defined in the PMX model will all be disabled, and you can then use the XPS tools to adjust the physics settings.

* [Body Colliders](xps_body_colliders.md)
* [Boobs Physics](xps_boobs.md)
* [Hair Physics](xps_hair.md)
* [Clothes Physics](xps_cloth.md)
* [Skirt Physics](xps_skirt.md)
* [Softbody Physics](xps_softbody.md)
* [Detach Object](xps_detech.md)