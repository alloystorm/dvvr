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
XPSモデルには物理定義が付属していないため、プログラムはどこに物理コンポーネントを追加すべきかわかりません。これに対処するために、各XPSモデルにいくつかの物理設定が追加され、XPSモデル上で物理コンポーネントを構成できるようになります。

これには以下が含まれます
* [ボディコライダー](xps_body_colliders.md)
* [おっぱいの物理](xps_boobs.md)
* [髪の物理](xps_hair.md)
* [服の物理](xps_cloth.md)
* [スカートの物理](xps_skirt.md)
* [ソフトボディの物理](xps_softbody.md)
* [オブジェクトの検出](xps_detech.md)


### デモ
{% include video id="-IZTzHUpROs" provider="youtube" %}

XPS物理ツールを使用するには、ほとんどの場合、適切なボーンを見つけて選択するだけで、プログラムが残りを処理します。

ポニーテールやリボンなどのものは、上記のビデオで示されているように非常に簡単です。

時々、子ボーンが多すぎて、実際に必要なボーンがそれらの子ボーンの数レベル下に埋もれていることがあります。この場合、親ボーンを選択してから、「最初のXボーンをスキップ」設定を使用して選択を微調整できます。

プロセス中に問題が発生した場合は、慌てないでください。選択を完了してから、設定で状況を安定させることができます。
* まず、「相互リンク距離」を0に減らして相互リンクジョイントを無効にし、次に
* コライダーサイズを少し増やしてみてください（やりすぎないでください）、
* それでもうまくいかない場合は、設定を無効にして再度有効にしてみてください、
* 最終的にはモデルを再読み込みし、不安定性を解消することができることがあります。