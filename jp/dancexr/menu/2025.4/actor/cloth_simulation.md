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
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr> リセット</nobr>|| 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>布 1</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; メッシュ再構築</nobr>|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) トポロジー</nobr>| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) ストリング接続</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) インナー半径</nobr>| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 傾斜</nobr>| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アーク</nobr>| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 長さ</nobr>| [0.25] (0 ~ 0.75) | 長さ（メートル）
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アームホール</nobr>| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) バック長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) サイド長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 垂直解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 距離制約への適合性</nobr>| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) UVマッピング</nobr>| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>アンカー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) トップレイヤー</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>トップアンカー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) アンカーボーン</nobr>| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>アンカーポジション</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>アンカー回転</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ボトムレイヤー</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>ボトムアンカー</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) アンカーボーン</nobr>| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) スワップサイド</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>アンカーポジション</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>アンカー回転</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子特性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粘着性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 曲げ制約を有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 曲げ適合性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 自己衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ質量</nobr>| [2] (0 ~ 4) | グリップ粒子の質量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ摩擦</nobr>| [2] (-2 ~ 4) | グリップ粒子の摩擦
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ粘着性</nobr>| [0.25] (0 ~ 1) | グリップ粒子の粘着性
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ抗力</nobr>| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップスケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 引き裂きを有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 引き裂き閾値</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 引き裂き速度の制限</nobr>| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **(Top)** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>C1 マテリアル</b></nobr>| | 
|<nobr>├&nbsp;![texture icon](/images/icon/ic_texture.png) <b>表面</b></nobr>|| 
|<nobr>├&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) ガラスモード</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) アルファをグロスとして</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) ダブルサイド</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 薄暗いバック</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) シャドウをキャスト</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) デプスプリパス</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) グロス</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) バンプ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) グロー</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アンビエント</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アルファ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) クリップ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>色</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ブレンドモード</nobr>| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ブレンド</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>トゥーンシェーダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シェーディング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アウトライン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スペキュラー</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトスペキュラー</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ハイライトエリア</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトハイライト</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンビエント</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シャドウエリア</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シャドウ</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトシャドウ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>特別シェーダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) モード</nobr>| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 屈折</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 厚さ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) テクスチャ</nobr>| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>ディテールマップ</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) サイズ</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) バンプ</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ノイズ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) (Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトエッジ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) マップ選択</nobr>| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップの回転</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップのスケール</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップのバンプ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) AOに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スムーズさに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 金属に影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カラーブレンドに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 異方性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) MIPマップバイアス</nobr>| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>布 2</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; メッシュ再構築</nobr>|| ここでのほとんどのパラメータは、効果を得るためにメッシュを再構築する必要があります。
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) トポロジー</nobr>| **水平レイアウト** | 適応六角形, 適応長方形, 水平レイアウト, 水平ストリング, 垂直レイアウト, 垂直ストリング,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) ストリング接続</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) インナー半径</nobr>| [0.08] (0 ~ 0.2) | 内円の半径（メートル）
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 傾斜</nobr>| [45] (0 ~ 90) | 長さに沿ってメッシュを拡張する角度。0 = チューブ、90 = 平らな円。
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アーク</nobr>| [0] (-1 ~ 1) | 長さに沿って外向きまたは内向きのアーク。正 = バルーン形、負 = ベル形
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 長さ</nobr>| [0.25] (0 ~ 0.75) | 長さ（メートル）
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アームホール</nobr>| [0.5] (0 ~ 1) | 周囲に対するアームホールのサイズ
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 全長に対するアームホールの高さ
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) バック長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) サイド長さ</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 垂直解像度</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 距離制約への適合性</nobr>| [0] (0 ~ 0.1) | 粒子間の距離制約に対する適合性
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) UVマッピング</nobr>| **ミラー拡大** | 円形, ミラー拡大, ミラー実際, ラップ拡大, ラップ実際,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>アンカー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) トップレイヤー</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>トップアンカー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) アンカーボーン</nobr>| **トルソ** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>アンカーポジション</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>アンカー回転</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ボトムレイヤー</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>ボトムアンカー</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンカー選択</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 選択オフセット</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) アンカーボーン</nobr>| **ウエスト** | ウエスト, トルソ, ヒップ, 頭, 太もも, 脛, 上腕, 下腕, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) スワップサイド</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ロックモード</nobr>| **なし** | なし, ロック, ロック高さ, スティッキー,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>アンカーポジション</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>アンカー回転</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子特性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粘着性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 曲げ制約を有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 曲げ適合性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 自己衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ質量</nobr>| [2] (0 ~ 4) | グリップ粒子の質量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ摩擦</nobr>| [2] (-2 ~ 4) | グリップ粒子の摩擦
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ粘着性</nobr>| [0.25] (0 ~ 1) | グリップ粒子の粘着性
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップ抗力</nobr>| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グリップスケール</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 引き裂きを有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 引き裂き閾値</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 引き裂き速度の制限</nobr>| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **スカート** | スカート, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>C2 マテリアル</b></nobr>| | 
|<nobr>├&nbsp;![texture icon](/images/icon/ic_texture.png) <b>表面</b></nobr>|| 
|<nobr>├&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **マットグレー** | オリジナル, マットグレー, 半透明, グロー, シルバー, ソリッドグラス, 薄いガラス, アウトライン, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) ガラスモード</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) アルファをグロスとして</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) ダブルサイド</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 薄暗いバック</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) シャドウをキャスト</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) デプスプリパス</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) グロス</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) バンプ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) グロー</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アンビエント</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) アルファ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) クリップ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>色</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) ブレンドモード</nobr>| **(Multiply)** | オリジナル, (Multiply), ブレンド, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ブレンド</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **(Gray)** | オリジナル, 白, 黒, 赤, (Yellow), (Dark Gray), 青, 肌, (Gray), (Orange),  |
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>トゥーンシェーダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シェーディング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アウトライン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スペキュラー</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトスペキュラー</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ハイライトエリア</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトハイライト</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) アンビエント</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シャドウエリア</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) シャドウ</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトシャドウ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **シャープ** | シャープ, ソフト, 明るい, フラット + スペキュラー, フラット,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>特別シェーダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) モード</nobr>| **オフ** | オフ, 屈折厚, 屈折薄, アウトライン, 未点灯, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 屈折</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 厚さ</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) テクスチャ</nobr>| **[ソリッドカラー]** | [ソリッドカラー], [ウッド1], [ウッド2], [タイル], [コンクリート], [ビデオ],  |
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>ディテールマップ</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) サイズ</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) バンプ</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ノイズ</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) (Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) ソフトエッジ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) マップ選択</nobr>| **ファブリック 3** | カーボンファイバー, レザー, ファブリック 1, ファブリック 2, ファブリック 3, ウール 1, ウール 2, メタルサテン, メタルブラシ, 髪,  |
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップの回転</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップのスケール</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ディテールマップのバンプ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) AOに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スムーズさに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 金属に影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カラーブレンドに影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 異方性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) MIPマップバイアス</nobr>| [0] (-5 ~ 5) | ディテールテクスチャのシャープネスを調整
|<nobr>![check_off icon](/images/icon/ic_check_off.png) 結合</nobr>| [OFF] | 布 1 と 2 を単一のシミュレーションとして結合します。これにより、2つの間での衝突が可能になりますが、速度は遅くなります。
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>流体（実験的）</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>スポーン</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>位置</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>回転</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スポーン半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拡散</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スポーンレート</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スピード</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) マウス / 手の操作</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) オートエイム</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大TTL</nobr>| [10] (5 ~ 15) | この時間が経過した後にパーティクルは消失し、再出現します。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 床のTTL</nobr>| [0.1] (0 ~ 1) | 床に当たった後の生存時間。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) スムージング</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **スプリンクラー** | シャワー, 噴水, スプリンクラー, ハンドヘルド,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>流体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) コヒージョン</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粘度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面に付着</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ターゲット密度</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) コヒージョン範囲</nobr>| [20] (1 ~ 50) | コヒージョン効果の最大距離
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) ターゲット距離</nobr>| [10] (1 ~ 20) | コヒージョンがオフのときのパーティクル間の最小距離（mm）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 標高</nobr>| [0.25] (0 ~ 0.5) | サイズに比例してパーティクルを持ち上げる
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **水** | 水, 粘着性, 砂,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>レンダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) パーティクルをレンダリング</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 水滴をレンダリング</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水滴サイズ</nobr>| [2] (0 ~ 50) | 水滴サイズ（mm）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 密度によるスケール</nobr>| [0] (0 ~ 5) | 流体の密度で水滴サイズをスケールする
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>色</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) カラーモード</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 彩度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 明度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 赤</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 緑</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 青</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 金属的</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 滑らかさ</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) グロー</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子特性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 空気の抗力</nobr>| [-2] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水中の抗力</nobr>| [-2] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) プレイヤー</nobr>| [OFF] | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>ジオメトリコライダー</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 表示</nobr>| [OFF] | 
|<nobr>├&nbsp; エクスポート形状</nobr>|| 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>頭</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>首</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>胸</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>肋骨</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>ウエスト</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>腹部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>臀部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>肩</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>上腕</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>前腕</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>手</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>ヒップ</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>太もも</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>すね</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>中間位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中間半径</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中間曲線</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>足</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>開始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 開始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) カーブ</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>終了位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 終了半径</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>スケール</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>メッシュコライダー</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) ジオメトリコライダーを無効にする</nobr>| [ON] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可視化</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Skip Edge)</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Skip Point)</nobr>| [ON] | 
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Single Collision)</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>シミュレーション設定</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) ドラッグを有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) スケールをリセット</nobr>| [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) シミュレート</nobr>| [ON] | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 二段階解法</nobr>| [OFF] | 
|<nobr>![list icon](/images/icon/ic_list.png) プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
