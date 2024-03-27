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

内容库是DanceXR定位内容并存储用户创建设置的文件夹。

DanceXR在内容库中的不同子文件夹中搜索各种类型的内容。

* actors：角色模型
* motion：动作和音频文件
* stages：舞台的3D模型
* accessory：可以附加到角色身体部位的3D模型。
* props：可以用于舞台道具的3D模型。比如家具。
* texture
  * cookie：光掩模的纹理
  * drawing：用于身体绘画功能的保存图像
  * ground：地面纹理
  * mask：可以应用于模型的细节和法线贴图
  * particle：[粒子效果](features/particles.md)的纹理
  * sky：[全景天空地图](features/skymap.md)，建议使用HDR格式
* settings：所有保存的设置。这些文件不应由用户修改，但如果您愿意，可以复制并备份。
* scenes：保存的场景文件。
* bundles：保存的场景以及所有必要的资源，包含在一个zip包中。
* export：使用3D快照功能时，可以在此找到导出的模型文件。
* presets：保存的预设文件。只要您使用DanceXR的相同版本，就可以与朋友分享这些文件。
* videos：可用于投影和动态纹理映射的视频。仅支持MP4格式。
* chat：用于[AI聊天系统](ai_chat.md)的文件。
  * character：角色缩略图和模板。这些是自动生成的，但您可以进行修改。
  * template：提示模板，您可以进行修改并创建新的模板。
  * history：保存的聊天记录
  * persona：可以应用于角色的个性描述
  * voice/piper/：TTS系统的自定义语音模型

## 支持的格式

* 3D模型：PMX，XPS和OBJ（用于舞台道具）
* 音频：OGG和MP3（仅限移动平台）
* 视频：MP4
* 动作：VMD，BVH
* 纹理：PNG，JPG和HDR（用于天空地图）

## 分组和组织

为了更轻松地管理数据文件，特别是对于那些需要多个文件一起工作的内容，我们支持使用zip包来组织您的文件。您还可以将所有所需的文件放在子文件夹中，它们应该可以正常工作。

#### 3D模型

3D模型通常包含一个描述网格的文件和多个纹理文件。确保在移动或提取文件时，纹理和网格文件之间的相对关系保持不变非常重要，这对于程序找到正确的纹理使用非常重要。

对于PMX，网格文件是.pmx文件，对于XPS，网格文件可以是.xps，.mesh或.mesh.ascii文件。

建议将一个模型的所有文件放在一个zip包中，以便文件大小更小，更易于管理。

一些模型具有[替代纹理](features/alternative_textures.md)，DanceXR可以搜索文件夹或zip包以找到与模型使用的纹理类似的纹理文件，并自动将其包含在菜单中供您选择。为了使其工作，您需要确保替代纹理具有与主纹理相同的文件名。例如，如果基本贴图命名为base.png，当DanceXR在不同的子文件夹中找到另一个base.png时，它将自动将其添加为替代纹理。如果您的模型在zip包中，DanceXR将搜索整个zip包以查找替代纹理，如果您的模型在子文件夹中，它将搜索网格文件所在的所有子文件夹。请记住这一点，因为如果您将替代纹理放在网格文件夹之外，它们将不会被识别。

![演员文件夹示例](/images/content_actors.PNG)

#### 动作文件

通常，动作数据包含音频文件、角色动作和摄像机动作。在DanceXR中，我们将一组音频、角色动作和摄像机动作称为“舞蹈套装”。

为了让DanceXR检测到舞蹈套装，您只需要将所有这些文件放在一个子文件夹或zip包中。但请确保其中只有一个音频文件。

对于只有一个动作/音频对的简单内容，您可以在一个文件夹中有多个这样的文件，但您需要确保音频和动作文件具有相同的名称，例如“dance.vmd”和“dance.ogg”。这样DanceXR就知道它们是一对，并为其创建一个舞蹈套装。

您还可以在同一个文件夹中拥有多个无关的动作或音频文件。它们将被识别为没有与其他文件关联的单独动作或音频文件。

![动作文件夹示例](/images/content_motion.PNG)

## 内容库工具

在您对内容库文件进行更改后，当您启动DanceXR时，DanceXR应该会自动检测更改并重新扫描内容。

但是，如果没有发生这种情况，或者在运行时移动了文件，您可以使用系统菜单中的内容库工具来手动刷新它。

您还可以使用“更改库”选项将其指向不同的位置。

## Google Drive集成

DanceXR可以[从Google Drive下载文件](features/googledrive.md)。只要共享的驱动器文件夹没有任何限制。只需输入您共享文件夹的URL，DanceXR就能够扫描驱动器文件夹并下载本地不存在的文件。

## 为Android和Oculus Quest准备内容

Android系统有严格的文件访问规则。通常，应用程序无法访问存储中的文件夹。因此，默认情况下，Android和Quest版本的内容库位于应用程序存储空间内，需要PC将文件复制到其中。

在最新版本中，我们正在请求存储权限，以使文件管理变得更加容易。为此，您需要授予DanceXR访问您的存储的权限，然后您就可以使用系统文件应用程序移动和复制文件。

对于旧版本，或者如果您选择使用应用程序内部存储空间，内容库位于此处：/Android/data/com.vrstormlab.dancexr/files/。

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