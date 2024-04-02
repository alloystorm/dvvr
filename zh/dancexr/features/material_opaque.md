---
locale: zh-CN
layout: single
toc: true
title: 不透明材料
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/material_opaque) | [繁中](/tw/dancexr/features/material_opaque) | [日本語](/jp/dancexr/features/material_opaque) | [한국어](/kr/dancexr/features/material_opaque) | [简中](/zh/dancexr/features/material_opaque)

## 不透明材质
不透明材质是不透明的材质，不包括皮肤、头发、眼睛或嘴唇材质。

默认情况下关闭此选项，以便在材质列表中单独控制材质。如果您希望对所有不透明材质应用一致的设置，可以启用它并在此处进行调整。

## 分类
系统会根据网格信息（对于XPS模型）或纹理格式（对于PMX模型）自动确定材质是不透明还是透明。有时可能会出错，因此您可以手动将材质分配到这个类别。

[材质如何分类](material_settings.md#material-category)

## 纹理增强
您可以通过利用特定效果的高光图，从基础图或高光图生成法线图，以及使用自定义细节贴图来改善这个类别的材质的纹理。

* [使用高光/遮罩图](specular_map.md)
* [生成法线图](normal_map.md)
* [使用自定义细节贴图](custom_detail_map.md)