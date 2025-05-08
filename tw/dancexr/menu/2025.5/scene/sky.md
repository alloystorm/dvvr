---
locale: zh-rTW
layout: single
title: 天空
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.5/scene/sky) | [繁中](/tw/dancexr/menu/2025.5/scene/sky) | [日本語](/jp/dancexr/menu/2025.5/scene/sky) | [한국어](/kr/dancexr/menu/2025.5/scene/sky) | [简中](/zh/dancexr/menu/2025.5/scene/sky)

[環境](../menu#環境) > 天空

SkySetting 管理天空渲染，包括天空貼圖、程序化天空、環境光和風效應。

## 配置

| 設定 | 值 | 描述 |
| :--- | --- | :--- |
| ☑ 模式 | 顏色 | 顏色, 天空貼圖, 程序化, <br/>選擇天空渲染模式：顏色、天空貼圖或程序化。
| ⊖ 背景 | [1] (0 ~ 1) | 控制天空渲染時的亮度。
| ⊖ 天空環境光 | [1] (0 ~ 1) | 控制天空對環境光的影響程度。
| ⊖ 星星 | [1] (0 ~ 8) | 設定使用程序化天空時夜晚星星的強度。
| > 天空貼圖 | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]), (adams_place_bridge_4k), (aft_lounge_4k), (birbeck_street_underpass_4k), (blue_lagoon_night_8k), (canary_wharf_4k), (canary_wharf_8k), (cobblestone_street_night_4k), (hansaplatz_8k), (leadenhall_market_4k), (metro_noord_4k), (modern_buildings_2_4k), (modern_buildings_8k), (neuer_zollhof_4k), (old_bus_depot_4k), (old_hall_4k), (palermo_square_4k), (piazza_martin_lutero_4k), (portland_landing_pad_8k), (pretville_street_4k), (quattro_canti_4k), (rathaus_4k), (rostock_laage_airport_4k), (royal_esplanade_4k), (san_giuseppe_bridge_4k), (schadowplatz_8k), (school_hall_4k), (shanghai_bund_4k), (shanghai_riverside_4k), (skylit_garage_4k), (snowy_field_4k (1)), (st_peters_square_night_4k), (subway_entrance_4k), (sunset_jhbcentral_4k), (ulmer_muenster_4k), (urban_street_01_4k), (urban_street_04_4k), (venetian_crossroads_4k), (vignaioli_night_8k), (xiequ_yuan_4k),  |
| ⊖ 方向 | [0] (0 ~ 360) | 設定天空旋轉角度（度）。
| ⊖ 風 | [1] (0 ~ 4) | 影響布料模擬、粒子動態和雲朵的全局風速。
| ⊖ 風向 | [0] (0 ~ 360) | 設定全局風向角度（度）。
| ☐ 風場 | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **位置** | | Sets the position of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **旋轉** | | Sets the rotation of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| ⊖ 距離 | [5] (0 ~ 10) | 設定風場距離。
| ⊖ 半徑 | [1] (0 ~ 2) | 設定風場半徑。
| ⊖ 速度 | [1] (0 ~ 4) | 設定風場速度。
|  **天空環境光** || 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **天空顏色** | | 
| ├─☑ 色彩模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 飽和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 紅色 | [1] (0 ~ 1) | 
| ├─⊖ 綠色 | [1] (0 ~ 1) | 
| ├─⊖ 藍色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台顏色 | [OFF] | 使用舞台燈環的顏色
| ├─☑ 色溫 | [6500] (3000 ~ 8000) | 
| └─≡ 預設值 | **白色** | 白色, 夕陽, 紅色, 黃色, 藍色, 綠色,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **中間色** | | 
| ├─☑ 色彩模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 飽和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 紅色 | [1] (0 ~ 1) | 
| ├─⊖ 綠色 | [1] (0 ~ 1) | 
| ├─⊖ 藍色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台顏色 | [OFF] | 使用舞台燈環的顏色
| ├─☑ 色溫 | [6500] (3000 ~ 8000) | 
| └─≡ 預設值 | **白色** | 白色, 夕陽, 紅色, 黃色, 藍色, 綠色,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **地面顏色** | | 
| ├─☑ 色彩模式 | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 飽和度 | [0] (0 ~ 1) | 
| ├─⊖ 亮度 | [1] (0 ~ 1) | 
| ├─⊖ 紅色 | [1] (0 ~ 1) | 
| ├─⊖ 綠色 | [1] (0 ~ 1) | 
| ├─⊖ 藍色 | [1] (0 ~ 1) | 
| ├─☐ 使用舞台顏色 | [OFF] | 使用舞台燈環的顏色
| ├─☑ 色溫 | [6500] (3000 ~ 8000) | 
| └─≡ 預設值 | **白色** | 白色, 夕陽, 紅色, 黃色, 藍色, 綠色,  |
| ☐ **雲朵** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─☐ 啟用 | [OFF] | 啟用或關閉體積雲。
| ├─⊖ 形狀比例 | [1] (-1 ~ 2) | 控制雲形的比例。
| ├─⊖ 形狀因子 | [0.8] (0 ~ 1) | 調整雲的形狀因子。
| ├─⊖ 侵蝕比例 | [2] (0 ~ 5) | 控制雲侵蝕的比例。
| ├─⊖ 侵蝕因子 | [0.8] (0 ~ 1) | 調整雲侵蝕因子。
| ├─⊖ 密度 | [0.2] (0 ~ 1) | 設定雲的密度倍數。
| ├─☐ 陰影 | [OFF] | 啟用或關閉雲層陰影。
| └─⊖ 風力倍數 | [3] (0 ~ 4) | 設定雲朵移動的風力倍數。
| ≡ 預設值 | **室內（天空模式）** | 天空貼圖, 程序化, 室內（天空模式）, 薄雲, 多雲,  |
