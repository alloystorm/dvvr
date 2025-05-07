---
locale: ja-rJP
layout: single
title: ライティング
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[環境](../menu#環境) > ライティング



[(Feature Page)](/djp/ancexr/features/lighting)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>日光</b>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 黄道角| [0] (-90 ~ 90) | 地平線と太陽が移動する面の間の角度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オリエンテーション| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間帯| [9] (0 ~ 24) | 特定の時間における太陽の角度を時間単位で設定します。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [100] (0 ~ 200) | 太陽の明るさ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色温度| [6500] (1000 ~ 20000) | 日光の色温度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スポット半径| [0.1] (0 ~ 1) | これは手続き型の空での太陽ディスクのサイズや影の柔らかさに影響を与えます。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボリュメトリック倍率| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 星| [1] (0 ~ 8) | 手続き型の空を使用しているときの夜間の星の強度を設定します。
| ├─ □ <b>ウィンドウ</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 幅| [8] (0 ~ 16) | クッキーマップが有効なときのウィンドウの幅。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高さ| [2] (0 ~ 16) | クッキーマップが有効なときのウィンドウの高さ。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 底| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [1] (0 ~ 16) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 行| [1] (0 ~ 8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 列| [2] (0 ~ 8) | 
| │ ├─ □ サークル| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 間隔| [0.05] (0 ~ 0.5) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロー| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>シャドウ</b>| | Shadow settings.
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ ☑ モード| グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─ □ 接触シャドウ| [OFF] | 細かいディテールのためにシャドウを有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サンプル数| [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果が良いが、パフォーマンスが悪化します。
| │ ├─ □ ノイズ除去| [OFF] | レイトレーシングシャドウ使用時にノイズ除去を有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ除去半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウディマー| [1] (0 ~ 1) | シャドウの強度を減少させる。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> レンズフレア| [ON] | レンズフレアを有効にする
|  □ <b>追加 1</b>| | Configure light group 1
| ├─ □ 有効にする| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボリュメトリック倍率| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> タイプ| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温度| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> クッキー| **[なし]** | [なし], [ウィンドウ], [ブラインド], [スポット], [チューブ], [ビデオ],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エミッタ半径| [0.05] (0 ~ 1) | 光源のサイズ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Xサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Yサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 表示| [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると、不可視になります。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コーンの長さ| [1.25] (0 ~ 2) | ボリュメトリックライトコーンの長さ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オリエンテーション| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [25] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高さ| [2] (0 ~ 16) | 光の位置の高さ。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ダイナミクス| **距離を維持** | 静止, フォローアクター, アクターの後ろ, 距離を維持,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大フォローディスタンス| [5] ((Unlimited)) | 
| ├─ □ サスペンション| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンションセグメント| [2] (1 ~ 5) | サスペンション効果を有効にする。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンション距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイング速度| [0.5] (0 ~ 1) | スイング動作を維持するための速度を制御
| ├─ □ アクターの位置を使用| [OFF] | ライトを配置する際にアクターの位置と向きを使用。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲットの高さ| [0] (-2 ~ 2) | 
| ├─ □ レンズフレア| [OFF] | 
| ├─ □ <b>リピート</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数| [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─ ☑ フォーメーション| グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半径| [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範囲| [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>シャドウ</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ ☑ モード| グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─ □ 接触シャドウ| [OFF] | 細かいディテールのためにシャドウを有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サンプル数| [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果が良いが、パフォーマンスが悪化します。
| │ ├─ □ ノイズ除去| [OFF] | レイトレーシングシャドウ使用時にノイズ除去を有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ除去半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウディマー| [1] (0 ~ 1) | シャドウの強度を減少させる。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近, ピラミッドプロジェクター遠, ボックスプロジェクター近, ボックスプロジェクター遠, スポットライトアレイ, サスペンドスポットライト, (Preset 1),  |
|  □ <b>追加 2</b>| | Configure light group 2
| ├─ □ 有効にする| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボリュメトリック倍率| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> タイプ| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温度| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> クッキー| **[なし]** | [なし], [ウィンドウ], [ブラインド], [スポット], [チューブ], [ビデオ],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エミッタ半径| [0.05] (0 ~ 1) | 光源のサイズ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Xサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Yサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 表示| [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると、不可視になります。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コーンの長さ| [1.25] (0 ~ 2) | ボリュメトリックライトコーンの長さ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オリエンテーション| [-135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高さ| [2] (0 ~ 16) | 光の位置の高さ。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ダイナミクス| **フォローアクター** | 静止, フォローアクター, アクターの後ろ, 距離を維持,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大フォローディスタンス| [5] ((Unlimited)) | 
| ├─ □ サスペンション| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンションセグメント| [2] (1 ~ 5) | サスペンション効果を有効にする。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンション距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイング速度| [0.5] (0 ~ 1) | スイング動作を維持するための速度を制御
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> アクターの位置を使用| [ON] | ライトを配置する際にアクターの位置と向きを使用。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲットの高さ| [0] (-2 ~ 2) | 
| ├─ □ レンズフレア| [OFF] | 
| ├─ □ <b>リピート</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数| [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─ ☑ フォーメーション| グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半径| [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範囲| [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>シャドウ</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ ☑ モード| グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─ □ 接触シャドウ| [OFF] | 細かいディテールのためにシャドウを有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サンプル数| [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果が良いが、パフォーマンスが悪化します。
| │ ├─ □ ノイズ除去| [OFF] | レイトレーシングシャドウ使用時にノイズ除去を有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ除去半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウディマー| [1] (0 ~ 1) | シャドウの強度を減少させる。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近, ピラミッドプロジェクター遠, ボックスプロジェクター近, ボックスプロジェクター遠, スポットライトアレイ, サスペンドスポットライト, (Preset 1),  |
|  □ <b>追加 3</b>| | Configure light group 3
| ├─ □ 有効にする| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボリュメトリック倍率| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> タイプ| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温度| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> クッキー| **[なし]** | [なし], [ウィンドウ], [ブラインド], [スポット], [チューブ], [ビデオ],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エミッタ半径| [0.05] (0 ~ 1) | 光源のサイズ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Xサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Yサイズ| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 表示| [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると、不可視になります。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コーンの長さ| [1.25] (0 ~ 2) | ボリュメトリックライトコーンの長さ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オリエンテーション| [135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高さ| [2] (0 ~ 16) | 光の位置の高さ。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ダイナミクス| **フォローアクター** | 静止, フォローアクター, アクターの後ろ, 距離を維持,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大フォローディスタンス| [5] ((Unlimited)) | 
| ├─ □ サスペンション| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンションセグメント| [2] (1 ~ 5) | サスペンション効果を有効にする。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サスペンション距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイング速度| [0.5] (0 ~ 1) | スイング動作を維持するための速度を制御
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> アクターの位置を使用| [ON] | ライトを配置する際にアクターの位置と向きを使用。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲットの高さ| [0] (-2 ~ 2) | 
| ├─ □ レンズフレア| [OFF] | 
| ├─ □ <b>リピート</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数| [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─ ☑ フォーメーション| グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半径| [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範囲| [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>シャドウ</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ ☑ モード| グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─ □ 接触シャドウ| [OFF] | 細かいディテールのためにシャドウを有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サンプル数| [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果が良いが、パフォーマンスが悪化します。
| │ ├─ □ ノイズ除去| [OFF] | レイトレーシングシャドウ使用時にノイズ除去を有効にする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ除去半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウディマー| [1] (0 ~ 1) | シャドウの強度を減少させる。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近, ピラミッドプロジェクター遠, ボックスプロジェクター近, ボックスプロジェクター遠, スポットライトアレイ, サスペンドスポットライト, (Preset 1),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 全体の強度| [1] (0 ~ 2) | すべてのライトの全体強度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 空の環境光| [1] (0 ~ 14) | 空からの環境光の強度。
|  □ <b>自動露出</b>| | Auto exposure settings.
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ 測定モード| 平均 | 平均, スポット, 中心加重, <br/>測定モードを選択します。
| ├─ ☑ 補償| (0.00) | (-3.00), (-2.75), (-2.50), (-2.25), (-2.00), (-1.75), (-1.50), (-1.25), (-1.00), (-0.75), (-0.50), (-0.25), (0.00), (0.25), (0.50), (0.75), (1.00), (1.25), (1.50), (1.75), (2.00), (2.25), (2.50), (2.75), (3.00), 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範囲| [0] (0 ~ 15) | 
| └─ ☑ 適応| 通常 | 通常, 高速, 瞬時, <br/>照明条件が変化したときの自動露出レベルの変化速度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 霧| [0] (0 ~ 1) | 霧レベル
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ライト制限| [8] (0 ~ 16) | シーンで利用可能な最大ライト数を設定します。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウ制限| [4] (0 ~ 16) | シャドウを持つことができる最大ライト数を設定します。
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アロケーション</b>| | 
| ├─ ☑ 自動割り当て| 距離による | 距離による, インデックスによる（固定）, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> リフレッシュ間隔| [8] (1 ~ 32) | ライトを再割り当てする頻度。ビートで。
| └─ 手動リフレッシュ|| ライトを強制的に再割り当て。
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **日中** | 夕焼け, 日中, ウィンドウ, ステージ, シルエット, プロジェクター, エリアライト, ポイントライトアレイ, (Preset 1), (Preset 2), (Preset 3),  |
