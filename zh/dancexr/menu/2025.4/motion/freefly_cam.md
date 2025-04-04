---
locale: zh-rCN
layout: single
title: [自由飞行相机]
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/motion/freefly_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/freefly_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/freefly_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/freefly_cam) | [简中](/zh/dancexr/menu/2025.4/motion/freefly_cam)

[程序化](../menu#程序化) > [自由飞行相机]

(Provides a free-fly camera mode where the user has full control over camera movement and rotation. The camera can move forward, backward, up, down, and rotate or tilt based on user input. Additional options include orbit movement and vertical movement restriction.)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 分配给主对象</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目标选择</nobr>| **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 跟踪模式</nobr>| **中心** | 中心, 头部, 胸部,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标平滑</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 预测</nobr>| [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 锁定目标</nobr>| [OFF] | 自动聚焦目标
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 相机抖动</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 锁定旋转</nobr>| [OFF] | 相机跟随目标的旋转
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 自动缩放</nobr>| [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 缩放速度</nobr>| [0.5] (0 ~ 1) | 缩放到目标视场所需的时间
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标处的视场高度</nobr>| [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 垂直偏移</nobr>| [0] (-1 ~ 1) | 垂直偏移
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 视场</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 节拍循环</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 使用轨道移动</nobr>| [OFF] | (Enable or disable orbit movement, allowing the camera to rotate around a central point.)
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
