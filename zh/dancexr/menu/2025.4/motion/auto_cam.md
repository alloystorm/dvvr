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
| 分配给主对象 || 0/34/True
| (Target Select: Auto) || 1/34/True
| 目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| (Tracking Mode: Center) || 2/34/True
| 跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| 目标平滑 | [0.5] (0 ~ 2) | 3/34/True
| 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟4/34/True
| 视场 | [30] (5 ~ 120) | 5/34/True
| 节拍循环 | [8] (1 ~ 16) | 6/34/True
| 近距离 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)7/34/True
| 远距离 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)8/34/True
| 使用角色朝向 | ON | (Enable or disable alignment of the camera to the actor's orientation.)9/34/True
| 种子 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)10/34/True
| 淡入黑色 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)11/34/True
| 淡入概率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)12/34/True
| 音频灵敏度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)13/34/True
| 目标选择 || 14/34/True
| 头部 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)15/34/True
| 胸部 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)16/34/True
| 中心 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)17/34/True
| 腿 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)18/34/True
| 脚 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)19/34/True
| 距离选择 || 20/34/True
| 特写 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)21/34/True
| 放大 | [0.25] (0 ~ 1) | (Probability of zooming in.)22/34/True
| 缩小 | [0.25] (0 ~ 1) | (Probability of zooming out.)23/34/True
| 中间 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)24/34/True
| 远 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)25/34/True
| 路径选择 || 26/34/True
| 高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)27/34/True
| 低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)28/34/True
| 方向 || 29/34/True
| 前中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)30/34/True
| 前45度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)31/34/True
| 侧面90度 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)32/34/True
| 后135度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)33/34/True
| 后180度 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)34/34/True
| 预设 | **默认（重置）** | 默认（重置）, (Preset 1),  |
