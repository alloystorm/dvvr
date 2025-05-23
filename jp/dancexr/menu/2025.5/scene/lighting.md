---
locale: ja-rJP
layout: single
title: ライティング
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.5/scene/lighting) | [繁中](/tw/dancexr/menu/2025.5/scene/lighting) | [日本語](/jp/dancexr/menu/2025.5/scene/lighting) | [한국어](/kr/dancexr/menu/2025.5/scene/lighting) | [简中](/zh/dancexr/menu/2025.5/scene/lighting)

[環境](../menu#環境) > ライティング

シーンのライティングを設定します。

## 設定

| 設定 | 値 | 説明 |
| :--- | --- | :--- |
| ☐ **日光** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─☐ 有効にする | [OFF] | 
| ├─⊖ 黄道角 | [0] (-90 ~ 90) | 地平線と太陽が動く平面との角度です。
| ├─⊖ 向き | [0] (-180 ~ 180) | 
| ├─⊖ 時刻 | [9] (0 ~ 24) | 特定の時間（時間単位）で太陽の角度を設定します。
| ├─⊖ 強度 | [100] (0 ~ 200) | 太陽の明るさ。
| ├─⊖ 色温度 | [6500] (1000 ~ 20000) | 日光の色温度。
| ├─⊖ スポット半径 | [0.1] (0 ~ 1) | プロシージャルスカイにおける太陽ディスクの大きさと影のぼかしに影響します。
| ├─⊖ ボリューメトリック倍率 | [1] (0 ~ 16) | 
| ├─☐ **ウィンドウ** | | 
| │ ├─☐ 有効にする | [OFF] | 
| │ ├─⊖ 幅 | [8] (0 ~ 16) | クッキーマップが有効な時のウィンドウの幅。
| │ ├─⊖ 高さ | [2] (0 ~ 16) | クッキーマップが有効な時のウィンドウの高さ。
| │ ├─⊖ 下 | [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **位置** | | 
| │ │ ├─⊖ (X) | [-2] ((Unlimited)) | 
| │ │ └─⊖ (Y) | [0] ((Unlimited)) | 
| │ ├─⊖ 行数 | [1] (0 ~ 8) | 
| │ ├─⊖ 列数 | [2] (0 ~ 8) | 
| │ ├─⊖ (Space X) | [0.05] (0 ~ 0.5) | 
| │ ├─⊖ (Space Y) | [0.05] (0 ~ 0.5) | 
| │ ├─☐ 表示 | [OFF] | シーン内にウィンドウを表示します。
| │ ├─⊖ (Origin) | [1] (-1 ~ 1) | 
| │ ├─⊖ (Sky Light) | [0.5] (0 ~ 2) | スカイライトの明るさ。
| │ ├─⊖ (Sky Light Angle) | [0] (0 ~ 90) | 
| │ └─☐ (Sky Light Shadow) | [OFF] | スカイライトのシャドウを有効にします。
| ├─☐ **影** | | Shadow settings.
| │ ├─☐ 有効にする | [OFF] | 
| │ ├─☑ モード | グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─☐ コンタクトシャドウ | [OFF] | 小さなディテールの影を有効にします。
| │ ├─⊖ サンプル数 | [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果は良いがパフォーマンスは低下します。
| │ ├─☐ ノイズ除去 | [OFF] | レイトレーシングシャドウ使用時のノイズ除去を有効にします。
| │ ├─⊖ ノイズ除去半径 | [8] (1 ~ 32) | 
| │ └─⊖ シャドウディマー | [1] (0 ~ 1) | 影の強度を減少させます。
| └─☑ レンズフレア | [ON] | レンズフレアを有効にします。
| ☑ **追加1** | | Configure light group 1
| ├─☑ 有効にする | [ON] | 
| ├─⊖ ボリューメトリック倍率 | [1] (0 ~ 16) | 
| ├─> タイプ | **ピラミッド** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **カラー** | | 
| │ ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| │ ├─⊖ 色相 | [0] (0 ~ 1) | 
| │ ├─⊖ 彩度 | [0] (0 ~ 1) | 
| │ ├─⊖ 明度 | [1] (0 ~ 1) | 
| │ ├─⊖ レッド | [1] (0 ~ 1) | 
| │ ├─⊖ グリーン | [1] (0 ~ 1) | 
| │ ├─⊖ ブルー | [1] (0 ~ 1) | 
| │ ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| │ ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| │ └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| ├─⊖ 強度 | [25] (0 ~ 100) | 
| ├─> クッキー（パターン） | **[ビデオ]** | [なし], [窓], [ブラインド], [スポット], [チューブ], [ビデオ], (love),  |
| ├─⊖ エミッタ半径 | [0.05] (0 ~ 1) | 光源のサイズ。
| ├─⊖ サイズX | [1.25] (0 ~ 16) | 
| ├─⊖ サイズY | [1.25] (0 ~ 16) | 
| ├─☑ 表示 | [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると不可視になります。
| ├─⊖ コーン長 | [1.25] (0 ~ 2) | ボリューメトリックライトのコーンの長さ。
| ├─⊖ 向き | [0] (-180 ~ 180) | 
| ├─⊖ 角度 | [25] (-90 ~ 180) | 
| ├─⊖ 距離 | [3] (0 ~ 20) | 
| ├─⊖ 高さ | [2] (0 ~ 16) | ライトの位置の高さ。
| ├─> 動的効果 | **固定** | 固定, フォローアクター, アクターの背後, 距離を維持,  |
| ├─⊖ 最大追従距離 | [5] ((Unlimited)) | 
| ├─☐ サスペンション | [OFF] | 
| ├─⊖ サスペンションセグメント | [2] (1 ~ 5) | サスペンション効果を有効化。
| ├─⊖ サスペンション距離 | [1] (0 ~ 5) | 
| ├─⊖ 揺れ速度 | [0.5] (0 ~ 1) | 揺れ運動を維持するための速度調整
| ├─☐ アクターの位置を使用 | [OFF] | ライトの配置にアクターの位置と方向を使用。
| ├─⊖ ターゲット高さ | [0] (-2 ~ 2) | 
| ├─☐ レンズフレア | [OFF] | 
| ├─☐ **リピート** | | 
| │ ├─☐ 有効にする | [OFF] | 
| │ ├─⊖ 数 | [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─☑ フォーメーション | グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─⊖ 距離 / 半径 | [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─⊖ 範囲 | [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─≡ プリセット | **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─☑ **影** | | 
| │ ├─☑ 有効にする | [ON] | 
| │ ├─☑ モード | グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─☐ コンタクトシャドウ | [OFF] | 小さなディテールの影を有効にします。
| │ ├─⊖ サンプル数 | [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果は良いがパフォーマンスは低下します。
| │ ├─☐ ノイズ除去 | [OFF] | レイトレーシングシャドウ使用時のノイズ除去を有効にします。
| │ ├─⊖ ノイズ除去半径 | [8] (1 ~ 32) | 
| │ └─⊖ シャドウディマー | [1] (0 ~ 1) | 影の強度を減少させます。
| └─≡ プリセット | **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近距離, ピラミッドプロジェクター遠距離, ボックスプロジェクター近距離, ボックスプロジェクター遠距離, スポットライト配列, スポットライト吊り下げ, ((Preset )1), (Preset 1),  |
| ☐ **追加2** | | Configure light group 2
| ├─☐ 有効にする | [OFF] | 
| ├─⊖ ボリューメトリック倍率 | [1] (0 ~ 16) | 
| ├─> タイプ | **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **カラー** | | 
| │ ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| │ ├─⊖ 色相 | [0] (0 ~ 1) | 
| │ ├─⊖ 彩度 | [0] (0 ~ 1) | 
| │ ├─⊖ 明度 | [1] (0 ~ 1) | 
| │ ├─⊖ レッド | [1] (0 ~ 1) | 
| │ ├─⊖ グリーン | [1] (0 ~ 1) | 
| │ ├─⊖ ブルー | [1] (0 ~ 1) | 
| │ ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| │ ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| │ └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| ├─⊖ 強度 | [25] (0 ~ 100) | 
| ├─> クッキー（パターン） | **[なし]** | [なし], [窓], [ブラインド], [スポット], [チューブ], [ビデオ], (love),  |
| ├─⊖ エミッタ半径 | [0.05] (0 ~ 1) | 光源のサイズ。
| ├─⊖ サイズX | [1.25] (0 ~ 16) | 
| ├─⊖ サイズY | [1.25] (0 ~ 16) | 
| ├─☑ 表示 | [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると不可視になります。
| ├─⊖ コーン長 | [1.25] (0 ~ 2) | ボリューメトリックライトのコーンの長さ。
| ├─⊖ 向き | [-135] (-180 ~ 180) | 
| ├─⊖ 角度 | [35] (-90 ~ 180) | 
| ├─⊖ 距離 | [3] (0 ~ 20) | 
| ├─⊖ 高さ | [2] (0 ~ 16) | ライトの位置の高さ。
| ├─> 動的効果 | **フォローアクター** | 固定, フォローアクター, アクターの背後, 距離を維持,  |
| ├─⊖ 最大追従距離 | [5] ((Unlimited)) | 
| ├─☐ サスペンション | [OFF] | 
| ├─⊖ サスペンションセグメント | [2] (1 ~ 5) | サスペンション効果を有効化。
| ├─⊖ サスペンション距離 | [1] (0 ~ 5) | 
| ├─⊖ 揺れ速度 | [0.5] (0 ~ 1) | 揺れ運動を維持するための速度調整
| ├─☑ アクターの位置を使用 | [ON] | ライトの配置にアクターの位置と方向を使用。
| ├─⊖ ターゲット高さ | [0] (-2 ~ 2) | 
| ├─☐ レンズフレア | [OFF] | 
| ├─☐ **リピート** | | 
| │ ├─☐ 有効にする | [OFF] | 
| │ ├─⊖ 数 | [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─☑ フォーメーション | グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─⊖ 距離 / 半径 | [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─⊖ 範囲 | [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─≡ プリセット | **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─☑ **影** | | 
| │ ├─☑ 有効にする | [ON] | 
| │ ├─☑ モード | グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─☐ コンタクトシャドウ | [OFF] | 小さなディテールの影を有効にします。
| │ ├─⊖ サンプル数 | [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果は良いがパフォーマンスは低下します。
| │ ├─☐ ノイズ除去 | [OFF] | レイトレーシングシャドウ使用時のノイズ除去を有効にします。
| │ ├─⊖ ノイズ除去半径 | [8] (1 ~ 32) | 
| │ └─⊖ シャドウディマー | [1] (0 ~ 1) | 影の強度を減少させます。
| └─≡ プリセット | **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近距離, ピラミッドプロジェクター遠距離, ボックスプロジェクター近距離, ボックスプロジェクター遠距離, スポットライト配列, スポットライト吊り下げ, ((Preset )1), (Preset 1),  |
| ☐ **追加3** | | Configure light group 3
| ├─☐ 有効にする | [OFF] | 
| ├─⊖ ボリューメトリック倍率 | [1] (0 ~ 16) | 
| ├─> タイプ | **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **カラー** | | 
| │ ├─☑ カラーモード | (RGB) | (RGB), (HSV), 
| │ ├─⊖ 色相 | [0] (0 ~ 1) | 
| │ ├─⊖ 彩度 | [0] (0 ~ 1) | 
| │ ├─⊖ 明度 | [1] (0 ~ 1) | 
| │ ├─⊖ レッド | [1] (0 ~ 1) | 
| │ ├─⊖ グリーン | [1] (0 ~ 1) | 
| │ ├─⊖ ブルー | [1] (0 ~ 1) | 
| │ ├─☐ ステージカラーを使用 | [OFF] | ステージリングの色を使用
| │ ├─☑ 色温度 | [6500] (3000 ~ 8000) | 
| │ └─≡ プリセット | **ホワイト** | ホワイト, 夕焼け, レッド, イエロー, ブルー, グリーン,  |
| ├─⊖ 強度 | [25] (0 ~ 100) | 
| ├─> クッキー（パターン） | **[なし]** | [なし], [窓], [ブラインド], [スポット], [チューブ], [ビデオ], (love),  |
| ├─⊖ エミッタ半径 | [0.05] (0 ~ 1) | 光源のサイズ。
| ├─⊖ サイズX | [1.25] (0 ~ 16) | 
| ├─⊖ サイズY | [1.25] (0 ~ 16) | 
| ├─☑ 表示 | [0] (0 ~ 4) | レンダリング時の光源の明るさを制御します。0に設定すると不可視になります。
| ├─⊖ コーン長 | [1.25] (0 ~ 2) | ボリューメトリックライトのコーンの長さ。
| ├─⊖ 向き | [135] (-180 ~ 180) | 
| ├─⊖ 角度 | [35] (-90 ~ 180) | 
| ├─⊖ 距離 | [3] (0 ~ 20) | 
| ├─⊖ 高さ | [2] (0 ~ 16) | ライトの位置の高さ。
| ├─> 動的効果 | **フォローアクター** | 固定, フォローアクター, アクターの背後, 距離を維持,  |
| ├─⊖ 最大追従距離 | [5] ((Unlimited)) | 
| ├─☐ サスペンション | [OFF] | 
| ├─⊖ サスペンションセグメント | [2] (1 ~ 5) | サスペンション効果を有効化。
| ├─⊖ サスペンション距離 | [1] (0 ~ 5) | 
| ├─⊖ 揺れ速度 | [0.5] (0 ~ 1) | 揺れ運動を維持するための速度調整
| ├─☑ アクターの位置を使用 | [ON] | ライトの配置にアクターの位置と方向を使用。
| ├─⊖ ターゲット高さ | [0] (-2 ~ 2) | 
| ├─☐ レンズフレア | [OFF] | 
| ├─☐ **リピート** | | 
| │ ├─☐ 有効にする | [OFF] | 
| │ ├─⊖ 数 | [1] (1 ~ 8) | 配列内のライトの数。
| │ ├─☑ フォーメーション | グリッド | サークル, グリッド, <br/>グリッドまたは円形配置を使用。
| │ ├─⊖ 距離 / 半径 | [7] (0 ~ 20) | グリッドモードでのライト間の距離。
| │ ├─⊖ 範囲 | [360] (0 ~ 360) | 円形モードでのライトの角度。
| │ └─≡ プリセット | **オフ** | オフ, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─☑ **影** | | 
| │ ├─☑ 有効にする | [ON] | 
| │ ├─☑ モード | グローバル設定を使用 | グローバル設定を使用, シャドウマップ, スクリーンスペース, レイトレーシング（利用可能な場合）, 
| │ ├─☐ コンタクトシャドウ | [OFF] | 小さなディテールの影を有効にします。
| │ ├─⊖ サンプル数 | [8] (1 ~ 32) | レイトレーシングシャドウ使用時のサンプル数。高いほど結果は良いがパフォーマンスは低下します。
| │ ├─☐ ノイズ除去 | [OFF] | レイトレーシングシャドウ使用時のノイズ除去を有効にします。
| │ ├─⊖ ノイズ除去半径 | [8] (1 ~ 32) | 
| │ └─⊖ シャドウディマー | [1] (0 ~ 1) | 影の強度を減少させます。
| └─≡ プリセット | **スポットライト** | スポットライト, ポイントライト, エリアライト, ピラミッドプロジェクター近距離, ピラミッドプロジェクター遠距離, ボックスプロジェクター近距離, ボックスプロジェクター遠距離, スポットライト配列, スポットライト吊り下げ, ((Preset )1), (Preset 1),  |
| ⊖ 全体強度 | [1] (0 ~ 2) | 全ライトの全体強度。
| ⊖ スカイアンビエント | [1] (0 ~ 14) | 空からの環境光の強度。
| ☐ **自動露出** | | Auto exposure settings.
| ├─☐ 有効にする | [OFF] | 
| ├─☑ 測光モード | 平均 | 平均, スポット, 中央重点, <br/>測光モードを選択してください。
| ├─☑ 補正 | (0.00) | (-3.00), (-2.75), (-2.50), (-2.25), (-2.00), (-1.75), (-1.50), (-1.25), (-1.00), (-0.75), (-0.50), (-0.25), (0.00), (0.25), (0.50), (0.75), (1.00), (1.25), (1.50), (1.75), (2.00), (2.25), (2.50), (2.75), (3.00), 
| ├─⊖ 範囲 | [0] (0 ~ 15) | 
| └─☑ アダプテーション | ノーマル | ノーマル, 速い, 瞬時, <br/>ライティング条件が変化したときの自動露出レベルの変化速度。
| ⊖ フォグ | [0] (0 ~ 1) | フォグレベル
| ⊖ ライト制限 | [8] (0 ~ 16) | シーンで使用可能なライトの最大数を設定します。
| ⊖ シャドウ制限 | [4] (0 ~ 16) | 影を持つことができるライトの最大数を設定します。
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **アロケーション** | | 
| ├─☑ 自動アロケート | 距離による | 距離による, インデックスによる（固定）, 
| ├─⊖ リフレッシュ間隔 | [8] (1 ~ 32) | ライトの再割り当ての頻度（ビート単位）。
| └─ 手動リフレッシュ || 強制的にライトを再割り当てします。
| ≡ プリセット | **プロジェクター** | 夕焼け, 日光, ウィンドウ, ステージ, シルエット, プロジェクター, エリアライト, ポイントライト配列, (Preset 1), (Preset 2), (Preset 3), (Preset 4),  |
