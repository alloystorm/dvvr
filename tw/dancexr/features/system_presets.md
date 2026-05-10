---
layout: release
title: 系統預設
locale: zh-TW
toc: true
---

# 系統預設

<!-- TODO: confirm exact contents and UI flow. Drafted from the 2024.1 release notes. -->

系統預設可將**場景級和環境設定**——例如圖形品質、燈光、天空、地面——儲存為一個單一的命名預設，之後您可以重新套用或與他人分享。

新增於 **2024.1**。預設以獨立的 JSON 檔案儲存於 [內容庫](../preparecontent) 中。

---

## 系統預設包含內容

<!-- TODO: confirm the exact list of settings captured. The release notes call out: graphics quality, lighting, sky, ground. There are likely more. -->

一個典型的系統預設包含以下設定：

- [圖形設定](graphics) — 渲染品質、後期效果。
- [燈光](lighting) — 方向性與環境光設置、[光球](light_ball)。
- [天空與雲](skymap) 和 [天空顏色](sky)。
- [地面](ground) — 材質、僅陰影模式等。
- <!-- TODO: confirm whether camera, weather, simulation, or audio settings are included. -->

系統預設**不**包含以下內容：

- 單個角色設定 — 這些儲存在 [角色預設](actor_presets) 中。
- 已載入的角色、動作、音樂或舞台資源 — 這些儲存在 [儲存的場景](save_scene) 中。

---

## 儲存與載入

<!-- TODO: confirm exact UI path. -->

1. 將場景配置成您想要的樣子。
2. 開啟相關的場景/系統選單。
3. **儲存預設** — 為其命名。預設會作為 JSON 檔案寫入內容庫中的 `presets/` (或 system-presets 子資料夾)。
4. **載入預設** — 根據名稱選擇已儲存的預設進行套用。

由於每個預設都是一個獨立的檔案，您可以將其複製到不同機器間或與其他使用者分享。

---

## 系統預設與其他預設類型比較

| 預設 | 範圍 | 典型包含內容 | 頁面 |
|---|---|---|---|
| **系統預設** | 場景級 | 圖形、燈光、天空、地面 | (本頁) |
| **角色預設** | 每個角色 | 材質、物理、服裝 | [角色預設](actor_presets) |
| **儲存的場景** | 所有內容 | 場景級 + 角色 + 動作 + 指定 | [儲存的場景](save_scene) |
| **場景包** | 所有內容 + 資源 | 儲存的場景 + 模型 / 動作 / 音樂檔案 | [場景包](scene_bundle) |

---

## 相關頁面

- [角色預設](actor_presets)
- [儲存的場景](save_scene)
- [場景包](scene_bundle)
- [內容庫](../preparecontent)