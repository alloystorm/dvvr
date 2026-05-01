---
layout: release
title: DanceXR Operator
locale: ja-JP
nav_links:
  - label: イントロ
    url: /jp/dancexr
  - label: 機能
    url: /jp/dancexr/features
  - label: リリース
    url: /jp/dancexr/releases
  - label: ダウンロード
    url: /jp/dancexr/download
---


# DanceXR Operator
DanceXR Operator は DanceXR 専用の AI バックエンドであり、高度な音声合成、大規模言語モデル (LLM) チャット、ダイナミックなロールプレイ機能をゲームに提供します。

## 概要
Operator はローカルサーバーとして動作し、Kokoro TTS と llama.cpp LLM を統一 HTTP API の背後にまとめ、DanceXR の Unity クライアントとシームレスに連携するよう設計されています。

Operator を使うことで、自然なキャラクターボイスを生成し、ゲーム内 AI 会話を有効にし、柔軟なプロンプトテンプレートでカスタムロールプレイシナリオを管理できます。サーバーは複数の言語と音声をサポートし、モデル管理やベンチマーク用のツールも備えています。

初回のモデルダウンロード後はインターネット接続なしで動作し、すべて自分のハードウェア上で実行されます。DanceXR Operator は、AI 駆動の機能を DanceXR 体験に直接追加します。

## インストール
DanceXR フォルダーの横にダウンロードしてインストールするだけです。

推奨フォルダー構成:
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

ダウンロードリンク:
https://github.com/alloystorm/dvvr/releases/download/operator1.0/operator-install-lite-1.0.exe

## 使用方法

### 自動起動
上記の構成でインストールされている場合、DanceXR で AI Chat を有効にすると Operator は自動的に起動します。

システムトレイアイコンが表示され、Operator の Web インターフェースへアクセスしたり、状態を確認したりできます。

DanceXR を終了してしばらくすると、Operator は自動的に自身を終了します。

### 手動起動
`Operator.exe` を実行して手動で起動することもできます。

システムトレイアイコンが表示され、アイコンをクリックすることで Web インターフェースへのアクセスや終了操作ができます。

### Web インターフェース
デフォルトでは、Operator の Web インターフェースは `http://localhost:8110` で利用できます。主なセクションは次のとおりです。

- **Model Management**: LLM モデルのダウンロードと切り替え
- **TTS Preview**: TTS 音声の試聴
- **Benchmarking**: LLM のパフォーマンスベンチマークの実行