---
layout: single
title: 圖形
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/tw/dancexr/features/graphics) | [繁中](/tw/tw/dancexr/features/graphics) | [日本語](/jp/tw/dancexr/features/graphics) | [한국어](/kr/tw/dancexr/features/graphics) | [简中](/zh/tw/dancexr/features/graphics)


## 特殊渲染模式：深度和法线
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 先前的卡通着色器已擴展為包含2種模式，深度和法线。
* 這些模式是為了與穩定擴散控制網絡（Stable Diffusion ControlNet）一起使用，為您的AI圖像提供基礎。
* 典型的用例是在DanceXR中設置您的構圖和演員的姿勢，然後使用穩定擴散生成具有完全不同角色和環境的詳細圖像。
* 是的，您可以從ControlNet中的任何圖像生成深度和法线圖，但是渲染的深度和法线圖比生成的更準確，您可以自行測試。
* 在ControlNet中使用渲染的深度和法线圖時，請確保選擇“無”作為預處理器，因為它們不需要進一步處理。