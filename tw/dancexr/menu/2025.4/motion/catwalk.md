---
locale: zh-rTW
layout: single
title: [走秀]
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/motion/catwalk) | [繁中](/tw/dancexr/menu/2025.4/motion/catwalk) | [日本語](/jp/dancexr/menu/2025.4/motion/catwalk) | [한국어](/kr/dancexr/menu/2025.4/motion/catwalk) | [简中](/zh/dancexr/menu/2025.4/motion/catwalk)

[程序化](../menu#程序化) > [走秀]



| Setting | Value | Description |
| :--- | --- | :--- |
| 指派給所有 || 0/17/False
| 指派給選定 || 1/17/False
| 指派給所有作為第二 || 2/17/False
| 指派給選定作為第二 || 3/17/False
| 擺動 | [15] (0 ~ 45) | 4/17/False
| 扭轉 | [5] (0 ~ 45) | 5/17/False
| 距離 | [18] (0 ~ 60) | 6/17/False
| 步高 | [0.05] (0 ~ 0.2) | 7/17/False
| 躯幹彎曲 | [0] (0 ~ 30) | 8/17/False
| 躯幹擺動 | [-0.5] (-1 ~ 1) | 9/17/False
| 躯幹扭轉 | [2] (-2 ~ 2) | 10/17/False
| 腳跟 | [0] (0 ~ 90) | 11/17/False
| 重疊 | [0.25] (0 ~ 2) | 12/17/False
| 曲線 | [0.35] (0 ~ 1) | 13/17/False
| 手部對稱 | ON | 14/17/False
| **左手** | | 15/17/False
| ├ (Gesture: Grab) || 0/18/True
| │ 手勢 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手部位置** | | 1/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手掌旋轉** | | 2/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 3/18/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 4/18/True
| ├ 鏡像左右 | OFF | 5/18/True
| ├ (Reference Actor: Self) || 6/18/True
| │ 參考演員 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: Hip) || 7/18/True
| │ 參考骨骼 | **臀部** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, (Align), 8/18/True
| ├ 側面選擇 | 自動 | 自動, 左, 右, 9/18/True
| ├ 混合範圍 | [0.75] (0 ~ 2) | 10/18/True
| ├ 對稱偏移 | [0] (-1 ~ 1) | 11/18/True
| ├ 使用配件位置 | ON | 12/18/True
| ├ **運動** | | 13/18/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **速度** | | 1/3/False
| │ │ ├ 每拍動作數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 每組動作數 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 曲線 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 變量速度 | OFF | 4/7/False
| │ │ ├ 模式 | (Gradual) | (Gradual), 隨機, 音量, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **自定義姿勢** | | 14/18/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 打開 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 拇指軸 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 拇指摺疊 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 拇指彎曲 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 食指彎曲 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指彎曲 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 無名指彎曲 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指彎曲 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 傳播 | [1] (0 ~ 1) | 9/10/False
| │ └ 混合 | [1] (0 ~ 1) | 10/10/False
| ├ 姿勢權重 | [1] (0 ~ 1) | 15/18/True
| ├ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 16/18/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 17/18/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 18/18/True
| └ 預設 | **臀部** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **右手** | | 16/17/False
| ├ (Gesture: Grab) || 0/18/True
| │ 手勢 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手部位置** | | 1/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手掌旋轉** | | 2/18/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 3/18/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 4/18/True
| ├ 鏡像左右 | OFF | 5/18/True
| ├ (Reference Actor: Self) || 6/18/True
| │ 參考演員 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: Hip) || 7/18/True
| │ 參考骨骼 | **臀部** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, (Align), 8/18/True
| ├ 側面選擇 | 自動 | 自動, 左, 右, 9/18/True
| ├ 混合範圍 | [0.75] (0 ~ 2) | 10/18/True
| ├ 對稱偏移 | [0] (-1 ~ 1) | 11/18/True
| ├ 使用配件位置 | ON | 12/18/True
| ├ **運動** | | 13/18/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **速度** | | 1/3/False
| │ │ ├ 每拍動作數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 每組動作數 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 曲線 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 變量速度 | OFF | 4/7/False
| │ │ ├ 模式 | (Gradual) | (Gradual), 隨機, 音量, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **自定義姿勢** | | 14/18/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 打開 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 拇指軸 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 拇指摺疊 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 拇指彎曲 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 食指彎曲 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指彎曲 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 無名指彎曲 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指彎曲 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 傳播 | [1] (0 ~ 1) | 9/10/False
| │ └ 混合 | [1] (0 ~ 1) | 10/10/False
| ├ 姿勢權重 | [1] (0 ~ 1) | 15/18/True
| ├ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 16/18/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 17/18/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 18/18/True
| └ 預設 | **臀部** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **圍繞行走** | | 17/17/False
| ├ 圍繞行走 | OFF | 0/1/False
| └ 半徑 | [2] (0 ~ 5) | 1/1/False
