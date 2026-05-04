---
layout: feature
title: [Freefly Cam]
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

# [Freefly Cam]

這是一種完全手動的攝影機模式，您可以直接控制位置和旋轉。您可以在場景中自由移動，圍繞某個點環繞，或鎖定演員進行追蹤。


## 移動 (Movement)

**移動阻尼 (Movement Damping)** 平滑攝影機位置的變化——數值越低，攝影機越靈敏；數值越高，則會增加慣性，以達到電影般的緩入/緩出效果。

**使用環繞移動 (Use Orbit Move)** 可將模式從自由飛翔切換到環繞模式，在這種模式下，攝影機不是自由平移，而是圍繞其前方 1.5 米的點旋轉。這對於環繞拍攝主體非常有用。

**限制垂直移動 (Restrict Vertical Move)**（僅限 VR 平台）透過將微小的垂直位移拉回地面水平，防止意外的高度變化。


## 鎖定目標 (Lock On Target)

當啟用 **鎖定目標 (Lock On Target)** 時，攝影機會自動追蹤選定的演員。**追蹤模式 (Tracking Mode)** 可選擇跟隨身體的哪個部位（中心、頭部或胸部）。**目標平滑度 (Target Smoothing)** 和 **預測 (Prediction)** 可以減少跟蹤過程中的延遲和抖動。**自動縮放 (Auto Zoom)** 會調整視野，使目標保持一致的畫面大小；**目標處 FOV 高度 (FOV Height At Target)** 則控制期望的視覺高度。**攝影機晃動 (Camera Shake)** 會根據追蹤延遲添加微妙的手持風格運動。**鎖定旋轉 (Lock Rotation)** 會讓攝影機也跟隨目標的方向。


## 預設 (Presets)

四個內建預設涵蓋了常見的設置：*自由飛翔 (Freefly)*（完全手動控制）、*鎖定演員 (Lock On Actor)*（不縮放的追蹤）、*鎖定 + 縮放全身 (Lock + Zoom Fullbody)*，以及 *鎖定 + 縮放上身 (Lock + Zoom Upper Body)*（更貼近軀幹的構圖）。