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
|<nobr>有効にする</nobr>| [ON] | 
|<nobr>パーティクルダイナミクスを使用</nobr>| [ON] | 
|<nobr><b>シミュレーション設定</b></nobr>| | 
|<nobr>├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr><b>プライマリーグループ</b></nobr>|| 
|<nobr>ボーンを選択</nobr>|| 
|<nobr>ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr><b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr><b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr><b>親子ジョイント</b></nobr>| | 
|<nobr>├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr><b>横ジョイント</b></nobr>| | 
|<nobr>├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr><b>コライダー</b></nobr>| | 
|<nobr>├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>追加グループ</nobr>| [0] (0 ~ 7) | 
|<nobr><b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr><b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;<b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;<b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;<b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
