---
layout: release
title: 透明材料
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---


## 透明度材料
透明材料是透明的材料，不包括皮膚、頭髮、眼睛或嘴唇材料。

這是默認關閉的，以便在材料列表中單獨控制材料。如果您想對所有透明材料應用一致的設置，可以啟用它並在此進行調整。

## 分類
系統會根據網格（對於XPS模型）或紋理格式（對於PMX模型）的信息自動確定材料是不透明還是透明。有時這可能是錯誤的，因此您可以手動將材料分配到這個類別。

[材料如何分類](material_settings#material-category)

## 紋理增強
您可以通過利用特定效果的高光圖，從基本圖或高光圖生成法線圖，以及使用自定義細節圖來改善材料的細節，來增強此類材料的紋理。

* [使用高光/遮罩圖](specular_map)
* [生成法線圖](generate_normal_map)
* [使用自定義細節圖](custom_detail_map)