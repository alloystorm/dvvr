---
locale: ja-rJP
layout: single
title: ぶら下がり物理
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > ぶら下がり物理



| Setting | Value | Description |
| :--- | --- | :--- |
| 有効にする | ON | 
| ボーンを選択 || ボーンを選択
| 最初のXボーンをスキップ | [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| **パーティクルダイナミクス** | | 
| ├&nbsp;有効にする | ON | 
| ├&nbsp;スイングコンプライアンス | [0.25] (0 ~ 1) | 
| ├&nbsp;ツイストコンプライアンス | [0.75] (0 ~ 1) | 
| ├&nbsp;パーティクルアンカー | [0.5] (0 ~ 1) | 
| ├&nbsp;減少比率 | [0] (0 ~ 1) | 各レベルでの質量削減
| ├&nbsp;可視化 | OFF | 
| ├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| ├&nbsp;慣性 | [2] (1 ~ 5) | 
| ├&nbsp;ソフト化 | [0] (0 ~ 1) | パーティクル制約をソフト化する。
| ├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| ├&nbsp;摩擦 | [1] (0 ~ 2) | 
| ├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| ├&nbsp;空気の抗力 | [0] (0 ~ 2) | 空気抵抗
| ├&nbsp;水中の抗力 | [1] (0 ~ 2) | 水中抵抗
| ├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| ├&nbsp;**風** | | 
| │&nbsp;├&nbsp;風の影響 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;乱流スケール | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;乱流強度 | [1] (0 ~ 2) | 
| │&nbsp;└&nbsp;乱流時間スケール | [0] (-4 ~ 4) | 
| ├&nbsp;**衝突する** | | 
| │&nbsp;├&nbsp;頭 | ON | 
| │&nbsp;├&nbsp;体 | ON | 
| │&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;├&nbsp;手 | ON | 
| │&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;├&nbsp;足 | ON | 
| │&nbsp;└&nbsp;プレイヤー | ON | 
| └&nbsp;**シミュレーション設定** | | 
| &nbsp;&nbsp;├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| &nbsp;&nbsp;├&nbsp;ドラッグを有効にする | ON | 
| &nbsp;&nbsp;├&nbsp;シミュレート | ON | 
| &nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| &nbsp;&nbsp;│&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| &nbsp;&nbsp;├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;サブステップ | [4] (1 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;イテレーション | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;偶数サブステップを逆転 | OFF | 
| &nbsp;&nbsp;├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| &nbsp;&nbsp;└&nbsp;二段階解法 | OFF | 
| スプリング | [0.5] (0 ~ 5) | 
| ダンプ | [0.01] (0 ~ 0.1) | 
| 減少比率 | [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ツイストリミット | [5] (0 ~ 180) | ツイスト回転の制限
| リミットフォース | [3] (0 ~ 8) | 
| 質量 | [0.05] (0 ~ 0.1) | 
| ドラッグ | [1] (0 ~ 10) | 
| コライダー半径 | [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| コライダーの長さ | [0.9] (0 ~ 1) | 
| アンカーポジション | [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| (Presets: Default (Reset)) || 
| プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
