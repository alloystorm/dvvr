---
locale: zh-rCN
layout: single
title: [Freefly Cam]
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.5/motion/freefly_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/freefly_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/freefly_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/freefly_cam) | [简中](/zh/dancexr/menu/2025.5/motion/freefly_cam)

[程序化](../menu#程序化) > [Freefly Cam]

提供一种自由飞行摄像机模式，用户可以完全控制摄像机的移动和旋转。摄像机可以根据用户输入自由前后、上下移动及旋转或倾斜。附加选项包括环绕移动和垂直移动限制。

## 配置

| 设置 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 分配给主动作 || 
| > 目标选择 | **已选择** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| > 跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| ⊖ 目标平滑 | [0.5] (0 ~ 2) | 
| ⊖ 预测 | [1] (0 ~ 2) | 预测目标位置以减少平滑造成的延迟
| ☐ 锁定目标 | [OFF] | 自动聚焦目标
| ☐ 相机抖动 | [0.5] (0 ~ 1) | 
| ☐ 锁定旋转 | [OFF] | 相机跟随目标旋转
| ⊖ 自动缩放 | [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
| ⊖ 缩放速度 | [0.5] (0 ~ 1) | 缩放到目标视野所需时间
| ⊖ 目标处视野高度 | [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
| ⊖ 垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
| ⊖ 视野 | [30] (5 ~ 120) | 
| ⊖ 节拍周期 | [8] (1 ~ 16) | 
| ☐ 使用环绕移动 | [OFF] | 启用或禁用环绕移动，允许摄像机绕中心点旋转。
| ≡ 预设 | **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
