---
layout: single
title: 内容库
toc: true
sidebar:
  nav: "docs-zh"
---
[English](/dancexr/preparecontent) | [简体中文](/zh/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent)


## 内容库

内容库是一个文件夹，DanceXR在其中定位内容并存储用户创建的设置。

DanceXR在内容库中的不同子文件夹中搜索各种类型的内容。
* actors：角色模型
* motion：动作和音频文件
* stages：舞台模型
* accessory：配饰模型
* skys：全景天空贴图
* textures：地面和内置舞台的纹理文件
* masks：特殊纹理。用于服装和粒子效果。

## 角色模型

![actors文件夹示例](/images/content_actors.PNG)

只要依赖的纹理文件与PMX文件的相对位置正确，对于角色模型的放置没有特定要求。

为了更方便管理，建议将所有文件存储在zip包或单独的文件夹中。

## 动作数据

![motion文件夹示例](/images/content_motion.PNG)

虽然可以播放单个动作文件而无需音频或任何相关的相机动作，但通常动作数据会带有一个音频文件，一个或多个动作文件，以及可能有几个相机动作文件。

建议将与动作数据相关的所有文件存储在一个子文件夹中，或者更好地存储在一个zip包中。还必须避免混合其他动作数据的文件，并确保只有一个与动作数据相关联的音频文件。请记住，只支持WAV和OGG音频格式。

## 演示视频

在PC上：
{% include video id="-2LStDN7WB8" provider="youtube" %}

在Android上使用内容管理器：
{% include video id="VQjnL9oq-hY" provider="youtube" %}

在Quest上加载内容：
{% include video id="ZmDeuWwZtmI" provider="youtube" %}

## 内容库工具
内容库菜单中提供了一些工具。

* "刷新内容"：DanceXR可以检测内容库的更改并自动执行扫描。但是，如果由于某种原因自动扫描不起作用，您可以使用此选项强制重新扫描整个内容库。
* "更改库"：使用此选项切换到计算机上的其他内容库。这在Quest和Android版本中不可用。

## Google Drive集成
DanceXR可以从Google Drive下载文件。只要共享的文件夹没有任何限制。只需输入共享文件夹的URL，DanceXR就能够扫描该Drive文件夹并下载本地不存在的文件。
## 准备Android和Oculus Quest的内容

与PC版本类似，DanceXR需要准备一个内容文件夹，以便知道在哪里找到所有的模型、动作和纹理。然而，在Android上，应用程序只能访问特定的文件夹，除非授予特殊权限。因此，在Android和Oculus Quest平台上，您将无法像在PC上那样选择内容文件夹。内容需要放在特定的位置。

如果您可以将设备连接到PC

使用PC来管理设备上的内容仍然更容易。只需在Windows“文件资源管理器”中复制和粘贴文件即可。在从PC复制内容之前，建议将内容单独压缩以便更容易管理和减少存储空间。

- 在设备上安装DanceXR
- 将设备连接到PC。从弹出对话框或系统设置中选择“文件传输”。
- 现在打开文件资源管理器，您应该能够看到您的设备。
- 导航到/Android/data/com.vrstormlab.dancexr/files/。如果您没有看到该文件夹，请确保已安装DanceXR，并且如果安装后仍然找不到，请告诉我们，我们将尽力解决。
- 将整个内容文件夹复制到该目录中。因此，您的内容文件夹结构将类似于![示例文件夹](/images/content_folder_android.png)

然后，下次在设备上运行DanceXR时，您应该能够看到您的内容。

如果您无法访问PC（仅适用于Android版本）

Android版本附带了一个名为Content Manager的应用程序，可以帮助您在设备上组织内容。安装DanceXR后，您应该能够在应用程序抽屉或桌面上看到它。它的图标与DanceXR播放器相同，但标题为“Content Manager”。Content Manager应用程序仅支持zip、png和jpg格式。

打开它后，您将看到您的内容文件夹，并浏览其中包含的文件。您可以点击文件，将它们移动到其他位置或[设置zip文件编码](features/zip_format)。

Content Manager应用程序还在打开或共享支持的文件类型（zip、png或jpg）时将自身设置为目标。

- 如果您从浏览器下载zip文件。下载完成后，点击下载的文件，您应该会看到带有“添加到库”的DanceXR图标，选择该选项，然后可以选择将文件保存到哪里，然后它将被复制到内容库中。
- 您还可以使用文件管理器应用程序浏览手机，然后从菜单中选择“打开方式”，您也将能够看到DanceXR的“添加到库”选项。

这只是Content Manager的第一个版本，我们将继续在其中添加更多功能。