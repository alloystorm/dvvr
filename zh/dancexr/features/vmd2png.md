---
layout: release
title: VMD2PNG
locale: zh-CN
toc: true
---

# VMD2PNG

<!-- TODO: confirm details against the actual tool. Drafted from the 2026.3 release notes. -->

**VMD2PNG** 是一个单独的开源工具，它将 `.vmd` 运动文件编码为 `.png` 图像。DanceXR 可以直接从这些 PNG 文件加载运动数据，因此您可以在任何通常需要 VMD 运动的地方使用它们。

在 **2026.3** 添加。

[GitHub: alloystorm/vmd2png](https://github.com/alloystorm/vmd2png)

---

## 为什么使用它

- **文件尺寸更小**：在许多情况下，比原始的 VMD 文件尺寸更小。
- **更易分享**：PNG 可以在任何平台上作为图像读取，无需剥离特殊元数据。
- **可视化**：PNG 本身就是运动数据的视觉表示，因此您可以一目了然地看出运动的稀疏程度或密度。
- <!-- TODO: confirm whether the PNG also serves as a thumbnail / preview in the DanceXR motion picker. -->

---

## 加载 VMD2PNG 文件

有两种等效的方法：

1. **拖放**：将 `.png` 文件拖放到正在运行的 DanceXR 窗口中——它会像 VMD 一样加载为运动。（有关拖放与舞美设置如何交互的说明，请参阅 [2026.3 的拖放加载说明](../releases/2026.3)）。
2. **内容库**：将 `.png` 运动文件与您的 `motions/` 文件夹中的 `.vmd` / `.bvh` / `.pose` / `.vpd` 文件放在一起。它们会像任何其他运动一样出现在运动选择器中。

---

## 创建您自己的文件

使用 [VMD2PNG](https://github.com/alloystorm/vmd2png) 命令行工具将现有的 `.vmd` 转换为 `.png`。输出的 PNG 是可移植的——任何拥有最新 DanceXR 构建版本的人都可以加载它。

<!-- TODO: confirm:
- Is decoding lossless? Round-trip vmd → png → vmd identity?
- Are camera / morph tracks preserved or only bone tracks?
- Any size or frame-count limits? -->

---

## 局限性

<!-- TODO: confirm. Likely:
- DanceXR versions before 2026.3 cannot load these.
- The PNG must not be re-encoded by image tools that strip the relevant metadata. -->

---

## 相关页面

- [分配运动](assign_motion)
- [运动设置](motion_settings)
- [姿势文件 (.pose / .vpd)](pose_files)
- [内容库](../preparecontent)