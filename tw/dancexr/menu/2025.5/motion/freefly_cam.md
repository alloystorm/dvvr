---
locale: zh-rTW
layout: single
title: [Freefly Cam]
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.5/motion/freefly_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/freefly_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/freefly_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/freefly_cam) | [简中](/zh/dancexr/menu/2025.5/motion/freefly_cam)

[程序化](../menu#程序化) > [Freefly Cam]

提供一種自由飛行攝影機模式，使用者可完全控制攝影機的移動與旋轉。攝影機可向前、向後、向上、向下移動，並根據使用者輸入旋轉或傾斜。額外選項包括環繞移動與垂直移動限制。

## 配置

| 設定 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 指定到主要 || 
| > 目標選擇 | **已選擇** | 自動, 已選擇, 群組, 旋轉, 旋轉 + 群組, 舞台中心,  |
| > 追蹤模式 | **中心** | 中心, 頭部, 胸部,  |
| ⊖ 目標平滑 | [0.5] (0 ~ 2) | 
| ⊖ 預測 | [1] (0 ~ 2) | 預測目標位置以降低平滑造成的延遲
| ☐ 鎖定目標 | [OFF] | 自動對焦目標
| ☐ 相機晃動 | [0.5] (0 ~ 1) | 
| ☐ 鎖定旋轉 | [OFF] | 相機跟隨目標旋轉
| ⊖ 自動縮放 | [0] (0 ~ 1) | 自動縮放以維持目標尺寸在畫面中
| ⊖ 縮放速度 | [0.5] (0 ~ 1) | 縮放到目標視野所需時間
| ⊖ 目標處的視野高度 | [1] (0.2 ~ 2) | 自動縮放時目標的垂直高度
| ⊖ 垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
| ⊖ 視野 | [30] (5 ~ 120) | 
| ⊖ 節拍週期 | [8] (1 ~ 16) | 
| ☐ 使用環繞移動 | [OFF] | 啟用或停用環繞移動，允許攝影機繞著中心點旋轉。
| ≡ 預設值 | **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
