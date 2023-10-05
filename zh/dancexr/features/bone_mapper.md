---
layout: single
title: XPS骨骼映射器
toc: true
---
[English](/dancexr/features/bone_mapper) | [简体中文](/zh/dancexr/features/bone_mapper) | [日本語](/jp/dancexr/features/bone_mapper)


## 概述
XPS模型需要进行骨骼映射，以便动画和其他功能能够找到正确的骨骼。

如果您已经加载了一个模型，但它仍然保持标准姿势，那么您需要做以下操作才能使其正常工作。

{% include video id="g0VAfBHauXw" provider="youtube" %}

## 映射状态
通常，程序已经对大部分骨骼进行了映射，只有少数骨骼没有映射。您只需要映射带有“！”标记的骨骼，模型就可以正常工作。

骨骼映射的状态使用圆形图标表示。
* 空心圆表示骨骼未映射，但不是关键的，这意味着即使没有映射该骨骼，模型也可以正常工作。
* 内部有点的圆表示骨骼已经映射。
* 带有感叹号的圆表示骨骼未映射，对于模型的正常运行是关键的。

{% include video id="jtxQo5NYk2o" provider="youtube" %}