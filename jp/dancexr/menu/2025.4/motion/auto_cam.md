---
locale: ja-rJP
layout: single
title: [オートカム]
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[プロシージャル](../menu#プロシージャル) > [オートカム]



[(Feature Page)](/jp/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> メインに割り当て|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ターゲット選択| **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> トラッキングモード| **センター** | センター, 頭, 胸,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲットスムージング| [0.5] (0 ~ 2) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 予測| [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> FOV| [30] (5 ~ 120) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ビートサイクル| [8] (1 ~ 16) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距離| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠距離| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> アクターの向きを使用| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> シード| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> フェード・トゥ・ブラック| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B 確率| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|  □ オーディオ感度| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|  <b>ターゲット選択</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> センター| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 脚| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 足| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|  <b>距離選択</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> クローズアップ| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ズームイン| [0.25] (0 ~ 1) | (Probability of zooming in.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> ズームアウト| [0.25] (0 ~ 1) | (Probability of zooming out.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠方| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|  <b>パス選択</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|  <b>オリエンテーション</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方中央| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方 45| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 横 90| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 後方 135| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 後方 180| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
