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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> パーティクルダイナミクスを使用| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| ├─ □ 偶数サブステップを逆転| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| └─ □ 二段階解法| [OFF] | 
|  <b>プライマリーグループ</b>|| 
|  ボーンを選択|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| ├─ □ 可視化| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| ├─ □ 可視化| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| ├─ □ 可視化| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| ├─ □ ロックY| [OFF] | 
| └─ □ ロックZ| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 追加グループ| [0] (0 ~ 7) | 
|  □ <b>(Group 2)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 3)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 4)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 5)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 6)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 7)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
|  □ <b>(Group 8)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
