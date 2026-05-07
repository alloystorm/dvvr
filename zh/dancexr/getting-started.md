---
layout: release
title: 入门指南
locale: zh-CN
---

# 开始使用 DanceXR

本指南将带你完成第一次使用 DanceXR 的基本流程，从下载应用到加载模型、播放动作，一步步上手。如果你是第一次接触 DanceXR，也不用担心，它的设计目标就是直观、易用。

---

## 1. 下载并安装

DanceXR 可用于 **PC（Windows/Mac）**、**Android**、**iOS** 和 **Meta Quest**。请前往下载页面，获取适合你平台的版本。

[**下载 DanceXR →**](/zh/dancexr/download)

下面是目前可用版本的简要说明：

| 平台 | 推荐版本 |
|----------|-----------------|
| **Windows PC** | 画质与性能均衡请选择 **HD**，需要光线追踪请选择 **RT**，更注重性能请选择 **LW** |
| **Mac** | **HD** 版本 — 可通过 Steam 获取，但由于用户基数较小，最近没有更新 |
| **Android** | **LW** 版本 — 可通过 Google Play 或 Itch.io 获取 |
| **iOS** | App Store |
| **Meta Quest** | 独立运行版本 — 可通过 Itch.io 获取 |

**安装提示：**

- **Windows：** 将下载的 `.7z` 压缩包解压到任意文件夹，然后运行 `DanceXR.exe`。
- **Mac：** 通过 Steam 安装。
- **Android / Quest：** 从下载来源安装 APK。
- **iOS：** 直接从 App Store 安装。

> 如果启动时遇到问题，请查看 [支持页面](/zh/dancexr/support) 中的常见解决方法。

---

## 2. 准备内容库

我们建议你在启动 DanceXR 之前先准备好内容库。不过，你也可以直接把模型文件和动作文件拖放到 DanceXR 窗口中来加载内容。现在也可以先跳过这一步，等你准备好添加自己的模型和动作时再回来。

DanceXR 会在 **content library** 文件夹中查找模型、动作和其他内容。你需要把 PMX 和 XPS 模型文件复制到这里。

具体位置取决于平台：

- **Windows：** 打开 DanceXR，点击左下角的齿轮图标（系统菜单），然后在 Content Library 下选择“Show in Explorer”。
- **Android / Quest：** 从 2024.3 更新开始，该文件夹位于存储中的 `/DanceXR/`。
- **iOS：** 在设备的 Files 应用中查找名为 “DanceXR” 的文件夹。

有关文件夹结构和支持格式的完整说明，请参阅 [内容库指南](/zh/dancexr/preparecontent)。

![Example of actors folder](/images/content_actors.PNG)

---

## 3. 基本 UI 和操作

打开 DanceXR 后，你应该会在屏幕底部看到菜单栏。如果没有显示，请点击空白区域以切换 UI 状态，直到它出现。
在 VR 中，UI 会悬浮在你面前；在桌面模式中，它固定在屏幕底部。无论你使用鼠标还是 VR 控制器，点击和拖动的操作方式基本一致。在 VR 中，你可以按住握把键并移动手部来拖动 UI。

### UI 组成
![DanceXR UI overview](/images/menu.PNG)
- **进度条：** 位于底部，显示当前动作或音频名称以及播放进度。点击可播放或暂停，拖动可快速定位。
- **菜单区域：** 左侧有五个图标。
  - 系统菜单（齿轮）：常规设置、内容库和支持链接
  - 环境菜单（图片）：更改舞台、天空盒、灯光和相机设置
  - 场景菜单（舞台）：加载舞台和道具，以及保存 / 加载场景设置
  - 音频 / 动作菜单（音符）：加载并分配动作文件和音频文件
  - 角色菜单（人物）：加载和管理角色模型
- **播放和聊天控制：** 右侧有音量滑块、播放列表、上一首 / 下一首按钮，以及 AI 聊天开关。

### 场景操作

已加载的角色脚下会显示一个黄色圆圈。
- 点击圆圈打开角色菜单
- 拖动可在舞台上移动角色
- 拖动时滚动鼠标滚轮可旋转角色

### 切换显示状态

点击空白区域可以在以下模式之间切换：
- **UI 模式：** 所有菜单和控制项都可见。
- **控制模式：** 菜单隐藏，但角色圆圈仍可见。
- **沉浸模式：** 菜单和圆圈都被隐藏，获得最沉浸的体验。

---

## 4. 加载模型

### 还没放进内容库？

没问题。你可以直接把模型文件拖放到 DanceXR 窗口中即时加载。支持的格式包括 `.pmx`、`.xps`、`.mesh` 和 `.mesh.ascii`。只要把文件拖进去，它就会出现在角色菜单中。

### 从内容库中加载

点击角色图标并选择 “Load Model”。你会看到 `actors` 文件夹中的所有模型列表。默认情况下，新模型会替换当前舞台上选中的模型。如果想添加而不是替换，请点击模型名称旁边的 “+” 图标。此功能仅在付费版本中可用。

---

## 5. 加载 VMD 动作

### 拖放加载

把音频文件拖到 DanceXR 窗口中即可立即加载。支持 WAV 和 OGG 格式。
把 VMD 或 BVH 格式的动作文件拖到 DanceXR 窗口中即可加载。如果当前选中的角色还没有分配动作，该动作会自动分配给它。

### 从内容库加载

点击音频 / 动作图标并选择 “Load Audio / Motion”。你会看到 `motions` 文件夹中的所有动作列表。

动作和音频会自动归组为 “dance sets”。加载后，你会在进度条中看到音频名称，并在舞蹈菜单中看到动作列表。要分配动作，可以先选择动作，再点击 “Assign To”；或者打开角色菜单，从已加载的动作中选择一个。

如需了解如何整理动作文件，请参阅 [内容库指南](/zh/dancexr/preparecontent#motion-files)。

---

## 接下来做什么？

现在你已经可以开始使用了。接下来可以继续深入了解 DanceXR 的更多功能：

- **[功能概览](/zh/dancexr/features)** — 浏览 DanceXR 的全部功能和工具
- **[准备内容库](/zh/dancexr/preparecontent)** — 详细了解如何整理模型、动作、舞台等内容
- **[物理效果](/zh/dancexr/features/physics)** — 布料模拟、头发物理、软体和布娃娃
- **[换装系统](/zh/dancexr/features/optionals)** — 更换服装、材质和配件
- **[相机](/zh/dancexr/features/camera_settings)** — Orbit cam、freefly、auto cam、第一人称等
- **[AI 聊天](/zh/dancexr/features/ai_chat)** — 通过语音和文字与角色对话
- **[创作者版](/zh/dancexr/creator)** — 面向内容创作者的离线 4K / VR 渲染
- **[故障排除](/zh/dancexr/troubleshooting)** — 解决常见问题
- **[支持与 FAQ](/zh/dancexr/support)** — 常见问题解答

祝你玩得开心。
