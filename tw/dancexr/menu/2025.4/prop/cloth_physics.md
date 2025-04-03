---
locale: zh-rTW
layout: single
title: 垂懸物理
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > 垂懸物理



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Dangling Physics) | ON | 0/13/True
| 選擇骨骼 || 選擇骨骼1/13/True
| 跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接2/13/True
| **粒子動力學** | | 3/13/True
| ├ (Enable Particle Dynamics) | ON | 0/18/False
| ├ 擺動柔性 | [0.25] (0 ~ 1) | 1/18/False
| ├ 扭轉柔性 | [0.75] (0 ~ 1) | 2/18/False
| ├ 粒子錨點 | [0.5] (0 ~ 1) | 3/18/False
| ├ 減少比率 | [0] (0 ~ 1) | 在每個層級減少質量4/18/False
| ├ 可視化 | OFF | 5/18/False
| ├ 最大角速度 | [2] (0 ~ 4) | 6/18/False
| ├ 慣性 | [2] (1 ~ 5) | 7/18/False
| ├ 軟化 | [0] (0 ~ 1) | 軟化粒子約束。8/18/False
| ├ 粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）9/18/False
| ├ 重力 | [9.8] (-9.8 ~ 9.8) | 10/18/False
| ├ 摩擦 | [1] (0 ~ 2) | 11/18/False
| ├ 地面摩擦 | [1] (-2 ~ 2) | 12/18/False
| ├ 空氣阻力 | [0] (0 ~ 2) | 空氣阻抗13/18/False
| ├ 水下阻力 | [1] (0 ~ 2) | 水下阻抗14/18/False
| ├ 浮力 | [-0.1] (-1 ~ 1) | 15/18/False
| ├ **風** | | 16/18/False
| │ ├ 風的影響 | [0.25] (0 ~ 1) | 0/3/False
| │ ├ 湍流比例 | [0] (-2 ~ 2) | 1/3/False
| │ ├ 湍流強度 | [1] (0 ~ 2) | 2/3/False
| │ └ 湍流時間比例 | [0] (-4 ~ 4) | 3/3/False
| ├ **碰撞物** | | 17/18/False
| │ ├ 頭部 | ON | 0/8/False
| │ ├ 身體 | ON | 1/8/False
| │ ├ 胸部 | ON | 2/8/False
| │ ├ 臀部 | ON | 3/8/False
| │ ├ (Arms) | ON | 4/8/False
| │ ├ 手 | ON | 5/8/False
| │ ├ 腿部 | ON | 6/8/False
| │ ├ 腳 | ON | 7/8/False
| │ └ 玩家 | ON | 8/8/False
| └ **模擬設置** | | 18/18/False
|   ├ 使用全局 | ON | 在專業版/布料模擬下查找全局設置0/10/False
|   ├ 啟用拖動 | ON | 1/10/False
|   ├ 模擬 | ON | 2/10/False
|   ├ (Simulation FPS: Dynamic) || 3/10/False
|   │ 模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|   ├ 時間比例 | [0.65] (0.1 ~ 1) | 4/10/False
|   ├ 子步驟 | [4] (1 ~ 20) | 5/10/False
|   ├ 迭代次數 | [1] (0 ~ 10) | 6/10/False
|   ├ 反向偶數子步驟 | OFF | 7/10/False
|   ├ 替代組大小 | [0] (0 ~ 20) | 8/10/False
|   ├ 數據表大小 | [6] (1 ~ 20) | 9/10/False
|   └ 兩步求解 | OFF | 10/10/False
| 彈簧 | [0.5] (0 ~ 5) | 4/13/True
| 減震 | [0.01] (0 ~ 0.1) | 5/13/True
| 減少比率 | [0.25] (0 ~ 1) | 在每個級別降低剛度6/13/True
| 扭轉限制 | [5] (0 ~ 180) | 限制扭轉旋轉7/13/True
| 限制力量 | [3] (0 ~ 8) | 8/13/True
| 質量 | [0.05] (0 ~ 0.1) | 9/13/True
| 拖曳 | [1] (0 ~ 10) | 10/13/True
| 碰撞體半徑 | [0.01] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。11/13/True
| 碰撞體長度 | [0.9] (0 ~ 1) | 12/13/True
| 錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼13/13/True
| 預設 | **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2),  |
