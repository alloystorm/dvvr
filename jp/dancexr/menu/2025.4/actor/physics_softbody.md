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
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする</nobr>| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ</nobr>| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション</nobr>| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 偶数サブステップを逆転</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ</nobr>| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ</nobr>| [6] (1 ~ 20) | 
| └─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 二段階解法</nobr>| [OFF] | 
|  <b>プライマリーグループ</b></nobr>|| 
|  ボーンを選択</nobr>|| ボーンを選択
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| ├─ <b>ジョイント</b></nobr>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| │ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 追加グループ</nobr>| [0] (0 ~ 7) | 
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 2)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 3)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 4)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 5)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 6)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 7)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 8)</b></nobr>| | 
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 有効にする</nobr>| [OFF] | 
| ├─ ボーンを選択</nobr>|| ボーンを選択
| ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 軸に沿ったアンカー</nobr>| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカーオフセット</b></nobr>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用</nobr>| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>ジョイント</b></nobr>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約</nobr>| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約</nobr>| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約</nobr>| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック</nobr>| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング</nobr>| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響</nobr>| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール</nobr>| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度</nobr>| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b></nobr>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 体</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_off.png" alt="check off icon"/> 脚</nobr>| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー</nobr>| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
