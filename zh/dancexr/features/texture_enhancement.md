---
layout: release
title: 纹理增强
locale: zh-CN
---


## 纹理增强
您可以通过利用特定效果的高光贴图来增强此类别中材质的纹理，从基础贴图或高光贴图生成法线贴图，以及使用自定义细节贴图来改善材质的细节。

### 高光/蒙版贴图控制
[使用高光/蒙版贴图](texture_enhancement#specular-mask-map)

### 生成法线贴图
* [生成法线贴图](texture_enhancement#generate-normal-map)

### 自定义细节贴图
* [使用自定义细节贴图](texture_enhancement#custom-detail-map)

### 渐变控制

允许沿着渐变路径改变材质属性。

{% include video id="Yi2W_cwufNk" provider="youtube" %}

{% include video id="d8GP3G0wF3M" provider="youtube" %}

{% include video id="atIdSd2TIrA" provider="youtube" %}

## 高光 / 蒙版地图 {#specular-mask-map}

## 高光/遮罩图

使用高光或遮罩图来控制材质的某些属性。例如金属感、环境光遮蔽、发光和光滑度。

这使您可以选择地图的每个通道来控制材质的不同属性。

对于每个属性，选择控制该属性的地图通道，并调整属性的强度。

## 生成法线贴图 {#generate-normal-map}

# 生成法线贴图

DanceXR 可以使用 **基础贴图** 或 **高光贴图** 作为源，为缺少法线贴图的材料合成法线贴图。这可以在无需您编写或提供单独法线贴图的情况下，增加表面的浮雕感。

---

## 何时使用此功能

- 模型的基础纹理有明显的细节（织物纹理、鳞片、刺绣），但没有单独的法线贴图。
- 模型的高光/遮罩贴图编码了您希望作为凹凸细节（bump）而非光泽（gloss）的细节。
- 您想为平坦的材料快速添加一个程序化的细节层。

---

## 如何启用

1. 打开相关类别的材料设置——通常是 [Skin](material_skin)、[Hair](material_hair)、[Opaque](material_settings#opaque-materials) 或 [Custom](material_settings#custom-materials)。
2. 启用 **Generate Normal Map**。
3. 选择源：**基础贴图** 或 **高光贴图**。
4. 调整强度。

生成的法线贴图只计算一次，并在渲染时使用。除了法线贴图材料本身，它不会产生额外的实时单帧开销。

---

## 与其他纹理增强功能结合使用

生成法线贴图属于与以下功能同属一类纹理增强功能：

- [Specular / Mask Map](texture_enhancement#specular-mask-map) — 使用一个源贴图来处理多个 PBR 通道。
- [Custom Detail Map](texture_enhancement#custom-detail-map) — 叠加平铺的细节纹理。
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern) — 程序化的六边形图案细节。

您可以将它们结合使用——例如，使用基础贴图生成的法线贴图 + 顶部的六边形细节凹凸。

---

## 相关页面

- [Specular / Mask Map](texture_enhancement#specular-mask-map)
- [Custom Detail Map](texture_enhancement#custom-detail-map)
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern)
- [Material Settings](material_settings)

## 自定义详细地图 {#custom-detail-map}

## 自定义细节地图
自定义细节地图允许您向材质添加自定义细节地图。该地图可用于向材质添加在基础地图中不存在的细节。

有一个内置的细节地图列表可供使用，您可以将细节地图放置在内容库的纹理文件夹中以供使用。

还有一个程序化的[六边形细节地图](texture_enhancement#hexagon-pattern)，可用于向材质添加六边形细节。

## 六边形图案细节地图 {#hexagon-pattern}

## 六边形图案细节地图
这是一个实时生成的程序化细节地图。可以在支持细节地图和服装效果的材质类别中使用。

## 设置
* 密度：六边形的密度。
* 圆形：使用圆形而不是六边形。
* 大小：六边形中心区域的大小。
* 凸起：六边形边缘的凸起效果强度。可以为负以反转凸起方向。
* 噪音：为每个六边形单元的法线贴图添加随机方向。
* 柔边：使六边形边缘变软，以便它可以融入正常纹理。

## 典型用途
* 为材质添加六边形图案凸起效果：启用细节地图和六边形图案，调整凸起值以获得所需效果。
* 为材质添加闪闪发光效果：启用细节地图和六边形图案，增加密度，增加噪音值，调整光滑度和金属度值以获得所需效果。

{% include video id="G9SSJQieO-E" provider="youtube" %}

{% include video id="BV1VD421W7YK" provider="bilibili" %}
