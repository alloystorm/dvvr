---
layout: feature
title: "Audio Visualizer"
locale: en-US
---

# Audio Visualizer

Visualizes audio spectrum data as ring overlays on the ground plane, reacting to beats in real time.


## Layout

Choose between *Horizontal*, *Vertical*, or *Circle* layout. *Circle* wraps the visualization around the performer and works best with a round stage. In *Horizontal* or *Vertical* mode, the visualization extends along the floor in one direction.


## Ring Settings

**Size** scales the overall visualization area. **Depth** controls how far the visualization extends from the center. **Ring Size** adjusts the thickness of each ring. **Data Scale** multiplies the audio amplitude — amplify a weak signal or dampen a strong one. **Color Transition** controls how smoothly colors blend between rings; lower values produce crisp, separate bands.

**Shape Shift** distorts the ring shape over time to create organic movement, while **Gap** sets the spacing between adjacent rings. **Align** offsets the rings relative to their start point — useful to fine-tune alignment with stage geometry.


## Ring Color

The ring color uses a base color with a *Glow* intensity that can pulse with the beat. Presets include *Animated Hue* (slowly cycling through the spectrum) and *Glow w/ Music* (glow synced to the music, useful for emphasis on strong beats).


## Background

An optional background layer sits behind the rings with its own color. A texture image can be applied; *Background Vibration* makes it shimmer with the audio, creating a reactive texture effect. Background is only visible when *Transparent* is disabled.


## Foreground

A foreground layer renders on top of the rings with independent color and texture control. *Foreground Scale* zooms the foreground texture; *Foreground Vibration* adds audio-reactive shimmer. The foreground's colors are multiplied by the ring color, so start with a bright foreground and tint it via the ring color. Foreground is always visible and blends with the rings below.


## Beat Clock

When *Beat Clock* is enabled, rings pulse in sync with the detected BPM rather than raw audio amplitude — producing cleaner, rhythmic animations on tracks with steady tempo. *Auto BPM* switches from the configured BPM to real-time detected tempo instead.


## Transparency

Enabling *Transparent* removes the background fill, keeping only the rings and their glow for a minimal look suited to dark stages. Shadow effects remain active regardless of this setting.


# Sub-Components

## Audio Visualizer

Holds the ring visualization layout, colors, textures, and audio-reactive settings.

### Ring Color

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

### Background Color

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

### Foreground Color

Holds a base color and glow intensity for audio-reactive elements.
Glow is multiplied with the color and animates with the beat when auto-update is enabled.

