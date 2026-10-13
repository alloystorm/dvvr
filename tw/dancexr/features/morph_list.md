---
layout: release
title: ## PMX 混合形狀變形 (Blendshape Morphs)
locale: zh-TW
toc: true
---

# PMX 形變參數

PMX 模型會附帶一系列由模型作者定義的命名 **形變參數** (morphs) — 包括面部表情、嘴部形狀、服裝切換和身體調整。在 DanceXR 中，您可以在「形變參數列表」(Morph List) 瀏覽和應用它們。

「形變參數列表」(Morph List) 出現在任何加載的 **PMX** 模型的主體（actor）選單中。XPS 模型則使用 [Dressing system](optionals) 代替。

---

## 什麼是形變參數

形變參數 (morph) 是模型儲存的形變 — 頂點位置、骨骼偏移、材質參數或子網格可見性 — 可以通過 0 到 1 的數值進行混合或移除。PMX 模型通常包括：

- **Facial morphs**: 面部形變參數 — 開心、生氣、難過、驚訝、眼睛開/關、嘴型 (a/i/u/e/o)
- **Bone morphs**: 骨骼形變參數 — 細微的骨骼調整
- **Material morphs**: 材質形變參數 — 顏色或透明度變化 (由 [dressing system](optionals) 使用)
- **Vertex morphs**: 頂點形變參數 — 直接網格變形
- **Group morphs**: 群組形變參數 — 以上參數的組合

DanceXR 直接從 PMX 檔案讀取這些參數；您無法在 DanceXR 中自行創建它們。

---

## 使用形變參數列表

1. 開啟主體選單（點擊主體選取圓盤）。
2. 開啟角色選單中的PMX變形控制。
3. 啟用所需PMX變形的 **Override Value**。
4. 調整数值。覆寫關閉時使用正常動作驅動的值，需要已解鎖該功能的版本。

除非您更改或重新加載模型，否則形變參數都會保持應用狀態。某些形變參數（例如面部表情）在 [Facial control](facial_control) 和 [Blink, breathing & eye contact](lifelike_motions#eye-contact) 處於活躍狀態時，將會被覆蓋。

---

## 提示

- **Morph names depend on the author**. 日本模型作者通常會用日語命名面部形變參數 (まばたき, あ, い…)。英文模型通常使用英文名稱。
- **Material morphs** 在這裡顯示的通常與 [Dressing system](optionals) 呈現的相同；無論從哪個位置應用，效果都是一致的。
- 清單較長時捲動查看作者定義的名稱。使用 **Application Settings → Use Translated Names** 對照翻譯名稱與原名，必要時重新載入模型。

---

## 相關頁面

- [Dressing system](optionals)
- [Facial control](facial_control)
- [Blink, breathing & eye contact](lifelike_motions#eye-contact)
- [Concepts & glossary](../concepts)
