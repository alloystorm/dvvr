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
|  ☑ 有効にする| [ON] | 
|  ☑ パーティクルダイナミクスを使用| [ON] | 
|  ⚙️ **シミュレーション設定**| | 
| ├─ ☑ グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| ├─ ☑ ドラッグを有効にする| [ON] | 
| ├─ ☑ シミュレート| [ON] | 
| ├─ > シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─ ⊖ 時間スケール| [0.65] (0.1 ~ 1) | 
| ├─ ⊖ サブステップ| [4] (1 ~ 20) | 
| ├─ ⊖ イテレーション| [1] (0 ~ 10) | 
| ├─ □ 偶数サブステップを逆転| [OFF] | 
| ├─ ⊖ 代替グループサイズ| [0] (0 ~ 20) | 
| ├─ ⊖ テーブルサイズ| [6] (1 ~ 20) | 
| └─ □ 二段階解法| [OFF] | 
|  **プライマリーグループ**|| 
|  ボーンを選択|| 
|  > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|  ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
|  ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|  ⚙️ **パーティクルダイナミクス**| | 
| ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| ├─ □ 可視化| [OFF] | 
| ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| ├─ ⚙️ **風**| | 
| │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| └─ ⚙️ **衝突する**| | 
|  ├─ ☑ 頭| [ON] | 
|  ├─ ☑ 体| [ON] | 
|  ├─ ☑ 胸部| [ON] | 
|  ├─ ☑ 臀部| [ON] | 
|  ├─ ☑ (Arms)| [ON] | 
|  ├─ ☑ 手| [ON] | 
|  ├─ ☑ 脚| [ON] | 
|  ├─ ☑ 足| [ON] | 
|  └─ ☑ プレイヤー| [ON] | 
|  ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|  ⚙️ **親子ジョイント**| | 
| ├─ □ 可視化| [OFF] | 
| ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|  ⚙️ **横ジョイント**| | 
| ├─ □ 可視化| [OFF] | 
| ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| ├─ □ ロックY| [OFF] | 
| └─ □ ロックZ| [OFF] | 
|  ⚙️ **コライダー**| | 
| ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|  ⊖ 追加グループ| [0] (0 ~ 7) | 
|  □ **(Group 2)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 3)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 4)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 5)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 6)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 7)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  □ **(Group 8)**| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─ ⚙️ **風**| | 
| │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─ ⚙️ **衝突する**| | 
| │  ├─ ☑ 頭| [ON] | 
| │  ├─ ☑ 体| [ON] | 
| │  ├─ ☑ 胸部| [ON] | 
| │  ├─ ☑ 臀部| [ON] | 
| │  ├─ ☑ (Arms)| [ON] | 
| │  ├─ ☑ 手| [ON] | 
| │  ├─ ☑ 脚| [ON] | 
| │  ├─ ☑ 足| [ON] | 
| │  └─ ☑ プレイヤー| [ON] | 
| ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⚙️ **親子ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─ ⚙️ **横ジョイント**| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─ ⚙️ **コライダー**| | 
| │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─ ☑ プライマリーグループ設定を使用| [ON] | 
|  ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
