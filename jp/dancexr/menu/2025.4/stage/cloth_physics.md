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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
|  ボーンを選択|| ボーンを選択
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>パーティクルダイナミクス</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
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
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 偶数サブステップを逆転| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─ □ 二段階解法| [OFF] | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリング| [0.5] (0 ~ 5) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンプ| [0.01] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストリミット| [5] (0 ~ 180) | ツイスト回転の制限
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> リミットフォース| [3] (0 ~ 8) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.05] (0 ~ 0.1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.9] (0 ~ 1) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
