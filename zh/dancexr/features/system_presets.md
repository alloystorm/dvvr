---
layout: release
title: 系统预设
locale: zh-CN
toc: true
---

# 系统预设

<!-- TODO: confirm exact contents and UI flow. Drafted from the 2024.1 release notes. -->

系统预设将**场景和环境设置**——图形质量、灯光、天空、地面——保存到一个名为预设的单体文件中，您可以稍后重新应用或与其他用户分享。

添加于 **2024.1** 版本。预设作为单独的 JSON 文件保存在 [内容库](../preparecontent) 中。

---

## 系统预设包含的内容

<!-- TODO: confirm the exact list of settings captured. The release notes call out: graphics quality, lighting, sky, ground. There are likely more. -->

一个典型的系统预设捕获了以下内容：

- [图形设置](graphics) — 渲染质量、后期效果。
- [灯光](lighting) — 方向和环境光设置，[灯光球](light_ball)。
- [天空和云层](skymap) 和 [天空颜色](sky)。
- [地面](ground) — 材质、仅阴影模式等。
- <!-- TODO: confirm whether camera, weather, simulation, or audio settings are included. -->

系统预设不包含的内容：

- 个体角色设置 — 这些存储在 [角色预设](actor_presets) 中。
- 已加载的角色、动作、音乐或舞台资源 — 这些存储在 [已保存场景](save_scene) 中。

---

## 保存和加载

<!-- TODO: confirm exact UI path. -->

1. 根据需要配置您的场景。
2. 打开相关的场景/系统菜单。
3. **保存预设** — 给它命名。预设会作为 JSON 文件写入内容库的 `presets/` (或 system-presets 子文件夹) 下。
4. **加载预设** — 按名称选择已保存的预设即可应用。

由于每个预设都是一个独立的文件，您可以将其在不同机器间复制或与其他用户分享。

---

## 系统预设与其它预设类型

| 预设 | 范围 | 典型内容 | 页面 |
|---|---|---|---|
| **系统预设** | 场景级 | 图形、灯光、天空、地面 | (本页面) |
| **角色预设** | 个体角色 | 材质、物理、服装 | [角色预设](actor_presets) |
| **已保存场景** | 全部 | 场景级 + 角色 + 动作 + 分配 | [已保存场景](save_scene) |
| **场景包** | 全部 + 资源 | 已保存场景 + 所依赖的模型/动作/音乐文件 | [场景包](scene_bundle) |

---

## 相关页面

- [角色预设](actor_presets)
- [已保存场景](save_scene)
- [场景包](scene_bundle)
- [内容库](../preparecontent)