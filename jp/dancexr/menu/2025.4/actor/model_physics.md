---
locale: ja-rJP
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/model_physics) | [繁中](/tw/dancexr/menu/2025.4/actor/model_physics) | [日本語](/jp/dancexr/menu/2025.4/actor/model_physics) | [한국어](/kr/dancexr/menu/2025.4/actor/model_physics) | [简中](/zh/dancexr/menu/2025.4/actor/model_physics)

[アクター](../menu#アクター) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>PMX物理を無効にする</nobr>| [OFF] | XPSツールを使用するためにPMX物理を無効にする
|<nobr>制約の軽減</nobr>| [ON] | 滑らかなシミュレーションを可能にするために制約を減らす実験的設定を使用
|<nobr>**衝突**</nobr>| | 
|<nobr>├&nbsp;静的包括</nobr>| [ON] | 
|<nobr>├&nbsp;静的排他的</nobr>| [ON] | 
|<nobr>├&nbsp;動的包括</nobr>| [ON] | 
|<nobr>└&nbsp;動的排他的</nobr>| [ON] | 
|<nobr>**線形運動**</nobr>| | Settings for linear movements
|<nobr>├&nbsp;制約</nobr>| 自動 | 自動, 制限あり, ロックされた, 自由, 
|<nobr>├&nbsp;0制限をロック</nobr>| [ON] | 
|<nobr>├&nbsp;最小スプリング力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;最大制限</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp;弾力性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**角運動**</nobr>| | Settings for angular movements
|<nobr>├&nbsp;制約</nobr>| 自動 | 自動, 制限あり, ロックされた, 自由, 
|<nobr>├&nbsp;0制限をロック</nobr>| [ON] | 
|<nobr>├&nbsp;最小スプリング力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;最大制限</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp;弾力性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**線形ドライブ**</nobr>| | Apply linear drive
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;スプリングフォース</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp;ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**角ドライブ**</nobr>| | Apply angular drive
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;スプリングフォース</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp;ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**線形モーション**</nobr>| | Settings for linear motion
|<nobr>├&nbsp;堅固さ</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;メイン駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;セカンド駆動力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;ターゲット位置</nobr>| ゼロ | ゼロ, センター, 最小, 最大, 
|<nobr>├&nbsp;可能な限りロック</nobr>| [ON] | 
|<nobr>├&nbsp;加速モード</nobr>| [ON] | 
|<nobr>├&nbsp;ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | ジョイント制限を無視することで制約をさらに減少
|<nobr>**角モーション**</nobr>| | Settings for angular motion
|<nobr>├&nbsp;堅固さ</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;メイン駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;セカンド駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;ターゲット位置</nobr>| ゼロ | ゼロ, センター, 最小, 最大, 
|<nobr>├&nbsp;可能な限りロック</nobr>| [OFF] | 
|<nobr>├&nbsp;加速モード</nobr>| [ON] | 
|<nobr>├&nbsp;ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | ジョイント制限を無視することで制約をさらに減少
|<nobr>**オプション**</nobr>| | 
|<nobr>├&nbsp;最小ドラッグ</nobr>| [0] (0 ~ 1) | 自動モードにおける最小ドラッグ値
|<nobr>├&nbsp;ドラッグスケール</nobr>| [1] (0 ~ 5) | 自動モードにおいてドラッグ値に適用されるスケール
|<nobr>├&nbsp;最小質量</nobr>| [0] (0 ~ 1) | 自動モードにおける最小質量値
|<nobr>├&nbsp;質量スケール</nobr>| [1] (0 ~ 10) | 自動モードにおいて質量値に適用されるスケール
|<nobr>├&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;投影距離</nobr>| [0.05] (0 ~ 0.1) | 無中立に対する物体間の距離がこの値を超えたときにジョイントをリセットする力
|<nobr>└&nbsp;投影角度</nobr>| [5] (0 ~ 60) | 無中立に対する物体間の角度がこの値を超えたときにジョイントをリセットする力
|<nobr>自動リセット閾値</nobr>| [35] (0 ~ 100) | 速度がこの値を超えたときにボーンとその子を自動的にリセットする
|<nobr>**自動リセット**</nobr>| | 
|<nobr>└&nbsp;しきい値</nobr>| [30] (0 ~ 50) | 
|<nobr>**ボディコライダー**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;サイズ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;頭部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;腕の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;前腕</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;胸の幅</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;ウエストの幅</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;ヒップの幅</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;お尻の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;お尻の位置</nobr>|| 
|<nobr>├&nbsp;(X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;お腹の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;お腹の位置</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;脚の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;太ももの前後</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;太ももの開始位置</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;手</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (amy), (misaki),  |
|<nobr>**胸部物理**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;スプリングフォース</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp;ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;重力カウンター</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp;**回転制限**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;上限</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp;下限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;左 / 右制限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;スプリングフォース</nobr>| [1.25] (0 ~ 10) | 制限を超えたときのスプリング力
|<nobr>│&nbsp;├&nbsp;ダンピング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;バウンス</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;**アンカー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**センター**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**衝突**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;腕との衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;コライダー曲線</nobr>| [2] (-2 ~ 2) | 布シミュレーションと連動します。
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;乳首を有効にする</nobr>| [ON] | 布シミュレーションと連動します。
|<nobr>│&nbsp;├&nbsp;**乳首の位置**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;乳首のサイズ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;**(Softbody)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;ジョイント</nobr>|| 
|<nobr>│&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>│&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
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
|<nobr>│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**シミュレーション設定**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr>├&nbsp;ソフトボディのみ</nobr>| [OFF] | 物理ジョイントを無効にし、ソフトボディパーティクルのみを使用します。
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr>**スカートフィジックス**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;パーティクルダイナミクスを使用</nobr>| [ON] | 
|<nobr>├&nbsp;**シミュレーション設定**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp;プライマリーグループ</nobr>|| 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;**パーティクルダイナミクス**</nobr>| | 
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
|<nobr>│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
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
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>├&nbsp;追加グループ</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp;**(Group 2)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 3)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 4)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 5)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 6)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 7)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 8)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp;ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp;クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**風**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**衝突する**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理プロパティ**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp;質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp;質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp;**親子ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp;**横ジョイント**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**コライダー**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr>**ヘア物理**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
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
|<nobr>│&nbsp;└&nbsp;**シミュレーション設定**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp;スプリング</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp;ダンプ</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;減少比率</nobr>| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
|<nobr>├&nbsp;ツイストリミット</nobr>| [5] (0 ~ 180) | ツイスト回転の制限
|<nobr>├&nbsp;リミットフォース</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;質量</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;コライダー半径</nobr>| [0.005] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
|<nobr>├&nbsp;コライダーの長さ</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (momiji bob), (Preset 1),  |
|<nobr>**ぶら下がり物理**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp;**パーティクルダイナミクス**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
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
|<nobr>│&nbsp;└&nbsp;**シミュレーション設定**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp;スプリング</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp;ダンプ</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;減少比率</nobr>| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
|<nobr>├&nbsp;ツイストリミット</nobr>| [5] (0 ~ 180) | ツイスト回転の制限
|<nobr>├&nbsp;リミットフォース</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;質量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp;ドラッグ</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;コライダー半径</nobr>| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
|<nobr>├&nbsp;コライダーの長さ</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>└&nbsp;プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
|<nobr>**オブジェクトを切り離す**</nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| 
|<nobr>├&nbsp;重力</nobr>| [ON] | 
|<nobr>├&nbsp;質量</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;ダンプ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;コライダー</nobr>| 球体 | なし, 球体, カプセル, 
|<nobr>├&nbsp;コライダー半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp;コライダーの長さ</nobr>| [0.3] (0 ~ 2) | 
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
