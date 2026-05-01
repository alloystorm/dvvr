---
layout: release
title: Sky Settings
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
Sky settings control the appearance of the sky backdrop, ambient lighting, wind, and volumetric clouds in the scene.

## Sky mode
Choose between three sky rendering modes:

* **Color**: Renders a flat solid-color sky. Ambient lighting is derived from the ambient color settings (Sky, Horizon, and Ground colors).
* **Sky Map**: Uses an HDRI or texture as the sky backdrop. An orientation slider lets you rotate the sky map, and sky exposure controls overall brightness.
* **Procedural**: Generates a dynamic sky with atmosphere simulation, including a simulated sun position and realistic sky gradient.

## Sky map
Select the sky texture to use when Sky Map mode is active.

## Orientation
Rotates the sky map horizontally (0–360°). Only available in Sky Map mode.

## Background brightness (HDRP only)
Controls the rendered sky brightness in the scene.

## Ambient influence (HDRP only)
Controls how much the sky contributes to ambient lighting in the scene.

## Ambient colors
Three color channels that define the ambient light contribution:
* **Sky**: Color of light coming from above.
* **Horizon**: Color of light coming from the horizon.
* **Ground**: Color of light reflected from below.

## Wind
Global wind settings that affect cloth simulation, particles, and clouds.

* **Wind Speed** (0–4): Controls the global wind speed.
* **Wind Direction** (0–360°): Controls the global wind direction in degrees.

### Wind field
An optional localized wind field that applies wind within a defined area.

* **Position**: The 3D position of the wind field volume.
* **Rotation**: The rotation of the wind field volume.
* **Radius**: The radius of the wind field area.
* **Distance**: The effective distance of the wind force.
* **Speed**: The wind speed within the field.

## Volumetric clouds (HDRP only)
Enables volumetric cloud rendering in the sky.

* **Shape Scale**: Scale of the large cloud formations.
* **Shape Factor**: How much the large-scale shape influences cloud density.
* **Erosion Scale**: Scale of fine-detail erosion applied to clouds.
* **Erosion Factor**: How strongly the erosion detail is applied.
* **Density**: Overall density of the cloud layer.
* **Shadow**: Controls cloud shadow casting strength.
* **Wind Multiplier**: How much the global wind affects cloud movement.

## Presets
Built-in sky presets to quickly configure common environments: **Skymap**, **Procedural**, **Indoor**, **Thin Cloud**, **Cloudy** (HDRP only).
