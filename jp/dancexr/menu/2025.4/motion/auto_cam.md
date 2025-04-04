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



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>メインに割り当て</nobr>|| 
|<nobr>ターゲット選択</nobr>| **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|<nobr>トラッキングモード</nobr>| **センター** | センター, 頭, 胸,  |
|<nobr>ターゲットスムージング</nobr>| [0.5] (0 ~ 2) | 
|<nobr>予測</nobr>| [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|<nobr>FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>ビートサイクル</nobr>| [8] (1 ~ 16) | 
|<nobr>近距離</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr>遠距離</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr>アクターの向きを使用</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr>シード</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr>フェード・トゥ・ブラック</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr>F2B 確率</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr>オーディオ感度</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr><b>ターゲット選択</b></nobr>|| 
|<nobr>頭</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr>胸</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr>センター</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr>脚</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr>足</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr><b>距離選択</b></nobr>|| 
|<nobr>クローズアップ</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr>ズームイン</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr>ズームアウト</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr>中間</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr>遠方</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr><b>パス選択</b></nobr>|| 
|<nobr>高角度</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr>低角度</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr><b>オリエンテーション</b></nobr>|| 
|<nobr>前方中央</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr>前方 45</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr>横 90</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr>後方 135</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr>後方 180</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr>プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
