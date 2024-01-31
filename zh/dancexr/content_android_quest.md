---
locale: zh-CN
layout: single
title: 适用于Android和Quest / Pico的内容库
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本語](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)


## 为Android和Oculus Quest准备内容

与PC版本类似，DanceXR需要准备一个内容文件夹，以便知道在哪里找到所有的模型、动作和纹理。然而在Android上，应用程序只能访问特定的文件夹，除非授予特殊权限。因此，在Android和Oculus Quest平台上，您将无法像在PC上那样选择内容文件夹。内容需要放置在特定的位置。

## 如果您可以将设备连接到PC

使用PC在设备上管理内容仍然更容易。只需在Windows的“文件资源管理器”中复制和粘贴文件即可。在从PC复制内容之前，建议将内容单独压缩以便更容易管理和减少存储空间。

* 在设备上安装DanceXR
* 将设备连接到PC。从弹出对话框或系统设置中选择“文件传输”。
* 现在打开文件资源管理器，您应该能够看到您的设备。
* 导航到/Android/data/com.vrstormlab.dancexr/files/。如果您看不到该文件夹，请确保已安装DanceXR，如果安装后仍然找不到，请告诉我们，我们将尽力解决。
* 将整个内容文件夹复制到该目录中。因此，您的内容文件夹结构将类似于![示例文件夹](/images/content_folder_android.png)

然后，您应该能够在下次在设备上运行DanceXR时看到您的内容。

## 如果您无法访问PC（仅适用于Android版本）

Android版本附带了一个名为Content Manager的应用程序，可以帮助您在设备上组织内容。安装DanceXR后，您应该能够在应用程序抽屉或桌面上看到它。它的图标与DanceXR播放器相同，但标题为“Content Manager”。Content Manager应用程序仅支持zip、png和jpg格式。

打开它后，您将看到您的内容文件夹，并浏览其中包含的文件。您可以点击文件，将它们移动到其他位置或[设置zip文件编码](features/zip_format)。

Content Manager应用程序还在打开或共享支持的文件类型（zip、png或jpg）时将自身设置为目标。

* 如果您从浏览器下载zip文件。下载完成后，点击下载的文件，您应该会看到带有“添加到库”的DanceXR图标，选择该选项，然后选择要保存该文件的位置，它将被复制到内容库中。
* 您还可以使用文件管理器应用程序浏览手机，然后从菜单中选择“打开方式”，您也将能够看到DanceXR的“添加到库”选项。

这只是Content Manager的第一个版本，我们将继续在其中添加更多功能。