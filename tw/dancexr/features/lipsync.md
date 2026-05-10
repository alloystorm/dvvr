---
layout: release
title: 口型同步
locale: zh-TW
toc: true
---

# 唇形同步

LipSync 從音訊訊號即時驅動角色的嘴型，讓角色彷彿在播放任何音訊內容時說話或唱歌。與內建於 [AI Voice Chat](ai_chat) 的舊版唇形同步不同，此系統**可在所有平台**上使用，包括 Android 和 Quest。

增補於 **2024.9**。

---

## 啟用唇形同步

<!-- TODO: confirm exact UI path. -->

1. 在 [Playback Options](playback_options) 中全域開啟 LipSync。
2. 對於每個應該動嘴的角色，開啟 [Facial Control](facial_control) 並啟用 **LipSync**。

這兩個開關都需要：全域開關控制是否分析音訊；單角色開關則控制哪些角色會響應此音訊。

---

## 與空間音訊搭配

LipSync 與 [Spatial Audio](spatial_audio) 自然搭配——將音訊固定到角色的頭部，並在該角色上啟用 LipSync，結果看起來就像「這個角色正在說話」。

---

## 與 AI 語音聊天搭配

[AI Voice Chat](ai_chat) 驅動的語音內容，可讓 LipSync 系統像分析音樂或視訊音訊一樣來分析。 <!-- TODO: confirm whether AI Voice Chat uses LipSync directly, or its own internal mouth driver, or both. -->

---

## 設定

<!-- TODO: list. Likely candidates: sensitivity / gain, smoothing, mouth-open intensity, which morph(s) drive what. -->

---

## 限制

<!-- TODO: confirm. Areas to verify:
- Does it require specific blendshapes / morphs (a / i / u / e / o)? What if the model lacks them?
- Does it work with PMX, XPS, and FBX equally?
- Latency on Android / Quest. -->

---

## 相關頁面

- [Playback Options](playback_options)
- [Facial Control](facial_control)
- [Spatial Audio](spatial_audio)
- [AI Voice Chat](ai_chat)
- [Blink, Breathing & Eye Contact](eyecontact)