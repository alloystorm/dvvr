---
locale: zh-CN
layout: single
title: DanceXR Operator
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/operator) | [繁中](/tw/dancexr/features/operator) | [日本語](/jp/dancexr/features/operator) | [한국어](/kr/dancexr/features/operator) | [简中](/zh/dancexr/features/operator)

# DanceXR Operator
DanceXR Operator 是 DanceXR 的专用 AI 后端，为游戏提供高级语音合成、大语言模型 (LLM) 聊天以及动态角色扮演功能。

## 概述
Operator 以本地服务器形式运行，将 Kokoro TTS 和 llama.cpp LLM 封装在统一的 HTTP API 之后，并被设计为与 DanceXR 的 Unity 客户端无缝协作。

通过 Operator，您可以生成更自然的角色语音、启用游戏内 AI 对话，并通过灵活的提示模板管理自定义角色扮演场景。该服务支持多种语言和语音，并包含模型管理和性能测试工具。

初次下载模型之后，它可以完全在您自己的硬件上运行，无需持续联网。DanceXR Operator 将强大的 AI 驱动能力直接带入 DanceXR 体验。

## 安装
只需下载并安装到 DanceXR 文件夹旁边即可。

推荐目录结构：
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

下载链接：
https://github.com/alloystorm/dvvr/releases/download/operator1.0/operator-install-lite-1.0.exe

## 使用方法

### 自动启动
如果按上述结构安装，当您在 DanceXR 中启用 AI Chat 时，Operator 会自动启动。

系统托盘中会出现图标，方便您打开 Operator 的 Web 界面并查看其状态。

在您退出 DanceXR 一段时间后，Operator 会自动关闭自身。

### 手动启动
您也可以通过运行 `Operator.exe` 手动启动它。

系统托盘图标会出现，您可以点击图标打开 Web 界面或关闭服务。

### Web 界面
默认情况下，Operator 的 Web 界面位于 `http://localhost:8110`。它包含以下部分：

- **Model Management**: 下载并切换 LLM 模型
- **TTS Preview**: 试听 TTS 语音
- **Benchmarking**: 运行 LLM 性能测试