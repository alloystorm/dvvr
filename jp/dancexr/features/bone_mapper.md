---
layout: single
title: XPSボーンマッパー
toc: true
sidebar:
  nav: "docs-jp"
---
[English](/dancexr/features/bone_mapper) | [简体中文](/zh/dancexr/features/bone_mapper) | [日本語](/jp/dancexr/features/bone_mapper)


## 概要
XPSモデルでは、アニメーションやその他の機能が正しいボーンを見つけるためにボーンマッピングが必要です。

モデルを読み込んでも標準のポーズのままであれば、動作させるためには以下の手順が必要です。

{% include video id="g0VAfBHauXw" provider="youtube" %}

## マッピングの状態
ボーンのほとんどはすでにプログラムによってマッピングされていますが、一部のボーンが不足している場合があります。"!"マークが付いているボーンのみをマッピングすれば、モデルは正常に動作します。

ボーンマッピングの状態は、円形のアイコンで示されます。
* 空の円はボーンがマッピングされていないことを意味しますが、重要ではないため、そのボーンがマッピングされていなくてもモデルは動作します。
* 円内に点がある円は、ボーンがすでにマッピングされていることを意味します。
* ビックリマークが付いている円は、ボーンがマッピングされておらず、モデルの動作には重要です。

{% include video id="jtxQo5NYk2o" provider="youtube" %}

## その他のデモ
以下は、FBXモデルをXPS形式に変換し、ボーンマッパーを使用してDanceXRで動作させるデモのビデオです。

{% include video id="YqX_uktVvQk" provider="youtube" %}
{% include video id="BV1CF411o7P2" provider="bilibili" %}