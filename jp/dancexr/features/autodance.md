---
layout: release
title: 自動ダンス
locale: ja-JP
toc: true
---

# オートダンス

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

オートダンスは、**ファーストジェネレーション**のプロシージャルダンスジェネレーターです。内蔵のモーションライブラリからダンスムーブをオンザフライで生成し、音楽のビートと音量に応じてムーブを選択し、ブレンドします。

オートダンスは、[Auto Dance 2](autodance#auto-dance-2) および [Auto Dance 3](autodance3) によって大部分が置き換えられています。新しいバージョンは、より多くのバリエーション、より細かい制御、そしてより優れた音楽同期を実現しています。オリジナルのジェネレーターの挙動を特に使用したい場合に、オートダンスを使用してください。

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
- **[Auto Dance 2](autodance#auto-dance-2)** — セカンドジェネレーション。より大きなプールで、ムーブ間のバリエーションが増加しています。
- **[Auto Dance 3](autodance3)** — 現在のデフォルト。カスタマイズ性が高く、[Sex Motion 3](sex_motion_3)の共有モーション制御システムと統合され、ビート検出を伴うリアルタイムオーディオアナライザーを使用します。

---

## 関連ページ

- [Auto Dance 2](autodance#auto-dance-2)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)

## Auto Dance 2 {#auto-dance-2}

# Auto Dance 2

<!-- TODO: confirm settings. Drafted from procedural-motion family. -->

Auto Dance 2は、**2世代目**のプロシージャルダンスジェネレーターです。オリジナル版の[Auto Dance](autodance)から、より大きなモーションプール、連続するムーブ間の改善されたバリエーション、そして音楽のビートと音量へのよりクリーンな同期を実現し、改良されています。

Auto Dance 2自体は、[Sex Motion 3](sex_motion_3)と共有される最新のモーションコントロールシステムを使用し、リアルタイムオーディオアナライザーと統合された[Auto Dance 3](autodance3)によって後継されています。

---

## Auto Dance 1からの変更点

- 内蔵ダンスセグメントのプールが拡大しました。
- 連続するムーブ間のブレンドが改善され、スライドショーのように見えることが減少しました。
- 音楽の音量への反応が向上しました。高エネルギーの部分では、より大きなムーブが生成されます。

---

## 設定

<!-- TODO: confirm exact settings. Likely candidates:
- Variety / pool size
- Energy multiplier
- Random seed (for reproducible sequences) -->

---

## Auto Dance 2を選択するタイミング

Auto Dance 2が必要なのは、以下のようなプロシージャルダンスを求める場合です。

- オリジナルのAuto Danceよりもバリエーション豊かであること。
- 設定が非常に細かいAuto Dance 3よりもシンプルであること — ノブ（調整項目）が少なく、設定が速い。

新しいプロジェクトでは、Auto Dance 2の動作を特別に求めている場合を除き、[Auto Dance 3](autodance3)を推奨します。

---

## 関連ページ

- [Auto Dance](autodance)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)
