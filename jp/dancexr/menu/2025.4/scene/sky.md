---
locale: ja-rJP
layout: single
title: 空
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/scene/sky) | [繁中](/tw/dancexr/menu/2025.4/scene/sky) | [日本語](/jp/dancexr/menu/2025.4/scene/sky) | [한국어](/kr/dancexr/menu/2025.4/scene/sky) | [简中](/zh/dancexr/menu/2025.4/scene/sky)

[環境](../menu#環境) > 空



| Setting | Value | Description |
| :--- | --- | :--- |
| モード | プロシージャル | 色, スカイマップ, プロシージャル, <br/>(Selects the sky rendering mode: Color, Sky Map, or Procedural.)0/17/True
| バックグラウンド | [1] (0 ~ 1) | (Controls the brightness of the sky when it is rendered.)1/17/True
| 空の環境光 | [1] (0 ~ 1) | 空が環境光にどの程度影響するかを制御します。2/17/True
| (Sky Map: [Cloud]) || 3/17/True
| スカイマップ | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]),  |
| オリエンテーション | [0] (0 ~ 360) | (Sets the rotation of the sky in degrees.)4/17/True
| 風 | [1] (0 ~ 4) | (Global wind speed affecting cloth simulation, particle dynamics, and clouds.)5/17/True
| 風向き | [0] (0 ~ 360) | (Sets the global wind direction in degrees.)6/17/True
| 風フィールド | OFF | 7/17/True
| **位置** | | Sets the position of the wind field.8/17/True
| ├ (X) | [0] ((Unlimited)) | 0/2/False
| ├ (Y) | [0] ((Unlimited)) | 1/2/False
| └ (Z) | [0] ((Unlimited)) | 2/2/False
| **回転** | | Sets the rotation of the wind field.9/17/True
| ├ (X) | [0] ((Unlimited)) | 0/2/False
| ├ (Y) | [0] ((Unlimited)) | 1/2/False
| └ (Z) | [0] ((Unlimited)) | 2/2/False
| 距離 | [5] (0 ~ 10) | (Sets the distance of the wind field.)10/17/True
| 半径 | [1] (0 ~ 2) | (Sets the radius of the wind field.)11/17/True
| スピード | [1] (0 ~ 4) | (Sets the speed of the wind field.)12/17/True
| 空の環境光 || 13/17/True
| **スカイカラー** | | 14/17/True
| ├ カラーモード | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 彩度 | [0] (0 ~ 1) | 2/8/True
| ├ 明度 | [1] (0 ~ 1) | 3/8/True
| ├ 赤 | [1] (0 ~ 1) | 4/8/True
| ├ 緑 | [1] (0 ~ 1) | 5/8/True
| ├ 青 | [1] (0 ~ 1) | 6/8/True
| ├ ステージカラーを使用 | OFF | ステージリングからの色を使用7/8/True
| ├ 色温度 | [6500] (3000 ~ 8000) | 8/8/True
| └ プリセット | **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| **ミドルカラー** | | 15/17/True
| ├ カラーモード | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 彩度 | [0] (0 ~ 1) | 2/8/True
| ├ 明度 | [1] (0 ~ 1) | 3/8/True
| ├ 赤 | [1] (0 ~ 1) | 4/8/True
| ├ 緑 | [1] (0 ~ 1) | 5/8/True
| ├ 青 | [1] (0 ~ 1) | 6/8/True
| ├ ステージカラーを使用 | OFF | ステージリングからの色を使用7/8/True
| ├ 色温度 | [6500] (3000 ~ 8000) | 8/8/True
| └ プリセット | **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| **グラウンドカラー** | | 16/17/True
| ├ カラーモード | (RGB) | (RGB), (HSV), 0/8/True
| ├ 色相 | [0] (0 ~ 1) | 1/8/True
| ├ 彩度 | [0] (0 ~ 1) | 2/8/True
| ├ 明度 | [1] (0 ~ 1) | 3/8/True
| ├ 赤 | [1] (0 ~ 1) | 4/8/True
| ├ 緑 | [1] (0 ~ 1) | 5/8/True
| ├ 青 | [1] (0 ~ 1) | 6/8/True
| ├ ステージカラーを使用 | OFF | ステージリングからの色を使用7/8/True
| ├ 色温度 | [6500] (3000 ~ 8000) | 8/8/True
| └ プリセット | **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| **雲** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.17/17/True
| ├ (Enable Cloud) | ON | (Enables or disables volumetric clouds.)0/7/False
| ├ 形状スケール | [1] (-1 ~ 2) | (Controls the scale of the cloud shapes.)1/7/False
| ├ 形状係数 | [0.8] (0 ~ 1) | (Adjusts the shape factor of the clouds.)2/7/False
| ├ 侵食スケール | [2] (0 ~ 5) | (Controls the scale of cloud erosion.)3/7/False
| ├ 侵食係数 | [0.8] (0 ~ 1) | (Adjusts the erosion factor of the clouds.)4/7/False
| ├ 密度 | [0.2] (0 ~ 1) | (Sets the density multiplier for the clouds.)5/7/False
| ├ シャドウ | OFF | (Enables or disables cloud shadows.)6/7/False
| └ 風の倍率 | [3] (0 ~ 4) | (Sets the wind multiplier for cloud movement.)7/7/False
| プリセット | **薄い雲** | スカイマップ, プロシージャル, 屋内, 薄い雲, 曇り,  |
