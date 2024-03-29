---
locale: zh-CN
layout: single
title: 自动更新
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/autoupdate) | [繁中](/tw/dancexr/features/autoupdate) | [日本語](/jp/dancexr/features/autoupdate) | [한국어](/kr/dancexr/features/autoupdate) | [简中](/zh/dancexr/features/autoupdate)


## 概述
自动更新是一个工具，允许您根据时间轴、音频频谱、自定义输入等各种数据源来对配置更改进行动画处理。

它可以用于许多不同类型的配置，包括位置、旋转、缩放，甚至颜色和不透明度。

## 自动更新设置
自动更新的配置包括：
* 模式：这是自动更新的数据源。可以是时间轴、音频频谱、自定义输入等。
* 输入来自：输入的起始值
* 输入至：输入的结束值
* 值来自：输出的起始值
* 值至：输出的结束值
* 曲线：定义值随时间变化的曲线。您可以使用曲线编辑器编辑曲线。
* 周期时间：值从输入来自到输入至所需的时间。当您想要重复动画时，这很有用。
* 相位：动画的时间偏移。例如，如果有两个具有相同周期时间的自动更新，但一个相位为0，另一个相位为0.5，则这两个动画将相位差半个周期。
* 频段：在使用音频频谱时，这控制要使用的频谱带。
* 输入通道：在选择轴输入模式时要使用的输入轴
* 消耗输入：一旦切换打开，所选的输入轴将不会触发输入设置中指定的其他操作。

计算如下：

输出 = (值至 - 值来自) * (输入值 - 输入来自) / (输入至 - 输入来自) + 值来自

请注意，输入值始终在输入来自和输入至之间夹紧，因此输出永远不会超出值来自和值至的范围。

例如，对于范围从0到1的配置，当模式设置为时间轴时，“输入来自”为20，“输入至”为80，“值来自”为40，“值至”为60。
* 当时间轴为20%时，输出将为1 * 40% = 0.4
* 当时间轴低于20%时，输出也将为0.4，因为它被夹紧。
* 当时间轴为80%时，输出将为1 * 60% = 0.6
* 当时间轴超过80%时，输出也将为0.6，因为它被夹紧。
* 当时间轴为50%时，输出将为1 * ((0.6 - 0.4) * (50% - 20%) / (80% - 20%) + 0.4) = 0.5

## 音频数据源
{% include video id="A00DhbCOgu0" provider="youtube" %}
{% include video id="BV1cm4y1t74d" provider="bilibili" %}

* 音频振幅模式允许根据当前音频输出级别更改配置值。
    * 您可以选择平滑设置来根据需要微调输出。
    * 更高的平滑设置会生成平滑的输出，而较低的平滑设置则允许更快的响应。
* 频谱带模式从音频频谱数据中获取输出。
* 它分为1024个频带。按频率顺序排列。
* 较低的频带号代表低音，反之亦然。

## 自动更新数值
所有活动的自动更新数值都显示在“场景”菜单下的“自动更新数值”列表中。在这里，您可以快速查看每个自动更新的当前值，并编辑配置。