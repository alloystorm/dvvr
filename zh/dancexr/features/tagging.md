---
layout: single
title: 标签
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/tagging) | [繁中](/tw/dancexr/features/tagging) | [日本](/jp/dancexr/features/tagging) | [한국어](/kr/dancexr/features/tagging) | [简中](/zh/dancexr/features/tagging)


## 概述
DanceXR允许您为演员模型和舞蹈动作创建标签，以便更容易管理和检索它们。

{% include video id="kOrp7rESrXQ" provider="youtube" %}

## 自动标记
使用此工具，DanceXR会分析内容库中所有项目的名称，并为您生成可能的标签供您选择。

由于大多数情况下模型的文件名应包含用于识别模型的必要信息，DanceXR将名称分成不同的部分，然后将所有模型的元素组合在一起，生成一个在内容库中最常出现的元素列表。

您只需选择您想要的元素并确认即可自动为您的模型创建标签。

## 合并标签
如果为同一概念创建了多个不同的标签，您可以选择这些标签并选择合并，然后这些标签将合并为一个标签。

## 标签类别和过滤逻辑
对于每个标签，您可以分配一个类别，包括"角色"、"服装"、"发型"、"系列"、"特征"和"通用"。

这会影响在筛选器中选择多个标签时的过滤行为。

同一类别内的标签被视为"或"关系。例如，如果您选择了"Tamaki"和"Leifang"标签，因为它们都属于"角色"类别，筛选结果将是"Tamaki"或"Leifang"。

不属于同一类别的标签将被视为"与"关系。如果您同时选择了"Leifang"和"Bikini"，那么只有具有这两个标签的模型将出现在筛选结果中。