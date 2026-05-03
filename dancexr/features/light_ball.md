---
layout: release
title: "Light Ball"
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

# Light Ball

Spawns physics-driven glowing orbs attached to actor bones.
**Shape** selects Ball, Diamond, or Crystal mesh. **Size**
scales the orbs. Toggle attachment points: **Hands**,
**Hip**, and **Torso**.

The **Style** panel controls appearance with presets
(Glow, Reflective, Crystal), color, gloss, glow, metallic,
intensity, refraction, shadow, and trail. Use **Stage
Color** to sync with scene lighting or **Flashing With
Beats** for audio-reactive pulsing.

The **Physics** panel configures spring joint behavior with
presets (Spring, Hanging, Floating), gravity, collision,
mass, distance, spring force, damping, and speed limits.

# Sub-Components

## Style

Nested config for light ball appearance. Presets: **Glow**
(emissive), **Reflective** (metallic), **Crystal**
(refractive). **Use Stage Color** syncs with scene
lighting. **Flashing With Beats** pulses intensity to
audio. Controls **Color**, **Gloss**, **Glow**, **Radius**,
**Metallic**, **Intensity**, **Refraction**, **Cast
Shadow**, and **Trail** length.

## Physics

Nested config for light ball physics behavior. Presets:
**Spring** (no gravity/collision), **Hanging** (gravity +
collision), **Floating** (no gravity/collision). **Gravity**
enables downward force. **Collision** enables physics
collisions. **Mass**, **Distance**, **Spring Force**, and
**Damping** configure the spring joint. **Min/Max Speed**
clamp velocity.

