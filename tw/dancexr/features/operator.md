---
layout: release
title: DanceXR Operator
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---
[Eng](/dancexr/features/operator) | [繁中](/tw/dancexr/features/operator) | [日本語](/jp/dancexr/features/operator) | [한국어](/kr/dancexr/features/operator) | [简中](/zh/dancexr/features/operator)

# DanceXR Operator
DanceXR Operator 是 DanceXR 的專用 AI 後端，為遊戲提供進階語音合成、大型語言模型 (LLM) 聊天與動態角色扮演功能。

## 概述
Operator 會以本地伺服器形式運作，將 Kokoro TTS 與 llama.cpp LLM 整合在統一的 HTTP API 背後，並設計成可與 DanceXR 的 Unity 用戶端無縫配合。

透過 Operator，您可以生成更自然的角色語音、啟用遊戲內 AI 對話，並利用彈性的提示模板管理自訂角色扮演場景。此服務支援多種語言與聲音，並提供模型管理與效能測試工具。

在初次下載模型後，它即可完全在您自己的硬體上執行，不需要持續連線。DanceXR Operator 將強大的 AI 驅動功能直接帶入 DanceXR 體驗中。

## 安裝
只要下載並安裝在 DanceXR 資料夾旁邊即可。

建議的資料夾結構：
```
DanceXR Root Folder
├─ content
├─ DanceXR HD Pro_WIN64
├─ DanceXR RT Pro_WIN64
├─ [other DanceXR versions]
└─ Operator
   ├─ Operator.exe
   └─ [other Operator files]
```

下載連結：
https://github.com/alloystorm/dvvr/releases/download/operator1.0/operator-install-lite-1.0.exe

## 使用方式

### 自動啟動
如果依照上述結構安裝，當您在 DanceXR 中啟用 AI Chat 時，Operator 會自動啟動。

系統匣中會出現圖示，讓您可以開啟 Operator 的 Web 介面並查看狀態。

在您離開 DanceXR 一段時間後，Operator 會自動關閉自己。

### 手動啟動
您也可以直接執行 `Operator.exe` 來手動啟動。

系統匣圖示會出現，您可以點擊圖示開啟 Web 介面或關閉服務。

### Web 介面
預設情況下，Operator 的 Web 介面位於 `http://localhost:8110`。其中包含以下區段：

- **Model Management**: 下載與切換 LLM 模型
- **TTS Preview**: 試聽 TTS 聲音
- **Benchmarking**: 執行 LLM 效能測試