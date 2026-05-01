---
layout: release
title: 舞动套装
locale: zh-CN
nav_links:
  - label: 简介
    url: /zh/dancexr
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
---
[Eng](/dancexr/features/dance_set) | [繁中](/tw/dancexr/features/dance_set) | [日本語](/jp/dancexr/features/dance_set) | [한국어](/kr/dancexr/features/dance_set) | [简中](/zh/dancexr/features/dance_set)

## 概述
舞蹈集是一组包含音频演员动作和摄像机动作（如果有的话）的集合。

舞蹈集可以包含任意数量的动作，可以有音频也可以没有。

在内容库中，如果您有一个包含1个音频文件和1个或多个演员动作的文件夹，这些数据将自动组成一个舞蹈集。

## 加载舞蹈集
通常舞蹈集的文件名与其音频文件相同。当您从内容菜单加载舞蹈集时，音频和所有动作也将被加载。

## 舞蹈集设置
舞蹈集具有每个动作的单独[设置](/dancexr/features/motion_settings)，以及所有动作的共同[时间和节拍](/dancexs/features/music_timing)设置。

## [混音](/dancexr/features/remix)
在DanceXR中，混音指的是使用一个舞蹈集的动作数据与另一个舞蹈集的音频进行配合。通过这个功能，您可以将动作适应不同的音频。它还会自动调整速度以匹配动作和音乐。

## VMD2PNG (v2026.3)
[VMD2PNG](https://github.com/alloystorm/vmd2png) 是一个开源工具，可将VMD动作数据编码为PNG图像文件，提供更小的文件大小、易于分享以及动作数据的视觉表示。

DanceXR 2026.3 支持从VMD2PNG文件加载动作。您可以通过将PNG文件拖拽到应用程序窗口中，或在内容库中与其它动作文件一同放置PNG文件来加载它们。