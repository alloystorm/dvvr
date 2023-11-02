---
layout: single
title: 音樂節奏
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)


## 概述
音樂節奏信息對於所有程序化動作來說非常重要，因為它用於將動作與音樂匹配。如果沒有它，BPM（每分鐘節拍數）將默認為120，並且不會與音樂同步。

## 演示
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## 點擊節拍
我們提供了一個“點擊節拍”的功能，讓您可以輕鬆準確地設置節奏信息。

您需要做的是播放音樂，然後在每次節拍下降時點擊按鈕。該程序需要約4次點擊來計算平均BPM和偏移值。您可以從地板上發光的圓環上看出，當設置正確時，光點可以完美地與音樂節拍匹配。如果第一次沒有做對，沒關係，只需繼續點擊節拍，直到一切看起來正確為止。

以前，我們在應用程序中捆綁了一個命令行工具，用於解析庫中的每個音樂文件並生成節奏信息，該方法仍然有效，但使用起來有些困難，並且僅支持WAV格式，無法從ZIP文件中讀取。以下是舊方法的視頻演示：

{% include video id="chI-3GQS08Q" provider="youtube" %}