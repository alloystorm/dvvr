---
layout: release
title: 节奏光环
locale: zh-CN
---

# 节拍光环

<!-- TODO: full description. The Beats Ring is referenced as a tile on /dancexr/features under Stage & Props but no other page describes it. Likely an audio-reactive visualizer ring; confirm and fill in. -->

节拍光环是一个音频反应式视觉效果道具，会随着音乐脉动。它是 [auto-update](autoupdate) 数据源之一，这意味着其他设置可以根据其输出自行驱动。

---

## 功能

<!-- TODO: confirm shape (ring? particles? geometry?), where it is rendered (around the actor? on the stage?), how it scales with audio. -->

节拍光环获取当前的音频信号，并产生一个与节拍相关的数值，该数值可用于：

- 在表演者或舞台周围渲染一个可见的光环或脉冲效果。
- 与音乐同步驱动其他自动更新参数（例如：灯光强度、材质参数、运动速度）。

---

## 启用

<!-- TODO: confirm the menu path. Likely under environment menu or a per-actor setting. -->

---

## 设置

<!-- TODO: list. Possibly: visibility, color, scale, sensitivity threshold, smoothing. -->

---

## 相关页面

- [Auto update](autoupdate) — 将节拍光环用作其他设置的数据源
- [Music timing](music_timing) — 将动作与音乐同步
- [Audio options](audio_options)