---
layout: release
title: Getting Started
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

# Getting Started with DanceXR

Welcome! This guide will walk you through your first experience with DanceXR — from downloading the app to loading a model and playing a motion. If you're new to 3D character viewers, don't worry: we'll keep it simple.

---

## 1. Download and Install

DanceXR is available on **PC (Windows/Mac)**, **Android**, **iOS**, and **Meta Quest**. Visit the download page to get the right version for your platform:

[**Download DanceXR →**](/dancexr/download)

Here's a quick overview of what's available:

| Platform | Recommended Build |
|----------|-----------------|
| **Windows PC** | Choose **HD** for balanced quality, **RT** for ray tracing, or **LW** for performance |
| **Mac** | **HD** build |
| **Android** | **LW** build — available on Google Play or Itch.io |
| **iOS** | App Store |
| **Meta Quest** | Standalone build — available on Itch.io |

**Installation tips:**

- **Windows:** Extract the downloaded `.7z` archive to any folder, then run `DanceXR.exe`.
- **Mac:** Mount the `.dmg` and drag DanceXR to your Applications folder.
- **Android / Quest:** Install the APK from your download source.
- **iOS:** Install directly from the App Store.

> If you run into any issues at launch, check the [Support page](/dancexr/support) for common fixes.

---

## 2. Find Your Content Library

DanceXR looks for models, motions, and other content inside a **content library** folder. This is where you'll copy your PMX and XPS model files.

The location depends on your platform:

- **Windows:** Open DanceXR, click the gear icon (system menu) on the bottom left, then select "Show in Explorer" under Content Library.
- **Mac / iOS:** Look for a "DanceXR" folder in your device's Files app.
- **Android / Quest:** After the 2024.3 update, the folder is at `/DanceXR/` on your storage. For older versions, it's at `/Android/data/com.vrstormlab.dancexr/files/`.

For a full breakdown of the folder structure and supported formats, see the [Content Library guide](/dancexr/preparecontent).

---

## 3. Drop in a Model

DanceXR supports **PMX** (MMD) and **XPS** (XNALara) models — the two most common formats for anime and game character models.

Here's how to get a model loaded:

1. **Find a model** — PMX models are widely available from sites like DeviantArt, Booth.pm, and Nico Nico. XPS models are common on DeviantArt and other 3D model communities.
2. **Copy the files** — Place the model file (`.pmx`, `.xps`, `.mesh`, or `.mesh.ascii`) along with its texture files into the `actors` subfolder inside your content library.
3. **Zip it (recommended)** — For easier management, zip the model and all its textures into a single `.zip` file. DanceXR reads models inside zip packages just fine.
4. **Launch DanceXR** — The model should appear in the actor picker. Select it and it loads automatically with all its materials, physics, and textures applied.

![Example of actors folder](/images/content_actors.PNG)

> **Tip:** The first time you load a model, DanceXR may take a moment to scan your content library. After that, new files are detected automatically.

---

## 4. Load a VMD Motion

Once your model is on stage, it's time to make it dance.

1. **Get a motion file** — VMD (Vocaloid Motion Data) files are the most common format. They're usually shared alongside an audio file.
2. **Copy to the `motion` folder** — Place the `.vmd` file (and optionally its `.ogg` or `.mp3` audio file) in the `motion` subfolder of your content library.
3. **Keep audio and motion paired** — If a motion file and an audio file have the same name (e.g., `dance.vmd` and `dance.ogg`), DanceXR automatically groups them as a "dance set." Put multiple pairs in subfolders or zip packages for the cleanest experience.
4. **Select the motion** — In DanceXR, open the **motion picker** (the music note icon). You'll see all available motions and dance sets. Click one to apply it.

The model's bones will automatically adapt to the motion — no manual fixing required. DanceXR handles T-pose, A-pose, and most common bone structure differences on the fly.

For more details on organizing motion files, see the [Content Library guide](/dancexr/preparecontent#motion-files).

---

## 5. Basic Controls

Once you have a model loaded and a motion playing, here's how to navigate the scene:

| Control | Action |
|---------|--------|
| **Drag with mouse** (or touch) | Orbit the camera around the actor |
| **Scroll wheel** | Zoom in and out |
| **Right-click drag** | Pan the camera |
| **Spacebar** | Play / Pause the current motion |
| **Number keys 1–4** | Quick actions: 1 = Center Actor, 2 = Next Model, 3 = Next Motion, 4 = Play/Pause |
| **W / A / S / D** | Move the camera (when not in orbit mode) |

A full control reference is available on the [Controls page](/dancexr/features/controls), including gamepad and VR controller mappings.

---

## What's Next?

You're up and running! Now dive into what DanceXR can really do:

- **[Features Overview](/dancexr/features)** — Browse every feature and tool in DanceXR
- **[Prepare Your Content Library](/dancexr/preparecontent)** — Detailed guide on organizing models, motions, stages, and more
- **[Physics](/dancexr/features/physics)** — Cloth simulation, hair physics, soft body, and ragdoll
- **[Dressing System](/dancexr/features/optionals)** — Change outfits, materials, and accessories
- **[Cameras](/dancexr/features/camera_settings)** — Orbit cam, freefly, auto cam, first-person, and more
- **[AI Chat](/dancexr/features/ai_chat)** — Talk to your characters with voice and text
- **[Creator Edition](/dancexr/creator)** — Offline 4K / VR rendering for content creators
- **[Troubleshooting](/dancexr/troubleshooting)** — Fix common issues
- **[Support & FAQ](/dancexr/support)** — Frequently asked questions

Happy dancing!
