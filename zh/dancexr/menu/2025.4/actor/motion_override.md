---
locale: zh-rCN
layout: single
title: 动作重写
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[专业版](../menu#专业版) > 动作重写



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Motion Override) | OFF | 0/8/True
| **身体** | | 1/8/True
| ├ 位置 | 自由 | 自由, 锁定水平, 锁定垂直, 锁定位置, 0/13/False
| ├ 旋转 | 自由 | 自由, 锁定旋转, 1/13/False
| ├ 阻尼 | [0.5] (0 ~ 1) | 2/13/False
| ├ 倾斜 | [0] (-45 ~ 90) | 3/13/False
| ├ 弯曲 | [0] (-150 ~ 150) | 4/13/False
| ├ 扭转 | [0] (-90 ~ 90) | 5/13/False
| ├ 头部 | [0] (-90 ~ 90) | 6/13/False
| ├ 高度 | [0] (-1 ~ 1) | 7/13/False
| ├ 前进/后退 | [0] (-1 ~ 1) | 8/13/False
| ├ 距离 | OFF | 9/13/False
| ├ 目标角色 || 10/13/False
| │ 目标角色 |  |  |
| ├ 检测范围 | [2] (0 ~ 10) | 11/13/False
| ├ 最小距离 | [0.5] (0 ~ 1) | 12/13/False
| └ 最大距离 | [1] (0.5 ~ 2) | 13/13/False
| **摇摆动作** | | 2/8/True
| ├ (Enable Rocking Motion) | ON | 0/8/False
| ├ **速度** | | 1/8/False
| │ ├ 每拍动作数 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ ├ 每组动作数 | [8] (4 ~ 32) | 1/7/False
| │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ ├ 曲线 | [0] (0 ~ 1) | 3/7/False
| │ ├ 可变速度 | OFF | 4/7/False
| │ ├ 模式 | (Gradual) | (Gradual), 随机, 音量, 5/7/False
| │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| ├ 摇摆角度 | [30] (0 ~ 60) | 2/8/False
| ├ 上下 | [0.1] (0 ~ 0.3) | 3/8/False
| ├ 前后 | [0.1] (0 ~ 0.3) | 4/8/False
| ├ 深度变化 | [0.1] (0 ~ 0.3) | 5/8/False
| ├ 深度最大 | [0.15] (0 ~ 0.3) | 6/8/False
| ├ 深度额外 | [0] (-0.1 ~ 0.1) | 7/8/False
| └ 脚部动作 | [0] (-1 ~ 1) | 8/8/False
| **头部姿势** | | 3/8/True
| ├ (Enable Head Pose) | OFF | 0/3/False
| ├ 旋转 X | [0] (-90 ~ 90) | 1/3/False
| ├ 旋转 Y | [0] (-90 ~ 90) | 2/3/False
| └ 旋转 Z | [0] (-90 ~ 90) | 3/3/False
| **腿部姿势** | | 4/8/True
| ├ (Enable Leg Pose) | ON | 0/5/True
| ├ 相对于地面 | ON | 1/5/True
| ├ 最大扭转 | [60] (0 ~ 90) | 2/5/True
| ├ 对称的 | ON | 3/5/True
| ├ **左** | | 4/5/True
| │ ├ 打开 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 脚 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 脚 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 脚 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 脚旋转 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 脚旋转 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 脚旋转 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 脚趾 | [0] (-180 ~ 180) | 7/7/False
| ├ **右** | | 5/5/True
| │ ├ 打开 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 脚 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 脚 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 脚 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 脚旋转 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 脚旋转 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 脚旋转 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 脚趾 | [0] (-180 ~ 180) | 7/7/False
| └ 预设 | **(Ride)** | (Sit), (Ride), (Kneel), (Stand),  |
| 双手对称 | ON | 5/8/True
| **左手** | | 6/8/True
| ├ (Enable Left Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 手势 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手的位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手部旋转** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 4/19/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 5/19/True
| ├ 左右镜像 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 参考演员 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 参考骨骼 | **无** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自动 | 自动, 正常, (Cylinder), 球体, (Align), 9/19/True
| ├ 侧面选择 | 自动 | 自动, 左, 右, 10/19/True
| ├ 混合范围 | [0.75] (0 ~ 2) | 11/19/True
| ├ 对称偏移 | [0] (-1 ~ 1) | 12/19/True
| ├ 使用附件位置 | ON | 13/19/True
| ├ **运动** | | 14/19/True
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
| ├ **自定义姿势** | | 15/19/True
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
| ├ 姿势权重 | [1] (0 ~ 1) | 16/19/True
| ├ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 预设 | **(Rest)** | (Rest), 背面, 前面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **右手** | | 7/8/True
| ├ (Enable Right Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 手势 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手的位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手部旋转** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 4/19/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 5/19/True
| ├ 左右镜像 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 参考演员 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 参考骨骼 | **无** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自动 | 自动, 正常, (Cylinder), 球体, (Align), 9/19/True
| ├ 侧面选择 | 自动 | 自动, 左, 右, 10/19/True
| ├ 混合范围 | [0.75] (0 ~ 2) | 11/19/True
| ├ 对称偏移 | [0] (-1 ~ 1) | 12/19/True
| ├ 使用附件位置 | ON | 13/19/True
| ├ **运动** | | 14/19/True
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
| ├ **自定义姿势** | | 15/19/True
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
| ├ 姿势权重 | [1] (0 ~ 1) | 16/19/True
| ├ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 预设 | **(Rest)** | (Rest), 背面, 前面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **骑行模型** | | 8/8/True
| ├ (Enable Ride Model) | ON | 0/14/False
| ├ (Model: [Hoverbike]) || 1/14/False
| │ 模型 | **([Hoverbike])** | ([Hoverbike]), ([Rocking Horse]),  |
| ├ 加速度 | [10] (0 ~ 20) | 2/14/False
| ├ 拖拽 | [0.05] (0 ~ 1) | 3/14/False
| ├ 转弯时倾斜 | [0.5] (0 ~ 1) | 4/14/False
| ├ 位置 || 5/14/False
| ├ (X) | [0] (-1 ~ 1) | 6/14/False
| ├ (Y) | [0] (-1 ~ 1) | 7/14/False
| ├ (Z) | [0] (-1 ~ 1) | 8/14/False
| ├ 旋转 || 9/14/False
| ├ (X) | [0] (-90 ~ 90) | 10/14/False
| ├ (Y) | [0] (-90 ~ 90) | 11/14/False
| ├ (Z) | [0] (-90 ~ 90) | 12/14/False
| ├ 缩放 | [0] (-5 ~ 5) | 13/14/False
| └ 粒子效果 | ON | 14/14/False
| 预设 | **自由** | 自由, 摇摆动作, 悬浮摩托车, 摇摆马, 杆运动, 杆混合,  |
