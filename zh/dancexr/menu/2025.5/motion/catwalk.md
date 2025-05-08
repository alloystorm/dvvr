---
locale: zh-rCN
layout: single
title: [Catwalk]
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.5/motion/catwalk) | [繁中](/tw/dancexr/menu/2025.5/motion/catwalk) | [日本語](/jp/dancexr/menu/2025.5/motion/catwalk) | [한국어](/kr/dancexr/menu/2025.5/motion/catwalk) | [简中](/zh/dancexr/menu/2025.5/motion/catwalk)

[程序化](../menu#程序化) > [Catwalk]

跟随音乐节拍的程序化舞台走秀动作。

## 配置

| 设置 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 分配给所有 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 分配给选中 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 分配给所有作为第二动作 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 分配给选中作为第二动作 || 
| ⊖ 摆动 | [15] (0 ~ 45) | 臀部左右摆动。
| ⊖ 扭转 | [5] (0 ~ 45) | 躯干扭转。
| ⊖ 距离 | [18] (0 ~ 60) | 腿部动作角度。
| ⊖ 步高 | [0.05] (0 ~ 0.2) | 步高。
| ⊖ 躯干弯曲 | [0] (0 ~ 30) | 腿部弯曲。
| ⊖ 躯干摆动 | [-0.5] (-1 ~ 1) | 
| ⊖ 躯干扭转 | [2] (-2 ~ 2) | 
| ⊖ 脚跟 | [0] (0 ~ 90) | 
| ⊖ 重叠 | [0.25] (0 ~ 2) | 脚步重叠。
| ⊖ 曲线 | [0.35] (0 ~ 1) | 
| ☑ 双手对称 | [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **左手** | | 
| ├─> 手势 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部位置** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部旋转** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─☑ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 
| ├─⊖ 肘部方向 | [0] (-180 ~ 180) | 
| ├─☐ 左右镜像 | [OFF] | 
| ├─> 参考角色 | **(Partner)** | (Self), (Partner), (Closest),  |
| ├─> 参考骨骼 | **臀部** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├─☑ 逆向运动学模式 | 自动 | 自动, 正常, (Cylinder), 球体, 对齐, 
| ├─☑ 侧面选择 | 自动 | 自动, 左侧, 右侧, 
| ├─⊖ 混合范围 | [0.75] (0 ~ 2) | 
| ├─⊖ 对称偏移 | [0] (-1 ~ 1) | 
| ├─☑ 使用附件位置 | [ON] | 
| ├─☐ **动作** | | 
| │ ├─☐ 启用 | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **速度** | | 
| │ │ ├─☑ 每拍移动次数 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| │ │ ├─⊖ 每组移动次数 | [8] (4 ~ 32) | 
| │ │ ├─⊖ 相位 | [0] (0 ~ 1) | 
| │ │ ├─⊖ 曲线 | [0] (0 ~ 1) | 
| │ │ ├─☐ 可变速度 | [OFF] | 
| │ │ ├─☑ 模式 | (Gradual) | (Gradual), 随机, 音量, 
| │ │ ├─☑ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| │ │ └─☑ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 
| │ ├─⊖ 距离 | [0.1] (0 ~ 0.3) | 
| │ └─⊖ 角度 | [0] (-60 ~ 60) | 
| ├─☐ **自定义姿势** | | 
| │ ├─☐ 启用 | [OFF] | 
| │ ├─⊖ 打开 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指轴线 | [90] (-360 ~ 360) | 
| │ ├─⊖ 拇指折叠 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 食指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 中指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 无名指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 小指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 传播 | [1] (0 ~ 1) | 
| │ └─⊖ 混合 | [1] (0 ~ 1) | 
| ├─⊖ 姿势权重 | [1] (0 ~ 1) | 
| ├─⊖ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 
| ├─⊖ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 
| ├─⊖ (Grab Axis) | [0] (-180 ~ 180) | 
| └─≡ 预设 | **臀部** | (Rest), 背面, 正面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **右手** | | 
| ├─> 手势 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 点, (Middle Finger), (Thumb Up), (Grab),  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部位置** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部旋转** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─☑ 旋转类型 | 相对于参考骨骼 | 相对于参考骨骼, 相对于自身, 绝对旋转, 无旋转, 
| ├─⊖ 肘部方向 | [0] (-180 ~ 180) | 
| ├─☐ 左右镜像 | [OFF] | 
| ├─> 参考角色 | **(Partner)** | (Self), (Partner), (Closest),  |
| ├─> 参考骨骼 | **臀部** | 无, 臀部, 胸部, 头部, 中心, 杆, (Upperarm), (Forearm), 手, 腿, 膝盖, 脚, 腹部, 胸部, (Pussy), (Dick),  |
| ├─☑ 逆向运动学模式 | 自动 | 自动, 正常, (Cylinder), 球体, 对齐, 
| ├─☑ 侧面选择 | 自动 | 自动, 左侧, 右侧, 
| ├─⊖ 混合范围 | [0.75] (0 ~ 2) | 
| ├─⊖ 对称偏移 | [0] (-1 ~ 1) | 
| ├─☑ 使用附件位置 | [ON] | 
| ├─☐ **动作** | | 
| │ ├─☐ 启用 | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **速度** | | 
| │ │ ├─☑ 每拍移动次数 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| │ │ ├─⊖ 每组移动次数 | [8] (4 ~ 32) | 
| │ │ ├─⊖ 相位 | [0] (0 ~ 1) | 
| │ │ ├─⊖ 曲线 | [0] (0 ~ 1) | 
| │ │ ├─☐ 可变速度 | [OFF] | 
| │ │ ├─☑ 模式 | (Gradual) | (Gradual), 随机, 音量, 
| │ │ ├─☑ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| │ │ └─☑ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 
| │ ├─⊖ 距离 | [0.1] (0 ~ 0.3) | 
| │ └─⊖ 角度 | [0] (-60 ~ 60) | 
| ├─☐ **自定义姿势** | | 
| │ ├─☐ 启用 | [OFF] | 
| │ ├─⊖ 打开 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指轴线 | [90] (-360 ~ 360) | 
| │ ├─⊖ 拇指折叠 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 食指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 中指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 无名指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 小指弯曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 传播 | [1] (0 ~ 1) | 
| │ └─⊖ 混合 | [1] (0 ~ 1) | 
| ├─⊖ 姿势权重 | [1] (0 ~ 1) | 
| ├─⊖ 抓取距离 | [0.015] (-0.1 ~ 0.1) | 
| ├─⊖ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 
| ├─⊖ (Grab Axis) | [0] (-180 ~ 180) | 
| └─≡ 预设 | **臀部** | (Rest), 背面, 正面, 臀部, 头部, 杆, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **圆圈行走** | | 
| ├─☐ 圆圈行走 | [OFF] | 
| └─⊖ 半径 | [2] (0 ~ 5) | 
