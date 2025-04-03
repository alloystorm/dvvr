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
|<nobr>有効にする</nobr>| [ON] | 
|<nobr>リセット</nobr>|| 
|<nobr>**布 1**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;メッシュ再構築</nobr>|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
|<nobr>├&nbsp;トポロジー</nobr>| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
|<nobr>├&nbsp;ストリング接続</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;インナー半径</nobr>| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
|<nobr>├&nbsp;傾斜</nobr>| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
|<nobr>├&nbsp;アーク</nobr>| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
|<nobr>├&nbsp;長さ</nobr>| [0.25] (0 ~ 0.75) | 長さ（メートル）
|<nobr>├&nbsp;アームホール</nobr>| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
|<nobr>├&nbsp;(Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
|<nobr>├&nbsp;バック長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;サイド長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;水平解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;垂直解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;距離制約への適合性</nobr>| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
|<nobr>├&nbsp;UVマッピング</nobr>| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
|<nobr>├&nbsp;**アンカー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;トップレイヤー</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;**トップアンカー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカーボーン</nobr>| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカーポジション</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカー回転</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ボトムレイヤー</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;**ボトムアンカー**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカーボーン</nobr>| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;スワップサイド</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカーポジション</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカー回転</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;**粒子特性**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;粘着性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;曲げ制約を有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;曲げ適合性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;自己衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;グリップ質量</nobr>| [2] (0 ~ 4) | グリップ粒子の質量
|<nobr>│&nbsp;├&nbsp;グリップ摩擦</nobr>| [2] (-2 ~ 4) | グリップ粒子の摩擦
|<nobr>│&nbsp;├&nbsp;グリップ粘着性</nobr>| [0.25] (0 ~ 1) | グリップ粒子の粘着性
|<nobr>│&nbsp;├&nbsp;グリップ抗力</nobr>| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
|<nobr>│&nbsp;├&nbsp;グリップスケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;引き裂きを有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;引き裂き閾値</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;引き裂き速度の制限</nobr>| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
|<nobr>└&nbsp;プリセット</nobr>| **(Top)** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr>**C1 マテリアル**</nobr>| | 
|<nobr>├&nbsp;表面</nobr>|| 
|<nobr>├&nbsp;プリセット</nobr>| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;ガラスモード</nobr>| [OFF] | 
|<nobr>├&nbsp;アルファをグロスとして</nobr>| [OFF] | 
|<nobr>├&nbsp;ダブルサイド</nobr>| [ON] | 
|<nobr>├&nbsp;薄暗いバック</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;シャドウをキャスト</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;デプスプリパス</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;グロス</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;バンプ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;グロー</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;アンビエント</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;アルファ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;クリップ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;**色**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ブレンドモード</nobr>| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;ブレンド</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
|<nobr>├&nbsp;**トゥーンシェーダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;シェーディング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;アウトライン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;スペキュラー</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトスペキュラー</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ハイライトエリア</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトハイライト</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;アンビエント</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;シャドウエリア</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;シャドウ</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトシャドウ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
|<nobr>├&nbsp;**特別シェーダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;モード</nobr>| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;屈折</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;厚さ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;テクスチャ</nobr>| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
|<nobr>└&nbsp;**ディテールマップ**</nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;**(Hexagon Map)**</nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;サイズ</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;バンプ</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;ノイズ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;ソフトエッジ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;マップ選択</nobr>| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップの回転</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップのスケール</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップのバンプ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;AOに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;スムーズさに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;金属に影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;カラーブレンドに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;異方性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIPマップバイアス</nobr>| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|<nobr>**布 2**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;メッシュ再構築</nobr>|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
|<nobr>├&nbsp;トポロジー</nobr>| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
|<nobr>├&nbsp;ストリング接続</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;インナー半径</nobr>| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
|<nobr>├&nbsp;傾斜</nobr>| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
|<nobr>├&nbsp;アーク</nobr>| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
|<nobr>├&nbsp;長さ</nobr>| [0.25] (0 ~ 0.75) | 長さ（メートル）
|<nobr>├&nbsp;アームホール</nobr>| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
|<nobr>├&nbsp;(Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
|<nobr>├&nbsp;バック長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;サイド長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;水平解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;垂直解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;距離制約への適合性</nobr>| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
|<nobr>├&nbsp;UVマッピング</nobr>| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
|<nobr>├&nbsp;**アンカー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;トップレイヤー</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;**トップアンカー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカーボーン</nobr>| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカーポジション</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;アンカー回転</nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ボトムレイヤー</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;**ボトムアンカー**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカーボーン</nobr>| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;スワップサイド</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカーポジション</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;アンカー回転</nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;**粒子特性**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;粘着性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;曲げ制約を有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;曲げ適合性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;自己衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;グリップ質量</nobr>| [2] (0 ~ 4) | グリップ粒子の質量
|<nobr>│&nbsp;├&nbsp;グリップ摩擦</nobr>| [2] (-2 ~ 4) | グリップ粒子の摩擦
|<nobr>│&nbsp;├&nbsp;グリップ粘着性</nobr>| [0.25] (0 ~ 1) | グリップ粒子の粘着性
|<nobr>│&nbsp;├&nbsp;グリップ抗力</nobr>| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
|<nobr>│&nbsp;├&nbsp;グリップスケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;引き裂きを有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;引き裂き閾値</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;引き裂き速度の制限</nobr>| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
|<nobr>└&nbsp;プリセット</nobr>| **スカート** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr>**C2 マテリアル**</nobr>| | 
|<nobr>├&nbsp;表面</nobr>|| 
|<nobr>├&nbsp;プリセット</nobr>| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;ガラスモード</nobr>| [OFF] | 
|<nobr>├&nbsp;アルファをグロスとして</nobr>| [OFF] | 
|<nobr>├&nbsp;ダブルサイド</nobr>| [ON] | 
|<nobr>├&nbsp;薄暗いバック</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;シャドウをキャスト</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;デプスプリパス</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;グロス</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;バンプ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;グロー</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;アンビエント</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;アルファ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;クリップ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;**色**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ブレンドモード</nobr>| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;ブレンド</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
|<nobr>├&nbsp;**トゥーンシェーダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;シェーディング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;アウトライン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;スペキュラー</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトスペキュラー</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ハイライトエリア</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトハイライト</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;アンビエント</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;シャドウエリア</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;シャドウ</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソフトシャドウ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
|<nobr>├&nbsp;**特別シェーダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;モード</nobr>| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;屈折</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;厚さ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;テクスチャ</nobr>| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
|<nobr>└&nbsp;**ディテールマップ**</nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;**(Hexagon Map)**</nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;サイズ</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;バンプ</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;ノイズ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;ソフトエッジ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;マップ選択</nobr>| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップの回転</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップのスケール</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ディテールマップのバンプ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;AOに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;スムーズさに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;金属に影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;カラーブレンドに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;異方性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIPマップバイアス</nobr>| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|<nobr>結合</nobr>| [OFF] | 布 1 と 2 を単一のシミュレーションとして結合します。これにより、2つの間での衝突が可能になりますが、速度は遅くなります。
|<nobr>**流体（実験的）**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;**スポーン**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;**位置**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;├&nbsp;**回転**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;スポーン半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;拡散</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;スポーンレート</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;スピード</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;マウス / 手の操作</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;オートエイム</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;最大TTL</nobr>| [10] (5 ~ 15) | この時間が経過した後にパーティクルは消失し、再出現します。
|<nobr>│&nbsp;├&nbsp;床のTTL</nobr>| [0.1] (0 ~ 1) | 床に当たった後の生存時間。
|<nobr>│&nbsp;├&nbsp;スムージング</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **スプリンクラー** | シャワー, 噴水, スプリンクラー, ハンドヘルド,  |
|<nobr>├&nbsp;**流体**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;コヒージョン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粘度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;表面に付着</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ターゲット密度</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;コヒージョン範囲</nobr>| [20] (1 ~ 50) | コヒージョン効果の最大距離
|<nobr>│&nbsp;├&nbsp;ターゲット距離</nobr>| [10] (1 ~ 20) | コヒージョンがオフのときのパーティクル間の最小距離（mm）
|<nobr>│&nbsp;├&nbsp;標高</nobr>| [0.25] (0 ~ 0.5) | サイズに比例してパーティクルを持ち上げる
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **水** | 水, 粘着性, 砂,  |
|<nobr>├&nbsp;**レンダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;パーティクルをレンダリング</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;水滴をレンダリング</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;水滴サイズ</nobr>| [2] (0 ~ 50) | 水滴サイズ（mm）
|<nobr>│&nbsp;├&nbsp;密度によるスケール</nobr>| [0] (0 ~ 5) | 流体の密度で水滴サイズをスケールする
|<nobr>│&nbsp;├&nbsp;**色**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;滑らかさ</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;グロー</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;**粒子特性**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [-2] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [-2] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [OFF] | 
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
|<nobr>**ジオメトリコライダー**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;表示</nobr>| [OFF] | 
|<nobr>├&nbsp;エクスポート形状</nobr>|| 
|<nobr>├&nbsp;**頭**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**首**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**胸**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;**肋骨**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**ウエスト**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;**腹部**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;**臀部**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**肩**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**上腕**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**前腕**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**手**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**ヒップ**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**太もも**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**すね**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;中間位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;中間半径</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;中間曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;**足**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;開始位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;開始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;終了位置</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;終了半径</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;スケール</nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr>**メッシュコライダー**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;ジオメトリコライダーを無効にする</nobr>| [ON] | 
|<nobr>├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>├&nbsp;深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;(Skip Edge)</nobr>| [ON] | 
|<nobr>├&nbsp;(Skip Point)</nobr>| [ON] | 
|<nobr>└&nbsp;(Single Collision)</nobr>| [ON] | 
|<nobr>**シミュレーション設定**</nobr>| | 
|<nobr>├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;スケールをリセット</nobr>| [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
|<nobr>├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
