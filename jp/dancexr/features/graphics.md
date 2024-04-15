---
locale: ja-JP
layout: single
title: グラフィックス
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## グラフィック設定

### アンチエイリアシング

### スーパーサンプリング
DLSS、FSR

### 反射

### アンビエントオクルージョン

### グローバルイルミネーション

### デプスオブフィールド

### モーションブラー

### ブルーム

### レンズフレア

### カラー調整

### カラーフィルター

### ホワイトバランス

### 特殊レンダリングモード：デプスとノーマル
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 以前のカートゥーンシェーダーは、デプスとノーマルの2つのモードを含むように拡張されました。
* これらは、Stable Diffusion ControlNetと共に使用するように設計されており、AI画像の基盤を提供します。
* DanceXRの俳優の構図とポーズを設定し、その後Stable Diffusionを使用して、異なるキャラクターや環境を持つ詳細な画像を生成するのが一般的な使用例です。
* ControlNetの任意の画像からデプスとノーマルマップを生成できますが、レンダリングされたデプスとノーマルマップの方が生成されたものよりもはるかに正確です。自分でテストしてみてください。
* ControlNetでレンダリングされたデプスとノーマルマップを使用する場合は、プリプロセッサとして「なし」を選択してください。それ以上の処理は必要ありません。

### オプション