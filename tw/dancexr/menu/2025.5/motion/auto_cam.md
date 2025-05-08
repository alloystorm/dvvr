---
locale: zh-rTW
layout: single
title: [自動攝影機]
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.5/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.5/motion/auto_cam)

[程序化](../menu#程序化) > [自動攝影機]

(
## Overview
The Automatic Camera Motion System (AutoCam) is a dynamic camera control solution designed to enhance visual storytelling by synchronizing camera movements with music beats, actor orientation, and configurable parameters.

## Key Features
- Dynamic adjustment of camera motion based on music beats.
- Configurable parameters for distance, target selection, and motion paths.
- Support for actor orientation alignment.
- Randomized camera motion generation with seed control.
- Fade-to-black transitions with adjustable duration and probability.
- Audio sensitivity for motion responsiveness to sound levels.

## Use Cases
- Creating cinematic sequences in real-time.
- Enhancing the visual appeal of dance or music-based performances.
- Automating camera control for interactive applications or games.)

## 配置

| 設定 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 指定到主要 || 
| > 目標選擇 | **自動** | 自動, 已選擇, 群組, 旋轉, 旋轉 + 群組, 舞台中心,  |
| > 追蹤模式 | **中心** | 中心, 頭部, 胸部,  |
| ⊖ 目標平滑 | [0.5] (0 ~ 2) | 
| ⊖ 預測 | [1] (0 ~ 2) | 預測目標位置以降低平滑造成的延遲
| ⊖ 視野 | [30] (5 ~ 120) | 
| ⊖ 節拍週期 | [8] (1 ~ 16) | 
| ⊖ 近距離 | [1.5] (0.5 ~ 3) | 相機距離目標的最短距離。
| ⊖ 遠距離 | [2.5] (0.5 ~ 3) | 相機距離目標的最遠距離。
| ☑ 使用演員方向 | [ON] | 啟用或停用相機對演員方向的對齊。
| ⊖ 種子值 | [1234] ((Unlimited)) | 用於生成隨機相機運動的種子值。
| ⊖ 淡出至黑 | [0] (0 ~ 0.25) | 過渡期間淡出至黑效果的持續時間。
| ⊖ 淡出至黑概率 | [0.5] (0 ~ 1) | 觸發淡出至黑效果的概率。
| ☐ 音訊靈敏度 | [1] (0 ~ 4) | 相機運動對音頻水平的敏感度。
|  **目標選擇** || 
| ⊖ 頭部 | [1] (0 ~ 1) | 定位演員頭部的概率。
| ⊖ 胸部 | [1] (0 ~ 1) | 定位演員胸部的概率。
| ⊖ 中心 | [1] (0 ~ 1) | 定位演員中心的概率。
| ⊖ 雙腿 | [0.5] (0 ~ 1) | 定位演員腿部的概率。
| ⊖ 腳部 | [0] (0 ~ 1) | 定位演員腳部的概率。
|  **距離選擇** || 
| ⊖ 特寫 | [1] (0 ~ 1) | 特寫距離的概率。
| ⊖ 放大 | [0.25] (0 ~ 1) | 放大的概率。
| ⊖ 縮小 | [0.25] (0 ~ 1) | 縮小的概率。
| ⊖ 中間 | [0.25] (0 ~ 1) | 中距離攝影的概率。
| ⊖ 遠距離 | [0.25] (0 ~ 1) | 遠距離攝影的概率。
|  **路徑選擇** || 
| ⊖ 高角度 | [20] (0 ~ 30) | 相機最大向上角度。
| ⊖ 低角度 | [-20] (-30 ~ 0) | 相機最大向下角度。
|  **方向** || 
| ⊖ 正前中心 | [1] (0 ~ 1) | 相機對准演員正前中心的概率。
| ⊖ 前方45度 | [0] (0 ~ 1) | 相機對准演員前方45度角的概率。
| ⊖ 側面90度 | [0.25] (0 ~ 1) | 相機對准演員側面90度角的概率。
| ⊖ 後方135度 | [0] (0 ~ 1) | 相機對准演員後方135度角的概率。
| ⊖ 後方180度 | [0.25] (0 ~ 1) | 相機直接對准演員背面的概率。
| ≡ 預設值 | **預設（重置）** | 預設（重置）, (Preset 1),  |
