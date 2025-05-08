---
locale: zh-rCN
layout: single
title: [自动摄像机]
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.5/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.5/motion/auto_cam)

[程序化](../menu#程序化) > [自动摄像机]

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

| 设置 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 分配给主动作 || 
| > 目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| > 跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| ⊖ 目标平滑 | [0.5] (0 ~ 2) | 
| ⊖ 预测 | [1] (0 ~ 2) | 预测目标位置以减少平滑造成的延迟
| ⊖ 视野 | [30] (5 ~ 120) | 
| ⊖ 节拍周期 | [8] (1 ~ 16) | 
| ⊖ 近距离 | [1.5] (0.5 ~ 3) | 摄像机与目标的最小距离。
| ⊖ 远距离 | [2.5] (0.5 ~ 3) | 摄像机与目标的最大距离。
| ☑ 使用演员朝向 | [ON] | 启用或禁用摄像机与演员朝向的对齐。
| ⊖ 种子 | [1234] ((Unlimited)) | 用于生成随机摄像机运动的种子值。
| ⊖ 淡出至黑 | [0] (0 ~ 0.25) | 过渡期间淡出至黑效果的持续时间。
| ⊖ 淡出至黑概率 | [0.5] (0 ~ 1) | 触发淡出至黑效果的概率。
| ☐ 音频灵敏度 | [1] (0 ~ 4) | 摄像机运动对音频音量的灵敏度。
|  **目标选择** || 
| ⊖ 头部 | [1] (0 ~ 1) | 以头部为目标的概率。
| ⊖ 胸部 | [1] (0 ~ 1) | 以胸部为目标的概率。
| ⊖ 中心 | [1] (0 ~ 1) | 以中心为目标的概率。
| ⊖ 双腿 | [0.5] (0 ~ 1) | 以腿部为目标的概率。
| ⊖ 脚 | [0] (0 ~ 1) | 以脚部为目标的概率。
|  **距离选择** || 
| ⊖ 特写 | [1] (0 ~ 1) | 特写摄像机距离的概率。
| ⊖ 拉近 | [0.25] (0 ~ 1) | 拉近的概率。
| ⊖ 拉远 | [0.25] (0 ~ 1) | 拉远的概率。
| ⊖ 中间 | [0.25] (0 ~ 1) | 中距离摄像机的概率。
| ⊖ 远处 | [0.25] (0 ~ 1) | 远距离摄像机的概率。
|  **路径选择** || 
| ⊖ 高角度 | [20] (0 ~ 30) | 摄像机最大向上仰角。
| ⊖ 低角度 | [-20] (-30 ~ 0) | 摄像机最大向下俯角。
|  **方向** || 
| ⊖ 正前方中心 | [1] (0 ~ 1) | 将摄像机对准演员正前方中心的概率。
| ⊖ 正前方45度 | [0] (0 ~ 1) | 将摄像机对准演员正前方45度角的概率。
| ⊖ 侧面90度 | [0.25] (0 ~ 1) | 将摄像机对准演员侧面90度角的概率。
| ⊖ 背后135度 | [0] (0 ~ 1) | 将摄像机对准演员背后135度角的概率。
| ⊖ 背后180度 | [0.25] (0 ~ 1) | 将摄像机直接对准演员背后的概率。
| ≡ 预设 | **默认（重置）** | 默认（重置）, (Preset 1),  |
