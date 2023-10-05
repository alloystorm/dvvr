---
layout: single
title: Content Library
toc: true
sidebar:
  nav: "docs"
---
[English](/dancexr/preparecontent) | [简体中文](/zh/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent)


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


## Preparing content for Android & Oculus Quest

Similar to the PC versions, DanceXR requires a content folder to be prepared so it knows where to find all the models, motions & textures. However on Android, apps can only access specific folders unless a special permission is granted. Therefore on Android and Oculus Quest platforms you will not be able to select content folder like on PC. The content needs to be at a specific location. 

### If you can connect your device to a PC

It's still easier to use a PC to manage your content on the device. It's just copy & paste files within your Windows "File Explorer". Before you copy content from your PC, it is recommended to zip the content individually for easier manage and reduce storage space. 

* Install DanceXR on the device
* Connect your device to your PC. Select "File Transfer" from the popup dialog or from system settings. 
* Now open File Explorer and you should be able to see your device.
* Navigate to /Android/data/com.vrstormlab.dancexr/files/. If you don't see that folder, make sure DanceXR is installed, and if you still cannot find it after install, let us know and we'll try our best to figure that out.
* Copy your entire content folder into that directory. So your content folder structure will be like ![example folder](/images/content_folder_android.png)

Then you should be able to see your content next time you run DanceXR on the device

### If you don't have access to a PC (Android version only)

The Android version comes with a Content Manager app that can help you organize your content on the device. You should be able to see it from your apps drawer or desktop after installing DanceXR. It has the same icon as DanceXR player but is titled "Content Manager". Content Manager app supports only zip, png and jpg format. 

Once you open it, you'll see your content folders and browse through the files they contain. You can click on the files to either move them elsewhere or [set zip file encodings](features/zip_format). 

Content Manager app also set itself as a destination when you open or share a file of the supported file type (zip, png or jpg). 

* If you download zip from your browser. Once downloaded, tap on the downloaded file and you should see the DanceXR icon with "Add to library", select that one and you can then select where to save that file into, and it will then be copied to the content library.
* You can also use File Manager app to browse through your phone and then select "Open with" from the menu and you'll be able to see the DanceXR "Add to library" option as well.

This is just the first version of Content Manager, we'll continue to add more features to it along the way. 

