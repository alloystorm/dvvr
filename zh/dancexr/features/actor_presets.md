---
layout: release
title: 角色预设
locale: zh-CN
toc: true
---

# 角色预设

角色预设会保存角色设置的快照——包括物理、材质、服装、动作偏好等——以便您稍后将相同的配置重新应用于同一模型，或应用于具有相似体型的不同模型。

添加于 **2024.1**。存储在 [内容库](../preparecontent) 的 `presets/` 目录下，这意味着预设可以在使用同一版本的 DanceXR 的用户之间共享。

---

## 预设包含的内容

<!-- TODO: confirm the exact list of settings included. -->

一个典型的角色预设捕获了：

- 角色动作 [运动设置](motion_settings)
- [服装系统](optionals) 状态（可见/隐藏物品）
- 每个插槽的 [材质设置](material_settings)
- 物理配置（PMX 或 XPS，包括 [头发](hair_physics)、[裙子](skirt_physics)、[乳房](boobs_physics)、[身体碰撞体](body_colliders)）
- [脚部调整](feet_adjustment) 和 [缩放与偏移](scale_offset)

预设中**不包含**的内容：

- 模型文件本身（预设引用设置，而不是资源）。
- 全局设置——这些设置存在于 [系统预设](#system-presets) 中。
- 场景构成（舞台、灯光、摄影机）——这些存在于 [场景](save_scene) 中。

---

## 保存和加载

<!-- TODO: confirm exact UI path and naming flow. -->

1. 以您希望的方式配置角色。
2. 打开角色菜单，然后是 **工具菜单**（扳手和锤子图标）。
3. 保存预设；给它命名。
4. 要应用，在任何角色上打开相同的工具菜单，并按名称选择一个已保存的预设。

预设存储在内容库的 `presets/` 目录下。您可以将预设文件复制到不同机器之间。

---

## 预设在不同模型间可重复使用的场景

当应用于以下情况时，预设最为可靠：

- 您保存时的**同一模型**。
- **高度相似的模型**（相同的源角色，相同的骨骼）。
- **格式相同且体型相似的模型**（PMX到PMX，骨骼命名相似）。

对于差异很大的模型，依赖骨骼名称的设置——例如 XPS 物理骨架、[骨骼映射器](bone_mapper) 覆盖——可能无法干净地迁移。

---

## 系统预设

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

系统预设保存的是场景范围的设置（灯光、环境、摄影机、图形），而不是单个角色的设置。保存和应用流程相似；系统预设是单独存储的。

---

## 相关页面

- [保存场景](save_scene) — 捕获整个场景，而不是单个角色的设置
- [场景包](scene_bundle) — 将已保存的场景与其依赖的资源一起打包
- [内容库](../preparecontent) — `presets/` 文件夹位置
- [角色菜单与工具](actor_tools)