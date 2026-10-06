---
layout: release
title: Discovery App
locale: en-US
---

# DanceXR Discovery

Discovery is a companion app for finding and installing content from DeviantArt into the DanceXR content library. It handles downloads and extraction; DanceXR then loads the installed models and other supported content.

## Windows setup

The [DanceXR Launcher](../download) included with current Windows releases can install, update or repair Discovery. If you install Discovery manually, extract it beside your DanceXR runtimes and shared `content` folder:

```
DanceXR Root Folder
├─ content
├─ DanceXR HD Pro_WIN64
├─ DanceXR RT Pro_WIN64
└─ dancexr-discovery-win32-x64
```

Keep the content folder accessible to the runtime you intend to use. Installing a model into a second, unrelated library will not make it appear in the first one. See [Content Library](../preparecontent) for supported folder and package layouts.

## First download

1. Open Discovery and authorize your DeviantArt account when prompted. The integration uses that authorization to browse content and manage favourites.
2. Choose a supported model or asset and start its download. Wait for downloading and extraction to finish before trying to load it.
3. Open DanceXR's content browser and find the installed item in the corresponding library list. If DanceXR was already open, rescan or reopen that list before downloading another copy.
4. Load one item to check its model, textures and compatibility before installing a large batch.

For Android or Quest, check the [mobile content-library setup](../content_android_quest) before moving downloaded files. Storage locations and permissions differ from the Windows shared-folder layout. [Google Drive Integration](googledrive) provides another way to synchronize a shared content folder to those devices.

## If content does not appear

Check that the download and extraction completed, that Discovery and DanceXR use the intended library, and that the package contains a supported model or motion. If a model appears but textures are missing, inspect the downloaded package and keep its texture files with the model. Authorization failures need account access corrected before retrying; reinstalling the actor in DanceXR will not repair that connection.

{% include video id="bMtgN0cNJm8" provider="youtube" %}
