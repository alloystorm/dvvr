---
layout: release
title: "Application Settings"
locale: en-rUS
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



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Auto Load</strong></td><td>Options</td><td>None, Last Actor, Last Scene</td><td>Last Actor</td><td></td><td></td></tr>
<tr><td><strong>Recover Tags From Save</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Attempts to recover tags from saved settings in case your content cache is rebuilt or broken</td></tr>
<tr><td><strong>Flip DDS Compressed</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Flip compressed DDS texture</td></tr>
<tr><td><strong>Flip DDS Uncompressed</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Flip uncomrpessed DDS texture</td></tr>
<tr><td><strong>Gizmo 3rd Axis</strong></td><td>Options</td><td>Rotation, Depth</td><td>Rotation</td><td></td><td></td></tr>
<tr><td><strong>Use Translated Names</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody>
</table>

