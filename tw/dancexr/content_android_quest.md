---
locale: zh-TW
layout: single
title: 安卓和Quest的內容庫
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本語](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)

## 為Android和Oculus Quest準備內容

與PC版本類似，DanceXR需要準備一個內容文件夾，以便知道在哪裡找到所有的模型、動作和紋理。

然而，Android系統有嚴格的文件訪問規則。通常應用程序無法訪問您的存儲內部的文件夾。因此，默認情況下，Android和Quest版本的內容庫位於應用程序存儲空間內，需要使用PC將文件複製到其中。

從版本2024.3開始，我們使用存儲權限來使文件管理變得更加容易。為此，您需要授予DanceXR訪問您的存儲的權限，然後您將能夠使用系統文件應用程序移動和複製文件。

{% include video id="mFnXE7LBV-M" provider="youtube" %}

對於舊版本或者如果您選擇使用應用程序內部存儲空間，內容庫位於此處：/Android/data/com.vrstormlab.dancexr/files/。

## 如果您可以將您的設備連接到PC

在設備上管理內容仍然更容易。只需在Windows“文件總管”中複製和粘貼文件。在從PC複製內容之前，建議將內容單獨壓縮以便更容易管理和減少存儲空間。

* 在設備上安裝DanceXR
* 將您的設備連接到PC。從彈出對話框或系統設置中選擇“文件傳輸”。
* 現在打開文件總管，您應該能夠看到您的設備。
* 導航到/DanceXR/或/Android/data/com.vrstormlab.dancexr/files/，如果您使用舊版本或選擇使用內部存儲。如果您沒有看到該文件夾，請確保DanceXR已安裝，如果安裝後仍然找不到它，請告訴我們，我們將盡力找出原因。
* 將整個內容文件夾複製到該目錄中。因此，您的內容文件夾結構將類似於![example folder](/images/content_folder_android.png)

然後，您應該能夠在下次在設備上運行DanceXR時看到您的內容。

## 使用系統文件應用程序

有了新的外部存儲權限，您可以使用系統文件應用程序在庫中傳輸和管理內容。

找到存儲的根目錄下的DanceXR內容文件夾，然後您可以看到不同類型內容的所有子文件夾，並將文件移動到它們之間。

## 內容管理器應用程序（僅限Android）

Android版本附帶了一個內容管理器應用程序，可以幫助您在設備上組織您的內容。安裝DanceXR後，您應該能夠在應用程序抽屜或桌面上看到它。它具有與DanceXR播放器相同的圖標，但標題為“內容管理器”。內容管理器應用程序僅支持zip、png和jpg格式。

打開它後，您將看到您的內容文件夾，並瀏覽它們包含的文件。您可以點擊文件，將它們移動到其他地方或[設置zip文件編碼](features/zip_format)。

內容管理器應用程序還會在您打開或共享支持的文件類型（zip、png或jpg）時設置自己為目的地。

* 如果您從瀏覽器下載zip文件。下載後，點擊下載的文件，您應該看到DanceXR圖標和“添加到庫”，選擇該選項，然後您可以選擇將文件保存到何處，然後它將被複製到內容庫中。
* 您還可以使用文件管理器應用程序瀏覽您的手機，然後從菜單中選擇“打開方式”，您也將能夠看到DanceXR的“添加到庫”選項。

這只是內容管理器的第一個版本，我們將繼續在途中添加更多功能。