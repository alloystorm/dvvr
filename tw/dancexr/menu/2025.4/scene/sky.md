---
locale: zh-rTW
layout: single
title: 天空
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/scene/sky) | [繁中](/tw/dancexr/menu/2025.4/scene/sky) | [日本語](/jp/dancexr/menu/2025.4/scene/sky) | [한국어](/kr/dancexr/menu/2025.4/scene/sky) | [简中](/zh/dancexr/menu/2025.4/scene/sky)

[環境](../menu#環境) > 天空



| Setting | Value | Description |
| :--- | --- | :--- |
| 模式 | 程序化 | 顏色, 天空地圖, 程序化, <br/>(Selects the sky rendering mode: Color, Sky Map, or Procedural.)0/17/True
| 背景 | [1] (0 ~ 1) | (Controls the brightness of the sky when it is rendered.)1/17/True
| 天空環境光 | [1] (0 ~ 1) | 控制天空對環境光照明的影響程度。2/17/True
| (Sky Map: [Cloud]) || 3/17/True
| 天空地圖 | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]),  |
| 朝向 | [0] (0 ~ 360) | (Sets the rotation of the sky in degrees.)4/17/True
| 風 | [1] (0 ~ 4) | (Global wind speed affecting cloth simulation, particle dynamics, and clouds.)5/17/True
| 風向 | [0] (0 ~ 360) | (Sets the global wind direction in degrees.)6/17/True
| 風場 | OFF | 7/17/True
| **位置** | | Sets the position of the wind field.8/17/True
| ├ (X) | [0] ((Unlimited)) | 0/2/False
| ├ (Y) | [0] ((Unlimited)) | 1/2/False
| └ (Z) | [0] ((Unlimited)) | 2/2/False
| **旋轉** | | Sets the rotation of the wind field.9/17/True
| ├ (X) | [0] ((Unlimited)) | 0/2/False
| ├ (Y) | [0] ((Unlimited)) | 1/2/False
| └ (Z) | [0] ((Unlimited)) | 2/2/False
| 距離 | [5] (0 ~ 10) | (Sets the distance of the wind field.)10/17/True
| 半徑 | [1] (0 ~ 2) | (Sets the radius of the wind field.)11/17/True
| 速度 | [1] (0 ~ 4) | (Sets the speed of the wind field.)12/17/True
| 天空環境光 || 13/17/True
| **天空顏色** | | 14/17/True
| ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
| ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| ├ 紅色 | [1] (0 ~ 1) | 4/8/True
| ├ 綠色 | [1] (0 ~ 1) | 5/8/True
| ├ 藍色 | [1] (0 ~ 1) | 6/8/True
| ├ 使用舞台顏色 | OFF | 使用舞台環的顏色7/8/True
| ├ 色溫 | [6500] (3000 ~ 8000) | 8/8/True
| └ 預設 | **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| **中間顏色** | | 15/17/True
| ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
| ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| ├ 紅色 | [1] (0 ~ 1) | 4/8/True
| ├ 綠色 | [1] (0 ~ 1) | 5/8/True
| ├ 藍色 | [1] (0 ~ 1) | 6/8/True
| ├ 使用舞台顏色 | OFF | 使用舞台環的顏色7/8/True
| ├ 色溫 | [6500] (3000 ~ 8000) | 8/8/True
| └ 預設 | **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| **地面顏色** | | 16/17/True
| ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
| ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| ├ 紅色 | [1] (0 ~ 1) | 4/8/True
| ├ 綠色 | [1] (0 ~ 1) | 5/8/True
| ├ 藍色 | [1] (0 ~ 1) | 6/8/True
| ├ 使用舞台顏色 | OFF | 使用舞台環的顏色7/8/True
| ├ 色溫 | [6500] (3000 ~ 8000) | 8/8/True
| └ 預設 | **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| **雲** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.17/17/True
| ├ (Enable Cloud) | ON | (Enables or disables volumetric clouds.)0/7/False
| ├ 形狀縮放 | [1] (-1 ~ 2) | (Controls the scale of the cloud shapes.)1/7/False
| ├ 形狀因子 | [0.8] (0 ~ 1) | (Adjusts the shape factor of the clouds.)2/7/False
| ├ 侵蝕縮放 | [2] (0 ~ 5) | (Controls the scale of cloud erosion.)3/7/False
| ├ 侵蝕因子 | [0.8] (0 ~ 1) | (Adjusts the erosion factor of the clouds.)4/7/False
| ├ 密度 | [0.2] (0 ~ 1) | (Sets the density multiplier for the clouds.)5/7/False
| ├ 陰影 | OFF | (Enables or disables cloud shadows.)6/7/False
| └ 風倍增器 | [3] (0 ~ 4) | (Sets the wind multiplier for cloud movement.)7/7/False
| 預設 | **薄雲** | 天空貼圖, 程序化, 室內, 薄雲, 多雲,  |
