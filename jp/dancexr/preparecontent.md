---
locale: ja-JP
layout: single
title: コンテンツライブラリ
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)

## コンテンツライブラリ

コンテンツライブラリは、DanceXRがコンテンツを検索し、ユーザーが作成した設定を保存するフォルダです。

DanceXRは、コンテンツライブラリ内にある異なるサブフォルダにさまざまなタイプのコンテンツを検索します。

* actors: キャラクターモデル
* motion: モーションとオーディオファイル
* stages: ステージ用の3Dモデル
* accessory: アクターのボディパーツに取り付けられる3Dモデル
* props: ステージ小道具に使用できる3Dモデル。家具など
* texture
  * cookie: ライトマスク用のテクスチャ
  * drawing: ボディペイント機能のための保存された画像
  * ground: 地面のテクスチャ
  * mask: モデルに適用できる詳細マップと法線マップ
  * particle: [パーティクルエフェクト](features/particles.md)用のテクスチャ
  * sky: [パノラマスカイマップ](features/skymap.md)、HDR形式を推奨
* settings: すべての保存された設定。これらのファイルはユーザーによって変更されることはありませんが、バックアップを取っておくことができます。
* scenes: 保存されたシーンファイル
* bundles: 必要なすべてのアセットが含まれた保存されたシーンを含むzipパッケージ
* export: 3Dスナップショット機能を使用すると、ここでエクスポートされたモデルファイルを見つけることができます。
* presets: 保存されたプリセットファイル。DanceXRの同じバージョンを使用している限り、これらのファイルを友達と共有することができます。
* videos: プロジェクションやダイナミックテクスチャマップに使用できるビデオ。MP4形式のみをサポート
* chat: [AIチャットシステム](ai_chat.md)に使用されるファイル
  * characters: キャラクターサムネイルとテンプレート。これらは自動的に生成されますが、変更することができます。
  * tempplates: プロンプトテンプレート、変更して新しいものを作成できます。
  * history: 保存されたチャット履歴
  * persona: キャラクターに適用できるパーソナリティの説明
  * voices/piper/: TTSシステム用のカスタムボイスモデル

## サポートされている形式

* 3Dモデル: PMX、XPS、OBJ（ステージ小道具用）
* オーディオ: OGG、MP3（モバイルプラットフォームのみ）
* ビデオ: MP4
* モーション: VMD、BVH
* テクスチャ: PNG、JPG、HDR（スカイマップ用）

## グルーピングと組織

特に複数のファイルが連携して動作するコンテンツの管理を容易にするために、zipパッケージを使用してファイルを整理することをサポートしています。また、必要なすべてのファイルをサブフォルダに保管し、同じように機能させることもできます。

#### 3Dモデル

3Dモデルには通常、メッシュを記述する1つのファイルと複数のテクスチャファイルが付属しています。ファイルを移動したり抽出したりする際に、テクスチャとメッシュファイルの相対関係が変わらないようにしてください。それはプログラムが正しいテクスチャを見つけるために重要です。

PMXの場合、メッシュファイルは.pmxファイルであり、XPSの場合、メッシュファイルは.xps、.mesh、または.mesh.asciiファイルです。

1つのモデルのすべてのファイルをzipパッケージに保管することをお勧めします。ファイルサイズが小さく、管理が容易になります。

一部のモデルには[代替テクスチャ](features/alternative_textures.md)があります。DanceXRは、フォルダやzipパッケージを検索して、モデルで使用されているテクスチャファイルに類似したテクスチャファイルを自動的にメニューに追加します。これを機能させるには、代替テクスチャがメインテクスチャと同じファイル名であることを確認する必要があります。たとえば、ベースマップがbase.pngという名前の場合、DanceXRが別のサブフォルダでbase.pngを見つけると、それを自動的に代替テクスチャとして追加します。モデルがzipパッケージにある場合、DanceXRは代替テクスチャを検索するためにzipパッケージ全体を検索します。モデルがサブフォルダにある場合、DanceXRはメッシュファイルがある場所からすべてのサブフォルダを検索します。メッシュファイルフォルダの外に代替テクスチャを配置した場合、認識されないため、これを考慮してください。

![actorsフォルダの例](/images/content_actors.PNG)

#### モーションファイル

通常、モーションデータにはオーディオファイル、キャラクターモーション、カメラモーションが含まれます。DanceXRでは、オーディオ、キャラクターモーション、カメラモーションのバンドルを「ダンスセット」と呼びます。

DanceXRがダンスセットを検出できるようにするには、これらのファイルをすべてサブフォルダまたはzipパッケージ内に保管するだけです。ただし、1つのオーディオファイルのみが含まれていることを確認してください。

モーション/オーディオのペアのみを持つシンプルなコンテンツの場合、1つのフォルダに複数のこれらを持つことができますが、オーディオファイルとモーションファイルが同じ名前であることを確認する必要があります。たとえば、「dance.vmd」と「dance.ogg」のようにです。これにより、DanceXRはそれらがペアであることを認識し、それに対してダンスセットを作成します。

また、同じフォルダに複数の関連のないモーションまたはオーディオファイルを持つこともできます。それらは単独のモーションまたはオーディオファイルとして認識されますが、他のファイルとの関係はありません。

![motionフォルダの例](/images/content_motion.PNG)

## コンテンツライブラリツール

コンテンツライブラリのファイルを変更した後、DanceXRは起動時に変更を自動的に検出してコンテンツを再スキャンするはずです。

ただし、それが起こらない場合やファイルを移動した場合は、システムメニューのコンテンツライブラリツールを使用して手動でリフレッシュすることができます。

また、[ライブラリの変更](features/googledrive.md)オプションを使用して、別の場所を指定することもできます。

## Googleドライブ統合
DanceXRは[Googleドライブからファイルをダウンロード](features/googledrive.md)することができます。ドライブフォルダが制限なく共有されている限りです。共有フォルダのURLを入力するだけで、DanceXRはドライブフォルダをスキャンし、ローカルに存在しないファイルをダウンロードすることができます。

## AndroidおよびOculus Quest向けのコンテンツの準備

Androidシステムには厳格なファイルアクセスルールがあります。通常、アプリはストレージ内のフォルダにアクセスできません。そのため、AndroidおよびQuestバージョンでは、デフォルトでアプリストレージ内にコンテンツライブラリがあり、PCを使用してファイルをコピーする必要があります。

最新バージョンでは、ファイルの管理を少し簡単にするために、ストレージの許可を要求しています。そのためには、DanceXRにストレージへのアクセス許可を与える必要があり、その後、システムファイルアプリを使用してファイルを移動およびコピーできるようになります。

古いバージョンまたはアプリ内ストレージスペースを使用する場合、コンテンツライブラリはここにあります: /Android/data/com.vrstormlab.dancexr/files/.

## デモ動画

PC版:
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

Androidのコンテンツマネージャの使用
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

Questでのコンテンツの読み込み
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}