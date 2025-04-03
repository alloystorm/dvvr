---
locale: zh-rCN
layout: single
title: 悬挂物理
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/stage/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/stage/cloth_physics)

[舞台](../menu#舞台) > 悬挂物理



| Setting | Value | Description |
| :--- | --- | :--- |
| 启用 | ON | 
| 选择骨骼 || 选择骨骼
| 跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| **粒子动力学** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| ├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| ├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| ├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| ├&nbsp;可视化 | OFF | 
| ├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| ├&nbsp;惯性 | [2] (1 ~ 5) | 
| ├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| ├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| ├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| ├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| ├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| ├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| ├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| ├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| ├&nbsp;**风** | | 
| │&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| ├&nbsp;**碰撞与** | | 
| │&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;├&nbsp;手 | ON | 
| │&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;└&nbsp;玩家 | ON | 
| └&nbsp;**模拟设置** | | 
| &nbsp;&nbsp;├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| &nbsp;&nbsp;├&nbsp;启用拖动 | ON | 
| &nbsp;&nbsp;├&nbsp;模拟 | ON | 
| &nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| &nbsp;&nbsp;│&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| &nbsp;&nbsp;├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;子步 | [4] (1 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;迭代 | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;反向偶数子步 | OFF | 
| &nbsp;&nbsp;├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;表格大小 | [6] (1 ~ 20) | 
| &nbsp;&nbsp;└&nbsp;两步求解 | OFF | 
| 弹簧 | [0.5] (0 ~ 5) | 
| 阻尼 | [0.01] (0 ~ 0.1) | 
| 减少比例 | [0.25] (0 ~ 1) | 每个层级减少刚度
| 扭转限制 | [5] (0 ~ 180) | 限制扭转旋转
| 限制力 | [3] (0 ~ 8) | 
| 质量 | [0.05] (0 ~ 0.1) | 
| 拖拽 | [1] (0 ~ 10) | 
| 碰撞体半径 | [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
| 碰撞体长度 | [0.9] (0 ~ 1) | 
| 锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| (Presets: Default (Reset)) || 
| 预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
