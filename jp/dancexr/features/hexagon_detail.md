---
locale: ja-JP
layout: single
toc: true
title: 六角形パターン詳細マップ
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/hexagon_detail) | [繁中](/tw/dancexr/features/hexagon_detail) | [日本語](/jp/dancexr/features/hexagon_detail) | [한국어](/kr/dancexr/features/hexagon_detail) | [简中](/zh/dancexr/features/hexagon_detail)

## ヘキサゴンパターン詳細マップ
これは即座に生成されるプロシージャルな詳細マップです。詳細マップをサポートするマテリアルカテゴリやアウトフィット効果で使用できます。

## 設定
* 密度: ヘキサゴンの密度。
* サークル: ヘキサゴンの代わりに円を使用します。
* サイズ: ヘキサゴンの中心領域のサイズ。
* バンプ: ヘキサゴンの側面のバンプ効果の強度。バンプの方向を逆にするために負の値にすることもできます。
* ノイズ: 各ヘキサゴンセルに対して法線マップにランダムな方向を追加します。
* ソフトエッジ: ヘキサゴンのエッジを柔らかくして通常のテクスチャに溶け込むようにします。

## 典型的な使用法
* マテリアルにヘキサゴンパターンのバンプ効果を追加する: 詳細マップとヘキサゴンパターンを有効にし、望ましい効果のためにバンプ値を調整します。
* マテリアルにキラキラ効果を追加する: 詳細マップとヘキサゴンパターンを有効にし、密度を増やしノイズ値を増やし、滑らかさと金属価値を調整します。

{% include video id="G9SSJQieO-E" provider="youtube" %}

{% include video id="BV1VD421W7YK" provider="bilibili" %}