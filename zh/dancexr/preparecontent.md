---
layout: single
title: Content Library
toc: true
locale: zh-TW
sidebar:
  nav: "docs-zh"
---

## 內容庫

內容庫是一個文件夾，DanceXR可以找到內容並存儲用戶創建的設置。

Dancexr在內容庫中的不同子文件夾中搜索各種類型的內容。
*演員：角色模型
*運動：運動和音頻文件
*階段：舞台模型
*附件：配件模型
* Skys：全景Skymaps
*紋理：地面和內置階段的紋理文件
*口罩：特殊紋理。用於服裝和顆粒效應。


## 角色模型

![Actors文件夾的示例](/images/content_actors.png)

只要將PMX或XPS文件，以及其依賴的紋理文件放在actors子文件夾中就可以了。

為了更容易管理，推薦將所有文件壓縮在zip軟件包或單獨的文件夾中。


## 運動數據

![運動文件夾的示例](/images/content_motion.png)

儘管在沒有音頻或任何相關的相機運動的情況下播放單個運動文件是可行的，但通常情況下，運動數據帶有音頻文件，一個或多個運動文件，也可能是幾個相機運動文件。

建議將與運動數據相關的所有文件存儲在單個子文件夾中，或者最好將其存儲在ZIP軟件包中。避免將文件混合以獲取其他運動數據，並確保只有一個與運動數據關聯的音頻文件。請記住，僅支持WAV和OGG音頻格式。


## 演示視頻

在PC上：
{% include video id="-2LSTDN7WB8" provider="YouTube" %}


在Android上使用內容管理器
{% include video id="vqjnl9oq-hy" provider="youtube" %}


在任務上加載內容
{% include video id="zmdeuwwztmi" provider="youtube" %}


## 內容庫工具
內容庫菜單中提供了一些工具。

*“刷新內容”：Dancexr可以檢測內容庫的更改並自動執行掃描。但是，如果出於某種原因，自動掃描不起作用，則可以使用此選項強制重新掃描整個內容庫。
*“更改庫”：使用它切換到計算機上的其他內容庫。這在Quest和Android版本中不可用。


## Google Drive集成
Dancexr可以從Google Drive下載文件。只要共享驅動文件夾而無需任何限制即可。只需輸入您共享文件夾的URL即可，DanceXR將能夠掃描驅動器文件夾並下載本地不存在的文件。


## 為Android＆Oculus Quest準備內容

與PC版本類似，DanceXR需要準備一個內容文件夾，以便知道在哪裡可以找到所有模型，運動和紋理。但是，在Android上，除非授予特殊許可，否則應用只能訪問特定文件夾。因此，在Android和Oculus Quest平台上，您將無法像PC上選擇內容文件夾。內容需要在特定位置。

### 如果您可以將設備連接到PC

使用PC在設備上管理您的內容仍然更容易。它只是在您的Windows“文件資源管理器”中復制和粘貼文件。在您從PC複製內容之前，建議單獨拉鍊內容，以更輕鬆地管理和減少存儲空間。

*在設備上安裝Dancexr
*將您的設備連接到PC。從彈出對話框或系統設置中選擇“文件傳輸”。
*現在打開文件資源管理器，您應該能夠查看設備。
*導航到/android/data/com.vrstormlab.dancexr/files/。如果您看不到該文件夾，請確保安裝DanceXR，並且安裝後仍然找不到它，請告訴我們，我們會盡力解決該問題。
*將整個內容文件夾複製到該目錄中。因此您的內容文件夾結構就像！[示例文件夾](/images/content_folder_android.png)

那麼下次您在設備上運行DanceXR時，您應該可以看到您的內容

### 如果您無法訪問PC(僅Android版本)

Android版本帶有一個內容管理器應用程序，該應用程序可以幫助您在設備上組織內容。安裝DanceXr後，您應該可以從應用程序抽屜或桌面看到它。它具有與Dancexr播放器相同的圖標，但標題為“內容經理”。Content Manager App僅支持ZIP，PNG和JPG格式。

打開它後，您將看到您的內容文件夾並瀏覽其中包含的文件。您可以單擊文件以將其移動到其他地方或[設置zip文件編碼](zip_format.md)。

當您打開或共享受支持的文件類型(ZIP，PNG或JPG)的文件時，Content Manager應用程序還將自己設置為目標。

*如果您從瀏覽器下載ZIP。下載後，點擊下載的文件，您應該看到帶有“添加到庫”的Dancexr圖標，選擇該文件，然後您可以選擇將該文件保存到的位置，然後將其複製到內容庫中。
*您還可以使用文件管理器應用程序瀏覽手機，然後從菜單中選擇“打開”，您也可以看到Dancexr“添加到庫”選項。

這只是內容管理器的第一個版本，我們將繼續在此過程中添加更多功能。

