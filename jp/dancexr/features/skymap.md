---
locale: ja-JP
layout: single
title: 空と雲
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/skymap) | [繁中](/tw/dancexr/features/skymap) | [日本語](/jp/dancexr/features/skymap) | [한국어](/kr/dancexr/features/skymap) | [简中](/zh/dancexr/features/skymap)

## スカイモード
スカイをレンダリングするために、スカイマップ、純色、またはプロシージャルモードを選択できます。

## クエスト上
パフォーマンス上の理由から、クエスト上ではスカイマップやプロシージャルオプションは使用できません。スカイカラーオプションはライティング構成にあります。ミックスリアリティを可能にするために、背景の透明度を制御する追加のパススルースライダーがあります。

## PC上のパススルー
特定のPC VRストリーミングプログラムでは、純色の背景をパススルー画像で置き換えることができます。スカイをカラーモードに設定し、ストリーミングシステムが使用する色（例えば、真っ黒や緑）を選択することで、これを実現できます。

## 雲
風に影響を受け、時間とともにリアルに変化する雲をプロシージャルに生成します。

## スカイマップ
HDRI全天周画像をスカイマップとして使用できます。jpgフォーマットとHDRフォーマットの両方がサポートされています。

{% include video id="2NZpffP1X5o" provider="youtube" %}

{% include video id="vUY7DY4cCV0" provider="youtube" %}

スカイマップを見つけ、DanceXRに背景として読み込んでください。

## プロシージャルスカイ
- 太陽光の角度は、昼の時間、黄道角、および方向で制御されます。
- 昼と夜の自動的な切り替えは、昼の時間の値に基づいて行われます。
- 星のある夜空
{% include video id="D745FYNcx4c" provider="youtube" %}