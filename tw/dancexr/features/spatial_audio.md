---
layout: release
title: 空間音訊
locale: zh-TW
toc: true
---

# 空間音訊

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. -->

空間音訊從三維空間的特定位置播放場景音訊，而非單純的立體聲混音。將音訊錨定到角色的頭部，使聲音隨著該角色移動，這在 VR 和多角色舞台上能帶來強烈的臨場感。

Added in **2024.9**.

---

## 啟用空間音訊

<!-- TODO: confirm exact menu path. Drafted from the release notes which name the option as "Spatialize" under Playback Options. -->

1. 開啟 [Playback Options](playback_options)。
2. 開啟 **空間化**。
3. 從下拉式選單中選擇一個角色 — 該角色的 **頭部位置** 將成為音訊來源。

音訊隨距離衰減，並相對於攝影機或 VR 頭戴設備正確環繞。

---

## 行為

- 音訊來源會隨著選擇的角色移動的頭部骨骼而移動。
- 在 VR 中，此效果使用頭部追蹤，因此轉動頭部會自然地改變左右平衡。
- <!-- TODO: confirm whether stereo is preserved or audio is downmixed to mono at the source. -->
- <!-- TODO: confirm distance attenuation curve and whether it is configurable. -->

---

## 與語音同步 (LipSync) 的搭配

空間音訊與同一版本中引入的 [audio-driven lip sync](lipsync) 自然搭配：將音訊錨定到角色的頭部並從相同音訊驅動該角色的口型，能產生一致的「這個角色正在說話」的效果。

---

## 限制

<!-- TODO: confirm. Likely areas to verify: which audio types this applies to (music vs voice chat vs video), behavior with multiple actors, behavior on Android / Quest, behavior in AR mode. -->

---

## 相關頁面

- [Playback Options](playback_options)
- [Audio Options](audio_options)
- [LipSync](lipsync)
- [AI Voice Chat](ai_chat)