---
locale: zh-CN
layout: single
title: 加载选项
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/loader_options) | [繁中](/tw/dancexr/features/loader_options) | [日本語](/jp/dancexr/features/loader_options) | [한국어](/kr/dancexr/features/loader_options) | [简中](/zh/dancexr/features/loader_options)


## 概述
加载选项包含在加载演员模型时的选项，并提供演员缓存的管理。

### 演员缓存
加载的演员模型被缓存在内存中，以便下次加载时可以立即使用。在缓存管理器中，您可以更改缓存模型的数量，并从缓存中删除特定的模型。

### 保留选项
一旦打开，替换演员时，将保留出场演员的设置，并应用于新的演员模型。

### 过渡效果
选择并配置演员模型淡入淡出时的动画。

### 自动演员更换
这是一个特殊功能，当此滑块的值超过某个阈值时，自动用缓存的演员替换舞台上的当前演员。

例如，如果缓存中有4个演员。滑块的值及相应的演员将为：
* 0-0.25：演员1
* 0.25-0.5：演员2
* 0.5-0.75：演员3
* 0.75-1：演员4

这个功能的常见用例是启用[自动更新](autoupdate)并将其设置为时间轴的0-100%。当歌曲处于前25%时，第一个演员将在舞台上，然后当它超过25%的标记时，系统将开始从演员1过渡到演员2。