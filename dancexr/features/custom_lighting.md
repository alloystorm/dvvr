---
locale: en-US
layout: single
title: Custom Lighting
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/custom_lighting) | [繁中](/tw/dancexr/features/custom_lighting) | [日本語](/jp/dancexr/features/custom_lighting) | [한국어](/kr/dancexr/features/custom_lighting) | [简中](/zh/dancexr/features/custom_lighting)

## Overview
Custom lighting lets you configure the scene's lighting including the main directional light (sun or moon), up to three additional light groups, fog, global scene brightness, and light allocation controls.

## Celestial (sunlight)
The main directional light that simulates sunlight or moonlight.

* **Color**: The color of the directional light.
* **Intensity**: The brightness of the directional light.
* **Angle / Direction**: Controls the direction from which the light arrives, simulating sun position.
* **Shadow**: Enables or disables shadow casting from the directional light, with strength and softness controls.

## Light groups
Up to three independent light groups can be configured. Each group functions as a point or spot light source.

* **Color**: The color of the light.
* **Intensity**: The brightness of the light.
* **Range**: How far the light reaches.
* **Position**: The 3D position of the light in the scene.

## Fog
Enables atmospheric fog in the scene.

* **Enable**: Toggles fog on or off.
* **Color**: The color of the fog.
* **Density**: Controls how thick the fog appears.
* **Start**: The distance from the camera at which fog begins.
* **End**: The distance at which fog reaches full opacity.

## Global dim
A global brightness multiplier that scales the overall scene illumination. Use this to darken or brighten the scene uniformly.

## Light limits
Sets the maximum number of dynamic lights that are processed simultaneously. Lowering this value can improve performance.

## Light allocation
Controls how lights are distributed between actors and the rest of the scene, allowing you to prioritize lighting on characters or the environment.
