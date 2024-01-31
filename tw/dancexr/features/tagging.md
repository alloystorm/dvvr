---
locale: zh-TW
layout: single
title: 標籤
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/tagging) | [繁中](/tw/dancexr/features/tagging) | [日本語](/jp/dancexr/features/tagging) | [한국어](/kr/dancexr/features/tagging) | [简中](/zh/dancexr/features/tagging)


## 概述
DanceXR 允許您為演員模型和舞蹈動作創建標籤，以便更容易管理和檢索它們。

{% include video id="kOrp7rESrXQ" provider="youtube" %}

## 自動標籤
使用此工具，DanceXR 將分析您內容庫中所有項目的名稱，並為您生成可能的標籤供您選擇。

由於大多數情況下模型的文件名應包含識別模型的必要信息，DanceXR 將名稱拆分為不同部分，然後將所有模型的元素結合在一起，生成在您的內容庫中最常出現的元素列表。

您只需要選擇您想要的元素並確認即可。然後標籤將自動為您的模型創建。

## 合併標籤
如果為同一概念創建了多個不同的標籤，您可以選擇這些標籤並選擇合併，然後這些標籤將合併為一個。

## 標籤類別和篩選邏輯
對於每個標籤，您可以從「角色」、「服裝」、「髮型」、「系列」、「特色」和「通用」中分配一個類別。

這會影響在篩選器中選擇多個標籤時的篩選行為。

同一類別中的標籤被視為「或」關係。例如，如果您選擇「Tamaki」和「Leifang」標籤，因為它們都屬於「角色」類別，篩選結果將是「Tamaki」或「Leifang」。

不屬於同一類別的標籤將被視為「且」關係。如果您選擇「Leifang」和「比基尼」，則只有具有這兩個標籤的模型將出現在篩選結果中。