---
locale: ja-JP
layout: single
title: XPS Physics

XPS物理
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/xps_physics) | [繁中](/tw/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics) | [한국어](/kr/dancexr/features/xps_physics) | [简中](/zh/dancexr/features/xps_physics)

## XPSモデル固有の設定
XPSモデルには物理定義が付属していないため、プログラムはどこに物理コンポーネントを追加すべきかわかりません。このため、XPSモデルごとにいくつかの物理設定が追加され、XPSモデル上で物理コンポーネントを構成できるようになっています。

これには以下が含まれます：
* [ボディコライダー](xps_body_colliders.md)
* [おっぱいの物理](xps_boobs.md)
* [髪の物理](xps_hair.md)
* [服の物理](xps_cloth.md)
* [スカートの物理](xps_skirt.md)
* [ソフトボディの物理](xps_softbody.md)
* [オブジェクトの検出](xps_detect.md)

### デモ
{% include video id="-IZTzHUpROs" provider="youtube" %}

XPS物理ツールを使用する際、ほとんどの場合、適切なボーンを見つけて選択するだけで、プログラムが残りの作業を処理します。

ポニーテールやリボンなどのものは、上記のビデオで実証されているように非常に簡単です。

時々、子ボーンが多すぎて、必要なボーンが実際にはそれらの子ボーンの数レベル下に埋もれていることがあります。この場合、親ボーンを選択してから、「最初のX個のボーンをスキップ」設定を使用して選択を微調整できます。

プロセス中に問題が発生した場合は、慌てないでください。選択を完了した後、設定で状況を安定させることができます。
* まず、"inter-link dist"を0に減らしてインターリンクジョイントを無効にし、その後
* コライダーサイズを少し大きくすることを試してみてください（やりすぎないでください）。
* それでもうまくいかない場合は、設定を無効にして再度有効にすることができます。
* 最終的には、モデルを再読み込みすることもできます。これにより、不安定性が解消されることがあります。