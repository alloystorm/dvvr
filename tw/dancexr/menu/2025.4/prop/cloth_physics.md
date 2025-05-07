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
|<nobr> ☑ 啟用</nobr>| [ON] | 
|<nobr> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr> ☑ <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ └─ ☑ 玩家</nobr>| [ON] | 
|<nobr>└─ ⚙️ <b>模擬設置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 啟用拖動</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模擬</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> > 模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶數子步驟</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─ □ 兩步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 彈簧</nobr>| [0.5] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 減震</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率</nobr>| [0.25] (0 ~ 1) | 在每個級別降低剛度
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 扭轉限制</nobr>| [5] (0 ~ 180) | 限制扭轉旋轉
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 限制力量</nobr>| [3] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拖曳</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 碰撞體半徑</nobr>| [0.01] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 碰撞體長度</nobr>| [0.9] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2),  |
