---
locale: zh-rCN
layout: single
title: [走台]
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/motion/catwalk) | [繁中](/tw/dancexr/menu/2025.4/motion/catwalk) | [日本語](/jp/dancexr/menu/2025.4/motion/catwalk) | [한국어](/kr/dancexr/menu/2025.4/motion/catwalk) | [简中](/zh/dancexr/menu/2025.4/motion/catwalk)

[程序化](../menu#程序化) > [走台]



| Setting | Value | Description |
| :--- | --- | :--- |
| 分配给所有 || 0/17/False
| 分配给所选 || 1/17/False
| 作为第二个分配给所有 || 2/17/False
| 作为第二个分配给所选 || 3/17/False
| 摆动 | [15] (0 ~ 45) | 4/17/False
| 扭转 | [5] (0 ~ 45) | 5/17/False
| 距离 | [18] (0 ~ 60) | 6/17/False
| 步高 | [0.05] (0 ~ 0.2) | 7/17/False
| 躯干弯曲 | [0] (0 ~ 30) | 8/17/False
| 躯干摆动 | [-0.5] (-1 ~ 1) | 9/17/False
| 躯干扭转 | [2] (-2 ~ 2) | 10/17/False
| 脚后跟 | [0] (0 ~ 90) | 11/17/False
| 重叠 | [0.25] (0 ~ 2) | 12/17/False
| 曲线 | [0.35] (0 ~ 1) | 13/17/False
| 双手对称 | ON | 14/17/False
| **左手** | | 15/17/False
| ├ (Gesture: Grab) || 0/18/True
| │ 手势 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手的位置** | | 1/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手部旋转** | | 2/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 3/18/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 4/18/True
| ├ 左右镜像 | OFF | 5/18/True
| ├ (Reference Actor: Self) || 6/18/True
| │ 参考演员 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: Hip) || 7/18/True
| │ 参考骨骼 | **臀部** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自动 | 自动, 正常, (Cylinder), 球体, (Align), 8/18/True
| ├ 侧面选择 | 自动 | 自动, 左, 右, 9/18/True
| ├ 混合范围 | [0.75] (0 ~ 2) | 10/18/True
| ├ 对称偏移 | [0] (-1 ~ 1) | 11/18/True
| ├ 使用附件位置 | ON | 12/18/True
| ├ **运动** | | 13/18/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **速度** | | 1/3/False
| │ │ ├ 每拍动作数 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 每组动作数 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 曲线 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 可变速度 | OFF | 4/7/False
| │ │ ├ 模式 | (Gradual) | (Gradual), 随机, 音量, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距离 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **自定义姿势** | | 14/18/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 打开 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 拇指轴 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 拇指折叠 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 拇指弯曲 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 食指弯曲 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指弯曲 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 无名指弯曲 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指弯曲 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 传播 | [1] (0 ~ 1) | 9/10/False
| │ └ 混合 | [1] (0 ~ 1) | 10/10/False
| ├ 姿势权重 | [1] (0 ~ 1) | 15/18/True
| ├ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 16/18/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 17/18/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 18/18/True
| └ 预设 | **臀部** | (Rest), 背面, 前面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **右手** | | 16/17/False
| ├ (Gesture: Grab) || 0/18/True
| │ 手势 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手的位置** | | 1/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手部旋转** | | 2/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 3/18/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 4/18/True
| ├ 左右镜像 | OFF | 5/18/True
| ├ (Reference Actor: Self) || 6/18/True
| │ 参考演员 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: Hip) || 7/18/True
| │ 参考骨骼 | **臀部** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自动 | 自动, 正常, (Cylinder), 球体, (Align), 8/18/True
| ├ 侧面选择 | 自动 | 自动, 左, 右, 9/18/True
| ├ 混合范围 | [0.75] (0 ~ 2) | 10/18/True
| ├ 对称偏移 | [0] (-1 ~ 1) | 11/18/True
| ├ 使用附件位置 | ON | 12/18/True
| ├ **运动** | | 13/18/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **速度** | | 1/3/False
| │ │ ├ 每拍动作数 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 每组动作数 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 曲线 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 可变速度 | OFF | 4/7/False
| │ │ ├ 模式 | (Gradual) | (Gradual), 随机, 音量, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距离 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **自定义姿势** | | 14/18/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 打开 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 拇指轴 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 拇指折叠 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 拇指弯曲 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 食指弯曲 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指弯曲 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 无名指弯曲 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指弯曲 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 传播 | [1] (0 ~ 1) | 9/10/False
| │ └ 混合 | [1] (0 ~ 1) | 10/10/False
| ├ 姿势权重 | [1] (0 ~ 1) | 15/18/True
| ├ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 16/18/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 17/18/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 18/18/True
| └ 预设 | **臀部** | (Rest), 背面, 前面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **圆周行走** | | 17/17/False
| ├ 圆周行走 | OFF | 0/1/False
| └ 半径 | [2] (0 ~ 5) | 1/1/False
