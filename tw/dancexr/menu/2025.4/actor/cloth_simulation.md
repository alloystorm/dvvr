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
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr> 重置</nobr>|| 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>布料 1</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 重建網格</nobr>|| 此處的大多數參數需要重建網格才能生效。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 拓撲</nobr>| **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 繩索連接</nobr>| [4] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內半徑</nobr>| [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 斜坡</nobr>| [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 弧形</nobr>| [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 長度</nobr>| [0.25] (0 ~ 0.75) | 長度（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 臂孔</nobr>| [0.5] (0 ~ 1) | 臂孔相對於周長的大小
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 背部長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 側邊長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 垂直解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離遵從性</nobr>| [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV映射</nobr>| **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 上層</nobr>| [2] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>上錨點</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 錨點骨骼</nobr>| **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 下層</nobr>| [0] (0 ~ 10) | 
|<nobr>│ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>下錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 錨點骨骼</nobr>| **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 交換側面</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 黏性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 身體</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腿部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr>│ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用彎曲約束</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 縮放</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 自我碰撞</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用撕裂</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C1 材質</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 玻璃模式</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 光澤作為透明度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 雙面</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 暗邊</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 投擲陰影</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 深度預處理</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 光澤</nobr>| [0.3] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凸起</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 發光</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 環境光</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 剪裁</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 混合模式</nobr>| **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>卡通著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 輪廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 光澤</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔軟光澤</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高光區域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 環境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影區域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔和陰影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>特殊著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模式</nobr>| **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 紋理</nobr>| **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
|<nobr>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>細節圖</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Hexagon Map)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 密度</nobr>| [2] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凸起</nobr>| [0.5] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 噪聲</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> (Use Circle)</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔邊</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 選擇地圖</nobr>| **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖旋轉</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖比例</nobr>| [6] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響環境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響金屬感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響顏色混合</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 各向異性</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP貼圖偏差</nobr>| [0] (-5 ~ 5) | 調整細節材質的清晰度。
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>布料 2</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 重建網格</nobr>|| 此處的大多數參數需要重建網格才能生效。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 拓撲</nobr>| **水平佈局** | 自適應六邊形, 自適應矩形, 水平佈局, 水平繩索, 垂直佈局, 垂直繩索,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 繩索連接</nobr>| [4] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內半徑</nobr>| [0.08] (0 ~ 0.2) | 內圓半徑（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 斜坡</nobr>| [45] (0 ~ 90) | 沿長度擴展網格的角度。0 = 管子，90 = 平圓。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 弧形</nobr>| [0] (-1 ~ 1) | 沿長度向外或向內的弧形。正值 = 氣球形狀，負值 = 鐘形
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 長度</nobr>| [0.25] (0 ~ 0.75) | 長度（以米為單位）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 臂孔</nobr>| [0.5] (0 ~ 1) | 臂孔相對於周長的大小
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 臂孔相對於總長度的高度
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 背部長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 側邊長度</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 垂直解析度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離遵從性</nobr>| [0] (0 ~ 0.1) | 粒子之間的距離約束的遵從性
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV映射</nobr>| **鏡像縮放** | 圓形, 鏡像縮放, 鏡像實際, 包裹縮放, 包裹實際,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 上層</nobr>| [2] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>上錨點</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 錨點骨骼</nobr>| **軀幹** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 下層</nobr>| [0] (0 ~ 10) | 
|<nobr>│ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>下錨點</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 錨點選擇</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 選擇偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 錨點骨骼</nobr>| **腰部** | 腰部, 軀幹, 臀部, 頭部, 大腿, 小腿, 上臂, 下臂, 手, 胸部,  |
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 交換側面</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 鎖定模式</nobr>| **無** | 無, 鎖定, 鎖定高度, 粘性,  |
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>錨點位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>錨點旋轉</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 黏性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 身體</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腿部</nobr>| [ON] | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr>│ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用彎曲約束</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 縮放</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 自我碰撞</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用撕裂</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C2 材質</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **啞光灰** | 原版, 啞光灰, 半透明, 發光, 銀色, 實心玻璃, 薄玻璃, 輪廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 玻璃模式</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 光澤作為透明度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 雙面</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 暗邊</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 投擲陰影</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 深度預處理</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 光澤</nobr>| [0.3] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凸起</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 發光</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 環境光</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 剪裁</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 混合模式</nobr>| **(Multiply)** | 原版, (Multiply), 混合, (Color Shift),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Gray)** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>卡通著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 輪廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 光澤</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔軟光澤</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高光區域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 環境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影區域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔和陰影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>特殊著色器</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模式</nobr>| **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 紋理</nobr>| **[實心顏色]** | [實心顏色], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
|<nobr>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>細節圖</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Hexagon Map)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 密度</nobr>| [2] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凸起</nobr>| [0.5] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 噪聲</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> (Use Circle)</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 柔邊</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 選擇地圖</nobr>| **布料 3** | 碳纖維, 皮革, 布料 1, 布料 2, 布料 3, 羊毛 1, 羊毛 2, 金屬亮面, 金屬拉絲, 頭髮,  |
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖旋轉</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖比例</nobr>| [6] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 細節圖凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響環境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響金屬感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 影響顏色混合</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 各向異性</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP貼圖偏差</nobr>| [0] (-5 ~ 5) | 調整細節材質的清晰度。
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 合併</nobr>| [OFF] | 將布料 1 和 2 合併為單一模擬，這允許兩者之間的碰撞，但會變慢。
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>流體（實驗性）</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>生成</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>位置</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>旋轉</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 生成半徑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 擴散</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 生成速率</nobr>| [20] (0 ~ 20) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 速度</nobr>| [5] (0 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 滑鼠 / 手控制</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 自動瞄準</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大壽命</nobr>| [10] (5 ~ 15) | 粒子在這段時間後消失並重新生成。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面壽命</nobr>| [0.1] (0 ~ 1) | 撞擊地面後的生存時間。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 平滑度</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **噴霧器** | 淋浴, 噴泉, 噴霧器, 手持式,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>流體</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凝聚力</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粘度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 緊貼表面</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標密度</nobr>| [2] (1 ~ 10) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 凝聚範圍</nobr>| [20] (1 ~ 50) | 凝聚效果的最大距離
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標距離</nobr>| [10] (1 ~ 20) | 當凝聚關閉時，粒子之間的最小距離（以毫米計算）。
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度</nobr>| [0.25] (0 ~ 0.5) | 根據粒子的大小提升粒子
|<nobr>│ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **水** | 水, 粘性, 沙子,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>渲染</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 渲染粒子</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 渲染水滴</nobr>| [OFF] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水滴大小</nobr>| [2] (0 ~ 50) | 水滴大小（以毫米計算）
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 按密度縮放</nobr>| [0] (0 ~ 5) | 根據流體的密度縮放水滴大小
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 顏色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 金屬質感</nobr>| [0] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 光滑度</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 發光</nobr>| [0] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子屬性</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [0] (0 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [-2] (0 ~ 2) | 空氣阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [-2] (0 ~ 2) | 水下阻抗
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ │ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 身體</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腿部</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 玩家</nobr>| [OFF] | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置),  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>幾何碰撞器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可見</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 匯出形狀</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>頭部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>脖子</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>胸部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>肋骨</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>腰部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>腹部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>臀部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>肩膀</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>上臂</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>前臂</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>手</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>髖部</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>大腿</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>小腿</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>中間位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間半徑</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>腳</b></nobr>| | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>起始位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 起始半徑</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>結束位置</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 結束半徑</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/> <b>縮放</b></nobr>|| 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ <img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>網格碰撞體</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 禁用幾何碰撞體</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Edge)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Point)</nobr>| [ON] | 
|<nobr>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Single Collision)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>模擬設置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用拖動</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重置比例</nobr>| [1] (1 ~ 5) | 從較大比例過渡到布料，以幫助適應重置。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 模擬</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 反向偶數子步驟</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 兩步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置),  |
