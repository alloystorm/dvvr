---
locale: ja-rJP
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[(Prop)](../menu#(Prop)) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
| PMX物理を無効にする | OFF | XPSツールを使用するためにPMX物理を無効にする
| 制約の軽減 | ON | 滑らかなシミュレーションを可能にするために制約を減らす実験的設定を使用
| **衝突** | | 
| ├&nbsp;静的包括 | ON | 
| ├&nbsp;静的排他的 | ON | 
| ├&nbsp;動的包括 | ON | 
| └&nbsp;動的排他的 | ON | 
| **線形運動** | | Settings for linear movements
| ├&nbsp;制約 | 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├&nbsp;0制限をロック | ON | 
| ├&nbsp;最小スプリング力 | [5] (0 ~ 15) | 
| ├&nbsp;最大制限 | [0.05] (0.05 ~ 0.1) | 
| ├&nbsp;弾力性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接触距離 | [0.5] (0 ~ 1) | 
| ├&nbsp;ダンピング | [0.05] (0 ~ 1) | 
| └&nbsp;ドラッグ | [0.15] (0 ~ 1) | 
| **角運動** | | Settings for angular movements
| ├&nbsp;制約 | 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├&nbsp;0制限をロック | ON | 
| ├&nbsp;最小スプリング力 | [5] (0 ~ 15) | 
| ├&nbsp;最大制限 | [90] (3 ~ 90) | 
| ├&nbsp;弾力性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接触距離 | [0.5] (0 ~ 1) | 
| ├&nbsp;ダンピング | [0.05] (0 ~ 1) | 
| └&nbsp;ドラッグ | [0.15] (0 ~ 1) | 
| **線形ドライブ** | | Apply linear drive
| ├&nbsp;有効にする | ON | 
| ├&nbsp;スプリングフォース | [3] (0 ~ 5) | 
| └&nbsp;ダンピング | [0.1] (0 ~ 1) | 
| **角ドライブ** | | Apply angular drive
| ├&nbsp;有効にする | ON | 
| ├&nbsp;スプリングフォース | [0.1] (0 ~ 5) | 
| └&nbsp;ダンピング | [0.1] (0 ~ 1) | 
| **線形モーション** | | Settings for linear motion
| ├&nbsp;堅固さ | [0] (-1 ~ 1) | 
| ├&nbsp;メイン駆動力 | [5] (0 ~ 8) | 
| ├&nbsp;セカンド駆動力 | [3] (0 ~ 8) | 
| ├&nbsp;ターゲット位置 | ゼロ | ゼロ, センター, 最小, 最大, 
| ├&nbsp;可能な限りロック | ON | 
| ├&nbsp;加速モード | ON | 
| ├&nbsp;ダンピング | [0.05] (0 ~ 1) | 
| ├&nbsp;ドラッグ | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | ジョイント制限を無視することで制約をさらに減少
| **角モーション** | | Settings for angular motion
| ├&nbsp;堅固さ | [0] (-1 ~ 1) | 
| ├&nbsp;メイン駆動力 | [5] (0 ~ 8) | 
| ├&nbsp;セカンド駆動力 | [5] (0 ~ 8) | 
| ├&nbsp;ターゲット位置 | ゼロ | ゼロ, センター, 最小, 最大, 
| ├&nbsp;可能な限りロック | OFF | 
| ├&nbsp;加速モード | ON | 
| ├&nbsp;ダンピング | [0.05] (0 ~ 1) | 
| ├&nbsp;ドラッグ | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | ジョイント制限を無視することで制約をさらに減少
| **オプション** | | 
| ├&nbsp;最小ドラッグ | [0] (0 ~ 1) | 自動モードにおける最小ドラッグ値
| ├&nbsp;ドラッグスケール | [1] (0 ~ 5) | 自動モードにおいてドラッグ値に適用されるスケール
| ├&nbsp;最小質量 | [0] (0 ~ 1) | 自動モードにおける最小質量値
| ├&nbsp;質量スケール | [1] (0 ~ 10) | 自動モードにおいて質量値に適用されるスケール
| ├&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├&nbsp;投影距離 | [0.05] (0 ~ 0.1) | 無中立に対する物体間の距離がこの値を超えたときにジョイントをリセットする力
| └&nbsp;投影角度 | [5] (0 ~ 60) | 無中立に対する物体間の角度がこの値を超えたときにジョイントをリセットする力
| 自動リセット閾値 | [35] (0 ~ 100) | 速度がこの値を超えたときにボーンとその子を自動的にリセットする
| **自動リセット** | | 
| └&nbsp;しきい値 | [30] (0 ~ 50) | 
| **ボディコライダー** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;サイズ | [0.5] (0 ~ 1) | 
| ├&nbsp;頭部半径 | [1] (0 ~ 2) | 
| ├&nbsp;腕の半径 | [1] (0 ~ 2) | 
| ├&nbsp;前腕 | [1] (0 ~ 2) | 
| ├&nbsp;胸の幅 | [1] (0 ~ 2) | 
| ├&nbsp;ウエストの幅 | [0.5] (0 ~ 1) | 
| ├&nbsp;ヒップの幅 | [0] (-1 ~ 1) | 
| ├&nbsp;お尻の半径 | [1] (0 ~ 2) | 
| ├&nbsp;お尻の位置 || 
| ├&nbsp;(X) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Y) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Z) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;お腹の半径 | [1] (0 ~ 2) | 
| ├&nbsp;お腹の位置 | [0] (-1 ~ 1) | 
| ├&nbsp;脚の半径 | [1] (0 ~ 2) | 
| ├&nbsp;太ももの前後 | [0] (-1 ~ 1) | 
| ├&nbsp;太ももの開始位置 | [0] (0 ~ 1) | 
| ├&nbsp;手 | [0] (0 ~ 1) | 
| ├&nbsp;可視化 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (amy), (misaki),  |
| **胸部物理**<sup>[PRO]</sup> | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;ボーンを選択 || 
| ├&nbsp;スプリングフォース | [1.5] (0 ~ 5) | 
| ├&nbsp;ダンピング | [0.1] (0 ~ 1) | 
| ├&nbsp;質量 | [0.1] (0 ~ 1) | 
| ├&nbsp;ドラッグ | [0.1] (0 ~ 10) | 
| ├&nbsp;重力カウンター | [10] (0 ~ 45) | 
| ├&nbsp;**回転制限** | | 
| │&nbsp;├&nbsp;上限 | [100] (0 ~ 120) | 
| │&nbsp;├&nbsp;下限 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;左 / 右制限 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;スプリングフォース | [1.25] (0 ~ 10) | 制限を超えたときのスプリング力
| │&nbsp;├&nbsp;ダンピング | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;接触距離 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;バウンス | [0.2] (0 ~ 1) | 
| ├&nbsp;**アンカー** | | 
| │&nbsp;├&nbsp;(X) | [-0.03] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [0.03] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.08] (-0.2 ~ 0.2) | 
| ├&nbsp;**センター** | | 
| │&nbsp;├&nbsp;(X) | [0.02] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [-0.05] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.025] (-0.2 ~ 0.2) | 
| ├&nbsp;**衝突** | | 
| │&nbsp;├&nbsp;腕との衝突 | OFF | 
| │&nbsp;├&nbsp;コライダー半径 | [0.07] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;コライダーの長さ | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;コライダー曲線 | [2] (-2 ~ 2) | 布シミュレーションと連動します。
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;乳首を有効にする | ON | 布シミュレーションと連動します。
| │&nbsp;├&nbsp;**乳首の位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [-0.18] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.09] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0.2] (0 ~ 1) | 
| │&nbsp;└&nbsp;乳首のサイズ | [0.1] (0 ~ 1) | 
| ├&nbsp;**(Softbody)** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;ジョイント || 
| │&nbsp;├&nbsp;深度 | [0.4] (0 ~ 1) | 
| │&nbsp;├&nbsp;中心を含める | ON | 
| │&nbsp;├&nbsp;体積制約 | [0.85] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;内部制約 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;表面制約 | [0.75] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;回転制約 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;エッジロック | [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| │&nbsp;├&nbsp;中心ロック | [1] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;ダンピング | [15] (0 ~ 40) | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;├&nbsp;風の影響 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;├&nbsp;体 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;脚 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**シミュレーション設定** | | 
| │&nbsp;│&nbsp;├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │&nbsp;│&nbsp;├&nbsp;ドラッグを有効にする | ON | 
| │&nbsp;│&nbsp;├&nbsp;シミュレート | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;│&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;│&nbsp;├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;サブステップ | [4] (1 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;イテレーション | [1] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;偶数サブステップを逆転 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| │&nbsp;│&nbsp;└&nbsp;二段階解法 | OFF | 
| │&nbsp;└&nbsp;(Presets: Boobs) || 
| │&nbsp;&nbsp;&nbsp;プリセット | **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| ├&nbsp;ソフトボディのみ | OFF | 物理ジョイントを無効にし、ソフトボディパーティクルのみを使用します。
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| **スカートフィジックス**<sup>[PRO]</sup> | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;パーティクルダイナミクスを使用 | ON | 
| ├&nbsp;**シミュレーション設定** | | 
| │&nbsp;├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │&nbsp;├&nbsp;ドラッグを有効にする | ON | 
| │&nbsp;├&nbsp;シミュレート | ON | 
| │&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| │&nbsp;├&nbsp;サブステップ | [4] (1 ~ 20) | 
| │&nbsp;├&nbsp;イテレーション | [1] (0 ~ 10) | 
| │&nbsp;├&nbsp;偶数サブステップを逆転 | OFF | 
| │&nbsp;├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| │&nbsp;├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| │&nbsp;└&nbsp;二段階解法 | OFF | 
| ├&nbsp;プライマリーグループ || 
| ├&nbsp;ボーンを選択 || 
| ├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| ├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| ├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├&nbsp;**親子ジョイント** | | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├&nbsp;**横ジョイント** | | 
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;└&nbsp;ロックZ | OFF | 
| ├&nbsp;**コライダー** | | 
| │&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| ├&nbsp;追加グループ | [0] (0 ~ 7) | 
| ├&nbsp;**(Group 2)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 3)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 4)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 5)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 6)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 7)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| ├&nbsp;**(Group 8)** | | 
| │&nbsp;├&nbsp;有効にする | OFF | 
| │&nbsp;├&nbsp;ボーンを選択 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 横の接続を作るときのソーティング方式を設定します。
| │&nbsp;│&nbsp;ソーティング | **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │&nbsp;├&nbsp;クローズドループ | ON | 各レベルのクローズドループ用のボーン
| │&nbsp;├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │&nbsp;├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ラテラルアンカー | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| │&nbsp;│&nbsp;├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**風** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**衝突する** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー | ON | 
| │&nbsp;├&nbsp;**物理プロパティ** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;質量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ドラッグ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平オーバーラップ | [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │&nbsp;│&nbsp;├&nbsp;質量分布 | [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │&nbsp;│&nbsp;├&nbsp;摩擦 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数 | [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │&nbsp;│&nbsp;└&nbsp;質量中心 | ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │&nbsp;├&nbsp;**親子ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;スイングドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ツイストドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │&nbsp;├&nbsp;**横ジョイント** | | 
| │&nbsp;│&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;線形ドライブ | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角ドライブ | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;ドライブダンピング | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;減衰率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;ロックY | OFF | 
| │&nbsp;│&nbsp;└&nbsp;ロックZ | OFF | 
| │&nbsp;├&nbsp;**コライダー** | | 
| │&nbsp;│&nbsp;├&nbsp;コライダー半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;コライダタイプ | **ボックス** | ボックス, カプセル, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;コライダーの長さ | [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │&nbsp;└&nbsp;プライマリーグループ設定を使用 | ON | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| **ヘア物理** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;ボーンを選択 || ボーンを選択
| ├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │&nbsp;└&nbsp;**シミュレーション設定** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │&nbsp;&nbsp;&nbsp;├&nbsp;ドラッグを有効にする | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;シミュレート | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;サブステップ | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;イテレーション | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;偶数サブステップを逆転 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;二段階解法 | OFF | 
| ├&nbsp;スプリング | [1.25] (0 ~ 5) | 
| ├&nbsp;ダンプ | [0.01] (0 ~ 0.1) | 
| ├&nbsp;減少比率 | [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├&nbsp;ツイストリミット | [5] (0 ~ 180) | ツイスト回転の制限
| ├&nbsp;リミットフォース | [3] (0 ~ 8) | 
| ├&nbsp;質量 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;ドラッグ | [1] (0 ~ 10) | 
| ├&nbsp;コライダー半径 | [0.005] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├&nbsp;コライダーの長さ | [0.9] (0 ~ 1) | 
| ├&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (momiji bob), (Preset 1),  |
| **ぶら下がり物理** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;ボーンを選択 || ボーンを選択
| ├&nbsp;最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├&nbsp;**パーティクルダイナミクス** | | 
| │&nbsp;├&nbsp;有効にする | ON | 
| │&nbsp;├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| │&nbsp;├&nbsp;可視化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;慣性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
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
| │&nbsp;└&nbsp;**シミュレーション設定** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │&nbsp;&nbsp;&nbsp;├&nbsp;ドラッグを有効にする | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;シミュレート | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;サブステップ | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;イテレーション | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;偶数サブステップを逆転 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;二段階解法 | OFF | 
| ├&nbsp;スプリング | [0.5] (0 ~ 5) | 
| ├&nbsp;ダンプ | [0.01] (0 ~ 0.1) | 
| ├&nbsp;減少比率 | [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├&nbsp;ツイストリミット | [5] (0 ~ 180) | ツイスト回転の制限
| ├&nbsp;リミットフォース | [3] (0 ~ 8) | 
| ├&nbsp;質量 | [0.05] (0 ~ 0.1) | 
| ├&nbsp;ドラッグ | [1] (0 ~ 10) | 
| ├&nbsp;コライダー半径 | [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├&nbsp;コライダーの長さ | [0.9] (0 ~ 1) | 
| ├&nbsp;アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
| **オブジェクトを切り離す** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;ボーンを選択 || 
| ├&nbsp;重力 | ON | 
| ├&nbsp;質量 | [0.1] (0 ~ 10) | 
| ├&nbsp;ダンプ | [0] (0 ~ 1) | 
| ├&nbsp;コライダー | 球体 | なし, 球体, カプセル, 
| ├&nbsp;コライダー半径 | [0.1] (0 ~ 1) | 
| └&nbsp;コライダーの長さ | [0.3] (0 ~ 2) | 
| (Presets: Default (Reset)) || 
| プリセット | **デフォルト（リセット）** | デフォルト（リセット）,  |
