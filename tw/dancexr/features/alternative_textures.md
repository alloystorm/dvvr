---
locale: zh-TW
layout: single
title: 替代紋理
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/alternative_textures) | [繁中](/tw/dancexr/features/alternative_textures) | [日本語](/jp/dancexr/features/alternative_textures) | [한국어](/kr/dancexr/features/alternative_textures) | [简中](/zh/dancexr/features/alternative_textures)

## 概述
替代材質是一組可用來取代模型預設材質的材質集合。

### 運作方式
DanceXR 會掃描模型套件或資料夾中的材質檔案，尋找與預設材質同名的檔案。若找到，將建立可能的替代材質清單，並提供給使用者選擇。

當使用者選取某個替代材質時，新的材質會被載入並取代模型所使用的預設材質。選取替代材質也會自動更新材質選單，以反映目前用於材質的活躍設定。

### 位置
為讓 DanceXR 正確找到材質檔案，您需將材質檔案置於不同的資料夾中，且資料夾位置需遵循以下規則：

若模型位於壓縮套件中，將掃描整個套件以尋找替代材質。

若模型位於資料夾中，您需將材質檔案置於包含主要模型檔案的資料夾子資料夾中的不同資料夾中。