---
locale: zh-rTW
layout: single
title: 地面
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/ground.md) | [繁中](/tw/dancexr/menu/2025.4/scene/ground.md) | [日本語](/jp/dancexr/menu/2025.4/scene/ground.md) | [한국어](/kr/dancexr/menu/2025.4/scene/ground.md) | [简中](/zh/dancexr/menu/2025.4/scene/ground.md)
# 地面
## 
| Setting | Value | Description |
| :--- | --- | :--- |
|**地面** | | 
|- 地面高度| [0] (-2 ~ 2) | 
| 地面 | OFF | 
|- 半徑| [200] (2 ~ 100) | 地面網格的大小。
| 如果舞台存在則隱藏 | ON | 當有舞台模型時隱藏地面。
|**表面** | | 
| 紋理 |  [Sky Map],  [Wood1],  [Wood2],  **[Tiles]**,  [Concrete],  [Video],  |  |
|**平鋪** | | 
|- 平鋪 X| [1] (0.1 ~ 10) | 
|- 平鋪 Y| [1] (0.1 ~ 10) | 
|- 包裹模式|  **Repeat**,  | 
|- 偏移X| [0] (0 ~ 1) | 
|- 偏移 Y| [0] (0 ~ 1) | 
|- 旋轉| [0] (0 ~ 360) | 
|- 變化| [0.5] (0 ~ 1) | 
| 適應紋理 | OFF | 
| 重置 || 
| (Confirm Reset) || 
|
|- 光澤| [0.95] (0 ~ 1) | 
|- 金屬質感| [0] (0 ~ 1) | 
|- 凸起| [0.2] (0 ~ 1) | 
|- 發光| [0] (0 ~ 10) | 
|- 環境光| [1] (0 ~ 1) | 
|- 透明度| [1] (0 ~ 1) | 
|- 剪裁| [0] (0 ~ 1) | 
|**顏色** | | 
|- 顏色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 飽和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 紅色| [1] (0 ~ 1) | 
|- 綠色| [1] (0 ~ 1) | 
|- 藍色| [1] (0 ~ 1) | 
| 混合模式 |  Original,  Multiply,  **Blend**,  Color Shift,  |  |
|- 混合| [1] (0 ~ 1) | 
| 預設 |  Original,  White,  **Black**,  Red,  Yellow,  Dark Gray,  Blue,  Skin,  Gray,  Orange,  |  |
|
|**卡通著色器** | | 
| (Enable Toon Shader) | OFF | 
|- 陰影| [1] (0 ~ 1) | 
|- 輪廓| [0.5] (0 ~ 1) | 
|- 光澤| [0.25] (0 ~ 1) | 
|- 柔軟光澤| [0.1] (0 ~ 1) | 
|- 高光區域| [0.25] (0 ~ 1) | 
|- 柔和高光| [0.1] (0 ~ 1) | 
|- 環境光| [0.75] (0 ~ 1) | 
|- 陰影區域| [0.65] (0 ~ 1) | 
|- 陰影| [0.75] (0 ~ 1) | 
|- 柔和陰影| [0.1] (0 ~ 1) | 
| 預設 |  **Sharp**,  Soft,  Bright,  Flat + Specular,  Flat,  |  |
|
|**特殊著色器** | | 
| 模式 |  **Off**,  Refraction Thick,  Refraction Thin,  Outline,  Unlit,  Experiment,  |  |
|- 折射| [0.5] (1 ~ 3) | 
|- 厚度| [1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|- 觀眾高度| [1.5] (0.5 ~ 3) | 投影紋理到地面時使用的觀眾高度
|**LED 模式** | | 
| (Enable LED Mode) | OFF | 
|- 密度| [7] (4 ~ 10) | 
|- 大小| [0.8] (0 ~ 1) | 
|- 柔邊| [0.3] (0 ~ 1) | 
|- 視角| [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
|- 邊緣| [0.5] (0 ~ 1) | 
|- 減少摩爾紋| [0.1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
| 預設 |  Sky Map,  Wood,  Concrete,  Blue Tiles,  Projector Screen,  Emissive Screen,  LED Screen,  **Black Gloss**,  Glow,  Glass,  |  |
|
|**僅影子** | | 
| 陰影顏色 || 
| 預設 |  White,  **Black**,  Red,  Yellow,  Dark Gray,  Blue,  Skin,  Gray,  Orange,  Preset 1,  |  |
|- 顏色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 飽和度| [0] (0 ~ 1) | 
|- 亮度| [0] (0 ~ 1) | 
|- 紅色| [0] (0 ~ 1) | 
|- 綠色| [0] (0 ~ 1) | 
|- 藍色| [0] (0 ~ 1) | 
|- 透明度| [0.5] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
| 舞台/泳池 | OFF | 
| 預設 |  **Off**,  Runway,  Pool,  Room,  Background Board,  Projector Screen,  LED Screen,  |  |
|- 抬高| [0.5] (-2 ~ 2) | 抬高或降低舞台。
|- (Front / Back Offset)| [0] (-10 ~ 10) | 
|**形狀** | | 
|- 中央寬度| [8] (0 ~ 10) | 中央區域的寬度。
|- 中央深度| [5] (0 ~ 9) | 中央區域的深度。
|- 後面高度| [0] (0 ~ 9) | 背景板的高度。
|- 側面延伸| [0] (0 ~ 5) | 左右的延伸。
|- 前面延伸| [0] (0 ~ 10) | 前方的延伸。
|- 後面延伸| [0] (0 ~ 10) | 後方的延伸。
|- 牆高| [0.05] (0 ~ 5) | 地面上方邊緣的高度。
|- 牆厚| [0.1] (0 ~ 1) | 邊緣的大小。
|- 窗戶| [0] (0 ~ 1) | 
| 浮動 | OFF | 
| 重置 || 
| (Confirm Reset) || 
|
|**表面** | | 
| 紋理 |  [Blank],  **[Wood1]**,  [Wood2],  [Tiles],  [Concrete],  [Video],  |  |
|**平鋪** | | 
|- 平鋪 X| [1] (0.1 ~ 10) | 
|- 平鋪 Y| [1] (0.1 ~ 10) | 
|- 包裹模式|  **Repeat**,  | 
|- 偏移X| [0] (0 ~ 1) | 
|- 偏移 Y| [0] (0 ~ 1) | 
|- 旋轉| [0] (0 ~ 360) | 
|- 變化| [0.5] (0 ~ 1) | 
| 適應紋理 | OFF | 
| 重置 || 
| (Confirm Reset) || 
|
|- 光澤| [0.95] (0 ~ 1) | 
|- 金屬質感| [0] (0 ~ 1) | 
|- 凸起| [0.2] (0 ~ 1) | 
|- 發光| [0] (0 ~ 10) | 
|- 環境光| [1] (0 ~ 1) | 
|- 透明度| [1] (0 ~ 1) | 
|- 剪裁| [0] (0 ~ 1) | 
|**顏色** | | 
|- 顏色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 飽和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 紅色| [1] (0 ~ 1) | 
|- 綠色| [1] (0 ~ 1) | 
|- 藍色| [1] (0 ~ 1) | 
| 混合模式 |  Original,  Multiply,  **Blend**,  Color Shift,  |  |
|- 混合| [1] (0 ~ 1) | 
| 預設 |  Original,  **White**,  Black,  Red,  Yellow,  Dark Gray,  Blue,  Skin,  Gray,  Orange,  |  |
|
|**卡通著色器** | | 
| (Enable Toon Shader) | OFF | 
|- 陰影| [1] (0 ~ 1) | 
|- 輪廓| [0.5] (0 ~ 1) | 
|- 光澤| [0.25] (0 ~ 1) | 
|- 柔軟光澤| [0.1] (0 ~ 1) | 
|- 高光區域| [0.25] (0 ~ 1) | 
|- 柔和高光| [0.1] (0 ~ 1) | 
|- 環境光| [0.75] (0 ~ 1) | 
|- 陰影區域| [0.65] (0 ~ 1) | 
|- 陰影| [0.75] (0 ~ 1) | 
|- 柔和陰影| [0.1] (0 ~ 1) | 
| 預設 |  **Sharp**,  Soft,  Bright,  Flat + Specular,  Flat,  |  |
|
|**特殊著色器** | | 
| 模式 |  **Off**,  Refraction Thick,  Refraction Thin,  Outline,  Unlit,  Experiment,  |  |
|- 折射| [0.5] (1 ~ 3) | 
|- 厚度| [1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**LED 模式** | | 
| (Enable LED Mode) | OFF | 
|- 密度| [7] (4 ~ 10) | 
|- 大小| [0.8] (0 ~ 1) | 
|- 柔邊| [0.3] (0 ~ 1) | 
|- 視角| [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
|- 邊緣| [0.5] (0 ~ 1) | 
|- 減少摩爾紋| [0.1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
| 預設 |  Blank,  **Wood**,  Concrete,  Blue Tiles,  Projector Screen,  Emissive Screen,  LED Screen,  Black Gloss,  Glow,  Glass,  |  |
|
|**後面表面** | | 
| 紋理 |  **[Blank]**,  [Wood1],  [Wood2],  [Tiles],  [Concrete],  [Video],  |  |
|**平鋪** | | 
|- 平鋪 X| [1] (0.1 ~ 10) | 
|- 平鋪 Y| [1] (0.1 ~ 10) | 
|- 包裹模式|  **Repeat**,  | 
|- 偏移X| [0] (0 ~ 1) | 
|- 偏移 Y| [0] (0 ~ 1) | 
|- 旋轉| [0] (0 ~ 360) | 
|- 變化| [0.5] (0 ~ 1) | 
| 適應紋理 | ON | 
| 重置 || 
| (Confirm Reset) || 
|
|- 光澤| [0.95] (0 ~ 1) | 
|- 金屬質感| [0] (0 ~ 1) | 
|- 凸起| [0.2] (0 ~ 1) | 
|- 發光| [0] (0 ~ 10) | 
|- 環境光| [1] (0 ~ 1) | 
|- 透明度| [1] (0 ~ 1) | 
|- 剪裁| [0] (0 ~ 1) | 
|**顏色** | | 
|- 顏色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 飽和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 紅色| [1] (0 ~ 1) | 
|- 綠色| [1] (0 ~ 1) | 
|- 藍色| [1] (0 ~ 1) | 
| 混合模式 |  **Original**,  Multiply,  Blend,  Color Shift,  |  |
|- 混合| [1] (0 ~ 1) | 
| 預設 |  Original,  **White**,  Black,  Red,  Yellow,  Dark Gray,  Blue,  Skin,  Gray,  Orange,  |  |
|
|**卡通著色器** | | 
| (Enable Toon Shader) | OFF | 
|- 陰影| [1] (0 ~ 1) | 
|- 輪廓| [0.5] (0 ~ 1) | 
|- 光澤| [0.25] (0 ~ 1) | 
|- 柔軟光澤| [0.1] (0 ~ 1) | 
|- 高光區域| [0.25] (0 ~ 1) | 
|- 柔和高光| [0.1] (0 ~ 1) | 
|- 環境光| [0.75] (0 ~ 1) | 
|- 陰影區域| [0.65] (0 ~ 1) | 
|- 陰影| [0.75] (0 ~ 1) | 
|- 柔和陰影| [0.1] (0 ~ 1) | 
| 預設 |  **Sharp**,  Soft,  Bright,  Flat + Specular,  Flat,  |  |
|
|**特殊著色器** | | 
| 模式 |  **Off**,  Refraction Thick,  Refraction Thin,  Outline,  Unlit,  Experiment,  |  |
|- 折射| [0.5] (1 ~ 3) | 
|- 厚度| [1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**LED 模式** | | 
| (Enable LED Mode) | OFF | 
|- 密度| [7] (4 ~ 10) | 
|- 大小| [0.8] (0 ~ 1) | 
|- 柔邊| [0.3] (0 ~ 1) | 
|- 視角| [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
|- 邊緣| [0.5] (0 ~ 1) | 
|- 減少摩爾紋| [0.1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
| 預設 |  **Blank**,  Wood,  Concrete,  Blue Tiles,  Projector Screen,  Emissive Screen,  LED Screen,  Black Gloss,  Glow,  Glass,  |  |
|
| 水系統 | OFF | 
| 預設 |  **Off**,  Pool,  Still Water,  Ocean,  |  |
|- 類型|  **Pool**,  | 
|- 高度| [-0.1] (-2 ~ 2) | 水位高度
|- 漣漪| [3] (0 ~ 10) | 小浪的強度
|- 大浪| [30] (0 ~ 100) | 大浪的強度
|- 折射最大距離| [0.35] (0 ~ 3.5) | 控制用於限制水下折射深度的最大距離（以米為單位），更高的值會增加失真量。
|- 吸收距離| [5] (1 ~ 10) | 從上方可以在水中看到的最大距離。
|- 光影效果| [0.5] (0 ~ 1) | 光影效果
|- 吸收乘數| [2] (0 ~ 5) | 在從下方觀看時應用於吸收距離的乘數。
| 預設 |  Sky Map,  **Black Gloss**,  Stage,  Pool,  Ocean,  Background Board,  Projector Screen,  Emissive Screen,  Preset 1,  |  |
|
