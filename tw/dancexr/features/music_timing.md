---
layout: release
title: 音樂節奏
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


## 總覽
音樂節奏資訊對於所有程序化動作來說都非常重要，因為它用於將動作與音樂匹配。若沒有它，BPM（每分鐘節拍數）將預設為120，且不會與音樂同步。

## 示範
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## 點擊節拍
我們提供了一個「點擊節拍」功能，讓您能輕鬆準確地設定節奏資訊。

您需要做的是播放音樂，並在每次節拍下降時點擊按鈕。這個程序需要約4次點擊來計算平均BPM與偏移值。您可以從地板上發光的圓環看出，當設定正確時，光點能完美與音樂節拍匹配。若第一次沒設置正確也無妨，只需繼續點擊節拍，直到一切看起來正確為止。

先前我們在應用程式中與應用程式捆綁了一個命令列工具，用於解析庫中每個音樂檔案並生成節奏資訊，此方法仍然有效，但使用起來較困難，且僅支援WAV格式，無法從ZIP檔案讀取。以下是舊方法的視頻示範：

{% include video id="chI-3GQS08Q" provider="youtube" %}

## 音訊節奏改進 (v2026.2)
DanceXR 2026.2 包含改進的音訊節奏同步功能，進一步降低音訊/動作不同步的問題，並消除因幀率波動導致的偶發卡頓。在 v2026.3 中，額外修復了因音訊時間平滑處理在幀率大幅波動時可能引發的震盪問題。