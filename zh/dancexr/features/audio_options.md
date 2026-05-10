---
layout: release
title: 音频选项
locale: zh-CN
toc: true
---

# 音频选项

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.5, 2024.7, 2024.9, 2025.5, 2026.2). -->

音频选项控制当前 [dance set] 中的音频轨道如何播放，包括循环、音量以及音频源在场景中的定位。

---

## 播放模式

选择音频如何通过您的加载内容进行播放：

- **单曲** — 播放当前曲目一次。
- **循环** — 重复播放当前曲目。如果设置了循环区域（开始/结束时间），则只循环该区域。
- **随机播放** — 从队列中随机选择下一个曲目。
- <!-- TODO: confirm whether "Sequential / next in folder" is also a separate mode. -->

音频循环与动作循环是相互独立的（2024.5 添加）——您可以只循环音频而让动作持续播放，反之亦然。

---

## 音量

音频轨的标准主音量滑块。

<!-- TODO: confirm whether per-actor / per-source volume controls live here or under Playback Options. -->

---

## 空间音频

将音频固定在场景中的 3D 位置，而不是将其作为平面的立体声混音播放。请参阅 [Spatial Audio]。

---

## 音频分析

音乐 BPM 检测、节拍检测和副歌部分数据来自此层。请参见：

- [Music Timing] 用于设置 BPM 和节拍偏移量。
- [Auto Update] 用于使用音频电平/节拍作为其他设置的数据源。
- [Beats Ring] 和更新的 Audio Visualizer 用于可视化音频的反应。

实时音频分析器在 2025.5 版本中增加了节拍检测功能，因此程序化动作可以对实时节拍做出反应，而无需预计算时间。

---

## 音频/动作同步

当音频时间和动作时间产生偏差时，DanceXR 可以自动重新同步它们。请选择是同步 **音频到动作** 还是 **动作到音频** ——请参阅 [Motion Settings]。

音频计时在 2026.2 版本中得到进一步改进，以减少可变帧率下的卡顿；2026.3 版本修复了帧率大幅波动时出现的振荡问题。

---

## 相关页面

- [Playback Options](playback_options)
- [Music Timing](music_timing)
- [Dance Set](dance_set)
- [Spatial Audio](spatial_audio)
- [LipSync](lipsync)