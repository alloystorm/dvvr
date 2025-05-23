---
locale: zh-rCN
layout: single
title: 天空
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/scene/sky) | [繁中](/tw/dancexr/menu/2025.4/scene/sky) | [日本語](/jp/dancexr/menu/2025.4/scene/sky) | [한국어](/kr/dancexr/menu/2025.4/scene/sky) | [简中](/zh/dancexr/menu/2025.4/scene/sky)

[环境](../menu#环境) > 天空



[(Feature Page)](/zh/dancexr/features/sky)

| Setting | Value | Description |
| :--- | --- | :--- |
| ☑ 模式| 程序化 | 颜色, 天空贴图, 程序化, <br/>(Selects the sky rendering mode: Color, Sky Map, or Procedural.)
|  ⊖ 背景| [1] (0 ~ 1) | (Controls the brightness of the sky when it is rendered.)
|  ⊖ 天空环境光| [1] (0 ~ 1) | 控制天空对环境光照的影响程度。
|  > 天空贴图| **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]),  |
|  ⊖ 方向| [0] (0 ~ 360) | (Sets the rotation of the sky in degrees.)
|  ⊖ 风| [1] (0 ~ 4) | (Global wind speed affecting cloth simulation, particle dynamics, and clouds.)
|  ⊖ 风向| [0] (0 ~ 360) | (Sets the global wind direction in degrees.)
|  □ 风场| [OFF] | 
|  ⚙️ **位置**| | Sets the position of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⚙️ **旋转**| | Sets the rotation of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⊖ 距离| [5] (0 ~ 10) | (Sets the distance of the wind field.)
|  ⊖ 半径| [1] (0 ~ 2) | (Sets the radius of the wind field.)
|  ⊖ 速度| [1] (0 ~ 4) | (Sets the speed of the wind field.)
|  **天空环境光**|| 
|  ⚙️ **天空颜色**| | 
| ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 饱和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 红色| [1] (0 ~ 1) | 
| ├─ ⊖ 绿色| [1] (0 ~ 1) | 
| ├─ ⊖ 蓝色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| ├─ ☑ 色温| [6500] (3000 ~ 8000) | 
| └─ ≡ 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
|  ⚙️ **中间颜色**| | 
| ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 饱和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 红色| [1] (0 ~ 1) | 
| ├─ ⊖ 绿色| [1] (0 ~ 1) | 
| ├─ ⊖ 蓝色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| ├─ ☑ 色温| [6500] (3000 ~ 8000) | 
| └─ ≡ 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
|  ⚙️ **地面颜色**| | 
| ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 饱和度| [0] (0 ~ 1) | 
| ├─ ⊖ 亮度| [1] (0 ~ 1) | 
| ├─ ⊖ 红色| [1] (0 ~ 1) | 
| ├─ ⊖ 绿色| [1] (0 ~ 1) | 
| ├─ ⊖ 蓝色| [1] (0 ~ 1) | 
| ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| ├─ ☑ 色温| [6500] (3000 ~ 8000) | 
| └─ ≡ 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
|  ☑ **云**| | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─ ☑ 启用| [ON] | (Enables or disables volumetric clouds.)
| ├─ ⊖ 形状比例| [1] (-1 ~ 2) | (Controls the scale of the cloud shapes.)
| ├─ ⊖ 形状因子| [0.8] (0 ~ 1) | (Adjusts the shape factor of the clouds.)
| ├─ ⊖ 侵蚀比例| [2] (0 ~ 5) | (Controls the scale of cloud erosion.)
| ├─ ⊖ 侵蚀因子| [0.8] (0 ~ 1) | (Adjusts the erosion factor of the clouds.)
| ├─ ⊖ 密度| [0.2] (0 ~ 1) | (Sets the density multiplier for the clouds.)
| ├─ □ 阴影| [OFF] | (Enables or disables cloud shadows.)
| └─ ⊖ 风的倍增器| [3] (0 ~ 4) | (Sets the wind multiplier for cloud movement.)
|  ≡ 预设| **薄云** | 天空贴图, 程序化, 室内, 薄云, 阴云,  |
