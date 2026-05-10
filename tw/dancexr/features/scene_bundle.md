---
layout: release
title: 場景包
locale: zh-TW
toc: true
---

# 場景包

<!-- TODO: confirm exact UI flow and bundle format. Drafted from release notes (2024.1, 2024.9). -->

場景包 (Scene Bundle) 是 [儲存場景](save_scene) 加上其參考的實際模型、動作和音樂檔案的集合 — 將所有內容打包在一起，這樣接收者就可以載入整個場景，而不需要先追尋每一個資源。

**2024.1** 版本首次（實驗性地）加入。

---

## 儲存場景 vs 場景包

- **儲存場景** 是一個*參考*資源名稱的小檔案。當您載入它時，DanceXR 會在接收者的內容庫中查找每個參考資源。如果接收者缺少其中一個模型或動作，場景的這部分就載入失敗。
- **場景包** 會將儲存場景**與**所有它所依賴的資源包裹起來。接收者可以直接載入該場景包 — 不會有資源遺失的問題。

當分享場景時，請使用場景包；當為自己使用、且您已擁有所有資源時，請使用儲存場景。

---

## 建立場景包

<!-- TODO: confirm UI path. -->

1. 以您希望的方式設定場景。
2. 開啟場景選單並選擇 **另存為場景包**。
3. DanceXR 會收集所有參考的資源（模型、動作、音樂），並將其打包成單一的場景包檔案。

該場景包包含了場景在另一台機器、在其他國家運作所需的一切內容，接收者無需手動尋找相同的模型資料包。

---

## 載入場景包

將場景包檔案視為任何其他內容庫項目 — 將其拖入您的庫，或透過場景選單開啟。

載入時，DanceXR 會將資源提取到臨時或專屬的場景包位置，並從該處載入場景。預設情況下，這些資源不會合併到接收者的主內容庫中 <!-- TODO: confirm exact behavior here — extracted to a subfolder vs. merged. -->

---

## 限制

<!-- TODO: confirm. Likely:
- Bundle size scales with the assets included; large stage models can produce very large bundles.
- Tier-locked features still require the recipient to have that tier.
- Personal / unauthorized model redistribution — the bundle does not strip licensing constraints. -->

2024.1 版本標記為實驗性；請參閱發布說明以了解當前狀態。

---

## 相關頁面

- [儲存場景](save_scene)
- [內容庫](../preparecontent)
- [角色預設](actor_presets)
- [系統預設](system_presets)