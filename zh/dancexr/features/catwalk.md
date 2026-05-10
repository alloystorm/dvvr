---
layout: release
title: T台动作
locale: zh-CN
toc: true
---

# 猫步运动

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

猫步运动是一种程序化行走/T台走秀动作。角色会以走秀般的步伐走向目标点——伴有臀部摆动、刻意迈步、抬着头——而无需使用VMD行走动作文件。

适用于：

- 角色从舞台外进入的定点摆姿场景。
- T台/时装视频。
- 在另一个动作开始前填充时间。

---

## 行为

- 角色沿着场景的Z轴向前行走（或走向目标点 — <!-- TODO: confirm whether target selection is exposed -->）。
- 步态节拍是程序化的；如果设置了音乐BPM ([Music Timing](music_timing))，则步子可以与节拍同步。
- 该动作会循环；角色会持续行走，直到您停止它或分配其他动作。

---

## 相关页面

- [待机动作](idle_motion)
- [Auto Dance 3](autodance3)
- [写实动作](lifelike_motions)
- [脚部调整](feet_adjustment)
- [音乐时机](music_timing)