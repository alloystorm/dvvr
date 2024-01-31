---
locale: zh-TW
layout: single
title: 載入選項
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/loader_options) | [繁中](/tw/dancexr/features/loader_options) | [日本語](/jp/dancexr/features/loader_options) | [한국어](/kr/dancexr/features/loader_options) | [简中](/zh/dancexr/features/loader_options)


## 概述
載入選項包含在載入演員模型時的選項，並提供演員快取的管理。

### 演員快取
已載入的演員模型會被快取在記憶體中，以便下次載入時能立即使用。在快取管理器中，您可以更改快取的模型數量，並從快取中刪除特定的模型。

### 保留選項
一旦開啟，當替換演員時，原演員的設定將被保留並應用於新的演員模型。

### 轉場效果
選擇並配置演員模型淡入淡出時的動畫。

### 自動演員更換
這是一個特殊功能，當此滑桿的值超過某個閾值時，它會自動用快取的演員替換舞台上的當前演員。

例如，如果快取中有4個演員。滑桿的值和相應的演員將為：
* 0-0.25：演員1
* 0.25-0.5：演員2
* 0.5-0.75：演員3
* 0.75-1：演員4

這個功能的常見用法是啟用[自動更新](autoupdate)並將其設置為時間軸的0-100%。當歌曲在前25%時，第一個演員將出現在舞台上，然後當它超過25%的標記時，系統將開始從演員1過渡到演員2。