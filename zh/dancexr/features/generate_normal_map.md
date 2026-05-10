---
layout: release
title: 生成法线贴图
locale: zh-CN
toc: true
---

# 生成法线贴图

DanceXR 可以使用 **基础贴图** 或 **高光贴图** 作为源，为缺少法线贴图的材料合成法线贴图。这可以在无需您编写或提供单独法线贴图的情况下，增加表面的浮雕感。

---

## 何时使用此功能

- 模型的基础纹理有明显的细节（织物纹理、鳞片、刺绣），但没有单独的法线贴图。
- 模型的高光/遮罩贴图编码了您希望作为凹凸细节（bump）而非光泽（gloss）的细节。
- 您想为平坦的材料快速添加一个程序化的细节层。

---

## 如何启用

1. 打开相关类别的材料设置——通常是 [Skin](material_skin)、[Hair](material_hair)、[Opaque](material_opaque) 或 [Custom](material_custom1)。
2. 启用 **Generate Normal Map**。
3. 选择源：**基础贴图** 或 **高光贴图**。
4. 调整强度。

生成的法线贴图只计算一次，并在渲染时使用。除了法线贴图材料本身，它不会产生额外的实时单帧开销。

---

## 与其他纹理增强功能结合使用

生成法线贴图属于与以下功能同属一类纹理增强功能：

- [Specular / Mask Map](specular_map) — 使用一个源贴图来处理多个 PBR 通道。
- [Custom Detail Map](custom_detail_map) — 叠加平铺的细节纹理。
- [Hexagon Detail Map](hexagon_detail) — 程序化的六边形图案细节。

您可以将它们结合使用——例如，使用基础贴图生成的法线贴图 + 顶部的六边形细节凹凸。

---

## 相关页面

- [Specular / Mask Map](specular_map)
- [Custom Detail Map](custom_detail_map)
- [Hexagon Detail Map](hexagon_detail)
- [Material Settings](material_settings)