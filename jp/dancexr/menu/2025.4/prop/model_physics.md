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
|  □ PMX物理を無効にする| [OFF] | XPSツールを使用するためにPMX物理を無効にする
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 制約の軽減| [ON] | 滑らかなシミュレーションを可能にするために制約を減らす実験的設定を使用
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 静的包括| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 静的排他的| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 動的包括| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 動的排他的| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>線形運動</b>| | Settings for linear movements
| ├─ ☑ 制約| 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 0制限をロック| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最小スプリング力| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大制限| [0.05] (0.05 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 弾力性| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 接触距離| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>角運動</b>| | Settings for angular movements
| ├─ ☑ 制約| 自動 | 自動, 制限あり, ロックされた, 自由, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 0制限をロック| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最小スプリング力| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大制限| [90] (3 ~ 90) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 弾力性| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 接触距離| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>線形ドライブ</b>| | Apply linear drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリングフォース| [3] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>角ドライブ</b>| | Apply angular drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリングフォース| [0.1] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>線形モーション</b>| | Settings for linear motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 堅固さ| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> メイン駆動力| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> セカンド駆動力| [3] (0 ~ 8) | 
| ├─ ☑ ターゲット位置| ゼロ | ゼロ, センター, 最小, 最大, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可能な限りロック| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 加速モード| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | ジョイント制限を無視することで制約をさらに減少
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>角モーション</b>| | Settings for angular motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 堅固さ| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> メイン駆動力| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> セカンド駆動力| [5] (0 ~ 8) | 
| ├─ ☑ ターゲット位置| ゼロ | ゼロ, センター, 最小, 最大, 
| ├─ □ 可能な限りロック| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 加速モード| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | ジョイント制限を無視することで制約をさらに減少
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>オプション</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最小ドラッグ| [0] (0 ~ 1) | 自動モードにおける最小ドラッグ値
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグスケール| [1] (0 ~ 5) | 自動モードにおいてドラッグ値に適用されるスケール
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最小質量| [0] (0 ~ 1) | 自動モードにおける最小質量値
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量スケール| [1] (0 ~ 10) | 自動モードにおいて質量値に適用されるスケール
| ├─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 投影距離| [0.05] (0 ~ 0.1) | 無中立に対する物体間の距離がこの値を超えたときにジョイントをリセットする力
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 投影角度| [5] (0 ~ 60) | 無中立に対する物体間の角度がこの値を超えたときにジョイントをリセットする力
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 自動リセット閾値| [35] (0 ~ 100) | 速度がこの値を超えたときにボーンとその子を自動的にリセットする
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>自動リセット</b>| | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> しきい値| [30] (0 ~ 50) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ボディコライダー</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サイズ| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭部半径| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 腕の半径| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 前腕| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸の幅| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ウエストの幅| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ヒップの幅| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> お尻の半径| [1] (0 ~ 2) | 
| ├─ <b>お尻の位置</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> お腹の半径| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> お腹の位置| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 脚の半径| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 太ももの前後| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 太ももの開始位置| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 手| [0] (0 ~ 1) | 
| ├─ □ 可視化| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (amy), (misaki),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>胸部物理</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリングフォース| [1.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力カウンター| [10] (0 ~ 45) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>回転制限</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 上限| [100] (0 ~ 120) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 下限| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 左 / 右制限| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリングフォース| [1.25] (0 ~ 10) | 制限を超えたときのスプリング力
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 接触距離| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バウンス| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>アンカー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.03] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.03] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.08] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>センター</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.02] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.05] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.025] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突</b>| | 
| │ ├─ □ 腕との衝突| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.07] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー曲線| [2] (-2 ~ 2) | 布シミュレーションと連動します。
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 乳首を有効にする| [ON] | 布シミュレーションと連動します。
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>乳首の位置</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.18] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.09] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.2] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乳首のサイズ| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>(Softbody)</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| │ ├─ <b>ジョイント</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 中心を含める| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体積制約| [0.85] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 内部制約| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面制約| [0.75] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 回転制約| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> エッジロック| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心ロック| [1] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンピング| [15] (0 ~ 40) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ ├─ □ 体| [OFF] | 
| │ │ ├─ □ 胸部| [OFF] | 
| │ │ ├─ □ 臀部| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ ├─ □ 脚| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| │ │ ├─ □ 偶数サブステップを逆転| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| │ │ └─ □ 二段階解法| [OFF] | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
| ├─ □ ソフトボディのみ| [OFF] | 物理ジョイントを無効にし、ソフトボディパーティクルのみを使用します。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>スカートフィジックス</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> パーティクルダイナミクスを使用| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| │ ├─ □ 偶数サブステップを逆転| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| │ └─ □ 二段階解法| [OFF] | 
| ├─ <b>プライマリーグループ</b>|| 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ ├─ □ 可視化| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ ├─ □ ロックY| [OFF] | 
| │ └─ □ ロックZ| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 追加グループ| [0] (0 ~ 7) | 
| ├─ □ <b>(Group 2)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 3)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 4)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 5)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 6)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| │ │ └─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| │ │ ├─ □ ロックY| [OFF] | 
| │ │ └─ □ ロックZ| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 7)</b>| | 
| │ ├─ □ 有効にする| [OFF] | 
| │ ├─ ボーンを選択|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 可視化| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ ロックY| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ ロックZ| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| <img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| ├─ □ <b>(Group 8)</b>| | 
| <img src="/images/icon/ic_line_v.png"/>├─ □ 有効にする| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/>├─ ボーンを選択|| 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ソーティング| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> クローズドループ| [ON] | 各レベルのクローズドループ用のボーン
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルコンプライアンス| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ラテラルアンカー| [0] (0 ~ 0.5) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>物理プロパティ</b>| | Physics properties like mass, drag and friction
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水平オーバーラップ| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量分布| [0] (-1 ~ 1) | 各レベルで質量を減少させる
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソルバーの反復回数| [20] (1 ~ 150) | 衝突を解決する際の反復回数
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 質量中心| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>親子ジョイント</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングドライブ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストドライブ| [5] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.01] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>横ジョイント</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 線形ドライブ| [5] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角ドライブ| [0] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドライブダンピング| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減衰率| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ ロックY| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ ロックZ| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>コライダー</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> コライダタイプ| **ボックス** | ボックス, カプセル, 球体,  |
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
| <img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プライマリーグループ設定を使用| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ヘア物理</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| <img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ □ 偶数サブステップを逆転| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ □ 二段階解法| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリング| [1.25] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンプ| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストリミット| [5] (0 ~ 180) | ツイスト回転の制限
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> リミットフォース| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.005] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (momiji bob), (Preset 1),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ぶら下がり物理</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ボーンを選択|| ボーンを選択
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最初のXボーンをスキップ| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>パーティクルダイナミクス</b>| | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スイングコンプライアンス| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストコンプライアンス| [0.75] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> パーティクルアンカー| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0] (0 ~ 1) | 各レベルでの質量削減
| <img src="/images/icon/ic_line_v.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ソフト化| [0] (0 ~ 1) | パーティクル制約をソフト化する。
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半径| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空気の抗力| [0] (0 ~ 2) | 空気抵抗
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水中の抗力| [1] (0 ~ 2) | 水中抵抗
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風の影響| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流スケール| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 乱流時間スケール| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>衝突する</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 体| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 胸部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 臀部| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 脚| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 足| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> プレイヤー| [ON] | 
| <img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>シミュレーション設定</b>| | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルを使用| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ドラッグを有効にする| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シミュレート| [ON] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> シミュレーションFPS| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間スケール| [0.65] (0.1 ~ 1) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> サブステップ| [4] (1 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> イテレーション| [1] (0 ~ 10) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ □ 偶数サブステップを逆転| [OFF] | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 代替グループサイズ| [0] (0 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> テーブルサイズ| [6] (1 ~ 20) | 
| <img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ □ 二段階解法| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スプリング| [0.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンプ| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 減少比率| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ツイストリミット| [5] (0 ~ 180) | ツイスト回転の制限
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> リミットフォース| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.05] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ドラッグ| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> アンカーポジション| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>オブジェクトを切り離す</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ボーンを選択|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 重力| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 質量| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ダンプ| [0] (0 ~ 1) | 
| ├─ ☑ コライダー| 球体 | なし, 球体, カプセル, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダー半径| [0.1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コライダーの長さ| [0.3] (0 ~ 2) | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）,  |
