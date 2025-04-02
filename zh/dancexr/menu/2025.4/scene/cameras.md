---
locale: zh-rCN
layout: single
title: (Camera: [Freefly Cam])
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/scene/cameras) | [繁中](/tw/dancexr/menu/2025.4/scene/cameras) | [日本語](/jp/dancexr/menu/2025.4/scene/cameras) | [한국어](/kr/dancexr/menu/2025.4/scene/cameras) | [简中](/zh/dancexr/menu/2025.4/scene/cameras)

[环境](../menu#环境) > (Camera: [Freefly Cam])



| Setting | Value | Description |
| :--- | --- | :--- |
| [自由飞行相机] || 
|**[自由飞行相机]** | | 
| 目标选择 | **自动**, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |  |
| 跟踪模式 | **中心**, 头部, 胸部,  |  |
|- 目标平滑 | [0.5] (0 ~ 2) | 
|- 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| 锁定目标 | OFF | 自动聚焦目标
|- 相机抖动 | [0.5] (0 ~ 1) | 
| 锁定旋转 | OFF | 相机跟随目标的旋转
|- 自动缩放 | [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
|- 缩放速度 | [0.5] (0 ~ 1) | 缩放到目标视场所需的时间
|- 目标处的视场高度 | [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
|- 垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
|- 视场 | [30] (5 ~ 120) | 
|- 节拍循环 | [8] (1 ~ 16) | 
| 使用轨道移动 | OFF | (Enable or disable orbit movement, allowing the camera to rotate around a central point.)
| 预设 | **(Freefly)**, (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |  |
| [轨道摄像机] || 
|**[轨道摄像机]** | | 
| 目标选择 | **自动**, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |  |
| 跟踪模式 | **中心**, 头部, 胸部,  |  |
|- 目标平滑 | [0.5] (0 ~ 2) | 
|- 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
|- 视场 | [30] (5 ~ 120) | 
|- 节拍循环 | [8] (1 ~ 16) | 
| 使用控制器输入 | OFF | 
| 防止低于地面 | ON | 
| 保持速度 | OFF | 在没有输入时保持旋转
|- 最大速度 | [15] (0 ~ 30) | 最大旋转速度
|- 最小速度 | [0] (0 ~ 30) | 最小旋转速度
| 自动模式 | OFF | 
|- 最小距离 | [1] (0 ~ 10) | 
|- 最大距离 | [3] (1 ~ 10) | 
|- 距离循环 | [12] ((Unlimited)) | 
|- 最小俯仰 | [-15] (-45 ~ 0) | 
|- 最大俯仰 | [15] (0 ~ 45) | 
|- 俯仰循环 | [32] ((Unlimited)) | 
|- 最小高度 | [0] (-1 ~ 0) | 
|- 最大高度 | [0.5] (0 ~ 1) | 
|- 高度循环 | [32] ((Unlimited)) | 
|- 速度 | [10] (0 ~ 90) | 
| 预设 | **默认（重置）**, (Preset 1),  |  |
| [自动摄像机] || 
|**[自动摄像机]** | | 
| 目标选择 | **自动**, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |  |
| 跟踪模式 | **中心**, 头部, 胸部,  |  |
|- 目标平滑 | [0.5] (0 ~ 2) | 
|- 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
|- 视场 | [30] (5 ~ 120) | 
|- 节拍循环 | [8] (1 ~ 16) | 
|- 近距离 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|- 远距离 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| 使用角色朝向 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
|- 种子 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|- 淡入黑色 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|- 淡入概率 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|- 音频灵敏度 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
| 目标选择 || 
|- 头部 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|- 胸部 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|- 中心 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|- 腿 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|- 脚 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
| 距离选择 || 
|- 特写 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|- 放大 | [0.25] (0 ~ 1) | (Probability of zooming in.)
|- 缩小 | [0.25] (0 ~ 1) | (Probability of zooming out.)
|- 中间 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|- 远 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
| 路径选择 || 
|- 高角度 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|- 低角度 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
| 方向 || 
|- 前中央 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|- 前45度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|- 侧面90度 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|- 后135度 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|- 后180度 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| 预设 | **默认（重置）**, (Preset 1),  |  |
| [长镜头] || 
|**[长镜头]** | | 
| 目标选择 | **自动**, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |  |
| 跟踪模式 | **中心**, 头部, 胸部,  |  |
|- 目标平滑 | [0.5] (0 ~ 2) | 
|- 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
|- 视场 | [30] (5 ~ 120) | 
|- 节拍循环 | [8] (1 ~ 16) | 
|- 旋转范围 | [60] (0 ~ 180) | 水平旋转范围。
|- 距离 | [0.5] (0.2 ~ 5) | 
|- 俯仰角 | [-15] (-90 ~ 90) | 
|- 曲线 | [0] (-1 ~ 1) | 更改运动时使用的缓动曲线
| 防止低于地面 | ON | 
| 使用角色朝向 | ON | 
| 靠近时提高焦点 | OFF | 距离变小时向上移动焦点位置
| 预设 | **默认（重置）**, (Preset 1), (Preset 2), (Preset 3),  |  |
| [第一人称] || 
|**[第一人称]** | | 
| 选择角色 |  |  |
|- 视野 | [45] (30 ~ 100) | 
|- 近裁剪距离 | [0.15] (0 ~ 0.3) | 
| 控制角色移动 | ON | 
| 在虚拟现实中控制手部 | ON | 
|- 移除滚转 | [1] (0 ~ 1) | 
|- 稳定器 | [5] (0 ~ 20) | 
|- 阻尼 | [0.1] (0 ~ 1) | 
| 禁用自动返回 | OFF | 
| 重新居中 || 
| [固定摄影机] || 
|**[固定摄影机]** | | 
| 目标选择 | **自动**, 已选择, 组, 旋转, 旋转 + 组, 舞台中心,  |  |
| 跟踪模式 | **中心**, 头部, 胸部,  |  |
|- 目标平滑 | [0.5] (0 ~ 2) | 
|- 预测 | [1] (0 ~ 2) | 预测目标的位置以减少平滑造成的延迟
| 锁定目标 | OFF | 自动聚焦目标
|- 相机抖动 | [0.5] (0 ~ 1) | 
| 锁定旋转 | OFF | 相机跟随目标的旋转
|- 自动缩放 | [0] (0 ~ 1) | 自动缩放以保持目标在视野中的大小
|- 缩放速度 | [0.5] (0 ~ 1) | 缩放到目标视场所需的时间
|- 目标处的视场高度 | [1] (0.2 ~ 2) | 使用自动缩放时目标的垂直高度
|- 垂直偏移 | [0] (-1 ~ 1) | 垂直偏移
|- 视场 | [10] (5 ~ 120) | 
|- 节拍循环 | [8] (1 ~ 16) | 
|- 大小 | [1] (0 ~ 2) | 
|- 偏移 | [0] (-1 ~ 1) | 
|- 目标中心 | [0] (-1 ~ 1) | 
| 偏移 || 
|- (X) | [0] (-2 ~ 2) | 
|- (Y) | [0] (-2 ~ 2) | 
|- (Z) | [0] (-2 ~ 2) | 
| 预设 | 近, **远**,  |  |
| 配置 || 
| [配置摄影机](#配置摄影机) |


### **配置摄影机**



| Setting | Value | Description |
| :--- | --- | :--- |
|- 高度偏移 | [0] (-5 ~ 5) | 
|- 视场缩放 | [1] (0.25 ~ 2) | 
|- 肖像模式缩放 | [1.2] (1 ~ 2) | 
|- 旋转过滤器 | 无旋转, 仅方向, **完全旋转**,  | 
|- 近裁剪 | [0.01] (0 ~ 0.5) | 
| 运动变化时重置 | ON | 
| 重置偏移 || 
