---
locale: zh-rCN
layout: single
title: [自动摄像机]
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[程序化](../menu#程序化) > [自动摄像机]



| Setting | Value | Description |
| :--- | --- | :--- |
| 分配给主对象 || 
| (Target Select: Auto) || 
| 目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| (Tracking Mode: Center) || 
| 跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| 目标平滑 | [0.5] (0 ~ 2) | 
| 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| 视场 | [30] (5 ~ 120) | 
| 节拍循环 | [8] (1 ~ 16) | 
| 近距离 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| 远距离 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| 使用角色朝向 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
| 种子 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| 淡入黑色 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| 淡入概率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
| 音频灵敏度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
| 目标选择 || 
| 头部 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| 胸部 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| 中心 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| 腿 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| 脚 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
| 距离选择 || 
| 特写 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| 放大 | [0.25] (0 ~ 1) | (Probability of zooming in.)
| 缩小 | [0.25] (0 ~ 1) | (Probability of zooming out.)
| 中间 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| 远 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
| 路径选择 || 
| 高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| 低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
| 方向 || 
| 前中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| 前45度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| 侧面90度 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| 后135度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| 后180度 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| 预设 | **默认（重置）** | 默认（重置）, (Preset 1),  |
