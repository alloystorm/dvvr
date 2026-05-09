---
layout: release
title: 物理系統
locale: zh-TW
toc: true
---

# 物理系統

DanceXR 為 PMX 和 XPS 格式提供了各自特定的物理系統，此外還建構了自定義的 XPBD（擴展粒子動力學）系統，可模擬布料、軟體和簡化的剛體。

對於 PMX 模型，物理骨架定義在檔案內，並透過 PMX 物理設定暴露出來。

對於 XPS 模型，檔案內沒有骨架，因此您需要使用 XPS 物理工具從零開始設置物理。

PMX 和 XPS 物理預設使用內建的 Unity 物理引擎，該引擎基於 PhysX，但可以切換到 XPBD 後端。

使用 XPBD 系統的布料模擬適用於 PMX 和 XPS 模型，並透過布料模擬設定進行配置。

有關術語（剛體、關節、碰撞器、彈簧力、阻尼、投影距離、投影角度），請參閱 [概念與術語表](concepts#bones-physics-and-colliders)。

> 系統級物理對話框和每個 PMX 模型的獨立對話框的詳細參數參考資料位於 [物理（設定參考資料）](features/physics)。

---

## 兩條路徑：PMX vs XPS

最大的決策點是模型格式。

| | PMX | XPS |
|---|---|---|
| 是否有物理骨架？ | 是 — 內建於檔案 | 否 — 在 DanceXR 中設置 |
| 預設行為 | 開箱即用 | 未設定任何東西不會移動 |
| 調整位置 | [PMX 物理](features/pmx_physics)（每個角色） | [XPS 物理工具](features/xps_physics)（每個角色） |
| 常見陷阱 | 模型作者設置的關節剛度可能需要覆蓋 | 您必須為頭髮、胸部、裙子**選擇骨骼**，它們才能做出任何動作 |

這兩條路徑共用系統級別的對話框（重力、模擬步數），並且下方有一系列專業化的骨骼設定。

---

## 系統級別設定

系統級別的物理設定會全局應用於 DanceXR 中的所有物理模擬，與模型格式或骨架類型無關。

---

## 骨架家族（The rig family）

這些是針對身體部位的物理骨架設定。大部分骨架適用於 PMX 和 XPS，但有些是 XPS 特有的，因為 PMX 模型已經包含這些部位自己的剛體。

### 身體形狀 (Body shape)

[身體碰撞器](features/body_colliders) — 沿著角色的身體配置的膠囊碰撞器，用於讓自由移動的部位（頭髮、布料、裙子）與身體發生碰撞，而不是穿透。

### 頭髮 (Hair)

[頭髮物理](features/hair_physics) — 在根植於頭部的骨骼樹上進行的彈簧骨骼模擬。設置根骨骼，DanceXR 會遍歷子骨骼來構建骨架。

### 裙子和垂飾 (Skirt and dangling)

- [裙子物理](features/skirt_physics) — 具有水平連接的鏈式物理（類似網狀），適用於裙子和邊緣。
- [垂飾物理](features/dangling_physics) — 沒有水平連接的鏈式物理，適用於彩帶、繫帶、耳鏈、動物尾巴，任何懸掛的物體。

差異點在於周圍的鏈是否水平連接。如果沒有這些鏈接，裙子會塌陷；如果沒有這些連接，彩帶會懸掛得很不自然。

### 胸部 (Breast)

[胸部物理](features/boobs_physics) — 基於關節的胸部擺動模擬，並配有反重力以補償恆定的向下拉力。此功能與 XPS 相關，因為 PMX 模型通常會在檔案內包含自己的胸部關節。

### 布料（基於網格）(Cloth (mesh-based))

- [布料模擬](features/cloth_simulation) — 在服裝網格上的 Unity 布料樣式模擬。
- [網格到布料](features/mesh_to_cloth) — 將模型上的網格轉換為布料模擬的物體。

這與裙子/垂飾鏈式物理不同：布料模擬整個網格，而不是一小組控制骨骼。這讓它更重；更適合戲劇性的全身服裝運動。

### 軟體 (Soft body)

- [軟體物理](features/softbody_physics) — 體積形變模擬。<!-- TODO: confirm primary use cases. -->
- [粒子動力學](features/particle_dynamics) — 基於粒子的次要運動模擬。

### 全身 (Whole-body)

- [玩偶骨架](features/ragdoll) — 物理系統接管整個骨骼；角色變得鬆弛。
- [分離物體](features/detach_object) — 釋放一塊骨骼或一個物體，讓物理系統獨立驅動它。
- [次要運動](features/secondary_motion) — 程序化層，在現有動作之上增加呼吸、搖擺和慣性。

---

## 如何選擇

| 需求 | 建議使用 |
|---|---|
| 頭髮擺動 | [頭髮物理](features/hair_physics) — 設置根骨骼 |
| 裙子展開 | [裙子物理](features/skirt_physics) (XPS)，或 [PMX 物理](features/pmx_physics) (PMX) |
| 彩帶、尾巴或繫帶懸掛 | [垂飾物理](features/dangling_physics) |
| XPS 上的胸部擺動 | [胸部物理](features/boobs_physics) — 分配骨骼 |
| 整個服裝像布料一樣模擬 | [布料模擬](features/cloth_simulation) |
| 讓身體部位感覺有體積感 | [軟體物理](features/softbody_physics) |
| 角色倒下 | [玩偶骨架](features/ragdoll) |
| 動態移除身體部位 | [分離物體](features/detach_object) |
| 在任何動作之上增加細微的生命感 | [次要運動](features/secondary_motion) |
| 頭髮/布料實際與身體碰撞 | [身體碰撞器](features/body_colliders) |

---

## 常見問題

| 症狀 | 可能原因 |
|---|---|
| 頭髮/布料穿透身體 | 未設定 [身體碰撞器](features/body_colliders)，或在 [物理設定](features/physics) 中啟用了 *禁用碰撞* |
| 選擇了頭髮但沒有動作 | 選定的骨骼可能不是根骨骼；請檢查 [骨骼結構範例](features/bones) |
| 胸部沒有移動 | 胸部物理開關已開啟，但尚未分配骨骼 — 請參閱 [胸部物理](features/boobs_physics) |
| 骨骼隨時間漂移 | 減少 *投影距離* / *投影角度*，或在 [物理設定](features/physics) 中啟用 *變動重置* |
| 高 FPS 時抖動 | 增加 [模擬](features/simulation) 中的每秒步數 |
| 物理開啟時 FPS 下降 | 減少每秒步數；關閉您不需要的沉重骨架（布料、軟體） |
| 裙子看起來像硬錐體 | 您使用了垂飾物理而非裙子物理；請切換（[裙子](features/skirt_physics) vs [垂飾](features/dangling_physics)） |

---

## 相關頁面

- [概念與術語表](concepts#bones-physics-and-colliders)
- [使用角色模型](actors)
- [物理（設定參考資料）](features/physics) — 系統級和 PMX 特定對話框參數
- [XPS 物理](features/xps_physics) — XPS 骨架配置
- [骨骼結構範例](features/bones) — 骨骼選擇參考骨架

<!-- TODO Phase 3: resolve duplicate pages — cloth_sim.md vs cloth_simulation.md, physics_softbody.md vs softbody_physics.md, transparency.md vs material_transparent.md. Also consider renaming features/physics.md to features/pmx_physics_settings.md to make this hub the canonical "Physics" entry. -->