---
layout: single
title: Google Driveの統合
toc: true
sidebar:
  nav: "docs-jp"
---
[English](/dancexr/features/googledrive) | [简体中文](/zh/dancexr/features/googledrive) | [日本語](/jp/dancexr/features/googledrive)


## Google Driveの統合
{% include video id="N7o0CdbFvD4" provider="youtube" %}
* プログラムは、Google Driveの共有フォルダからコンテンツをダウンロードすることができます。
* これにより、PCなしでGoogle Drive上のコンテンツを管理し、コンテンツを自動的にデバイスにダウンロードすることができます（特にQuestとAndroidに便利です）。
* ビデオには表示されていない機能として、URL短縮サービスを使用してURLを短縮し、Google Driveの完全なURLの代わりに入力することもできます。
* また、これを使用して友達とコンテンツを共有することもできます。
なお、これはまだ実験的な機能です。ユーザーエクスペリエンスを簡素化するために、認証を必要としない方法でGoogle DriveのAPIを使用していますが、その代わりにGoogle Driveフォルダを制限なく共有する必要があります（ビデオで示されています）。また、Googleは同じIPアドレスから一定期間内にダウンロードできる量に制限を設けています。突然ダウンロードできなくなった場合は、通常はダウンロード制限を超えていることを意味します。再度ダウンロードできるようになるまで数時間待つ必要があります。