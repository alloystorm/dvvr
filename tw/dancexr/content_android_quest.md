---
locale: zh-TW
layout: single
title: Android & Quest內容庫
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本語](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)

## 為Android和Oculus Quest準備內容

與PC版本類似，DanceXR需要準備一個內容文件夾，以便知道在哪裡找到所有的模型、動作和紋理。

然而，Android系統有嚴格的文件訪問規則。通常，應用程序無法訪問存儲器內的文件夾。因此，默認情況下，Android和Quest版本將內容庫放在應用程序存儲空間內，這需要使用PC將文件複製到其中。

從版本2024.3開始，我們使用存儲權限來使文件管理變得更加容易。為此，您需要授予DanceXR訪問您的存儲空間的權限，然後您將能夠使用系統文件應用程序移動和複製文件。

{% include video id="mFnXE7LBV-M" provider="youtube" %}

對於舊版本或者如果您選擇使用應用程序內部存儲空間，內容庫位於這裡：/Android/data/com.vrstormlab.dancexr/files/。

## 如果您可以將設備連接到PC

使用PC來管理設備上的內容仍然更加容易。只需在Windows文件總管中複製和粘貼文件。在從PC複製內容之前，建議將內容逐個進行壓縮，以便更輕鬆地進行管理並減少存儲空間。

* 在設備上安裝DanceXR
* 將您的設備連接到PC。從彈出對話框或系統設置中選擇“文件傳輸”。
* 現在打開文件總管，您應該能夠看到您的設備。
* 導航到/DanceXR/或/Android/data/com.vrstormlab.dancexr/files/，如果您使用舊版本或選擇使用內部存儲。如果您沒有看到該文件夾，請確保已安裝DanceXR，如果安裝後仍無法找到它，請告訴我們，我們將盡力找出原因。
* 將整個內容文件夾複製到該目錄中。因此，您的內容文件夾結構將類似於![示例文件夾](/images/content_folder_android.png)

然後，您應該能夠在下次在設備上運行DanceXR時看到您的內容

## 使用系統文件應用程序

有了新的外部存儲權限，您可以使用系統文件應用程序來在庫中傳輸和管理內容。

找到存儲器根目錄下的DanceXR內容文件夾，然後您可以看到所有不同類型內容的子文件夾，並將文件移動到它們之間。

## 內容管理器應用程序（僅限Android）

Android版本附帶了一個內容管理器應用程序，可以幫助您在設備上組織您的內容。安裝DanceXR後，您應該能夠在應用程序抽屜或桌面上看到它。它與DanceXR播放器具有相同的圖標，但標題為“內容管理器”。內容管理器應用程序僅支持zip、png和jpg格式。

打開後，您將看到您的內容文件夾，並瀏覽其中包含的文件。您可以點擊文件，將其移動到其他位置，或[設置zip文件編碼](features/zip_format)。

內容管理器應用程序還會在您打開或共享支持的文件類型（zip、png或jpg）的文件時設置自己為目的地。

* 如果您從瀏覽器下載zip文件。下載後，點擊下載的文件，您應該看到帶有“添加到庫”的DanceXR圖標，選擇該選項，然後您可以選擇將文件保存到何處，然後將其複製到內容庫中。
* 您還可以使用文件管理器應用程序瀏覽您的手機，然後從菜單中選擇“打開方式”，您將能夠看到DanceXR“添加到庫”的選項。

這只是內容管理器的第一個版本；我們將繼續在途中添加更多功能。