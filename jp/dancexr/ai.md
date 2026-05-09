---
layout: release
title: ダンスXRにおけるAI
locale: ja-JP
toc: true
---

# DanceXRにおけるAI

DanceXRにはいくつかのAI駆動型機能があります。これらのほとんどは、音声合成、大規模言語モデルのチャット、およびサポートサービスを単一のプロセスにバンドルするローカルバックエンド「**DanceXR Operator**」を経由します。このページは概要であり、各機能には詳細ページがあります。

用語（Operator、TTS、STT、persona、template）については、[Concepts & glossary](concepts#ai-backends)を参照してください。

---

## 全体像

- **Operator** はローカルのAIバックエンドです。DanceXRと並行して分離したプロセスとして実行されます。詳細は[DanceXR Operator](features/operator)を参照してください。
- **AI Voice Chat** は、Operatorを利用するユーザー向けのチャット体験です。詳細は[AI Powered Voice Chat](features/ai_chat)を参照してください。


---

## DanceXR Operator

[Operator](features/operator) は、**2026.5**で導入された専用のローカルバックエンドです。以下の要素をバンドルしています。

- **TTS** — Kokoro：テキストの応答を音声に変換します。
- **LLM** — llama.cpp：チャットの生成に使用されます。
- **HTTP API** — `http://localhost:8110` の統一エンドポイント。
- **Web interface** — モデル管理、TTSプレビュー、ベンチマーク。

Operatorは、DanceXRでAIチャットを有効にすると自動的に起動し、DanceXRが終了すると自動的にシャットダウンします。また、`Operator.exe`から手動で起動することも可能です。

### クラウドサービスではなくOperatorである理由

- プライバシー — チャット履歴はマシンから外部に送信されることはありません。
- サブスクリプションやレート制限がありません。
- 2026.5以降の、より長くシーンを認識したロールプレイセッションの安定した基盤を提供します。
- 音声とチャットの両方を単一のインストールで処理できます。

トレードオフとなるのはハードウェアの要件です。選択したLLMモデルを実行するために、ゲーミングクラスのGPUと十分なRAM/VRAMが必要です。

良好な体験を得るためには、最低16GBのRAMと、6GB以上のVRAMを持つGPUを持つことが推奨されます。OperatorのWeb UIでは、低スペックなハードウェア向けにより小型のモデルを選択できますが、パフォーマンスは変動します。