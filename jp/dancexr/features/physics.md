---
locale: ja-JP
layout: single
title: 物理
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/physics) | [繁中](/tw/dancexr/features/physics) | [日本語](/jp/dancexr/features/physics) | [한국어](/kr/dancexr/features/physics) | [简中](/zh/dancexr/features/physics)
## ## 物理の微調整

### システム全体の物理設定
システム全体の物理設定は、設定→オプション→物理の順に進んで設定することができます。

![システム物理](/images/system-physics.png)

有効化
: 物理シミュレーションのオン/オフを切り替えます。

重力
: 重力の力を変更します。負の値に設定すると重力の方向が反転します。

衝突無効化
: モデルのパーツ間の衝突を制御します。モデルには2種類のコライダーがあります。タイプAはアームやレッグなどのアニメーションとともに移動するもので、タイプBは通常、1つ以上のジョイントで他のパーツに接続されて自由に移動します。デフォルトでは、タイプBはタイプAと衝突しますが、「衝突無効化」をオンにすると、タイプBオブジェクトはもはやタイプAオブジェクトと衝突せず、貫通します。

1秒あたりのステップ数
: 物理シミュレーションはステップ間の一定の間隔で計算され、固定の間隔が最適です。このオプションは、1秒間に何回シミュレーションが実行されるかを制御します。多ければ多いほど良いですが、ステップが多すぎるとFPSが低下します。スムーズなアニメーションのためには、FPSに合わせるのが最適です。

### PMXモデル固有の設定
モデル固有の物理設定は、モデル設定→オプション→物理の順に進んで設定することができます。

![モデル物理](/images/model-physics.png)

硬さ
: すべてのジョイントのバネ力に適用される全体的な乗数です。値を増やすと動きが制限されます。さらに、以下の設定を使用して線形および角度の動きのバネ力を個別に制御することもできます。

線形動き
: すべてのジョイントの線形動きの制限方法を選択します。自動では、モデルで定義された線形制限に基づいて制限が設定されます。制限が非常に小さい場合はロックされ、それ以外の場合は制限されます。"バウンシネス"は、制限の端に当たったときにどれだけの速度が保持され、バウンスバックするかを制御します。"接触距離"は、制限に近づいたときに制限バネ力を適用するタイミングを決定します。0は、実際に制限に達するまで自由に移動し、1は、制限内にある場合に常に力が適用されることを意味します。

角度動き
: 上記の線形動きと同様に、すべてのジョイントの角度動きを制御します。

線形ドライブ
: 接続されたオブジェクトを元の位置に戻すために使用されるバネ力を制御します。ここでの「ターゲット」設定は、中立位置がどこにあるかを制御します。

角度ドライブ
: オブジェクトを元の向きに戻す力を制御します。

投影距離
: 投影距離。2つの接続されたオブジェクト間の距離がここで定義された値よりも大きい場合、オブジェクトは逃げ場所を避けるために移動します。

投影角度
: 上記と同様に、回転を制御します。

変更時にリセット
: このオプションを切り替えると、ここで変更が行われるたびに、すべてのボーンが新しい設定値が適用される前に初期位置にリセットされます。これにより、物理設定を変更する際にボーンがずれるのを防ぐことができます。ただし、変更の効果を観察するのが難しい場合もあります。その場合は、変更を行う前にこのオプションをオフにし、理想の設定を見つけた後に再度オンにすることができます。

移動とドライブの設定内には、いくつかの共通の設定値があります。

バネ力
: フックの法則に基づいて力を計算するために使用されます。

ダンプ/ドラッグ
: 現在の速度に対してどれだけの力が適用され、動きを停止させるかを制御します。

### XPSモデル固有の設定
XPSモデルには物理定義が含まれていないため、プログラムはどこに物理コンポーネントを追加するかわかりません。そのため、XPSモデルごとにいくつかの物理設定が追加され、XPSモデル上で物理コンポーネントを設定できるようになっています。

#### ボーンコライダー
この設定では、一般的なボディパーツにコライダーを作成し、他の物理オブジェクトとの相互作用を可能にします。スライダーを使用してサイズを変更し、モデルのボディビルドに合わせることができます。

#### おっぱいの物理
デフォルトでオンになっていますが、設定から正しいおっぱいに関連するボーンを選択するまで何もしません。通常、それらはtorso2の子ボーンであり、それぞれのサイドに1つずつあります。

バネ、質量、ダンプ
: ジョイントの物理特性を制御します。

制限
: 親ボーンからどれだけ回転できるかを制御します。

逆重力
: おっぱいを選択した度数だけ持ち上げ、重力による引っ張りを相殺します。

コライダー半径
: コライダーのサイズを制御します。モデルに合わせた値に設定することが良いです。

アンカーとセンター
: ジョイントの位置を制御します。

#### 髪の物理
おっぱいの設定と同様に、機能させるためにはボーンを選択する必要があります。通常、これらはheadの子ボーンです。適切なボーンを見つけるには少し探索が必要な場合もあります。物理コンポーネントを作成する方法は、選択したボーンから始まり、子ボーンとその子ボーンを接続して末端に到達するまで、ジョイントとコライダーのツリー構造を形成することです。

コライダー半径
: コライダーは円筒形状であり、コライダー半径は直径を制御します。

最初のX個のボーンをスキップ
: このオプションを使用すると、"ツリー"を作成する際に最初のX個のボーンをスキップするようにプログラムに指示することができます。ボーンが多すぎる場合に、個々のボーンを選択する必要がなくなります。

#### クロス物理
これは髪の物理と似ていますが、"ツリー"の枝同士に水平な接続もあり、"メッシュ"を形成します。