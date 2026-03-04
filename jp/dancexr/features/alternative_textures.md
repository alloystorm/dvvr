---
locale: ja-JP
layout: single
title: 代替テクスチャ
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/alternative_textures) | [繁中](/tw/dancexr/features/alternative_textures) | [日本語](/jp/dancexr/features/alternative_textures) | [한국어](/kr/dancexr/features/alternative_textures) | [简中](/zh/dancexr/features/alternative_textures)

## 概要
代替テクスチャは、モデルのデフォルトのテクスチャを置き換えることができるテクスチャのセットです。

### 動作原理
DanceXRは、モデルのパッケージやフォルダ内のテクスチャファイルをスキャンし、デフォルトのテクスチャと同じ名前のファイルを探します。見つかった場合、可能な代替テクスチャのリストを作成し、ユーザーが選択できるようにします。

ユーザーが代替テクスチャのうちの1つを選択すると、新しいテクスチャが読み込まれ、モデルによって使用されるデフォルトのテクスチャが置き換えられます。代替テクスチャを選択すると、テクスチャメニューも自動的に更新され、現在アクティブなテクスチャが反映されます。

### 位置
DanceXRがテクスチャファイルを正しく見つけるためには、テクスチャファイルを別々のフォルダに配置し、フォルダの場所が以下のルールに従う必要があります。

モデルがzipパッケージ内にある場合、代替テクスチャを検索するためにパッケージ全体がスキャンされます。

モデルがフォルダ内にある場合、メインのモデルファイルを含むフォルダのサブフォルダ内に、テクスチャファイルを別々のフォルダに配置する必要があります。