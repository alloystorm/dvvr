---
layout: release
title: 空間オーディオ
locale: ja-JP
toc: true
---

# 空間オーディオ

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. -->

空間オーディオは、ステレオミックスとしてではなく、3D空間上の特定の位置からシーンの音声を再生します。音声をアクターの頭部にアンカーすることで、その音はアクターと一緒に動き、VRや複数アクターのステージにおいて、強い存在感をもたらします。

**2024.9**で追加されました。

---

## 空間オーディオの有効化

<!-- TODO: confirm exact menu path. Drafted from the release notes which name the option as "Spatialize" under Playback Options. -->

1. [再生オプション](playback_options)を開きます。
2. **Spatialize**をオンにします。
3. ドロップダウンからアクターを選択します — そのアクターの**頭部の位置**が音声ソースになります。

その後、音声は距離に応じて減衰し、カメラまたはVRヘッドセットに対して正しくパンニングされます。

---

## 動作

- 音声ソースは、アクターが動くにつれて、選択したアクターの頭部ボーンを追跡します。
- VRでは、このエフェクトはヘッドトラッキングを使用するため、頭を動かすと左右のバランスが自然に変化します。
- <!-- TODO: confirm whether stereo is preserved or audio is downmixed to mono at the source. -->
- <!-- TODO: confirm distance attenuation curve and whether it is configurable. -->

---

## LipSyncとの組み合わせ

空間オーディオは、同じリリースで導入された[音声駆動のリップシンク](lipsync)と自然に組み合わせます。音声をアクターの頭部にアンカーし、そのアクターの口を同じ音声で駆動させることで、「このアクターが話している」という一貫した効果が得られます。

---

## 制限事項

<!-- TODO: confirm. Likely areas to verify: which audio types this applies to (music vs voice chat vs video), behavior with multiple actors, behavior on Android / Quest, behavior in AR mode. -->

---

## 関連ページ

- [再生オプション](playback_options)
- [オーディオオプション](audio_options)
- [LipSync](lipsync)
- [AI音声チャット](ai_chat)