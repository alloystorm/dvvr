---
locale: zh-rCN
layout: single
title: 网格转布料
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[专业版](../menu#专业版) > 网格转布料



| Setting | Value | Description |
| :--- | --- | :--- |
| 合并为一个 | OFF | 0/3/False
| 逐渐启用 | [2] (0 ~ 5) | 1/3/False
| **粒子属性** | | 2/3/False
| ├ 粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）0/21/False
| ├ 粘性 | [0] (0 ~ 1) | 1/21/False
| ├ 重力 | [9.8] (-9.8 ~ 9.8) | 2/21/False
| ├ 摩擦力 | [1] (0 ~ 2) | 3/21/False
| ├ 地面摩擦 | [1] (-2 ~ 2) | 4/21/False
| ├ 拖拽（空气） | [0] (0 ~ 2) | 空气阻力5/21/False
| ├ 拖拽（水下） | [1] (0 ~ 2) | 水下阻力6/21/False
| ├ 浮力 | [-0.1] (-1 ~ 1) | 7/21/False
| ├ **风** | | 8/21/False
| │ ├ 风的影响 | [0.25] (0 ~ 1) | 0/3/False
| │ ├ 湍流比例 | [0] (-2 ~ 2) | 1/3/False
| │ ├ 湍流强度 | [1] (0 ~ 2) | 2/3/False
| │ └ 湍流时间比例 | [0] (-4 ~ 4) | 3/3/False
| ├ **碰撞与** | | 9/21/False
| │ ├ 头部 | ON | 0/8/False
| │ ├ 身体 | ON | 1/8/False
| │ ├ 胸部 | ON | 2/8/False
| │ ├ 臀部 | ON | 3/8/False
| │ ├ (Arms) | ON | 4/8/False
| │ ├ 手 | ON | 5/8/False
| │ ├ 腿 | ON | 6/8/False
| │ ├ 脚 | ON | 7/8/False
| │ └ 玩家 | ON | 8/8/False
| ├ 启用弯曲约束 | ON | 10/21/False
| ├ 弯曲顺应性 | [0] (0 ~ 1) | 11/21/False
| ├ 缩放 | [1] (0 ~ 2) | 12/21/False
| ├ 自我碰撞 | OFF | 13/21/False
| ├ 抓地质量 | [2] (0 ~ 4) | 抓地粒子的质量14/21/False
| ├ 抓地摩擦 | [2] (-2 ~ 4) | 抓地粒子的摩擦15/21/False
| ├ 抓地粘性 | [0.25] (0 ~ 1) | 抓地粒子的粘性16/21/False
| ├ 抓地拖拽 | [0] (-2 ~ 2) | 抓地粒子的空气阻力17/21/False
| ├ 抓地比例 | [1] (0 ~ 2) | 18/21/False
| ├ 启用撕裂 | OFF | 19/21/False
| ├ 撕裂阈值 | [2] (1 ~ 10) | 20/21/False
| └ 限制撕裂速度 | [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）21/21/False
| **模拟设置** | | 3/3/False
| ├ 使用全局 | ON | 在 Pro / 布料模拟下找到全局设置0/11/False
| ├ 启用拖动 | ON | 1/11/False
| ├ 重置比例 | [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。2/11/False
| ├ 模拟 | ON | 3/11/False
| ├ (Simulation FPS: Dynamic) || 4/11/False
| │ 模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├ 时间比例 | [0.65] (0.1 ~ 1) | 5/11/False
| ├ 子步 | [4] (1 ~ 20) | 6/11/False
| ├ 迭代 | [1] (0 ~ 10) | 7/11/False
| ├ 反向偶数子步 | OFF | 8/11/False
| ├ 备用组大小 | [0] (0 ~ 20) | 9/11/False
| ├ 表格大小 | [6] (1 ~ 20) | 10/11/False
| └ 两步求解 | OFF | 11/11/False
