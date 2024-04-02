---
locale: en-US
layout: single
title: Softbody Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/xps_softbody) | [繁中](/tw/dancexr/features/xps_softbody) | [日本語](/jp/dancexr/features/xps_softbody) | [한국어](/kr/dancexr/features/xps_softbody) | [简中](/zh/dancexr/features/xps_softbody)


## Softbody Physics

Softbody physics creates an interconnected mesh of joints between a group of bones to simulate softbody physics. Unlike skirt physics, which has a clear hierarchy from root to tip, this is more like a flat relationship between all the bones.

This works best for buttocks and thigh physics.

The softbody mode in [boobs physics](xps_boobs.md) uses the same mechanism.

## Settings

* Select Bones: Select the bones that are related to the softbody.
* Physics Properties: Mass, drag, collider radius, friction, center of mass, and solver iteration count for the joints.
* Parent Joint: Adjust joint configurations for parent-child joints.
* Inter-Joint: Adjust joint configurations for joints between bones.
* Visualize: Visualize the created joints.
* Apply To Other Groups: Use the same settings for other groups of bones.
* Additional Groups: Set the number of additional groups that you need.
* Group N: Configure additional groups.