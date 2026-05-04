---
layout: feature
title: 動作流程
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

# 動作傳遞

一個僅供除錯的面板，允許您選擇性地禁用表演者動畫管線的每個舞台。每個開關都對應於每幀更新循環中的一個傳遞：**重設骨骼**，**動畫**，**位移**，**虛擬骨骼**，**形態後更新**，**繼承骨骼**，**轉換後**，以及**最終更新**。

禁用傳遞對於隔離動畫錯誤或測試單個管線舞台非常有用，但在正常使用中禁用它們會產生錯誤或僵硬的姿態。