---
layout: feature
title: "Lifelike Motions"
locale: en-US
---

# Lifelike Motions

Adds subtle behaviors over the actor's current pose or motion: breathing, blinking, micro-movements,
and eye contact.


## Eye Contact {#eye-contact}

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


These effects need a compatible eye, eyelid and torso rig. If
eye bones are unavailable, configure **Shape Morph Eye Control**
with appropriate morphs instead. Test with **Stare Mode** off and
change one target priority at a time.

{% include video id="zP966sQ6h0g" provider="youtube" %}

## Shape Morph Eye Control {#shape-morph-eye-control}

An alternative to bone-based eye rotation that uses blend
shapes (morphs) instead. Enable the toggle and assign
morphs for each gaze direction (Left Eye Left, Left Eye
Right, etc.). **Left Right Range** and **Up Down Range**
set the blend shape activation angles.


## Breathing {#breathing}

Simulates chest expansion during breathing by subtly
rotating the torso and neck bones. **Breath Rate** controls
the speed of the cycle.


## Micro Move {#micro-move}

Adds tiny random rotations to the head and torso to prevent
the actor from looking completely frozen. **Extent** scales
the amplitude; **Cycle** sets the oscillation period.


## Blink {#blink}

Random blinking at 2–10 second intervals. **Blink Duration**
controls how long each blink takes.

