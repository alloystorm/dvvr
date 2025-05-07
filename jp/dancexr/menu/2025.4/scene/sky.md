---
locale: ja-rJP
layout: single
title: 空
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/scene/sky) | [繁中](/tw/dancexr/menu/2025.4/scene/sky) | [日本語](/jp/dancexr/menu/2025.4/scene/sky) | [한국어](/kr/dancexr/menu/2025.4/scene/sky) | [简中](/zh/dancexr/menu/2025.4/scene/sky)

[環境](../menu#環境) > 空



[(Feature Page)](/jp/dancexr/features/sky)

| Setting | Value | Description |
| :--- | --- | :--- |
| ☑ モード| プロシージャル | 色, スカイマップ, プロシージャル, <br/>(Selects the sky rendering mode: Color, Sky Map, or Procedural.)
|  ⊖ バックグラウンド| [1] (0 ~ 1) | (Controls the brightness of the sky when it is rendered.)
|  ⊖ 空の環境光| [1] (0 ~ 1) | 空が環境光にどの程度影響するかを制御します。
|  > スカイマップ| **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]),  |
|  ⊖ オリエンテーション| [0] (0 ~ 360) | (Sets the rotation of the sky in degrees.)
|  ⊖ 風| [1] (0 ~ 4) | (Global wind speed affecting cloth simulation, particle dynamics, and clouds.)
|  ⊖ 風向き| [0] (0 ~ 360) | (Sets the global wind direction in degrees.)
|  □ 風フィールド| [OFF] | 
|  ⚙️ <b>位置</b>| | Sets the position of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⚙️ <b>回転</b>| | Sets the rotation of the wind field.
| ├─ ⊖ (X)| [0] ((Unlimited)) | 
| ├─ ⊖ (Y)| [0] ((Unlimited)) | 
| └─ ⊖ (Z)| [0] ((Unlimited)) | 
|  ⊖ 距離| [5] (0 ~ 10) | (Sets the distance of the wind field.)
|  ⊖ 半径| [1] (0 ~ 2) | (Sets the radius of the wind field.)
|  ⊖ スピード| [1] (0 ~ 4) | (Sets the speed of the wind field.)
|  <b>空の環境光</b>|| 
|  ⚙️ <b>スカイカラー</b>| | 
| ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| ├─ ⊖ 明度| [1] (0 ~ 1) | 
| ├─ ⊖ 赤| [1] (0 ~ 1) | 
| ├─ ⊖ 緑| [1] (0 ~ 1) | 
| ├─ ⊖ 青| [1] (0 ~ 1) | 
| ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| ├─ ☑ 色温度| [6500] (3000 ~ 8000) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
|  ⚙️ <b>ミドルカラー</b>| | 
| ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| ├─ ⊖ 明度| [1] (0 ~ 1) | 
| ├─ ⊖ 赤| [1] (0 ~ 1) | 
| ├─ ⊖ 緑| [1] (0 ~ 1) | 
| ├─ ⊖ 青| [1] (0 ~ 1) | 
| ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| ├─ ☑ 色温度| [6500] (3000 ~ 8000) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
|  ⚙️ <b>グラウンドカラー</b>| | 
| ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| ├─ ⊖ 明度| [1] (0 ~ 1) | 
| ├─ ⊖ 赤| [1] (0 ~ 1) | 
| ├─ ⊖ 緑| [1] (0 ~ 1) | 
| ├─ ⊖ 青| [1] (0 ~ 1) | 
| ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| ├─ ☑ 色温度| [6500] (3000 ~ 8000) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
|  ☑ <b>雲</b>| | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─ ☑ 有効にする| [ON] | (Enables or disables volumetric clouds.)
| ├─ ⊖ 形状スケール| [1] (-1 ~ 2) | (Controls the scale of the cloud shapes.)
| ├─ ⊖ 形状係数| [0.8] (0 ~ 1) | (Adjusts the shape factor of the clouds.)
| ├─ ⊖ 侵食スケール| [2] (0 ~ 5) | (Controls the scale of cloud erosion.)
| ├─ ⊖ 侵食係数| [0.8] (0 ~ 1) | (Adjusts the erosion factor of the clouds.)
| ├─ ⊖ 密度| [0.2] (0 ~ 1) | (Sets the density multiplier for the clouds.)
| ├─ □ シャドウ| [OFF] | (Enables or disables cloud shadows.)
| └─ ⊖ 風の倍率| [3] (0 ~ 4) | (Sets the wind multiplier for cloud movement.)
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **薄い雲** | スカイマップ, プロシージャル, 屋内, 薄い雲, 曇り,  |
