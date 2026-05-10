---
layout: release
title: 音訊選項
locale: zh-TW
toc: true
---

# 音訊選項

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.5, 2024.7, 2024.9, 2025.5, 2026.2). -->

音訊選項控制當前 [舞步場景](dance_set) 中的音訊軌如何播放，包括循環、音量和音訊來源在場景中的定位。

---

## 播放模式

選擇音訊如何根據您載入的內容進行推進：

- **單曲 (Single)** — 播放當前曲目一次。
- **循環 (Loop)** — 重複播放當前曲目。如果設定了循環區域（開始/結束時間），則僅循環該區域。
- **隨機 (Shuffle)** — 從隊列中隨機選擇下一個曲目。
- <!-- TODO: confirm whether "Sequential / next in folder" is also a separate mode. -->

音訊循環與動作循環是獨立的（2024.5 加入）— 您可以只讓音訊循環，同時讓動作播放，反之亦然。

---

## 音量

音訊軌的標準主音量滑桿。

<!-- TODO: confirm whether per-actor / per-source volume controls live here or under Playback Options. -->

---

## 空間音訊

將音訊錨定到場景的 3D 位置，而不是播放為平面立體聲混音。參見 [空間音訊](spatial_audio)。

---

## 音訊分析

音樂 BPM 檢測、節拍檢測和副歌段數據均來自此層。參見：

- [音樂時序](music_timing) 以設定 BPM 和節拍偏移。
- [自動更新](autoupdate) 以使用音訊電平/節拍作為其他設定的數據來源。
- [節拍環 (Beats Ring)](beats_ring) 和較新的 Audio Visualizer，用於視覺化音訊的響應。

即時音訊分析器在 2025.5 加入了節拍檢測功能，因此程序化動作可以在沒有預計算時序的情況下響應實時節拍。

---

## 音訊 / 動作同步

當音訊時間和動作時間出現漂移時，DanceXR 可以自動重新同步它們。選擇同步 **音訊到動作** 還是 **動作到音訊** — 參見 [動作設定](motion_settings)。

音訊時序在 2026.2 得到進一步改進，以減少變動幀率下的卡頓現象；2026.3 修復了幀率顯著波動時的振盪問題。

---

## 相關頁面

- [播放選項](playback_options)
- [音樂時序](music_timing)
- [舞步場景](dance_set)
- [空間音訊](spatial_audio)
- [唇形同步 (LipSync)](lipsync)