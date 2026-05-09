---
layout: release
title: AI在DanceXR中
locale: zh-CN
toc: true
---

# DanceXR中的AI

DanceXR拥有多个由AI驱动的功能。其中大多数功能都通过一个本地后端——**DanceXR Operator**——运行。该后端在您的硬件上运行，并将语音合成、大型语言模型聊天和支持服务捆绑到一个进程中。本页面是概述；每个功能都有其详细页面。

有关术语（Operator、TTS、STT、persona、template），请参阅 [概念与术语表](concepts#ai-backends)。

---

## 宏观视图

- **Operator** 是本地AI后端。它作为独立进程与 DanceXR 并行运行。请参阅 [DanceXR Operator](features/operator)。
- **AI 语音聊天**是消费 Operator 的用户界面聊天体验。请参阅 [AI 语音聊天功能](features/ai_chat)。


---

## DanceXR Operator

[Operator](features/operator) 是在 **2026.5** 中引入的专用本地后端。它捆绑了：

- **TTS** — Kokoro，用于将文本回复转换为语音。
- **LLM** — llama.cpp，用于聊天生成。
- **HTTP API** — `http://localhost:8110` 的统一端点。
- **Web 界面** — 模型管理、TTS 预览、基准测试。

当您在 DanceXR 中启用 AI 聊天时，Operator 会自动启动，并在 DanceXR 退出后自动关闭。您也可以从 `Operator.exe` 手动启动它。

### 为什么选择 Operator 而不是云服务

- 隐私——聊天记录永远不会离开您的机器。
- 无需订阅或速率限制。
- 为 2026.5 及更高版本中的更长、更具场景意识的角色扮演会话提供了稳定的基础。
- 一次安装即可同时处理语音和聊天。

唯一的权衡是硬件要求：您需要一个游戏级的 GPU 以及足够的 RAM/VRAM 来运行所选的 LLM 模型。

建议至少配备 16GB RAM 和具有 6GB+ VRAM 的 GPU 以获得良好的体验。您可以在 Operator 的网页 UI 中选择更小的模型，以支持低端硬件，但性能会有所不同。