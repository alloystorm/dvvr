---
locale: zh-rTW
layout: single
title: 縮放與偏移
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.5/actor/scale_n_offset) | [繁中](/tw/dancexr/menu/2025.5/actor/scale_n_offset) | [日本語](/jp/dancexr/menu/2025.5/actor/scale_n_offset) | [한국어](/kr/dancexr/menu/2025.5/actor/scale_n_offset) | [简中](/zh/dancexr/menu/2025.5/actor/scale_n_offset)

[設定](../menu#設定) > 縮放與偏移

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

| 設定 | 值 | 描述 |
| :--- | --- | :--- |
| ⊖ 模型縮放 | [0] (-3 ~ 3) | 調整模型的整體縮放。數值採用指數形式以便更精細控制。
| ⊖ 地面偏移 | [0] (-2 ~ 2) | 設定模型相對於地面的垂直偏移。
| ☑ 統一高度 | [ON] | 啟用後將模型縮放至平均人體高度。
| ⊖ 旋轉 | [0] (-180 ~ 180) | 設定模型的旋轉角度（度）。
| ⊖ X 偏移 | [0] (-5 ~ 5) | 調整模型在 X 軸方向的水平偏移。
| ⊖ Z 軸偏移 | [0] (-5 ~ 5) | 調整模型在 Z 軸方向的水平偏移。
| ☑ 吸附 | (0) | (0), (0.1), (0.2), (0.5), (1), (2), <br/>設定拖曳調整的吸附增量。較小的數值允許更精細的控制。
| ≡ 預設值 | **統一實際大小** | 統一實際大小, 微型, 巨型, 初始材質,  |
