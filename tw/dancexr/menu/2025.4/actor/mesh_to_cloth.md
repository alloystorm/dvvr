---
locale: zh-rTW
layout: single
title: 網格轉布料
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[專業版](../menu#專業版) > 網格轉布料



| Setting | Value | Description |
| :--- | --- | :--- |
| 合併為一 | OFF | 0/3/False
| 逐漸啟用 | [2] (0 ~ 5) | 1/3/False
| **粒子屬性** | | 2/3/False
| ├ 粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）0/21/False
| ├ 黏性 | [0] (0 ~ 1) | 1/21/False
| ├ 重力 | [9.8] (-9.8 ~ 9.8) | 2/21/False
| ├ 摩擦 | [1] (0 ~ 2) | 3/21/False
| ├ 地面摩擦 | [1] (-2 ~ 2) | 4/21/False
| ├ 空氣阻力 | [0] (0 ~ 2) | 空氣阻抗5/21/False
| ├ 水下阻力 | [1] (0 ~ 2) | 水下阻抗6/21/False
| ├ 浮力 | [-0.1] (-1 ~ 1) | 7/21/False
| ├ **風** | | 8/21/False
| │ ├ 風的影響 | [0.25] (0 ~ 1) | 0/3/False
| │ ├ 湍流比例 | [0] (-2 ~ 2) | 1/3/False
| │ ├ 湍流強度 | [1] (0 ~ 2) | 2/3/False
| │ └ 湍流時間比例 | [0] (-4 ~ 4) | 3/3/False
| ├ **碰撞物** | | 9/21/False
| │ ├ 頭部 | ON | 0/8/False
| │ ├ 身體 | ON | 1/8/False
| │ ├ 胸部 | ON | 2/8/False
| │ ├ 臀部 | ON | 3/8/False
| │ ├ (Arms) | ON | 4/8/False
| │ ├ 手 | ON | 5/8/False
| │ ├ 腿部 | ON | 6/8/False
| │ ├ 腳 | ON | 7/8/False
| │ └ 玩家 | ON | 8/8/False
| ├ 啟用彎曲約束 | ON | 10/21/False
| ├ 彎曲順應性 | [0] (0 ~ 1) | 11/21/False
| ├ 縮放 | [1] (0 ~ 2) | 12/21/False
| ├ 自我碰撞 | OFF | 13/21/False
| ├ 抓取質量 | [2] (0 ~ 4) | 抓取粒子的質量14/21/False
| ├ 抓取摩擦 | [2] (-2 ~ 4) | 抓取粒子的摩擦15/21/False
| ├ 抓取黏性 | [0.25] (0 ~ 1) | 抓取粒子的黏性16/21/False
| ├ 抓取阻力 | [0] (-2 ~ 2) | 抓取粒子的空氣阻抗17/21/False
| ├ 抓取比例 | [1] (0 ~ 2) | 18/21/False
| ├ 啟用撕裂 | OFF | 19/21/False
| ├ 撕裂閾值 | [2] (1 ~ 10) | 20/21/False
| └ 限制撕裂速度 | [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀21/21/False
| **模擬設置** | | 3/3/False
| ├ 使用全局 | ON | 在專業版/布料模擬下查找全局設置0/11/False
| ├ 啟用拖動 | ON | 1/11/False
| ├ 重置比例 | [1] (1 ~ 5) | 從較大比例過渡到布料，以幫助適應重置。2/11/False
| ├ 模擬 | ON | 3/11/False
| ├ (Simulation FPS: Dynamic) || 4/11/False
| │ 模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├ 時間比例 | [0.65] (0.1 ~ 1) | 5/11/False
| ├ 子步驟 | [4] (1 ~ 20) | 6/11/False
| ├ 迭代次數 | [1] (0 ~ 10) | 7/11/False
| ├ 反向偶數子步驟 | OFF | 8/11/False
| ├ 替代組大小 | [0] (0 ~ 20) | 9/11/False
| ├ 數據表大小 | [6] (1 ~ 20) | 10/11/False
| └ 兩步求解 | OFF | 11/11/False
