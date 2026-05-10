---
layout: release
title: 自动舞蹈
locale: zh-CN
toc: true
---

# 自动舞蹈

Auto Dance 是**第一代**程序化舞蹈生成器。它从内置的动作库中即时生成舞蹈动作，并根据音乐的节拍和音量来选择和混合这些动作。

Auto Dance 已很大程度上被 [Auto Dance 2](autodance2) 和 [Auto Dance 3](autodance3) 取代——更新的版本具有更多变化、更精细的控制和更好的音乐同步性。如果需要原始生成器的行为，请使用 Auto Dance。

---

## 工作原理

- DanceXR 分析播放的音频，识别**节拍**（节奏）和**音量**（能量）。
- 在每个节拍上，生成器会从一系列短小的制作好的舞蹈片段库中选择下一个动作，并将其与上一个动作进行混合。
- 音量越高的部分会触发更大/更具活力的动作。

你不需要为 Auto Dance 加载 VMD 文件——动作是自动生成的。

---

## 设置

---

## 如何选择 Auto Dance 与新版本进行比较

- **Auto Dance（本页）** — 原始生成器。动作库较小，对音乐的反应较简单。
- **[Auto Dance 2](autodance2)** — 第二代，池子更大，动作间的变化更多。
- **[Auto Dance 3](autodance3)** — 当前默认。高度可定制；可与 [Sex Motion 3](sex_motion_3) 共享动作控制系统集成；使用包含节拍检测的实时音频分析器。

---

## 相关页面

- [Auto Dance 2](autodance2)
- [Auto Dance 3](autodance3)
- [音乐节拍](music_timing)
- [音频选项](audio_options)
- [AI in DanceXR](../ai)