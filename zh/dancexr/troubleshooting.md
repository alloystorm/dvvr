---
layout: release
title: 故障排除
locale: zh-CN
---

## 报告错误
建议在[GitHub问题跟踪器](https://github.com/alloystorm/dvvr/issues)上提出错误，以便能够得到适当的管理。

您也可以直接发送电子邮件至vrstormlab@gmail.com。最好附上屏幕截图和示例模型，如果可能的话。

我们将尽力阅读并回复其他平台上的评论和私信，但我们不能保证所有消息都会通过这些渠道得到处理。


## 定位日志文件（仅适用于PC）
如果发生了任何错误，通常在日志文件中会包含描述该错误的条目。因此，当您报告问题时，如果能够定位并将其发送给我们日志文件将非常有帮助。

日志文件可以在**C:\Users\\\[您的用户名]\AppData\LocalLow\VR Storm Lab\DanceXR HD**中找到，最后一个文件夹名称取决于您正在运行的版本，因此可能是“DanceXR HD”、“DanceXR LW”或“DanceXR RT”。

您的系统中可能默认隐藏了其中一些文件夹，因此您可能需要在[设置资源管理器以显示隐藏文件](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)之前才能找到它们。

打开文件夹后，您将看到日志文件“**Player.log**”和“**Player-prev.log**”。

---

## 首先查看哪些内容

根据症状进行分类：

- **应用无法启动/启动时崩溃** → [FAQ → 只显示天空](faq#only-sky-is-displayed-no-ui-or-camera-control-available), [FAQ → 突然开始崩溃](faq)
- **VR无法启动** → [FAQ → 无法启动VR](faq#unable-to-launch-vr)
- **激活问题** → [FAQ → 被要求再次激活](faq#im-asked-to-activate-again)，然后[支持](support)
- **特定模型问题（特定模型行为异常）** → [角色故障排除](features/troubleshooting)
- **头发、布料、裙子或胸部物理效果** → [物理系统](physics)
- **材质或纹理看起来不对** → [外观与材质](appearance), [FAQ → 模型加载但一切都是白色](faq#model-loads-but-everything-is-white)
- **动画未播放或演员错误** → [动画系统](motion)
- **不知道某个术语的含义** → [概念与术语表](concepts)

## 相关页面

- [FAQ](faq)
- [支持](support) — Discord, 电子邮件, GitHub问题
- [概念与术语表](concepts)