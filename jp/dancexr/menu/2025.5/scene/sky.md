---
locale: ja-rJP
layout: single
title: 空
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.5/scene/sky) | [繁中](/tw/dancexr/menu/2025.5/scene/sky) | [日本語](/jp/dancexr/menu/2025.5/scene/sky) | [한국어](/kr/dancexr/menu/2025.5/scene/sky) | [简中](/zh/dancexr/menu/2025.5/scene/sky)

[環境](../menu#環境) > 空

SkySettingはスカイマップ、プロシージャルスカイ、環境光、風の効果を含む空のレンダリングを管理します。

## 設定

| 設定 | 値 | 説明 |
| :--- | --- | :--- |
| ☑ モード | カラー | カラー, スカイマップ, プロシージャル, <br/>空のレンダリングモードを選択します：色、スカイマップ、またはプロシージャル。
| ⊖ 背景 | [1] (0 ~ 1) | 空の明るさを制御します。
| ⊖ スカイアンビエント | [1] (0 ~ 1) | 空が環境光に与える影響を制御します。
| ⊖ 星 | [1] (0 ~ 8) | プロシージャルスカイ使用時の夜空の星の強さを設定します。
| > スカイマップ | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]), (adams_place_bridge_4k), (aft_lounge_4k), (birbeck_street_underpass_4k), (blue_lagoon_night_8k), (canary_wharf_4k), (canary_wharf_8k), (cobblestone_street_night_4k), (hansaplatz_8k), (leadenhall_market_4k), (metro_noord_4k), (modern_buildings_2_4k), (modern_buildings_8k), (neuer_zollhof_4k), (old_bus_depot_4k), (old_hall_4k), (palermo_square_4k), (piazza_martin_lutero_4k), (portland_landing_pad_8k), (pretville_street_4k), (quattro_canti_4k), (rathaus_4k), (rostock_laage_airport_4k), (royal_esplanade_4k), (san_giuseppe_bridge_4k), (schadowplatz_8k), (school_hall_4k), (shanghai_bund_4k), (shanghai_riverside_4k), (skylit_garage_4k), (snowy_field_4k (1)), (st_peters_square_night_4k), (subway_entrance_4k), (sunset_jhbcentral_4k), (ulmer_muenster_4k), (urban_street_01_4k), (urban_street_04_4k), (venetian_crossroads_4k), (vignaioli_night_8k), (xiequ_yuan_4k),  |
| ⊖ 向き | [0] (0 ~ 360) | 空の回転角度を度単位で設定します。
| ⊖ 風 | [1] (0 ~ 4) | 布のシミュレーション、粒子の動態、雲に影響する全体の風速。
| ⊖ 風向き | [0] (0 ~ 360) | 風の全体的な方向を度単位で設定します。
| ☐ 風フィールド | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **位置** | | Sets the position of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **回転** | | Sets the rotation of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| ⊖ 距離 | [5] (0 ~ 10) | 風フィールドの距離を設定します。
| ⊖ 半径 | [1] (0 ~ 2) | 風フィールドの半径を設定します。
| ⊖ 速度 | [1] (0 ~ 4) | 風フィールドの速度を設定します。
|  **スカイアンビエント** || 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **空の色** | | 
| ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 彩度 | [0] (0 ~ 1) | 
| ├─⊖ 明度 | [1] (0 ~ 1) | 
| ├─⊖ レッド | [1] (0 ~ 1) | 
| ├─⊖ グリーン | [1] (0 ~ 1) | 
| ├─⊖ ブルー | [1] (0 ~ 1) | 
| ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **ミドルカラー** | | 
| ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 彩度 | [0] (0 ~ 1) | 
| ├─⊖ 明度 | [1] (0 ~ 1) | 
| ├─⊖ レッド | [1] (0 ~ 1) | 
| ├─⊖ グリーン | [1] (0 ~ 1) | 
| ├─⊖ ブルー | [1] (0 ~ 1) | 
| ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **地面の色** | | 
| ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| ├─⊖ 色相 | [0] (0 ~ 1) | 
| ├─⊖ 彩度 | [0] (0 ~ 1) | 
| ├─⊖ 明度 | [1] (0 ~ 1) | 
| ├─⊖ レッド | [1] (0 ~ 1) | 
| ├─⊖ グリーン | [1] (0 ~ 1) | 
| ├─⊖ ブルー | [1] (0 ~ 1) | 
| ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| ☐ **雲** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─☐ 有効にする | [OFF] | ボリュメトリッククラウドの有効／無効を切り替えます。
| ├─⊖ 形状スケール | [1] (-1 ~ 2) | 雲の形状のスケールを制御します。
| ├─⊖ 形状ファクター | [0.8] (0 ~ 1) | 雲の形状ファクターを調整します。
| ├─⊖ 浸食スケール | [2] (0 ~ 5) | 雲の浸食のスケールを制御します。
| ├─⊖ 浸食ファクター | [0.8] (0 ~ 1) | 雲の浸食ファクターを調整します。
| ├─⊖ 密度 | [0.2] (0 ~ 1) | 雲の密度倍率を設定します。
| ├─☐ 影 | [OFF] | 雲の影の有効／無効を切り替えます。
| └─⊖ 風の倍率 | [3] (0 ~ 4) | 雲の移動に対する風の倍率を設定します。
| ≡ プリセット | **屋内** | スカイマップ, プロシージャル, 屋内, 薄い雲, 曇り,  |
