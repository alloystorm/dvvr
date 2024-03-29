---
locale: ja-JP
layout: single
title: トラブルシューティングオプション
toc: true
sidebar:
  nav: "docs-jp"
---

[Eng](/dancexr/features/troubleshooting_options) | [繁中](/tw/dancexr/features/troubleshooting_options) | [日本語](/jp/dancexr/features/troubleshooting_options) | [한국어](/kr/dancexr/features/troubleshooting_options) | [简中](/zh/dancexr/features/troubleshooting_options)

## 概要
これらはモデルの一般的な問題を処理するために設計されたオプションです。

### 体の回転を中心に適用する
これにより、胴体と腰の回転が中心のボーンに適用されます。ほとんどのモデルでは、位置オフセット以外に中心のボーンは使用されませんが、一部のモデルでは腰の領域が中心のボーンにリグされています。したがって、腰の領域がねじれないように、中心のボーンを回転させる必要があります。

### ねじれ補正
これにより、腕のボーンのねじれが過度にならないように調整されます。モーションが正常範囲を超えて腕のボーンをねじれさせる場合に便利です。

### 手のスケール
一部のモデルでは手が大きすぎる場合があります。このオプションを使用すると、手のサイズを自分の希望するサイズにスケールすることができます。

### BVHの親指のモーション
一部のBVHモーションには奇妙な親指のモーションがあります。このオプションを使用すると、親指のモーションを縮小したり完全に無効にしたりすることができます。