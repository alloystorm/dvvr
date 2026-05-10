---
layout: release
title: ## 使用實體
locale: zh-TW
toc: true
---

# 處理角色

角色（actor）是載入場景中的模型。DanceXR 會即時調整模型的骨骼以適應動作，並使用物理系統模擬頭髮和服裝的動態。

您可以透過更改材質、套用紋理，或使用裝扮系統（dressing system）來切換服裝單品，來客製化模型的外觀。您還可以調整模型的比例和位置，並微調其與舞台和其他角色的互動方式。

關於這裡使用的術語（角色、選取圓盤、縮放立方體、裝扮系統）的詞彙表，請參閱 [Concepts & glossary](concepts)。

---

## 載入角色

DanceXR 會讀取三種模型格式：

- **PMX** — MikuMikuDance 格式。包含內建的骨骼層級、物理綁定和形態列表。
- **XPS** — XNALara / XPS 格式（`.xps`, `.mesh`, `.mesh.ascii`）。不包含物理綁定或標準骨骼，因此您需要在 DanceXR 中設定這些內容。
- **FBX** *(預覽版，2025.9 起)* — 通用 3D 格式。DanceXR 目前只能載入模型本身，無法載入嵌入的動畫或其他 FBX 專屬功能。和 XPS 一樣，FBX 在動畫播放前需要透過 [骨骼映射器](features/bone_mapper) 進行映射。

所有這三種格式也可以打包成 **ZIP**。請參閱 [ZIP 格式](features/zip_format) 以了解檔案命名規則和編碼。

### 兩種載入方式

- **拖放** 模型檔案（或 zip）到 DanceXR 視窗。對於單次載入非常快速。
- **內容庫** — 將模型放入您 [content library](preparecontent) 中的 `actors/` 資料夾。它們將出現在角色選單的 *載入模型* 清單中。

### 替換 vs 新增

預設情況下，載入模型會 **替換** 當前選取的角色。如果您想將模型作為額外的角色新增，請點擊模型名稱旁邊的 **+** 圖標。多角色場景需要專業版（paid build）——請參閱 [Download & editions](download)。

### 載入選項

[Loader options](features/loader_options) 控制新角色的載入方式：快取大小、紋理壓縮、過渡效果和自動角色切換。

---

## PMX 與 XPS 與 FBX — 有何不同

大多數設定在這三種格式上都是相同的。它們分歧的地方值得了解：

| 主題 | PMX | XPS | FBX (預覽版) |
|---|---|---|---|
| 骨骼 | 檔案中的標準骨骼名稱 | 透過 [骨骼映射器](features/bone_mapper) 映射 | 透過 [骨骼映射器](features/bone_mapper) 映射 |
| 物理綁定 | 建置在檔案內（[PMX 物理](features/pmx_physics)） | 物理設定 | XPS 物理設定 |
| 形態 / 混合形狀 | [形態列表](features/morph_list) | 無 — 請改用 [裝扮系統](features/optionals) | 無 |
| 服裝切換 | 材質形態（PMX） | 選用物品（XPS）— 使用相同 UI ([裝扮系統](features/optionals)) | 無 |

如果本指南提到「僅限 PMX」或「僅限 XPS」，那就是原因所在。FBX 支援作為預覽版（截至 2025.9），模型幾何和材質會載入，但檔案內部的動畫和其他 FBX 功能會被忽略。

---

## 角色選單

每個角色腳下都有一個黃色的 **選取圓盤**。點擊它會開啟角色選單 — 這是所有角色相關設定的中央樞紐。請參閱 [Actor menu & tools](features/actor_tools) 了解完整詳情。

選單分為以下幾個組件：

- **動作** — 分配的動作、[隊形](features/formation) 槽位和特定模型的動作設定。
- **最近修改** — 快速跳轉到您剛剛修改過的對話框。請參閱 [Recently modified settings](features/recently_modified)。
- **裝扮與紋理** — [裝扮系統](features/optionals)、[骨骼映射器](features/bone_mapper) (XPS)、[alternative textures](features/alternative_textures)。
- **材質** — 每槽位設定：皮膚、頭髮、眼睛、嘴唇、不透明、透明、自定義。請參閱 [Appearance & materials](appearance) 了解槽位之間的搭配關係。
- **設定** — 物理、[feet adjustment](features/feet_adjustment)、[facial control](features/facial_control)、[eye contact](features/eyecontact)、[troubleshooting](features/troubleshooting)。
- **專業版** (paid builds) — [outfit & body paint](features/outfit)、[accessory](features/accessory)、[ragdoll](features/ragdoll)、[motion override](features/motion_override)、[light ball](features/light_ball)、進階物理、NSFW 疊層。
- **形態列表** (僅限 PMX) — [PMX 混合形狀](features/morph_list)。
- **工具** (扳手和錘子圖標) — 收藏、標籤、[spectator](features/spectator_mode)、向上/向下移動、重置、[duplicate](features/actor_tools#tools-menu)、重新載入、[3D snapshot](features/snapshot_3d)、移除。

---

## 多角色場景

當舞台上有超過一個角色時，有三個功能用於處理群組行為：

- [Formation](features/formation) — 將角色排列成特定隊形（直線、網格、自定義）。順序由工具選單中的 **Move Up** / **Move Down** 決定。
- [Actor playlist](features/actor_playlist) — 隨時間依序播放清單中的模型，可選同步音樂。
- [Attach to actor](features/attach_to_actor) — 將一個角色或配件父級化給另一個角色（拿著的物品、懸掛物、配對動作）。

使用 [Spectator mode](features/spectator_mode) 可以讓模型停留在舞台上，但排除其自動分配的動作和隊形槽位。

[Global actor control](features/global_actor_control) 對每個角色套用一個設定——當您希望所有載入的模型共享相同的物理調整、裝扮或材質時非常有用。

---

## 快照和預設

儲存您所建構內容有三種方式：

- [3D snapshot](features/snapshot_3d) — 將當前姿態匯出為 OBJ 格式，可用於其他 3D 工具。
- [Actor presets](features/actor_presets) — 儲存角色的設定（材質、物理、裝扮），以便日後將相同的外觀套用給相同模型，或相似的模型。
- [Save scene](features/save_scene) 和 [scene bundle](features/scene_bundle) — 捕捉包含所有角色、動作、舞台和配置的整個場景。

---

## 遇到錯誤

症狀先行式排除故障：

| 症狀 | 應檢查處 |
|---|---|
| 模型載入但一切都是白色的 | [FAQ → Model loads but everything is white](faq) |
| 模型固定在標準姿勢 | [XPS bone mapper](features/bone_mapper)、[Example bone structure](features/bones) |
| 漂浮、下沉、在地面滑動 | [Feet adjustment](features/feet_adjustment) |
| 尺寸或位置不正確 | [Scale & offset](features/scale_offset) |
| 頭髮/裙子/布料不移動或抖動 | [Physics system](physics) |
| 每個模型有奇怪的行為 | [Actor troubleshooting](features/troubleshooting) |
| 應用程式層級崩潰，無法啟動 | [Troubleshooting](features/troubleshooting)、[FAQ](faq) |

---

## 相關頁面

- [Concepts & glossary](concepts)
- [Appearance & materials](appearance)
- [Physics system](physics)
- [Motion system](motion)
- [Actor menu & tools](features/actor_tools)
- [Content library](preparecontent)