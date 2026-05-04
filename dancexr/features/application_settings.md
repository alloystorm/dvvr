---
layout: feature
title: "Application Settings"
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

# Application Settings

Global application settings for startup behavior and content handling.

## Startup

**Auto Load** controls what happens when the application starts.
*None* starts with an empty stage, *Last Actor* loads the most recently
used actor model, and *Last Scene* restores the last saved scene.

## Texture Loading

**Flip DDS Compressed** and **Flip DDS Uncompressed** control whether
DDS textures are vertically flipped on load. Enable these if textures
appear upside-down — which setting you need depends on the texture
compression format.

## UI Behavior

**Gizmo 3rd Axis** changes what the mouse wheel does when using the
transform gizmo. *Rotation* spins the object along the selected axis,
while *Depth* moves the object closer or farther.

**Use Translated Names** displays content names in the localized
language when available, rather than the original filenames.

**Recover Tags From Save** attempts to restore tag data from saved
settings if the content cache is rebuilt or corrupted.

