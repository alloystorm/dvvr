---
locale: zh-CN
layout: single
title: 天空与云
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/skymap) | [繁中](/tw/dancexr/features/skymap) | [日本語](/jp/dancexr/features/skymap) | [한국어](/kr/dancexr/features/skymap) | [简中](/zh/dancexr/features/skymap)

## 天空模式
您可以选择使用天空地图、纯色或程序化模式来渲染天空。

## 在Quest上
出于性能原因，在Quest上，您没有天空地图或程序化选项。天空颜色选项位于照明配置中。它有一个额外的透明度滑块，用于控制背景的透明度，以实现混合现实。

## PC上的透视
某些PC VR流媒体程序允许用透视图像替换纯色背景。您可以将天空设置为颜色模式，并选择一个颜色（例如纯黑或绿色），流媒体系统将使用此颜色来实现此功能。

## 云
程序生成的云可以受风影响，并随时间变化。

## 天空地图
您可以使用HDRI全景图像作为天空地图。支持jpg和HDR格式。

{% include video id="2NZpffP1X5o" provider="youtube" %}

{% include video id="vUY7DY4cCV0" provider="youtube" %}

在DanceXR中找到天空地图并将其加载为背景。

## 程序化天空
* 太阳光角现在由白天时间、黄道角和方向控制。
* 根据白天时间值自动在白天和黑夜之间过渡。
* 夜空中有星星
{% include video id="D745FYNcx4c" provider="youtube" %}