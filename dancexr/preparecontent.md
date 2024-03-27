---
locale: en-US
layout: single
title: Content Library
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)


## The Content Library

The content library is a folder where DanceXR locates content and stores user created settings. 

DanceXR searches for various types of content in distinct subfolders located within the content library. 

* actors: Character models 
* motion: Motion & audio files
* stages: 3D models for stage
* accessory: 3D models that can be attached to actor body parts. 
* props: 3D models that can be used for stage props. Like furnitures. 
* texture 
  * cookie: Textures for light mask
  * drawing: Saved images for body paint feature
  * ground: Ground textures
  * mask: Detail & normal maps that can be applied to models
  * particle: Textures for particle effect
  * sky: Panaramic sky maps, recommend using HDR format
* settings: All the saved settings. These files are not meant to be modified by users but you can copy and keep a backup if you prefer.
* scenes: Saved scene files. 
* bundles: Saved scene along with all the necessary assets included in a zip package.
* export: Exported model files can be found here when you use the 3D snapshot feature.
* presets: Saved preset files. You can share these files with your friendds as long as you are using the same version of DanceXR.  
* videos: Videos that can be used for projection and dynamic texture map. Supports MP4 format only.
* chat: Files used for the AI chat system. 
  * characters: Character thumbnail and templates. These are automatically generated but you can make modifications.
  * tempplates: Prompt templates, you can make modifications and create new ones.
  * history: Saved chat history
  * persona: Personality descriptions that can be applied to characters
  * voices/piper/: Custom voice models for the TTS system

## Supported formats

* 3D models: PMX, XPS and OBJ (for stage props)
* Audio: OGG and MP3 (on mobile platforms only)
* Video: MP4
* Motion: VMD, BVH
* Textures: PNG, JPG and HDR (for sky maps)

## Grouping and organization

For easier management of data files, especially for those content that requires multiple files to work together, we support using zip package to organize your files. You can also keep all the required files in a subfolder and they should work the same.

#### 3D Models

3D models usually comes with one file that describe the mesh and multiple texture files. Make sure the relative relationship of the textures and the mesh files stay the same when you move or extract files. That's important for the program to find the correct textures to use.

For PMX the mesh file is the .pmx file and for XPS the mesh file can be .xps, .mesh or .mesh.ascii. 

It is recommended to keep all the files for one model in a zip package for smaller file size and easier management.

Some models have alternative textures, DanceXR can search through the folder or zip package to find textures files that are similar to the ones used for the model and automatically include them in a menu for you to choose from. To allow this to work you need to make sure the alternative textures have the same file name of the main texture. For example if the base map is named base.png, when DanceXR finds another base.png in a different subfolder, it will automatically add it as an alternative texture. If your model is in a zip package, DanceXR will search the entire zip package for alternative textures, if your model is in a subfolder, it will search all the subfolders from where the mesh file is located. Keep this in mind since if you place your alternative textures outside of the mesh file folder, they won't be recognized.

![Example of actors folder](/images/content_actors.PNG)


#### Motion files

Typically motion data contains audio file, character motions and camera motions. In DanceXR we call a bundle of audio, character motions and camera motions a "dance set". 

To allow DanceXR to detect dance sets, you just need to keep all of these files inside a subfolder, or a zip package. But make sure that there is only one audio file in it.

For simple content that has only a motion / audio pair, you can have multiple of these in a single folder but you need to make sure the audio and motion file have the same name, for example "dance.vmd" and "dance.ogg". That allows DanceXR to know that they are a pair and create a dance set for it.

You can also have multiple unrelated motions or audios files in the same folders too. They'll just be recognized as individual motion or audio files that has no relationship with other files.

![Example of motion folder](/images/content_motion.PNG)


## Content Library Tools

After you made changes to your content library files, DanceXR should automatically detect changes and rescan the content when you launch it. 

However if that doesn't happen or you moved files when it is running, you can use the Content Library tools in the system menu to refresh it manually.

You can also point it to a different location by using the "Change Library" option.


## Google Drive Integration
DanceXR can download files from Google drive. As long as the drive folder is shared without any restriction. Simply type in the URL of your shared folder and DanceXR will be able to scan the drive folder and download the files that doesn't exist locally.


## Preparing content for Android & Oculus Quest

Android system has strict file access rules. Normally apps can't access folders withint your storage. So by default the Android and Quest version have the content library inside the app storage space which requires a PC to copy files into it.

In the latest version we are requesting the storage permission to make mangaging files a bit easier. For that you need to grant DanceXR the permission to access your storage and then you'll be able to use the system files app to move and copy files.

{% include video id="mFnXE7LBV-M" provider="youtube" %}

For older versions or if you choose to use app internal storage space, the content library is located here: /Android/data/com.vrstormlab.dancexr/files/. 

## Demo Videos

On PC:
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

Using content manager on Android
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

Loading content on Quest
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}

