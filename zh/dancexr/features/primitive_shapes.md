---
layout: release
title: 基本形状
locale: zh-CN
toc: true
---

# 基本形状

内置几何道具 — **盒子**、**圆柱体** 和 **球体** — 您无需外部模型文件即可将其放置在场景中。它们适用于搭建舞台、模拟建筑元素（柱子、墙壁、基座）或作为与角色和布料交互的物理对象。

---

## 放置

从 [道具菜单](props) 中添加基本形状。每种基本形状都支持与任何其他道具相同的放置小部件：沿每个轴移动、旋转和缩放。

---

## 材质

每种基本形状都有其自身的材质设置：

- 表面颜色和纹理。
- 光滑度 / 金属度。
- <!-- TODO: confirm whether the full material slot system applies here, or a simplified subset. -->

这使得基本形状在布置镜头或测试灯光时，作为平面颜色参考道具非常有用。

---

## 物理

基本形状可以被设置为物理对象，使其可以掉落、与角色发生碰撞，并与 [布料](cloth_simulation) 和 [Softbody](softbody_physics) 系统进行交互。

- 在基本形状的设置中切换物理开关。
- 基本形状碰撞体匹配视觉形状（盒子使用盒子碰撞体等）。
- <!-- TODO: confirm whether primitives can be set kinematic / static separately from "physics off". -->

基本形状配合 [仅阴影地面模式](ground) 是 AR 拍摄中的常用技巧：基本形状模拟了一个现实世界中的物体，这样模型的阴影就可以投射到它上面。

---

## 相关页面

- [道具](props)
- [舞台](stages)
- [地面](ground)
- [镜子](mirror) — 反射表面，与基本形状平面互补
- [屏幕](screen)