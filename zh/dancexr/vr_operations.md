---
layout: release
title: VR操作
locale: zh-CN
toc: true
---

# VR 操作

如何在 VR 中使用 DanceXR — 控制器、光标、抓取拖拽 UI、舒适度以及与桌面端不同的操作。有关技术 VR 设置（视差渲染、光标校准值、手部渲染开关），请参阅 [VR 设置](features/vr_settings)。有关输入映射表和抽象控制方案，请参阅 [控制与 UI](controls)。

---

## 手部控制器

每只手映射到：

- **扳机键（Trigger）** — 模拟输入，用于“自定义”动作，并且在与第二动作一起按住时用作 UI 开关
- **抓握（Grip）** — 默认分配给**第二动作**。按住它以访问其他任何控制器的第二动作。它也用于 UI 抓取（详见下文 [抓取拖拽 UI](#grip-drag-ui)）。
- **按钮 1 / 按钮 2** — 面板按钮（例如 Quest 控制器上的 A / B / X / Y）
- **拇指摇杆（Thumbstick）** — 拖动时移动和旋转角色；也用于 UI 滚动
- **菜单按钮（Menu button）** — 左手菜单 = 开关 UI / UI 返回；右手菜单 = 开关麦克风

默认设置列在 [控制与 UI](controls#default-mappings)。

### 手部渲染

VR 中可以显示或隐藏虚拟手。可以在 [VR 设置 → 手部](features/vr_settings#hand) 中切换。设置包括每只手是否启用、是否投射阴影和姿势预设。

---

## 光标（激光射线）

每个控制器都投射一个激光光标，用于操作菜单和拖拽可交互对象（角色选择盘、万向器立方体、道具）。

- **指向 UI 元素**即可高亮显示；**按下扳机键或按钮 1**即可选择。
- **指向角色的选择盘**并捏紧扳机键/按钮进行拖拽。
- **指向万向器立方体**即可抓取并摆姿势身体部位。

如果光标射线感觉偏差，请在 [VR 设置 → 光标](features/vr_settings#pointer) 中校准它。您可以调整方向、方向和偏移量。

### 虚拟空间中的鼠标模式

在 v2025.10 加入。它让您可以使用鼠标而不是（或除了）手部控制器来驱动光标。对于坐在桌前玩的用户很有用。结合键盘输入，这可在头戴设备内提供类似桌面的控制方案。可以在 [VR 设置 → UI → 虚拟空间中的鼠标模式](features/vr_settings#ui) 中启用。

### 光标手柄

在 v2025.10 加入。一个物理杆状模型，手握，由物理引擎驱动，您可以使用它来推和拨动角色。不适合工作场合使用（NSFW）；在纯净版本中不可用。您也可以加载任何具有骨骼链的外部模型作为自定义手柄使用。<!-- TODO: link to a Pointer Handle settings page if/when one exists -->

---

## 抓取拖拽 UI

菜单面板在 VR 中漂浮在您面前。要移动它：

1. 按住**抓握按钮（grip button）**，同时将手指向面板。
2. 将面板拖动到新的位置。
3. 松开抓握按钮即可将其留在原地。

如果面板漂离视线范围，**UI 自动返回**（在 [VR 设置 → UI](features/vr_settings#ui) 中）会平稳地将其带回您的视野。

您还可以使用**UI 距离**滑块（0.5–5 米）调整面板与您头部的休息距离。

---

## VR 中的开关状态

与桌面端相同的三个 UI 开关状态适用于 VR — 参见 [控制与 UI → 开关状态](controls#toggle-states)。可以通过点击空白区域，或按分配的**开关 UI**输入（默认左手菜单按钮）进行循环。

在**沉浸模式**下，面板和选择盘会消失，只留下场景本身——这对于纯粹被动观看非常有用。

---

## 舒适度与观看

<!-- TODO: confirm which of these settings actually exist. Below is what would belong here. -->

- **屏蔽桌面窗口** ([VR 设置 → UI](features/vr_settings#ui)) — 停止将头戴设备视图镜像到桌面显示器，以提高隐私性。
- **视差渲染** ([VR 设置 → 视差渲染](features/vr_settings#foveated-rendering)) — 目前仅在 Quest 版本上有效。它降低周边分辨率以释放 GPU 时间。等级越高 = 性能越高，边缘的模糊越明显。

---

## Quest 性能

Quest standalone 比 PC VR 更受资源限制。Quest 上有些功能表现不同：

- 无论 [角色选项 → 转换](features/loader_options#transition) 设置如何，为保持运行时成本低，角色加载/卸载**转换已被禁用**于 Quest 版本。
- 内容库存储在存储上的 `/DanceXR/`（2024.3 版本后）；请参阅 [Android 和 Quest 上的内容库](content_android_quest)。
- 在 **自动模式**下使用语音转文本在 Quest 上不推荐，因为音频处理太慢；建议使用**手动模式**。请参阅 [AI 语音聊天 → 语音转文本](features/ai_chat#speech-to-text)。

---

## VR 中的麦克风

AI 聊天的麦克风开关默认映射到**右手菜单按钮**。您可以在输入设置中重新绑定它；请参阅 [AI 语音聊天 → 键绑定](features/ai_chat#key-binding)。

为了在 VR 中获得最佳效果，请在启动 DanceXR 之前，在您的操作系统音频设置中选择头戴设备的内置麦克风作为输入设备。

---

## AR 模式（移动设备/Quest）

AR 模式使用设备的相机透视，使角色看起来像是站在您的真实环境中。在支持的移动设备和 Quest 版本上可用；专业版。请参阅 [AR 模式](features/ar_mode)。

---

## 相关页面

- [控制与 UI](controls) — 输入映射和选择盘行为
- [VR 设置](features/vr_settings) — 光标校准、视差渲染、手部渲染
- [AI 语音聊天](features/ai_chat) — 麦克风设置
- [概念与术语表](concepts) — 开关状态、万向器立方体、选择盘