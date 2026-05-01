---
layout: release
title: Weather Particles
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


## Overview
Weather particles add atmospheric particle effects to the scene to simulate environmental conditions such as rain, snow, or falling leaves. Built-in presets are available: **Off**, **Dust**, **Rain**, **Snow**, **Petal**, **Leaf**, **Glitter**.

## Particle settings

* **Spawn Rate** (0–2): Controls the density of particles. Higher values produce more particles.
* **Gravity**: Controls how strongly particles fall. Negative values cause particles to fall downward.
* **Velocity**: Sets the initial velocity of particles when spawned.
* **Turbulence**: Applies random movement to particles, creating a more natural appearance.
* **Drag**: Air resistance applied to particles, slowing them as they travel.
* **Bounce**: Controls how much particles bounce when they hit the ground or scene objects.
* **Spin**: Rotation speed of individual particles.
* **Collision**: When enabled, particles collide with scene objects rather than passing through them.
* **Spawn from top**: When enabled, particles spawn from the top of the spawn area. When disabled, particles spawn randomly throughout the volume.
* **Texture**: Selects the particle texture or type to use.
* **Size**: Controls the size of each particle.
* **Lifetime**: Sets how long each particle remains visible before disappearing.
* **Height**: Sets the height of the particle spawn area.
* **Stay on Ground** (0+): How long particles remain on the ground after landing. A value of 0 causes them to disappear on contact.

## Rain shader
The rain shader applies a screen-space effect that simulates rain droplets forming on the camera lens, adding an extra layer of immersion during rain weather.

## Audio
Controls the volume of weather audio, such as rain sounds or ambient environmental noise.
