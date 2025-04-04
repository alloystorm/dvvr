---
locale: ja-rJP
layout: single
title: ソフトボディフィジックス
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/physics_softbody) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_softbody) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_softbody) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_softbody) | [简中](/zh/dancexr/menu/2025.4/actor/physics_softbody)

[物理](../menu#物理) > ソフトボディフィジックス



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>有効にする</nobr>| [ON] | 
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
|<nobr>ボーンを選択</nobr>|| ボーンを選択
|<nobr>軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr><b>アンカーオフセット</b></nobr>| | 
|<nobr>├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
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
|<nobr>│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr>追加グループ</nobr>| [0] (0 ~ 7) | 
|<nobr><b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr><b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [OFF] | 
|<nobr>├&nbsp;ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp;軸に沿ったアンカー</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>アンカーオフセット</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp;<b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>ジョイント</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;中心を含める</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>&nbsp;&nbsp;├&nbsp;中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>&nbsp;&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>&nbsp;&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>&nbsp;&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;脚</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
