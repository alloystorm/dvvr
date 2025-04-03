---
locale: zh-rTW
layout: single
title: [自動攝影機]
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[程序化](../menu#程序化) > [自動攝影機]



| Setting | Value | Description |
| :--- | --- | :--- |
| 指派給主體 || 
| (Target Select: Auto) || 
| 目標選擇 | **自動** | 自動, 已選擇, 群組, 旋轉, 旋轉 + 群組, 舞台中心,  |
| (Tracking Mode: Center) || 
| 追踪模式 | **中心** | 中心, 頭部, 胸部,  |
| 目標平滑 | [0.5] (0 ~ 2) | 
| 預測 | [1] (0 ~ 2) | 預測目標位置以減少因平滑造成的延遲
| 視場 | [30] (5 ~ 120) | 
| 節拍循環 | [8] (1 ~ 16) | 
| 近距離 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| 遠距離 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| 使用演員方向 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
| 種子 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| 淡入黑色 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| F2B 機率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
| 音頻靈敏度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
| 目標選擇 || 
| 頭部 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| 胸部 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| 中心 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| 腿部 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| 腳 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
| 距離選擇 || 
| 特寫 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| 放大 | [0.25] (0 ~ 1) | (Probability of zooming in.)
| 縮小 | [0.25] (0 ~ 1) | (Probability of zooming out.)
| 中間 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| 遠 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
| 路徑選擇 || 
| 高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| 低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
| 朝向 || 
| 正中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| 前方 45 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| 側面 90 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| 背面 135 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| 背面 180 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| 預設 | **預設 (重置)** | 預設 (重置), (Preset 1),  |
