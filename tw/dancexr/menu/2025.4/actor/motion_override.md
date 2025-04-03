---
locale: zh-rTW
layout: single
title: 動作覆蓋
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[專業版](../menu#專業版) > 動作覆蓋



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Motion Override) | OFF | 0/8/True
| **身體** | | 1/8/True
| ├ 位置 | 自由 | 自由, 鎖定水平, 鎖定垂直, 鎖定位置, 0/13/False
| ├ 旋轉 | 自由 | 自由, 鎖定旋轉, 1/13/False
| ├ 阻尼 | [0.5] (0 ~ 1) | 2/13/False
| ├ 傾斜 | [0] (-45 ~ 90) | 3/13/False
| ├ 彎曲 | [0] (-150 ~ 150) | 4/13/False
| ├ 扭轉 | [0] (-90 ~ 90) | 5/13/False
| ├ 頭部 | [0] (-90 ~ 90) | 6/13/False
| ├ 高度 | [0] (-1 ~ 1) | 7/13/False
| ├ 向前/向後 | [0] (-1 ~ 1) | 8/13/False
| ├ 距離 | OFF | 9/13/False
| ├ 目標演員 || 10/13/False
| │ 目標演員 |  |  |
| ├ 檢測範圍 | [2] (0 ~ 10) | 11/13/False
| ├ 最小距離 | [0.5] (0 ~ 1) | 12/13/False
| └ 最大距離 | [1] (0.5 ~ 2) | 13/13/False
| **搖擺動作** | | 2/8/True
| ├ (Enable Rocking Motion) | ON | 0/8/False
| ├ **速度** | | 1/8/False
| │ ├ 每拍動作數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ ├ 每組動作數 | [8] (4 ~ 32) | 1/7/False
| │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ ├ 曲線 | [0] (0 ~ 1) | 3/7/False
| │ ├ 變量速度 | OFF | 4/7/False
| │ ├ 模式 | (Gradual) | (Gradual), 隨機, 音量, 5/7/False
| │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| ├ 搖擺角度 | [30] (0 ~ 60) | 2/8/False
| ├ 上下 | [0.1] (0 ~ 0.3) | 3/8/False
| ├ 前後 | [0.1] (0 ~ 0.3) | 4/8/False
| ├ 深度變化 | [0.1] (0 ~ 0.3) | 5/8/False
| ├ 深度最大 | [0.15] (0 ~ 0.3) | 6/8/False
| ├ 深度額外 | [0] (-0.1 ~ 0.1) | 7/8/False
| └ 腳部動作 | [0] (-1 ~ 1) | 8/8/False
| **頭部姿勢** | | 3/8/True
| ├ (Enable Head Pose) | OFF | 0/3/False
| ├ X 旋轉 | [0] (-90 ~ 90) | 1/3/False
| ├ Y 旋轉 | [0] (-90 ~ 90) | 2/3/False
| └ Z 旋轉 | [0] (-90 ~ 90) | 3/3/False
| **腿部姿勢** | | 4/8/True
| ├ (Enable Leg Pose) | ON | 0/5/True
| ├ 相對於地面 | ON | 1/5/True
| ├ 最大扭轉 | [60] (0 ~ 90) | 2/5/True
| ├ 對稱 | ON | 3/5/True
| ├ **左** | | 4/5/True
| │ ├ 打開 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 腳 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 腳 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 腳 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 腳旋轉 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 腳旋轉 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 腳旋轉 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 腳趾 | [0] (-180 ~ 180) | 7/7/False
| ├ **右** | | 5/5/True
| │ ├ 打開 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 腳 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 腳 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 腳 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 腳旋轉 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 腳旋轉 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 腳旋轉 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 腳趾 | [0] (-180 ~ 180) | 7/7/False
| └ 預設 | **(Ride)** | (Sit), (Ride), (Kneel), (Stand),  |
| 手部對稱 | ON | 5/8/True
| **左手** | | 6/8/True
| ├ (Enable Left Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 手勢 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手部位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手掌旋轉** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 4/19/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 5/19/True
| ├ 鏡像左右 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 參考演員 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 參考骨骼 | **無** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, (Align), 9/19/True
| ├ 側面選擇 | 自動 | 自動, 左, 右, 10/19/True
| ├ 混合範圍 | [0.75] (0 ~ 2) | 11/19/True
| ├ 對稱偏移 | [0] (-1 ~ 1) | 12/19/True
| ├ 使用配件位置 | ON | 13/19/True
| ├ **運動** | | 14/19/True
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
| ├ **自定義姿勢** | | 15/19/True
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
| ├ 姿勢權重 | [1] (0 ~ 1) | 16/19/True
| ├ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 預設 | **(Rest)** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **右手** | | 7/8/True
| ├ (Enable Right Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 手勢 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手部位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手掌旋轉** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 4/19/True
| ├ 肘部方向 | [0] (-180 ~ 180) | 5/19/True
| ├ 鏡像左右 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 參考演員 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 參考骨骼 | **無** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, (Align), 9/19/True
| ├ 側面選擇 | 自動 | 自動, 左, 右, 10/19/True
| ├ 混合範圍 | [0.75] (0 ~ 2) | 11/19/True
| ├ 對稱偏移 | [0] (-1 ~ 1) | 12/19/True
| ├ 使用配件位置 | ON | 13/19/True
| ├ **運動** | | 14/19/True
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
| ├ **自定義姿勢** | | 15/19/True
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
| ├ 姿勢權重 | [1] (0 ~ 1) | 16/19/True
| ├ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 預設 | **(Rest)** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **騎乘模型** | | 8/8/True
| ├ (Enable Ride Model) | ON | 0/14/False
| ├ (Model: [Hoverbike]) || 1/14/False
| │ 模型 | **([Hoverbike])** | ([Hoverbike]), ([Rocking Horse]),  |
| ├ 加速度 | [10] (0 ~ 20) | 2/14/False
| ├ 拖曳 | [0.05] (0 ~ 1) | 3/14/False
| ├ 轉彎時傾斜 | [0.5] (0 ~ 1) | 4/14/False
| ├ 位置 || 5/14/False
| ├ (X) | [0] (-1 ~ 1) | 6/14/False
| ├ (Y) | [0] (-1 ~ 1) | 7/14/False
| ├ (Z) | [0] (-1 ~ 1) | 8/14/False
| ├ 旋轉 || 9/14/False
| ├ (X) | [0] (-90 ~ 90) | 10/14/False
| ├ (Y) | [0] (-90 ~ 90) | 11/14/False
| ├ (Z) | [0] (-90 ~ 90) | 12/14/False
| ├ 縮放 | [0] (-5 ~ 5) | 13/14/False
| └ 粒子效果 | ON | 14/14/False
| 預設 | **自由** | 自由, 搖擺動作, 懸浮摩托車, 搖擺馬, 桿子動作, 桿子混合,  |
