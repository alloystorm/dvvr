---
layout: release
title: Dance Set
locale: en-US
---



## Overview
A dance set is a collection of audio actor motions and camera motions if available. 

A dance set can have any number of motions, with or without audio. 

In the content library, if you have a folder that contains 1 audio file and 1 or more actor motions, these data will automatically gruped into a dance set.

## Loading Dance Set
Usually the dance set will have the same file name as the audio file it has. When you load a dance set from the content menu, the audio and all the motions will be loaded as well.

## Dance Set Settings
Dance Set have individual [settings for each motion](motion_settings), and a common [Timing & Beats](music_timing) settings for all the motions.

## [Remix](remix)
Remix in DanceXR means using motion data from one dance set with the audio from another dance set. With this feature, you can adapt motions for different audio. And it will automatically adjust speed to match the motion and music.

## VMD2PNG (v2026.3)
[VMD2PNG](https://github.com/alloystorm/vmd2png) is an open-source tool that encodes VMD motion data into a PNG image file, offering a smaller file size, easy sharing, and a visual representation of the motion data.

DanceXR 2026.3 supports loading motion from VMD2PNG files. You can load them by dragging and dropping the PNG file into the application window, or by placing the PNG files in your content library alongside other motion files.
