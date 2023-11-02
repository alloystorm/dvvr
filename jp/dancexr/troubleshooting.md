---
layout: single
title: トラブルシューティング
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/troubleshooting) | [繁中](/tw/dancexr/troubleshooting) | [日本](/jp/dancexr/troubleshooting) | [한국어](/kr/dancexr/troubleshooting) | [简中](/zh/dancexr/troubleshooting)


## バグの報告
問題を適切に管理するために、[GitHubの問題追跡システム](https://github.com/alloystorm/dvvr/issues)でバグを報告することをおすすめします。

また、直接vrstormlab@gmail.comにメールを送信することもできます。可能であれば、スクリーンショットや例のモデルを添付すると良いです。

コメントや他のプラットフォームでの直接メッセージにも目を通そうと努力しますが、すべてのメッセージがこれらのチャンネルを通じて処理されることを保証することはできません。


## ログファイルの場所（PCのみ）
エラーが発生した場合、通常はログファイルにそのエラーについて説明するログエントリがあります。したがって、問題を報告する際にログファイルを特定し、送信していただけると非常に助かります。

ログファイルは**C:\Users\\\[ユーザー名]\AppData\LocalLow\VR Storm Lab\DanceXR HD**にあります。最後のフォルダ名は実行しているバージョンによって異なるため、「DanceXR HD」、「DanceXR LW」または「DanceXR RT」のいずれかになる場合があります。

システムでは、いくつかのフォルダがデフォルトで非表示になっている場合があるため、それらを見つける前に[エクスプローラーで非表示ファイルを表示するように設定](https://support.microsoft.com/ja-jp/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)する必要があるかもしれません。

フォルダを開くと、ログファイルの「**Player.log**」と「**Player-prev.log**」が表示されます。