---
layout: release
title: 自動ダンス
locale: ja-JP
toc: true
---

# オートダンス

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

オートダンスは、**ファーストジェネレーション**のプロシージャルダンスジェネレーターです。内蔵のモーションライブラリからダンスムーブをオンザフライで生成し、音楽のビートと音量に応じてムーブを選択し、ブレンドします。

オートダンスは、[Auto Dance 2](autodance2) および [Auto Dance 3](autodance3) によって大部分が置き換えられています。新しいバージョンは、より多くのバリエーション、より細かい制御、そしてより優れた音楽同期を実現しています。オリジナルのジェネレーターの挙動を特に使用したい場合に、オートダンスを使用してください。

---

## 仕組み

- DanceXRは、再生中のオーディオから**ビート**（タイミング）と**音量**（エネルギー）を分析します。
- 各ビートにおいて、ジェネレーターは、短く作成されたダンスセグメントのライブラリから次のムーブを選び、前のムーブとブレンドします。
- 音量の高いセクションでは、より大きく、よりエネルギッシュなムーブがトリガーされます。

オートダンスの場合、VMDファイルを読み込む必要はありません。ムーブが生成されるためです。

---

## 設定

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## オートダンスと新しいバージョンを使い分ける際の選択基準

- **オートダンス（本ページ）** — オリジナルのジェネレーター。ムーブライブラリが小さく、音楽への応答がシンプルです。
- **[Auto Dance 2](autodance2)** — セカンドジェネレーション。より大きなプールで、ムーブ間のバリエーションが増加しています。
- **[Auto Dance 3](autodance3)** — 現在のデフォルト。カスタマイズ性が高く、[Sex Motion 3](sex_motion_3)の共有モーション制御システムと統合され、ビート検出を伴うリアルタイムオーディオアナライザーを使用します。

---

## 関連ページ

- [Auto Dance 2](autodance2)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)