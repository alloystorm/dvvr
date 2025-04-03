---
locale: zh-rTW
layout: single
title: 網格轉布料
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[專業版](../menu#專業版) > 網格轉布料



| Setting | Value | Description |
| :--- | --- | :--- |
| 合併為一 | OFF | 
| 逐漸啟用 | [2] (0 ~ 5) | 
| **粒子屬性** | | 
| ├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| ├&nbsp;黏性 | [0] (0 ~ 1) | 
| ├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| ├&nbsp;摩擦 | [1] (0 ~ 2) | 
| ├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| ├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| ├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| ├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| ├&nbsp;**風** | | 
| │&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| ├&nbsp;**碰撞物** | | 
| │&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;├&nbsp;手 | ON | 
| │&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;└&nbsp;玩家 | ON | 
| ├&nbsp;啟用彎曲約束 | ON | 
| ├&nbsp;彎曲順應性 | [0] (0 ~ 1) | 
| ├&nbsp;縮放 | [1] (0 ~ 2) | 
| ├&nbsp;自我碰撞 | OFF | 
| ├&nbsp;抓取質量 | [2] (0 ~ 4) | 抓取粒子的質量
| ├&nbsp;抓取摩擦 | [2] (-2 ~ 4) | 抓取粒子的摩擦
| ├&nbsp;抓取黏性 | [0.25] (0 ~ 1) | 抓取粒子的黏性
| ├&nbsp;抓取阻力 | [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
| ├&nbsp;抓取比例 | [1] (0 ~ 2) | 
| ├&nbsp;啟用撕裂 | OFF | 
| ├&nbsp;撕裂閾值 | [2] (1 ~ 10) | 
| └&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
| **模擬設置** | | 
| ├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| ├&nbsp;啟用拖動 | ON | 
| ├&nbsp;重置比例 | [1] (1 ~ 5) | 從較大比例過渡到布料，以幫助適應重置。
| ├&nbsp;模擬 | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| ├&nbsp;子步驟 | [4] (1 ~ 20) | 
| ├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| ├&nbsp;反向偶數子步驟 | OFF | 
| ├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| ├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| └&nbsp;兩步求解 | OFF | 
