---
layout: release
title: 增强现实模式
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
[Eng](/dancexr/features/ar_mode) | [繁中](/tw/dancexr/features/ar_mode) | [日本語](/jp/dancexr/features/ar_mode) | [한국어](/kr/dancexr/features/ar_mode) | [简中](/zh/dancexr/features/ar_mode)

AR模式适用于支持的iOS、Android和Quest设备。并非所有设备都具备AR功能，因此，如果在菜单中看不到AR选项，这意味着您的设备不支持AR。

在iOS和Android上，程序始终以普通模式启动，不带AR。然后，您可以转到场景菜单，勾选“AR”选项来启动AR。一旦激活，您将在屏幕上看到您的实时环境。

在Quest上，有两个独立的版本，DanceXR Mix是AR版本，而DanceXR Immersion仅支持VR。

## VR选项
* 遮挡：此选项将使虚拟对象出现在场景中真实对象的后面。当您希望虚拟对象出现在场景中真实对象的后面时，这将非常有用。请注意，遮挡并非完美，可能在某些情况下效果不佳。
* 仅阴影：此选项允许虚拟对象在场景中的真实对象上投下阴影。这通常会被遮挡所阻挡，因此当您希望看到阴影时，可能需要禁用遮挡。

## VR易用性（v2026.3）
DanceXR 2026.3使在VR和桌面模式之间切换更加便捷：

* 应用程序现在在启动时初始化VR，并在未检测到头显时自动回退到桌面模式，最大化兼容性。
* 新增的**退出VR**按钮可让您无需佩戴头显即可返回桌面模式。
* 从桌面模式进入VR仅需在场景菜单中点击**VR**选项即可。