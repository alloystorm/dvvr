---
layout: single
title: Sky & Cloud
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/skymap) | [繁中](/tw/dancexr/features/skymap) | [日本語](/jp/dancexr/features/skymap) | [한국어](/kr/dancexr/features/skymap) | [简中](/zh/dancexr/features/skymap)


## Sky Modes
You can choose to use sky map, pure color or procedural mode to render sky.

## On Quest and Pico
For performance reasons, on Quest and Pico devices you don't have sky map or procedural options. Sky color options are located in the lighting configurations. It has additional passthrough slider that controls the transparency of the background to allow for mixed reality.

## Passthrough on PC
Certain PC VR streaming programing allows reaplcing pure color background with passthrough image. You can set the sky to color mode and pick a color (for example pure black or green) that the streaming system uses for this to work.

## Cloud
Procedurally generate cloud that can be affected by wind and changes realistically over time. 

## Sky Map
You can use HDRI panaramic images as sky map. Both jpg and HDR formats are supported.

{% include video id="2NZpffP1X5o" provider="youtube" %}

{% include video id="vUY7DY4cCV0" provider="youtube" %}

Find skymaps and load them in DanceXR as background.

## Procedural Sky
* Sunlight angle is now controlled by time of day, ecliptic angle and orientation.
* Automatic transition between day and night based on time of day value.
* Night sky with stars
{% include video id="D745FYNcx4c" provider="youtube" %}