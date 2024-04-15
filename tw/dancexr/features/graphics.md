---
locale: zh-TW
layout: single
title: 圖形
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## 圖形設置

### 抗鋸齒

### 超級採樣
DLSS, FSR

### 反射

### 環境遮蔽

### 全局照明

### 景深

### 運動模糊

### 泛光

### 鏡頭光晕

### 色彩調整

### 色彩濾鏡

### 白平衡

### 特殊渲染模式：深度和法線
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 先前的卡通著色器已擴展到包括2種模式，深度和法線。
* 這些設計用於與Stable Diffusion ControlNet一起使用，為您的AI圖像提供基礎。
* 典型用例是在DanceXR中設置您的構圖和演員的姿勢，然後使用Stable Diffusion生成具有完全不同角色和環境的詳細圖像。
* 是的，您可以從ControlNet中的任何圖像生成深度和法線圖，但渲染的深度和法線圖比生成的更準確，您可以自行測試。
* 在ControlNet中使用渲染的深度和法線圖時，請確保選擇“無”作為預處理器，因為它們不需要進一步處理。

### 選項