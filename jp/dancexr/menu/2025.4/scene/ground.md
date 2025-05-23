---
locale: ja-rJP
layout: single
title: 地面
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/scene/ground) | [繁中](/tw/dancexr/menu/2025.4/scene/ground) | [日本語](/jp/dancexr/menu/2025.4/scene/ground) | [한국어](/kr/dancexr/menu/2025.4/scene/ground) | [简中](/zh/dancexr/menu/2025.4/scene/ground)

[環境](../menu#環境) > 地面



| Setting | Value | Description |
| :--- | --- | :--- |
|  ⊖ 地面の高さ| [0] (-2 ~ 2) | 
|  ☑ 地面| [OFF] | 
|  ⊖ 半径| [200] (2 ~ 100) | 地面メッシュのサイズ
|  ☑ ステージが存在する場合に非表示| [ON] | ステージモデルがある場合、地面を非表示にする
|  ⚙️ **表面**| | 
| ├─ > テクスチャ| **[タイル]** | [スカイマップ], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| ├─ ⚙️ **タイル**| | 
| │ ├─ ⊖ タイルX| [1] (0.1 ~ 10) | 
| │ ├─ ⊖ タイルY| [1] (0.1 ~ 10) | 
| │ ├─ ☑ ラップモード| リピート | リピート, ミラーU, ミラーV, ミラー両方, 
| │ ├─ ⊖ オフセットX| [0] (0 ~ 1) | 
| │ ├─ ⊖ オフセットY| [0] (0 ~ 1) | 
| │ ├─ ⊖ 回転| [0] (0 ~ 360) | 
| │ ├─ ⊖ バリエーション| [0.5] (0 ~ 1) | 
| │ └─ □ テクスチャにフィット| [OFF] | 
| ├─ ⊖ グロス| [0.95] (0 ~ 1) | 
| ├─ ⊖ 金属的| [0] (0 ~ 1) | 
| ├─ ⊖ バンプ| [0.2] (0 ~ 1) | 
| ├─ ⊖ グロー| [0] (0 ~ 10) | 
| ├─ ⊖ アンビエント| [1] (0 ~ 1) | 
| ├─ ⊖ アルファ| [1] (0 ~ 1) | 
| ├─ ⊖ クリップ| [0] (0 ~ 1) | 
| ├─ ⚙️ **色**| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 色相| [0] (0 ~ 1) | 
| │ ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| │ ├─ ⊖ 明度| [1] (0 ~ 1) | 
| │ ├─ ⊖ 赤| [1] (0 ~ 1) | 
| │ ├─ ⊖ 緑| [1] (0 ~ 1) | 
| │ ├─ ⊖ 青| [1] (0 ~ 1) | 
| │ ├─ > ブレンドモード| **ブレンド** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │ ├─ ⊖ ブレンド| [1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **黒** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├─ □ **トゥーンシェーダー**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ シェーディング| [1] (0 ~ 1) | 
| │ ├─ ⊖ アウトライン| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ スペキュラー| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトスペキュラー| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ハイライトエリア| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトハイライト| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ アンビエント| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ シャドウエリア| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ シャドウ| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ ソフトシャドウ| [0.1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├─ ⚙️ **特別シェーダー**| | 
| │ ├─ > モード| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │ ├─ ⊖ 屈折| [0.5] (1 ~ 3) | 
| │ └─ ⊖ 厚さ| [1] (0 ~ 1) | 
| ├─ ⊖ ビューアの高さ| [1.5] (0.5 ~ 3) | 地面にテクスチャを投影する際に使用されるビューアの高さ
| ├─ □ **LEDモード**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ 密度| [7] (4 ~ 10) | 
| │ ├─ ⊖ サイズ| [0.8] (0 ~ 1) | 
| │ ├─ ⊖ ソフトエッジ| [0.3] (0 ~ 1) | 
| │ ├─ ⊖ 視点角度| [1] (0 ~ 8) | 角度から見たときの明るさを低減。0＝完璧
| │ ├─ ⊖ エッジ| [0.5] (0 ~ 1) | 
| │ └─ ⊖ モアレを軽減| [0.1] (0 ~ 1) | 
| └─ ≡ プリセット| **ブラックグロス** | スカイマップ, 木材, コンクリート, 青いタイル, プロジェクタースクリーン, エミッシブスクリーン, LEDスクリーン, ブラックグロス, グロー, ガラス,  |
|  □ **影のみ**| | 
| ├─ **影の色**|| 
| ├─ ≡ プリセット| **黒** | 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange), (Preset 1),  |
| ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| ├─ ⊖ 色相| [0] (0 ~ 1) | 
| ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| ├─ ⊖ 明度| [0] (0 ~ 1) | 
| ├─ ⊖ 赤| [0] (0 ~ 1) | 
| ├─ ⊖ 緑| [0] (0 ~ 1) | 
| ├─ ⊖ 青| [0] (0 ~ 1) | 
| └─ ⊖ 透明度| [0.5] (0 ~ 1) | 
|  □ ステージ / プール| [OFF] | 
|  ≡ プリセット| **オフ** | オフ, 滑走路, プール, 部屋, 背景ボード, プロジェクタースクリーン, LEDスクリーン,  |
|  ⊖ リフト| [0.5] (-2 ~ 2) | ステージを上げる / 下げる
|  ⊖ (Front / Back Offset)| [0] (-10 ~ 10) | 
|  ⚙️ **形状**| | 
| ├─ ⊖ 中央幅| [8] (0 ~ 10) | 中央エリアの幅
| ├─ ⊖ 中央深さ| [5] (0 ~ 9) | 中央エリアの深さ
| ├─ ⊖ 後方の高さ| [0] (0 ~ 9) | 背景ボードの高さ
| ├─ ⊖ 横幅拡張| [0] (0 ~ 5) | 左右の拡張
| ├─ ⊖ 前方拡張| [0] (0 ~ 10) | 前方の拡張
| ├─ ⊖ 後方拡張| [0] (0 ~ 10) | 後方の拡張
| ├─ ⊖ 壁の高さ| [0.05] (0 ~ 5) | 地面上の端の高さ
| ├─ ⊖ 壁の厚さ| [0.1] (0 ~ 1) | 端のサイズ
| ├─ ⊖ ウィンドウ| [0] (0 ~ 1) | 
| └─ □ 浮遊| [OFF] | 
|  ⚙️ **表面**| | 
| ├─ > テクスチャ| **[ウッド1]** | [ブランク], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| ├─ ⚙️ **タイル**| | 
| │ ├─ ⊖ タイルX| [1] (0.1 ~ 10) | 
| │ ├─ ⊖ タイルY| [1] (0.1 ~ 10) | 
| │ ├─ ☑ ラップモード| リピート | リピート, ミラーU, ミラーV, ミラー両方, 
| │ ├─ ⊖ オフセットX| [0] (0 ~ 1) | 
| │ ├─ ⊖ オフセットY| [0] (0 ~ 1) | 
| │ ├─ ⊖ 回転| [0] (0 ~ 360) | 
| │ ├─ ⊖ バリエーション| [0.5] (0 ~ 1) | 
| │ └─ □ テクスチャにフィット| [OFF] | 
| ├─ ⊖ グロス| [0.95] (0 ~ 1) | 
| ├─ ⊖ 金属的| [0] (0 ~ 1) | 
| ├─ ⊖ バンプ| [0.2] (0 ~ 1) | 
| ├─ ⊖ グロー| [0] (0 ~ 10) | 
| ├─ ⊖ アンビエント| [1] (0 ~ 1) | 
| ├─ ⊖ アルファ| [1] (0 ~ 1) | 
| ├─ ⊖ クリップ| [0] (0 ~ 1) | 
| ├─ ⚙️ **色**| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 色相| [0] (0 ~ 1) | 
| │ ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| │ ├─ ⊖ 明度| [1] (0 ~ 1) | 
| │ ├─ ⊖ 赤| [1] (0 ~ 1) | 
| │ ├─ ⊖ 緑| [1] (0 ~ 1) | 
| │ ├─ ⊖ 青| [1] (0 ~ 1) | 
| │ ├─ > ブレンドモード| **ブレンド** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │ ├─ ⊖ ブレンド| [1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **白** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├─ □ **トゥーンシェーダー**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ シェーディング| [1] (0 ~ 1) | 
| │ ├─ ⊖ アウトライン| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ スペキュラー| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトスペキュラー| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ハイライトエリア| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトハイライト| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ アンビエント| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ シャドウエリア| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ シャドウ| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ ソフトシャドウ| [0.1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├─ ⚙️ **特別シェーダー**| | 
| │ ├─ > モード| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │ ├─ ⊖ 屈折| [0.5] (1 ~ 3) | 
| │ └─ ⊖ 厚さ| [1] (0 ~ 1) | 
| ├─ □ **LEDモード**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ 密度| [7] (4 ~ 10) | 
| │ ├─ ⊖ サイズ| [0.8] (0 ~ 1) | 
| │ ├─ ⊖ ソフトエッジ| [0.3] (0 ~ 1) | 
| │ ├─ ⊖ 視点角度| [1] (0 ~ 8) | 角度から見たときの明るさを低減。0＝完璧
| │ ├─ ⊖ エッジ| [0.5] (0 ~ 1) | 
| │ └─ ⊖ モアレを軽減| [0.1] (0 ~ 1) | 
| └─ ≡ プリセット| **木材** | 空白, 木材, コンクリート, 青いタイル, プロジェクタースクリーン, エミッシブスクリーン, LEDスクリーン, ブラックグロス, グロー, ガラス,  |
|  ⚙️ **後面**| | 
| ├─ > テクスチャ| **[ブランク]** | [ブランク], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| ├─ ⚙️ **タイル**| | 
| │ ├─ ⊖ タイルX| [1] (0.1 ~ 10) | 
| │ ├─ ⊖ タイルY| [1] (0.1 ~ 10) | 
| │ ├─ ☑ ラップモード| リピート | リピート, ミラーU, ミラーV, ミラー両方, 
| │ ├─ ⊖ オフセットX| [0] (0 ~ 1) | 
| │ ├─ ⊖ オフセットY| [0] (0 ~ 1) | 
| │ ├─ ⊖ 回転| [0] (0 ~ 360) | 
| │ ├─ ⊖ バリエーション| [0.5] (0 ~ 1) | 
| │ └─ ☑ テクスチャにフィット| [ON] | 
| ├─ ⊖ グロス| [0.95] (0 ~ 1) | 
| ├─ ⊖ 金属的| [0] (0 ~ 1) | 
| ├─ ⊖ バンプ| [0.2] (0 ~ 1) | 
| ├─ ⊖ グロー| [0] (0 ~ 10) | 
| ├─ ⊖ アンビエント| [1] (0 ~ 1) | 
| ├─ ⊖ アルファ| [1] (0 ~ 1) | 
| ├─ ⊖ クリップ| [0] (0 ~ 1) | 
| ├─ ⚙️ **色**| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 色相| [0] (0 ~ 1) | 
| │ ├─ ⊖ 彩度| [0] (0 ~ 1) | 
| │ ├─ ⊖ 明度| [1] (0 ~ 1) | 
| │ ├─ ⊖ 赤| [1] (0 ~ 1) | 
| │ ├─ ⊖ 緑| [1] (0 ~ 1) | 
| │ ├─ ⊖ 青| [1] (0 ~ 1) | 
| │ ├─ > ブレンドモード| **オリジナル** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │ ├─ ⊖ ブレンド| [1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **白** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├─ □ **トゥーンシェーダー**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ シェーディング| [1] (0 ~ 1) | 
| │ ├─ ⊖ アウトライン| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ スペキュラー| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトスペキュラー| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ハイライトエリア| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ソフトハイライト| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ アンビエント| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ シャドウエリア| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ シャドウ| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ ソフトシャドウ| [0.1] (0 ~ 1) | 
| │ └─ ≡ プリセット| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├─ ⚙️ **特別シェーダー**| | 
| │ ├─ > モード| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │ ├─ ⊖ 屈折| [0.5] (1 ~ 3) | 
| │ └─ ⊖ 厚さ| [1] (0 ~ 1) | 
| ├─ □ **LEDモード**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ⊖ 密度| [7] (4 ~ 10) | 
| │ ├─ ⊖ サイズ| [0.8] (0 ~ 1) | 
| │ ├─ ⊖ ソフトエッジ| [0.3] (0 ~ 1) | 
| │ ├─ ⊖ 視点角度| [1] (0 ~ 8) | 角度から見たときの明るさを低減。0＝完璧
| │ ├─ ⊖ エッジ| [0.5] (0 ~ 1) | 
| │ └─ ⊖ モアレを軽減| [0.1] (0 ~ 1) | 
| └─ ≡ プリセット| **空白** | 空白, 木材, コンクリート, 青いタイル, プロジェクタースクリーン, エミッシブスクリーン, LEDスクリーン, ブラックグロス, グロー, ガラス,  |
|  □ 水システム| [OFF] | 
|  ≡ プリセット| **オフ** | オフ, プール, (Still Water), 海洋,  |
| ☑ タイプ| プール | プール, 川, 海洋, 
|  ⊖ 高さ| [-0.1] (-2 ~ 2) | 水位の高さ
|  ⊖ 波紋| [3] (0 ~ 10) | 小波の強度
|  ⊖ 大波| [30] (0 ~ 100) | 大波の強度
|  ⊖ 屈折最大距離| [0.35] (0 ~ 3.5) | 水中の屈折深度を制限するための最大距離（メートル）。値が大きいほど歪みが増加します。
|  ⊖ 吸収距離| [5] (1 ~ 10) | 上から見たときに水中で見える最大距離。
|  ⊖ 焦点| [0.5] (0 ~ 1) | 焦点効果
|  ⊖ 吸収倍率| [2] (0 ~ 5) | 下から見るときに吸収距離に適用される倍率。
|  ≡ プリセット| **ブラックグロス** | スカイマップ, ブラックグロス, ステージ, プール, 海洋, 背景ボード, プロジェクタースクリーン, エミッシブスクリーン, (Preset 1),  |
