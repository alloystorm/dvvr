---
layout: single
title: XPS物理学
toc: true
---

## XPSモデル固有の設定
XPSモデルには物理学の定義が付属していないため、プログラムはどこに物理学のコンポーネントを追加すべきかわかりません。そのため、XPSモデルごとにいくつかの物理学の設定が追加されており、XPSモデル上で物理学のコンポーネントを設定できるようになっています。

### ボーンコライダー
この設定は、一般的な体の部位にコライダーを作成し、他の物理オブジェクトとの相互作用を可能にします。スライダーを使用してサイズを変更し、モデルの体の形に合わせてください。

### おっぱいの物理学
デフォルトではオンになっていますが、設定から正しいおっぱいに関連するボーンを選択するまで何もしません。通常、これらのボーンはtorso2の子ボーンであり、それぞれの側に2つあります。

バネ、質量、ダンプ
: ジョイントの物理特性を制御します。

制限
: 親ボーンからどれだけ回転できるかを制御します。

逆重力
: 選択した角度でおっぱいを持ち上げ、重力による引っ張りを相殺します。

コライダーの半径
: コライダーのサイズを制御します。モデルに合った値に設定すると良いです。

アンカーとセンター
: ジョイントの位置を制御します。

### 髪の物理学
おっぱいの設定と同様に、動作させるためにボーンを選択する必要があります。通常、これらはheadの子ボーンです。正しいボーンを見つけるには少し探索が必要な場合もあります。物理コンポーネントを作成する方法は、選択したボーンから、すべての子ボーンとその子ボーンを接続し、最後まで到達するまでジョイントとコライダーのツリー構造を形成することです。

コライダーの半径
: コライダーは円柱形であり、コライダーの半径は直径を制御します。

最初のX個のボーンをスキップ
: これにより、プログラムが「ツリー」を作成する際に最初のX個のボーンをスキップするように指示することができます。ボーンが多すぎる場合に、個々のボーンを選択する必要がなくなります。

### クロス物理学
これは髪の物理学と似ていますが、"ツリー"の枝同士の水平な接続もあり、"メッシュ"を形成します。

### デモ
{% include video id="-IZTzHUpROs" provider="youtube" %}

XPS物理学ツールを使用するには、ほとんどの場合、適切なボーンを見つけて選択するだけで、プログラムが残りの作業を処理します。

ポニーテールやリボンなどのものは、上記のビデオで示されているように非常に簡単です。

子ボーンが多すぎて必要なボーンが実際にはその子ボーンの数レベル下に埋もれている場合、親ボーンを選択し、"最初のX個のボーンをスキップ"設定を使用して選択を微調整することができます。

プロセス中に何かがうまくいかなくなった場合は、パニックにならないでください。選択を完了した後、設定で物事を安定させることができます。
* まず、"inter-link dist"を0に減らして相互リンクジョイントを無効にし、
* コライダーのサイズを少し大きくしてみてください（やりすぎないでください）。
* それでもうまくいかない場合は、設定を無効にして再度有効にしてみてください。
* 最終的にはモデルを再読み込みすると、不安定性が解消されることがあります。