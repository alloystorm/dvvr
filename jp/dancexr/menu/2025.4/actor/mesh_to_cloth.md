---
locale: ja-rJP
layout: single
title: メッシュを布に
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[プロ版](../menu#プロ版) > メッシュを布に



| Setting | Value | Description |
| :--- | --- | :--- |
| 一つに結合 | OFF | 
| 徐々に有効化 | [2] (0 ~ 5) | 
| **粒子特性** | | 
| ├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├&nbsp;粘着性 | [0] (0 ~ 1) | 
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
| ├&nbsp;曲げ制約を有効にする | ON | 
| ├&nbsp;曲げ適合性 | [0] (0 ~ 1) | 
| ├&nbsp;スケール | [1] (0 ~ 2) | 
| ├&nbsp;自己衝突 | OFF | 
| ├&nbsp;グリップ質量 | [2] (0 ~ 4) | グリップ粒子の質量
| ├&nbsp;グリップ摩擦 | [2] (-2 ~ 4) | グリップ粒子の摩擦
| ├&nbsp;グリップ粘着性 | [0.25] (0 ~ 1) | グリップ粒子の粘着性
| ├&nbsp;グリップ抗力 | [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| ├&nbsp;グリップスケール | [1] (0 ~ 2) | 
| ├&nbsp;引き裂きを有効にする | OFF | 
| ├&nbsp;引き裂き閾値 | [2] (1 ~ 10) | 
| └&nbsp;引き裂き速度の制限 | [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| **シミュレーション設定** | | 
| ├&nbsp;グローバルを使用 | ON | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| ├&nbsp;ドラッグを有効にする | ON | 
| ├&nbsp;スケールをリセット | [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
| ├&nbsp;シミュレート | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;シミュレーションFPS | **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├&nbsp;時間スケール | [0.65] (0.1 ~ 1) | 
| ├&nbsp;サブステップ | [4] (1 ~ 20) | 
| ├&nbsp;イテレーション | [1] (0 ~ 10) | 
| ├&nbsp;偶数サブステップを逆転 | OFF | 
| ├&nbsp;代替グループサイズ | [0] (0 ~ 20) | 
| ├&nbsp;テーブルサイズ | [6] (1 ~ 20) | 
| └&nbsp;二段階解法 | OFF | 
