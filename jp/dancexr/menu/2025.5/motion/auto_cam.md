---
locale: ja-rJP
layout: single
title: [オートカム]
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.5/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.5/motion/auto_cam)

[プロシージャル](../menu#プロシージャル) > [オートカム]

(
## Overview
The Automatic Camera Motion System (AutoCam) is a dynamic camera control solution designed to enhance visual storytelling by synchronizing camera movements with music beats, actor orientation, and configurable parameters.

## Key Features
- Dynamic adjustment of camera motion based on music beats.
- Configurable parameters for distance, target selection, and motion paths.
- Support for actor orientation alignment.
- Randomized camera motion generation with seed control.
- Fade-to-black transitions with adjustable duration and probability.
- Audio sensitivity for motion responsiveness to sound levels.

## Use Cases
- Creating cinematic sequences in real-time.
- Enhancing the visual appeal of dance or music-based performances.
- Automating camera control for interactive applications or games.)

## 設定

| 設定 | 値 | 説明 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> メインに割り当て || 
| > ターゲット選択 | **自動** | 自動, 選択済み, グループ, 回転, 回転＋グループ, ステージセンター,  |
| > トラッキングモード | **中心** | 中心, 頭, 胸,  |
| ⊖ ターゲットスムージング | [0.5] (0 ~ 2) | 
| ⊖ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減らすためにターゲットの位置を予測
| ⊖ FOV | [30] (5 ~ 120) | 
| ⊖ ビートサイクル | [8] (1 ~ 16) | 
| ⊖ 近距離 | [1.5] (0.5 ~ 3) | カメラとターゲット間の最小距離。
| ⊖ 遠距離 | [2.5] (0.5 ~ 3) | カメラとターゲット間の最大距離。
| ☑ アクターの向きを使用 | [ON] | カメラをアクターの向きに合わせるかどうかを有効化または無効化します。
| ⊖ シード | [1234] ((Unlimited)) | ランダムなカメラモーションを生成するためのシード値。
| ⊖ フェードアウト（ブラックアウト） | [0] (0 ~ 0.25) | トランジション中のフェードアウト効果の継続時間。
| ⊖ フェードアウト確率 | [0.5] (0 ~ 1) | フェードアウト効果が発動する確率。
| ☐ オーディオ感度 | [1] (0 ~ 4) | 音声レベルに対するカメラモーションの感度。
|  **ターゲット選択** || 
| ⊖ 頭 | [1] (0 ~ 1) | アクターの頭部をターゲットにする確率。
| ⊖ 胸 | [1] (0 ~ 1) | アクターの胸部をターゲットにする確率。
| ⊖ 中心 | [1] (0 ~ 1) | アクターの中央をターゲットにする確率。
| ⊖ 脚 | [0.5] (0 ~ 1) | アクターの脚をターゲットにする確率。
| ⊖ 足 | [0] (0 ~ 1) | アクターの足をターゲットにする確率。
|  **距離選択** || 
| ⊖ クローズアップ | [1] (0 ~ 1) | クローズアップ距離の確率。
| ⊖ ズームイン | [0.25] (0 ~ 1) | ズームインの確率。
| ⊖ ズームアウト | [0.25] (0 ~ 1) | ズームアウトの確率。
| ⊖ 中央 | [0.25] (0 ~ 1) | 中間距離の確率。
| ⊖ 遠く | [0.25] (0 ~ 1) | 遠距離の確率。
|  **パス選択** || 
| ⊖ ハイアングル | [20] (0 ~ 30) | カメラの最大上方向角度。
| ⊖ ローアングル | [-20] (-30 ~ 0) | カメラの最大下方向角度。
|  **向き** || 
| ⊖ 正面中央 | [1] (0 ~ 1) | カメラをアクターの正面中央に向ける確率。
| ⊖ 正面45度 | [0] (0 ~ 1) | アクターの正面45度角にカメラを向ける確率。
| ⊖ 側面90度 | [0.25] (0 ~ 1) | アクターの側面90度にカメラを向ける確率。
| ⊖ 背面135度 | [0] (0 ~ 1) | アクターの背面135度にカメラを向ける確率。
| ⊖ 背面180度 | [0.25] (0 ~ 1) | アクターの真後ろにカメラを向ける確率。
| ≡ プリセット | **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
