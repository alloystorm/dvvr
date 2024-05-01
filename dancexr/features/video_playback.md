---
locale: en-US
layout: single
title: Video Playback
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/video_playback) | [繁中](/tw/dancexr/features/video_playback) | [日本語](/jp/dancexr/features/video_playback) | [한국어](/kr/dancexr/features/video_playback) | [简中](/zh/dancexr/features/video_playback)


Video playback allows you to play a video and have the image projected from a light source or used as a texture on wall or prop surfaces in your scene. Currently, only MP4 format is supported. (It will also recognise WEBM files in the folder but keep in mind that only vp8 encoding is supported. If you try to load a webm file but nothing happens, that means the encoding of that file is not supported.)

* Content location: place your video files in MP4 format in the `content/videos` folder.
* Use as projector: Go to light settings and select [video] as the cookie map. There are other settings to control the size of projected images. Use newly included presets to see how they work.
* Use as texture: In the surface settings and select [video] as the texture map. The included "Room" stage model has several presets for you to see how they work.

Video playback is synchronized with the dance music (if there is dance music loaded) and is controlled by the same playback and timeline control.

When you have a music loaded in your scene, make sure to select the "mute" option for the video so that the music from the video does not interfere with the dance music. 

You can also play the video without dance music. In this case, uncheck the "mute" option and the audio will come out from the same audio source and you can use the volume control to adjust the volume of the video audio. 

When you use the video image for projection or texture, make sure you have the correct aspect ratio selected. Since internally the image are stored in a rectangular texture and needs to be scaled back to the correct aspect ratio when projected or placed on object. 

In the LW variants (Android, Quest, Mac, iOS and PC LW), there's a "Fit Frame" option that will place the images with black bars to fit the rectangle aspect ratio. Only use this mode when you want to use a spotlight to project the image.

## Settings

* Loop: Loop the video when the audio is longer than the video.
* Mute: Mute the audio of the video. 
* Time Offset: Sync the video timeline with the dance music.
* Aspect Ratio: Select the aspect ratio of the video. This needs to be set correctly for the video image to be displayed properly.
* Fit Frame: Adds black bars to fit the video image in the rectangle texture. This is only needed when you use a spotlight to project the image in the LW versions.
* Projector Scene Example: Load the procedural stage in the projector preset and switch to "Projector" preset to projector the video on the wall.
* LED Screen Example: Load the procedural stage with the LED screen. 
* Timing settings: BPM, time offset, etc. Configure the timing for the video if you want to use the audio from the video with the procedural motions.
* Load Video: Select a video from your content library to play.