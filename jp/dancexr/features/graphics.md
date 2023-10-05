---
layout: single
title: グラフィックス
toc: true
---
[English](/dancexr/features/graphics) | [简体中文](/zh/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics)


## 特殊なレンダリングモード：デプスとノーマル
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 以前のカートゥーンシェーダーは、デプスとノーマルの2つのモードを含むように拡張されました。
* これらは、Stable Diffusion ControlNetと組み合わせて使用するために設計されており、AI画像の基盤を提供します。
* 典型的なユースケースは、DanceXRのアクターの構成とポーズを設定し、Stable Diffusionを使用して異なるキャラクターや環境で詳細な画像を生成することです。
* ControlNetの任意の画像からデプスとノーマルマップを生成することはできますが、レンダリングされたデプスとノーマルマップの方が生成されたものよりもはるかに正確です。自分でテストしてみてください。
* ControlNetでレンダリングされたデプスとノーマルマップを使用する場合は、プリプロセッサとして「なし」を選択するようにしてください。これらはさらなる処理を必要としません。