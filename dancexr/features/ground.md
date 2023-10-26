---
layout: single
title: Ground
toc: true
sidebar:
  nav: "docs"
---
[English](/dancexr/features/ground) | [简体中文](/zh/dancexr/features/ground) | [日本語](/jp/dancexr/features/ground)


## Ground Modes
You can use either a textured surface or the sky map for your ground. 

### Sky Map As Ground
When using sky map for ground, the sky map is projected on to the ground surface. It is recommended to use a sky map that don't have close up details. Because the sky map don't have three-dimentional information, when being projected on to a 3D surface the distortion is very obvious if it has close up objects. 

### Custom Ground Textures
You can put texture images in texture/ground folder of your content library to allow them to appear in the texture list for ground.

## Procedural Stage
{% include video id="K3WSqEj7K-4" provider="youtube" %}
{% include video id="BV1F3411d7gn" provider="bilibili" %}

Procedural Stage provides adjustable simple geometry to use as stage. With it you can
* Easily change the width and depth of the stage
* Raise it up or lower it down, even digging holes into the ground.
* Extensions on all 4 sides. For example you can use this to easily create a fashion show runway.
* Physics interaction. It has physics colliders that conforms to the shape of the stage. So other physics objects can interact with it correctly.

## Water System
For HD and RT version, a water system is available to create realistic visual of swimming pool, reiver or ocean. When using the swimming pool mode, you can use the procedural stage to dig a hole in the ground for the pool. It also works with custom stage models.

Use the provided presets as example to see how the parameters affect the final result.

## Demo
{% include video id="kOrp7rESrXQ" provider="youtube" %}
