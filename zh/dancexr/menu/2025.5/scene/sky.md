---
locale: zh-rCN
layout: single
title: 天空
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.5/scene/sky) | [繁中](/tw/dancexr/menu/2025.5/scene/sky) | [日本語](/jp/dancexr/menu/2025.5/scene/sky) | [한국어](/kr/dancexr/menu/2025.5/scene/sky) | [简中](/zh/dancexr/menu/2025.5/scene/sky)

[环境](../menu#环境) > 天空

SkySetting 管理天空渲染，包括天空贴图、程序化天空、环境光照和风的效果。

## 配置

| 设置 | 值 | 描述 |
| :--- | --- | :--- |
| ☑ 模式 | 颜色 | 颜色, 天空贴图, 程序化, <br/>选择天空渲染模式：颜色、天空贴图或程序化。
| ⊖ 背景 | [1] (0 ~ 1) | 控制天空渲染时的亮度。
| ⊖ 天空环境光 | [1] (0 ~ 1) | 控制天空对环境光照的影响程度。
| ⊖ 星星 | [1] (0 ~ 8) | 设置使用程序化天空时夜间星星的强度。
| > 天空贴图 | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]), (adams_place_bridge_4k), (aft_lounge_4k), (birbeck_street_underpass_4k), (blue_lagoon_night_8k), (canary_wharf_4k), (canary_wharf_8k), (cobblestone_street_night_4k), (hansaplatz_8k), (leadenhall_market_4k), (metro_noord_4k), (modern_buildings_2_4k), (modern_buildings_8k), (neuer_zollhof_4k), (old_bus_depot_4k), (old_hall_4k), (palermo_square_4k), (piazza_martin_lutero_4k), (portland_landing_pad_8k), (pretville_street_4k), (quattro_canti_4k), (rathaus_4k), (rostock_laage_airport_4k), (royal_esplanade_4k), (san_giuseppe_bridge_4k), (schadowplatz_8k), (school_hall_4k), (shanghai_bund_4k), (shanghai_riverside_4k), (skylit_garage_4k), (snowy_field_4k (1)), (st_peters_square_night_4k), (subway_entrance_4k), (sunset_jhbcentral_4k), (ulmer_muenster_4k), (urban_street_01_4k), (urban_street_04_4k), (venetian_crossroads_4k), (vignaioli_night_8k), (xiequ_yuan_4k),  |
| ⊖ 方向 | [0] (0 ~ 360) | 设置天空的旋转角度（度）。
| ⊖ 风 | [1] (0 ~ 4) | 影响布料模拟、粒子动力学和云朵的全局风速。
| ⊖ 风向 | [0] (0 ~ 360) | 设置全局风向（度）。
| ☐ 风场 | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **位置** | | Sets the position of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **旋转** | | Sets the rotation of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| ⊖ 距离 | [5] (0 ~ 10) | 设置风场的距离。
| ⊖ 半径 | [1] (0 ~ 2) | 设置风场的半径。
| ⊖ 速度 | [1] (0 ~ 4) | 设置风场的速度。
|  **天空环境光** || 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **天空颜色** | | 
| ├─☑ 颜色模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 饱和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 红色 | [1] (0 ~ 1) | 
| ├─⊖ 绿色 | [1] (0 ~ 1) | 
| ├─⊖ 蓝色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台颜色 | [OFF] | 使用舞台灯环的颜色
| ├─☑ 色温 | [6500] (3000 ~ 8000) | 
| └─≡ 预设 | **白色** | 白色, 日落, 红色, 黄色, 蓝色, 绿色,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **中间色** | | 
| ├─☑ 颜色模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 饱和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 红色 | [1] (0 ~ 1) | 
| ├─⊖ 绿色 | [1] (0 ~ 1) | 
| ├─⊖ 蓝色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台颜色 | [OFF] | 使用舞台灯环的颜色
| ├─☑ 色温 | [6500] (3000 ~ 8000) | 
| └─≡ 预设 | **白色** | 白色, 日落, 红色, 黄色, 蓝色, 绿色,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **地面颜色** | | 
| ├─☑ 颜色模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 饱和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 红色 | [1] (0 ~ 1) | 
| ├─⊖ 绿色 | [1] (0 ~ 1) | 
| ├─⊖ 蓝色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台颜色 | [OFF] | 使用舞台灯环的颜色
| ├─☑ 色温 | [6500] (3000 ~ 8000) | 
| └─≡ 预设 | **白色** | 白色, 日落, 红色, 黄色, 蓝色, 绿色,  |
| ☐ **云朵** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─☐ 启用 | [OFF] | 开启或关闭体积云。
| ├─⊖ 形状缩放 | [1] (-1 ~ 2) | 控制云朵形状的缩放。
| ├─⊖ 形状因子 | [0.8] (0 ~ 1) | 调整云朵的形状因子。
| ├─⊖ 侵蚀缩放 | [2] (0 ~ 5) | 控制云朵侵蚀的缩放。
| ├─⊖ 侵蚀因子 | [0.8] (0 ~ 1) | 调整云朵的侵蚀因子。
| ├─⊖ 密度 | [0.2] (0 ~ 1) | 设置云朵的密度倍数。
| ├─☐ 阴影 | [OFF] | 开启或关闭云影。
| └─⊖ 风力倍数 | [3] (0 ~ 4) | 设置云朵移动的风力倍数。
| ≡ 预设 | **室内** | 天空贴图, 程序化, 室内, 薄云, 多云,  |
