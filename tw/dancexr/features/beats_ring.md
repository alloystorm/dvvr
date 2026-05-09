---
layout: release
title: 節拍環
locale: zh-TW
---

# 節拍光環

<!-- TODO: full description. The Beats Ring is referenced as a tile on /dancexr/features under Stage & Props but no other page describes it. Likely an audio-reactive visualizer ring; confirm and fill in. -->

「節拍光環」是一個會隨著音樂脈動的音訊反應式視覺化道具。它是 [auto-update](/dancexr/features/autoupdate) 的資料來源之一，這意味著其他設定可以根據其輸出自動驅動。

---

## 作用

<!-- TODO: confirm shape (ring? particles? geometry?), where it is rendered (around the actor? on the stage?), how it scales with audio. -->

「節拍光環」接收當前的音訊訊號，產生一個由節拍驅動的值，可用於：

- 在演員或舞台周圍渲染一個可見的光環或脈衝效果。
- 與音樂同步驅動其他自動更新參數（例如：燈光強度、材質參數、運動速度）。

---

## 啟用方式

<!-- TODO: confirm the menu path. Likely under environment menu or a per-actor setting. -->

---

## 設定

<!-- TODO: list. Possibly: visibility, color, scale, sensitivity threshold, smoothing. -->

---

## 相關頁面

- [自動更新](/dancexr/features/autoupdate) — 將節拍光環作為其他設定的資料來源
- [音樂時機](/dancexr/features/music_timing) — 將運動同步到音樂
- [音訊選項](/dancexr/features/audio_options)