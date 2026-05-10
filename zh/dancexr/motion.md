---
layout: release
title: 运动系统
locale: zh-CN
toc: true
---

# 动作系统

DanceXR 中的动作来源于多个源头，并在多个层级进行配置，它们可以叠加。本页面就是您的地图：了解动作的来源、设置的存储位置以及各个层如何结合。

有关术语（动作层、覆盖、舞步包、混音、自定义继承），请参阅 [概念与术语表](concepts#motion-concepts)。

---

## 动作源

动作可以来自五个位置：

1. **动作文件** (VMD 或 BVH)，从磁盘加载。
2. **舞步包** — 由一个音频文件加上一个或多个动作组成，当它们在一个文件夹或 zip 文件中分组时，系统会自动检测。
3. **程序化动作** — 由自动舞步、待机动作、T台走秀、拟真动作和二次动作在运行时生成。
4. **关键帧动画** — 在 DanceXR 中手动制作的姿势。
5. **混音** — 使用一个舞步包的动作数据，搭配另一个舞步包的音频。

您可以混合使用这些动作。一个典型的场景会播放一个由 VMD 驱动的舞步，并在其上叠加一个程序化的 [二次动作](features/secondary_motion) 层，同时还包括由各自系统处理的 [眼部接触](features/eyecontact) 和呼吸。

---

## 舞步包单元

[舞步包](features/dance_set) 是“歌曲”的天然分组。当您将包含一个音频文件和一个或多个匹配的 VMD/BVH 文件的文件夹或 zip 文件放置在 `motion/` 中时，DanceXR 会自动将它们分组。加载的舞步包：

- 播放音频。
- 将动作路由到角色（默认每个角色一个动作；可重新分配）。
- 如果包含摄影机 VMD，可选择性地驱动摄影机。
- 拥有一个与音频 BPM 绑定的共享 [音乐时序](features/music_timing)。

舞步包是您加载、保存、分享和混音的单元。虽然单个动作仍有自己独立的设置（例如每动作的速度、循环范围等），但舞步包负责保持它们之间的协调一致。

[VMD2PNG](features/dance_set#vmd2png-v20263)（2026.3 版本新增）允许您加载从 PNG 文件中编码的动作数据——这些文件更小，更容易分享，并且包含缩略图。

---

## 设置层级

动作设置存在于三个级别。当同一个参数在多个级别存在时，更具体的级别具有最高的优先级。

| 级别 | 页面 | 范围 |
|---|---|---|
| 系统 | [动作设置](features/motion_settings) | 场景中每个动作的默认值 |
| 角色级 | [角色动作设置](features/motion_settings) | 覆盖单个角色的动作设置 |
| 动作级 | [舞步包](features/dance_set) 内 | 舞步包内的每动作微调 |

[播放选项](features/playback_options) — 速度、循环模式、范围 — 应用于播放级别（即整个音频/动作时间线）。

---

## 分配动作

[分配动作](features/assign_motion) 涵盖了实际的机械流程：将 VMD 拖放到窗口，或点击音频/动作菜单中的 *分配给*，或打开角色菜单并在已加载的动作中选择。

当您有多个角色时，顺序很重要。在角色 [工具菜单](features/actor_tools#tools-menu) 中使用 **上移 / 下移** 可以重新排列角色，从而改变它们在自动分配时获得的舞步包中的动作。

[旁观者模式](features/spectator_mode) 会将一个角色排除在自动分配之外。

---

## 分层与覆盖

当您想要组合或修改动作时，四个页面执行相关操作——请为您的任务选择合适的页面：

| 想要实现 | 使用 |
|---|---|
| 一个角色同时播放两个动作（例如舞蹈动作加手势） | [动作层](features/motion_passes) |
| 替换动作中的特定骨骼（修复手臂穿模、更换面部） | [动作覆盖](features/motion_override) |
| 将一个舞步包的动作与另一个舞步包的音频配对 | [混音动作](features/remix) |

动作层进行堆叠；覆盖对每根骨骼进行遮罩；继承动作改变了哪些骨骼被视为跟随其他骨骼；混音是在同一动作上进行音频层面的替换。

---

## 程序化动作

在运行时生成，无需源 VMD：

- [待机动作](features/idle_motion) — 在没有任何其他动作播放时，处理呼吸和静止姿势。
- [T台走秀动作](features/catwalk) — 程序化的行走周期。
- [自动舞步 1](features/autodance)、[自动舞步 2](features/autodance2)、[自动舞步 3](features/autodance3) — 程序化舞蹈生成器。除非您有理由选择早期版本，否则请使用 **自动舞步 3**；它具备节拍分析和最强的变化性。
- [拟真动作](features/lifelike_motions) — 使处于暂停或待机的角色感觉更生动的微动作。
- [二次动作](features/secondary_motion) — 一个运行在任何动作之上的程序化层（摆动、呼吸、跟随）。
- [关键帧动画](features/keyframe_animation) — 使用手动关键帧制作您自己的姿势。

[待机动作](features/idle_motion)、[自动舞步](features/autodance)、[自动舞步 2](features/autodance2) 和 [动作覆盖](features/motion_override) 都提供了 [Gizmo 立方体](controls#gizmo-cubes) 以进行直接摆姿。

---

## 音乐时序

[音乐时序](features/music_timing) 检测（或允许您设置）加载音频的 BPM 和节拍偏移。多个系统会消耗这些数据：

- [自动舞步 3](features/autodance3) 将动作变化与节拍同步。
- [自动摄影机](features/auto_cam) 可以将镜头切换与节拍同步，并响应音频的敏感度。
- [自动更新](features/autoupdate) 可以从节拍信号驱动任何设置。

如果程序化舞蹈感觉节拍不对，请先修复音乐时序。

---

## 角色行为 — 持续层

有三个系统会持续运行，无论播放什么动作，以防止角色看起来像机器人：

- [眨眼、呼吸和眼部接触](features/eyecontact) — 眼睑行为、自动注视目标、呼吸升降。
- [面部控制](features/facial_control) — 手动或自动的面部表情/形变混合。
- [拟真动作](features/lifelike_motions) — 微小的待机调整。

这些都会与您使用的任何动作源进行组合。

---

## 常见问题

| 症状 | 解决方法 |
|---|---|
| 加载了动作但没有任何变化 | 动作已加载但未分配 — 请参阅 [分配动作](features/assign_motion) |
| 错误的角色执行了舞蹈 | 在 [工具菜单](features/actor_tools#tools-menu) 中使用上移/下移重新排序角色 |
| 动作运行速度不对 | 检查 [播放选项](features/playback_options) 以及 [舞步包](features/dance_set) 中的每动作速度 |
| 程序化舞蹈的节拍不对 | [音乐时序](features/music_timing) — 验证 BPM 和偏移量 |
| 手臂穿模身体 | 在出问题的手臂骨骼上使用 [动作覆盖](features/motion_override) |
| 角色在动作间隙看起来僵硬 | 启用 [待机动作](features/idle_motion)、[眼部接触](features/eyecontact) 和 [拟真动作](features/lifelike_motions) |

---

## 相关页面

- [概念与术语表](concepts#motion-concepts)
- [处理角色](actors)
- [DanceXR 中的 AI](ai) — 自动舞步和 AI 驱动的动作
- [电影化摄影机](cameras) — 自动摄影机也会读取音乐时序