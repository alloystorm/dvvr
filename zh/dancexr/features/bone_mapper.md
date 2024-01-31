---
locale: zh-CN
layout: single
title: XPS骨骼映射器
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/bone_mapper) | [繁中](/tw/dancexr/features/bone_mapper) | [日本語](/jp/dancexr/features/bone_mapper) | [한국어](/kr/dancexr/features/bone_mapper) | [简中](/zh/dancexr/features/bone_mapper)


## 概述
XPS模型需要进行骨骼映射，以便动画和其他功能能够找到正确的骨骼。

如果你加载了一个模型，但它保持在标准姿势，那么你需要做以下操作使其正常工作。

{% include video id="g0VAfBHauXw" provider="youtube" %}

## 映射状态
通常，大部分骨骼已经由程序进行了映射，只有少数骨骼未映射。你只需要映射带有"!"标记的骨骼，模型就能正常工作。

骨骼映射的状态用圆形图标表示。
* 空心圆表示骨骼未映射，但不是关键的，也就是说，即使没有映射该骨骼，模型也能正常工作。
* 带有内部点的圆表示骨骼已经映射。
* 带有感叹号的圆表示骨骼未映射，对于模型的正常运行是关键的。

{% include video id="jtxQo5NYk2o" provider="youtube" %}

## 更多演示
这是一个将FBX模型转换为XPS格式，并使用骨骼映射器使其在DanceXR中正常工作的视频演示。

{% include video id="YqX_uktVvQk" provider="youtube" %}
{% include video id="BV1CF411o7P2" provider="bilibili" %}