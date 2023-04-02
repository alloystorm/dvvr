---
layout: single
title: Content Library
toc: true
sidebar:
  nav: "docs"
---

## The Content Library

The content library is a folder where DanceXR locates content and stores user created settings. 

DanceXR searches for various types of content in distinct subfolders located within the content library. 
* actors: Character models 
* motion: Motion & audio files
* stages: Stage models 
* accessory: Accessory models
* skys: Panoramic skymaps
* textures: Texture files for ground and built-in stages
* masks: Special textures. Used in Outfit and particle effects.


## Character models

![Example of actors folder](/images/content_actors.PNG)

As long as the dependent texture files are in the correct location relative to the PMX files, there are no specific requirements for how actor models should be placed.

For easier management, it is advisable to store all files in either zip packages or separate folders.


## Motion data

![Example of motion folder](/images/content_motion.PNG)

Although it is feasible to play a single motion file without audio or any associated camera motion, typically, motion data comes with an audio file, one or more motion files, and possibly several camera motion files as well.

It is advisable to store all files related to the motion data in a single subfolder or, preferably, in a zip package. It is also essential to avoid mixing files for other motion data and to ensure that there is only one audio file associated with the motion data. Keep in mind that only WAV and OGG audio format are supported.


## Demo Videos

On PC:
{% include video id="-2LStDN7WB8" provider="youtube" %}


Using content manager on Android
{% include video id="VQjnL9oq-hY" provider="youtube" %}


Loading content on Quest
{% include video id="ZmDeuWwZtmI" provider="youtube" %}


## Content Library Tools
There are a few tools provided in the content library menu.

* "Refresh Content": DanceXR can detect changes of the content library and perform scan automatically. However if for some reason the auto scan doesn't work, you can use this option to force a re-scan of the whole content library. 
* "Change Library": Use this to switch to a different content library on your machine. This is not available in Quest and Android versions.

## Google Drive Integration
DanceXR can download files from Google drive. As long as the drive folder is shared without any restriction. Simply type in the URL of your shared folder and DanceXR will be able to scan the drive folder and download the files that doesn't exist locally.

