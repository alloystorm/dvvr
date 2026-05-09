---
layout: release
title: PMX 混合形状变形
locale: zh-CN
toc: true
---

# PMX 混合形状形态

PMX 模型自带一份由模型作者定义的命名 **形态**（blendshapes）列表——包括面部表情、口型、服装开关、身体调整等。在 DanceXR 中的“形态列表”就是您浏览和应用这些形态的地方。

“形态列表”出现在任何加载的 **PMX** 模型的人格体菜单中。XPS 模型则使用 [Dressing system](optionals) 代替。

---

## 什么是形态

形态是模型存储的变形——包括顶点位置、骨骼偏移、材质参数或子网格可见性——可以由 0 到 1 的数值进行混合控制。PMX 模型通常包括：

- **面部形态** — 快乐、愤怒、悲伤、惊讶、睁/闭眼、口型（a/i/u/e/o）
- **骨骼形态** — 微小的骨骼调整
- **材质形态** — 颜色或透明度变化（由 [dressing system](optionals) 使用）
- **顶点形态** — 直接的网格变形
- **组形态** — 以上各项的组合

DanceXR 直接从 PMX 文件中读取这些形态；您无法在 DanceXR 中创建它们。

---

## 使用形态列表

<!-- TODO: confirm exact UI path and layout -->

1. 打开人格体菜单（点击该人格体的选择盘）。
2. 在菜单底部找到 **形态列表**。
3. 每个形态都会显示其名称和一个 0 到 1 的滑块。
4. 拖动滑块来应用形态；松开滑块则使其保持在该数值。

只要您更改或重新加载模型，形态就会保持应用状态。一些形态（例如面部表情）将在 [Facial control](facial_control) 和 [Blink, breathing & eye contact](eyecontact) 激活时被其覆盖。

---

## 技巧

- **形态名称取决于作者**。日本模型作者通常使用日文命名面部形态（まばたき, あ, い…）。英文模型则常使用英文名称。
- 此处显示的 **材质形态** 通常与 [Dressing system](optionals) 提供的相同；无论从哪个位置应用，效果都是一样的。
- 对于包含数百个形态的 PMX 模型，请滚动或使用搜索框 <!-- TODO: confirm if search exists --> 来查找您需要的形态。

---

## 相关页面

- [Dressing system](optionals)
- [Facial control](facial_control)
- [Blink, breathing & eye contact](eyecontact)
- [Concepts & glossary](../concepts)