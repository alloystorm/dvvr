---
layout: release
title: "./motion/proc/auto_cam"
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

# ./motion/proc/auto_cam

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



## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Predict position of the target to reduce lag caused by smoothing</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Distance Near</strong></td><td>Float</td><td>0.5 – 3</td><td>1.5</td><td></td><td>Minimum distance of the camera from the target.</td></tr>
<tr><td><strong>Distance Far</strong></td><td>Float</td><td>0.5 – 3</td><td>2.5</td><td></td><td>Maximum distance of the camera from the target.</td></tr>
<tr><td><strong>Use Actor Orientation</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>Enable or disable alignment of the camera to the actor's orientation.</td></tr>
<tr><td><strong>Seed</strong></td><td>Float</td><td></td><td>1234</td><td></td><td>Seed value for generating random camera motions.</td></tr>
<tr><td><strong>Fade To Black</strong></td><td>Float</td><td>0 – 0.25</td><td>0</td><td></td><td>Duration of the fade-to-black effect during transitions.</td></tr>
<tr><td><strong>F2B Probability</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Probability of triggering the fade-to-black effect.</td></tr>
<tr><td><strong>Audio Sensitivity</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>Sensitivity of the camera motion to audio levels.</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Target Selection</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Head</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Probability of targeting the actor's head.</td></tr>
<tr><td><strong>Chest</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Probability of targeting the actor's chest.</td></tr>
<tr><td><strong>Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Probability of targeting the actor's center.</td></tr>
<tr><td><strong>Legs</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>Probability of targeting the actor's legs.</td></tr>
<tr><td><strong>Feet</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Probability of targeting the actor's feet.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Distance Selection</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Close Up</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Probability of a close-up camera distance.</td></tr>
<tr><td><strong>Zoom In</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of zooming in.</td></tr>
<tr><td><strong>Zoom Out</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of zooming out.</td></tr>
<tr><td><strong>Middle</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of a middle-range camera distance.</td></tr>
<tr><td><strong>Far</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of a far camera distance.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Path Selection</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>High Angle</strong></td><td>Float</td><td>0 – 30</td><td>20</td><td></td><td>Maximum upward angle for the camera.</td></tr>
<tr><td><strong>Low Angle</strong></td><td>Float</td><td>-30 – 0</td><td>-20</td><td></td><td>Maximum downward angle for the camera.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Orientation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Front Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>Probability of orienting the camera to the front center of the actor.</td></tr>
<tr><td><strong>Front 45</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Probability of orienting the camera to a 45-degree angle in front of the actor.</td></tr>
<tr><td><strong>Side 90</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of orienting the camera to the actor's side at a 90-degree angle.</td></tr>
<tr><td><strong>Back 135</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>Probability of orienting the camera to a 135-degree angle behind the actor.</td></tr>
<tr><td><strong>Back 180</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Probability of orienting the camera directly behind the actor.</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>

