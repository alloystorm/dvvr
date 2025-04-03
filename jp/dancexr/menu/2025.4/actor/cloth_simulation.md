---
locale: ja-rJP
layout: single
title: シミュレーション
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[プロ版](../menu#プロ版) > シミュレーション



| Setting | Value | Description |
| :--- | --- | :--- |
| 有効にする | ON | 
| リセット || 
| **布 1** | | 
| ├&nbsp;有効にする | OFF | 
| ├&nbsp;メッシュ再構築 || ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;トポロジー | **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
| ├&nbsp;ストリング接続 | [4] (1 ~ 10) | 
| ├&nbsp;インナー半径 | [0.08] (0 ~ 0.2) | 内円の半径（メートル）
| ├&nbsp;傾斜 | [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
| ├&nbsp;アーク | [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
| ├&nbsp;長さ | [0.25] (0 ~ 0.75) | 長さ（メートル）
| ├&nbsp;アームホール | [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
| ├&nbsp;バック長さ | [1] (0.1 ~ 1.9) | 
| ├&nbsp;サイド長さ | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平解像度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直解像度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距離制約への適合性 | [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UVマッピング | **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
| ├&nbsp;**アンカー** | | 
| │&nbsp;├&nbsp;トップレイヤー | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**トップアンカー** | | 
| │&nbsp;│&nbsp;├&nbsp;アンカー選択 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;選択オフセット | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;アンカーボーン | **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;ロックモード | **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │&nbsp;│&nbsp;├&nbsp;アンカーポジション || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;アンカー回転 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;ボトムレイヤー | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**ボトムアンカー** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカー選択 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;選択オフセット | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;アンカーボーン | **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;スワップサイド | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;ロックモード | **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカーポジション || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカー回転 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子特性** | | 
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;├&nbsp;粘着性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;曲げ制約を有効にする | ON | 
| │&nbsp;├&nbsp;曲げ適合性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;スケール | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自己衝突 | OFF | 
| │&nbsp;├&nbsp;グリップ質量 | [2] (0 ~ 4) | グリップ粒子の質量
| │&nbsp;├&nbsp;グリップ摩擦 | [2] (-2 ~ 4) | グリップ粒子の摩擦
| │&nbsp;├&nbsp;グリップ粘着性 | [0.25] (0 ~ 1) | グリップ粒子の粘着性
| │&nbsp;├&nbsp;グリップ抗力 | [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| │&nbsp;├&nbsp;グリップスケール | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;引き裂きを有効にする | OFF | 
| │&nbsp;├&nbsp;引き裂き閾値 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;引き裂き速度の制限 | [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| └&nbsp;(Presets: Top) || 
| &nbsp;&nbsp;プリセット | **(Top)** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C1 マテリアル** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;プリセット | **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;ガラスモード | OFF | 
| ├&nbsp;アルファをグロスとして | OFF | 
| ├&nbsp;ダブルサイド | ON | 
| ├&nbsp;薄暗いバック | [1] (0 ~ 1) | 
| ├&nbsp;シャドウをキャスト | [0.5] (0 ~ 1) | 
| ├&nbsp;デプスプリパス | [0.8] (0 ~ 1) | 
| ├&nbsp;グロス | [0.3] (0 ~ 1) | 
| ├&nbsp;金属的 | [0] (0 ~ 1) | 
| ├&nbsp;バンプ | [0.2] (0 ~ 1) | 
| ├&nbsp;グロー | [0] (0 ~ 10) | 
| ├&nbsp;アンビエント | [1] (0 ~ 1) | 
| ├&nbsp;アルファ | [1] (0 ~ 1) | 
| ├&nbsp;クリップ | [0] (0 ~ 1) | 
| ├&nbsp;**色** | | 
| │&nbsp;├&nbsp;カラーモード | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;彩度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;明度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;赤 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;緑 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;青 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;ブレンドモード | **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │&nbsp;├&nbsp;ブレンド | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├&nbsp;**トゥーンシェーダー** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;シェーディング | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;アウトライン | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;スペキュラー | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトスペキュラー | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ハイライトエリア | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトハイライト | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;アンビエント | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;シャドウエリア | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;シャドウ | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトシャドウ | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├&nbsp;**特別シェーダー** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;モード | **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │&nbsp;├&nbsp;屈折 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚さ | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;テクスチャ | **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| └&nbsp;**ディテールマップ** | | 
| &nbsp;&nbsp;├&nbsp;有効にする | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;有効にする | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;サイズ | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;バンプ | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;ノイズ | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;ソフトエッジ | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;マップ選択 | **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
| &nbsp;&nbsp;├&nbsp;ディテールマップの回転 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;ディテールマップのスケール | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;ディテールマップのバンプ | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;AOに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;スムーズさに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;金属に影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;カラーブレンドに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;異方性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIPマップバイアス | [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
| **布 2** | | 
| ├&nbsp;有効にする | OFF | 
| ├&nbsp;メッシュ再構築 || ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;トポロジー | **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
| ├&nbsp;ストリング接続 | [4] (1 ~ 10) | 
| ├&nbsp;インナー半径 | [0.08] (0 ~ 0.2) | 内円の半径（メートル）
| ├&nbsp;傾斜 | [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
| ├&nbsp;アーク | [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
| ├&nbsp;長さ | [0.25] (0 ~ 0.75) | 長さ（メートル）
| ├&nbsp;アームホール | [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
| ├&nbsp;バック長さ | [1] (0.1 ~ 1.9) | 
| ├&nbsp;サイド長さ | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平解像度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直解像度 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距離制約への適合性 | [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UVマッピング | **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
| ├&nbsp;**アンカー** | | 
| │&nbsp;├&nbsp;トップレイヤー | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**トップアンカー** | | 
| │&nbsp;│&nbsp;├&nbsp;アンカー選択 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;選択オフセット | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;アンカーボーン | **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;ロックモード | **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │&nbsp;│&nbsp;├&nbsp;アンカーポジション || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;アンカー回転 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;ボトムレイヤー | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**ボトムアンカー** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカー選択 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;選択オフセット | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;アンカーボーン | **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;スワップサイド | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;ロックモード | **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカーポジション || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;アンカー回転 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子特性** | | 
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;├&nbsp;粘着性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;曲げ制約を有効にする | ON | 
| │&nbsp;├&nbsp;曲げ適合性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;スケール | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自己衝突 | OFF | 
| │&nbsp;├&nbsp;グリップ質量 | [2] (0 ~ 4) | グリップ粒子の質量
| │&nbsp;├&nbsp;グリップ摩擦 | [2] (-2 ~ 4) | グリップ粒子の摩擦
| │&nbsp;├&nbsp;グリップ粘着性 | [0.25] (0 ~ 1) | グリップ粒子の粘着性
| │&nbsp;├&nbsp;グリップ抗力 | [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| │&nbsp;├&nbsp;グリップスケール | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;引き裂きを有効にする | OFF | 
| │&nbsp;├&nbsp;引き裂き閾値 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;引き裂き速度の制限 | [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| └&nbsp;(Presets: Skirt) || 
| &nbsp;&nbsp;プリセット | **スカート** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C2 マテリアル** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;プリセット | **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;ガラスモード | OFF | 
| ├&nbsp;アルファをグロスとして | OFF | 
| ├&nbsp;ダブルサイド | ON | 
| ├&nbsp;薄暗いバック | [1] (0 ~ 1) | 
| ├&nbsp;シャドウをキャスト | [0.5] (0 ~ 1) | 
| ├&nbsp;デプスプリパス | [0.8] (0 ~ 1) | 
| ├&nbsp;グロス | [0.3] (0 ~ 1) | 
| ├&nbsp;金属的 | [0] (0 ~ 1) | 
| ├&nbsp;バンプ | [0.2] (0 ~ 1) | 
| ├&nbsp;グロー | [0] (0 ~ 10) | 
| ├&nbsp;アンビエント | [1] (0 ~ 1) | 
| ├&nbsp;アルファ | [1] (0 ~ 1) | 
| ├&nbsp;クリップ | [0] (0 ~ 1) | 
| ├&nbsp;**色** | | 
| │&nbsp;├&nbsp;カラーモード | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;彩度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;明度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;赤 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;緑 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;青 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;ブレンドモード | **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │&nbsp;├&nbsp;ブレンド | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├&nbsp;**トゥーンシェーダー** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;シェーディング | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;アウトライン | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;スペキュラー | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトスペキュラー | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ハイライトエリア | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトハイライト | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;アンビエント | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;シャドウエリア | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;シャドウ | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソフトシャドウ | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├&nbsp;**特別シェーダー** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;モード | **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │&nbsp;├&nbsp;屈折 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚さ | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;テクスチャ | **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| └&nbsp;**ディテールマップ** | | 
| &nbsp;&nbsp;├&nbsp;有効にする | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;有効にする | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;サイズ | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;バンプ | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;ノイズ | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;ソフトエッジ | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;マップ選択 | **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
| &nbsp;&nbsp;├&nbsp;ディテールマップの回転 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;ディテールマップのスケール | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;ディテールマップのバンプ | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;AOに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;スムーズさに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;金属に影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;カラーブレンドに影響 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;異方性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIPマップバイアス | [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
| 結合 | OFF | 布 1 と 2 を単一のシミュレーションとして結合します。これにより、2つの間での衝突が可能になりますが、速度は遅くなります。
| **流体（実験的）** | | 
| ├&nbsp;有効にする | OFF | 
| ├&nbsp;**スポーン** | | 
| │&nbsp;├&nbsp;**位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] ((Unlimited)) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [2.5] ((Unlimited)) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] ((Unlimited)) | 
| │&nbsp;├&nbsp;**回転** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;スポーン半径 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;拡散 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;スポーンレート | [20] (0 ~ 20) | 
| │&nbsp;├&nbsp;スピード | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;マウス / 手の操作 | OFF | 
| │&nbsp;├&nbsp;オートエイム | ON | 
| │&nbsp;├&nbsp;最大TTL | [10] (5 ~ 15) | この時間が経過した後にパーティクルは消失し、再出現します。
| │&nbsp;├&nbsp;床のTTL | [0.1] (0 ~ 1) | 床に当たった後の生存時間。
| │&nbsp;├&nbsp;スムージング | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sprinkler) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **スプリンクラー** | シャワー, 噴水, スプリンクラー, ハンドヘルド,  |
| ├&nbsp;**流体** | | 
| │&nbsp;├&nbsp;コヒージョン | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;粘度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;表面に付着 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ターゲット密度 | [2] (1 ~ 10) | 
| │&nbsp;├&nbsp;コヒージョン範囲 | [20] (1 ~ 50) | コヒージョン効果の最大距離
| │&nbsp;├&nbsp;ターゲット距離 | [10] (1 ~ 20) | コヒージョンがオフのときのパーティクル間の最小距離（mm）
| │&nbsp;├&nbsp;標高 | [0.25] (0 ~ 0.5) | サイズに比例してパーティクルを持ち上げる
| │&nbsp;└&nbsp;(Presets: Water) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **水** | 水, 粘着性, 砂,  |
| ├&nbsp;**レンダー** | | 
| │&nbsp;├&nbsp;パーティクルをレンダリング | ON | 
| │&nbsp;├&nbsp;水滴をレンダリング | OFF | 
| │&nbsp;├&nbsp;水滴サイズ | [2] (0 ~ 50) | 水滴サイズ（mm）
| │&nbsp;├&nbsp;密度によるスケール | [0] (0 ~ 5) | 流体の密度で水滴サイズをスケールする
| │&nbsp;├&nbsp;**色** | | 
| │&nbsp;│&nbsp;├&nbsp;カラーモード | (RGB) | (RGB), (HSV), 
| │&nbsp;│&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;彩度 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;明度 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;赤 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;緑 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;青 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;金属的 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;滑らかさ | [0.95] (0 ~ 1) | 
| │&nbsp;├&nbsp;グロー | [0] (0 ~ 1) | 
| │&nbsp;└&nbsp;透明度 | [0.1] (0 ~ 1) | 
| ├&nbsp;**粒子特性** | | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空気の抗力 | [-2] (0 ~ 2) | 空気抵抗
| │&nbsp;├&nbsp;水中の抗力 | [-2] (0 ~ 2) | 水中抵抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風の影響 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）,  |
| **ジオメトリコライダー** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;表示 | OFF | 
| ├&nbsp;エクスポート形状 || 
| ├&nbsp;**頭** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.04] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.5] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**首** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.065] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**胸** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.023] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.04] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [0.88] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.7] (0 ~ 1) | 
| ├&nbsp;**肋骨** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0.075] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**ウエスト** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.032] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [-0.3] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.8] (0 ~ 1) | 
| ├&nbsp;**腹部** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.013] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.073] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.65] (0 ~ 1) | 
| ├&nbsp;**臀部** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.0425] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.105] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.012] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.09] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**肩** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [-0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.4] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**上腕** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.15] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.035] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**前腕** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.0445] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.44] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.01] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**手** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.0315] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [-0.0316] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**ヒップ** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.027] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.1] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.1] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.085] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**太もも** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.073] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.05599999] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**すね** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.05926838] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;中間位置 || 
| │&nbsp;├&nbsp;(X) | [0.009999919] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05999992] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01666657] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;中間半径 | [0.06707321] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;中間曲線 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.03231711] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**足** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;開始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.03166673] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;開始半径 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;カーブ | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;終了位置 || 
| │&nbsp;├&nbsp;(X) | [0.028] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;終了半径 | [0.0625] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;スケール || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| **メッシュコライダー** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;ジオメトリコライダーを無効にする | ON | 
| ├&nbsp;可視化 | OFF | 
| ├&nbsp;深度 | [0.025] (0 ~ 0.1) | 
| ├&nbsp;(Skip Edge) | ON | 
| ├&nbsp;(Skip Point) | ON | 
| └&nbsp;(Single Collision) | ON | 
| **シミュレーション設定** | | 
| ├&nbsp;ドラッグを有効にする | ON | 
| ├&nbsp;スケールをリセット | [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
| ├&nbsp;シミュレート | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| ├&nbsp;サブステップ | [4] (1 ~ 20) | 
| ├&nbsp;イテレーション | [1] (0 ~ 10) | 
| ├&nbsp;偶数サブステップを逆転 | OFF | 
| ├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| ├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| └&nbsp;二段階解法 | OFF | 
| (Presets: Default (Reset)) || 
| プリセット | **デフォルト（リセット）** | デフォルト（リセット）,  |
