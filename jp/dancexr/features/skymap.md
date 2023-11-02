---
layout: single
title: 空と雲
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/skymap) | [繁中](/tw/dancexr/features/skymap) | [日本語](/jp/dancexr/features/skymap) | [한국어](/kr/dancexr/features/skymap) | [简中](/zh/dancexr/features/skymap)


## 空のモード
空をレンダリングするために、スカイマップ、純色、または手続き的なモードを選択することができます。

## QuestとPicoで
パフォーマンスの理由から、QuestとPicoデバイスではスカイマップや手続き的なオプションは使用できません。スカイの色のオプションは、ライティングの設定にあります。ミックスリアリティを可能にするために、背景の透明度を制御する追加のパススルーのスライダーがあります。

## PC上のパススルー
特定のPC VRストリーミングプログラムでは、純色の背景をパススルーイメージで置き換えることができます。スカイをカラーモードに設定し、ストリーミングシステムが使用する色（例えば純黒または緑）を選択することで、これを実現できます。

## 雲
風に影響を受け、時間の経過とともに現実的に変化する手続き的に生成された雲です。

## スカイマップ
HDRIパノラマ画像をスカイマップとして使用することができます。jpgとHDR形式の両方がサポートされています。

{% include video id="2NZpffP1X5o" provider="youtube" %}

{% include video id="vUY7DY4cCV0" provider="youtube" %}

Skymapsを見つけてDanceXRの背景として読み込んでください。

## 手続き的なスカイ
* 太陽光の角度は、日時、黄道傾斜角、および方向によって制御されます。
* 日中と夜間の自動的な切り替えは、日時の値に基づいて行われます。
* 星のある夜空
{% include video id="D745FYNcx4c" provider="youtube" %}