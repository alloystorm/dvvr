---
layout: release
title: 外观与材质
locale: zh-CN
toc: true
---

# 外观与材质

DanceXR 的材质系统高度可定制，包含多个设置层级，这些层级堆叠组合，创造出角色或舞台上物体最终的外观效果。您可以更改材质属性、更换纹理、涂抹彩绘、切换服装部件等等。

有关特定功能细节，请遵循链接到每个专用页面。对于此处使用的术语（材质槽、着装系统、替代纹理、彩绘），请参阅 [Concepts & glossary](concepts#materials-and-appearance)。

---

## 控制层级

加载模型的材质通过多个层级进行控制，从底层到顶层：

1. **个体材质** — 您可以单独访问每个材质，并逐一更改其设置。
2. **材质槽** — 材质按表面类型（皮肤、毛发、眼睛、嘴唇、不透明、透明、自定义）分组到槽位中。每个槽位都有其自身的设置，当该槽位被开启时，这些设置将应用于该类别的角色所有材质。
3. **全局材质设置** — 适用于角色所有材质的全局覆盖设置，可用于快速更改需要保持整个模型一致的属性（例如，卡通阴影和所有透明材质的透明度阈值）。
4. **叠加层 (Overlays)** — 绘制在基础材质之上的图层，例如服装和彩绘、汗液效果、细节贴图和镜面/遮罩贴图。
5. **系统级渲染属性** — 适用于整个场景的设置，例如无光照模式、阴影质量、光线追踪效果和透明度预渲染。

请记住，当您启用了更高层级的控制时，个体的材质设置可能不会产生任何影响。

---

## 网格与可见性 — 着装系统

[着装系统](features/optionals) 结合了 PMX 的形变和 XPS 的可选网格，提供了一个统一的界面来切换模型部件的可见性。使用它可以开启或关闭服装部件，切换到替代形状，或隐藏特定的身体部位。

- 对于 **PMX** 模型，它通过模型作者定义的 *材质形变* 工作。切换功能显示或隐藏特定的子网格。
- 对于 **XPS** 模型，它通过每个槽位定义的 *可选物品* 工作。

两种情况下用户界面都是相同的。可用于服装更换、移除模型自带的配饰、更换发型子部件、隐藏肢体以实现特殊效果。

PMX 模型还通过 [Morph list](features/morph_list) 暴露个体形变——当形变没有作为着装开关显示时特别有用。

---

## 纹理增强 (专业版)

- [Custom detail map](features/custom_detail_map) — 自定义细节法线贴图。
- [Hexagon detail map](features/hexagon_detail) — 内置六边形图案细节。
- [Generate normal map](features/generate_normal_map) — 从漫反射纹理自动推导出法线贴图。
- [Specular / mask map](features/specular_map) — 镜面和遮罩贴图配置。

---
## 纹理 — 替代纹理集

[Alternative textures](features/alternative_textures) 允许您在运行时更换整个纹理集，而无需编辑模型。

工作原理：将额外的纹理与模型原始纹理使用**相同的文件名**放入不同的文件夹（或同一个 zip 中的其他位置）。DanceXR 会检测到这些文件并提供一个选择器。常见用途：多种肤色、昼夜版本、改色服装。

您还可以使用 [Texture enhancement](features/texture_enhancement)（专业版）在加载时对纹理进行 AI 放大和锐化。

---

## 材质 — 槽位系统

DanceXR 将材质按表面类型分组到**槽位**中。每个槽位都有其自身的设置；当槽位被开启时，这些设置将应用于该类别角色所有材质。

| 槽位 | 用途 | 页面 |
|---|---|---|
| Skin | 身体、脸部 | [Skin materials](features/material_skin) |
| Hair | 头部毛发、身体毛发 | [Hair materials](features/material_hair) |
| Eyes | 虹膜、巩膜、眼部高光 | [Eye materials](features/material_eyes) |
| Lips | 嘴唇和口腔内部 | [Lips materials](features/material_lips) |
| Opaque | 任何不属于身体槽位的固体物——服装、模型上的道具 | [Opaque materials](features/material_opaque) |
| Transparent | 任何透明物——玻璃、薄纱、粒子、毛发尖端 | [Transparent materials](features/material_transparent) |
| Custom | 最多两个用于需要独立设置着色器的自由形式槽位 | [Custom materials](features/material_custom1) |

材质进入槽位的方式：

- **PMX**: 基于模型文件中的材质属性（透明度、名称提示）。
- **XPS**: 基于您在着装系统/骨骼映射器中分配的槽位。

如果出现外观错误（皮肤显示为不透明、毛发显示为皮肤），通常是槽位分配问题。

---

## 叠加层

绘制在基础材质之上的图层：

- [Outfit & body paint](features/outfit) — 服装槽位和基于图像的彩绘，从 `texture/drawing` 中的图像绘制。
- [Sweat effect](features/sweat_effect) — 皮肤上的程序化汗液叠加层。

---

## 阴影风格

[Toon shading](features/toon_shading) 可为每个角色切换卡通/动漫风格的阴影效果。卡通路径使用的光照包裹、阴影渐变和边缘光数学与默认的 PBR 风格路径不同。根据所需的视觉效果进行选择；混合使用也是可以的。

[Raytracing effects](features/raytracing) 是一个独立的、场景级的特性（仅限 PC, RT 构建），无论阴影风格如何，它都会影响阴影和反射的质量。

---

## 常见问题

| 症状 | 可能的修复方法 |
|---|---|
| 能透过头发看穿 | 透明度深度预渲染 — 参见 [FAQ](faq#i-can-see-through-hair-materials) |
| 纹理缺失，模型是白色的 | 文件名或路径不匹配 — 参见 [FAQ](faq#model-loads-but-everything-is-white) |
| 皮肤看起来像塑料/反光 | 调整 [skin materials](features/material_skin) — 通常是降低镜面反射 |
| 无法移除服装 | 模型作者必须将其作为形变（PMX）或可选物品（XPS）暴露；使用 [着装系统](features/optionals) 查找可用选项 |
| 纹理看起来低分辨率 | 尝试 [Texture enhancement](features/texture_enhancement)，或放置更高分辨率的替代纹理 |
| 天球体看起来像素化/有孔洞 | 多个透明天球体 + 透明度深度预渲染；参见 [FAQ](faq) |

---

## 进一步阅读

- [Concepts & glossary](concepts#materials-and-appearance)
- [Working with actors](actors)
- [Physics system](physics) — 用于布料和毛发运动（与布料材质分开）
- [Content library](preparecontent) — `texture/`, `drawing/`, `mask/` 文件夹