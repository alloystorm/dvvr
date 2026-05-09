---
layout: release
title: 概念與術語表
locale: zh-TW
toc: true
---

# 概念與詞彙表

這是一份用於 DanceXR 文件中術語的簡短參考指南。如果一個頁面使用了您不認識的詞，它很可能在這裡定義了。每個條目都會連結到其完整的功能頁面。

---

## 核心實體

**角色（Actor）**
：載入場景的角色的模型。角色來自 PMX、XPS 或 FBX 檔案（FBX 支援預覽至 2025.9）。每個角色都有其自身的動態、材質、物理和行為設定。多個角色可以共用一個舞台；每個角色腳下的**選取圓盤**是您選擇對象的方法。參閱 [角色菜單與工具](/dancexr/features/actor_tools)。

**動作（Motion）**
：驅動角色骨骼的動畫。動作通常來自 VMD 或 BVH 檔案。動作也可以是程序化的（在執行時期生成）— 請參閱下方的 *程序化動作*。

**音訊（Audio）**
：音樂或聲音檔案（PC 上為 OGG、WAV；行動裝置上為 MP3），可供回放，通常與動作搭配組成**舞動集**。

**舞動集（Dance set）**
：包含一個音訊檔案以及一個或多個角色動作的組合包，可選配攝影機動作。當音訊檔案和匹配的動作檔案共用資料夾或 zip 時，DanceXR 會自動檢測舞動集。參閱 [舞動集](/dancexr/features/dance_set)。

**舞台（Stage）**
：角色站立的 3D 環境。舞台可以從外部 3D 模型載入，或設定為內建的 [房間舞台](/dancexr/features/room_stage)。

**道具（Prop）**
：場景的一部分 3D 模型，但不屬於角色—例如家具、螢幕、鏡子、基本幾何形狀。參閱 [道具](/dancexr/features/props)。

**配件（Accessory）**
：附著在角色骨骼上的 3D 模型—例如帽子、武器、手持物品。不同於道具，因為它會跟隨角色。參閱 [配件](/dancexr/features/accessory)。

**場景（Scene）**
：螢幕上所有內容的完整狀態—包括角色、動作、舞台、燈光、攝影機和設定。場景可以儲存到磁碟並重新載入。參閱 [儲存場景](/dancexr/features/save_scene)。

**場景包（Scene bundle）**
：將一個場景與其所依賴的所有模型和動作檔案一起打包，以便無需遺失資源就能分享。參閱 [場景包](/dancexr/features/scene_bundle)。

---

## UI 元素

**菜單欄（Menu bar）**
：屏幕底部的圖標條（或在 VR 中漂浮在您前方）。左側的五個圖標分別開啟了系統、環境、場景、音訊/動作和角色菜單。回放控制在右側。

**選取圓盤（Selection disc）**
：畫在每個已載入角色腳下的黃色圓圈。點擊它會開啟角色菜單。拖動它來移動角色。在拖動時，滑鼠滾輪會旋轉，水平滾輪（或 VR 拇指搖桿）會垂直移動角色。

**輔助格體（Gizmo cube）**
：當支援的動作或工具處於活動狀態時，出現在身體部位的虛擬立方體（例如：空閒動作、自動舞蹈、動作覆蓋和許多其他動作）。拖動一個面來沿其移動；使用滾輪或拇指搖桿來旋轉。每個角色通常有五個輔助格體：兩隻手、兩隻腳、一個軀幹。參閱 [角色菜單與工具](/dancexr/features/actor_tools#gizmo-cube)。

**切換狀態（Toggle states）**
：點擊空白區域可以循環切換三個 UI 狀態。**UI 模式**顯示菜單和圓盤。**控制模式**隱藏菜單但保留角色選取圓盤。**沉浸式模式**隱藏所有元素以達到乾淨的觀看效果。參閱 [控制與 UI](/dancexr/controls)。

**進度條（Progress bar）**
：最底部的條狀介面，顯示當前動作/音訊名稱和播放位置。點擊可播放/暫停；拖動可快轉。

---

## 骨骼、物理和碰撞體

**骨骼（Bone）**
：模型骨架中的一個點。動作作用於動畫骨骼；物理模擬附加到骨骼上的部位。

**關節（Joint）**
：連接兩個物理物體的約束，允許它們在設定的限制內擺動或伸展。大多數布料和頭髮的行為來自關節鏈。

**碰撞體（Colliders）**
：碰撞體定義了物理物體的形狀，用於碰撞檢測。碰撞體可以是靜態的（嚴格跟隨動畫的骨骼），也可以是動態的（由物理引擎使用速度、重力和約束模擬）。可以將碰撞體分配給一個群組，並啟用或停用群組間的碰撞。

**剛體（Rigid body）**
：一個具有形狀、質量和定義運動類型的物理物體。PMX 模型在檔案中包含剛體。XPS 模型則不包含，這就是為什麼 XPS 物理需要手動配置。

**彈簧力/阻尼（Spring force / damping）**
：關節將骨骼拉回其靜止位置的力（彈簧），以及抵抗與速度成比例運動的力（阻尼）。這些是每個物理頁面中的核心控制參數。

**投影距離/投影角度（Projection distance / projection angle）**
：PMX 關節中的安全限制。如果兩個連接的物體漂移超過投影閾值（或旋轉過多），它們會彈回，以防止模擬失控。

---

## 材質與外觀

**材質槽（Material slot）**
：模型上的材質類別。DanceXR 將材質分組為 Skin（皮膚）、Hair（頭髮）、Eyes（眼睛）、Lips（嘴唇）、Opaque（不透明）、Transparent（透明）和 Custom（自訂）槽。槽上的設定會應用到該類別中的所有材質。參閱 [材質設定](/dancexr/features/material_settings)。

**服裝系統（Dressing system）**
：用於切換模型部分可見性的機制。它有兩種工作方式：**材質變體**（PMX）和**可選物品**（XPS）。用於更換服裝、移除配件、換髮。參閱 [服裝系統](/dancexr/features/optionals)。

**替代紋理（Alternative textures）**
：額外的紋理集。當模型資料夾或 zip 中的檔案與模型紋理共用名稱時，DanceXR 會自動檢測。讓使用者在執行時期無需編輯模型即可更換外觀。參閱 [替代紋理](/dancexr/features/alternative_textures)。

**身體彩繪（Body paint）**
：在皮膚材質之上的疊加層，從放置在 `texture/drawing` 資料夾中的圖像繪製而成。參閱 [服裝與身體彩繪](/dancexr/features/outfit)。

**卡通陰影（Toon shading）**
：賽璐珞風格的動畫陰影。為每個角色切換；影響光線的包裹方式和陰影的漸變。參閱 [卡通陰影](/dancexr/features/toon_shading)。

**透明度深度預通道（Transparency depth prepass）**
：一種在繪製透明表面之前運行深度通道的渲染技術，只選擇頂層。這解決了排序問題，但意味著堆疊的透明層（多層頭髮、嵌套的天空球）只顯示頂層。在圖形設定中切換。提及於 [FAQ](/dancexr/faq#i-can-see-through-hair-materials)。

---

## 動作概念

**程序化動作（Procedural motion）**
：在執行時期生成的動作，而非從檔案中讀取。包括 [空閒動作](/dancexr/features/idle_motion)、[走秀](/dancexr/features/catwalk)、[自動舞蹈 1/2/3](/dancexr/features/autodance3)、[栩栩如生動作](/dancexr/features/lifelike_motions) 以及程序化的 [次要動作](/dancexr/features/secondary_motion) 層。

**動作層（Motion pass）**
：疊加在另一個動作之上的動作層。它允許您將一個動作作為基礎播放，並用另一個動作覆蓋特定的骨骼。參閱 [動作層](/dancexr/features/motion_passes)。

**動作覆蓋（Motion override）**
：對動作中特定骨骼的目標式替換。有助於修復手臂穿模、重新目標臉部骨骼，或將自訂姿勢套用到動畫的一部分。參閱 [動作覆蓋](/dancexr/features/motion_override)。

**混音（Remix）**
：將一個舞動集中的動作數據與另一個舞動集的音訊配對。DanceXR 會自動調整速度以匹配。參閱 [混音動作](/dancexr/features/remix)。

**自訂繼承動作（Custom inherit motion）**
：使用者定義的繼承骨骼設定，用於添加或修改某些 PMX 模型所依賴的骨骼跟隨關係。參閱 [自訂繼承動作](/dancexr/features/custom_inherit)。

---

## 配置和持久性

**內容庫（Content library）**
：DanceXR 用來讀取模型、動作、音樂、舞台和使用者內容的資料夾。位置因平台而異。參閱 [內容庫](/dancexr/preparecontent)。

**預設集（Preset）**
：一套儲存的設定組合包—用於角色、材質、物理骨架等。儲存在內容庫的 `presets/` 下。可與使用相同 DanceXR 版本的用戶分享。

**設定資料夾（Settings folder）**
：內容庫中的 `settings/`。包含 DanceXR 自動寫入的每項功能配置（材質、物理、服裝、等）。不建議手動編輯，但備份是安全的。

**快取檔案（Cache file）**
：內容庫中的 `cache.json`。包含檢測到的模型、動作和其他資源的索引列表。可以安全刪除—下次啟動時 DanceXR 會重建它。

**配置檔（Config file）**
：位於執行檔旁邊的 `config.json`。包含應用程式級別的偏好設定。刪除它會將 DanceXR 重置為預設值。

**授權檔（License file）**
：`license.txt`。與您的激活綁定。移除它會強制重新激活。參閱 [FAQ](/dancexr/faq)。

---

## 版本和層級

DanceXR 有多個版本和層級。完整的矩陣在 [下載頁面](/dancexr/download)；簡要版本如下：

**免費版（Free）**
：單角色、基本功能。僅限 PC。

**Pure 版（Pure）**
：付費 PC 版本。支持多角色、XPS 物理、程序化舞蹈、包含光線追蹤。不包含成人內容。

**專業版（Pro）**
：付費 PC 版本，支持成人內容。光線追蹤作為本版本單獨的 DLC 販售。

**創作版（Creator）**
：增加了離線渲染—支持 4K、VR 180、VR 360、不論實時幀率如何，均可分幀渲染。可透過 Patreon 使用。參閱 [創作版](/dancexr/creator)。

**HD / RT / LW 版本變體**
：PC 版本的三個渲染層級。**HD** 具有平衡的品質。**RT** 增加了實時光線追蹤。**LW** 是性能優化的輕量級版本。根據 GPU 和使用場景選擇。

**Patreon 層級**
：在單次 Steam/Itch.io 購買之外，還包括 Patreon 的 Patron / Pro / Creator。Patreon 包含每月發布的早期存取權。

---

## AI 後端

**操作員（Operator）**
：DanceXR 專用的本地 AI 後端。它將語音合成（TTS）、大型語言模型推論和統一的 HTTP API 整合在一個程序後方。提供現代 AI 語音聊天工作流的動力。在您自己的硬體上運行。參閱 [DanceXR Operator](/dancexr/features/operator)。

**TTS（文本轉語音）**
：將 AI 生成的文字回傳為語音。Operator 使用 Kokoro；舊版使用 Piper。

**STT（語音轉文本）**
：將您的麥克風輸入轉換為文本，發送給 AI。DanceXR 使用內建的 Whisper 模型。

**人設（Persona）**
：應用於 AI 聊天中的角色個性和描述資料。可以手動撰寫或從 TavernAI 風格的 PNG 人物卡片中導入。

**模板（Template）**
：驅動 AI 生成聊天內容的提示腳本。儲存在 `chat/templates` 下。可編輯的純文本。

---

## 錄製和擷取

**離線渲染（Offline render）**
：幀級錄製，忽略您的實時 FPS。允許低規格 PC 透過為每一幀消耗更多實時時間，來捕獲 4K/60fps 影片。僅限創作版。參閱 [創作版](/dancexr/creator)。

**3D SBS**
：並排立體視訊，每隻眼睛一張水平放置的圖像。一種常見的 3D 影片格式。

**VR 180**
：立體 180 度 VR 影片（在 DanceXR 中，目前為每眼 120 度，填充至 180 度）。輸出固定為 4096×2048。

---

## 相關頁面

- [控制與 UI](/dancexr/controls) — 詳細記錄上述 UI 元素的位置
- [操作角色](/dancexr/actors) — 角色生命週期和配置
- [內容庫](/dancexr/preparecontent) — 資料夾結構和支援格式
- [下載與版本](/dancexr/download) — 完整層級矩陣
- [AI 文件索引](/dancexr/ai-index) — AI 代理的頁面導航