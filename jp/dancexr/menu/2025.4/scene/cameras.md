---
locale: ja-rJP
layout: single
title: (Camera: [Freefly Cam])
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[環境](../menu#環境) > (Camera: [Freefly Cam])



| Setting | Value | Description |
| :--- | --- | :--- |
| [フリーフライカメラ] || 
| └ **[フリーフライカメラ]** | | 
|   ├ (Target Select: Auto) || 
|   │ ターゲット選択 | **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|   ├ (Tracking Mode: Center) || 
|   │ トラッキングモード | **センター** | センター, 頭, 胸,  |
|   ├ ターゲットスムージング | [0.5] (0 ~ 2) | 
|   ├ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|   ├ ターゲットにロックオン | OFF | 自動的にターゲットに焦点を合わせる
|   ├ カメラの揺れ | [0.5] (0 ~ 1) | 
|   ├ 回転固定 | OFF | カメラがターゲットの回転に従う
|   ├ 自動ズーム | [0] (0 ~ 1) | ターゲットサイズを見える範囲に保つために自動でズームイン・アウト
|   ├ ズーム速度 | [0.5] (0 ~ 1) | ターゲットFOVにズームするのにかかる時間
|   ├ ターゲット時のFOVの高さ | [1] (0.2 ~ 2) | 自動ズーム時のターゲットの縦の高さ
|   ├ 縦オフセット | [0] (-1 ~ 1) | 縦にオフセット
|   ├ FOV | [30] (5 ~ 120) | 
|   ├ ビートサイクル | [8] (1 ~ 16) | 
|   ├ オービット移動を使用 | OFF | (Enable or disable orbit movement, allowing the camera to rotate around a central point.)
|   └ (Presets: Freefly) || 
|     プリセット | **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
| [オービットカム] || 
| └ **[オービットカム]** | | 
|   ├ (Target Select: Auto) || 
|   │ ターゲット選択 | **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|   ├ (Tracking Mode: Center) || 
|   │ トラッキングモード | **センター** | センター, 頭, 胸,  |
|   ├ ターゲットスムージング | [0.5] (0 ~ 2) | 
|   ├ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|   ├ FOV | [30] (5 ~ 120) | 
|   ├ ビートサイクル | [8] (1 ~ 16) | 
|   ├ コントローラー入力を使用 | OFF | 
|   ├ 床下を防ぐ | ON | 
|   ├ 速度を維持する | OFF | 入力がないときに回転を維持
|   ├ 最大速度 | [15] (0 ~ 30) | 最大回転速度
|   ├ 最小速度 | [0] (0 ~ 30) | 最小回転速度
|   ├ 自動モード | OFF | 
|   ├ 最小距離 | [1] (0 ~ 10) | 
|   ├ 最大距離 | [3] (1 ~ 10) | 
|   ├ 距離サイクル | [12] ((Unlimited)) | 
|   ├ 最小ピッチ | [-15] (-45 ~ 0) | 
|   ├ 最大ピッチ | [15] (0 ~ 45) | 
|   ├ ピッチサイクル | [32] ((Unlimited)) | 
|   ├ 最小高さ | [0] (-1 ~ 0) | 
|   ├ 最大高さ | [0.5] (0 ~ 1) | 
|   ├ 高さサイクル | [32] ((Unlimited)) | 
|   ├ スピード | [10] (0 ~ 90) | 
|   └ (Presets: Default (Reset)) || 
|     プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
| [オートカム] || 
| └ **[オートカム]** | | 
|   ├ (Target Select: Auto) || 
|   │ ターゲット選択 | **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|   ├ (Tracking Mode: Center) || 
|   │ トラッキングモード | **センター** | センター, 頭, 胸,  |
|   ├ ターゲットスムージング | [0.5] (0 ~ 2) | 
|   ├ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|   ├ FOV | [30] (5 ~ 120) | 
|   ├ ビートサイクル | [8] (1 ~ 16) | 
|   ├ 近距離 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|   ├ 遠距離 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|   ├ アクターの向きを使用 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
|   ├ シード | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|   ├ フェード・トゥ・ブラック | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|   ├ F2B 確率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|   ├ オーディオ感度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|   ├ ターゲット選択 || 
|   ├ 頭 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|   ├ 胸 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|   ├ センター | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|   ├ 脚 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|   ├ 足 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|   ├ 距離選択 || 
|   ├ クローズアップ | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|   ├ ズームイン | [0.25] (0 ~ 1) | (Probability of zooming in.)
|   ├ ズームアウト | [0.25] (0 ~ 1) | (Probability of zooming out.)
|   ├ 中間 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|   ├ 遠方 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|   ├ パス選択 || 
|   ├ 高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|   ├ 低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|   ├ オリエンテーション || 
|   ├ 前方中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|   ├ 前方 45 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|   ├ 横 90 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|   ├ 後方 135 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|   ├ 後方 180 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|   └ (Presets: Default (Reset)) || 
|     プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
| [長回し] || 
| └ **[長回し]** | | 
|   ├ (Target Select: Auto) || 
|   │ ターゲット選択 | **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|   ├ (Tracking Mode: Center) || 
|   │ トラッキングモード | **センター** | センター, 頭, 胸,  |
|   ├ ターゲットスムージング | [0.5] (0 ~ 2) | 
|   ├ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|   ├ FOV | [30] (5 ~ 120) | 
|   ├ ビートサイクル | [8] (1 ~ 16) | 
|   ├ 回転範囲 | [60] (0 ~ 180) | 水平方向の回転範囲。
|   ├ 距離 | [0.5] (0.2 ~ 5) | 
|   ├ ピッチ角度 | [-15] (-90 ~ 90) | 
|   ├ カーブ | [0] (-1 ~ 1) | 動きが変わるときに使用されるイーズカーブ
|   ├ 床下を防ぐ | ON | 
|   ├ アクターの向きを使用 | ON | 
|   ├ 近くに来たときにフォーカスを上げる | OFF | 距離が小さくなるときにフォーカス位置を上に移動する
|   └ (Presets: Default (Reset)) || 
|     プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1), (Preset 2), (Preset 3),  |
| [第一人称] || 
| └ **[第一人称]** | | 
|   ├ アクターを選択 || 
|   │ アクターを選択 |  |  |
|   ├ 視野角 | [45] (30 ~ 100) | 
|   ├ 近接クリップ距離 | [0.15] (0 ~ 0.3) | 
|   ├ アクターの移動を制御 | ON | 
|   ├ VR内の手を制御 | ON | 
|   ├ ロールを解除 | [1] (0 ~ 1) | 
|   ├ スタビライザー | [5] (0 ~ 20) | 
|   ├ ダンピング | [0.1] (0 ~ 1) | 
|   ├ 自動復帰を無効化 | OFF | 
|   └ 中心に戻す || 
| [固定カメラ] || 
| └ **[固定カメラ]** | | 
|   ├ (Target Select: Auto) || 
|   │ ターゲット選択 | **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|   ├ (Tracking Mode: Center) || 
|   │ トラッキングモード | **センター** | センター, 頭, 胸,  |
|   ├ ターゲットスムージング | [0.5] (0 ~ 2) | 
|   ├ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|   ├ ターゲットにロックオン | OFF | 自動的にターゲットに焦点を合わせる
|   ├ カメラの揺れ | [0.5] (0 ~ 1) | 
|   ├ 回転固定 | OFF | カメラがターゲットの回転に従う
|   ├ 自動ズーム | [0] (0 ~ 1) | ターゲットサイズを見える範囲に保つために自動でズームイン・アウト
|   ├ ズーム速度 | [0.5] (0 ~ 1) | ターゲットFOVにズームするのにかかる時間
|   ├ ターゲット時のFOVの高さ | [1] (0.2 ~ 2) | 自動ズーム時のターゲットの縦の高さ
|   ├ 縦オフセット | [0] (-1 ~ 1) | 縦にオフセット
|   ├ FOV | [10] (5 ~ 120) | 
|   ├ ビートサイクル | [8] (1 ~ 16) | 
|   ├ サイズ | [1] (0 ~ 2) | 
|   ├ シフト | [0] (-1 ~ 1) | 
|   ├ ターゲットセンター | [0] (-1 ~ 1) | 
|   ├ オフセット || 
|   ├ (X) | [0] (-2 ~ 2) | 
|   ├ (Y) | [0] (-2 ~ 2) | 
|   ├ (Z) | [0] (-2 ~ 2) | 
|   └ (Presets: Far) || 
|     プリセット | **遠方** | 近く, 遠方,  |
| 設定 || 
| [カメラ設定](config_camera) |
