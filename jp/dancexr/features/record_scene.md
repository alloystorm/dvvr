---
layout: feature
title: Record Scene
locale: ja-JP
toc: true
---

# Record Scene

**Record Scene** は、DanceXR Native で画面に映っているもの（アクター、そのクリップ、音楽、カメラ）をクリップとしてレンダリングし、**MP4** として保存します。専用のクロックでレンダリングするため、PC の実際のフレームレートに関係なく滑らかな結果になり、ウィンドウやモニターのサイズにも依存しません。**Creator** エディションの機能です。

Unity アプリの録画については、[Creator エディション](../creator)をご覧ください。

---

## クリップを収録する

**Scene > Record Scene** を開きます。

| 設定 | 選択肢 |
|---|---|
| **Name** | テイクの名前。 |
| **Size** | 1280 x 720、1920 x 1080、2560 x 1440、3840 x 2160、または 1080 x 1920（縦向き）。 |
| **Frame Rate** | 24、30、または 60。 |
| **Full Dance** | **Length** の代わりに、ダンスセット全体（音楽とすべてのクリップ）を最初から収録します。 |
| **Length** | 再生ヘッドから何秒収録するか（1〜120）。 |
| **Camera** | **Current view, as set up**、**Current view, fixed pose**、**Orbit the first actor**、**Leave to the scene**。 |

**Record Video** を押します。実行中はボタンが進行状況になり、**Stop Recording** で、それまでに書き込まれた分を保持して終了できます。**Show Folder** で、直近のテイクのフォルダーが開きます。

## カメラの選択

- **Current view, as set up** は、ダンサーを追うフリーフライのトラッキングを含め、カメラをそのまま再現します。キャラクターを追う視点は、追い続けます。
- **Current view, fixed pose** は、カメラの現在のポーズを保持し、トラッキングを無視します。
- **Orbit the first actor** は、ビューの位置から始めて、最初のキャラクターの周りを回ります。
- **Leave to the scene** は、独自のカメラを書き込みません。ダンスに専用のカメラモーションがある場合に使います。

## 動画に含まれるもの

- 読み込んだ音楽が、クリップの先頭からミックスされます。
- ハンドル、ホバーリング、カーソルなどの画面上の補助表示は含まれません。
- テイクは、アプリの隣の `recordings` フォルダーに、テイク名と時刻のフォルダーとして保存されます。

## 必要なもの

収録には **ffmpeg** が必要で、Native のアプリの隣の `ffmpeg` フォルダーに同梱されています。Native は、PC が対応する最初のビデオエンコーダー（NVIDIA、AMD、Intel、または Windows Media Foundation）を選び、ソフトウェアエンコードにフォールバックします。Record Scene メニューはすべてのエディションに表示されますが、収録できるのは有効化された Creator ライセンスだけです。

---

## 関連ページ

- [Creator エディション](../creator)
- [DanceXR Native](native)
