---
locale: zh-CN
layout: single
title: 图形
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## 图形设置

### 抗锯齿

### 超采样
DLSS，FSR

### 反射

### 环境遮挡

### 全局光照

### 景深

### 运动模糊

### 泛光

### 镜头光晕

### 色彩调整

### 色彩滤镜

### 白平衡

### 特殊渲染模式：深度和法线
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 之前的卡通着色器已经扩展到包括2种模式，深度和法线。
* 这些设计用于与稳定扩散控制网络一起使用，为您的AI图像提供基础。
* 一个典型的用例是在DanceXR中为演员设置构图和姿势，然后使用稳定扩散生成具有完全不同角色和环境的详细图像。
* 是的，您可以从ControlNet中的任何图像生成深度和法线图，但渲染的深度和法线图比生成的更准确，您可以自行测试。
* 在ControlNet中使用渲染的深度和法线图时，请确保选择“无”作为预处理器，因为它们不需要进一步处理。

### 选项