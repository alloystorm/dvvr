---
locale: zh-rTW
layout: single
title: [自動攝影機]
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[程序化](../menu#程序化) > [自動攝影機]



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 指派給主體</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目標選擇</nobr>| **自動** | 自動, 已選擇, 群組, 旋轉, 旋轉 + 群組, 舞台中心,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 追踪模式</nobr>| **中心** | 中心, 頭部, 胸部,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標平滑</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 預測</nobr>| [1] (0 ~ 2) | 預測目標位置以減少因平滑造成的延遲
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 視場</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 節拍循環</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距離</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠距離</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用演員方向</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 種子</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入黑色</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B 機率</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 音頻靈敏度</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr> <b>目標選擇</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭部</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸部</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腿部</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr> <b>距離選擇</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 特寫</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 放大</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 縮小</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr> <b>路徑選擇</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr> <b>朝向</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 正中央</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方 45</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 側面 90</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 背面 135</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 背面 180</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1),  |
