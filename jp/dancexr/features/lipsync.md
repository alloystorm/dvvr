---
layout: release
title: リップシンク
locale: ja-JP
toc: true
---

# LipSync

LipSyncは、音響信号からアクターの口の形をリアルタイムで駆動するため、キャラクターが再生されている音源に合わせて話している、または歌っているように見えます。以前の[AI Voice Chat](ai_chat)内に存在していたリップシンクとは異なり、このシステムはAndroidやQuestを含む**すべてのプラットフォームで利用可能**です。

**2024.9**に追加されました。

---

## LipSyncの有効化

<!-- TODO: confirm exact UI path. -->

1. [Playback Options](playback_options)でLipSyncをグローバルにオンにします。
2. 口を動かすべきアクターごとに、[Facial Control](facial_control)を開き、**LipSync**を有効にします。

両方のトグルが必要です。グローバルなトグルは、音声が解析されるかどうかを制御し、アクターごとのトグルは、どのキャラクターがそれに対応するかを制御します。

---

## 空間オーディオとの組み合わせ

LipSyncは[Spatial Audio](spatial_audio)と自然に組み合わさります。音声をアクターの頭にアンカーし、同じアクターでLipSyncを有効にすると、「このキャラクターが話している」という結果が読み取られます。

---

## AI Voice Chatとの組み合わせ

[AI Voice Chat](ai_chat)は、LipSyncシステムが音楽やビデオ音声と同じように解析できる発話音声を駆動します。<!-- TODO: confirm whether AI Voice Chat uses LipSync directly, or its own internal mouth driver, or both. -->

---

## 設定

<!-- TODO: list. Likely candidates: sensitivity / gain, smoothing, mouth-open intensity, which morph(s) drive what. -->

---

## 制限事項

<!-- TODO: confirm. Areas to verify:
- Does it require specific blendshapes / morphs (a / i / u / e / o)? What if the model lacks them?
- Does it work with PMX, XPS, and FBX equally?
- Latency on Android / Quest. -->

---

## 関連ページ

- [Playback Options](playback_options)
- [Facial Control](facial_control)
- [Spatial Audio](spatial_audio)
- [AI Voice Chat](ai_chat)
- [Blink, Breathing & Eye Contact](eyecontact)