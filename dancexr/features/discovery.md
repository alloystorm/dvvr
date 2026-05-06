---
layout: release
title: Discovery App
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

## DanceXR Discovery App

Easily Expand Your DanceXR Library with Seamless Asset Management

Introducing a powerful companion tool for DanceXR that simplifies the way you discover and use new content. Fully integrated with DeviantArt, this tool automatically handles the downloading, extraction, and installation of models and other assets directly into your DanceXR content library. No more manual setup—just browse, click, and enjoy.

Available for free on both **Windows desktop** and **Android**, it's the easiest way to enhance your DanceXR experience with fresh, high-quality content.

{% include video id="bMtgN0cNJm8" provider="youtube" %}

## How It Works

The Discovery App connects to your DeviantArt account and scans your favourites and watched artists for DanceXR-compatible content. When it finds models, poses, scenes, or other assets, it presents them in a browsable, filterable gallery directly on your device.

Once you select something you want to add, the app handles the entire pipeline:

1. **Downloads** the file from DeviantArt
2. **Extracts** it from any archive format (ZIP, RAR, 7z)
3. **Installs** it into the correct folder inside your DanceXR content directory
4. The content is immediately available in DanceXR—no import steps, no file shuffling

This eliminates the traditional workflow of manually downloading archives, finding the right extraction tool, figuring out where files should go, and then verifying everything landed correctly.

## Installation

To install DanceXR Discovery, simply extract or place the tool inside your DanceXR root folder. Your folder structure should look like this:

```
DanceXR Root Folder
├─ content
├─ DanceXR HD Pro_WIN64
├─ DanceXR RT Pro_WIN64
├─ [other DanceXR versions]
└─ dancexr-discovery-win32-x64
```

The app detects the `content` folder automatically and uses it as the installation target. If you have a non-standard setup (e.g., a symlink to content on a different drive), it should still work as long as the path resolves correctly.

### Android Setup

The Android version follows the same principle—place it on your device, point it at your DanceXR content directory, and it handles the rest. The mobile interface is optimised for touch-based browsing, making it convenient to queue up downloads while on the go.

## DeviantArt Authorization

You need a DeviantArt account to use the Discovery App. The tool requests permission to:

- **Browse your favourites** — Finds models and assets you've already bookmarked
- **Manage favourites on your behalf** — Lets you favourite content directly from the app's browser

When you first launch Discovery, it will redirect you to DeviantArt's OAuth authorization page. This is a standard, secure flow—the app never sees your DeviantArt password. Once authorized, it can pull content lists and download assets without further login prompts.

### Revoking Access

You can revoke the app's access at any time from your DeviantArt account settings under "Authorized Applications." This will not affect any content already downloaded to your library.

## Browsing Tips

- **Filter by category** — The Discovery App can sort by model, pose, scene, and other asset types, so you're not scrolling through unrelated content.
- **Preview before downloading** — Each asset shows a preview image and description, so you know what you're getting.
- **Queue multiple downloads** — Add several items to a download queue and let the app process them sequentially. This is especially handy for bulk-librating a new collection.
- **Check the version** — The app auto-updates to stay compatible with DeviantArt's API. If you run into connectivity issues, make sure you're on the latest release.

## Why Use Discovery?

The manual approach to building a DanceXR library works, but it's tedious: find content, download, extract, figure out folder structure, move files, test, repeat. The Discovery App compresses all of that into a single action. For anyone who regularly adds new content, or who has a large DeviantArt favourites collection they'd like to pull into DanceXR, it's a significant time saver.

It also reduces errors—misplaced folders are the most common cause of "content not showing up in DanceXR," and the Discovery App eliminates that problem entirely by installing files to the correct locations automatically.

Demo video: https://youtu.be/bMtgN0cNJm8
