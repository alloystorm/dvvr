---
layout: single
title: 資料庫
toc: true
locale: zh-TW
sidebar:
  nav: "docs-zh"
---

## 資料庫

資料庫是一個文件夾，DanceXR可以在裏面找到内容並存儲用戶創建的設置。

在系統菜單中選擇 資料庫 / 在資源管理器中顯示 就可以打開内容庫的文件夾。裏面會有如下的目錄：
* actors：角色模型
* accessory: 角色道具模型
* motion：運動和音頻文件
* props: 舞臺道具模型
* scenes: 保存的場景
* settings: 保存的設定
* stages：舞台模型
* texture
    * drawing: 保存的人體彩繪圖片
    * ground: 地面的紋理文件
    * mask: 用於紋身等紋理
    * particle: 用於粒子系統的紋理
    * sky: 天空紋理


## 角色模型

![Actors文件夾的示例](/images/content_actors.PNG)

只要將PMX或XPS文件，以及其依賴的紋理文件放在actors子文件夾中就可以了。

為了更容易管理，推薦將所有文件壓縮在zip軟件包或單獨的文件夾中。


## 動作數據

![動作文件夾的示例](/images/content_motion.PNG)

動作文件可以是VMD或者BVH格式。通常會把一個聲音文件（wav或ogg格式）連同有關聯的多個動作文件（包括攝像機動作）放在一個文件夾内，這樣DanceXR可以把文件關聯到一起，載入聲音的時候可以同時載入所有動作文件。請注意這種情況必須文件夾内只有一個聲音文件，否則會混淆。然後最好是把這個文件夾用zip格式壓縮起來，這樣方便管理以及查找。
也可以只有聲音或只有動作的文件。例如把單獨的聲音文件都放在一個audio_only文件夾内，單獨的動作文件放在一個motion_only的文件夾内。

## 演示視頻

在PC上：
{% include video id="-2LStDN7WB8" provider="youtube" %}


在Android上使用內容管理器
{% include video id="VQjnL9oq-hY" provider="youtube" %}


在任務上加載內容
{% include video id="ZmDeuWwZtmI" provider="youtube" %}


## 資料庫工具
資料庫菜單中提供了一些工具。

* “刷新內容”：通常DanceXR可以檢測資料庫的更改並自動執行掃描。但是，如果出於某種原因，自動掃描不起作用，則可以使用此選項強制重新掃描整個資料庫。
* “更改庫”：使用它切換到計算機上的其他資料庫。這在Quest和Android版本中不可用。


## Google Drive集成
DanceXR可以從Google Drive下載文件。只要共享驅動文件夾而無需任何限制即可。只需輸入您共享文件夾的URL即可，DanceXR將能夠掃描驅動器文件夾並下載本地不存在的文件。


## 為Android＆Oculus Quest準備內容

與PC版本類似，DanceXR需要準備一個內容文件夾，以便知道在哪裡可以找到所有模型，運動和紋理。但是，在Android上，除非授予特殊許可，否則應用只能訪問特定文件夾。因此，在Android和Oculus Quest平台上，您將無法像PC上選擇內容文件夾。內容需要在特定位置。

### 如果您可以將設備連接到PC

使用PC在設備上管理您的內容仍然更容易。它只是在您的Windows“文件資源管理器”中復制和粘貼文件。在您從PC複製內容之前，建議單獨拉鍊內容，以更輕鬆地管理和減少存儲空間。

* 在設備上安裝DanceXR
* 將您的設備連接到PC。從彈出對話框或系統設置中選擇“文件傳輸”。
* 現在打開文件資源管理器，您應該能夠查看設備。
* 導航到/android/data/com.vrstormlab.dancexr/files/。如果您看不到該文件夾，請確保安裝DanceXR，並且安裝後仍然找不到它，請告訴我們，我們會盡力解決該問題。
* 將整個內容文件夾複製到該目錄中。因此您的內容文件夾結構就像！[示例文件夾](/images/content_folder_android.png)

那麼下次您在設備上運行DanceXR時，您應該可以看到您的內容

### 如果您無法訪問PC(僅Android版本)

Android版本帶有一個內容管理器應用程序，該應用程序可以幫助您在設備上組織內容。安裝DanceXr後，您應該可以從應用程序抽屜或桌面看到它。它具有與DanceXR播放器相同的圖標，但標題為“內容經理”。Content Manager App僅支持ZIP，PNG和JPG格式。

打開它後，您將看到您的內容文件夾並瀏覽其中包含的文件。您可以單擊文件以將其移動到其他地方或[設置zip文件編碼](zip_format.md)。

當您打開或共享受支持的文件類型(ZIP，PNG或JPG)的文件時，Content Manager應用程序還將自己設置為目標。

*如果您從瀏覽器下載ZIP。下載後，點擊下載的文件，您應該看到帶有“添加到庫”的DanceXR圖標，選擇該文件，然後您可以選擇將該文件保存到的位置，然後將其複製到資料庫中。
*您還可以使用文件管理器應用程序瀏覽手機，然後從菜單中選擇“打開”，您也可以看到DanceXR“添加到庫”選項。

這只是內容管理器的第一個版本，我們將繼續在此過程中添加更多功能。

