---
locale: zh-rTW
layout: single
title: 裙擺物理
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/physics_skirt) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_skirt) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_skirt) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_skirt) | [简中](/zh/dancexr/menu/2025.4/actor/physics_skirt)

[物理](../menu#物理) > 裙擺物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ☑ 啟用</nobr>| [ON] | 
|<nobr> ☑ 使用粒子動力學</nobr>| [ON] | 
|<nobr> ⚙️ <b>模擬設置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用拖動</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 模擬</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 反向偶數子步驟</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└─ □ 兩步求解</nobr>| [OFF] | 
|<nobr> <b>主要組</b></nobr>|| 
|<nobr> 選擇骨骼</nobr>|| 
|<nobr> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>└─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>└─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>└─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr> ⊖ 附加組</nobr>| [0] (0 ~ 7) | 
|<nobr> □ <b>(Group 2)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 3)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 4)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 5)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 6)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 7)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr> □ <b>(Group 8)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子動力學</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│ └─ ☑ 質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>橫向關節</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 鎖定 Y</nobr>| [OFF] | 
|<nobr>│ └─ □ 鎖定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│ └─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>└─ ☑ 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
