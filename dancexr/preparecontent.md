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

The content library is a folder where DanceXR locates content and stores user-created settings.


## Locating the content library

**Windows**: On Windows, you can locate the content library by clicking on the "Show in Explorer" item from within the "Content Library" section in the system menu (the gear icon on the bottom left).

**Android**: After the 2024.3 update, the content folder is located at /DanceXR/ in your storage. If you are using an older version, it is located at /Android/data/com.vrstormlab.dancexr/files/.

**iPhone and iPad**: You can find the content library in the "On My iPhone" or "On My iPad" section in the Files app. DanceXR creates a folder called "DanceXR" in the root directory of your device.

**Oculus Quest**: The content library is located at /DanceXR/ in your storage after 2024.3 and for older versions at /Android/data/com.vrstormlab.dancexr/files/. Similar to the Android version.


## Folder Structure

DanceXR searches for various types of content in distinct subfolders located within the content library.

* actors: Character models
* motion: Motion & audio files
* stages: 3D models for the stage
* accessory: 3D models that can be attached to actor body parts.
* props: 3D models that can be used for stage props, like furniture.
* texture
  * cookie: Textures for light mask
  * drawing: Saved images for [body paint feature](features/outfit_body_paint.md)
  * ground: Ground textures
  * mask: [Detail & normal maps](features/custom_detail_map.md) that can be applied to models
  * particle: Textures for [particle effect](features/particles.md)
  * sky: [Panoramic sky maps](features/skymap.md), recommend using HDR format
* settings: All the saved settings. These files are not meant to be modified by users, but you can copy and keep a backup if you prefer.
* scenes: [Saved scene](features/save_scene.md) files.
* bundles: [Saved scene along with all the necessary assets](features/scene_bundle.md) included in a zip package.
* export: Exported model files can be found here when you use the 3D snapshot feature.
* presets: Saved preset files. You can share these files with your friends as long as you are using the same version of DanceXR.
* videos: Videos that can be used for [projection and dynamic texture map](features/video_playback.md). Supports MP4 format only.
* chat: Files used for the [AI chat system](ai_chat.md).
  * characters: Character thumbnails and templates. These are automatically generated, but you can make modifications.
  * templates: Prompt templates, you can make modifications and create new ones.
  * history: Saved chat history
  * persona: Personality descriptions that can be applied to characters
  * voices/piper/: Custom voice models for the TTS system

## Supported formats

* 3D models: PMX, XPS, and OBJ (for stage props)
* Audio: OGG and MP3 (on mobile platforms only)
* Video: MP4
* Motion: VMD, BVH
* Textures: PNG, JPG, and HDR (for sky maps)

## Grouping and organization

For easier management of data files, especially for that content that requires multiple files to work together, we support using a zip package to organize your files. You can also keep all the required files in a subfolder, and they should work the same.

### 3D Models<a id="3d-models"></a>

3D models usually come with one file that describes the mesh and multiple texture files. Make sure the relative relationship of the textures and the mesh files stays the same when you move or extract files. That's important for the program to find the correct textures to use.

For PMX, the mesh file is the .pmx file, and for XPS, the mesh file can be .xps, .mesh, or .mesh.ascii.

It is recommended to keep all the files for one model in a zip package for a smaller file size and easier management.

Some models have [alternative textures](features/alternative_textures.md). DanceXR can search through the folder or zip package to find texture files that are similar to the ones used for the model and automatically include them in a menu for you to choose from. To allow this to work, you need to make sure the alternative textures have the same file name as the main texture. For example, if the base map is named base.png, when DanceXR finds another base.png in a different subfolder, it will automatically add it as an alternative texture. If your model is in a zip package, DanceXR will search the entire zip package for alternative textures. If your model is in a subfolder, it will search all the subfolders from where the mesh file is located. Keep this in mind since if you place your alternative textures outside of the mesh file folder, they won't be recognized.

![Example of actors folder](/images/content_actors.PNG)

### Motion files<a id="motion-files"></a>

Typically, motion data contains an audio file, character motions, and camera motions. In DanceXR, we call a bundle of audio, character motions, and camera motions a "dance set".

To allow DanceXR to detect dance sets, you just need to keep all of these files inside a subfolder or a zip package. But make sure that there is only one audio file in it.

For simple content that has only a motion/audio pair, you can have multiple of these in a single folder, but you need to make sure the audio and motion file have the same name, for example, "dance.vmd" and "dance.ogg". That allows DanceXR to know that they are a pair and create a dance set for it.

You can also have multiple unrelated motions or audio files in the same folders too. They'll just be recognized as individual motion or audio files that have no relationship with other files.

![Example of motion folder](/images/content_motion.PNG)


## Content Library Tools

After you made changes to your content library files, DanceXR should automatically detect changes and rescan the content when you launch it.

However, if that doesn't happen or you moved files when it is running, you can use the Content Library tools in the system menu to refresh it manually.

You can also point it to a different location by using the "Change Library" option.

## Google Drive Integration

DanceXR can [download files from Google Drive](features/googledrive.md). As long as the drive folder is shared without any restriction. Simply type in the URL of your shared folder, and DanceXR will be able to scan the drive folder and download the files that don't exist locally.

## Preparing content for Android & Oculus Quest

The Android system has strict file access rules. Normally, apps can't access folders within your storage. So by default, the Android and Quest version have the content library inside the app storage space, which requires a PC to copy files into it.

From version 2024.3, we are using the storage permission to make managing files a bit easier. For that, you need to grant DanceXR the permission to access your storage, and then you'll be able to use the system files app to move and copy files.

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