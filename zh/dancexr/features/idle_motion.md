---
layout: release
title: 待机动画
locale: zh-CN
toc: true
---

# 闲置动作

<!-- TODO: confirm UI labels. Drafted from release notes (2025.12) and the procedural-motion family. -->

闲置动作是一种程序化运动，当模型没有被分配其他运动时会播放。它模拟呼吸、体重转移以及头部和四肢的小幅移动，使模型在站立姿势中看起来栩栩如生，而非僵硬。

---

## 闲置动作播放时机

- 当给模型分配任何运动之前。
- 当一个运动结束时（且模型不处于序列的一部分）。
- 在序列中的暂停期间。

如果正在播放明确的运动，则不会运行闲置动作。要将微妙的微小动作叠加到活动的运动之上，请参阅 [Lifelike Motions](lifelike_motions) 而非使用闲置动作。

---

## 设置

<!-- TODO: confirm exact slider names and ranges. -->

- **强度** — 闲置动作的整体振幅。
- **速度** — 呼吸/体重转移循环的速度。
- **身体摆动、头部动作** — 按区域的倍数。

---

## 新闲置动作 (v2025.12)

DanceXR 2025.12 引入了由新的程序化运动控制系统驱动的更自然的闲置动作。新版本产生的闲置动画比早期版本更平滑，重复性更低。未来版本计划对程序化运动控制进行更多改进。

---

## 相关页面

- [Lifelike Motions](lifelike_motions) — 任何运动上的微妙微小动作
- [Catwalk Motion](catwalk)
- [Auto Dance 3](autodance3)
- [Blink, Breathing & Eye Contact](eyecontact)
- [Motion Settings](motion_settings)