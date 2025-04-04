---
locale: ja-rJP
layout: single
title: スカートフィジックス
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/physics_skirt) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_skirt) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_skirt) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_skirt) | [简中](/zh/dancexr/menu/2025.4/actor/physics_skirt)

[物理](../menu#物理) > スカートフィジックス



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  パーティクルダイナミクスを使用</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>シミュレーション設定</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  ドラッグを有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  シミュレート</nobr>| [ON] | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  二段階解法</nobr>| [OFF] | 
|<nobr> <b>プライマリーグループ</b></nobr>|| 
|<nobr> ボーンを選択</nobr>|| 
|<nobr> ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr> ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr> ![slider icon](/images/icon/ic_slider.png)  追加グループ</nobr>| [0] (0 ~ 7) | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr> ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
