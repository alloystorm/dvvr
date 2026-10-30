---
layout: feature
title: Record Scene
locale: zh-CN
toc: true
---

# Record Scene

**Record Scene** 会把 DanceXR Native 屏幕上的内容（角色、它们的片段、音乐和相机）渲染成片段，并保存为 **MP4**。它使用自己的时钟渲染，因此无论你的 PC 实际帧率是多少，结果都很流畅，也不依赖窗口或显示器的大小。它是 **Creator** 版本的一部分。

关于 Unity 应用的录制，请参阅 [Creator 版本](../creator)。

---

## 录制片段

打开 **Scene > Record Scene**。

| 设置 | 选项 |
|---|---|
| **Name** | 本次录制的名称。 |
| **Size** | 1280 x 720、1920 x 1080、2560 x 1440、3840 x 2160，或 1080 x 1920（竖屏）。 |
| **Frame Rate** | 24、30 或 60。 |
| **Full Dance** | 从头录制整个舞蹈集（音乐和每个片段），而不是按 **Length**。 |
| **Length** | 从播放头开始录制多少秒（1 到 120）。 |
| **Camera** | **Current view, as set up**、**Current view, fixed pose**、**Orbit the first actor** 或 **Leave to the scene**。 |

点击 **Record Video**。录制期间，按钮会显示进度，**Stop Recording** 会结束录制并保留已写入的内容。**Show Folder** 会打开最近一次录制所在的文件夹。

## 相机选项

- **Current view, as set up** 会还原你的相机，包括对舞者的自由飞行跟踪，因此跟随角色的视角会继续跟随。
- **Current view, fixed pose** 保持相机当前的姿态，忽略跟踪。
- **Orbit the first actor** 从当前视角开始，围绕第一个角色环绕。
- **Leave to the scene** 不写入自己的相机。舞蹈本身带有相机动作时使用。

## 视频包含的内容

- 已加载的音乐会从片段开头混入。
- 手柄、悬停圆环和光标等屏幕辅助元素不会被录入。
- 录制内容保存到应用旁的 `recordings` 文件夹，文件夹以录制名称和时间命名。

## 要求

录制需要 **ffmpeg**，它随 Native 一同提供，位于应用旁的 `ffmpeg` 文件夹。Native 会选用你的 PC 支持的第一个视频编码器：NVIDIA、AMD、Intel 或 Windows Media Foundation，并提供软件编码作为后备。Record Scene 菜单在所有版本中都会显示，但只有已激活的 Creator 许可才能录制。

---

## 相关页面

- [Creator 版本](../creator)
- [DanceXR Native](native)
