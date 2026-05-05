---
layout: feature
title: 網格到布料
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

# 網格轉布料

將行為者（actor）上的任何渲染網格轉換為基於粒子的布料模擬。每個網格都配有自己的配置面板，用於選擇固定頂點（用於錨定布料的骨骼）和模擬參數。

**漸進式啟用 (Gradual Enable)** 會在預設秒數內淡入模擬，防止網格突然「彈入」到位。嵌套的 **Particle Props** 面板定義了全局物理屬性，例如剛度、阻尼和重力乘數，這些屬性會應用於所有轉換的網格。