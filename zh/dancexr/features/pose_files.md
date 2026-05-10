---
layout: release
title: 姿态文件 (.pose / .vpd)
locale: zh-CN
toc: true
---

# 姿势文件

<!-- TODO: confirm details against current build. Drafted primarily from the 2024.6 release notes. -->

DanceXR 可以加载 **`.pose`** (XPS / XNALara) 和 **`.vpd`** (MMD / PMX) 格式的静态姿势文件，并将其用作单个姿势，或作为一系列姿势并自动在它们之间进行过渡。

新增于 **2024.6**。

---

## 姿势文件的位置

将姿势文件放置在 `motions/` 文件夹中，位于 [内容库](../preparecontent)。它们会与 VMD 和 BVH 文件一同出现在动作选择器中。

---

## 使用单个姿势

1. 加载一个演员模型。
2. 打开动作菜单，像选择任何动作一样选择 `.pose` 或 `.vpd` 文件。
3. 演员模型会立即摆到保存的姿势上。

---

## 姿势序列（自动生成动作）

如果您在一个目录中保留了多个姿势文件，您可以将它们全部加载为一个生成的动作序列：

1. 在动作选择器中，选择包含姿势的 **文件夹**。
2. 使用右下角的选项：
   - **加载为序列 (Load as sequence)** — 按文件夹顺序播放姿势。
   - **加载为随机序列 (Load as random sequence)** — 随机播放姿势。

DanceXR 会自动在每个姿势之间创建 **过渡动作**，因此演员模型会从一个姿势平滑地移动到下一个姿势，而不是突然跳变。

---

## 过渡动作设置

打开序列设置菜单可以微调过渡效果：

<!-- TODO: list the actual settings exposed in the sequence menu. -->

- **过渡持续时间 (Transition duration)** — 从姿势 A 到姿势 B 移动所需的时间。
- **过渡锚定 (Transition anchoring)** — 在过渡期间保持身体部分固定的设置。*脚部*锚定对于站立姿势效果很好，可以防止模型滑动。
- <!-- TODO: confirm other settings (easing curve, hold time at each pose, etc.). -->

---

## 跨格式姿势调整

`.pose` 文件是为 XPS 骨骼搭建的，而 `.vpd` 文件是为 PMX 骨骼搭建的。当您跨格式应用姿势时，手臂和腿部可能需要进行手动偏移调整：

- 在姿势/序列设置中使用 **手臂角度 (arm angle)** 和 **腿部角度 (leg angle)** 调整，可以使 `.pose` 在 PMX 模型上看起来正确，或者使 `.vpd` 在 XPS 模型上看起来正确。

<!-- TODO: confirm exact location and naming of the cross-format adjustment controls. -->

---

## 兼容性说明

<!-- TODO: confirm: which transition-anchoring modes survived the new motion system from 2024.8 ("Motion transition anchoring is not working" was listed as temporarily unsupported). -->

---

## 相关页面

- [分配动作 (Assigning Motion)](assign_motion)
- [动作设置 (Motion Settings)](motion_settings)
- [动作覆盖 (Motion Override)](motion_override)
- [关键帧动画 (Keyframe Animation)](keyframe_animation)
- [内容库](../preparecontent)