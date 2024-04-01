---
locale: zh-TW
layout: single
toc: true
title: 不透明材料
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/material_opaque) | [繁中](/tw/dancexr/features/material_opaque) | [日本語](/jp/dancexr/features/material_opaque) | [한국어](/kr/dancexr/features/material_opaque) | [简中](/zh/dancexr/features/material_opaque)

## 不透明材料
不透明材料是不透明的材料，不包括皮膚、頭髮、眼睛或嘴唇材料。

這是默認關閉的，以便在材料列表中單獨控制材料。如果您想對所有不透明材料應用一致的設置，您可以啟用它並在這裡進行調整。

## 分類
系統會根據網格（對於XPS模型）或紋理格式（對於PMX模型）的信息自動確定材料是不透明還是透明。有時這可能是錯誤的，因此您可以手動將材料分配到這個類別。

[材料如何分類](material_settings.md#material-category)

## 紋理增強
您可以通過利用特定效果的高光圖，從基本圖或高光圖生成法線圖，以及使用自定義細節圖來改善材料的細節，來增強這個類別的材料的紋理。

* [使用高光/遮罩圖](specular_map.md)
* [生成法線圖](normal_map.md)
* [使用自定義細節圖](detail_map.md)