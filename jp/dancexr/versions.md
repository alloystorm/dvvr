---
layout: single
title: ダウンロード
toc: true
sidebar:
  nav: "docs-jp"
---

[English](/dancexr/versions) | [简体中文](/zh/dancexr/versions) | [日本語](/jp/dancexr/versions)

## 概要
DanceXRには、異なるバージョンがあり、異なる機能セットとレンダリング技術があります。これにより、さまざまなプラットフォームの能力に合わせることができます。

## レンダリングパイプライン
LW、HD、RTは異なるレンダリングパイプラインを表します。

LWはUnity Universal Render Pipelineを使用しており、これはモバイルプラットフォームや低性能なコンピューターでもうまく動作する、最もパフォーマンスの高いオプションです。

HDはUnity HDRPを使用しており、これはより高品質なグラフィックスに焦点を当てていますが、高性能なPCでもVRを利用することができます。

RTはレイトレーシングを使用しており、最高のグラフィックスを提供しますが、VRでフルフレームレートで実行できない場合があります。

HDとRTはモバイルプラットフォームでは利用できないため、Android、Quest、PicoビルドではLWオプションのみが利用可能です。

## 機能セット
Free、Pure、Pro、Creatorの4つのティアがあり、異なる機能を提供しています。

Freeバージョンでは、一度に1つのアクターしか読み込むことができず、高度な機能が欠けています。

Pureバージョンには高度な機能がありますが、NSFW機能はありません。

Proバージョンには、オフラインレンダリングやビデオキャプチャの機能など、Creator専用の機能を除くすべての機能が備わっています。

## リリースプラットフォーム
Patreon、Itch.io、Steamで利用可能です。

利用可能なプラットフォームは以下の通りです。

| プラットフォーム＆ティア | Pure | Pro | RT | Creator | Quest / Pico | Android |
| --- | --- | --- | --- | --- | --- | --- | 
| Patreon Patronティア |  | * | |  |  | |
| Patreon Proティア |  | * | * |  | * | |
| Patreon Creatorティア |  | * | * | * | * | |
| Itch.io PC | | * | | | | |
| Itch.io Quest | | | | | * | |
| Itch.io Android Pro | | | | | | * |
| Steam Pure | * | | | | | |
| Steam Pro | | * | | | | |
| Steam Raytracing | | * | * | | | |