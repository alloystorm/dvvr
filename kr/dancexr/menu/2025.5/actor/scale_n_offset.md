---
locale: ko-rKR
layout: single
title: 스케일 및 오프셋
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.5/actor/scale_n_offset) | [繁中](/tw/dancexr/menu/2025.5/actor/scale_n_offset) | [日本語](/jp/dancexr/menu/2025.5/actor/scale_n_offset) | [한국어](/kr/dancexr/menu/2025.5/actor/scale_n_offset) | [简中](/zh/dancexr/menu/2025.5/actor/scale_n_offset)

[설정](../menu#설정) > 스케일 및 오프셋

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

## 구성

| 설정 | 값 | 설명 |
| :--- | --- | :--- |
| ⊖ 모델 스케일 | [0] (-3 ~ 3) | 모델의 전체 스케일을 조정합니다. 값은 더 세밀한 제어를 위해 지수 방식입니다.
| ⊖ 지면 오프셋 | [0] (-2 ~ 2) | 모델의 지면 대비 수직 오프셋을 설정합니다.
| ☑ 균일 높이 | [ON] | 모델을 평균 인체 높이에 맞게 스케일합니다.
| ⊖ 회전 | [0] (-180 ~ 180) | 모델의 회전을 도 단위로 설정합니다.
| ⊖ X 오프셋 | [0] (-5 ~ 5) | 모델의 X축을 따라 수평 오프셋을 조정합니다.
| ⊖ 오프셋 Z | [0] (-5 ~ 5) | 모델의 Z축을 따라 수평 오프셋을 조정합니다.
| ☑ 스내핑 | (0) | (0), (0.1), (0.2), (0.5), (1), (2), <br/>드래그 조정 시 스내핑 단위를 설정합니다. 작은 값일수록 더 세밀한 제어가 가능합니다.
| ≡ 프리셋 | **균일 실물 크기** | 균일 실물 크기, 미니어처, 거인, 초기 텍스처,  |
