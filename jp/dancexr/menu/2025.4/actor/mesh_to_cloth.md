---
locale: ja-rJP
layout: single
title: メッシュを布に
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[プロ版](../menu#プロ版) > メッシュを布に



| Setting | Value | Description |
| :--- | --- | :--- |
|  □ 一つに結合| [OFF] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 徐々に有効化| [2] (0 ~ 5) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子特性</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粘着性| [0] (0 ~ 1) | 
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
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 曲げ制約を有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲げ適合性| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スケール| [1] (0 ~ 2) | 
| ├─ □ 自己衝突| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ質量| [2] (0 ~ 4) | グリップ粒子の質量
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ摩擦| [2] (-2 ~ 4) | グリップ粒子の摩擦
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ粘着性| [0.25] (0 ~ 1) | グリップ粒子の粘着性
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップ抗力| [0] (-2 ~ 2) | グリップ粒子の空気抵抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グリップスケール| [1] (0 ~ 2) | 
| ├─ □ 引き裂きを有効にする| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き閾値| [2] (1 ~ 10) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 引き裂き速度の制限| [0] (0 ~ 25) | 引き裂き後のクールダウン間隔（フレーム単位）
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スケールをリセット| [1] (1 ~ 5) | フィッティングを助けるためにリセット中に布のスケールを大きくする
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| ├─ □ 偶数サブステップを逆転| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| └─ □ 二段階解法| [OFF] | 
