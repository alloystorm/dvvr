---
layout: release
title: XPS物理
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

## XPS模型特定设置
XPS模型没有物理定义，因此程序不知道在哪里添加物理组件。为此，为每个XPS模型添加了几个物理设置，供您在XPS模型上配置物理组件。

这包括：
* [身体碰撞器](xps_body_colliders)
* [胸部物理](xps_boobs)
* [头发物理](xps_hair)
* [服装物理](xps_cloth)
* [裙子物理](xps_skirt)
* [软体物理](xps_softbody)
* [分离物体](xps_detach)

### 演示
{% include video id="-IZTzHUpROs" provider="youtube" %}

要使用XPS物理工具，大多数情况下您只需找到并选择正确的骨骼，程序就会处理其余部分。

像马尾辫和丝带这样的东西非常简单，如上面的视频所示。

有时子骨骼太多，您需要的骨骼可能实际上埋藏在这些子骨骼的数个级别之下。在这种情况下，您可以选择父骨骼，然后使用“跳过前X个骨骼”设置来微调您的选择。

如果在过程中出现混乱，不要惊慌。完成您的选择，然后您可以尝试在设置中稳定事物。
* 首先，尝试将“互连距离”减少到0以禁用互连关节，然后
* 尝试稍微增加碰撞器的大小（不要过度），
* 如果仍然不起作用，您可以尝试禁用然后重新启用设置，
* 最后重新加载模型，因为这有时可以解决不稳定性。