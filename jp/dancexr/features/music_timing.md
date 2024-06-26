---
locale: ja-JP
layout: single
title: 音楽のタイミング
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本語](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)


## 概要
音楽のタイミング情報は、すべての手続き的な動きにとって非常に重要です。なぜなら、それは動きを音楽に合わせるために使用されるからです。それがなければ、BPM（1分間の拍数）はデフォルトで120になり、音楽と同期しません。

## デモ
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## タップビート
正確なタイミング情報を簡単に設定するための「タップビート」機能があります。

やることは、音楽を再生し、ビートが落ちるたびにボタンをタップすることです。プログラムは、平均BPMとオフセット値を計算するために約4回のタップを必要とします。正しく設定されている場合、床の光点が音楽のビートと完全に一致することが、光るリングから分かります。最初に正確に合わせられなかった場合でも、すべてが正しく見えるまでビートをタップし続けてください。

以前は、アプリケーションにバンドルされているコマンドラインツールを使用して、ライブラリ内の各音楽ファイルを解析し、タイミング情報を生成していました。この方法はまだ機能しますが、使用が少し難しく、WAV形式のみをサポートし、ZIPから読み取ることはできません。古い方法のビデオ：

{% include video id="chI-3GQS08Q" provider="youtube" %}