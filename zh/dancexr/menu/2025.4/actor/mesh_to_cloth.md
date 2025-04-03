---
locale: zh-rCN
layout: single
title: 网格转布料
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[专业版](../menu#专业版) > 网格转布料



| Setting | Value | Description |
| :--- | --- | :--- |
| 合并为一个 | OFF | 
| 逐渐启用 | [2] (0 ~ 5) | 
| **粒子属性** | | 
| ├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| ├&nbsp;粘性 | [0] (0 ~ 1) | 
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
| ├&nbsp;启用弯曲约束 | ON | 
| ├&nbsp;弯曲顺应性 | [0] (0 ~ 1) | 
| ├&nbsp;缩放 | [1] (0 ~ 2) | 
| ├&nbsp;自我碰撞 | OFF | 
| ├&nbsp;抓地质量 | [2] (0 ~ 4) | 抓地粒子的质量
| ├&nbsp;抓地摩擦 | [2] (-2 ~ 4) | 抓地粒子的摩擦
| ├&nbsp;抓地粘性 | [0.25] (0 ~ 1) | 抓地粒子的粘性
| ├&nbsp;抓地拖拽 | [0] (-2 ~ 2) | 抓地粒子的空气阻力
| ├&nbsp;抓地比例 | [1] (0 ~ 2) | 
| ├&nbsp;启用撕裂 | OFF | 
| ├&nbsp;撕裂阈值 | [2] (1 ~ 10) | 
| └&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
| **模拟设置** | | 
| ├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| ├&nbsp;启用拖动 | ON | 
| ├&nbsp;重置比例 | [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。
| ├&nbsp;模拟 | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| ├&nbsp;子步 | [4] (1 ~ 20) | 
| ├&nbsp;迭代 | [1] (0 ~ 10) | 
| ├&nbsp;反向偶数子步 | OFF | 
| ├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| ├&nbsp;表格大小 | [6] (1 ~ 20) | 
| └&nbsp;两步求解 | OFF | 
