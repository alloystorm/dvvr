---
locale: zh-rCN
layout: single
title: [自动摄像机]
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[程序化](../menu#程序化) > [自动摄像机]



[(Feature Page)](/zh/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 分配给主对象|| 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目标选择| **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 跟踪模式| **中心** | 中心, 头部, 胸部,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标平滑| [0.5] (0 ~ 2) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 预测| [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 视场| [30] (5 ~ 120) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 节拍循环| [8] (1 ~ 16) | 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距离| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 远距离| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用角色朝向| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 种子| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入黑色| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入概率| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|  □ 音频灵敏度| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|  <b>目标选择</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 头部| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸部| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 腿| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 脚| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|  <b>距离选择</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 特写| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 放大| [0.25] (0 ~ 1) | (Probability of zooming in.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 缩小| [0.25] (0 ~ 1) | (Probability of zooming out.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 中间| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 远| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|  <b>路径选择</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|  <b>方向</b>|| 
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 前中央| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 前45度| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 侧面90度| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 后135度| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 后180度| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| <img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **默认（重置）** | 默认（重置）, (Preset 1),  |
