---
locale: zh-rCN
layout: single
title: 悬挂物理
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > 悬挂物理



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Dangling Physics) | ON | 0/13/True
| 选择骨骼 || 选择骨骼1/13/True
| 跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接2/13/True
| **粒子动力学** | | 3/13/True
| ├ (Enable Particle Dynamics) | ON | 0/18/False
| ├ 摆动柔顺性 | [0.25] (0 ~ 1) | 1/18/False
| ├ 扭转柔顺性 | [0.75] (0 ~ 1) | 2/18/False
| ├ 粒子锚点 | [0.5] (0 ~ 1) | 3/18/False
| ├ 减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量4/18/False
| ├ 可视化 | OFF | 5/18/False
| ├ 最大角速度 | [2] (0 ~ 4) | 6/18/False
| ├ 惯性 | [2] (1 ~ 5) | 7/18/False
| ├ 软化 | [0] (0 ~ 1) | 软化粒子约束。8/18/False
| ├ 粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）9/18/False
| ├ 重力 | [9.8] (-9.8 ~ 9.8) | 10/18/False
| ├ 摩擦力 | [1] (0 ~ 2) | 11/18/False
| ├ 地面摩擦 | [1] (-2 ~ 2) | 12/18/False
| ├ 拖拽（空气） | [0] (0 ~ 2) | 空气阻力13/18/False
| ├ 拖拽（水下） | [1] (0 ~ 2) | 水下阻力14/18/False
| ├ 浮力 | [-0.1] (-1 ~ 1) | 15/18/False
| ├ **风** | | 16/18/False
| │ ├ 风的影响 | [0.25] (0 ~ 1) | 0/3/False
| │ ├ 湍流比例 | [0] (-2 ~ 2) | 1/3/False
| │ ├ 湍流强度 | [1] (0 ~ 2) | 2/3/False
| │ └ 湍流时间比例 | [0] (-4 ~ 4) | 3/3/False
| ├ **碰撞与** | | 17/18/False
| │ ├ 头部 | ON | 0/8/False
| │ ├ 身体 | ON | 1/8/False
| │ ├ 胸部 | ON | 2/8/False
| │ ├ 臀部 | ON | 3/8/False
| │ ├ (Arms) | ON | 4/8/False
| │ ├ 手 | ON | 5/8/False
| │ ├ 腿 | ON | 6/8/False
| │ ├ 脚 | ON | 7/8/False
| │ └ 玩家 | ON | 8/8/False
| └ **模拟设置** | | 18/18/False
|   ├ 使用全局 | ON | 在 Pro / 布料模拟下找到全局设置0/10/False
|   ├ 启用拖动 | ON | 1/10/False
|   ├ 模拟 | ON | 2/10/False
|   ├ (Simulation FPS: Dynamic) || 3/10/False
|   │ 模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|   ├ 时间比例 | [0.65] (0.1 ~ 1) | 4/10/False
|   ├ 子步 | [4] (1 ~ 20) | 5/10/False
|   ├ 迭代 | [1] (0 ~ 10) | 6/10/False
|   ├ 反向偶数子步 | OFF | 7/10/False
|   ├ 备用组大小 | [0] (0 ~ 20) | 8/10/False
|   ├ 表格大小 | [6] (1 ~ 20) | 9/10/False
|   └ 两步求解 | OFF | 10/10/False
| 弹簧 | [0.5] (0 ~ 5) | 4/13/True
| 阻尼 | [0.01] (0 ~ 0.1) | 5/13/True
| 减少比例 | [0.25] (0 ~ 1) | 每个层级减少刚度6/13/True
| 扭转限制 | [5] (0 ~ 180) | 限制扭转旋转7/13/True
| 限制力 | [3] (0 ~ 8) | 8/13/True
| 质量 | [0.05] (0 ~ 0.1) | 9/13/True
| 拖拽 | [1] (0 ~ 10) | 10/13/True
| 碰撞体半径 | [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小11/13/True
| 碰撞体长度 | [0.9] (0 ~ 1) | 12/13/True
| 锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼13/13/True
| 预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
