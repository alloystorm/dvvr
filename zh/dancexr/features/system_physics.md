---
layout: single
title: 系统物理
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/system_physics) | [繁中](/tw/dancexr/features/system_physics) | [日本語](/jp/dancexr/features/system_physics) | [한국어](/kr/dancexr/features/system_physics) | [简中](/zh/dancexr/features/system_physics)


## 系统范围的物理设置
您可以在设置 -> 选项 -> 物理中找到系统范围的物理设置。

![系统物理](/images/system-physics.png)

启用
: 打开或关闭物理模拟

重力
: 改变重力力量。将其设置为负数将反转重力方向。

禁用碰撞
: 控制模型部件之间的碰撞。模型中有两种类型的碰撞器，类型A是随动画移动的部件，如手臂和腿部，类型B是自由移动的部件，通常它们通过一个或多个关节连接到其他部件上。默认情况下，类型B会与类型A发生碰撞，但如果打开“禁用碰撞”，则类型B对象将不再与类型A对象发生碰撞，而是穿透。

每秒步数
: 物理模拟是在步骤之间以一定的间隔计算的，如果间隔是固定的，效果最好。此选项控制每秒执行多少次模拟。步数越多越好，但过多的步数会降低帧率。最好与帧率匹配，以获得平滑的动画效果。