---
layout: release
title: Load Options
locale: en-US
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---



## Overview
Loader Options contains options when loading an actor model and provides management for actor cache.

### Actor Cache
Loaded actor models are cached in memory so that next time it is loaded it will be instant. Within the cache manager you can change number of cached models and delete particular models from the cache.

### Retain Options
Once turned on, when replacing actors, the settings for the outgoing actor will be kept and applied to the new actor model.

### Transition Effect
Choose and configure the animation when actor models are faded in and out. 

### Auto Actor Change
This is a special feature that automatically replace current actor on the stage with cached actors, when the value of this slider cross certain threshold. 

For example if you have 4 actors in the cache. The value of the slider and the corresponding actor will be:
* 0-0.25: Actor 1
* 0.25-0.5: Actor 2
* 0.5-0.75: Actor 3
* 0.75-1: Actor 4

A common usecase for this is to enable [Auto Update](autoupdate) and set it to timeline 0-100%. When the song is in the first 25%, the first actor will be on the stage, then when it cross the 25% mark, the system will start the transition from actor 1 to actor 2.

## Drag & drop file loading (v2026.3)
You can load model, motion, and audio files by dragging and dropping them directly into the application window, without navigating file dialogs or adding items to the content library.

**Model files**
Dropping a model file onto the application adds it as an additional actor (pro version). In the free version, it replaces the existing model in the scene. Content library items always replace by default unless you use the **+** button (pro version only).

**Motion and audio files**
Dropped motion or audio files are placed into a temporary dance set, letting you freely mix and match files without creating a permanent dance set entry. If a content-library dance set is already loaded when you drop a new file, it will be unloaded and replaced by the new temporary set.

See [VMD2PNG](dance_set#vmd2png-v20263) for information on loading VMD motion encoded as PNG images.
