---
layout: feature
title: Record Scene
locale: zh-TW
toc: true
---

# Record Scene

**Record Scene** 會把 DanceXR Native 螢幕上的內容（角色、它們的片段、音樂和相機）算繪成片段，並儲存為 **MP4**。它使用自己的時鐘算繪，因此無論你的 PC 實際影格率是多少，結果都很流暢，也不依賴視窗或螢幕的大小。它是 **Creator** 版本的一部分。

關於 Unity 應用的錄製，請參閱 [Creator 版本](../creator)。

---

## 錄製片段

開啟 **Scene > Record Scene**。

| 設定 | 選項 |
|---|---|
| **Name** | 本次錄製的名稱。 |
| **Size** | 1280 x 720、1920 x 1080、2560 x 1440、3840 x 2160，或 1080 x 1920（直式）。 |
| **Frame Rate** | 24、30 或 60。 |
| **Full Dance** | 從頭錄製整個舞蹈集（音樂和每個片段），而不是按 **Length**。 |
| **Length** | 從播放頭開始錄製多少秒（1 到 120）。 |
| **Camera** | **Current view, as set up**、**Current view, fixed pose**、**Orbit the first actor** 或 **Leave to the scene**。 |

點擊 **Record Video**。錄製期間，按鈕會顯示進度，**Stop Recording** 會結束錄製並保留已寫入的內容。**Show Folder** 會開啟最近一次錄製所在的資料夾。

## 相機選項

- **Current view, as set up** 會還原你的相機，包括對舞者的自由飛行追蹤，因此跟隨角色的視角會繼續跟隨。
- **Current view, fixed pose** 保持相機目前的姿態，忽略追蹤。
- **Orbit the first actor** 從目前視角開始，圍繞第一個角色環繞。
- **Leave to the scene** 不寫入自己的相機。舞蹈本身帶有相機動作時使用。

## 影片包含的內容

- 已載入的音樂會從片段開頭混入。
- 控制點、懸停圓環和游標等螢幕輔助元素不會被錄入。
- 錄製內容儲存到應用旁的 `recordings` 資料夾，資料夾以錄製名稱和時間命名。

## 需求

錄製需要 **ffmpeg**，它隨 Native 一同提供，位於應用旁的 `ffmpeg` 資料夾。Native 會選用你的 PC 支援的第一個影片編碼器：NVIDIA、AMD、Intel 或 Windows Media Foundation，並提供軟體編碼作為後備。Record Scene 選單在所有版本中都會顯示，但只有已啟用的 Creator 授權才能錄製。

---

## 相關頁面

- [Creator 版本](../creator)
- [DanceXR Native](native)
