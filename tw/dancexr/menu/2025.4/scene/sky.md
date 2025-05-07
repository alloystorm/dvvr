---
locale: zh-rTW
layout: single
title: 天空
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/scene/sky) | [繁中](/tw/dancexr/menu/2025.4/scene/sky) | [日本語](/jp/dancexr/menu/2025.4/scene/sky) | [한국어](/kr/dancexr/menu/2025.4/scene/sky) | [简中](/zh/dancexr/menu/2025.4/scene/sky)

[環境](../menu#環境) > 天空



[(Feature Page)](/tw/dancexr/features/sky)

| Setting | Value | Description |
| :--- | --- | :--- |
| ☑ 模式| 程序化 | 顏色, 天空地圖, 程序化, <br/>(Selects the sky rendering mode: Color, Sky Map, or Procedural.)
|  ⊖ 背景| [1] (0 ~ 1) | (Controls the brightness of the sky when it is rendered.)
|  ⊖ 天空環境光| [1] (0 ~ 1) | 控制天空對環境光照明的影響程度。
|  > 天空地圖| **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]),  |
|  ⊖ 朝向| [0] (0 ~ 360) | (Sets the rotation of the sky in degrees.)
|  ⊖ 風| [1] (0 ~ 4) | (Global wind speed affecting cloth simulation, particle dynamics, and clouds.)
|  ⊖ 風向| [0] (0 ~ 360) | (Sets the global wind direction in degrees.)
|  □ 風場| [OFF] | 
|  ⚙️ <b>位置</b>| | Sets the position of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⚙️ <b>旋轉</b>| | Sets the rotation of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⊖ 距離| [5] (0 ~ 10) | (Sets the distance of the wind field.)
|  ⊖ 半徑| [1] (0 ~ 2) | (Sets the radius of the wind field.)
|  ⊖ 速度| [1] (0 ~ 4) | (Sets the speed of the wind field.)
|  <b>天空環境光</b>|| 
|  ⚙️ <b>天空顏色</b>| | 
| ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 飽和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 紅色| [1] (0 ~ 1) | 
| ├─ ⊖ 綠色| [1] (0 ~ 1) | 
| ├─ ⊖ 藍色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| ├─ ☑ 色溫| [6500] (3000 ~ 8000) | 
| └─ ≡ 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
|  ⚙️ <b>中間顏色</b>| | 
| ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 飽和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 紅色| [1] (0 ~ 1) | 
| ├─ ⊖ 綠色| [1] (0 ~ 1) | 
| ├─ ⊖ 藍色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| ├─ ☑ 色溫| [6500] (3000 ~ 8000) | 
| └─ ≡ 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
|  ⚙️ <b>地面顏色</b>| | 
| ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 飽和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 紅色| [1] (0 ~ 1) | 
| ├─ ⊖ 綠色| [1] (0 ~ 1) | 
| ├─ ⊖ 藍色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| ├─ ☑ 色溫| [6500] (3000 ~ 8000) | 
| └─ ≡ 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
|  ☑ <b>雲</b>| | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─ ☑ 啟用| [ON] | (Enables or disables volumetric clouds.)
| ├─ ⊖ 形狀縮放| [1] (-1 ~ 2) | (Controls the scale of the cloud shapes.)
| ├─ ⊖ 形狀因子| [0.8] (0 ~ 1) | (Adjusts the shape factor of the clouds.)
| ├─ ⊖ 侵蝕縮放| [2] (0 ~ 5) | (Controls the scale of cloud erosion.)
| ├─ ⊖ 侵蝕因子| [0.8] (0 ~ 1) | (Adjusts the erosion factor of the clouds.)
| ├─ ⊖ 密度| [0.2] (0 ~ 1) | (Sets the density multiplier for the clouds.)
| ├─ □ 陰影| [OFF] | (Enables or disables cloud shadows.)
| └─ ⊖ 風倍增器| [3] (0 ~ 4) | (Sets the wind multiplier for cloud movement.)
|  ≡ 預設| **薄雲** | 天空貼圖, 程序化, 室內, 薄雲, 多雲,  |
