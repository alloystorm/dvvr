---
layout: single
title: 替代材質
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/alternative_textures) | [繁中](/tw/dancexr/features/alternative_textures) | [日本語](/jp/dancexr/features/alternative_textures) | [한국어](/kr/dancexr/features/alternative_textures) | [简中](/zh/dancexr/features/alternative_textures)


## 概述
替代材質是一組可以取代模型的預設材質的材質集。

### 如何運作
DanceXR會掃描模型的套件或資料夾中的材質檔案，尋找與預設材質同名的檔案。如果找到，它將建立一個可能的替代材質清單，並提供給使用者選擇。

當使用者選擇其中一個替代材質時，新的材質將被載入並取代模型使用的預設材質。

### 位置
為了讓DanceXR正確找到材質檔案，您需要將材質檔案放在不同的資料夾中，並且資料夾的位置需要遵循以下規則：

如果模型位於壓縮套件中，將掃描整個套件以尋找替代材質。

如果模型位於資料夾中，您需要將材質檔案放在包含主要模型檔案的資料夾的子資料夾中的不同資料夾中。