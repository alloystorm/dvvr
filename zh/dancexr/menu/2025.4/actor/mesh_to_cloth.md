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
|<nobr>合并为一个</nobr>| [OFF] | 
|<nobr>逐渐启用</nobr>| [2] (0 ~ 5) | 
|<nobr>**粒子属性**</nobr>| | 
|<nobr>├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>├&nbsp;粘性</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>├&nbsp;启用弯曲约束</nobr>| [ON] | 
|<nobr>├&nbsp;弯曲顺应性</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;缩放</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;自我碰撞</nobr>| [OFF] | 
|<nobr>├&nbsp;抓地质量</nobr>| [2] (0 ~ 4) | 抓地粒子的质量
|<nobr>├&nbsp;抓地摩擦</nobr>| [2] (-2 ~ 4) | 抓地粒子的摩擦
|<nobr>├&nbsp;抓地粘性</nobr>| [0.25] (0 ~ 1) | 抓地粒子的粘性
|<nobr>├&nbsp;抓地拖拽</nobr>| [0] (-2 ~ 2) | 抓地粒子的空气阻力
|<nobr>├&nbsp;抓地比例</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;启用撕裂</nobr>| [OFF] | 
|<nobr>├&nbsp;撕裂阈值</nobr>| [2] (1 ~ 10) | 
|<nobr>└&nbsp;限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
|<nobr>**模拟设置**</nobr>| | 
|<nobr>├&nbsp;使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>├&nbsp;重置比例</nobr>| [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。
|<nobr>├&nbsp;模拟</nobr>| [ON] | 
|<nobr>├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;两步求解</nobr>| [OFF] | 
