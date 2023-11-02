---
layout: single
title: XPS Bone Mapper
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/bone_mapper) | [繁中](/tw/dancexr/features/bone_mapper) | [日本語](/jp/dancexr/features/bone_mapper) | [한국어](/kr/dancexr/features/bone_mapper) | [简中](/zh/dancexr/features/bone_mapper)


## Overview
Bone mapping is required for XPS models to allow the animation and other features to find the correct bone.

If you have a model loaded but it stays in the standard pose, this is what you need to do to get it working.

{% include video id="g0VAfBHauXw" provider="youtube" %}

## The Mapping Status
Often the bones are mostly mapped by the program already, it's just a few that are missing. You only need to map the ones with "!" mark next to them and the model will work fine.

The statuc of bone mapping are indicated using circle icons. 
* Empty  circle means the bone is not mapped but is not critical, meaning the model should work even without that bone being mapped. 
* Circle with dot inside means the bone is already mapped. 
* Circle with exclamation mark means the bone is not mapped and is critical for the model to function.

{% include video id="jtxQo5NYk2o" provider="youtube" %}

## More Demos
Here's a video demo of converting FBX model into XPS format and then use the bone mapper to allow it to work in DanceXR
  
{% include video id="YqX_uktVvQk" provider="youtube" %}
{% include video id="BV1CF411o7P2" provider="bilibili" %}