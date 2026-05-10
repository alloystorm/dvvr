---
layout: release
title: オーディオオプション
locale: ja-JP
toc: true
---

# オーディオオプション

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.5, 2024.7, 2024.9, 2025.5, 2026.2). -->

Audio Options は、現在の [dance set](dance_set) 内のオーディオトラックの再生方法（ループ、音量、オーディオソースのシーン内での配置方法を含む）を制御します。

---

## 再生モード

オーディオがロードされたコンテンツをどのように進行させるかを選択します。

- **Single** — 現在のトラックを1回再生します。
- **Loop** — 現在のトラックを繰り返します。ループ領域が設定されている場合（開始/終了時間）、その領域のみがループします。
- **Shuffle** — キューから次のトラックをランダムに選択します。
- <!-- TODO: confirm whether "Sequential / next in folder" is also a separate mode. -->

オーディオのループは、モーションのループとは独立しています（2024.5で追加）。モーションを再生しつつオーディオのみをループさせるか、またはその逆が可能です。

---

## 音量

オーディオトラックの標準マスター音量スライダーです。

<!-- TODO: confirm whether per-actor / per-source volume controls live here or under Playback Options. -->

---

## 空間オーディオ

オーディオを単なるステレオミックスとして再生するのではなく、シーン内の3D位置に固定します。[Spatial Audio](spatial_audio)を参照してください。

---

## オーディオ解析

音楽のBPM検出、ビート検出、コーラスセクションデータは、このレイヤーから取得されます。以下を参照してください：

- BPMとビートオフセットの設定については、[Music Timing](music_timing)。
- オーディオレベルやビートを他の設定のデータソースとして使用するには、[Auto Update](autoupdate)。
- オーディオのリアクティブな視覚化については、[Beats Ring](beats_ring) および新しい Audio Visualizer。

リアルタイムオーディオアナライザーは、2025.5でビート検出機能が拡張されたため、事前に計算されたタイミングなしで、プロシージャルモーションがライブビートに反応できるようになりました。

---

## オーディオ / モーション同期

オーディオの時間とモーションの時間にズレが生じた場合、DanceXRが自動的に再同期を行います。**オーディオをモーションに同期**するか、**モーションをオーディオに同期**するかを選択してください。詳細は [Motion Settings](motion_settings) を参照してください。

オーディオのタイミングは2026.2でさらに改善され、可変フレームレート時のカクつきが軽減され、2026.3ではフレームレートが大きく変動した場合の振動問題が修正されました。

---

## 関連ページ

- [Playback Options](playback_options)
- [Music Timing](music_timing)
- [Dance Set](dance_set)
- [Spatial Audio](spatial_audio)
- [LipSync](lipsync)