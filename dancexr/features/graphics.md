---
locale: en-US
layout: single
title: Graphics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## Graphic Settings

### Anti-aliasing

### Super sampling DLSS, FSR

### Reflection

### Ambient Occlusion

### Global Illumination

### Depth Of Field

### Motion Blur

### Bloom

### Lens Flare

### Color Adjustment

### Color Filter

### White Balance

### Special rendering modes: Depth and Normal 
{% include video id="fKxTDq88gBk" provider="youtube" %} 

* The previous cartoon shader has been extended to include 2 more modes, depth and normal. 
* These are designed to be used with Stable Diffusion ControlNet to provide a base for your AI images. 
* A typical use case is to set up your composition and poses for the actors in DanceXR and then use Stable Diffusion to generate detailed images with totally different characters and environments. 
* Yes, you can generate depth and normal maps from any image in ControlNet, but the rendered depth and normal maps are much more accurate than the generated ones; you can test it out yourself. 
* When using the rendered depth and normal maps in ControlNet, be sure to select "none" as the preprocessor since they don't need any more processing.

### Options