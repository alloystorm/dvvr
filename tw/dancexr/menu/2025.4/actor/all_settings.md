---
locale: zh-rTW
layout: single
title: 設定
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/all_settings) | [繁中](/tw/dancexr/menu/2025.4/actor/all_settings) | [日本語](/jp/dancexr/menu/2025.4/actor/all_settings) | [한국어](/kr/dancexr/menu/2025.4/actor/all_settings) | [简中](/zh/dancexr/menu/2025.4/actor/all_settings)

[演員](../menu#演員) > 設定



| Setting | Value | Description |
| :--- | --- | :--- |
| [面部控制](#面部控制) |
| [比例與偏移](#比例與偏移) |
| [自然動態](#自然動態) |
| [故障排除](#故障排除) |
| [水的互動](#水的互動) |
| [可視化骨骼](#可視化骨骼) |
| [運動通過](#運動通過) |


### **面部控制**



| Setting | Value | Description |
| :--- | --- | :--- |
| 嘴巴 || 
| 使用口型同步 | OFF | 
| 眉毛 || 
| 眼瞼 || 


### **比例與偏移**

(Allows configuration of the model's scale, ground offset, rotation, and positional offsets. Includes snapping options for precise adjustments.)

| Setting | Value | Description |
| :--- | --- | :--- |
|- 模型比例 | [0] (-3 ~ 3) | (Adjust the overall scale of the model. Values are exponential for finer control.)
|- 地面偏移 | [0] (-2 ~ 2) | (Set the vertical offset of the model relative to the ground.)
| 均勻高度 | ON | (Enable to scale the model to an average human height.)
|- 旋轉 | [0] (-180 ~ 180) | (Set the rotation of the model in degrees.)
|- 偏移X | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the X-axis.)
|- 偏移Z | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the Z-axis.)
|- 對齊 | **(0)**, (0.1), (0.2), (0.5), (1), (2),  | (Set the snapping increment for drag adjustments. Smaller values allow finer control.)
| 預設 | **均勻實際大小**, 縮影, 巨型, 原版,  |  |


### **自然動態**



| Setting | Value | Description |
| :--- | --- | :--- |
| 眼神接觸 | ON | 啟用眼神接觸，當與攝影機或其他模型在視覺範圍內時，注視並轉頭
| 凝視模式 | OFF | 持續注視範圍內最近的目標。
|- 看向攝影機 | [1] (0 ~ 1) | 攝影機作為凝視目標的優先級
|- 看向同伴 | [0.5] (0 ~ 1) | 其他模型作為凝視目標的優先級
|- 看向身體 | [0.5] (0 ~ 1) | 特定身體部位作為凝視目標的優先級
|- 眼神接觸角度 | [80] (0 ~ 180) | 視覺範圍的角度，僅此角度內的物體可以作為凝視目標
|- 眼神接觸頭部轉動 | [0.7] (0 ~ 1) | 看向目標時的頭部轉動比率
| 卡通眼睛 | ON | 減少眼睛旋轉，對於擁有大卡通眼睛的模型很有用
|- 卡通眼睛限制 | [0.4] (0 ~ 1) | 卡通眼睛模式中減少多少旋轉
|- 微笑嘴巴 | [1] (0 ~ 1) | 
|- 微笑眉毛 | [0.5] (0 ~ 1) | 
| (Random Target) | ON | 
| 閉眼 | ON | 隨機間隔自動眨眼
| 呼吸 | ON | 呼吸動作
|- 呼吸速率 | [0.3] (0 ~ 1) | 
| 微小移動 | OFF | 添加微小動作
|- 微小移動幅度 | [0.25] (0 ~ 1) | 
|- 微小移動週期 | [3] (1 ~ 10) | 


### **故障排除**



| Setting | Value | Description |
| :--- | --- | :--- |
| 將身體旋轉應用於中心 | OFF | 將髖部和軀幹的旋轉應用於中心骨骼
| 扭轉修正 | OFF | 減少手臂和腿部在關節處的扭動
|- 上臂扭轉 | [0] (0 ~ 1) | 
|- 下臂扭轉 | [0] (0 ~ 1) | 
|- 下臂模式 | 從上臂開始, **從手開始**,  | 
|- 腿部扭轉 | [0] (0 ~ 1) | 
|- 清除手臂扭轉 | [0] (0 ~ 1) | 
|- 肘部軸心 | [0] (-180 ~ 180) | 肘部關節的旋轉軸
| 忽略漫反射顏色 | OFF | 
|- 手部縮放 | [1] (0 ~ 1) | 設置手部的縮放
|- BVH 拇指動作 | [0.5] (0 ~ 1) | 減少 BVH 動作的拇指運動
|- 限制頸部旋轉 | [0] (0 ~ 1) | 減少頸骨的旋轉
|- 限制頭部旋轉 | [0] (0 ~ 1) | 減少頭骨的旋轉
| 重置過渡 | OFF | 在重置物理時，從標準姿勢過渡到動畫姿勢，以確保物理組件正確放置。
|- 重置期間的腿部姿勢 | [30] (0 ~ 45) | 
| 跳過運動學更新 | OFF | 不更新未被動畫化的運動學骨骼。


### **水的互動**



| Setting | Value | Description |
| :--- | --- | :--- |
| 波紋 | OFF | 
|- 強度 | [1] (0 ~ 2) | 
|- 身體 | [1] (0.1 ~ 2) | 
|- 手 | [0.5] (0.1 ~ 2) | 
|- 腳 | [0.5] (0.1 ~ 2) | 
| 水滴 || 
|- 汗水滴 | [0] (0 ~ 1) | 
|- 水滴發光 | [5] (0 ~ 20) | 
|- 水滴重力 | [3] (0 ~ 10) | 
|- 拖曳 | [2.5] (0 ~ 10) | 
|- 金屬質感 | [0.25] (0 ~ 1) | 
|- 透明度 | [0.25] (0 ~ 1) | 
|- 大小 | [0.003] (0 ~ 0.01) | 
|- 持續時間 | [5] (0 ~ 10) | 
| 汗水碰撞 | OFF | 


### **可視化骨骼**



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Visualize Bones) | OFF | 
| 虛擬骨骼 | ON | 
| 骨骼 | OFF | 
| IK | OFF | 
| 布娃娃 | OFF | 


### **運動通過**



| Setting | Value | Description |
| :--- | --- | :--- |
| 重置骨骼 | ON | 
| 動畫 | ON | 
| 偏移 | ON | 
| IK | ON | 
| 虛擬骨骼 | ON | 
| 形狀後更新 | ON | 
| 繼承骨骼 | ON | 
| 後變換 | ON | 
| 後IK | ON | 
| 最終更新 | ON | 
