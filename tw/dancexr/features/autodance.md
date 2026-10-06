---
layout: release
title: 自動舞蹈
locale: zh-TW
toc: true
---

# 自動跳舞

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

自動跳舞是**第一代**程序化舞蹈生成器。它能從內建的動作庫隨時生成舞蹈動作，並根據音樂的節奏和音量來選擇和混合動作。

自動跳舞已經大部分被 [Auto Dance 2](autodance#auto-dance-2) 和 [Auto Dance 3](autodance3) 取代——較新的版本具備更多變化、更精細的控制，以及更好的音樂同步性。只有當您特別想要原始生成器的行為時，才使用自動跳舞。

---

## 工作原理

- DanceXR 會分析播放的音訊，以檢測**節拍**（時機）和**音量**（能量）。
- 在每個節拍，生成器都會從一套短小的、經過作者設計的舞蹈片段庫中選擇下一個動作，並從前一個動作進行混合。
- 音量較高的部分會觸發更大/更有活力的動作。

您不需要為自動跳舞載入 VMD 檔案——動作是自動生成的。

---

## 設定

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## 何時選擇自動跳舞 vs 新版本

- **自動跳舞（本頁）** — 原始生成器。動作庫較小，音樂反應較簡單。
- **[Auto Dance 2](autodance#auto-dance-2)** — 第二代，池子更大，動作變化更多。
- **[Auto Dance 3](autodance3)** — 當前預設。高度可自定義；整合了 [Sex Motion 3](sex_motion_3) 的共享動作控制系統；使用具備節拍檢測功能的即時音訊分析器。

---

## 相關頁面

- [Auto Dance 2](autodance#auto-dance-2)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)

## Auto Dance 2 {#auto-dance-2}

# 自動舞蹈2

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

自動舞蹈2是**第二代**程序化舞蹈生成器。它相較於原始的 [自動舞蹈](autodance)，具備更大的動作庫，相鄰動作之間的變化更自然，並且與音樂的節拍和音量同步更流暢。

自動舞蹈2本身已經被 [自動舞蹈3](autodance3) 取代，後者使用的是與 [性動作3](sex_motion_3) 共享的現代動作控制系統，並且能整合即時音訊分析器。

---

## 與自動舞蹈1相比的變更

- 內建舞蹈片段庫更大。
- 相鄰動作之間的過渡更平滑，結果不會像幻燈片一樣生硬。
- 對音樂音量的反應更佳——高能量段落的動作會更大氣。

---

## 設定

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## 選擇自動舞蹈2的場合

當您需要一個程序化舞蹈，且該舞蹈具有以下特性時，請使用自動舞蹈2：

- 比原始的自動舞蹈變化性更多。
- 比高度可配置的自動舞蹈3更簡單——旋鈕更少，設置更快。

對於新項目，除非您明確需要自動舞蹈2的特定行為，否則請優先使用 [自動舞蹈3](autodance3)。

---

## 相關頁面

- [自動舞蹈](autodance)
- [自動舞蹈3](autodance3)
- [音樂節拍](music_timing)
- [音訊選項](audio_options)
- [AI in DanceXR](../ai)
