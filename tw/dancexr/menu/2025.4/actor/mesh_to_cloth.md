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
|<nobr> □ 合併為一</nobr>| [OFF] | 
|<nobr> ☑ 逐漸啟用</nobr>| [2] (0 ~ 5) | 
|<nobr> ⚙️ **粒子屬性**</nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 黏性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ **風**</nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ **碰撞物**</nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ └─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用彎曲約束</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 縮放</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 自我碰撞</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用撕裂</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>└─ ⊖ 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr> ⚙️ **模擬設置**</nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用拖動</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 重置比例</nobr>| [1] (1 ~ 5) | 從較大比例過渡到布料，以幫助適應重置。
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 模擬</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 反向偶數子步驟</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└─ □ 兩步求解</nobr>| [OFF] | 
