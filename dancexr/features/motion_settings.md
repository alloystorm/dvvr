---
layout: single
title: Motion Settings
toc: true
---
[English](/dancexr/features/motion_settings) | [简体中文](/zh/dancexr/features/motion_settings) | [日本語](/jp/dancexr/features/motion_settings)


## Overview
Motion settings allow you to choose whether the motion is T pose or A pose, adjust motion speed and change looping options. 

## Selection
This is a list of bones and morphs this motion uses. You can use the toggles to control whether that bone or morph needs to be skipped or not. This is useful when you want to use a motion but don't want to use all the bones or morphs it uses.

## T or A pose
Motions are designed to work with models that has a specific standard pose. Traditionally this cannot be cross matched, but with DanceXR you can use any motion on any model regardless of the standard pose. All you need to do is to select the correct standard pose here in the motion settings, and the motion will be adjusted to work with the models.

## IK Controls
DanceXR determines whether the motion use IK automatically. So most of the time you can leave them as auto but if there's any issue with IK system, you can change the settings here to get the to work correctly.

## Imperfection
This is a feature that allows you to add imperfection to the motion. It will add random offsets to the motion to make it look more natural. You can adjust the amount of imperfection here.

## Apply Hip Motion To Torso
Some motion don't animate torso bones, but certain models require torso bones to be animated to look correct. This option allows you to apply hip motion to torso bones.

## Center Offset
This is workaround for certain motions that requires a particular bone configurations. The center bone of a model can be at the location of the hip or on the ground, or anywhere in between. If a motion is designed for a model with a different center bone location, you can use this option to adjust the motion to work with the model.

## Disable Curve
This controls whether to use curve for animation. If the motion is not setup correctly, disabling curve might have better result. Also disabling it can improve performance if you have many animations running at the same time.

## Loop Controls
Loop Count: How many time it loops. Use 0 for infinite.

Loop Start: The ratio of starting time vs full duration

Loop End: The ratio of end time vs full duration.

Loop Blend: When this is greater than 0, the animation will be blend between starting and end to create smooth transition between loops.

Play From Start Then Loop: When this is on, the animation will play from 0 to end and then loop from start. When this is off, the animation will loop from start to end. (start and end here are the values you set for Loop Start and Loop End)

Speed: The playback speed. By default all the motions are assumed to be 30fps. If your motion is 60fps, set this speed to 2.
