---
locale: ja-rJP
layout: single
title: グラフィックス
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[システム](../menu#システム) > グラフィックス



| Setting | Value | Description |
| :--- | --- | :--- |
| (Anti-Aliasing: Deferred SMAA) || 0/18/True
| アンチエイリアス | **ディファードSMAA** | AAなし, ディファードSMAA, ディファードTAA,  |
| **レイトレーシング** | | 1/18/True
| ├ (Enable Raytracing) | ON | 0/8/False
| ├ 反射 | ON | 1/8/False
| ├ 環境光遮蔽 | ON | 2/8/False
| ├ グローバルイルミネーション | ON | 3/8/False
| ├ シャドウ | ON | 4/8/False
| ├ 接触シャドウ | OFF | 5/8/False
| ├ レイの長さ | [50] (0 ~ 100) | 6/8/False
| ├ ノイズ除去 | ON | 7/8/False
| └ ノイズ除去半径 | [0.1] (0 ~ 1) | 8/8/False
| (Super Sampling: Off) || 2/18/True
| スーパサンプリング | **オフ** | オフ, DLSSパフォーマンス, DLSSバランス, DLSSクオリティ, DLSSウルトラパフォーマンス, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **反射** | | 3/18/True
| ├ (Enable Reflection) | ON | 0/7/False
| ├ モード | スクリーンスペース | スクリーンスペース, プローブ, 1/7/False
| ├ クオリティ | 高 | 低, 中, 高, 2/7/False
| ├ アルゴリズム | 近似 | 近似, PBR蓄積, <br/>スクリーンスペース反射のためのアルゴリズム。3/7/False
| ├ エッジフェードディスタンス | [0.1] (0 ~ 1) | 4/7/False
| ├ オブジェクトの厚さ | [0.01] (0 ~ 0.1) | 5/7/False
| ├ 空にフォールバック | ON | レイトレーシングにヒットがない場合、空の色にフォールバックします。6/7/False
| └ 空の反射 | ON | 7/7/False
| **霧** | | 4/18/True
| ├ (Enable Fog) | ON | 0/4/False
| ├ ボリュメトリックフォグ | ON | 1/4/False
| ├ ベース高さ | [0] (0 ~ 10) | 2/4/False
| ├ 最大高さ | [25] (10 ~ 100) | 3/4/False
| └ 最大距離 | [5000] (0 ~ 10000) | 4/4/False
| **環境光遮蔽** | | 5/18/True
| ├ (Enable Ambient Occlusion) | OFF | 0/2/False
| ├ クオリティ | 高 | 低, 中, 高, 1/2/False
| └ 強度 | [1] (0 ~ 1) | 2/2/False
| **グローバルイルミネーション** | | 6/18/True
| ├ (Enable Global Illumination) | OFF | 0/2/False
| ├ クオリティ | 低 | 低, 中, 高, 1/2/False
| └ 空にフォールバック | ON | 2/2/False
| **被写界深度** | | 7/18/True
| ├ (Enable Depth Of Field) | OFF | 0/3/False
| ├ クオリティ | 中 | 低, 中, 高, 1/3/False
| ├ 強度 | [0.25] (0 ~ 1) | 2/3/False
| └ オフセット | [0.1] (-1 ~ 1) | 3/3/False
| **モーションブラー** | | 8/18/True
| ├ (Enable Motion Blur) | OFF | 0/2/False
| ├ クオリティ | 中 | 低, 中, 高, 1/2/False
| └ 強度 | [0.25] (0 ~ 1) | 2/2/False
| **ブルーム** | | 9/18/True
| ├ (Enable Bloom) | ON | 0/2/False
| ├ クオリティ | 高 | 低, 中, 高, 1/2/False
| └ 強度 | [0.25] (0 ~ 1) | 2/2/False
| **レンズフレア** | | 10/18/True
| ├ (Enable Lens Flare) | ON | 0/7/False
| ├ VRで無効化 | ON | この効果はVRには推奨されません1/7/False
| ├ 強度 | [0.1] (0 ~ 1) | 2/7/False
| ├ **色** | | 3/7/False
| │ ├ カラーモード | (RGB) | (RGB), (HSV), 0/8/True
| │ ├ 色相 | [0] (0 ~ 1) | 1/8/True
| │ ├ 彩度 | [0] (0 ~ 1) | 2/8/True
| │ ├ 明度 | [1] (0 ~ 1) | 3/8/True
| │ ├ 赤 | [1] (0 ~ 1) | 4/8/True
| │ ├ 緑 | [1] (0 ~ 1) | 5/8/True
| │ ├ 青 | [1] (0 ~ 1) | 6/8/True
| │ ├ ステージカラーを使用 | OFF | ステージリングからの色を使用7/8/True
| │ ├ 色温度 | [6500] (3000 ~ 8000) | 8/8/True
| │ └ プリセット | **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| ├ フレア | [1] (0 ~ 1) | 4/7/False
| ├ ストリーク | [0.2] (0 ~ 1) | 5/7/False
| ├ 長さ | [0.5] (0 ~ 1) | 6/7/False
| └ 色収差 | [0.5] (0 ~ 1) | 7/7/False
| **カラー補正** | | 11/18/True
| ├ (Enable Color Adjustment) | ON | 0/5/False
| ├ ポスト露出 | [0] (-12 ~ 12) | 1/5/False
| ├ コントラスト | [1] (-100 ~ 100) | 2/5/False
| ├ 色相シフト | [0] (-180 ~ 180) | 3/5/False
| ├ 彩度 | [1] (-100 ~ 100) | 4/5/False
| └ **カラーフィルター** | | 5/5/False
|   ├ カラーモード | (HSV) | (RGB), (HSV), 0/7/True
|   ├ 色相 | [0] (0 ~ 1) | 1/7/True
|   ├ 彩度 | [0] (0 ~ 1) | 2/7/True
|   ├ 明度 | [1] (0 ~ 1) | 3/7/True
|   ├ 赤 | [1] (0 ~ 1) | 4/7/True
|   ├ 緑 | [1] (0 ~ 1) | 5/7/True
|   ├ 青 | [1] (0 ~ 1) | 6/7/True
|   ├ グロー | [1] (0 ~ 20) | 7/7/True
|   └ プリセット | **白** | 白, 赤, 緑, 青, アニメーション色相, 音楽による光,  |
| **カラー曲線** | | 12/18/True
| ├ (Enable Color Curve) | ON | 0/6/False
| ├ スタートグラデーション | [1] (0 ~ 4) | 1/6/False
| ├ 開始位置 | [0] (0 ~ 0.5) | 2/6/False
| ├ スタート値 | [0] (0 ~ 0.5) | 3/6/False
| ├ エンドグラデーション | [1] (0 ~ 4) | 4/6/False
| ├ エンド位置 | [1] (0.5 ~ 1) | 5/6/False
| └ エンド値 | [1] (0.5 ~ 1) | 6/6/False
| **ホワイトバランス** | | 13/18/True
| ├ (Enable White Balance) | ON | 0/2/False
| ├ 温度 | [0] (-100 ~ 100) | 1/2/False
| └ ティント | [0] (-100 ~ 100) | 2/2/False
| **スペシャルレンダー** | | 14/18/True
| ├ (Enable Special Render) | OFF | 0/5/False
| ├ モード | 深度出力 | 深度出力, ノーマル出力, 1/5/False
| ├ 深度範囲 | [1] (0 ~ 1) | 2/5/False
| ├ 深度スケール | [0.25] (0 ~ 1) | 3/5/False
| ├ ノーマルスケール | [1] (0 ~ 1) | 4/5/False
| └ ノーマルブレンド | [0] (0 ~ 1) | 5/5/False
| トーンマッピング | カスタム | なし, ニュートラル, ACES, カスタム, 15/18/True
| アクターズトゥーンシェーディング | OFF | すべてのアクターにトゥーンシェーディングを使用します。16/18/True
| ステージトゥーンシェーディング | OFF | ステージと小道具にトゥーンシェーディングを使用します。17/18/True
| **オプション** | | 18/18/True
| ├ トランスペアレントプリパス | ON | トランスペアレントプリパスを有効にします。これにより、隠れた透明素材が見えなくなります。0/5/False
| ├ スクリーンスペースシャドウ | ON | 1/5/False
| ├ 接触シャドウ | OFF | 小さなディテールのためのシャドウ。2/5/False
| ├ バンプマップシャドウ | [0.5] (0 ~ 1) | バンプマップとディテールマップのためのシャドウを有効にします。3/5/False
| ├ NaNを停止 | ON | (Prevent black screen when error happens during post processing. )4/5/False
| └ 厚さを計算 | ON | スキン効果に使用できる厚さを計算します。5/5/False
| プリセット | **高** | パフォーマンス, 中, 高, インドアGI, アウトドアGI, トゥーン効果,  |
