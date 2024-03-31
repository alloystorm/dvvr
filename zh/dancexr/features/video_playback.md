---
locale: zh-CN
layout: single
title: 视频播放
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/video_playback) | [繁中](/tw/dancexr/features/video_playback) | [日本語](/jp/dancexr/features/video_playback) | [한국어](/kr/dancexr/features/video_playback) | [简中](/zh/dancexr/features/video_playback)

视频播放允许您播放视频，并使图像从光源投射出来，或者在场景中的墙面或道具表面上用作纹理。目前，仅支持MP4格式。

* 内容位置：将您的视频文件放在`content/videos`文件夹中，格式为MP4。
* 用作投影仪：转到光源设置，并选择[video]作为cookie映射。还有其他设置来控制投影图像的大小。使用新包含的预设来看看它们是如何工作的。
* 用作纹理：在表面设置中选择[video]作为纹理映射。包含的“Room”舞台模型有几个预设，供您看看它们是如何工作的。

视频播放与舞蹈音乐（如果加载了舞蹈音乐）同步，并由相同的播放和时间轴控制。

当您在场景中加载音乐时，请确保选择视频的“静音”选项，以便视频中的音乐不会干扰舞蹈音乐。

您也可以播放没有舞蹈音乐的视频。在这种情况下，取消选中“静音”选项，音频将从相同的音频源输出，并且您可以使用音量控制来调整视频音频的音量。

当您使用视频图像进行投影或纹理时，请确保选择了正确的宽高比。由于内部图像存储在矩形纹理中，并且在投影或放置在物体上时需要缩放回正确的宽高比。

在LW变体（Android，Quest，Mac，iOS和PC LW）中，有一个“适应帧”选项，它将放置带有黑边的图像以适应矩形宽高比。只有在您想要使用聚光灯来投射图像时才使用此模式。