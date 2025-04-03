---
locale: zh-rTW
layout: single
title: 應用設置
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/system/application_settings) | [繁中](/tw/dancexr/menu/2025.4/system/application_settings) | [日本語](/jp/dancexr/menu/2025.4/system/application_settings) | [한국어](/kr/dancexr/menu/2025.4/system/application_settings) | [简中](/zh/dancexr/menu/2025.4/system/application_settings)

[系統](../menu#系統) > 應用設置



| Setting | Value | Description |
| :--- | --- | :--- |
| 載入上個場景 | OFF | 啟動時自動加載上個場景0/7/False
| 在 VR 中阻止桌面窗口 | ON | 在 VR 模式下阻止桌面窗口1/7/False
| 從保存中恢復標籤 | OFF | 嘗試從保存的設置中恢復標籤，以防你的內容緩存被重建或損壞2/7/False
| 翻轉 DDS 壓縮 | ON | 翻轉壓縮的 DDS 資源3/7/False
| 翻轉 DDS 解壓縮 | OFF | 翻轉未壓縮的 DDS 資源4/7/False
| **虛擬現實手部** | | 5/7/False
| ├ 手部可見 | ON | 0/7/False
| ├ 投擲陰影 | OFF | 1/7/False
| ├ (Time And FPS) | ON | 2/7/False
| ├ **手部方向** | | 3/7/False
| │ ├ 偏移 || 0/5/False
| │ ├ (X) | [0] (-0.1 ~ 0.1) | 1/5/False
| │ ├ (Y) | [0] (-0.1 ~ 0.1) | 2/5/False
| │ ├ (Z) | [0] (-0.1 ~ 0.1) | 3/5/False
| │ ├ 旋轉 | [45] (-90 ~ 90) | 4/5/False
| │ └ 更新指標 || 5/5/False
| ├ (Left Hand Pose: Auto) || 4/7/False
| │ 左手姿勢 | **自動** | 自動, (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **左手配件** | | 5/7/False
| │ ├ (Enable Left Hand Accessory) | OFF | 0/24/False
| │ ├ (Model: [Pole]) || 1/24/False
| │ │ 模型 | **[柱子]** | [柱子],  |
| │ ├ **錨點偏移** | | Set the anchor position for the attachment to attach to2/24/False
| │ │ ├ 位置 || 0/7/False
| │ │ ├ (X) | [0] (-1 ~ 1) | 1/7/False
| │ │ ├ (Y) | [0] (-1 ~ 1) | 2/7/False
| │ │ ├ (Z) | [0] (-1 ~ 1) | 3/7/False
| │ │ ├ 旋轉 || 4/7/False
| │ │ ├ (X) | [0] (-90 ~ 90) | 5/7/False
| │ │ ├ (Y) | [0] (-90 ~ 90) | 6/7/False
| │ │ └ (Z) | [0] (-90 ~ 90) | 7/7/False
| │ ├ 大小及對齊 || 3/24/False
| │ ├ 物件半徑 | [0.02] (0.01 ~ 0.05) | 4/24/False
| │ ├ 物件長度 | [0.2] (0 ~ 5) | 5/24/False
| │ ├ 縮放 | [0] (-5 ~ 5) | 6/24/False
| │ ├ 朝向 | (Y Up) | (Y Up), (Y Down), (X Up), (X Down), (Z Up), (Z Down), 7/24/False
| │ ├ 偏移 || 8/24/False
| │ ├ (X) | [0] (-2 ~ 2) | 9/24/False
| │ ├ (Y) | [0] (-2 ~ 2) | 10/24/False
| │ ├ (Z) | [0] (-2 ~ 2) | 11/24/False
| │ ├ 旋轉 || 12/24/False
| │ ├ (X) | [0] (-180 ~ 180) | 13/24/False
| │ ├ (Y) | [0] (-180 ~ 180) | 14/24/False
| │ ├ (Z) | [0] (-180 ~ 180) | 15/24/False
| │ ├ 吉他模式 | OFF | 16/24/False
| │ ├ **運動** | | Apply up / down motion to the attachment model17/24/False
| │ │ ├ (Enable Motion) | OFF | 0/3/False
| │ │ ├ **速度** | | 1/3/False
| │ │ │ ├ 每拍動作數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ │ ├ 每組動作數 | [8] (4 ~ 32) | 1/7/False
| │ │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
| │ │ │ ├ 曲線 | [0] (0 ~ 1) | 3/7/False
| │ │ │ ├ 變量速度 | OFF | 4/7/False
| │ │ │ ├ 模式 | (Gradual) | (Gradual), 隨機, 音量, 5/7/False
| │ │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
| │ │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| │ ├ (Animation: None) || 選擇已加載的運動供附加模型使用18/24/False
| │ │ 動畫 | **無** | 無, <br/>選擇已加載的運動供附加模型使用 |
| │ ├ **表面** | | 19/24/False
| │ │ ├ 光澤 | [0.9] (0 ~ 1) | 0/9/True
| │ │ ├ 金屬質感 | [1] (0 ~ 1) | 1/9/True
| │ │ ├ 凸起 | [0.2] (0 ~ 1) | 2/9/True
| │ │ ├ 發光 | [0] (0 ~ 10) | 3/9/True
| │ │ ├ 環境光 | [1] (0 ~ 1) | 4/9/True
| │ │ ├ 透明度 | [1] (0 ~ 1) | 5/9/True
| │ │ ├ 剪裁 | [0] (0 ~ 1) | 6/9/True
| │ │ ├ **顏色** | | 7/9/True
| │ │ │ ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
| │ │ │ ├ 色相 | [0] (0 ~ 1) | 1/8/True
| │ │ │ ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
| │ │ │ ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| │ │ │ ├ 紅色 | [1] (0 ~ 1) | 4/8/True
| │ │ │ ├ 綠色 | [1] (0 ~ 1) | 5/8/True
| │ │ │ ├ 藍色 | [1] (0 ~ 1) | 6/8/True
| │ │ │ ├ (Blend Mode: Blend) || 7/8/True
| │ │ │ │ 混合模式 | **混合** | 原版, (Multiply), 混合, (Color Shift),  |
| │ │ │ ├ 混合 | [1] (0 ~ 1) | 8/8/True
| │ │ │ └ 預設 | **白色** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| │ │ ├ **卡通著色器** | | 8/9/True
| │ │ │ ├ (Enable Toon Shader) | OFF | 0/10/True
| │ │ │ ├ 陰影 | [1] (0 ~ 1) | 1/10/True
| │ │ │ ├ 輪廓 | [0.5] (0 ~ 1) | 2/10/True
| │ │ │ ├ 光澤 | [0.25] (0 ~ 1) | 3/10/True
| │ │ │ ├ 柔軟光澤 | [0.1] (0 ~ 1) | 4/10/True
| │ │ │ ├ 高光區域 | [0.25] (0 ~ 1) | 5/10/True
| │ │ │ ├ 柔和高光 | [0.1] (0 ~ 1) | 6/10/True
| │ │ │ ├ 環境光 | [0.75] (0 ~ 1) | 7/10/True
| │ │ │ ├ 陰影區域 | [0.65] (0 ~ 1) | 8/10/True
| │ │ │ ├ 陰影 | [0.75] (0 ~ 1) | 9/10/True
| │ │ │ ├ 柔和陰影 | [0.1] (0 ~ 1) | 10/10/True
| │ │ │ └ 預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| │ │ ├ **特殊著色器** | | 9/9/True
| │ │ │ ├ (Mode: Off) || 0/2/False
| │ │ │ │ 模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │ │ │ ├ 折射 | [0.5] (1 ~ 3) | 1/2/False
| │ │ │ └ 厚度 | [1] (0 ~ 1) | 2/2/False
| │ │ └ 預設 | **鍍鉻** | 白色光澤, 紅色光澤, 鍍鉻, 黑色光澤, 金色, 實心玻璃, 薄玻璃,  |
| │ ├ X光 | [0] (0 ~ 1) | 20/24/False
| │ ├ 透明度 | [1] (0 ~ 1) | 21/24/False
| │ ├ 拉手 | [0.1] (0 ~ 0.5) | 當手接近附加物時向附加物拉手22/24/False
| │ ├ 抓取姿勢 | ON | 當手在附加物上時，自動改變手部姿勢為抓取23/24/False
| │ └ 手部運動 | [0] (-1 ~ 1) | 相對於附加物運動移動手部24/24/False
| ├ (Right Hand Pose: Auto) || 6/7/False
| │ 右手姿勢 | **自動** | 自動, (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
| └ **右手配件** | | 7/7/False
|   ├ (Enable Right Hand Accessory) | OFF | 0/24/False
|   ├ (Model: [Pole]) || 1/24/False
|   │ 模型 | **[柱子]** | [柱子],  |
|   ├ **錨點偏移** | | Set the anchor position for the attachment to attach to2/24/False
|   │ ├ 位置 || 0/7/False
|   │ ├ (X) | [0] (-1 ~ 1) | 1/7/False
|   │ ├ (Y) | [0] (-1 ~ 1) | 2/7/False
|   │ ├ (Z) | [0] (-1 ~ 1) | 3/7/False
|   │ ├ 旋轉 || 4/7/False
|   │ ├ (X) | [0] (-90 ~ 90) | 5/7/False
|   │ ├ (Y) | [0] (-90 ~ 90) | 6/7/False
|   │ └ (Z) | [0] (-90 ~ 90) | 7/7/False
|   ├ 大小及對齊 || 3/24/False
|   ├ 物件半徑 | [0.02] (0.01 ~ 0.05) | 4/24/False
|   ├ 物件長度 | [0.2] (0 ~ 5) | 5/24/False
|   ├ 縮放 | [0] (-5 ~ 5) | 6/24/False
|   ├ 朝向 | (Y Up) | (Y Up), (Y Down), (X Up), (X Down), (Z Up), (Z Down), 7/24/False
|   ├ 偏移 || 8/24/False
|   ├ (X) | [0] (-2 ~ 2) | 9/24/False
|   ├ (Y) | [0] (-2 ~ 2) | 10/24/False
|   ├ (Z) | [0] (-2 ~ 2) | 11/24/False
|   ├ 旋轉 || 12/24/False
|   ├ (X) | [0] (-180 ~ 180) | 13/24/False
|   ├ (Y) | [0] (-180 ~ 180) | 14/24/False
|   ├ (Z) | [0] (-180 ~ 180) | 15/24/False
|   ├ 吉他模式 | OFF | 16/24/False
|   ├ **運動** | | Apply up / down motion to the attachment model17/24/False
|   │ ├ (Enable Motion) | OFF | 0/3/False
|   │ ├ **速度** | | 1/3/False
|   │ │ ├ 每拍動作數 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
|   │ │ ├ 每組動作數 | [8] (4 ~ 32) | 1/7/False
|   │ │ ├ 相位 | [0] (0 ~ 1) | 2/7/False
|   │ │ ├ 曲線 | [0] (0 ~ 1) | 3/7/False
|   │ │ ├ 變量速度 | OFF | 4/7/False
|   │ │ ├ 模式 | (Gradual) | (Gradual), 隨機, 音量, 5/7/False
|   │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
|   │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
|   │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
|   │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
|   ├ (Animation: None) || 選擇已加載的運動供附加模型使用18/24/False
|   │ 動畫 | **無** | 無, <br/>選擇已加載的運動供附加模型使用 |
|   ├ **表面** | | 19/24/False
|   │ ├ 光澤 | [0.9] (0 ~ 1) | 0/9/True
|   │ ├ 金屬質感 | [1] (0 ~ 1) | 1/9/True
|   │ ├ 凸起 | [0.2] (0 ~ 1) | 2/9/True
|   │ ├ 發光 | [0] (0 ~ 10) | 3/9/True
|   │ ├ 環境光 | [1] (0 ~ 1) | 4/9/True
|   │ ├ 透明度 | [1] (0 ~ 1) | 5/9/True
|   │ ├ 剪裁 | [0] (0 ~ 1) | 6/9/True
|   │ ├ **顏色** | | 7/9/True
|   │ │ ├ 顏色模式 | (RGB) | (RGB), (HSV), 0/8/True
|   │ │ ├ 色相 | [0] (0 ~ 1) | 1/8/True
|   │ │ ├ 飽和度 | [0] (0 ~ 1) | 2/8/True
|   │ │ ├ 亮度 | [1] (0 ~ 1) | 3/8/True
|   │ │ ├ 紅色 | [1] (0 ~ 1) | 4/8/True
|   │ │ ├ 綠色 | [1] (0 ~ 1) | 5/8/True
|   │ │ ├ 藍色 | [1] (0 ~ 1) | 6/8/True
|   │ │ ├ (Blend Mode: Blend) || 7/8/True
|   │ │ │ 混合模式 | **混合** | 原版, (Multiply), 混合, (Color Shift),  |
|   │ │ ├ 混合 | [1] (0 ~ 1) | 8/8/True
|   │ │ └ 預設 | **白色** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
|   │ ├ **卡通著色器** | | 8/9/True
|   │ │ ├ (Enable Toon Shader) | OFF | 0/10/True
|   │ │ ├ 陰影 | [1] (0 ~ 1) | 1/10/True
|   │ │ ├ 輪廓 | [0.5] (0 ~ 1) | 2/10/True
|   │ │ ├ 光澤 | [0.25] (0 ~ 1) | 3/10/True
|   │ │ ├ 柔軟光澤 | [0.1] (0 ~ 1) | 4/10/True
|   │ │ ├ 高光區域 | [0.25] (0 ~ 1) | 5/10/True
|   │ │ ├ 柔和高光 | [0.1] (0 ~ 1) | 6/10/True
|   │ │ ├ 環境光 | [0.75] (0 ~ 1) | 7/10/True
|   │ │ ├ 陰影區域 | [0.65] (0 ~ 1) | 8/10/True
|   │ │ ├ 陰影 | [0.75] (0 ~ 1) | 9/10/True
|   │ │ ├ 柔和陰影 | [0.1] (0 ~ 1) | 10/10/True
|   │ │ └ 預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
|   │ ├ **特殊著色器** | | 9/9/True
|   │ │ ├ (Mode: Off) || 0/2/False
|   │ │ │ 模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
|   │ │ ├ 折射 | [0.5] (1 ~ 3) | 1/2/False
|   │ │ └ 厚度 | [1] (0 ~ 1) | 2/2/False
|   │ └ 預設 | **鍍鉻** | 白色光澤, 紅色光澤, 鍍鉻, 黑色光澤, 金色, 實心玻璃, 薄玻璃,  |
|   ├ X光 | [0] (0 ~ 1) | 20/24/False
|   ├ 透明度 | [1] (0 ~ 1) | 21/24/False
|   ├ 拉手 | [0.1] (0 ~ 0.5) | 當手接近附加物時向附加物拉手22/24/False
|   ├ 抓取姿勢 | ON | 當手在附加物上時，自動改變手部姿勢為抓取23/24/False
|   └ 手部運動 | [0] (-1 ~ 1) | 相對於附加物運動移動手部24/24/False
| (Gizmo 3rd Axis: Rotation) || 6/7/False
| Gizmo 第三軸 | **旋轉** | 旋轉, 深度,  |
| 使用翻譯名稱 | ON | 7/7/False
