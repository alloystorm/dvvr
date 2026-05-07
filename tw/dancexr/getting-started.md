---
layout: release
title: 快速上手
locale: zh-TW
---

# 開始使用 DanceXR

本指南會帶你完成第一次使用 DanceXR 的基本流程，從下載應用程式到載入模型、播放動作，一步步快速上手。如果你是第一次接觸 DanceXR，也不用擔心，它的設計目標就是直覺、好用。

---

## 1. 下載並安裝

DanceXR 支援 **PC（Windows/Mac）**、**Android**、**iOS** 與 **Meta Quest**。請前往下載頁面，取得適合你平台的版本。

[**下載 DanceXR →**](/tw/dancexr/download)

以下是目前可用版本的簡要說明：

| 平台 | 推薦版本 |
|----------|-----------------|
| **Windows PC** | 想要兼顧畫質與效能請選 **HD**，需要光線追蹤請選 **RT**，重視效能請選 **LW** |
| **Mac** | **HD** 版本 — 可透過 Steam 取得，但由於使用者較少，最近沒有更新 |
| **Android** | **LW** 版本 — 可透過 Google Play 或 Itch.io 取得 |
| **iOS** | App Store |
| **Meta Quest** | 獨立執行版本 — 可透過 Itch.io 取得 |

**安裝提示：**

- **Windows：** 將下載的 `.7z` 壓縮檔解壓到任意資料夾，然後執行 `DanceXR.exe`。
- **Mac：** 透過 Steam 安裝。
- **Android / Quest：** 從下載來源安裝 APK。
- **iOS：** 直接從 App Store 安裝。

> 如果啟動時遇到問題，請查看 [支援頁面](/tw/dancexr/support) 中的常見解法。

---

## 2. 準備內容庫

我們建議你在啟動 DanceXR 之前先準備好內容庫。不過，你也可以直接把模型檔與動作檔拖放到 DanceXR 視窗中來載入內容。現在也可以先跳過這一步，等你準備好加入自己的模型與動作時再回來。

DanceXR 會在 **content library** 資料夾中尋找模型、動作與其他內容。你需要把 PMX 與 XPS 模型檔複製到這裡。

具體位置會依平台而有所不同：

- **Windows：** 開啟 DanceXR，點擊左下角的齒輪圖示（系統選單），然後在 Content Library 下選擇「Show in Explorer」。
- **Android / Quest：** 從 2024.3 更新開始，該資料夾位於儲存空間中的 `/DanceXR/`。
- **iOS：** 在裝置的 Files App 中尋找名為「DanceXR」的資料夾。

如需完整的資料夾結構與支援格式說明，請參閱 [內容庫指南](/tw/dancexr/preparecontent)。

![Example of actors folder](/images/content_actors.PNG)

---

## 3. 基本 UI 與操作

開啟 DanceXR 後，你應該會在畫面底部看到選單列。如果沒有顯示，請點擊空白區域來切換 UI 狀態，直到它出現為止。
在 VR 中，UI 會浮在你面前；在桌面模式中，它會固定在畫面底部。無論使用滑鼠還是 VR 控制器，點擊與拖曳的操作方式基本相同。在 VR 中，你可以按住握把鍵並移動手部來拖動 UI。

### UI 組成
![DanceXR UI overview](/images/menu.PNG)
- **進度列：** 位於底部，顯示目前的動作或音訊名稱與進度。點擊可播放或暫停，拖曳可快速定位。
- **選單區域：** 左側有五個圖示。
  - 系統選單（齒輪）：一般設定、內容庫與支援連結
  - 環境選單（圖片）：變更舞台、天空盒、燈光與相機設定
  - 場景選單（舞台）：載入舞台與道具，以及儲存 / 載入場景設定
  - 音訊 / 動作選單（音符）：載入並指派動作檔與音訊檔
  - 角色選單（人物）：載入並管理角色模型
- **播放與聊天控制：** 右側有音量滑桿、播放清單、上一首 / 下一首按鈕，以及 AI 聊天切換。

### 場景操作

已載入的角色腳下會顯示一個黃色圓圈。
- 點擊圓圈可開啟角色選單
- 拖曳可在舞台上移動角色
- 拖曳時滾動滑鼠滾輪可旋轉角色

### 切換顯示狀態

點擊空白區域可以在以下模式之間切換：
- **UI 模式：** 所有選單與控制項都會顯示。
- **控制模式：** 選單會隱藏，但角色圓圈仍然可見。
- **沉浸模式：** 選單與圓圈都會隱藏，提供最沉浸的體驗。

---

## 4. 載入模型

### 還沒放進內容庫？

沒問題。你可以直接把模型檔拖放到 DanceXR 視窗中即時載入。支援格式包括 `.pmx`、`.xps`、`.mesh` 與 `.mesh.ascii`。只要把檔案拖進去，它就會出現在角色選單中。

### 從內容庫載入

點擊角色圖示並選擇「Load Model」。你會看到 `actors` 資料夾中的所有模型清單。預設情況下，新模型會取代目前舞台上選取的模型。如果你想新增而不是取代，請點擊模型名稱旁邊的「+」圖示。此功能僅適用於付費版本。

---

## 5. 載入 VMD 動作

### 拖放載入

把音訊檔拖到 DanceXR 視窗中即可立即載入。支援 WAV 與 OGG 格式。
把 VMD 或 BVH 格式的動作檔拖到 DanceXR 視窗中即可載入。如果目前選取的角色尚未指派動作，該動作會自動指派給它。

### 從內容庫載入

點擊音訊 / 動作圖示並選擇「Load Audio / Motion」。你會看到 `motions` 資料夾中的所有動作清單。

動作與音訊會自動分組為「dance sets」。載入後，你會在進度列中看到音訊名稱，並在舞蹈選單中看到動作清單。若要指派動作，可以先選取動作，再按下「Assign To」；或者開啟角色選單，從已載入的動作中選擇一個。

如需了解如何整理動作檔，請參閱 [內容庫指南](/tw/dancexr/preparecontent#motion-files)。

---

## 接下來做什麼？

現在你已經可以開始使用了。接下來可以繼續深入探索 DanceXR 的更多功能：

- **[功能總覽](/tw/dancexr/features)** — 瀏覽 DanceXR 的所有功能與工具
- **[準備內容庫](/tw/dancexr/preparecontent)** — 詳細了解如何整理模型、動作、舞台等內容
- **[物理效果](/tw/dancexr/features/physics)** — 布料模擬、頭髮物理、軟體與布娃娃
- **[換裝系統](/tw/dancexr/features/optionals)** — 更換服裝、材質與配件
- **[相機](/tw/dancexr/features/camera_settings)** — Orbit cam、freefly、auto cam、第一人稱等
- **[AI 聊天](/tw/dancexr/features/ai_chat)** — 以語音與文字和角色互動
- **[創作者版](/tw/dancexr/creator)** — 面向內容創作者的離線 4K / VR 渲染
- **[疑難排解](/tw/dancexr/troubleshooting)** — 解決常見問題
- **[支援與 FAQ](/tw/dancexr/support)** — 常見問題解答

祝你玩得愉快。
