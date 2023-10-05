---
layout: single
title: 故障排除
toc: true
sidebar:
  nav: "docs-zh"
---
[English](/dancexr/troubleshooting) | [简体中文](/zh/dancexr/troubleshooting) | [日本語](/jp/dancexr/troubleshooting)


## 报告错误
建议在[GitHub问题跟踪器](https://github.com/alloystorm/dvvr/issues)上提出错误，以便能够得到适当的管理。

您也可以直接发送电子邮件至vrstormlab@gmail.com。最好附上屏幕截图和示例模型。

我们将尽力阅读和回复其他平台上的评论和直接消息，但我们不能保证每条消息都会通过这些渠道处理。


## 定位日志文件（仅适用于PC）
如果发生任何错误，通常在日志文件中会有描述该错误的日志条目。因此，当您报告问题时，如果能够定位您的日志文件并将其发送给我们，将非常有帮助。

日志文件可以在**C:\Users\\\[您的用户名]\AppData\LocalLow\VR Storm Lab\DanceXR HD**中找到，最后一个文件夹名称取决于您正在运行的版本，因此可能是"DanceXR HD"、"DanceXR LW"或"DanceXR RT"。

您的系统中可能默认隐藏了其中一些文件夹，因此您可能需要在找到它们之前[设置资源管理器显示隐藏文件](https://support.microsoft.com/zh-cn/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

打开文件夹后，您将看到日志文件"**Player.log**"和"**Player-prev.log**"。