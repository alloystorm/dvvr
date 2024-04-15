---
locale: zh-CN
layout: single
title: 内容库
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)

## 内容库

内容库是一个文件夹，DanceXR用来定位内容并存储用户创建的设置。


## 定位内容库

**Windows**：在Windows上，您可以通过在系统菜单（左下角的齿轮图标）中的“内容库”部分点击“在资源管理器中显示”来定位内容库。

**Android**：在2024.3更新后，内容文件夹位于您的存储空间中的/DanceXR/。如果您使用的是旧版本，则位于/Android/data/com.vrstormlab.dancexr/files/。

**iPhone和iPad**：您可以在“我的iPhone”或“我的iPad”部分的文件应用中找到内容库。DanceXR在设备的根目录中创建一个名为“DanceXR”的文件夹。

**Oculus Quest**：在2024.3更新后，内容库位于您的存储空间中的/DanceXR/，旧版本位于/Android/data/com.vrstormlab.dancexr/files/。与Android版本类似。


## 文件夹结构

DanceXR在内容库中的不同子文件夹中搜索各种类型的内容。

* actors：角色模型
* motion：动作和音频文件
* stages：舞台的3D模型
* accessory：可以附加到角色身体部位的3D模型。
* props：可以用于舞台道具（如家具）的3D模型。
* texture
  * cookie：光掩模的纹理
  * drawing：[身体彩绘功能](features/outfit_body_paint.md)的保存图像
  * ground：地面纹理
  * mask：可应用于模型的[细节和法线贴图](features/custom_detail_map.md)
  * particle：[粒子效果](features/particles.md)的纹理
  * sky：[全景天空贴图](features/skymap.md)，建议使用HDR格式
* settings：所有保存的设置。这些文件不应由用户修改，但如果您愿意，可以复制并备份。
* scenes：[保存的场景](features/save_scene.md)文件。
* bundles：[保存的场景以及所有必要资源](features/scene_bundle.md)包含在一个zip包中。
* export：使用3D快照功能时，导出的模型文件可以在此找到。
* presets：保存的预设文件。只要您使用相同版本的DanceXR，就可以与朋友分享这些文件。
* videos：可用于[投影和动态纹理映射](features/video_playback.md)的视频。仅支持MP4格式。
* chat：用于[AI聊天系统](ai_chat.md)的文件。
  * characters：角色缩略图和模板。这些是自动生成的，但您可以进行修改。
  * templates：提示模板，您可以进行修改并创建新的。
  * history：保存的聊天记录
  * persona：可应用于角色的个性描述
  * voices/piper/：TTS系统的自定义语音模型

## 支持的格式

* 3D模型：PMX，XPS和OBJ（用于舞台道具）
* 音频：OGG和MP3（仅限移动平台）
* 视频：MP4
* 动作：VMD，BVH
* 纹理：PNG，JPG和HDR（用于天空贴图）

## 分组和组织

为了更轻松地管理数据文件，特别是对于那些需要多个文件一起工作的内容，我们支持使用zip包来组织您的文件。您也可以将所有必需的文件放在子文件夹中，它们应该可以正常工作。

#### 3D模型

3D模型通常包含一个描述网格的文件和多个纹理文件。确保在移动或提取文件时，纹理和网格文件之间的相对关系保持不变。这对于程序找到正确的纹理使用是很重要的。

对于PMX，网格文件是.pmx文件，对于XPS，网格文件可以是.xps，.mesh或.mesh.ascii。

建议将一个模型的所有文件放在一个zip包中，以获得更小的文件大小和更容易的管理。

一些模型具有[替代纹理](features/alternative_textures.md)。DanceXR可以搜索文件夹或zip包，找到与模型使用的纹理类似的纹理文件，并自动将其包含在菜单中供您选择。为使此功能正常工作，您需要确保替代纹理与主纹理具有相同的文件名。例如，如果基本贴图命名为base.png，当DanceXR在不同子文件夹中找到另一个base.png时，它将自动将其添加为替代纹理。如果您的模型在zip包中，DanceXR将在整个zip包中搜索替代纹理。如果您的模型在子文件夹中，它将从网格文件所在的所有子文件夹中搜索。请记住这一点，因为如果您将替代纹理放在网格文件文件夹之外，它们将无法被识别。

![actors文件夹示例](/images/content_actors.PNG)

#### 动作文件

通常，动作数据包含音频文件，角色动作和摄像机动作。在DanceXR中，我们将一组音频，角色动作和摄像机动作称为“舞蹈套”。

为了让DanceXR检测到舞蹈套，您只需要将所有这些文件放在一个子文件夹或zip包中。但请确保其中只有一个音频文件。

对于只包含动作/音频对的简单内容，您可以在单个文件夹中拥有多个这样的对，但您需要确保音频和动作文件具有相同的名称，例如“dance.vmd”和“dance.ogg”。这样DanceXR就知道它们是一对，并为其创建一个舞蹈套。

您也可以在同一个文件夹中拥有多个不相关的动作或音频文件。它们将被识别为没有与其他文件关联的单独动作或音频文件。

![motion文件夹示例](/images/content_motion.PNG)

## 内容库工具

在您对内容库文件进行更改后，当您启动DanceXR时，它应该会自动检测更改并重新扫描内容。

但是，如果这种情况没有发生，或者您在运行时移动了文件，您可以使用系统菜单中的内容库工具手动刷新它。

您还可以使用“更改库”选项将其指向不同的位置。

## Google Drive集成

DanceXR可以从Google Drive下载文件。只要共享的驱动器文件夹没有任何限制。只需输入您共享文件夹的URL，DanceXR就能够扫描驱动器文件夹并下载本地不存在的文件。

## 为Android和Oculus Quest准备内容

Android系统有严格的文件访问规则。通常，应用程序无法访问存储器中的文件夹。因此，默认情况下，Android和Quest版本的内容库位于应用程序存储空间内，需要PC将文件复制到其中。

从2024.3版本开始，我们使用存储权限使文件管理变得更加容易。为此，您需要授予DanceXR访问存储的权限，然后您就可以使用系统文件应用程序移动和复制文件。

对于旧版本或者如果您选择使用应用程序内部存储空间，内容库位于此处：/Android/data/com.vrstormlab.dancexr/files/。

## 演示视频

在PC上：
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

在Android上使用内容管理器
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

在Quest上加载内容
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}