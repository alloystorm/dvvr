---
layout: release
title: "Lifelike Motions"
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

# Lifelike Motions

Adds idle behaviors that make the actor feel alive when no
animation is playing: breathing, blinking, micro-movements,
and eye contact.


## Eye Contact

When enabled, the actor looks at cameras, other actors, or
body parts within a configurable visual angle. **Look At
Camera**, **Look At Peers**, and **Look At Body** set the
relative priority of each target type. **Eye Contact Head
Turn** controls how much of the gaze is done by rotating the
head versus just the eyes (real humans turn their head about
70% of the way).

**Cartoon Eyes** reduces eye rotation amplitude for models
with oversized anime eyes so they don't roll out of the
sockets; **Cartoon Eyes Limit** sets the reduction amount.
**Stare Mode** locks onto the closest target instead of
shifting gaze naturally. **Smile Mouth** and **Smile
Eyebrow** add subtle expression while making eye contact.


## Shape Morph Eye Control

An alternative to bone-based eye rotation that uses blend
shapes (morphs) instead. Enable the toggle and assign
morphs for each gaze direction (Left Eye Left, Left Eye
Right, etc.). **Left Right Range** and **Up Down Range**
set the blend shape activation angles.


## Breathing

Simulates chest expansion during breathing by subtly
rotating the torso and neck bones. **Breath Rate** controls
the speed of the cycle.


## Micro Move

Adds tiny random rotations to the head and torso to prevent
the actor from looking completely frozen. **Extent** scales
the amplitude; **Cycle** sets the oscillation period.


## Blink

Random blinking at 2–10 second intervals. **Blink Duration**
controls how long each blink takes.

