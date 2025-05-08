---
locale: zh-rTW
layout: single
title: [Catwalk]
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.5/motion/catwalk) | [繁中](/tw/dancexr/menu/2025.5/motion/catwalk) | [日本語](/jp/dancexr/menu/2025.5/motion/catwalk) | [한국어](/kr/dancexr/menu/2025.5/motion/catwalk) | [简中](/zh/dancexr/menu/2025.5/motion/catwalk)

[程序化](../menu#程序化) > [Catwalk]

隨音樂節拍而動的程序化伸展台動作。

## 配置

| 設定 | 值 | 描述 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 指定到全部 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 指定到選擇項 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 作為第二個指定到全部 || 
| <img src="/images/icon/ic_motion.png" alt="motion icon"/> 作為第二個指定到選擇項 || 
| ⊖ 擺動 | [15] (0 ~ 45) | 臀部左右擺動。
| ⊖ 扭轉 | [5] (0 ~ 45) | 軀幹扭轉。
| ⊖ 距離 | [18] (0 ~ 60) | 腿部動作角度。
| ⊖ 步伐高度 | [0.05] (0 ~ 0.2) | 步伐高度。
| ⊖ 軀幹彎曲 | [0] (0 ~ 30) | 腿部彎曲。
| ⊖ 軀幹擺動 | [-0.5] (-1 ~ 1) | 
| ⊖ 軀幹扭轉 | [2] (-2 ~ 2) | 
| ⊖ 腳跟 | [0] (0 ~ 90) | 
| ⊖ 重疊 | [0.25] (0 ~ 2) | 腳步重疊。
| ⊖ 曲線 | [0.35] (0 ~ 1) | 
| ☑ 手部對稱 | [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **左手** | | 
| ├─> 手勢 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部位置** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部旋轉** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─☑ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 無旋轉, 
| ├─⊖ 手肘方向 | [0] (-180 ~ 180) | 
| ├─☐ 左右鏡像 | [OFF] | 
| ├─> 參考角色 | **(Partner)** | (Self), (Partner), (Closest),  |
| ├─> 參考骨骼 | **臀部** | 無, 臀部, 胸部, 頭部, 中心, 杆子, (Upperarm), (Forearm), 手部, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├─☑ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, 對齊, 
| ├─☑ 側邊選擇 | 自動 | 自動, 左, 右, 
| ├─⊖ 混合範圍 | [0.75] (0 ~ 2) | 
| ├─⊖ 對稱偏移 | [0] (-1 ~ 1) | 
| ├─☑ 考慮配件位置 | [ON] | 
| ├─☐ **動作** | | 
| │ ├─☐ 啟用 | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **速度** | | 
| │ │ ├─☑ 每拍移動次數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| │ │ ├─⊖ 每組移動次數 | [8] (4 ~ 32) | 
| │ │ ├─⊖ 相位 | [0] (0 ~ 1) | 
| │ │ ├─⊖ 曲線 | [0] (0 ~ 1) | 
| │ │ ├─☐ 變速 | [OFF] | 
| │ │ ├─☑ 模式 | (Gradual) | (Gradual), 隨機, 音量, 
| │ │ ├─☑ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| │ │ └─☑ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 
| │ ├─⊖ 距離 | [0.1] (0 ~ 0.3) | 
| │ └─⊖ 角度 | [0] (-60 ~ 60) | 
| ├─☐ **自訂姿勢** | | 
| │ ├─☐ 啟用 | [OFF] | 
| │ ├─⊖ 打開 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指軸向 | [90] (-360 ~ 360) | 
| │ ├─⊖ 拇指折疊 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 食指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 中指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 無名指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 小指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 向下傳播 | [1] (0 ~ 1) | 
| │ └─⊖ 混合 | [1] (0 ~ 1) | 
| ├─⊖ 姿勢權重 | [1] (0 ~ 1) | 
| ├─⊖ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 
| ├─⊖ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 
| ├─⊖ (Grab Axis) | [0] (-180 ~ 180) | 
| └─≡ 預設值 | **臀部** | (Rest), 背面, 正面, 臀部, 頭部, 杆子, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **右手** | | 
| ├─> 手勢 | **(Grab)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部位置** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **手部旋轉** | | 
| │ ├─⊖ (X) | [0] ((Unlimited)) | 
| │ ├─⊖ (Y) | [0] ((Unlimited)) | 
| │ └─⊖ (Z) | [0] ((Unlimited)) | 
| ├─☑ 旋轉類型 | 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 無旋轉, 
| ├─⊖ 手肘方向 | [0] (-180 ~ 180) | 
| ├─☐ 左右鏡像 | [OFF] | 
| ├─> 參考角色 | **(Partner)** | (Self), (Partner), (Closest),  |
| ├─> 參考骨骼 | **臀部** | 無, 臀部, 胸部, 頭部, 中心, 杆子, (Upperarm), (Forearm), 手部, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
| ├─☑ IK 模式 | 自動 | 自動, 正常, (Cylinder), 球體, 對齊, 
| ├─☑ 側邊選擇 | 自動 | 自動, 左, 右, 
| ├─⊖ 混合範圍 | [0.75] (0 ~ 2) | 
| ├─⊖ 對稱偏移 | [0] (-1 ~ 1) | 
| ├─☑ 考慮配件位置 | [ON] | 
| ├─☐ **動作** | | 
| │ ├─☐ 啟用 | [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **速度** | | 
| │ │ ├─☑ 每拍移動次數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| │ │ ├─⊖ 每組移動次數 | [8] (4 ~ 32) | 
| │ │ ├─⊖ 相位 | [0] (0 ~ 1) | 
| │ │ ├─⊖ 曲線 | [0] (0 ~ 1) | 
| │ │ ├─☐ 變速 | [OFF] | 
| │ │ ├─☑ 模式 | (Gradual) | (Gradual), 隨機, 音量, 
| │ │ ├─☑ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| │ │ └─☑ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 
| │ ├─⊖ 距離 | [0.1] (0 ~ 0.3) | 
| │ └─⊖ 角度 | [0] (-60 ~ 60) | 
| ├─☐ **自訂姿勢** | | 
| │ ├─☐ 啟用 | [OFF] | 
| │ ├─⊖ 打開 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指軸向 | [90] (-360 ~ 360) | 
| │ ├─⊖ 拇指折疊 | [0] (-1 ~ 1) | 
| │ ├─⊖ 拇指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 食指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 中指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 無名指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 小指彎曲 | [0] (-1 ~ 1) | 
| │ ├─⊖ 向下傳播 | [1] (0 ~ 1) | 
| │ └─⊖ 混合 | [1] (0 ~ 1) | 
| ├─⊖ 姿勢權重 | [1] (0 ~ 1) | 
| ├─⊖ 抓取距離 | [0.015] (-0.1 ~ 0.1) | 
| ├─⊖ 抓取位置 | [-0.05] (-0.1 ~ 0.1) | 
| ├─⊖ (Grab Axis) | [0] (-180 ~ 180) | 
| └─≡ 預設值 | **臀部** | (Rest), 背面, 正面, 臀部, 頭部, 杆子, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **圓形行走** | | 
| ├─☐ 圓形行走 | [OFF] | 
| └─⊖ 半徑 | [2] (0 ~ 5) | 
