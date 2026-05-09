---
layout: release
title: DanceXR 中的 AI
locale: zh-TW
toc: true
---

# DanceXR 中的 AI

DanceXR 具有多個由 AI 驅動的功能。大多數這些功能都通過一個本地後端——**DanceXR Operator**——運行，它在您的硬體上運行，並將語音合成、大型語言模型聊天和支援服務打包成一個單一程序。本頁是概述；每個功能都有其詳細頁面。

對於術語 (Operator、TTS、STT、persona、template)，請參閱 [Concepts & glossary](/dancexr/concepts#ai-backends)。

---

## 概覽

- **Operator** 是本地 AI 後端。它作為一個獨立的程序與 DanceXR 並行運行。參見 [DanceXR Operator](/dancexr/features/operator)。
- **AI Voice Chat** 是使用者介面的聊天體驗，它使用 Operator。參見 [AI Powered Voice Chat](/dancexr/features/ai_chat)。

---

## DanceXR Operator

[Operator](/dancexr/features/operator) 是在 **2026.5** 版本中引入的專用本地後端。它打包了：

- **TTS** — Kokoro，用於將文字回覆轉換為語音。
- **LLM** — llama.cpp，用於聊天生成。
- **HTTP API** — 統一的端點，位於 `http://localhost:8110`。
- **Web interface** — 模型管理、TTS 預覽和基準測試。

當您在 DanceXR 中啟用 AI Chat 時，Operator 會自動啟動，並且在 DanceXR 退出後會自行關閉。您也可以從 `Operator.exe` 手動啟動它。

### 為什麼選擇 Operator 而不使用雲端服務

- 隱私權 — 聊天記錄永遠不會離開您的機器。
- 無需訂閱或速率限制。
- 為 2026.5 版本及之後的更長、具有場景意識的角色扮演會議提供了穩定的基礎。
- 一次安裝即可同時處理語音和聊天。

唯一的權衡點在於硬體：您需要一個遊戲級 GPU，以及足夠的 RAM/VRAM 來運行所選擇的 LLM 模型。

建議至少配備 16GB RAM 和具有 6GB+ VRAM 的 GPU，以獲得良好的體驗。對於較低階的硬體，您可以在 Operator 的 Web UI 中選擇較小的模型，但性能會有所不同。