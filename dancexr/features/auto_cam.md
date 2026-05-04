---
layout: release
title: "[Auto Cam]"
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

# [Auto Cam]

Automatic camera system that generates cinematic camera movements synced to music beats and actor actions.

## Distance

**Distance Near** and **Distance Far** define the range the camera can be from its target.
Narrower ranges keep the camera at a consistent distance, while wider ranges add more
variety between shots. The actual distance is also influenced by the *Distance Selection*
probabilities below.

## Target Selection

Controls which body part the camera focuses on. Each value is a relative probability —
higher numbers make that target more likely to be chosen. **Head** and **Chest** work
well for close-ups, while **Center** and **Legs** suit wider shots. Set a value to *0*
to exclude that target entirely.

## Distance Selection

Probabilities for how far the camera positions itself. **Close Up** fills the frame
with the actor, **Zoom In** and **Zoom Out** transition between distances during a shot,
**Middle** gives a balanced view, and **Far** captures the full scene. Only the
relative ratios matter — the final distance is clamped by the *Distance* range above.

## Path & Angles

**High Angle** and **Low Angle** limit how far the camera can tilt up or down. Lower
values keep the camera more level for a neutral look; wider ranges introduce dramatic
overhead or worm's-eye perspectives.

## Orientation

Determines which side of the actor the camera frames. **Front Center** faces the actor
directly, **Front 45** and **Side 90** show the actor in profile, and **Back 180**
shoots from behind. Mix these to keep the camera movement visually interesting.

## Effects

**Fade To Black** sets how long the screen fades to black during shot transitions,
and **F2B Probability** controls how often this happens. Use these to add cinematic
cuts between shots.

**Audio Sensitivity** makes camera motion respond to music volume when enabled.
Higher values speed up camera movements during loud passages.

## Random Seed

The **Seed** value controls the random number generator for camera motion. Change it
to get a different camera sequence while keeping all other settings the same, or set
it to *-1* for a new random seed each time.

