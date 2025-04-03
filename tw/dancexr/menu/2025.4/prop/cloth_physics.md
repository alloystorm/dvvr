---
locale: zh-rTW
layout: single
title: 垂懸物理
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > 垂懸物理



| Setting | Value | Description |
| :--- | --- | :--- |
| 啟用 | ON | 
| 選擇骨骼 || 選擇骨骼
| 跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| **粒子動力學** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| ├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| ├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| ├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| ├&nbsp;可視化 | OFF | 
| ├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| ├&nbsp;慣性 | [2] (1 ~ 5) | 
| ├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| ├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
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
| └&nbsp;**模擬設置** | | 
| &nbsp;&nbsp;├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| &nbsp;&nbsp;├&nbsp;啟用拖動 | ON | 
| &nbsp;&nbsp;├&nbsp;模擬 | ON | 
| &nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| &nbsp;&nbsp;│&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| &nbsp;&nbsp;├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;子步驟 | [4] (1 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;反向偶數子步驟 | OFF | 
| &nbsp;&nbsp;├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| &nbsp;&nbsp;└&nbsp;兩步求解 | OFF | 
| 彈簧 | [0.5] (0 ~ 5) | 
| 減震 | [0.01] (0 ~ 0.1) | 
| 減少比率 | [0.25] (0 ~ 1) | 在每個級別降低剛度
| 扭轉限制 | [5] (0 ~ 180) | 限制扭轉旋轉
| 限制力量 | [3] (0 ~ 8) | 
| 質量 | [0.05] (0 ~ 0.1) | 
| 拖曳 | [1] (0 ~ 10) | 
| 碰撞體半徑 | [0.01] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
| 碰撞體長度 | [0.9] (0 ~ 1) | 
| 錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| (Presets: Default (Reset)) || 
| 預設 | **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2),  |
