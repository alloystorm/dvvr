---
locale: zh-rTW
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[(Prop)](../menu#(Prop)) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
| 禁用 PMX 物理 | OFF | 禁用 PMX 物理以使用 XPS 工具
| 減少約束 | ON | 使用減少約束的實驗設置以允許更平滑的模擬
| **碰撞** | | 
| ├&nbsp;靜態包含 | ON | 
| ├&nbsp;靜態排除 | ON | 
| ├&nbsp;動態包含 | ON | 
| └&nbsp;動態排除 | ON | 
| **線性運動** | | Settings for linear movements
| ├&nbsp;限制 | 自動 | 自動, 有限制, 鎖定, 自由, 
| ├&nbsp;鎖定 0 限制 | ON | 
| ├&nbsp;最小彈簧力 | [5] (0 ~ 15) | 
| ├&nbsp;最大限制 | [0.05] (0.05 ~ 0.1) | 
| ├&nbsp;彈性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接觸距離 | [0.5] (0 ~ 1) | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| └&nbsp;拖曳 | [0.15] (0 ~ 1) | 
| **角運動** | | Settings for angular movements
| ├&nbsp;限制 | 自動 | 自動, 有限制, 鎖定, 自由, 
| ├&nbsp;鎖定 0 限制 | ON | 
| ├&nbsp;最小彈簧力 | [5] (0 ~ 15) | 
| ├&nbsp;最大限制 | [90] (3 ~ 90) | 
| ├&nbsp;彈性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接觸距離 | [0.5] (0 ~ 1) | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| └&nbsp;拖曳 | [0.15] (0 ~ 1) | 
| **線性驅動** | | Apply linear drive
| ├&nbsp;啟用 | ON | 
| ├&nbsp;彈簧力量 | [3] (0 ~ 5) | 
| └&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| **角驅動** | | Apply angular drive
| ├&nbsp;啟用 | ON | 
| ├&nbsp;彈簧力量 | [0.1] (0 ~ 5) | 
| └&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| **線性動作** | | Settings for linear motion
| ├&nbsp;堅固性 | [0] (-1 ~ 1) | 
| ├&nbsp;主驅動力 | [5] (0 ~ 8) | 
| ├&nbsp;第二驅動力 | [3] (0 ~ 8) | 
| ├&nbsp;目標位置 | 零 | 零, 中心, 最小, 最大, 
| ├&nbsp;盡可能鎖定 | ON | 
| ├&nbsp;加速度模式 | ON | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| ├&nbsp;拖曳 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 通過忽略關節限制進一步減少約束
| **角動作** | | Settings for angular motion
| ├&nbsp;堅固性 | [0] (-1 ~ 1) | 
| ├&nbsp;主驅動力 | [5] (0 ~ 8) | 
| ├&nbsp;第二驅動力 | [5] (0 ~ 8) | 
| ├&nbsp;目標位置 | 零 | 零, 中心, 最小, 最大, 
| ├&nbsp;盡可能鎖定 | OFF | 
| ├&nbsp;加速度模式 | ON | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| ├&nbsp;拖曳 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 通過忽略關節限制進一步減少約束
| **選項** | | 
| ├&nbsp;最小阻力 | [0] (0 ~ 1) | 自動模式下的最小阻力值
| ├&nbsp;阻力比例 | [1] (0 ~ 5) | 自動模式下施加於阻力值的比例
| ├&nbsp;最小質量 | [0] (0 ~ 1) | 自動模式下的最小質量值
| ├&nbsp;質量比例 | [1] (0 ~ 10) | 自動模式下施加於質量值的比例
| ├&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| ├&nbsp;投影距離 | [0.05] (0 ~ 0.1) | 當物體相對於靜止位置的距離超過此值時強制重置關節
| └&nbsp;投影角度 | [5] (0 ~ 60) | 當物體相對於靜止位置的角度超過此值時強制重置關節
| 自動重置閾值 | [35] (0 ~ 100) | 當速度超過該值時，自動重置骨骼及其子物件
| **自動重置** | | 
| └&nbsp;閾值 | [30] (0 ~ 50) | 
| **身體碰撞器** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;大小 | [0.5] (0 ~ 1) | 
| ├&nbsp;頭部半徑 | [1] (0 ~ 2) | 
| ├&nbsp;手臂半徑 | [1] (0 ~ 2) | 
| ├&nbsp;前臂 | [1] (0 ~ 2) | 
| ├&nbsp;胸部寬度 | [1] (0 ~ 2) | 
| ├&nbsp;腰部寬度 | [0.5] (0 ~ 1) | 
| ├&nbsp;臀部寬度 | [0] (-1 ~ 1) | 
| ├&nbsp;臀部半徑 | [1] (0 ~ 2) | 
| ├&nbsp;臀部位置 || 
| ├&nbsp;(X) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Y) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Z) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;腹部半徑 | [1] (0 ~ 2) | 
| ├&nbsp;腹部位置 | [0] (-1 ~ 1) | 
| ├&nbsp;腿部半徑 | [1] (0 ~ 2) | 
| ├&nbsp;大腿前/後 | [0] (-1 ~ 1) | 
| ├&nbsp;大腿起始位置 | [0] (0 ~ 1) | 
| ├&nbsp;手 | [0] (0 ~ 1) | 
| ├&nbsp;可視化 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (amy), (misaki),  |
| **胸部物理**<sup>[PRO]</sup> | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;選擇骨骼 || 
| ├&nbsp;彈簧力量 | [1.5] (0 ~ 5) | 
| ├&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| ├&nbsp;質量 | [0.1] (0 ~ 1) | 
| ├&nbsp;拖曳 | [0.1] (0 ~ 10) | 
| ├&nbsp;反重力 | [10] (0 ~ 45) | 
| ├&nbsp;**旋轉限制** | | 
| │&nbsp;├&nbsp;上限 | [100] (0 ~ 120) | 
| │&nbsp;├&nbsp;下限 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;左右限制 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;彈簧力量 | [1.25] (0 ~ 10) | 超過限制時的彈簧力
| │&nbsp;├&nbsp;阻尼 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;接觸距離 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;彈跳 | [0.2] (0 ~ 1) | 
| ├&nbsp;**錨點** | | 
| │&nbsp;├&nbsp;(X) | [-0.03] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [0.03] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.08] (-0.2 ~ 0.2) | 
| ├&nbsp;**中心** | | 
| │&nbsp;├&nbsp;(X) | [0.02] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [-0.05] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.025] (-0.2 ~ 0.2) | 
| ├&nbsp;**碰撞** | | 
| │&nbsp;├&nbsp;與手臂碰撞 | OFF | 
| │&nbsp;├&nbsp;碰撞體半徑 | [0.07] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;碰撞體長度 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;碰撞體曲線 | [2] (-2 ~ 2) | 與布料模擬配合使用。
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;啟用乳頭 | ON | 與布料模擬配合使用。
| │&nbsp;├&nbsp;**乳頭位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [-0.18] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.09] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0.2] (0 ~ 1) | 
| │&nbsp;└&nbsp;乳頭大小 | [0.1] (0 ~ 1) | 
| ├&nbsp;**(Softbody)** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;關節 || 
| │&nbsp;├&nbsp;深度 | [0.4] (0 ~ 1) | 
| │&nbsp;├&nbsp;包含中心 | ON | 
| │&nbsp;├&nbsp;體積約束 | [0.85] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;內部約束 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;表面約束 | [0.75] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;旋轉約束 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;邊緣鎖定 | [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| │&nbsp;├&nbsp;中心鎖定 | [1] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;阻尼 | [15] (0 ~ 40) | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風的影響 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身體 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**模擬設置** | | 
| │&nbsp;│&nbsp;├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| │&nbsp;│&nbsp;├&nbsp;啟用拖動 | ON | 
| │&nbsp;│&nbsp;├&nbsp;模擬 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;│&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;│&nbsp;├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;子步驟 | [4] (1 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;反向偶數子步驟 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| │&nbsp;│&nbsp;└&nbsp;兩步求解 | OFF | 
| │&nbsp;└&nbsp;(Presets: Boobs) || 
| │&nbsp;&nbsp;&nbsp;預設 | **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
| ├&nbsp;僅限軟體體 | OFF | 禁用物理連接，僅使用軟體體粒子。
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| **裙擺物理**<sup>[PRO]</sup> | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;使用粒子動力學 | ON | 
| ├&nbsp;**模擬設置** | | 
| │&nbsp;├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| │&nbsp;├&nbsp;啟用拖動 | ON | 
| │&nbsp;├&nbsp;模擬 | ON | 
| │&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;├&nbsp;子步驟 | [4] (1 ~ 20) | 
| │&nbsp;├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| │&nbsp;├&nbsp;反向偶數子步驟 | OFF | 
| │&nbsp;├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| │&nbsp;├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| │&nbsp;└&nbsp;兩步求解 | OFF | 
| ├&nbsp;主要組 || 
| ├&nbsp;選擇骨骼 || 
| ├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| ├&nbsp;閉環 | ON | 每一層閉環的骨骼
| ├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| ├&nbsp;**粒子動力學** | | 
| │&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| ├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| ├&nbsp;**父子關節** | | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| ├&nbsp;**橫向關節** | | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;└&nbsp;鎖定 Z | OFF | 
| ├&nbsp;**碰撞體** | | 
| │&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| ├&nbsp;附加組 | [0] (0 ~ 7) | 
| ├&nbsp;**(Group 2)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 3)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 4)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 5)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 6)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 7)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| ├&nbsp;**(Group 8)** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;選擇骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 設置在建立橫向連接時使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
| │&nbsp;├&nbsp;閉環 | ON | 每一層閉環的骨骼
| │&nbsp;├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| │&nbsp;├&nbsp;**粒子動力學** | | 
| │&nbsp;│&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;橫向柔性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;橫向錨點 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;│&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;│&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理屬性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖曳 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重疊 | [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
| │&nbsp;│&nbsp;├&nbsp;質量分佈 | [0] (-1 ~ 1) | 在每個層級減少質量
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解迭代次數 | [20] (1 ~ 150) | 解決碰撞時的迭代次數
| │&nbsp;│&nbsp;└&nbsp;質心 | 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
| │&nbsp;├&nbsp;**父子關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;擺動驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭轉驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| │&nbsp;├&nbsp;**橫向關節** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線性驅動 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驅動 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驅動阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;鎖定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;鎖定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞體** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞體類型 | **盒子** | 盒子, 膠囊, 球體,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞體長度 | [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
| │&nbsp;└&nbsp;使用主要組設置 | ON | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| **頭髮物理** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;選擇骨骼 || 選擇骨骼
| ├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| ├&nbsp;**粒子動力學** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;└&nbsp;**模擬設置** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| │&nbsp;&nbsp;&nbsp;├&nbsp;啟用拖動 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;模擬 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;子步驟 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;反向偶數子步驟 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;兩步求解 | OFF | 
| ├&nbsp;彈簧 | [1.25] (0 ~ 5) | 
| ├&nbsp;減震 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;減少比率 | [0.25] (0 ~ 1) | 在每個級別降低剛度
| ├&nbsp;扭轉限制 | [5] (0 ~ 180) | 限制扭轉旋轉
| ├&nbsp;限制力量 | [3] (0 ~ 8) | 
| ├&nbsp;質量 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;拖曳 | [1] (0 ~ 10) | 
| ├&nbsp;碰撞體半徑 | [0.005] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
| ├&nbsp;碰撞體長度 | [0.9] (0 ~ 1) | 
| ├&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (momiji bob), (Preset 1),  |
| **垂懸物理** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;選擇骨骼 || 選擇骨骼
| ├&nbsp;跳過前 X 根骨骼 | [0] (0 ~ 5) | 對前 x 級不創建物理連接
| ├&nbsp;**粒子動力學** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;擺動柔性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭轉柔性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子錨點 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 在每個層級減少質量
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;軟化 | [0] (0 ~ 1) | 軟化粒子約束。
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空氣阻力 | [0] (0 ~ 2) | 空氣阻抗
| │&nbsp;├&nbsp;水下阻力 | [1] (0 ~ 2) | 水下阻抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風的影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流時間比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞物** | | 
| │&nbsp;│&nbsp;├&nbsp;頭部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身體 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腳 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;└&nbsp;**模擬設置** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;使用全局 | ON | 在專業版/布料模擬下查找全局設置
| │&nbsp;&nbsp;&nbsp;├&nbsp;啟用拖動 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;模擬 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;模擬幀率 | **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;時間比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;子步驟 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;迭代次數 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;反向偶數子步驟 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;替代組大小 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;數據表大小 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;兩步求解 | OFF | 
| ├&nbsp;彈簧 | [0.5] (0 ~ 5) | 
| ├&nbsp;減震 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;減少比率 | [0.25] (0 ~ 1) | 在每個級別降低剛度
| ├&nbsp;扭轉限制 | [5] (0 ~ 180) | 限制扭轉旋轉
| ├&nbsp;限制力量 | [3] (0 ~ 8) | 
| ├&nbsp;質量 | [0.05] (0 ~ 0.1) | 
| ├&nbsp;拖曳 | [1] (0 ~ 10) | 
| ├&nbsp;碰撞體半徑 | [0.01] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
| ├&nbsp;碰撞體長度 | [0.9] (0 ~ 1) | 
| ├&nbsp;錨點位置 | [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2),  |
| **分離物體** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;選擇骨骼 || 
| ├&nbsp;重力 | ON | 
| ├&nbsp;質量 | [0.1] (0 ~ 10) | 
| ├&nbsp;減震 | [0] (0 ~ 1) | 
| ├&nbsp;碰撞體 | 球體 | 無, 球體, 膠囊, 
| ├&nbsp;碰撞體半徑 | [0.1] (0 ~ 1) | 
| └&nbsp;碰撞體長度 | [0.3] (0 ~ 2) | 
| (Presets: Default (Reset)) || 
| 預設 | **預設 (重置)** | 預設 (重置),  |
