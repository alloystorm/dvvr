---
layout: single
title: 音乐节奏
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)


## 概述
音乐节奏信息对于所有的程序化动作非常重要，因为它用于将动作与音乐匹配。如果没有它，BPM（每分钟节拍数）默认为120，与音乐不会同步。

## 演示
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## 敲击节拍
有一个“敲击节拍”的功能，可以帮助您准确设置节奏信息。

您需要做的是播放音乐，然后每次有节拍时点击按钮。程序需要大约4次敲击来计算平均BPM和偏移值。您可以从地板上发光的圆环看出，当设置正确时，光点可以完美地与音乐节拍匹配。如果第一次没有弄对，没关系，继续敲击节拍，直到一切看起来正确为止。

以前，我们在应用程序中捆绑了一个命令行工具，用于解析库中的每个音乐文件并生成节奏信息，该方法仍然有效，但使用起来有点困难，只支持WAV格式，不能从ZIP中读取。旧方法的视频：

{% include video id="chI-3GQS08Q" provider="youtube" %}