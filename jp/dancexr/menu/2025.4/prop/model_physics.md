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
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  PMX物理を無効にする</nobr>| [OFF] | XPSツールを使用するためにPMX物理を無効にする
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  制約の軽減</nobr>| [ON] | 滑らかなシミュレーションを可能にするために制約を減らす実験的設定を使用
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>衝突</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  静的包括</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  静的排他的</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  動的包括</nobr>| [ON] | 
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  動的排他的</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>線形運動</b></nobr>| | Settings for linear movements
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  制約</nobr>| 自動 | 自動, 制限あり, ロックされた, 自由, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  0制限をロック</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小スプリング力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大制限</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  弾力性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>角運動</b></nobr>| | Settings for angular movements
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  制約</nobr>| 自動 | 自動, 制限あり, ロックされた, 自由, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  0制限をロック</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小スプリング力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大制限</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  弾力性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>線形ドライブ</b></nobr>| | Apply linear drive
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリングフォース</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>角ドライブ</b></nobr>| | Apply angular drive
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリングフォース</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>線形モーション</b></nobr>| | Settings for linear motion
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  堅固さ</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  メイン駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  セカンド駆動力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  ターゲット位置</nobr>| ゼロ | ゼロ, センター, 最小, 最大, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  可能な限りロック</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  加速モード</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Ignore Limit)</nobr>| [OFF] | ジョイント制限を無視することで制約をさらに減少
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>角モーション</b></nobr>| | Settings for angular motion
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  堅固さ</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  メイン駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  セカンド駆動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  ターゲット位置</nobr>| ゼロ | ゼロ, センター, 最小, 最大, 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可能な限りロック</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  加速モード</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Ignore Limit)</nobr>| [OFF] | ジョイント制限を無視することで制約をさらに減少
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>オプション</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小ドラッグ</nobr>| [0] (0 ~ 1) | 自動モードにおける最小ドラッグ値
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグスケール</nobr>| [1] (0 ~ 5) | 自動モードにおいてドラッグ値に適用されるスケール
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小質量</nobr>| [0] (0 ~ 1) | 自動モードにおける最小質量値
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量スケール</nobr>| [1] (0 ~ 10) | 自動モードにおいて質量値に適用されるスケール
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  投影距離</nobr>| [0.05] (0 ~ 0.1) | 無中立に対する物体間の距離がこの値を超えたときにジョイントをリセットする力
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  投影角度</nobr>| [5] (0 ~ 60) | 無中立に対する物体間の角度がこの値を超えたときにジョイントをリセットする力
|<nobr> ![slider icon](/images/icon/ic_slider.png)  自動リセット閾値</nobr>| [35] (0 ~ 100) | 速度がこの値を超えたときにボーンとその子を自動的にリセットする
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>自動リセット</b></nobr>| | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  しきい値</nobr>| [30] (0 ~ 50) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>ボディコライダー</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サイズ</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  頭部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  腕の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  前腕</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  胸の幅</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ウエストの幅</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ヒップの幅</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  お尻の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; <b>お尻の位置</b></nobr>|| 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  お腹の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  お腹の位置</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  脚の半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  太ももの前後</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  太ももの開始位置</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  手</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (amy), (misaki),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>胸部物理</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリングフォース</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力カウンター</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>回転制限</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  上限</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  下限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  左 / 右制限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリングフォース</nobr>| [1.25] (0 ~ 10) | 制限を超えたときのスプリング力
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接触距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  バウンス</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>アンカー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>センター</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腕との衝突</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー曲線</nobr>| [2] (-2 ~ 2) | 布シミュレーションと連動します。
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  乳首を有効にする</nobr>| [ON] | 布シミュレーションと連動します。
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>乳首の位置</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乳首のサイズ</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>(Softbody)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>ジョイント</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  中心を含める</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体積制約</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  内部制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面制約</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  回転制約</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  エッジロック</nobr>| [0.85] (0.5 ~ 1) | エッジ上の粒子をロックする。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心ロック</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンピング</nobr>| [15] (0 ~ 40) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  体</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  脚</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>シミュレーション設定</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  二段階解法</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **胸部** | 胸部, 臀部, 脚, (tina), (预设1), (预设2),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ソフトボディのみ</nobr>| [OFF] | 物理ジョイントを無効にし、ソフトボディパーティクルのみを使用します。
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>スカートフィジックス</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  パーティクルダイナミクスを使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>シミュレーション設定</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp; <b>プライマリーグループ</b></nobr>|| 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  追加グループ</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 2)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 3)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 4)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 5)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 6)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 7)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 8)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  有効にする</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ボーンを選択</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  ソーティング</nobr>| **最短パス** | 最短パス, 円形, リニア, ソーティングなし, <br/>横の接続を作るときのソーティング方式を設定します。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  クローズドループ</nobr>| [ON] | 各レベルのクローズドループ用のボーン
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルコンプライアンス</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ラテラルアンカー</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理プロパティ</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平オーバーラップ</nobr>| [-0.2] (-1 ~ 1) | コライダーの水平オーバーラップ
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分布</nobr>| [0] (-1 ~ 1) | 各レベルで質量を減少させる
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソルバーの反復回数</nobr>| [20] (1 ~ 150) | 衝突を解決する際の反復回数
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質量中心</nobr>| ゼロ | 自動, ゼロ, <br/>質量中心をゼロまたは各コライダーの位置とサイズに基づいて自動的に設定
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>親子ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>横ジョイント</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線形ドライブ</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角ドライブ</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドライブダンピング</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減衰率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックY</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  ロックZ</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>コライダー</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  コライダタイプ</nobr>| **ボックス** | ボックス, カプセル, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.8] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 身体コライダーからの干渉を避けるために、最初のレベルのボーンのコライダーの長さを減少させます。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プライマリーグループ設定を使用</nobr>| [ON] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>ヘア物理</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>シミュレーション設定</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリング</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンプ</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストリミット</nobr>| [5] (0 ~ 180) | ツイスト回転の制限
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  リミットフォース</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.005] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (momiji bob), (Preset 1),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>ぶら下がり物理</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| ボーンを選択
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最初のXボーンをスキップ</nobr>| [0] (0 ~ 5) | 最初のXレベルには物理接続を作成しない
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>パーティクルダイナミクス</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スイングコンプライアンス</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストコンプライアンス</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  パーティクルアンカー</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 各レベルでの質量削減
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ソフト化</nobr>| [0] (0 ~ 1) | パーティクル制約をソフト化する。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半径</nobr>| [5] (1 ~ 20) | 粒子のサイズ（ミリメートル）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空気の抗力</nobr>| [0] (0 ~ 2) | 空気抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水中の抗力</nobr>| [1] (0 ~ 2) | 水中抵抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風の影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流スケール</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乱流時間スケール</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>衝突する</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  足</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  プレイヤー</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>シミュレーション設定</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  グローバルを使用</nobr>| [ON] | Pro / Cloth Simulationの下にあるグローバル設定を見つける
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  ドラッグを有効にする</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  シミュレート</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  シミュレーションFPS</nobr>| **ダイナミック** | ダイナミック, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間スケール</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  サブステップ</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  イテレーション</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  偶数サブステップを逆転</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  代替グループサイズ</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  テーブルサイズ</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  二段階解法</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  スプリング</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンプ</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0.25] (0 ~ 1) | 各レベルでの硬さの減少
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ツイストリミット</nobr>| [5] (0 ~ 180) | ツイスト回転の制限
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  リミットフォース</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ドラッグ</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.01] (0 ~ 0.05) | 衝突解決時に使用される粒子のサイズ。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  アンカーポジション</nobr>| [0] (0 ~ 1) | ジョイントを作成する際のアンカーポジションを選択。0 = 親ボーンにアンカー、1 = 子ボーンにアンカー
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>オブジェクトを切り離す</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  有効にする</nobr>| [ON] | 
|<nobr>├&nbsp; ボーンを選択</nobr>|| 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  重力</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  ダンプ</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  コライダー</nobr>| 球体 | なし, 球体, カプセル, 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダー半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  コライダーの長さ</nobr>| [0.3] (0 ~ 2) | 
|<nobr> ![list icon](/images/icon/ic_list.png)  プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）,  |
