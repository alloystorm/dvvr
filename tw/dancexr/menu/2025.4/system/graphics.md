---
locale: zh-rTW
layout: single
title: 圖形
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[系統](../menu#系統) > 圖形



| Setting | Value | Description |
| :--- | --- | :--- |
| (Anti-Aliasing: Deferred SMAA) || 0/18/True
| 抗鋸齒 | **延遲 SMAA** | 不使用抗鋸齒, 延遲 SMAA, 延遲 TAA,  |
| **光線追蹤** | | 1/18/True
| ├ (Enable Raytracing) | ON | 0/8/False
| ├ 反射 | ON | 1/8/False
| ├ 環境光遮蔽 | ON | 2/8/False
| ├ 全局光照 | ON | 3/8/False
| ├ 陰影 | ON | 4/8/False
| ├ 接觸陰影 | OFF | 5/8/False
| ├ 光線長度 | [50] (0 ~ 100) | 6/8/False
| ├ 去噪 | ON | 7/8/False
| └ 去噪半徑 | [0.1] (0 ~ 1) | 8/8/False
| (Super Sampling: Off) || 2/18/True
| 超取樣 | **關閉** | 關閉, DLSS 性能, DLSS 平衡, DLSS 品質, DLSS 超性能, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **反射** | | 3/18/True
| ├ (Enable Reflection) | ON | 0/7/False
| ├ 模式 | 螢幕空間 | 螢幕空間, 探針, 1/7/False
| ├ 品質 | 高 | 低, 中, 高, 2/7/False
| ├ 演算法 | 近似值 | 近似值, PBR累積, <br/>螢幕空間反射的演算法。3/7/False
| ├ 邊緣淡出距離 | [0.1] (0 ~ 1) | 4/7/False
| ├ 物件厚度 | [0.01] (0 ~ 0.1) | 5/7/False
| ├ 回退至天空 | ON | 當光線追蹤沒有命中時回退至天空顏色。6/7/False
| └ 天空反射 | ON | 7/7/False
| **霧** | | 4/18/True
| ├ (Enable Fog) | ON | 0/4/False
| ├ 體積霧 | ON | 1/4/False
| ├ 基礎高度 | [0] (0 ~ 10) | 2/4/False
| ├ 最大高度 | [25] (10 ~ 100) | 3/4/False
| └ 最大距離 | [5000] (0 ~ 10000) | 4/4/False
| **環境光遮蔽** | | 5/18/True
| ├ (Enable Ambient Occlusion) | OFF | 0/2/False
| ├ 品質 | 高 | 低, 中, 高, 1/2/False
| └ 強度 | [1] (0 ~ 1) | 2/2/False
| **全局光照** | | 6/18/True
| ├ (Enable Global Illumination) | OFF | 0/2/False
| ├ 品質 | 低 | 低, 中, 高, 1/2/False
| └ 回退至天空 | ON | 2/2/False
| **景深** | | 7/18/True
| ├ (Enable Depth Of Field) | OFF | 0/3/False
| ├ 品質 | 中 | 低, 中, 高, 1/3/False
| ├ 強度 | [0.25] (0 ~ 1) | 2/3/False
| └ 偏移 | [0.1] (-1 ~ 1) | 3/3/False
| **動態模糊** | | 8/18/True
| ├ (Enable Motion Blur) | OFF | 0/2/False
| ├ 品質 | 中 | 低, 中, 高, 1/2/False
| └ 強度 | [0.25] (0 ~ 1) | 2/2/False
| **泛光** | | 9/18/True
| ├ (Enable Bloom) | ON | 0/2/False
| ├ 品質 | 高 | 低, 中, 高, 1/2/False
| └ 強度 | [0.25] (0 ~ 1) | 2/2/False
| **鏡頭光暈** | | 10/18/True
| ├ (Enable Lens Flare) | ON | 0/7/False
| ├ 在 VR 中禁用 | ON | 此效果不建議用於 VR1/7/False
| ├ 強度 | [0.1] (0 ~ 1) | 2/7/False
| ├ **顏色** | | 3/7/False
| │ ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
| │ ├ 色相 | [0] (0 ~ 1) | 1/8/True
| │ ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
| │ ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| │ ├ 紅色 | [1] (0 ~ 1) | 4/8/True
| │ ├ 綠色 | [1] (0 ~ 1) | 5/8/True
| │ ├ 藍色 | [1] (0 ~ 1) | 6/8/True
| │ ├ 使用舞台顏色 | OFF | 使用舞台環的顏色7/8/True
| │ ├ 色溫 | [6500] (3000 ~ 8000) | 8/8/True
| │ └ 預設 | **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| ├ 光暈 | [1] (0 ~ 1) | 4/7/False
| ├ 條紋 | [0.2] (0 ~ 1) | 5/7/False
| ├ 長度 | [0.5] (0 ~ 1) | 6/7/False
| └ 色差 | [0.5] (0 ~ 1) | 7/7/False
| **顏色調整** | | 11/18/True
| ├ (Enable Color Adjustment) | ON | 0/5/False
| ├ 後期曝光 | [0] (-12 ~ 12) | 1/5/False
| ├ 對比度 | [1] (-100 ~ 100) | 2/5/False
| ├ 色相偏移 | [0] (-180 ~ 180) | 3/5/False
| ├ 飽和度 | [1] (-100 ~ 100) | 4/5/False
| └ **顏色濾鏡** | | 5/5/False
|   ├ 顏色模式 | (HSV) | (RGB), (HSV), 0/7/True
|   ├ 色相 | [0] (0 ~ 1) | 1/7/True
|   ├ 飽和度 | [0] (0 ~ 1) | 2/7/True
|   ├ 亮度 | [1] (0 ~ 1) | 3/7/True
|   ├ 紅色 | [1] (0 ~ 1) | 4/7/True
|   ├ 綠色 | [1] (0 ~ 1) | 5/7/True
|   ├ 藍色 | [1] (0 ~ 1) | 6/7/True
|   ├ 發光 | [1] (0 ~ 20) | 7/7/True
|   └ 預設 | **白色** | 白色, 紅色, 綠色, 藍色, 動畫色相, 隨音樂發光,  |
| **顏色曲線** | | 12/18/True
| ├ (Enable Color Curve) | ON | 0/6/False
| ├ 起始漸變 | [1] (0 ~ 4) | 1/6/False
| ├ 起始位置 | [0] (0 ~ 0.5) | 2/6/False
| ├ 起始值 | [0] (0 ~ 0.5) | 3/6/False
| ├ 結束漸變 | [1] (0 ~ 4) | 4/6/False
| ├ 結束位置 | [1] (0.5 ~ 1) | 5/6/False
| └ 結束值 | [1] (0.5 ~ 1) | 6/6/False
| **白平衡** | | 13/18/True
| ├ (Enable White Balance) | ON | 0/2/False
| ├ 溫度 | [0] (-100 ~ 100) | 1/2/False
| └ 色調 | [0] (-100 ~ 100) | 2/2/False
| **特殊渲染** | | 14/18/True
| ├ (Enable Special Render) | OFF | 0/5/False
| ├ 模式 | 深度輸出 | 深度輸出, 法線輸出, 1/5/False
| ├ 深度範圍 | [1] (0 ~ 1) | 2/5/False
| ├ 深度比例 | [0.25] (0 ~ 1) | 3/5/False
| ├ 法線比例 | [1] (0 ~ 1) | 4/5/False
| └ 法線混合 | [0] (0 ~ 1) | 5/5/False
| 色調映射 | 自訂 | 無, 中性, ACES, 自訂, 15/18/True
| 演員卡通陰影 | OFF | 對所有角色使用卡通陰影。16/18/True
| 階段卡通陰影 | OFF | 對舞台和道具使用卡通陰影。17/18/True
| **選項** | | 18/18/True
| ├ 透明預處理 | ON | 啟用透明預處理。這將使被遮擋的透明材質不可見。0/5/False
| ├ 螢幕空間陰影 | ON | 1/5/False
| ├ 接觸陰影 | OFF | 小細節的陰影。2/5/False
| ├ 凹凸貼圖陰影 | [0.5] (0 ~ 1) | 為凹凸貼圖和細節貼圖啟用陰影。3/5/False
| ├ 停止 NaN | ON | (Prevent black screen when error happens during post processing. )4/5/False
| └ 計算厚度 | ON | 計算可用於皮膚效果的厚度。5/5/False
| 預設 | **高** | 性能, 中, 高, 室內全局光照, 室外全局光照, 卡通效果,  |
