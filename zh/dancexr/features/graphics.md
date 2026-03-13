---
locale: zh-CN
layout: single
title: 图形
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

渲染质量设置。

## 配置

有关配置的详细说明，请访问以下页面：

[图形 v2025.4](/dancexr/menu/2025.4/system/graphics)

### 渲染质量改进 (v2025.10)
改进了着色器以获得更佳的皮肤效果，并去除了LW和Android版本中皮肤和头发对象上的过度天空反射。改进了细节和遮罩纹理的处理，以提升视觉质量。

### Unity 6.3升级及DLSS更新 (v2026.2)
DanceXR 2026.2将底层Unity引擎升级至6.3版本，带来性能优化、增强的图形功能及对最新引擎特性的支持。Unity 6.3随附DLSS版本310.4.0.0，进一步提升支持NVIDIA显卡的性能与视觉质量。

### 着色器优化 (v2026.3)
为简化场景添加了专用着色器变体——特别是当未使用**服装**和**汗水效果**高级功能时。这在高分辨率及VR场景中可显著提升帧率。

### 关于视网膜渲染的说明 (v2026.3)
PC端视网膜渲染需要DX12并禁用后期处理和阴影，这会显著限制其实用性。Unity目前暂无计划在PC端扩展其可用性。Quest独立版中，视网膜渲染表现正常。