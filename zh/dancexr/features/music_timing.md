---
locale: zh-CN
layout: single
title: 音乐同步
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本語](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)

## 概述
音乐节拍信息对于所有程序化动作都非常重要，因为它用于将动作与音乐匹配。如果没有它，BPM（每分钟节拍数）默认为120，与音乐不会同步。

## 演示
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## 敲击节拍
有一个“敲击节拍”的功能，可以帮助您准确设置节拍信息。

您需要做的是播放音乐，然后每次有节拍时点击按钮。程序需要大约4次敲击来计算平均BPM和偏移值。您可以从地板上发光的环看出，当设置正确时，光点可以完美地与音乐节拍匹配。如果第一次没有弄对，没关系，继续敲击节拍，直到一切看起来正确为止。

以前，我们在应用程序中捆绑了一个命令行工具，用于解析库中的每个音乐文件并生成节拍信息，该方法仍然有效，但使用起来有点困难，只支持WAV格式，不能从ZIP中读取。旧方法的视频：

{% include video id="chI-3GQS08Q" provider="youtube" %}

## 音频节拍改进（v2026.2）
DanceXR 2026.2 包含了改进的音频节拍同步功能，进一步减少了音频/动作不同步现象，并消除了因帧率波动导致的偶尔卡顿。在 v2026.3 中，一个额外的修复程序解决了由于音频时间平滑处理可能引入的帧率大幅波动导致的振荡问题。