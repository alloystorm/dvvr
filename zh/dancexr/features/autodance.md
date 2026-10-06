---
layout: release
title: 自动舞蹈
locale: zh-CN
toc: true
---

# 自动舞蹈

Auto Dance 是**第一代**程序化舞蹈生成器。它从内置的动作库中即时生成舞蹈动作，并根据音乐的节拍和音量来选择和混合这些动作。

Auto Dance 已很大程度上被 [Auto Dance 2](autodance#auto-dance-2) 和 [Auto Dance 3](autodance3) 取代——更新的版本具有更多变化、更精细的控制和更好的音乐同步性。如果需要原始生成器的行为，请使用 Auto Dance。

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
- **[Auto Dance 2](autodance#auto-dance-2)** — 第二代，池子更大，动作间的变化更多。
- **[Auto Dance 3](autodance3)** — 当前默认。高度可定制；可与 [Sex Motion 3](sex_motion_3) 共享动作控制系统集成；使用包含节拍检测的实时音频分析器。

---

## 相关页面

- [Auto Dance 2](autodance#auto-dance-2)
- [Auto Dance 3](autodance3)
- [音乐节拍](music_timing)
- [音频选项](audio_options)
- [AI in DanceXR](../ai)

## 自动舞动 2 {#auto-dance-2}

# 自动舞蹈2

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

自动舞蹈2是**第二代**程序化舞蹈生成器。它改进了最初的[自动舞蹈](autodance)，拥有更大的动作资源池，相邻动作之间的变化性更强，并且与音乐的节拍和音量同步更精确。

自动舞蹈2本身已被[自动舞蹈3](autodance3)取代，后者使用与[Sex Motion 3](sex_motion_3)共享的现代动作控制系统，并与实时音频分析器集成。

---

## 与自动舞蹈1的改动

- 内置舞蹈片段资源池更大。
- 相邻动作之间的融合更自然，结果看起来不像幻灯片。
- 对音乐音量的响应有所改进——能量更饱满的部分会有更大胆的动作。

---

## 设置

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## 何时选择自动舞蹈2

当您需要一种程序化舞蹈，且符合以下要求时，请使用自动舞蹈2：

- 比原始的自动舞蹈变化性更大。
- 比高度可配置的自动舞蹈3更简单——调节旋钮更少，设置更快。

对于新项目，除非您特别想要自动舞蹈2的行为，否则请优先选择[自动舞蹈3](autodance3)。

---

## 相关页面

- [自动舞蹈](autodance)
- [自动舞蹈3](autodance3)
- [音乐节拍](music_timing)
- [音频选项](audio_options)
- [AI在DanceXR](../ai)
