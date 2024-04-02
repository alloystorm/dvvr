---
locale: en-US
layout: single
title: Skirt Physics
toc: true
sidebar:
  nav: "docs"
---

## Skirt Physics

Skirt physics creates a inter-connected mesh of joints for the selected bones to simulate fabric physics.

## Settings

* Select Bones: Select the bones that are related to the skirt.
* Sorting: Select the sorting method that determine the order of the bones in the skirt. This is important because the bones needs to be connected in the correct order to allow the physics to work correctly.
* Closed Loop: If the skirt is a closed loop, enable this option to connect the last bone to the first bone. For skirt that has multiple pieces, disable this and use the additional groups option below for other pieces. 
* Visualize: Visualize the created joints.
* Skip First X Bones: This allows you to skip the first x number of bones when creating the joints. This is useful when there are too many bones to select individually.
* Physics Properties: Mass, drag, collider radius, friction, center of mass and solver iteration count for the joints. 
* Parent Joint: Adjust joint configurations for parent-child joints.
* Inter-Joint: Adjust joint configurations for joints between bones.
* Anchor Position: Adjust the anchor position for the joints.
* Apply To Other Groups: Use the same settings for other groups of bones.
* Additional Groups: Set the number of additional groups that you need. 
* Group N: If the skirt has multiple pieces, you can use this to create joints for the other pieces. For each of the group, you can select different set of bones. 