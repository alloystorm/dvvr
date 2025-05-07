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



[(Feature Page)](/tw/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 指派給主體|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目標選擇| **自動** | 自動, 已選擇, 群組, 旋轉, 旋轉 + 群組, 舞台中心,  |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 追踪模式| **中心** | 中心, 頭部, 胸部,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標平滑| [0.5] (0 ~ 2) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 預測| [1] (0 ~ 2) | 預測目標位置以減少因平滑造成的延遲
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 視場| [30] (5 ~ 120) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 節拍循環| [8] (1 ~ 16) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距離| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠距離| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用演員方向| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 種子| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入黑色| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B 機率| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|  □ 音頻靈敏度| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|  <b>目標選擇</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭部| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸部| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 腿部| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|  <b>距離選擇</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 特寫| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 放大| [0.25] (0 ~ 1) | (Probability of zooming in.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 縮小| [0.25] (0 ~ 1) | (Probability of zooming out.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 中間| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 遠| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|  <b>路徑選擇</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|  <b>朝向</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 正中央| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 前方 45| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 側面 90| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 背面 135| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 背面 180| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| <img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **預設 (重置)** | 預設 (重置), (Preset 1),  |
