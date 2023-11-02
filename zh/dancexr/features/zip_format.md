---
layout: single
title: ZIP格式
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/zip_format) | [繁中](/tw/dancexr/features/zip_format) | [日本語](/jp/dancexr/features/zip_format) | [한국어](/kr/dancexr/features/zip_format) | [简中](/zh/dancexr/features/zip_format)


## ZIP格式

### 内容

现在建议使用ZIP格式来打包个人内容，以便更容易管理和减少存储空间。这适用于模型和动作。

对于模型来说，每个ZIP包可以包含多个模型，其中应包括所有纹理和网格定义，并且它还可以在包内有其子文件夹。

对于动作来说，包内的所有动作文件将被分组在一个文件中。音频文件是可选的，但该包内不应超过一个音频文件。对于音频格式，支持WAV和OGG，但建议使用OGG以节省存储空间。

### 编码

ZIP格式确实具有文件夹结构，但当文件夹名称包含日文或中文字符时，可能会引起问题。这个问题的典型表现是模型加载成功，但纹理只显示为白色。

为了解决这个问题，我们在0.9.3版本中添加了一个解决方法，您可以使用正确的编码标签标记您的ZIP包，以便在解析ZIP包时知道使用哪种编码。这是通过在文件名末尾添加编码标签来完成的。目前支持的编码标签有"jis932"表示日文和"gb2312"表示中文。

例如，如果您的压缩文件名为"abc.zip"，并且其中包含日文文件名，您只需要将其重命名为"abc.jis932.zip"，DanceXR将能够正确解析它。

如果您使用的是Android系统，内置的内容管理器应用可以为您进行重命名，您只需要从菜单中选择正确的编码即可。