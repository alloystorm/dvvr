---
locale: zh-CN
layout: single
title: XPS Physics

XPS物理
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/xps_physics) | [繁中](/tw/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics) | [한국어](/kr/dancexr/features/xps_physics) | [简中](/zh/dancexr/features/xps_physics)

## XPS模型特定设置
XPS模型没有物理定义，因此程序不知道在哪里添加物理组件。为了解决这个问题，每个XPS模型都添加了几个物理设置，供您配置XPS模型上的物理组件。

这包括：
* [身体碰撞器](xps_body_colliders.md)
* [胸部物理](xps_boobs.md)
* [头发物理](xps_hair.md)
* [服装物理](xps_cloth.md)
* [裙子物理](xps_skirt.md)
* [软体物理](xps_softbody.md)
* [分离物体](xps_detach.md)

### 演示
{% include video id="-IZTzHUpROs" provider="youtube" %}

要使用XPS物理工具，大多数情况下只需找到并选择正确的骨骼，程序会处理其余部分。

像马尾辫和丝带这样的东西非常容易，就像上面的视频演示的那样。

有时候子骨骼太多，您实际需要的骨骼可能被埋在这些子骨骼的几个级别下面。在这种情况下，您可以选择父骨骼，然后使用“跳过前X个骨骼”设置来微调您的选择。

如果在过程中出现混乱，不要惊慌。完成您的选择，然后您可以尝试在设置中稳定事物。
* 首先，尝试将“互连距离”减少到0以禁用互连关节，然后
* 尝试稍微增加碰撞器的大小（不要过度），
* 如果仍然不起作用，可以尝试禁用然后重新启用设置，
* 最终重新加载模型，有时可以解决不稳定性。