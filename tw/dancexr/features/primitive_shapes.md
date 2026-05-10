---
layout: release
title: 基本形狀
locale: zh-TW
toc: true
---

# 原始形狀

內建的幾何道具——**方塊**、**圓柱**和**球體**——您無需外部模型檔案即可將其放置在場景中。這些道具可用於佈置舞台、模擬建築元素（如柱子、牆壁、基座），或作為與角色和布料互動的物理物件。

---

## 放置

從 [道具選單](props) 中添加原始形狀。每個原始形狀都支援與任何其他道具相同的放置輔助工具：沿每個軸移動、旋轉和縮放。

---

## 材質

每個原始形狀都有其獨立的材質設定：

- 表面顏色和紋理。
- 光滑度/金屬感。
- <!-- TODO: confirm whether the full material slot system applies here, or a simplified subset. -->

這使得原始形狀在佈局鏡頭或測試照明時，可用作平面顏色參考道具。

---

## 物理

原始形狀可以設置為物理物件，使其能夠下墜、與角色發生碰撞，並與 [布料](cloth_simulation) 和 [Softbody](softbody_physics) 系統互動。

- 在原始形狀的設定中切換物理功能。
- 原始形狀碰撞器與視覺形狀匹配（方塊使用方塊碰撞器等）。
- <!-- TODO: confirm whether primitives can be set kinematic / static separately from "physics off". -->

原始形狀結合 [僅陰影的地面模式](ground)，是 AR 拍攝的常用技巧：原始形狀模擬了真實世界物體，從而在它上面投射出角色的陰影。

---

## 相關頁面

- [道具](props)
- [舞台](stages)
- [地面](ground)
- [鏡子](mirror) — 反射表面，與原始形狀平面互補
- [螢幕](screen)