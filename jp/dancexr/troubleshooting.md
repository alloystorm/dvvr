---
layout: release
title: トラブルシューティング
locale: ja-JP
---

## バグの報告
問題を適切に管理するために、[GitHubの問題追跡システム](https://github.com/alloystorm/dvvr/issues)でバグを報告することをおすすめします。

また、直接vrstormlab@gmail.comにメールを送信することもできます。可能であれば、スクリーンショットや例のモデルを添付すると良いです。

コメントや他のプラットフォームでの直接メッセージにも目を通そうと努力しますが、すべてのメッセージがこれらのチャンネルを通じて処理されることを保証することはできません。


## ログファイルの場所（PCのみ）
エラーが発生した場合、通常はログファイルにそのエラーについて説明するログエントリがあります。したがって、問題を報告する際にログファイルを特定し、送信していただけると非常に助かります。

ログファイルは**C:\Users\\\[ユーザー名]\AppData\LocalLow\VR Storm Lab\DanceXR HD**で見つけることができます。最後のフォルダ名は実行しているバージョンによって異なるため、「DanceXR HD」、「DanceXR LW」または「DanceXR RT」のいずれかになる場合があります。

システムによっては、いくつかのフォルダがデフォルトで非表示になっている場合があるため、それらを見つける前に[エクスプローラーで非表示ファイルを表示するように設定](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)する必要があるかもしれません。

フォルダを開くと、ログファイル「**Player.log**」と「**Player-prev.log**」が表示されます。

---

## 最初に確認すべき場所

症状別の案内:

- **起動しない、または起動時にクラッシュする** → [FAQ → 空のみが表示される](faq#only-sky-is-displayed-no-ui-or-camera-control-available)、[FAQ → 突然クラッシュし始めた](faq)
- **VRが開始しない** → [FAQ → VRが起動できない](faq#unable-to-launch-vr)
- **アクティベーションの問題** → [FAQ → 再度アクティベートを求められる](faq#im-asked-to-activate-again)、次に[サポート](support)
- **モデル固有の問題（特定のモデルが予期せず動作しない）** → [アクターのトラブルシューティング](features/troubleshooting)
- **髪、布、スカート、または胸の物理演算** → [物理システム](physics)
- **マテリアルまたはテクスチャがおかしい** → [外観とマテリアル](appearance)、[FAQ → モデルはロードされるがすべてが白くなる](faq#model-loads-but-everything-is-white)
- **モーションが再生されない、またはアクターが間違っている** → [モーションシステム](motion)
- **用語の意味がわからない** → [コンセプトと用語集](concepts)

## 関連ページ

- [FAQ](faq)
- [サポート](support) — Discord, email, GitHub issues
- [コンセプトと用語集](concepts)