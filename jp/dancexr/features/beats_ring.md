---
layout: release
title: ビーツリング
locale: ja-JP
---

# ビーツリング

<!-- TODO: full description. The Beats Ring is referenced as a tile on /dancexr/features under Stage & Props but no other page describes it. Likely an audio-reactive visualizer ring; confirm and fill in. -->

ビーツリングは、音楽に合わせて脈動する、オーディオリアクティブなビジュアライザープロップです。これは[auto-update](/dancexr/features/autoupdate) データソースの一つであり、他の設定がその出力を利用して自動的に動く（駆動できる）ことを意味します。

---

## 何をするか

<!-- TODO: confirm shape (ring? particles? geometry?), where it is rendered (around the actor? on the stage?), how it scales with audio. -->

ビーツリングは現在のオーディオ信号を受け取り、ビートを駆動する値を生成し、これを使用して以下のことが可能です。

- アクターまたはステージの周りに可視のリングまたはパルスエフェクトをレンダリングする。
- 他のauto-updateパラメータ（ライティングの強度、マテリアルパラメータ、モーション速度）を音楽と同期して駆動する。

---

## 有効化

<!-- TODO: confirm the menu path. Likely under environment menu or a per-actor setting. -->

---

## 設定

<!-- TODO: list. Possibly: visibility, color, scale, sensitivity threshold, smoothing. -->

---

## 関連ページ

- [Auto update](/dancexr/features/autoupdate) — ビーツリングを他の設定のデータソースとして使用する
- [Music timing](/dancexr/features/music_timing) — 音楽へのモーション同期
- [Audio options](/dancexr/features/audio_options)