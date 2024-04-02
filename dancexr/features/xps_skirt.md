---
locale: en-US
layout: single
title: Skirt Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/xps_skirt) | [繁中](/tw/dancexr/features/xps_skirt) | [日本語](/jp/dancexr/features/xps_skirt) | [한국어](/kr/dancexr/features/xps_skirt) | [简中](/zh/dancexr/features/xps_skirt)


## Skirt Physics

Skirt physics creates an interconnected mesh of joints for the selected bones to simulate fabric physics.

## Settings

* Select Bones: Select the bones that are related to the skirt.
* Sorting: Select the sorting method that determines the order of the bones in the skirt. This is important because the bones need to be connected in the correct order to allow the physics to work correctly.
* Closed Loop: If the skirt is a closed loop, enable this option to connect the last bone to the first bone. For a skirt that has multiple pieces, disable this and use the additional groups option below for other pieces.
* Visualize: Visualize the created joints.
* Skip First X Bones: This allows you to skip the first x number of bones when creating the joints. This is useful when there are too many bones to select individually.
* Physics Properties: Mass, drag, collider radius, friction, center of mass, and solver iteration count for the joints.
* Parent Joint: Adjust joint configurations for parent-child joints.
* Inter-Joint: Adjust joint configurations for joints between bones.
* Anchor Position: Adjust the anchor position for the joints.
* Apply To Other Groups: Use the same settings for other groups of bones.
* Additional Groups: Set the number of additional groups that you need.
* Group N: If the skirt has multiple pieces, you can use this to create joints for the other pieces. For each of the groups, you can select a different set of bones.