---
layout: single
title: Transparent Materials
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/transparency) | [繁中](/tw/dancexr/features/transparency) | [日本](/jp/dancexr/features/transparency) | [한국어](/kr/dancexr/features/transparency) | [简中](/zh/dancexr/features/transparency)


## Transparent Materials

There are two main aspects of the transparent material issue:

* Determining whether a material is transparent or opaque.
* The rendering order of transparent materials.


### Determining Transparency/Opaque Materials

XPS model data includes the material's properties, which we can use to determine whether to use a transparent mode. Therefore, XPS models usually do not have misjudgment cases.

PMX models do not provide such data, so we currently mainly use two methods:
* Infer whether the material is transparent by the properties of the texture. If the texture contains an alpha channel, the material is judged to be transparent. However, there are exceptions, such as some materials that use the alpha channel as a smooth value rather than transparency.
* Infer through the name. For example, if the name contains words like "shadow" or "hair," it is judged to be transparent.

Therefore, PMX models may have a certain percentage of misjudgment cases.


### Rendering Order of Transparent Materials

Most XPS models include data on the rendering order, so there are usually no major issues.

Some PMX models' materials do not have a reasonable rendering order, which can cause strange screens to appear after layering.

### Transparent Depth Prepass (HD)
By default, the HD and RT versions will turn on transparent depth prepass mode. In this mode, all transparent materials will undergo a depth prepass pass, using the z-buffer to determine the layering relationship of the materials to ensure that the top layer of transparent materials is rendered correctly. This approach can solve the layering problem, but the downside is that it will discard all underlying materials. If the model requires multiple layers to be displayed simultaneously, problems may arise. For example, hair and transparent clothing or when the character is obscured by other transparent objects. This mode can be turned off in the system settings.

Starting from version 1.4.3, independent fine-tuning depth prepass settings can be set for each individual material:

* Transparent prepass switch: Each material can independently control whether to use depth prepass.
* Transparent prepass threshold: In the case of using depth prepass, this parameter can be used to control the depth prepass area. The larger the value, the smaller the depth prepass range. The default setting is 0.8.


### Transparent Material Settings

In each individual material option, you can change the material's transparency mode, which can be set to automatic, force transparency, or force opacity.

In the hair options, you can change the transparency mode of all hair materials.

In the Global Material Settings, you can choose the transparency sorting order from a few different options.
