---
locale: ja-rJP
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/model_physics) | [简中](/zh/dancexr/menu/2025.4/stage/model_physics)

[ステージ](../menu#ステージ) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
|  □ PMX物理を無効にする| [OFF] | XPSツールを使用するためにPMX物理を無効にする
|  ☑ 制約の軽減| [ON] | 滑らかなシミュレーションを可能にするために制約を減らす実験的設定を使用
|  ⚙️ **衝突**| | 
| ├─ ☑ 静的包括| [ON] | 
| ├─ ☑ 静的排他的| [ON] | 
| ├─ ☑ 動的包括| [ON] | 
| └─ ☑ 動的排他的| [ON] | 
|  ⚙️ **線形運動**| | Settings for linear movements
| ├─ ☑ 制約| 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├─ ☑ 0制限をロック| [ON] | 
| ├─ ⊖ 最小スプリング力| [5] (0 ~ 15) | 
| ├─ ⊖ 最大制限| [0.05] (0.05 ~ 0.1) | 
| ├─ ⊖ 弾力性| [0.5] (0 ~ 1) | 
| ├─ ⊖ 接触距離| [0.5] (0 ~ 1) | 
| ├─ ⊖ ダンピング| [0.05] (0 ~ 1) | 
| └─ ⊖ ドラッグ| [0.15] (0 ~ 1) | 
|  ⚙️ **角運動**| | Settings for angular movements
| ├─ ☑ 制約| 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├─ ☑ 0制限をロック| [ON] | 
| ├─ ⊖ 最小スプリング力| [5] (0 ~ 15) | 
| ├─ ⊖ 最大制限| [90] (3 ~ 90) | 
| ├─ ⊖ 弾力性| [0.5] (0 ~ 1) | 
| ├─ ⊖ 接触距離| [0.5] (0 ~ 1) | 
| ├─ ⊖ ダンピング| [0.05] (0 ~ 1) | 
| └─ ⊖ ドラッグ| [0.15] (0 ~ 1) | 
|  ☑ **線形ドライブ**| | Apply linear drive
| ├─ ☑ 有効にする| [ON] | 
| ├─ ⊖ スプリングフォース| [3] (0 ~ 5) | 
| └─ ⊖ ダンピング| [0.1] (0 ~ 1) | 
|  ☑ **角ドライブ**| | Apply angular drive
| ├─ ☑ 有効にする| [ON] | 
| ├─ ⊖ スプリングフォース| [0.1] (0 ~ 5) | 
| └─ ⊖ ダンピング| [0.1] (0 ~ 1) | 
|  ⚙️ **線形モーション**| | Settings for linear motion
| ├─ ⊖ 堅固さ| [0] (-1 ~ 1) | 
| ├─ ⊖ メイン駆動力| [5] (0 ~ 8) | 
| ├─ ⊖ セカンド駆動力| [3] (0 ~ 8) | 
| ├─ ☑ ターゲット位置| ゼロ | ゼロ, センター, 最小, 最大, 
| ├─ ☑ 可能な限りロック| [ON] | 
| ├─ ☑ 加速モード| [ON] | 
| ├─ ⊖ ダンピング| [0.05] (0 ~ 1) | 
| ├─ ⊖ ドラッグ| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | ジョイント制限を無視することで制約をさらに減少
|  ⚙️ **角モーション**| | Settings for angular motion
| ├─ ⊖ 堅固さ| [0] (-1 ~ 1) | 
| ├─ ⊖ メイン駆動力| [5] (0 ~ 8) | 
| ├─ ⊖ セカンド駆動力| [5] (0 ~ 8) | 
| ├─ ☑ ターゲット位置| ゼロ | ゼロ, センター, 最小, 最大, 
| ├─ □ 可能な限りロック| [OFF] | 
| ├─ ☑ 加速モード| [ON] | 
| ├─ ⊖ ダンピング| [0.05] (0 ~ 1) | 
| ├─ ⊖ ドラッグ| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | ジョイント制限を無視することで制約をさらに減少
|  ⚙️ **オプション**| | 
| ├─ ⊖ 最小ドラッグ| [0] (0 ~ 1) | 自動モードにおける最小ドラッグ値
| ├─ ⊖ ドラッグスケール| [1] (0 ~ 5) | 自動モードにおいてドラッグ値に適用されるスケール
| ├─ ⊖ 最小質量| [0] (0 ~ 1) | 自動モードにおける最小質量値
| ├─ ⊖ 質量スケール| [1] (0 ~ 10) | 自動モードにおいて質量値に適用されるスケール
| ├─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─ ⊖ 投影距離| [0.05] (0 ~ 0.1) | 無中立に対する物体間の距離がこの値を超えたときにジョイントをリセットする力
| └─ ⊖ 投影角度| [5] (0 ~ 60) | 無中立に対する物体間の角度がこの値を超えたときにジョイントをリセットする力
|  ⊖ 自動リセット閾値| [35] (0 ~ 100) | 速度がこの値を超えたときにボーンとその子を自動的にリセットする
|  ⚙️ **自動リセット**| | 
| └─ ⊖ しきい値| [30] (0 ~ 50) | 
|  ☑ **ボディコライダー**| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ⊖ サイズ| [0.5] (0 ~ 1) | 
| ├─ ⊖ 頭部半径| [1] (0 ~ 2) | 
| ├─ ⊖ 腕の半径| [1] (0 ~ 2) | 
| ├─ ⊖ 前腕| [1] (0 ~ 2) | 
| ├─ ⊖ 胸の幅| [1] (0 ~ 2) | 
| ├─ ⊖ ウエストの幅| [0.5] (0 ~ 1) | 
| ├─ ⊖ ヒップの幅| [0] (-1 ~ 1) | 
| ├─ ⊖ お尻の半径| [1] (0 ~ 2) | 
| ├─ **お尻の位置**|| 
| ├─ ⊖ (X)| [0] (-0.1 ~ 0.1) | 
| ├─ ⊖ (Y)| [0] (-0.1 ~ 0.1) | 
| ├─ ⊖ (Z)| [0] (-0.1 ~ 0.1) | 
| ├─ ⊖ お腹の半径| [1] (0 ~ 2) | 
| ├─ ⊖ お腹の位置| [0] (-1 ~ 1) | 
| ├─ ⊖ 脚の半径| [1] (0 ~ 2) | 
| ├─ ⊖ 太ももの前後| [0] (-1 ~ 1) | 
| ├─ ⊖ 太ももの開始位置| [0] (0 ~ 1) | 
| ├─ ⊖ 手| [0] (0 ~ 1) | 
| ├─ □ 可視化| [OFF] | 
| └─ ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (amy), (misaki),  |
|  ☑ **胸部物理**<sup>[PRO]</sup>| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ボーンを選択|| 
| ├─ ⊖ スプリングフォース| [1.5] (0 ~ 5) | 
| ├─ ⊖ ダンピング| [0.1] (0 ~ 1) | 
| ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| ├─ ⊖ ドラッグ| [0.1] (0 ~ 10) | 
| ├─ ⊖ 重力カウンター| [10] (0 ~ 45) | 
| ├─ ⚙️ **回転制限**| | 
| │ ├─ ⊖ 上限| [100] (0 ~ 120) | 
| │ ├─ ⊖ 下限| [15] (0 ~ 45) | 
| │ ├─ ⊖ 左 / 右制限| [15] (0 ~ 45) | 
| │ ├─ ⊖ スプリングフォース| [1.25] (0 ~ 10) | 制限を超えたときのスプリング力
| │ ├─ ⊖ ダンピング| [1] (0 ~ 1) | 
| │ ├─ ⊖ 接触距離| [0.5] (0 ~ 1) | 
| │ └─ ⊖ バウンス| [0.2] (0 ~ 1) | 
| ├─ ⚙️ **アンカー**| | 
| │ ├─ ⊖ (X)| [-0.03] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ (Y)| [0.03] (-0.2 ~ 0.2) | 
| │ └─ ⊖ (Z)| [0.08] (-0.2 ~ 0.2) | 
| ├─ ⚙️ **センター**| | 
| │ ├─ ⊖ (X)| [0.02] (-0.2 ~ 0.2) | 
| │ ├─ ⊖ (Y)| [-0.05] (-0.2 ~ 0.2) | 
| │ └─ ⊖ (Z)| [0.025] (-0.2 ~ 0.2) | 
| ├─ ⚙️ **衝突**| | 
| │ ├─ □ 腕との衝突| [OFF] | 
| │ ├─ ⊖ コライダー半径| [0.07] (0 ~ 0.1) | 
| │ ├─ ⊖ コライダーの長さ| [0.65] (0 ~ 1) | 
| │ ├─ ⊖ コライダー曲線| [2] (-2 ~ 2) | 布シミュレーションと連動します。
| │ ├─ □ 可視化| [OFF] | 
| │ ├─ ☑ 乳首を有効にする| [ON] | 布シミュレーションと連動します。
| │ ├─ ⚙️ **乳首の位置**| | 
| │ │ ├─ ⊖ (X)| [-0.18] (-1 ~ 1) | 
| │ │ ├─ ⊖ (Y)| [0.09] (-1 ~ 1) | 
| │ │ └─ ⊖ (Z)| [0.2] (0 ~ 1) | 
| │ └─ ⊖ 乳首のサイズ| [0.1] (0 ~ 1) | 
| ├─ ☑ **(Softbody)**| | 
| │ ├─ ☑ 有効にする| [ON] | 
| │ ├─ **ジョイント**|| 
| │ ├─ ⊖ 深度| [0.4] (0 ~ 1) | 
| │ ├─ ☑ 中心を含める| [ON] | 
| │ ├─ ☑ 体積制約| [0.85] (0.5 ~ 1) | 
| │ ├─ ⊖ 内部制約| [0.65] (0.5 ~ 1) | 
| │ ├─ ⊖ 表面制約| [0.75] (0.5 ~ 1) | 
| │ ├─ ⊖ 回転制約| [0.65] (0.5 ~ 1) | 
| │ ├─ ☑ エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| │ ├─ ⊖ 中心ロック| [1] (0.5 ~ 1) | 
| │ ├─ ⊖ ダンピング| [15] (0 ~ 40) | 
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
| │ │ ├─ ⊖ 風の影響| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ ├─ ⚙️ **衝突する**| | 
| │ │ ├─ ☑ 頭| [ON] | 
| │ │ ├─ □ 体| [OFF] | 
| │ │ ├─ □ 胸部| [OFF] | 
| │ │ ├─ □ 臀部| [OFF] | 
| │ │ ├─ ☑ (Arms)| [ON] | 
| │ │ ├─ ☑ 手| [ON] | 
| │ │ ├─ □ 脚| [OFF] | 
| │ │ ├─ ☑ 足| [ON] | 
| │ │ └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **シミュレーション設定**| | 
| │ │ ├─ ☑ グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │ │ ├─ ☑ ドラッグを有効にする| [ON] | 
| │ │ ├─ ☑ シミュレート| [ON] | 
| │ │ ├─ > シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │ │ ├─ ⊖ 時間スケール| [0.65] (0.1 ~ 1) | 
| │ │ ├─ ⊖ サブステップ| [4] (1 ~ 20) | 
| │ │ ├─ ⊖ イテレーション| [1] (0 ~ 10) | 
| │ │ ├─ □ 偶数サブステップを逆転| [OFF] | 
| │ │ ├─ ⊖ 代替グループサイズ| [0] (0 ~ 20) | 
| │ │ ├─ ⊖ テーブルサイズ| [6] (1 ~ 20) | 
| │ │ └─ □ 二段階解法| [OFF] | 
| │ └─ ≡ プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| ├─ □ ソフトボディのみ| [OFF] | 物理ジョイントを無効にし、ソフトボディパーティクルのみを使用します。
| └─ ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|  ☑ **スカートフィジックス**<sup>[PRO]</sup>| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ☑ パーティクルダイナミクスを使用| [ON] | 
| ├─ ⚙️ **シミュレーション設定**| | 
| │ ├─ ☑ グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │ ├─ ☑ ドラッグを有効にする| [ON] | 
| │ ├─ ☑ シミュレート| [ON] | 
| │ ├─ > シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │ ├─ ⊖ 時間スケール| [0.65] (0.1 ~ 1) | 
| │ ├─ ⊖ サブステップ| [4] (1 ~ 20) | 
| │ ├─ ⊖ イテレーション| [1] (0 ~ 10) | 
| │ ├─ □ 偶数サブステップを逆転| [OFF] | 
| │ ├─ ⊖ 代替グループサイズ| [0] (0 ~ 20) | 
| │ ├─ ⊖ テーブルサイズ| [6] (1 ~ 20) | 
| │ └─ □ 二段階解法| [OFF] | 
| ├─ **プライマリーグループ**|| 
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
| ├─ ⊖ 追加グループ| [0] (0 ~ 7) | 
| ├─ □ **(Group 2)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 3)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 4)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 5)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 6)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 7)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| ├─ □ **(Group 8)**| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─ > ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─ ☑ クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─ ⚙️ **パーティクルダイナミクス**| | 
| │ │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─ ⊖ ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─ ⊖ ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─ ⊖ 慣性| [2] (1 ~ 5) | 
| │ │ ├─ ⊖ ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─ ⊖ 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─ ⊖ 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─ ⊖ 摩擦| [1] (0 ~ 2) | 
| │ │ ├─ ⊖ 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─ ⊖ 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─ ⊖ 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─ ⊖ 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─ ⚙️ **風**| | 
| │ │ │ ├─ ⊖ 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─ ⊖ 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─ ⊖ 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─ ⊖ 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─ ⚙️ **衝突する**| | 
| │ │  ├─ ☑ 頭| [ON] | 
| │ │  ├─ ☑ 体| [ON] | 
| │ │  ├─ ☑ 胸部| [ON] | 
| │ │  ├─ ☑ 臀部| [ON] | 
| │ │  ├─ ☑ (Arms)| [ON] | 
| │ │  ├─ ☑ 手| [ON] | 
| │ │  ├─ ☑ 脚| [ON] | 
| │ │  ├─ ☑ 足| [ON] | 
| │ │  └─ ☑ プレイヤー| [ON] | 
| │ ├─ ⚙️ **物理プロパティ**| | Physics properties like mass, drag and friction
| │ │ ├─ ⊖ 質量| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─ ⊖ 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─ ⊖ 摩擦| [0] (0 ~ 1) | 
| │ │ ├─ ⊖ ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─ ⚙️ **親子ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─ ⚙️ **横ジョイント**| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─ ⊖ 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─ ⊖ 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─ ⊖ ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─ ⊖ 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─ ⚙️ **コライダー**| | 
| │ │ ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─ > コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─ ⊖ コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─ ⊖ (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─ ☑ プライマリーグループ設定を使用| [ON] | 
| └─ ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|  ☑ **ヘア物理**| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ☑ **パーティクルダイナミクス**| | 
| │ ├─ ☑ 有効にする| [ON] | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
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
| │ ├─ ⚙️ **衝突する**| | 
| │ │ ├─ ☑ 頭| [ON] | 
| │ │ ├─ ☑ 体| [ON] | 
| │ │ ├─ ☑ 胸部| [ON] | 
| │ │ ├─ ☑ 臀部| [ON] | 
| │ │ ├─ ☑ (Arms)| [ON] | 
| │ │ ├─ ☑ 手| [ON] | 
| │ │ ├─ ☑ 脚| [ON] | 
| │ │ ├─ ☑ 足| [ON] | 
| │ │ └─ ☑ プレイヤー| [ON] | 
| │ └─ ⚙️ **シミュレーション設定**| | 
| │  ├─ ☑ グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │  ├─ ☑ ドラッグを有効にする| [ON] | 
| │  ├─ ☑ シミュレート| [ON] | 
| │  ├─ > シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │  ├─ ⊖ 時間スケール| [0.65] (0.1 ~ 1) | 
| │  ├─ ⊖ サブステップ| [4] (1 ~ 20) | 
| │  ├─ ⊖ イテレーション| [1] (0 ~ 10) | 
| │  ├─ □ 偶数サブステップを逆転| [OFF] | 
| │  ├─ ⊖ 代替グループサイズ| [0] (0 ~ 20) | 
| │  ├─ ⊖ テーブルサイズ| [6] (1 ~ 20) | 
| │  └─ □ 二段階解法| [OFF] | 
| ├─ ⊖ スプリング| [1.25] (0 ~ 5) | 
| ├─ ⊖ ダンプ| [0.01] (0 ~ 0.1) | 
| ├─ ⊖ 減少比率| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├─ ⊖ ツイストリミット| [5] (0 ~ 180) | ツイスト回転の制限
| ├─ ⊖ リミットフォース| [3] (0 ~ 8) | 
| ├─ ⊖ 質量| [0.01] (0 ~ 0.1) | 
| ├─ ⊖ ドラッグ| [1] (0 ~ 10) | 
| ├─ ⊖ コライダー半径| [0.005] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├─ ⊖ コライダーの長さ| [0.9] (0 ~ 1) | 
| ├─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └─ ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (momiji bob), (Preset 1),  |
|  ☑ **ぶら下がり物理**| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ ⊖ 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─ ☑ **パーティクルダイナミクス**| | 
| │ ├─ ☑ 有効にする| [ON] | 
| │ ├─ ⊖ スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─ ⊖ パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─ ⊖ 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
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
| │ ├─ ⚙️ **衝突する**| | 
| │ │ ├─ ☑ 頭| [ON] | 
| │ │ ├─ ☑ 体| [ON] | 
| │ │ ├─ ☑ 胸部| [ON] | 
| │ │ ├─ ☑ 臀部| [ON] | 
| │ │ ├─ ☑ (Arms)| [ON] | 
| │ │ ├─ ☑ 手| [ON] | 
| │ │ ├─ ☑ 脚| [ON] | 
| │ │ ├─ ☑ 足| [ON] | 
| │ │ └─ ☑ プレイヤー| [ON] | 
| │ └─ ⚙️ **シミュレーション設定**| | 
| │  ├─ ☑ グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │  ├─ ☑ ドラッグを有効にする| [ON] | 
| │  ├─ ☑ シミュレート| [ON] | 
| │  ├─ > シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │  ├─ ⊖ 時間スケール| [0.65] (0.1 ~ 1) | 
| │  ├─ ⊖ サブステップ| [4] (1 ~ 20) | 
| │  ├─ ⊖ イテレーション| [1] (0 ~ 10) | 
| │  ├─ □ 偶数サブステップを逆転| [OFF] | 
| │  ├─ ⊖ 代替グループサイズ| [0] (0 ~ 20) | 
| │  ├─ ⊖ テーブルサイズ| [6] (1 ~ 20) | 
| │  └─ □ 二段階解法| [OFF] | 
| ├─ ⊖ スプリング| [0.5] (0 ~ 5) | 
| ├─ ⊖ ダンプ| [0.01] (0 ~ 0.1) | 
| ├─ ⊖ 減少比率| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├─ ⊖ ツイストリミット| [5] (0 ~ 180) | ツイスト回転の制限
| ├─ ⊖ リミットフォース| [3] (0 ~ 8) | 
| ├─ ⊖ 質量| [0.05] (0 ~ 0.1) | 
| ├─ ⊖ ドラッグ| [1] (0 ~ 10) | 
| ├─ ⊖ コライダー半径| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├─ ⊖ コライダーの長さ| [0.9] (0 ~ 1) | 
| ├─ ⊖ アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └─ ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
|  ☑ **オブジェクトを切り離す**| | 
| ├─ ☑ 有効にする| [ON] | 
| ├─ ボーンを選択|| 
| ├─ ☑ 重力| [ON] | 
| ├─ ⊖ 質量| [0.1] (0 ~ 10) | 
| ├─ ⊖ ダンプ| [0] (0 ~ 1) | 
| ├─ ☑ コライダー| 球体 | なし, 球体, カプセル, 
| ├─ ⊖ コライダー半径| [0.1] (0 ~ 1) | 
| └─ ⊖ コライダーの長さ| [0.3] (0 ~ 2) | 
|  ≡ プリセット| **デフォルト（リセット）** | デフォルト（リセット）,  |
