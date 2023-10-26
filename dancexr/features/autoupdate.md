---
layout: single
title: Auto Update
toc: true
sidebar:
  nav: "docs"
---
[English](/dancexr/features/autoupdate) | [简体中文](/zh/dancexr/features/autoupdate) | [日本語](/jp/dancexr/features/autoupdate)


## Overview
Auto Update is an amazing that allows you to animate configuration changes based on various data sources like timeline, audio spectrum, custom input, etc.

It can be used on many different types of configurations. Including position, rotation, scale, and even color and opacity.

## Auto Update Settings
Configuration for auto update includes:
* Mode: This is the data source for the auto update. It can be timeline, audio spectrum, custom input, etc.
* Input From: The start value of the input
* Input To: The end value of the input
* Value From: The start value of the output
* Value To: The end value of the output
* Curve: This is the curve that defines how the value changes over time. You can use the curve editor to edit the curve.
* Cycle Time: This is the time it takes for the value to go from Input From to Input To. This is useful when you want to repeat the animation.
* Phase: This is the time offset for the animation. For example if you have 2 auto update with the same cycle time, but one has phase 0 and the other has phase 0.5, then the 2 animations will be out of phase by half a cycle.
* Band: When using audio spectrum, this controls which band of the spectrum to use.

The calculation is done as follows:

output = (value_to - value_from) * (input_value - input_from) / (input_to - input_from) + value_from

Please note that the input_value is always clamped between input_from and input_to, so the output will never go out of the range of value_from and value_to.

For example, for a configuration that is ranged from 0 to 1, when the mode is set to timeline, "Input From" is 20, "Input To" is 80, "Value From" is 40, "Value To" is 60.
* When the timeline is at 20%, the output will be 1 * 40% = 0.4
* When the timeline is below 20%, the output will also be 0.4, since it is clamped.
* When the timeline is at 80%, the output will be 1 * 60% = 0.6
* When the timeline goes above 80%, the output will also be 0.6, since it is clamped.
* When the timeline is at 50%, the output will be 1 * ((0.6 - 0.4) * (50% - 20%) / (80% - 20%) + 0.4) = 0.5

## Audio Data Sources
{% include video id="A00DhbCOgu0" provider="youtube" %}
{% include video id="BV1cm4y1t74d" provider="bilibili" %}

* Audio Amplitude mode allows changing the config value based on currently audio output level. 
    * You can choose smoothing settings to fine tune the output according to your need. 
    * Higher smooth setting generates smooth output while lower smooth setting allows faster response.
* Spectrum Band mode gets output from the audio spectrum data. 
* It is divided into 1024 bands. In the order of frequency. 
* Lower band number represents bass and vice versa.

## Auto Update Values
All active Auto Update values are shown in the "Auto Update Values" list under "Scene" menu. Here you can quickly see the current value of each auto update and also edit the configurations.
