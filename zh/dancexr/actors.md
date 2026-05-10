---
layout: release
title: 使用角色
locale: zh-CN
toc: true
---

# 处理角色模型

角色模型（actor）是加载到场景中的角色。DanceXR 会实时调整模型的骨骼以适应动作，并使用物理系统模拟头发和服装的运动。

您可以通过更改材质、应用纹理或使用着装系统（dressing system）来切换服装部件，从而自定义模型的外观。您还可以调整模型的尺寸和位置，并精细调整其与舞台和其他角色模型的互动方式。

有关此处用到的术语（角色模型、选择圆盘、变换立方体、着装系统）的词汇表，请参阅 [Concepts & glossary](concepts)。

---

## 加载角色模型

DanceXR 读取三种模型格式：

- **PMX** — MikuMikuDance 格式。内置了骨骼层次结构、物理骨架和变形列表。
- **XPS** — XNALara / XPS 格式（`.xps`, `.mesh`, `.mesh.ascii`）。**不**包含物理骨架或标准骨骼，因此您需要在 DanceXR 中设置这些内容。
- **FBX** *(预览，自 2025.9 起)* — 通用 3D 格式。DanceXR 当前仅加载模型，不加载嵌入的动画或其他 FBX 特有功能。与 XPS 一样，FBX 在播放动作之前需要进行 [骨骼映射](features/bone_mapper)。

这三种格式都可以打包成 **ZIP** 文件。有关文件名规则和编码，请参阅 [ZIP 格式](features/zip_format)。

### 两种加载方式

- **拖放** 模型文件（或 zip）到 DanceXR 窗口。适合一次性加载。
- **内容库** — 将模型放置在内容库中的 `actors/` 目录下 [content library](preparecontent)。它们将出现在角色模型菜单的 *Load Model* 列表中。

### 替换与添加

默认情况下，加载模型会**替换**当前选中的角色模型。点击模型名称旁边的 **+** 图标，则可以将其添加为额外的角色模型。多角色场景需要专业版（Pro）构建版本 — 请参阅 [Download & editions](download)。

### 加载选项

[Loader options](features/loader_options) 控制新角色模型加载的方式：缓存大小、纹理压缩、过渡效果、自动角色切换。

---

## PMX vs XPS vs FBX — 有何不同

大多数设置在这三种格式上都是相同的。了解它们分歧的地方很有用：

| 主题 | PMX | XPS | FBX (预览) |
|---|---|---|---|
| 骨骼 | 文件中的标准骨骼名称 | 通过 [骨骼映射](features/bone_mapper) 映射 | 通过 [骨骼映射](features/bone_mapper) 映射 |
| 物理骨架 | 内置于文件（[PMX 物理骨架](features/pmx_physics)） | 在物理工具中配置 | 在物理工具中配置 |
| 变形/混合形状 | [变形列表](features/morph_list) | 无 — 请使用 [着装系统](features/optionals) 代替 | 无 |
| 服装切换 | 材质变形（PMX） | 可选物品（XPS）— 相同的 UI ([着装系统](features/optionals)) | 无 |

如果本指南中有内容提到“仅限 PMX”或“仅限 XPS”，那就是这个原因。FBX 支持截至 2025.9 为预览版 — 模型几何体和材质会加载，但文件内部的动画和其他 FBX 特性会被忽略。

---

## 角色模型菜单

每个角色模型在其脚下都有一个黄色的 **选择圆盘**。点击它会打开角色模型菜单——这是所有关于角色模型的核心枢纽。有关完整分解，请参阅 [Actor menu & tools](features/actor_tools)。

菜单按以下组划分：

- **运动** — 分配的运动、[formation](features/formation) 槽位和模型特定的运动设置。
- **最近修改** — 快速跳转到您刚刚更改的对话框。请参阅 [Recently modified settings](features/recently_modified)。
- **着装和纹理** — [着装系统](features/optionals)、[骨骼映射](features/bone_mapper) (XPS)、[alternative textures](features/alternative_textures)。
- **材质** — 每个槽位的设置：皮肤、头发、眼睛、嘴唇、不透明、透明、自定义。有关槽位如何协同工作的说明，请参阅 [Appearance & materials](appearance)。
- **设置** — 物理骨架、[feet adjustment](features/feet_adjustment)、[facial control](features/facial_control)、[eye contact](features/eyecontact)、[troubleshooting](features/troubleshooting)。
- **专业版（Pro）**（付费构建）— [outfit & body paint](features/outfit)、[accessory](features/accessory)、[ragdoll](features/ragdoll)、[motion override](features/motion_override)、[light ball](features/light_ball)、高级物理骨架、NSFW 覆盖层。
- **变形列表** (仅 PMX) — [PMX 变形混合形状](features/morph_list)。
- **工具** (扳手和锤子图标) — 收藏、标签、[spectator](features/spectator_mode)、向上/向下移动、重置、[duplicate](features/actor_tools#tools-menu)、重新加载、[3D snapshot](features/snapshot_3d)、移除。

---

## 多角色场景

当舞台上有多个角色模型时，有三个功能来处理群组行为：

- [Formation](features/formation) — 按照图案定位角色模型（直线、网格、自定义）。顺序通过工具菜单中的 **Move Up** / **Move Down** 设置。
- [Actor playlist](features/actor_playlist) — 循环播放一段时间内的一系列模型，可选地与音乐同步。
- [Attach to actor](features/attach_to_actor) — 将一个角色模型或配件父级化到另一个角色模型上（携带物品、骑乘物、配对动作）。

使用 [Spectator mode](features/spectator_mode) 可以让模型留在舞台上，但将其排除在自动分配的运动和 formation 槽位之外。

[Global actor control](features/global_actor_control) 一次性为所有角色模型应用设置 — 当您希望所有加载的模型共享相同的物理骨架调校、着装或材质时非常有用。

---

## 快照和预设

三种保存您所构建内容的方式：

- [3D snapshot](features/snapshot_3d) — 将当前姿势导出为 OBJ 文件，可用于其他 3D 工具。
- [Actor presets](features/actor_presets) — 保存角色模型的设置（材质、物理骨架、着装），以便稍后将相同的外观应用于相同的模型，或相似的模型。
- [Save scene](features/save_scene) 和 [scene bundle](features/scene_bundle) — 捕获整个场景，包括所有角色模型、运动、舞台和配置。

---

## 当某些内容看起来不对劲

先症状，再排查：

| 症状 | 查看位置 |
|---|---|
| 模型加载了，但所有内容都是白色 | [FAQ → Model loads but everything is white](faq) |
| 模型处于标准姿势时冻结 | [XPS bone mapper](features/bone_mapper), [Example bone structure](features/bones) |
| 漂浮、下沉、在地面上滑动 | [Feet adjustment](features/feet_adjustment) |
| 尺寸或位置错误 | [Scale & offset](features/scale_offset) |
| 头发/裙子/衣物不移动或抖动 | [Physics system](physics) |
| 特定模型异常 | [Actor troubleshooting](features/troubleshooting) |
| 应用程序级崩溃，无法启动 | [Troubleshooting](troubleshooting), [FAQ](faq) |

---

## 相关页面

- [Concepts & glossary](concepts)
- [Appearance & materials](appearance)
- [Physics system](physics)
- [Motion system](motion)
- [Actor menu & tools](features/actor_tools)
- [Content library](preparecontent)