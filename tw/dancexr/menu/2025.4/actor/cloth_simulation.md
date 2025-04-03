---
locale: zh-rTW
layout: single
title: 模擬
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[專業版](../menu#專業版) > 模擬



| Setting | Value | Description |
| :--- | --- | :--- |
| 啟用 | ON | 
| 重置 || 
| **布料 1** | | 
| ├&nbsp;啟用 | OFF | 
| ├&nbsp;重建網格 || 此處的大多數參數需要重建網格才能生效。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;拓撲 | **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
| ├&nbsp;繩索連接 | [4] (1 ~ 10) | 
| ├&nbsp;內半徑 | [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
| ├&nbsp;斜坡 | [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
| ├&nbsp;弧形 | [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
| ├&nbsp;長度 | [0.25] (0 ~ 0.75) | 長度（以米為單位）
| ├&nbsp;臂孔 | [0.5] (0 ~ 1) | 臂孔相對於周長的大小
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
| ├&nbsp;背部長度 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;側邊長度 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平解析度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直解析度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距離遵從性 | [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV映射 | **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
| ├&nbsp;**錨點** | | 
| │&nbsp;├&nbsp;上層 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**上錨點** | | 
| │&nbsp;│&nbsp;├&nbsp;錨點選擇 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;選擇偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;錨點骨骼 | **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;鎖定模式 | **無** | 無, 鎖定, 鎖定高度, 粘性,  |
| │&nbsp;│&nbsp;├&nbsp;錨點位置 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;錨點旋轉 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;下層 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**下錨點** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點選擇 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;選擇偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;錨點骨骼 | **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;交換側面 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;鎖定模式 | **無** | 無, 鎖定, 鎖定高度, 粘性,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點位置 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點旋轉 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子屬性** | | 
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;黏性 | [0] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;啟用彎曲約束 | ON | 
| │&nbsp;├&nbsp;彎曲順應性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;縮放 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自我碰撞 | OFF | 
| │&nbsp;├&nbsp;抓取質量 | [2] (0 ~ 4) | 抓取粒子的質量
| │&nbsp;├&nbsp;抓取摩擦 | [2] (-2 ~ 4) | 抓取粒子的摩擦
| │&nbsp;├&nbsp;抓取黏性 | [0.25] (0 ~ 1) | 抓取粒子的黏性
| │&nbsp;├&nbsp;抓取阻力 | [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
| │&nbsp;├&nbsp;抓取比例 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;啟用撕裂 | OFF | 
| │&nbsp;├&nbsp;撕裂閾值 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
| └&nbsp;(Presets: Top) || 
| &nbsp;&nbsp;預設 | **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C1 材質** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;預設 | **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;玻璃模式 | OFF | 
| ├&nbsp;光澤作為透明度 | OFF | 
| ├&nbsp;雙面 | ON | 
| ├&nbsp;暗邊 | [1] (0 ~ 1) | 
| ├&nbsp;投擲陰影 | [0.5] (0 ~ 1) | 
| ├&nbsp;深度預處理 | [0.8] (0 ~ 1) | 
| ├&nbsp;光澤 | [0.3] (0 ~ 1) | 
| ├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| ├&nbsp;凸起 | [0.2] (0 ~ 1) | 
| ├&nbsp;發光 | [0] (0 ~ 10) | 
| ├&nbsp;環境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪裁 | [0] (0 ~ 1) | 
| ├&nbsp;**顏色** | | 
| │&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;混合模式 | **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;預設 | **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| ├&nbsp;**卡通著色器** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;陰影 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;輪廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;光澤 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔軟光澤 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光區域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;環境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影區域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和陰影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| ├&nbsp;**特殊著色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;紋理 | **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
| └&nbsp;**細節圖** | | 
| &nbsp;&nbsp;├&nbsp;啟用 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;啟用 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;大小 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;凸起 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;噪聲 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;柔邊 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;選擇地圖 | **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
| &nbsp;&nbsp;├&nbsp;細節圖旋轉 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;細節圖比例 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;細節圖凹凸 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響環境光遮蔽 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響光滑度 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響金屬感 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響顏色混合 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;各向異性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP貼圖偏差 | [0] (-5 ~ 5) | 調整細節材質的清晰度。
| **布料 2** | | 
| ├&nbsp;啟用 | OFF | 
| ├&nbsp;重建網格 || 此處的大多數參數需要重建網格才能生效。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;拓撲 | **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
| ├&nbsp;繩索連接 | [4] (1 ~ 10) | 
| ├&nbsp;內半徑 | [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
| ├&nbsp;斜坡 | [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
| ├&nbsp;弧形 | [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
| ├&nbsp;長度 | [0.25] (0 ~ 0.75) | 長度（以米為單位）
| ├&nbsp;臂孔 | [0.5] (0 ~ 1) | 臂孔相對於周長的大小
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
| ├&nbsp;背部長度 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;側邊長度 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平解析度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直解析度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距離遵從性 | [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV映射 | **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
| ├&nbsp;**錨點** | | 
| │&nbsp;├&nbsp;上層 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**上錨點** | | 
| │&nbsp;│&nbsp;├&nbsp;錨點選擇 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;選擇偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;錨點骨骼 | **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;鎖定模式 | **無** | 無, 鎖定, 鎖定高度, 粘性,  |
| │&nbsp;│&nbsp;├&nbsp;錨點位置 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;錨點旋轉 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;下層 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**下錨點** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點選擇 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;選擇偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;錨點骨骼 | **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;交換側面 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;鎖定模式 | **無** | 無, 鎖定, 鎖定高度, 粘性,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點位置 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;錨點旋轉 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子屬性** | | 
| │&nbsp;├&nbsp;粒子半徑 | [5] (1 ~ 20) | 粒子大小（毫米）
| │&nbsp;├&nbsp;黏性 | [0] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;啟用彎曲約束 | ON | 
| │&nbsp;├&nbsp;彎曲順應性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;縮放 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自我碰撞 | OFF | 
| │&nbsp;├&nbsp;抓取質量 | [2] (0 ~ 4) | 抓取粒子的質量
| │&nbsp;├&nbsp;抓取摩擦 | [2] (-2 ~ 4) | 抓取粒子的摩擦
| │&nbsp;├&nbsp;抓取黏性 | [0.25] (0 ~ 1) | 抓取粒子的黏性
| │&nbsp;├&nbsp;抓取阻力 | [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
| │&nbsp;├&nbsp;抓取比例 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;啟用撕裂 | OFF | 
| │&nbsp;├&nbsp;撕裂閾值 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
| └&nbsp;(Presets: Skirt) || 
| &nbsp;&nbsp;預設 | **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C2 材質** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;預設 | **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;玻璃模式 | OFF | 
| ├&nbsp;光澤作為透明度 | OFF | 
| ├&nbsp;雙面 | ON | 
| ├&nbsp;暗邊 | [1] (0 ~ 1) | 
| ├&nbsp;投擲陰影 | [0.5] (0 ~ 1) | 
| ├&nbsp;深度預處理 | [0.8] (0 ~ 1) | 
| ├&nbsp;光澤 | [0.3] (0 ~ 1) | 
| ├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| ├&nbsp;凸起 | [0.2] (0 ~ 1) | 
| ├&nbsp;發光 | [0] (0 ~ 10) | 
| ├&nbsp;環境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪裁 | [0] (0 ~ 1) | 
| ├&nbsp;**顏色** | | 
| │&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;混合模式 | **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;預設 | **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| ├&nbsp;**卡通著色器** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;陰影 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;輪廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;光澤 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔軟光澤 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光區域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;環境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影區域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和陰影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| ├&nbsp;**特殊著色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;紋理 | **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
| └&nbsp;**細節圖** | | 
| &nbsp;&nbsp;├&nbsp;啟用 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;啟用 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;大小 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;凸起 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;噪聲 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;柔邊 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;選擇地圖 | **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
| &nbsp;&nbsp;├&nbsp;細節圖旋轉 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;細節圖比例 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;細節圖凹凸 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響環境光遮蔽 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響光滑度 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響金屬感 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影響顏色混合 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;各向異性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP貼圖偏差 | [0] (-5 ~ 5) | 調整細節材質的清晰度。
| 合併 | OFF | 將布料 1 和 2 合併為單一模擬，這允許兩者之間的碰撞，但會變慢。
| **流體（實驗性）** | | 
| ├&nbsp;啟用 | OFF | 
| ├&nbsp;**生成** | | 
| │&nbsp;├&nbsp;**位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] ((Unlimited)) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [2.5] ((Unlimited)) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] ((Unlimited)) | 
| │&nbsp;├&nbsp;**旋轉** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;生成半徑 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;擴散 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;生成速率 | [20] (0 ~ 20) | 
| │&nbsp;├&nbsp;速度 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;滑鼠 / 手控制 | OFF | 
| │&nbsp;├&nbsp;自動瞄準 | ON | 
| │&nbsp;├&nbsp;最大壽命 | [10] (5 ~ 15) | 粒子在這段時間後消失並重新生成。
| │&nbsp;├&nbsp;地面壽命 | [0.1] (0 ~ 1) | 撞擊地面後的生存時間。
| │&nbsp;├&nbsp;平滑度 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sprinkler) || 
| │&nbsp;&nbsp;&nbsp;預設 | **噴霧器** | 淋浴, 噴泉, 噴霧器, 手持式,  |
| ├&nbsp;**流體** | | 
| │&nbsp;├&nbsp;凝聚力 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;粘度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;緊貼表面 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;目標密度 | [2] (1 ~ 10) | 
| │&nbsp;├&nbsp;凝聚範圍 | [20] (1 ~ 50) | 凝聚效果的最大距離
| │&nbsp;├&nbsp;目標距離 | [10] (1 ~ 20) | 當凝聚關閉時，粒子之間的最小距離（以毫米計算）。
| │&nbsp;├&nbsp;高度 | [0.25] (0 ~ 0.5) | 根據粒子的大小提升粒子
| │&nbsp;└&nbsp;(Presets: Water) || 
| │&nbsp;&nbsp;&nbsp;預設 | **水** | 水, 粘性, 沙子,  |
| ├&nbsp;**渲染** | | 
| │&nbsp;├&nbsp;渲染粒子 | ON | 
| │&nbsp;├&nbsp;渲染水滴 | OFF | 
| │&nbsp;├&nbsp;水滴大小 | [2] (0 ~ 50) | 水滴大小（以毫米計算）
| │&nbsp;├&nbsp;按密度縮放 | [0] (0 ~ 5) | 根據流體的密度縮放水滴大小
| │&nbsp;├&nbsp;**顏色** | | 
| │&nbsp;│&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;│&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;光滑度 | [0.95] (0 ~ 1) | 
| │&nbsp;├&nbsp;發光 | [0] (0 ~ 1) | 
| │&nbsp;└&nbsp;透明度 | [0.1] (0 ~ 1) | 
| ├&nbsp;**粒子屬性** | | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空氣阻力 | [-2] (0 ~ 2) | 空氣阻抗
| │&nbsp;├&nbsp;水下阻力 | [-2] (0 ~ 2) | 水下阻抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風的影響 | [0] (0 ~ 1) | 
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
| │&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置),  |
| **幾何碰撞器** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;可見 | OFF | 
| ├&nbsp;匯出形狀 || 
| ├&nbsp;**頭部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.04] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.5] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**脖子** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.065] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**胸部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.023] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.04] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [0.88] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.7] (0 ~ 1) | 
| ├&nbsp;**肋骨** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.075] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**腰部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.032] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [-0.3] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.8] (0 ~ 1) | 
| ├&nbsp;**腹部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.013] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.073] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.65] (0 ~ 1) | 
| ├&nbsp;**臀部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.0425] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.105] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.012] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.09] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**肩膀** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [-0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.4] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**上臂** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.15] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.035] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**前臂** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.0445] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.44] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.01] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**手** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.0315] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [-0.0316] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**髖部** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.027] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.1] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.1] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.085] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**大腿** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.073] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.05599999] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**小腿** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.05926838] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;中間位置 || 
| │&nbsp;├&nbsp;(X) | [0.009999919] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05999992] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01666657] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;中間半徑 | [0.06707321] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;中間曲線 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.03231711] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**腳** | | 
| │&nbsp;├&nbsp;啟用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.03166673] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半徑 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲線 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;結束位置 || 
| │&nbsp;├&nbsp;(X) | [0.028] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;結束半徑 | [0.0625] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;縮放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;預設 | **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| **網格碰撞體** | | 
| ├&nbsp;啟用 | ON | 
| ├&nbsp;禁用幾何碰撞體 | ON | 
| ├&nbsp;可視化 | OFF | 
| ├&nbsp;深度 | [0.025] (0 ~ 0.1) | 
| ├&nbsp;(Skip Edge) | ON | 
| ├&nbsp;(Skip Point) | ON | 
| └&nbsp;(Single Collision) | ON | 
| **模擬設置** | | 
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
| (Presets: Default (Reset)) || 
| 預設 | **預設 (重置)** | 預設 (重置),  |
