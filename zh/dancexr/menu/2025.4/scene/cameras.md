---
locale: zh-rCN
layout: single
title: 摄像机
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[环境](../menu#环境) > 摄像机



| Setting | Value | Description |
| :--- | --- | :--- |
| [自由飞行相机] || 
| └&nbsp;**[自由飞行相机]** | | 
| &nbsp;&nbsp;├&nbsp;(Target Select: Auto) || 
| &nbsp;&nbsp;│&nbsp;目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| &nbsp;&nbsp;├&nbsp;(Tracking Mode: Center) || 
| &nbsp;&nbsp;│&nbsp;跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| &nbsp;&nbsp;├&nbsp;目标平滑 | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| &nbsp;&nbsp;├&nbsp;锁定目标 | OFF | 自动聚焦目标
| &nbsp;&nbsp;├&nbsp;相机抖动 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;锁定旋转 | OFF | 相机跟随目标的旋转
| &nbsp;&nbsp;├&nbsp;自动缩放 | [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
| &nbsp;&nbsp;├&nbsp;缩放速度 | [0.5] (0 ~ 1) | 缩放到目标视场所需的时间
| &nbsp;&nbsp;├&nbsp;目标处的视场高度 | [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
| &nbsp;&nbsp;├&nbsp;垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
| &nbsp;&nbsp;├&nbsp;视场 | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;节拍循环 | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;使用轨道移动 | OFF | (Enable or disable orbit movement, allowing the camera to rotate around a central point.)
| &nbsp;&nbsp;└&nbsp;(Presets: Freefly) || 
| &nbsp;&nbsp;&nbsp;&nbsp;预设 | **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
| [轨道摄像机] || 
| └&nbsp;**[轨道摄像机]** | | 
| &nbsp;&nbsp;├&nbsp;(Target Select: Auto) || 
| &nbsp;&nbsp;│&nbsp;目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| &nbsp;&nbsp;├&nbsp;(Tracking Mode: Center) || 
| &nbsp;&nbsp;│&nbsp;跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| &nbsp;&nbsp;├&nbsp;目标平滑 | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| &nbsp;&nbsp;├&nbsp;视场 | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;节拍循环 | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;使用控制器输入 | OFF | 
| &nbsp;&nbsp;├&nbsp;防止低于地面 | ON | 
| &nbsp;&nbsp;├&nbsp;保持速度 | OFF | 在没有输入时保持旋转
| &nbsp;&nbsp;├&nbsp;最大速度 | [15] (0 ~ 30) | 最大旋转速度
| &nbsp;&nbsp;├&nbsp;最小速度 | [0] (0 ~ 30) | 最小旋转速度
| &nbsp;&nbsp;├&nbsp;自动模式 | OFF | 
| &nbsp;&nbsp;├&nbsp;最小距离 | [1] (0 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;最大距离 | [3] (1 ~ 10) | 
| &nbsp;&nbsp;├&nbsp;距离循环 | [12] ((Unlimited)) | 
| &nbsp;&nbsp;├&nbsp;最小俯仰 | [-15] (-45 ~ 0) | 
| &nbsp;&nbsp;├&nbsp;最大俯仰 | [15] (0 ~ 45) | 
| &nbsp;&nbsp;├&nbsp;俯仰循环 | [32] ((Unlimited)) | 
| &nbsp;&nbsp;├&nbsp;最小高度 | [0] (-1 ~ 0) | 
| &nbsp;&nbsp;├&nbsp;最大高度 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;高度循环 | [32] ((Unlimited)) | 
| &nbsp;&nbsp;├&nbsp;速度 | [10] (0 ~ 90) | 
| &nbsp;&nbsp;└&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;&nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1),  |
| [自动摄像机] || 
| └&nbsp;**[自动摄像机]** | | 
| &nbsp;&nbsp;├&nbsp;(Target Select: Auto) || 
| &nbsp;&nbsp;│&nbsp;目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| &nbsp;&nbsp;├&nbsp;(Tracking Mode: Center) || 
| &nbsp;&nbsp;│&nbsp;跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| &nbsp;&nbsp;├&nbsp;目标平滑 | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| &nbsp;&nbsp;├&nbsp;视场 | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;节拍循环 | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;近距离 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| &nbsp;&nbsp;├&nbsp;远距离 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| &nbsp;&nbsp;├&nbsp;使用角色朝向 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
| &nbsp;&nbsp;├&nbsp;种子 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| &nbsp;&nbsp;├&nbsp;淡入黑色 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| &nbsp;&nbsp;├&nbsp;淡入概率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
| &nbsp;&nbsp;├&nbsp;音频灵敏度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
| &nbsp;&nbsp;├&nbsp;目标选择 || 
| &nbsp;&nbsp;├&nbsp;头部 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| &nbsp;&nbsp;├&nbsp;胸部 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| &nbsp;&nbsp;├&nbsp;中心 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| &nbsp;&nbsp;├&nbsp;腿 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| &nbsp;&nbsp;├&nbsp;脚 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
| &nbsp;&nbsp;├&nbsp;距离选择 || 
| &nbsp;&nbsp;├&nbsp;特写 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| &nbsp;&nbsp;├&nbsp;放大 | [0.25] (0 ~ 1) | (Probability of zooming in.)
| &nbsp;&nbsp;├&nbsp;缩小 | [0.25] (0 ~ 1) | (Probability of zooming out.)
| &nbsp;&nbsp;├&nbsp;中间 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| &nbsp;&nbsp;├&nbsp;远 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
| &nbsp;&nbsp;├&nbsp;路径选择 || 
| &nbsp;&nbsp;├&nbsp;高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| &nbsp;&nbsp;├&nbsp;低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
| &nbsp;&nbsp;├&nbsp;方向 || 
| &nbsp;&nbsp;├&nbsp;前中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| &nbsp;&nbsp;├&nbsp;前45度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| &nbsp;&nbsp;├&nbsp;侧面90度 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| &nbsp;&nbsp;├&nbsp;后135度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| &nbsp;&nbsp;├&nbsp;后180度 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| &nbsp;&nbsp;└&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;&nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1),  |
| [长镜头] || 
| └&nbsp;**[长镜头]** | | 
| &nbsp;&nbsp;├&nbsp;(Target Select: Auto) || 
| &nbsp;&nbsp;│&nbsp;目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| &nbsp;&nbsp;├&nbsp;(Tracking Mode: Center) || 
| &nbsp;&nbsp;│&nbsp;跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| &nbsp;&nbsp;├&nbsp;目标平滑 | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| &nbsp;&nbsp;├&nbsp;视场 | [30] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;节拍循环 | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;旋转范围 | [60] (0 ~ 180) | 水平旋转范围。
| &nbsp;&nbsp;├&nbsp;距离 | [0.5] (0.2 ~ 5) | 
| &nbsp;&nbsp;├&nbsp;俯仰角 | [-15] (-90 ~ 90) | 
| &nbsp;&nbsp;├&nbsp;曲线 | [0] (-1 ~ 1) | 更改运动时使用的缓动曲线
| &nbsp;&nbsp;├&nbsp;防止低于地面 | ON | 
| &nbsp;&nbsp;├&nbsp;使用角色朝向 | ON | 
| &nbsp;&nbsp;├&nbsp;靠近时提高焦点 | OFF | 距离变小时向上移动焦点位置
| &nbsp;&nbsp;└&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;&nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3),  |
| [第一人称] || 
| └&nbsp;**[第一人称]** | | 
| &nbsp;&nbsp;├&nbsp;选择角色 || 
| &nbsp;&nbsp;│&nbsp;选择角色 |  |  |
| &nbsp;&nbsp;├&nbsp;视野 | [45] (30 ~ 100) | 
| &nbsp;&nbsp;├&nbsp;近裁剪距离 | [0.15] (0 ~ 0.3) | 
| &nbsp;&nbsp;├&nbsp;控制角色移动 | ON | 
| &nbsp;&nbsp;├&nbsp;在虚拟现实中控制手部 | ON | 
| &nbsp;&nbsp;├&nbsp;移除滚转 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;稳定器 | [5] (0 ~ 20) | 
| &nbsp;&nbsp;├&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;禁用自动返回 | OFF | 
| &nbsp;&nbsp;└&nbsp;重新居中 || 
| [固定摄影机] || 
| └&nbsp;**[固定摄影机]** | | 
| &nbsp;&nbsp;├&nbsp;(Target Select: Auto) || 
| &nbsp;&nbsp;│&nbsp;目标选择 | **自动** | 自动, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |
| &nbsp;&nbsp;├&nbsp;(Tracking Mode: Center) || 
| &nbsp;&nbsp;│&nbsp;跟踪模式 | **中心** | 中心, 头部, 胸部,  |
| &nbsp;&nbsp;├&nbsp;目标平滑 | [0.5] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| &nbsp;&nbsp;├&nbsp;锁定目标 | OFF | 自动聚焦目标
| &nbsp;&nbsp;├&nbsp;相机抖动 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;锁定旋转 | OFF | 相机跟随目标的旋转
| &nbsp;&nbsp;├&nbsp;自动缩放 | [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
| &nbsp;&nbsp;├&nbsp;缩放速度 | [0.5] (0 ~ 1) | 缩放到目标视场所需的时间
| &nbsp;&nbsp;├&nbsp;目标处的视场高度 | [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
| &nbsp;&nbsp;├&nbsp;垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
| &nbsp;&nbsp;├&nbsp;视场 | [10] (5 ~ 120) | 
| &nbsp;&nbsp;├&nbsp;节拍循环 | [8] (1 ~ 16) | 
| &nbsp;&nbsp;├&nbsp;大小 | [1] (0 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;偏移 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;目标中心 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;偏移 || 
| &nbsp;&nbsp;├&nbsp;(X) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;(Y) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;(Z) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;└&nbsp;(Presets: Far) || 
| &nbsp;&nbsp;&nbsp;&nbsp;预设 | **远** | 近, 远,  |
| 配置 || 
| [配置摄影机](config_camera) |
