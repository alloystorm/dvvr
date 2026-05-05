---
layout: feature
title: "Auto Reset"
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

# Auto Reset

Automatically resets bones and their children when velocity
exceeds a safe limit. Prevents physics explosions and mesh
deformation under extreme forces or teleportation.


## Threshold

Sets the velocity threshold above which physics are reset.
Lower values trigger resets more aggressively, which can
prevent clipping but may cause visible snaps during fast
movement. Higher values allow more extreme motion before
intervention.

