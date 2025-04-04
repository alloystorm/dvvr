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

(Automatic camera motion system that dynamically adjusts based on music beats, actor orientation, and configurable parameters for distance, target selection, and motion paths.)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> メインに割り当て</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> ターゲット選択</nobr>| **自動** | 自動, 選択されました, グループ, 回転, 回転 + グループ, ステージセンター,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> トラッキングモード</nobr>| **センター** | センター, 頭, 胸,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> ターゲットスムージング</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 予測</nobr>| [1] (0 ~ 2) | スムージングによる遅延を減少させるため、ターゲットの位置を予測
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> FOV</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> ビートサイクル</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距離</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠距離</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> アクターの向きを使用</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> シード</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> フェード・トゥ・ブラック</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B 確率</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> オーディオ感度</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr> <b>ターゲット選択</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> センター</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 脚</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 足</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr> <b>距離選択</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> クローズアップ</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> ズームイン</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> ズームアウト</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠方</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr> <b>パス選択</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr> <b>オリエンテーション</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方中央</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方 45</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 横 90</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 後方 135</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 後方 180</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> プリセット</nobr>| **デフォルト（リセット）** | デフォルト（リセット）, (Preset 1),  |
