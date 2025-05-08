---
locale: zh-rCN
layout: single
title: 缩放与偏移
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.5/actor/scale_n_offset) | [繁中](/tw/dancexr/menu/2025.5/actor/scale_n_offset) | [日本語](/jp/dancexr/menu/2025.5/actor/scale_n_offset) | [한국어](/kr/dancexr/menu/2025.5/actor/scale_n_offset) | [简中](/zh/dancexr/menu/2025.5/actor/scale_n_offset)

[设置](../menu#设置) > 缩放与偏移

(
## Overview
The Model Scale & Offset configuration allows users to adjust the model's scale, position, and rotation with precision. It provides tools for aligning the model to the ground, setting uniform height, and fine-tuning offsets.

## Key Features
- **Scale Adjustment**: Modify the overall size of the model with exponential precision.
- **Ground Offset**: Set the vertical position relative to the ground.
- **Uniform Height**: Scale the model to match average human height.
- **Rotation Control**: Adjust the model's rotation in degrees.
- **Positional Offsets**: Fine-tune horizontal offsets along the X and Z axes.
- **Snapping Options**: Enable snapping increments for precise drag adjustments.)

## 配置

| 设置 | 值 | 描述 |
| :--- | --- | :--- |
| ⊖ 模型缩放 | [0] (-3 ~ 3) | 调整模型的整体缩放。数值采用指数形式以实现更细致的控制。
| ⊖ 地面偏移 | [0] (-2 ~ 2) | 设置模型相对于地面的垂直偏移。
| ☑ 统一高度 | [ON] | 启用此项可以将模型缩放至平均人体高度。
| ⊖ 旋转 | [0] (-180 ~ 180) | 设置模型的旋转角度（单位：度）。
| ⊖ X方向偏移 | [0] (-5 ~ 5) | 调整模型沿X轴的水平偏移。
| ⊖ Z轴偏移 | [0] (-5 ~ 5) | 调整模型沿Z轴的水平偏移。
| ☑ 吸附 | (0) | (0), (0.1), (0.2), (0.5), (1), (2), <br/>设置拖动调整时的吸附增量，较小数值允许更细致的控制。
| ≡ 预设 | **统一生命尺寸** | 统一生命尺寸, 微缩模型, 巨型, 初始纹理,  |
