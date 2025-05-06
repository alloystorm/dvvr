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



[(Feature Page)](/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 分配给主对象</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目标选择</nobr>| **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 跟踪模式</nobr>| **中心** | 中心, 头部, 胸部,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标平滑</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 预测</nobr>| [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 视场</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 节拍循环</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 近距离</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 远距离</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用角色朝向</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 种子</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入黑色</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 淡入概率</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 音频灵敏度</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr> <b>目标选择</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 头部</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 胸部</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腿</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 脚</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr> <b>距离选择</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 特写</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 放大</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 缩小</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中间</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 远</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr> <b>路径选择</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高角度</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 低角度</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr> <b>方向</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前中央</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前45度</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 侧面90度</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 后135度</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 后180度</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1),  |
