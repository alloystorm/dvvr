---
layout: single
title: 自动更新
toc: true
---

## 概述
自动更新是一个令人惊叹的功能，它允许您根据各种数据源（如时间轴、音频频谱、自定义输入等）来动画配置更改。

它可以用于许多不同类型的配置，包括位置、旋转、缩放，甚至颜色和不透明度。

## 自动更新设置
自动更新的配置包括：
* 模式：自动更新的数据源。可以是时间轴、音频频谱、自定义输入等。
* 输入起始值：输入的起始值
* 输入结束值：输入的结束值
* 输出起始值：输出的起始值
* 输出结束值：输出的结束值
* 曲线：定义值随时间变化的曲线。您可以使用曲线编辑器来编辑曲线。
* 循环时间：值从输入起始值到输入结束值所需的时间。当您想要重复动画时，这很有用。
* 相位：动画的时间偏移量。例如，如果您有两个循环时间相同但相位分别为0和0.5的自动更新，则这两个动画将相位差半个循环。
* 频段：在使用音频频谱时，控制要使用的频谱带。

计算方法如下：

输出 = （输出结束值 - 输出起始值）* （输入值 - 输入起始值）/ （输入结束值 - 输入起始值）+ 输出起始值

请注意，输入值始终被夹在输入起始值和输入结束值之间，因此输出永远不会超出值起始值和值结束值的范围。

例如，对于一个从0到1的配置，当模式设置为时间轴，"输入起始值"为20，"输入结束值"为80，"输出起始值"为40，"输出结束值"为60。
* 当时间轴为20%时，输出将为1 * 40% = 0.4
* 当时间轴低于20%时，输出也将为0.4，因为它被夹住了。
* 当时间轴为80%时，输出将为1 * 60% = 0.6
* 当时间轴超过80%时，输出也将为0.6，因为它被夹住了。
* 当时间轴为50%时，输出将为1 * ((0.6 - 0.4) * (50% - 20%) / (80% - 20%) + 0.4) = 0.5

## 自动更新数值
所有活动的自动更新数值都显示在"场景"菜单下的"自动更新数值"列表中。在这里，您可以快速查看每个自动更新的当前值，并编辑配置。