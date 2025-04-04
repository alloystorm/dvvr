---
locale: ja-rJP
layout: single
title: ぶら下がり物理
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/stage/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/stage/cloth_physics)

[ステージ](../menu#ステージ) > ぶら下がり物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>有効にする</nobr>| [ON] | 
|<nobr>ボーンを選択</nobr>|| ボーンを選択
|<nobr>最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr><b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>├&nbsp;有効にする</nobr>| [ON] | 
|<nobr>├&nbsp;スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
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
|<nobr>├&nbsp;<b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;頭</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;体</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;足</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;プレイヤー</nobr>| [ON] | 
|<nobr>└&nbsp;<b>シミュレーション設定</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>&nbsp;&nbsp;├&nbsp;ドラッグを有効にする</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;シミュレート</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>&nbsp;&nbsp;├&nbsp;時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>&nbsp;&nbsp;├&nbsp;偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>&nbsp;&nbsp;├&nbsp;テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>&nbsp;&nbsp;└&nbsp;二段階解法</nobr>| [OFF] | 
|<nobr>スプリング</nobr>| [0.5] (0 ~ 5) | 
|<nobr>ダンプ</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>減少比率</nobr>| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
|<nobr>ツイストリミット</nobr>| [5] (0 ~ 180) | ツイスト回転の制限
|<nobr>リミットフォース</nobr>| [3] (0 ~ 8) | 
|<nobr>質量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>ドラッグ</nobr>| [1] (0 ~ 10) | 
|<nobr>コライダー半径</nobr>| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
|<nobr>コライダーの長さ</nobr>| [0.9] (0 ~ 1) | 
|<nobr>アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
