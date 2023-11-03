---
layout: single
title: 內容庫
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)


## 內容庫

內容庫是一個資料夾，DanceXR用來定位內容並存儲用戶創建的設置。

DanceXR在內容庫中的不同子文件夾中搜索各種類型的內容。
* actors：角色模型
* motion：動作和音頻文件
* stages：舞台模型
* accessory：配飾模型
* skys：全景天空圖
* textures：地面和內置舞台的紋理文件
* masks：特殊紋理。用於服裝和粒子效果。

## 角色模型

![actors文件夾示例](/images/content_actors.PNG)

只要相關的紋理文件與PMX文件相對於正確位置，對於角色模型的放置沒有特定要求。

為了更方便管理，建議將所有文件存儲在zip包或單獨的文件夾中。

## 動作數據

![motion文件夾示例](/images/content_motion.PNG)

雖然播放單個動作文件而不帶音頻或任何相關的攝像機運動是可行的，但通常動作數據會帶有一個音頻文件，一個或多個動作文件，以及可能還有幾個攝像機運動文件。

建議將與動作數據相關的所有文件存儲在單個子文件夾中，或者更好地存儲在一個zip包中。還需要確保不混合其他動作數據的文件，並且確保只有一個與動作數據相關聯的音頻文件。請注意，僅支持WAV和OGG音頻格式。

## 演示視頻

在PC上：
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

在Android上使用內容管理器
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

在Quest上加載內容
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}

## 內容庫工具
內容庫菜單中提供了一些工具。

* "刷新內容"：DanceXR可以檢測內容庫的更改並自動進行掃描。但如果由於某種原因自動掃描無法工作，您可以使用此選項強制重新掃描整個內容庫。
* "更改庫"：使用此選項在您的設備上切換到不同的內容庫。這在Quest和Android版本中不可用。

## Google Drive集成
DanceXR可以從Google Drive下載文件。只要共享的文件夾沒有任何限制，只需輸入共享文件夾的URL，DanceXR就能夠掃描該Drive文件夾並下載本地不存在的文件。
## 準備 Android 和 Oculus Quest 的內容

與 PC 版本類似，DanceXR 需要準備一個內容文件夾，以便知道在哪裡找到所有的模型、動作和紋理。然而在 Android 上，應用程序只能訪問特定的文件夾，除非授予特殊權限。因此，在 Android 和 Oculus Quest 平台上，您將無法像在 PC 上那樣選擇內容文件夾。內容需要位於特定位置。

如果您可以將設備連接到 PC

使用 PC 在設備上管理內容仍然更容易。只需在 Windows 的「文件總管」中複製和粘貼文件即可。在從 PC 複製內容之前，建議將內容逐個壓縮以便更容易管理並減少存儲空間。

- 在設備上安裝 DanceXR
- 將設備連接到 PC。從彈出對話框或系統設置中選擇「文件傳輸」。
- 現在打開文件總管，您應該能夠看到您的設備。
- 導航到 /Android/data/com.vrstormlab.dancexr/files/。如果您看不到該文件夾，請確保已安裝 DanceXR，如果安裝後仍然找不到，請告訴我們，我們將盡力解決。
- 將整個內容文件夾複製到該目錄中。因此，您的內容文件夾結構將如下所示：![example folder](/images/content_folder_android.png)

然後，下次在設備上運行 DanceXR 時，您應該能夠看到您的內容。

如果您無法使用 PC（僅限 Android 版本）

Android 版本附帶了一個名為 Content Manager 的應用程序，可以幫助您在設備上組織內容。安裝 DanceXR 後，您應該能夠在應用程序抽屜或桌面上看到它。它的圖標與 DanceXR 播放器相同，但標題為「Content Manager」。Content Manager 應用程序僅支持 zip、png 和 jpg 格式。

打開它後，您將看到您的內容文件夾並瀏覽其中包含的文件。您可以點擊文件，將它們移動到其他位置或[設置 zip 文件編碼](features/zip_format)。

Content Manager 應用程序還在打開或共享支持的文件類型（zip、png 或 jpg）時將自己設置為目標。

- 如果您從瀏覽器下載 zip 文件。下載完成後，點擊下載的文件，您應該會看到 DanceXR 圖標和「添加到圖書館」，選擇該選項，然後您可以選擇將該文件保存到哪裡，然後它將被複製到內容圖書館。
- 您還可以使用文件管理器應用程序瀏覽手機，然後從菜單中選擇「打開方式」，您也將能夠看到 DanceXR 的「添加到圖書館」選項。

這只是 Content Manager 的第一個版本，我們將繼續在途中添加更多功能。