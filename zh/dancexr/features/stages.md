---
layout: release
title: 舞台
locale: zh-CN
toc: true
---

# 舞台

<!-- TODO: confirm exact UI flow. Drafted from the actors / props / content-library structure. -->

舞台是您的表演环境——可以是俱乐部地板、音乐厅、城市街道或程序化的 [room](room_stage)。DanceXR 从您的内容库加载舞台的方式与加载角色和动作的方式相同，并在其上应用自己的光照、物理和摄影机系统。

---

## 加载舞台

将舞台模型放入您的 [内容库](../preparecontent)，并进行适当的标签化，以便它们显示在舞台菜单下。PMX、XPS 和 FBX 模型都可以用作舞台。

从场景菜单打开舞台选择器并选择模型进行加载。加载一个舞台会替换之前加载的任何舞台；一次只能激活一个舞台。

---

## 舞台 vs 道具 vs 房间

- **舞台** — 主要环境。加载一次，设置场景的地板、墙壁和尺度。
- **[Props](props)** — 附加模型，可叠加在（或独立于）舞台之上。
- **[Primitive shapes](primitive_shapes)** — 内置的方块/圆柱体/球体道具。
- **[Room Stage](room_stage)** — 一个内置的程序化舞台，无需外部模型即可配置。
- **[Ground](ground)** — 渲染的地面平面。舞台和地面共存；地面可以设置为 *仅阴影* 模式 (2024.3)，以便将模型的阴影叠加到背景或 AR Passthrough 上。

---

## 舞台和动作

如果加载的动作包含摄影机或舞台道具轨迹，这些轨迹会附加到舞台的原点。为某个舞台编写的动作文件，当加载到不同尺度的舞台时，可能需要进行 [缩放与偏移](scale_offset) 调整。

---

## 分享舞台

通过 [保存场景](save_scene) 保存完整的场景（包括加载的舞台及其设置）。如需将实际的舞台资源与场景文件一起打包，以便接收方无需自己查找模型，请使用 [场景包](scene_bundle)。

---

## 相关页面

- [Room Stage](room_stage)
- [Props](props)
- [Ground](ground)
- [Lighting](lighting)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)