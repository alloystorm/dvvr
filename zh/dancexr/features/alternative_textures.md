---
locale: zh-CN
layout: single
title: 替代纹理
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/alternative_textures) | [繁中](/tw/dancexr/features/alternative_textures) | [日本語](/jp/dancexr/features/alternative_textures) | [한국어](/kr/dancexr/features/alternative_textures) | [简中](/zh/dancexr/features/alternative_textures)


## 概述
替代纹理是一组可以替换模型默认纹理的纹理集。

### 工作原理
DanceXR会扫描模型的包或文件夹中的纹理文件，以查找与默认纹理同名的文件。如果找到，它将创建一个可能的替代纹理列表，并为用户提供选择。

当用户选择其中一种替代纹理时，新的纹理将被加载并替换模型使用的默认纹理。

### 位置
为了让DanceXR能够正确找到纹理文件，您需要将纹理文件放置在单独的文件夹中，并且文件夹的位置需要遵循以下规则：

如果模型位于zip包中，将会扫描整个包以查找替代纹理。

如果模型位于文件夹中，您需要将纹理文件放置在包含主模型文件的子文件夹中的单独文件夹中。