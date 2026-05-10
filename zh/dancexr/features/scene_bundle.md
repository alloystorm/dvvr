---
layout: release
title: 场景包
locale: zh-CN
toc: true
---

# 场景包

<!-- TODO: confirm exact UI flow and bundle format. Drafted from release notes (2024.1, 2024.9). -->

场景包（Scene Bundle）是指一个[保存的场景](save_scene)加上它所引用的实际模型、动作和音乐文件——这些文件被一起打包，这样接收方就可以加载整个场景，而无需先费力搜集所有资源。

于 **2024.1** 版本（实验性）添加。

---

## 保存场景 vs 场景包

- 一个**保存的场景**是一个小文件，它*引用*资源名称。当您加载它时，DanceXR 会在接收方的资源库中查找每个引用的资源。如果接收方缺少这些模型或动作中的任何一个，该场景部分就无法加载。
- 一个**场景包**将保存的场景**与**其依赖的所有资源一起封装。接收方可以直接加载该包——没有缺少资源的困扰。

分发场景时请使用场景包；如果是在您自己使用，并且您已经拥有所有资源时，请使用保存的场景。

---

## 创建场景包

<!-- TODO: confirm UI path. -->

1. 以您想要的方式设置好场景。
2. 打开场景菜单，选择**保存为场景包**。
3. DanceXR 会收集所有引用的资源（模型、动作、音乐），并将它们打包成一个单独的场景包文件。

该场景包包含了该场景在另一台设备、另一个国家加载所需的一切，接收方无需费心寻找相同的模型包。

---

## 加载场景包

将场景包文件视为任何其他内容库项目——将其拖入您的库中，或通过场景菜单打开它。

加载时，DanceXR 会将资源提取到临时或每个场景包专用的位置，然后从那里加载场景。默认情况下，这些资源不会合并到接收方的主资源库中 <!-- TODO: confirm exact behavior here — extracted to a subfolder vs. merged. -->

---

## 限制

<!-- TODO: confirm. Likely:
- Bundle size scales with the assets included; large stage models can produce very large bundles.
- Tier-locked features still require the recipient to have that tier.
- Personal / unauthorized model redistribution — the bundle does not strip licensing constraints. -->

标记为 2024.1 版本实验性；有关当前状态，请参阅发布说明。

---

## 相关页面

- [保存场景](save_scene)
- [内容库](../preparecontent)
- [角色预设](actor_presets)
- [系统预设](system_presets)