---
layout: feature
title: "Particle Effect"
locale: en-US
---

# Particle Effect

Weather particles add atmospheric particle effects to the scene to simulate environmental conditions such as rain, snow, or falling leaves. Built-in presets are available: *Off*, *Dust*, *Rain*, *Snow*, *Petal*, *Leaf*, *Glitter*.

{% include video id="SLNw5XZflZ8" provider="youtube" %}


## Particle settings

**Spawn Rate** (0 to 2) controls the density of particles. Higher values produce more particles.

**Gravity** controls how strongly particles fall. Negative values cause particles to fall downward.

**Velocity** sets the initial velocity of particles when spawned.

**Turbulence** applies random movement to particles, creating a more natural appearance.

**Drag** is the air resistance applied to particles, slowing them as they travel.

**Bounce** controls how much particles bounce when they hit the ground or scene objects.

**Spin** controls the rotation speed of individual particles.

**Collision** enables or disables particle collision with scene objects.

**Spawn from top** spawns particles from the top of the spawn area when enabled, or randomly throughout the volume when disabled.

**Texture** selects the particle texture or type to use.

**Size** controls the size of each particle.

**Lifetime** sets how long each particle remains visible before disappearing.

**Height** sets the height of the particle spawn area.

**Stay on Ground** (0+) controls how long particles remain on the ground after landing. A value of 0 causes them to disappear on contact.


## Rain shader

The rain shader applies a screen-space effect that simulates rain droplets forming on the camera lens, adding an extra layer of immersion during rain weather.


## Audio

Controls the volume of weather audio, such as rain sounds or ambient environmental noise.

