---
layout: release
title: シーンバンドル
locale: ja-JP
toc: true
---

# シーンバンドル

<!-- TODO: confirm exact UI flow and bundle format. Drafted from release notes (2024.1, 2024.9). -->

シーンバンドルとは、[保存されたシーン]に、それが参照する実際のモデル、モーション、および音楽ファイルが含まれたものです。これらがすべてパッケージ化されているため、受信者はすべてのアセットを個別に探すことなく、シーン全体をロードできます。

**2024.1**で（実験的に）追加されました。

---

## 保存されたシーン vs シーンバンドル

- **保存されたシーン**は、アセットを名前で*参照*する小さなファイルです。これをロードすると、DanceXRは、参照された各アセットを受信者のコンテンツライブラリから検索します。受信者がモデルまたはモーションのいずれかを欠いている場合、その部分のシーンはロードに失敗します。
- **シーンバンドル**は、保存されたシーンを、それに依存するすべてのアセットで**ラップ**したものです。受信者はバンドルを直接ロードできます。欠品アセットの問題は起こりません。

シーンを共有する場合はシーンバンドルを、すでにすべてのアセットを持っている自分の使用目的の場合は保存されたシーンを使用してください。

---

## バンドルの作成

<!-- TODO: confirm UI path. -->

1. 望むようにシーンをセットアップします。
2. シーンメニューを開き、**シーンバンドルとして保存**を選択します。
3. DanceXRは、参照されたすべてのアセット（モデル、モーション、音楽）を収集し、単一のバンドルファイルにパッケージ化します。

このバンドルには、受信者が同じモデルパックをあちこち探さなくても、別のマシン、別の国でシーンをロードするために必要なものがすべて含まれています。

---

## バンドルのロード

バンドルファイルを他のコンテンツライブラリアイテムと同様に扱ってください。ライブラリにドロップするか、シーンメニュー経由で開くだけです。

ロード時、DanceXRはアセットを一時的な場所またはバンドルごとの場所に抽出してから、そこからシーンをロードします。アセットは、デフォルトでは受信者のメインライブラリにマージされません <!-- TODO: confirm exact behavior here — extracted to a subfolder vs. merged. -->

---

## 制限事項

<!-- TODO: confirm. Likely:
- Bundle size scales with the assets included; large stage models can produce very large bundles.
- Tier-locked features still require the recipient to have that tier.
- Personal / unauthorized model redistribution — the bundle does not strip licensing constraints. -->

2024.1で実験的とされています。現在の状態についてはリリースノートを参照してください。

---

## 関連ページ

- [保存されたシーン](save_scene)
- [コンテンツライブラリ](../preparecontent)
- [アクタープリセット](actor_presets)
- [システムプリセット](system_presets)