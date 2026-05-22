---
layout: release
title: 螢幕
locale: zh-TW
toc: true
---

# 螢幕

<!-- TODO: confirm exact settings. Drafted from release notes (2024.5 LED screen mode, props release notes). -->

螢幕是一種可自訂的道具資源，可以在平面表面上顯示影像、影片或來自場景攝影機的視圖。您可以使用它作為舞台背景、顯示器、投影螢幕，或作為 [room stage](room_stage) 內的媒體表面。

在早期的版本中，先前「螢幕」道具被拆分為兩個：[Mirror](mirror)（反射式）和 Screen（顯示式）。它們共享基礎的放置和尺寸，但材質和來源設定有所不同。

---

## 來源 (Source)

選擇螢幕顯示的內容：

- **攝影機 (Camera)** — 場景攝影機的視圖（在場景中使用第二個攝影機來觀察舞台上的演員）。
- **影片 (Video)** — 透過 [影片播放器](video_player) 播放的影片檔案。請將影片放置在您 [content library](../preparecontent) 的 `videos/` 資料夾中。
- **影像 (Image)** — 靜態紋理。

---

## 表面模式 (Surface modes)

新增於 2024.4 / 2024.5：

- **標準 (Standard)** — 平面材質；可作為具備可調反射度的電視風格螢幕使用。
- **自發光 (Emissive)** — 螢幕表面會將光線發射到場景中，無需外部照明。
- **LED 螢幕 (LED screen)** — 模擬舞台 LED 燈板的外觀，包括像素網格和發光特徵。適合演唱會舞台。
- **投影機 (Projector)** — 需搭配光樣（light cookie）；請參閱 [Lighting](lighting)。

當道具設定為 *Camera* 模式的螢幕，演員會與附加在該道具上的攝影機進行眼神交流（此模式隨道具拆分時新增）。

---

## 反射 (Reflection)

螢幕表面範圍可以從高光（電視風格的房間反射）到霧面（投影機螢幕行為）。請在表面設定中調整粗糙度 (roughness)。

---

## 可見攝影機模型 (Visible camera model)

當螢幕來源為場景攝影機時，螢幕位置會渲染一個小型攝影機模型。這在演唱會模式下擺拍場景時非常有用。請在螢幕設定中切換此可見性。

---

## 相關頁面 (Related pages)

- [影片播放器](video_player)
- [Mirror](mirror)
- [Props](props)
- [Room Stage](room_stage)
- [Lighting](lighting)