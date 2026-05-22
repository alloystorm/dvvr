---
layout: feature
title: "Video Player"
locale: en-US
---

# Video Player

Controls video playback, audio sync, and aspect ratio for the loaded video file.

Allows playing MP4 (and vp8-encoded WEBM) files and projecting them from a light source or using them as a texture on wall or prop surfaces.

* **Content Location**: Place your video files in the `content/videos` folder.
* **As Projector**: In light settings, select `[video]` as the cookie map. Adjust the size of the projected image using the projection settings.
* **As Texture**: In surface settings, select `[video]` as the texture map. The default "Room" stage model contains pre-configured presets demonstrating this setup.
* **Audio Sync**: Video playback is synchronized with the main dance music timeline. If dance music is loaded, keep the video muted so it doesn't conflict. If no dance music is loaded, uncheck mute to play the video's audio track.

## Playback

**Loop** restarts the video automatically when it ends. **Mute** silences the video's audio track — useful when playing video as a background layer and relying on the main audio mix instead.

**Time Offset** shifts the playback timeline relative to the audio; use this to correct sync drift between video and music.


## Display

**Aspect Ratio** lets you match the video to the screen shape — choose from common cinema and broadcast ratios. **Fit Frame** scales the video to fit the screen while preserving aspect ratio, which may introduce letterboxing or pillarboxing depending on the mismatch. In the LW variants (Android, Quest, Mac, iOS and PC LW), this adds black bars to fit the video image in the rectangle texture (only needed when using a spotlight projection).


## Timing

Inherits timing configuration from *Base Timing* — sets BPM, beat offset, and phrase structure used to sync video-reactive effects.


## Presets

**Projector Scene Example** and **LED Screen Example** apply preconfigured ground and lighting settings optimized for a projector screen look and an LED wall look respectively.
