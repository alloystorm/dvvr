---
locale: zh-CN
layout: single
title: 安卓和Quest的内容库
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本語](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)

## 为Android和Oculus Quest准备内容

与PC版本类似，DanceXR需要准备一个内容文件夹，以便知道在哪里找到所有的模型、动作和纹理。

然而，Android系统有严格的文件访问规则。通常，应用程序无法访问存储中的文件夹。因此，默认情况下，Android和Quest版本的内容库位于应用存储空间内，需要使用PC将文件复制到其中。

从版本2024.3开始，我们使用存储权限来使文件管理变得更加容易。为此，您需要授予DanceXR访问您的存储的权限，然后您就可以使用系统文件应用程序移动和复制文件了。

{% include video id="mFnXE7LBV-M" provider="youtube" %}

对于旧版本或者如果选择使用应用程序内部存储空间，内容库位于这里：/Android/data/com.vrstormlab.dancexr/files/。

## 如果您可以将设备连接到PC

使用PC来管理设备上的内容仍然更容易。只需在Windows文件资源管理器中复制和粘贴文件。在从PC复制内容之前，建议将内容单独压缩以便于管理和减少存储空间。

* 在设备上安装DanceXR
* 将您的设备连接到PC。从弹出对话框或系统设置中选择“文件传输”。
* 现在打开文件资源管理器，您应该能够看到您的设备。
* 转到/DanceXR/或/Android/data/com.vrstormlab.dancexr/files/，如果您使用旧版本或选择使用内部存储。如果您没有看到该文件夹，请确保已安装DanceXR，如果安装后仍然找不到，请告诉我们，我们将尽力找出原因。
* 将整个内容文件夹复制到该目录中。因此，您的内容文件夹结构将类似于![示例文件夹](/images/content_folder_android.png)

然后，您应该能够在下次在设备上运行DanceXR时看到您的内容

## 使用系统文件应用程序

有了新的外部存储权限，您可以使用系统文件应用程序来传输和管理库中的内容。

找到存储根目录下的DanceXR内容文件夹，然后您可以看到所有不同类型内容的子文件夹，并在它们之间移动文件。

## 内容管理器应用程序（仅限Android）

Android版本附带了一个内容管理器应用程序，可以帮助您在设备上组织内容。安装DanceXR后，您应该能够在应用程序抽屉或桌面上看到它。它与DanceXR播放器具有相同的图标，但标题为“内容管理器”。内容管理器应用程序仅支持zip、png和jpg格式。

打开后，您将看到您的内容文件夹，并浏览其中包含的文件。您可以单击文件，将它们移动到其他位置或[设置zip文件编码](features/zip_format)。

内容管理器应用程序还会在您打开或共享支持的文件类型（zip、png或jpg）时将自身设置为目标。

* 如果您从浏览器下载zip文件。下载完成后，点击下载的文件，您应该看到带有“添加到库”的DanceXR图标，选择该选项，然后选择要保存文件的位置，然后文件将被复制到内容库中。
* 您还可以使用文件管理器应用程序浏览手机，然后从菜单中选择“打开方式”，您也将能够看到DanceXR“添加到库”的选项。

这只是内容管理器的第一个版本；我们将继续在其中添加更多功能。