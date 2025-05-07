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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
|  リセット|| 
|  □ <b>布 1</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ メッシュ再構築|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> トポロジー| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ストリング接続| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> インナー半径| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 傾斜| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アーク| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 長さ| [0.25] (0 ~ 0.75) | 長さ（メートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アームホール| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バック長さ| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サイド長さ| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平解像度| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 垂直解像度| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離制約への適合性| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UVマッピング| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> トップレイヤー| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>トップアンカー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカー選択| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 選択オフセット| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> アンカーボーン| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ロックモード| **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │ │ ├─ <b>アンカーポジション</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>アンカー回転</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボトムレイヤー| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>ボトムアンカー</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカー選択| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 選択オフセット| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> アンカーボーン| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ スワップサイド| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ロックモード| **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>アンカーポジション</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>アンカー回転</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子特性</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粘着性| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 曲げ制約を有効にする| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲げ適合性| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スケール| [1] (0 ~ 2) | 
| │ ├─ □ 自己衝突| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ質量| [2] (0 ~ 4) | グリップ粒子の質量
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ摩擦| [2] (-2 ~ 4) | グリップ粒子の摩擦
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ粘着性| [0.25] (0 ~ 1) | グリップ粒子の粘着性
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ抗力| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップスケール| [1] (0 ~ 2) | 
| │ ├─ □ 引き裂きを有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き閾値| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き速度の制限| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **(Top)** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C1 マテリアル</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
| ├─ □ ガラスモード| [OFF] | 
| ├─ □ アルファをグロスとして| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ダブルサイド| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 薄暗いバック| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シャドウをキャスト| [0.5] (0 ~ 1) | 
| ├─ □ デプスプリパス| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロス| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 金属的| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バンプ| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロー| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンビエント| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アルファ| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> クリップ| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ブレンドモード| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ブレンド| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├─ □ <b>トゥーンシェーダー</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シェーディング| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アウトライン| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スペキュラー| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトスペキュラー| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ハイライトエリア| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトハイライト| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンビエント| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウエリア| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウ| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトシャドウ| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>特別シェーダー</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> モード| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 屈折| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 厚さ| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> テクスチャ| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ディテールマップ</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 有効にする| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 密度| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サイズ| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バンプ| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ (Use Circle)| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトエッジ| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> マップ選択| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップの回転| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップのスケール| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップのバンプ| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> AOに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スムーズさに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 金属に影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カラーブレンドに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 異方性| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIPマップバイアス| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|  □ <b>布 2</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ メッシュ再構築|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> トポロジー| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ストリング接続| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> インナー半径| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 傾斜| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アーク| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 長さ| [0.25] (0 ~ 0.75) | 長さ（メートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アームホール| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バック長さ| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サイド長さ| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平解像度| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 垂直解像度| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離制約への適合性| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UVマッピング| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> トップレイヤー| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>トップアンカー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカー選択| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 選択オフセット| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> アンカーボーン| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ロックモード| **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │ │ ├─ <b>アンカーポジション</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>アンカー回転</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ボトムレイヤー| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>ボトムアンカー</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカー選択| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 選択オフセット| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> アンカーボーン| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ スワップサイド| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ロックモード| **なし** | なし, ロック, ロック高さ, スティッキー,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>アンカーポジション</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>アンカー回転</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子特性</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粘着性| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 曲げ制約を有効にする| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲げ適合性| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スケール| [1] (0 ~ 2) | 
| │ ├─ □ 自己衝突| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ質量| [2] (0 ~ 4) | グリップ粒子の質量
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ摩擦| [2] (-2 ~ 4) | グリップ粒子の摩擦
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ粘着性| [0.25] (0 ~ 1) | グリップ粒子の粘着性
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ抗力| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップスケール| [1] (0 ~ 2) | 
| │ ├─ □ 引き裂きを有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き閾値| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き速度の制限| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **スカート** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C2 マテリアル</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
| ├─ □ ガラスモード| [OFF] | 
| ├─ □ アルファをグロスとして| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ダブルサイド| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 薄暗いバック| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シャドウをキャスト| [0.5] (0 ~ 1) | 
| ├─ □ デプスプリパス| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロス| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 金属的| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バンプ| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロー| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンビエント| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アルファ| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> クリップ| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ブレンドモード| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ブレンド| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
| ├─ □ <b>トゥーンシェーダー</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シェーディング| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アウトライン| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スペキュラー| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトスペキュラー| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ハイライトエリア| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトハイライト| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンビエント| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウエリア| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> シャドウ| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトシャドウ| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>特別シェーダー</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> モード| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 屈折| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 厚さ| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> テクスチャ| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ディテールマップ</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 有効にする| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 密度| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サイズ| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バンプ| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ (Use Circle)| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフトエッジ| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> マップ選択| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップの回転| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップのスケール| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ディテールマップのバンプ| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> AOに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スムーズさに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 金属に影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カラーブレンドに影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 異方性| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIPマップバイアス| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|  □ 結合| [OFF] | 布 1 と 2 を単一のシミュレーションとして結合します。これにより、2つの間での衝突が可能になりますが、速度は遅くなります。
|  □ <b>流体（実験的）</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>スポーン</b>| | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>位置</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] ((Unlimited)) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [2.5] ((Unlimited)) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] ((Unlimited)) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>回転</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-180 ~ 180) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-180 ~ 180) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-180 ~ 180) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スポーン半径| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 拡散| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スポーンレート| [20] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スピード| [5] (0 ~ 10) | 
| │ ├─ □ マウス / 手の操作| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> オートエイム| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大TTL| [10] (5 ~ 15) | この時間が経過した後にパーティクルは消失し、再出現します。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 床のTTL| [0.1] (0 ~ 1) | 床に当たった後の生存時間。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スムージング| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **スプリンクラー** | シャワー, 噴水, スプリンクラー, ハンドヘルド,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>流体</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コヒージョン| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粘度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面に付着| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲット密度| [2] (1 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コヒージョン範囲| [20] (1 ~ 50) | コヒージョン効果の最大距離
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲット距離| [10] (1 ~ 20) | コヒージョンがオフのときのパーティクル間の最小距離（mm）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 標高| [0.25] (0 ~ 0.5) | サイズに比例してパーティクルを持ち上げる
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **水** | 水, 粘着性, 砂,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>レンダー</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> パーティクルをレンダリング| [ON] | 
| │ ├─ □ 水滴をレンダリング| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水滴サイズ| [2] (0 ~ 50) | 水滴サイズ（mm）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 密度によるスケール| [0] (0 ~ 5) | 流体の密度で水滴サイズをスケールする
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 金属的| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 滑らかさ| [0.95] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロー| [0] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 透明度| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子特性</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [-2] (0 ~ 2) | 空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [-2] (0 ~ 2) | 水中抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ プレイヤー| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ジオメトリコライダー</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ □ 表示| [OFF] | 
| ├─ エクスポート形状|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>頭</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.04] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.5] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.11] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.8] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>首</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.045] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.065] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.045] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>胸</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.023] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.04] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.15] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.88] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.7] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>肋骨</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.075] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ウエスト</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.032] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.11] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [-0.3] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>腹部</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.013] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.073] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.65] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>臀部</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.0425] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.105] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.012] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.09] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>肩</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.4] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>上腕</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.15] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.035] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>前腕</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.0445] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.44] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.01] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>手</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.0315] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.0316] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ヒップ</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.027] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.1] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.455] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.1] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.085] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>太もも</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.073] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.455] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.05599999] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>すね</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.05926838] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0] (-2 ~ 2) | 
| │ ├─ <b>中間位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.009999919] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05999992] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01666657] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間半径| [0.06707321] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間曲線| [0] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.03231711] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>足</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>開始位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.03166673] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始半径| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> カーブ| [0.1] (-2 ~ 2) | 
| │ ├─ <b>終了位置</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.028] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 終了半径| [0.0625] (0 ~ 0.15) | 
| │ ├─ <b>スケール</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>メッシュコライダー</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ジオメトリコライダーを無効にする| [ON] | 
| ├─ □ 可視化| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.025] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Edge)| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Point)| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Single Collision)| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スケールをリセット| [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| ├─ □ 偶数サブステップを逆転| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| └─ □ 二段階解法| [OFF] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）,  |
