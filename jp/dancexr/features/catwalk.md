---
layout: release
title: ランウェイウォーク
locale: ja-JP
toc: true
---

# ウォーキング（キャットウォーク）モーション

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

キャットウォークモーションは、プロシージャルなウォーキング/ランウェイモーションです。俳優は、VMDウォーキングモーションファイルを用意することなく、ファッションショーのような歩幅（腰の揺れ、意図的な足取り、頭の構えなど）でターゲットに向かって歩きます。

使用用途：

- 俳優がステージ外から登場するポーズシーン。
- ランウェイ/ファッションビデオ。
- 次のモーションが始まるまでの時間稼ぎ。

---

## 動作

- 俳優はシーンのZ軸に沿って（またはターゲットに向かって — <!-- TODO: confirm whether target selection is exposed -->）前進します。
- 歩調はプロシージャルです。音楽のBPMを設定した場合（[音楽タイミング](music_timing)）、ステップをビートに同期させることができます。
- このモーションはループします。停止するか、別のモーションを割り当ててまで、俳優は歩き続けます。

---

## 関連ページ

- [アイドルモーション](idle_motion)
- [オートダンス3](autodance3)
- [リアルなモーション](lifelike_motions)
- [足の調整](feet_adjustment)
- [音楽タイミング](music_timing)