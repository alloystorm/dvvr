---
layout: release
title: 虛擬實境運作
locale: zh-TW
toc: true
---

# VR 操作

如何在 VR 中使用 DanceXR — 控制器、指標、抓取拖曳 UI、舒適度和與桌面模式不同的操作。關於技術 VR 設定（視場景渲染、指標校準值、手部渲染開關），請參閱 [VR 設定](/dancexr/features/vr_settings)。關於輸入映射表和抽象控制方案，請參閱 [控制與 UI](/dancexr/controls)。

---

## 手部控制器

每隻手對應以下功能：

- **扳機鍵 (Trigger)** — 類比輸入，用於「自訂」操作，以及在按住時作為 UI 切換開關，以執行第二個操作
- **握把 (Grip)** — 預設分配給 **第二個操作**。按住以存取其他任何控制器（例如：拇指搖桿）的次要功能。也用於 UI 抓取（參見下方的 [抓取拖曳 UI](#grip-drag-ui)）。
- **按鈕 1 / 按鈕 2** — 面板按鈕（例如：Quest 控制器上的 A / B / X / Y）
- **拇指搖桿 (Thumbstick)** — 在拖曳時移動和旋轉演員；也用於 UI 捲動
- **選單按鈕 (Menu button)** — 左手選單 = 切換 UI / UI 返回；右手選單 = 切換麥克風

預設映射列於 [控制與 UI](/dancexr/controls#default-mappings)。

### 手部渲染

在 VR 中可以顯示或隱藏虛擬手。可在 [VR 設定 → 手部](/dancexr/features/vr_settings#hand) 中切換。設定包括每個手的啟用、是否投射陰影和姿勢預設。

---

## 指標（雷射光束）

每個控制器都會投射一個雷射指標，用於操作選單和拖曳可互動的物件（演員選擇圓盤、萬用規立方體、道具）。

- **指向 UI 元素** 以高亮顯示；**按下扳機鍵或按鈕 1** 進行選擇。
- **指向演員的選擇圓盤** 並擠壓扳機鍵/按鈕以拖曳。
- **指向萬用規立方體** 以抓取和擺放身體部位的姿勢。

如果指標光束感覺偏離軸心，請在 [VR 設定 → 指標](/dancexr/features/vr_settings#pointer) 中進行校準。您可以使用它調整方向、方向和偏移量。

### VR 中的滑鼠模式

v2025.10 新增。讓您可以使用滑鼠而不是（或除了）手部控制器來控制指標。這對於坐在桌子前玩機器人非常有用。與鍵盤輸入結合使用，這可以在頭戴裝置內部提供類似桌面的控制方案。可在 [VR 設定 → UI → VR 中的滑鼠模式](/dancexr/features/vr_settings#ui) 中啟用。

### 指標把手

v2025.10 新增。一種物理的桿子模型，手部握持，受物理引擎驅動，您可以用它來推動和挑逗演員。不適合工作場所使用（NSFW）；Pure 版本無法使用。您也可以載入任何具有骨骼鏈的外部模型，作為自訂把手使用。<!-- TODO: link to a Pointer Handle settings page if/when one exists -->

---

## 抓取拖曳 UI

選單面板在 VR 中浮動在您身前。要移動它：

1. 在指向面板的同時，按住 **握把按鈕**。
2. 將面板拖曳到新的位置。
3. 釋放握把按鈕即可定格。

如果面板漂移到視野外，**UI 自動返回**（在 [VR 設定 → UI](/dancexr/features/vr_settings#ui) 中）會平滑地將其帶回您的視野。

您還可以使用 **UI 距離** 滑桿（0.5–5 米）調整面板與頭部的休息距離。

---

## VR 中的切換狀態

與桌面模式相同的三個 UI 切換狀態也適用於 VR — 請參見 [控制與 UI → 切換狀態](/dancexr/controls#toggle-states)。可以通過點擊空白處，或按下指定的 **切換 UI** 輸入（預設為左手選單按鈕）來循環切換。

在**沉浸式模式**中，面板和選擇圓盤會消失，只留下場景——這對於純粹被動觀看非常有用。

---

## 舒適度與視圖

<!-- TODO: confirm which of these settings actually exist. Below is what would belong here. -->

- **阻擋桌面視窗** ([VR 設定 → UI](/dancexr/features/vr_settings#ui)) — 停止將頭戴裝置視圖鏡像到桌面監控器，以提高隱私性。
- **視場景渲染** ([VR 設定 → 視場景渲染](/dancexr/features/vr_settings#foveated-rendering)) — 目前僅適用於 Quest 版本。它會降低周邊的解析度以釋放 GPU 時間。等級越高 = 性能越高，但邊緣的模糊越明顯。

---

## Quest 的性能

Quest 獨立裝置的資源限制比 PC VR 更嚴格。某些功能在 Quest 上表現不同：

- 為了保持運行時成本低，無論 [演員選項 → 轉換](/dancexr/features/loader_options#transition) 設定如何，演員的載入/卸載**在 Quest 版本上會強制禁用**。
- 內容庫位於儲存空間的 `/DanceXR/`（2024.3 版本之後）；參見 [Android 與 Quest 的內容庫](/dancexr/content_android_quest)。
- 在 **自動模式**下的語音轉文字功能在 Quest 上不推薦，因為音訊處理過於慢；建議使用**手動模式**。請參見 [AI 語音聊天 → 語音轉文字](/dancexr/features/ai_chat#speech-to-text)。

---

## VR 中的麥克風

AI 聊天的麥克風切換開關預設映射到 **右手選單按鈕**。您可以在輸入設定中重新綁定它；參見 [AI 語音聊天 → 鍵盤綁定](/dancexr/features/ai_chat#key-binding)。

為了在 VR 中獲得最佳效果，請在啟動 DanceXR 之前，在您的作業系統音訊設定中，選擇頭戴裝置內建的麥克風作為輸入設備。

---

## AR 模式（行動裝置 / Quest）

AR 模式使用設備的相機直通，讓演員看起來好像站在您的真實環境中。適用於支援的行動裝置和 Quest 版本；僅限 **專業版**。請參見 [AR 模式](/dancexr/features/ar_mode)。

---

## 相關頁面

- [控制與 UI](/dancexr/controls) — 輸入映射和選擇圓盤行為
- [VR 設定](/dancexr/features/vr_settings) — 指標校準、視場景渲染、手部渲染
- [AI 語音聊天](/dancexr/features/ai_chat) — 麥克風設定
- [概念與術語表](/dancexr/concepts) — 切換狀態、萬用規立方體、選擇圓盤