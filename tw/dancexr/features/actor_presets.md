---
layout: release
title: 角色預設
locale: zh-TW
toc: true
---

# 角色預設集

角色預設集儲存角色設定的快照—包括物理、材質、服裝、動態偏好等—以便您稍後將相同的配置應用到相同的模型，或應用到具有相似骨架的不同的模型上。

新增於 **2024.1**。預設集儲存在 [內容庫](../preparecontent) 的 `presets/` 目錄下，這意味著在相同的 DanceXR 版本中使用者之間可以共享預設集。

---

## 預設集包含的內容

<!-- TODO: confirm the exact list of settings included. -->

一個典型的角色預設集捕獲了：

- 每個角色的 [動態設定](actor_motion_settings)
- [服裝系統](optionals) 的狀態（可見/隱藏的項目）
- 每個槽位（slot）的 [材質設定](material_settings)
- [物理](physics) 配置（PMX 或 XPS，包括 [頭髮](hair_physics)、[裙子](skirt_physics)、[胸部](boobs_physics)、[身體碰撞體](body_colliders)）
- [腳部調整](feet_adjustment) 和 [縮放與偏移](scale_offset)

預設集**不包含**的內容：

- 模型檔案本身（預設集參考設定，而非資源）。
- 系統級別設定——這些儲存在 [系統預設集](#system-presets) 中。
- 場景組成（舞台、照明、攝影機）——這些儲存在 [場景](save_scene) 中。

---

## 儲存與載入

<!-- TODO: confirm exact UI path and naming flow. -->

1. 以您想要的樣式配置一個角色。
2. 開啟角色選單，然後是 **工具選單**（扳手和錘子圖標）。
3. 儲存預設集；為其命名。
4. 若要應用，請在任何角色的相同工具選單中選擇一個按名稱儲存的預設集。

預設集儲存在內容庫的 `presets/` 目錄下。您可以在機器之間複製預設集檔案。

---

## 預設集跨模型的重用性

當應用於以下場景時，預設集是最可靠的：

- 與您儲存它**相同的模型**。
- 一個**相關聯的模型**（相同的來源角色，相同的骨架）。
- 一個**格式相同且骨架相似的模型**（PMX 到 PMX，相似的骨骼命名）。

對於非常不同的模型，依賴於骨骼名稱的設定——例如 XPS 物理骨架、[骨骼映射器](bone_mapper) 覆寫——可能無法乾淨地轉移。

---

## 系統預設集

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

系統預設集儲存的是整個場景的設定（照明、環境、攝影機、圖形），而不是每個角色的設定。儲存和應用流程相似；系統預設集是單獨儲存的。

---

## 相關頁面

- [儲存場景](save_scene) — 捕獲整個場景，而不僅僅是單一角色的設定
- [場景包](scene_bundle) — 將一個儲存的場景及其所依賴的資源打包
- [內容庫](../preparecontent) — `presets/` 資料夾位置
- [角色選單與工具](actor_tools)