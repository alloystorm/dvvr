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



[(Feature Page)](/jp/dancexr/features/physics_softbody)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
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
|  ボーンを選択|| ボーンを選択
|  □ 軸に沿ったアンカー| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| ├─ <b>ジョイント</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
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
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ ├─ □ 体| [OFF] | 
| │ ├─ □ 胸部| [OFF] | 
| │ ├─ □ 臀部| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ ├─ □ 脚| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 追加グループ| [0] (0 ~ 7) | 
|  □ <b>(Group 2)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 3)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 4)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 5)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 6)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 7)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|  □ <b>(Group 8)</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─ □ 軸に沿ったアンカー| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 体| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 脚| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）,  |
