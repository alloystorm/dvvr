---
locale: zh-CN
layout: single
title: 地面
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/ground) | [繁中](/tw/dancexr/features/ground) | [日本語](/jp/dancexr/features/ground) | [한국어](/kr/dancexr/features/ground) | [简中](/zh/dancexr/features/ground)


## 地面模式
您可以使用纹理表面或天空地图作为地面。

### 天空地图作为地面
当使用天空地图作为地面时，天空地图会投射到地面上。建议使用没有近距离细节的天空地图。因为天空地图没有三维信息，当投射到三维表面上时，如果有近距离的物体，畸变会非常明显。

### 自定义地面纹理
您可以将纹理图像放在内容库的texture/ground文件夹中，以使它们出现在地面纹理列表中。

## 过程化舞台
{% include video id="K3WSqEj7K-4" provider="youtube" %}
{% include video id="BV1F3411d7gn" provider="bilibili" %}

过程化舞台提供可调节的简单几何形状作为舞台。您可以：
* 轻松更改舞台的宽度和深度
* 提高或降低舞台的高度，甚至在地面上挖洞
* 四边都可以扩展。例如，您可以使用它轻松创建时装秀的T型台。
* 物理交互。它具有与舞台形状相符的物理碰撞器，因此其他物理对象可以正确地与其交互。

## 水系统
对于HD和RT版本，提供了一个水系统，可以创建逼真的游泳池、河流或海洋视觉效果。当使用游泳池模式时，您可以使用过程化舞台在地面上挖一个池子。它也可以与自定义舞台模型一起使用。

使用提供的预设示例来查看参数如何影响最终结果。

## 演示
{% include video id="kOrp7rESrXQ" provider="youtube" %}