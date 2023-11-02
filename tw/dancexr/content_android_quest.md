---
layout: single
title: Android和Quest / Pico的內容庫
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)


## 為Android和Oculus Quest準備內容

與PC版本類似，DanceXR需要準備一個內容文件夾，以便它知道在哪裡找到所有的模型、動作和紋理。然而，在Android上，除非授予特殊權限，否則應用程序只能訪問特定的文件夾。因此，在Android和Oculus Quest平台上，您將無法像在PC上那樣選擇內容文件夾。內容需要位於特定位置。

## 如果您可以將設備連接到PC

使用PC來管理設備上的內容仍然更容易。只需在Windows的“文件總管”中進行文件的複製和粘貼。在從PC複製內容之前，建議將內容逐個壓縮以便更容易管理和減少存儲空間。

* 在設備上安裝DanceXR
* 將設備連接到PC。從彈出對話框或系統設置中選擇“文件傳輸”。
* 現在打開文件總管，您應該能夠看到您的設備。
* 導航到/Android/data/com.vrstormlab.dancexr/files/。如果您看不到該文件夾，請確保已安裝DanceXR，如果安裝後仍然找不到，請告訴我們，我們將盡力解決問題。
* 將整個內容文件夾複製到該目錄中。因此，您的內容文件夾結構將如下所示：![example folder](/images/content_folder_android.png)

然後，您應該能夠在下次在設備上運行DanceXR時看到您的內容。

## 如果您無法使用PC（僅適用於Android版本）

Android版本附帶了一個名為Content Manager的應用程序，可以幫助您在設備上組織內容。安裝DanceXR後，您應該能夠在應用程序抽屜或桌面上看到它。它的圖標與DanceXR播放器相同，但標題為“Content Manager”。Content Manager應用程序僅支持zip、png和jpg格式。

打開它後，您將看到您的內容文件夾並瀏覽它們包含的文件。您可以點擊文件，將它們移動到其他位置或[設置zip文件編碼](features/zip_format)。

Content Manager應用程序還在打開或共享支持的文件類型（zip、png或jpg）的文件時將自己設置為目的地。

* 如果您從瀏覽器下載zip文件。下載完成後，點擊下載的文件，您應該會看到DanceXR圖標和“添加到庫”的選項，選擇該選項，然後選擇要保存該文件的位置，然後它將被複製到內容庫中。
* 您還可以使用文件管理器應用程序瀏覽手機，然後從菜單中選擇“打開方式”，您也將能夠看到DanceXR的“添加到庫”選項。

這只是Content Manager的第一個版本，我們將繼續在途中添加更多功能。