---
locale: zh-rTW
layout: single
title: 模擬
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[專業版](../menu#專業版) > 模擬



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ☑ 啟用</nobr>| [ON] | 
|<nobr> 重置</nobr>|| 
|<nobr> □ <b>布料 1</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 重建網格</nobr>|| 此處的大多數參數需要重建網格才能生效。
|<nobr><img src="/images/icon/ic_line_t.png"/> > 拓撲</nobr>| **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 繩索連接</nobr>| [4] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 內半徑</nobr>| [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 斜坡</nobr>| [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弧形</nobr>| [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 長度</nobr>| [0.25] (0 ~ 0.75) | 長度（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 臂孔</nobr>| [0.5] (0 ~ 1) | 臂孔相對於周長的大小
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 背部長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 側邊長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 水平解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 垂直解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 距離遵從性</nobr>| [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
|<nobr><img src="/images/icon/ic_line_t.png"/> > UV映射</nobr>| **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 上層</nobr>| [2] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>上錨點</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> > 錨點骨骼</nobr>| **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> > 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ └─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 下層</nobr>| [0] (0 ~ 10) | 
|<nobr>│ └─ ⚙️ <b>下錨點</b></nobr>| | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> > 錨點骨骼</nobr>| **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> □ 交換側面</nobr>| [OFF] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> > 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│  └─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 黏性</nobr>| [0] (0 ~ 1) | 
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
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ │ └─ ☑ 玩家</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用彎曲約束</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 縮放</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 自我碰撞</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 啟用撕裂</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>│ └─ ⊖ 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ⚙️ <b>C1 材質</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 玻璃模式</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 光澤作為透明度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 雙面</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 暗邊</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 投擲陰影</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 深度預處理</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 光澤</nobr>| [0.3] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 凸起</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 發光</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 環境光</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 剪裁</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>顏色</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/>☑ 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 混合模式</nobr>| **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>卡通著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 輪廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 光澤</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔軟光澤</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 高光區域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 環境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影區域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔和陰影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>特殊著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 模式</nobr>| **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│ └─ ⊖ 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 紋理</nobr>| **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
|<nobr>└─ ☑ <b>細節圖</b></nobr>| | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> □ <b>(Hexagon Map)</b></nobr>| | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 密度</nobr>| [2] (0 ~ 8) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 大小</nobr>| [1] (0 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 凸起</nobr>| [0.5] (-1 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 噪聲</nobr>| [0.2] (0 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> □ (Use Circle)</nobr>| [OFF] | 
|<nobr> │ └─ ⊖ 柔邊</nobr>| [0.1] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> > 選擇地圖</nobr>| **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖旋轉</nobr>| [0] (-180 ~ 180) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖比例</nobr>| [6] (0 ~ 8) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響環境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響金屬感</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響顏色混合</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 各向異性</nobr>| [0] (-1 ~ 1) | 
|<nobr> └─ ⊖ MIP貼圖偏差</nobr>| [0] (-5 ~ 5) | 調整細節材質的清晰度。
|<nobr> □ <b>布料 2</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 重建網格</nobr>|| 此處的大多數參數需要重建網格才能生效。
|<nobr><img src="/images/icon/ic_line_t.png"/> > 拓撲</nobr>| **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 繩索連接</nobr>| [4] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 內半徑</nobr>| [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 斜坡</nobr>| [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弧形</nobr>| [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 長度</nobr>| [0.25] (0 ~ 0.75) | 長度（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 臂孔</nobr>| [0.5] (0 ~ 1) | 臂孔相對於周長的大小
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 背部長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 側邊長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 水平解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 垂直解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 距離遵從性</nobr>| [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
|<nobr><img src="/images/icon/ic_line_t.png"/> > UV映射</nobr>| **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 上層</nobr>| [2] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>上錨點</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> > 錨點骨骼</nobr>| **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> > 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ └─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 下層</nobr>| [0] (0 ~ 10) | 
|<nobr>│ └─ ⚙️ <b>下錨點</b></nobr>| | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> > 錨點骨骼</nobr>| **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> □ 交換側面</nobr>| [OFF] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> > 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│  └─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 黏性</nobr>| [0] (0 ~ 1) | 
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
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│ │ └─ ☑ 玩家</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用彎曲約束</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 縮放</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 自我碰撞</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 啟用撕裂</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>│ └─ ⊖ 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ⚙️ <b>C2 材質</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 玻璃模式</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 光澤作為透明度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 雙面</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 暗邊</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 投擲陰影</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 深度預處理</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 光澤</nobr>| [0.3] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 凸起</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 發光</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 環境光</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 剪裁</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>顏色</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/>☑ 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 混合模式</nobr>| **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>卡通著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 輪廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 光澤</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔軟光澤</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 高光區域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 環境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影區域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 陰影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 柔和陰影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>特殊著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> > 模式</nobr>| **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│ └─ ⊖ 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 紋理</nobr>| **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
|<nobr>└─ ☑ <b>細節圖</b></nobr>| | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> □ <b>(Hexagon Map)</b></nobr>| | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 密度</nobr>| [2] (0 ~ 8) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 大小</nobr>| [1] (0 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 凸起</nobr>| [0.5] (-1 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> ⊖ 噪聲</nobr>| [0.2] (0 ~ 1) | 
|<nobr> │ <img src="/images/icon/ic_line_t.png"/> □ (Use Circle)</nobr>| [OFF] | 
|<nobr> │ └─ ⊖ 柔邊</nobr>| [0.1] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> > 選擇地圖</nobr>| **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖旋轉</nobr>| [0] (-180 ~ 180) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖比例</nobr>| [6] (0 ~ 8) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 細節圖凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響環境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響金屬感</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 影響顏色混合</nobr>| [0] (0 ~ 1) | 
|<nobr> <img src="/images/icon/ic_line_t.png"/> ⊖ 各向異性</nobr>| [0] (-1 ~ 1) | 
|<nobr> └─ ⊖ MIP貼圖偏差</nobr>| [0] (-5 ~ 5) | 調整細節材質的清晰度。
|<nobr> □ 合併</nobr>| [OFF] | 將布料 1 和 2 合併為單一模擬，這允許兩者之間的碰撞，但會變慢。
|<nobr> □ <b>流體（實驗性）</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>生成</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>位置</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│ │ └─ ⊖ (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>旋轉</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ │ └─ ⊖ (Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 生成半徑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 擴散</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 生成速率</nobr>| [20] (0 ~ 20) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 速度</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 滑鼠 / 手控制</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 自動瞄準</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 最大壽命</nobr>| [10] (5 ~ 15) | 粒子在這段時間後消失並重新生成。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面壽命</nobr>| [0.1] (0 ~ 1) | 撞擊地面後的生存時間。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 平滑度</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **噴霧器** | 淋浴, 噴泉, 噴霧器, 手持式,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>流體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 凝聚力</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 粘度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 緊貼表面</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 目標密度</nobr>| [2] (1 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 凝聚範圍</nobr>| [20] (1 ~ 50) | 凝聚效果的最大距離
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 目標距離</nobr>| [10] (1 ~ 20) | 當凝聚關閉時，粒子之間的最小距離（以毫米計算）。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 高度</nobr>| [0.25] (0 ~ 0.5) | 根據粒子的大小提升粒子
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **水** | 水, 粘性, 沙子,  |
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>渲染</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 渲染粒子</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> □ 渲染水滴</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水滴大小</nobr>| [2] (0 ~ 50) | 水滴大小（以毫米計算）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 按密度縮放</nobr>| [0] (0 ~ 5) | 根據流體的密度縮放水滴大小
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>顏色</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/>☑ 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ └─ ⊖ 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 光滑度</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 發光</nobr>| [0] (0 ~ 1) | 
|<nobr>│ └─ ⊖ 透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦</nobr>| [0] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 空氣阻力</nobr>| [-2] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 水下阻力</nobr>| [-2] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⚙️ <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> ⊖ 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─ ⊖ 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─ ⚙️ <b>碰撞物</b></nobr>| | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 頭部</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 身體</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 腿部</nobr>| [ON] | 
|<nobr>│  <img src="/images/icon/ic_line_t.png"/> ☑ 腳</nobr>| [ON] | 
|<nobr>│  └─ □ 玩家</nobr>| [OFF] | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置),  |
|<nobr> ☑ <b>幾何碰撞器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可見</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 匯出形狀</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>頭部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>脖子</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>胸部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>肋骨</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>腰部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>腹部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>臀部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>肩膀</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>上臂</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>前臂</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>手</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>髖部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>大腿</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>小腿</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>中間位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 中間半徑</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 中間曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>腳</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 起始半徑</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ 結束半徑</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr> ☑ <b>網格碰撞體</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 禁用幾何碰撞體</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ (Skip Edge)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ (Skip Point)</nobr>| [ON] | 
|<nobr>└─ ☑ (Single Collision)</nobr>| [ON] | 
|<nobr> ⚙️ <b>模擬設置</b></nobr>| | 
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
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置),  |
