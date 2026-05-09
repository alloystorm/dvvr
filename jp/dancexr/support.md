---
layout: home
title: サポート
toc: false
locale: ja-JP
lang_path: /dancexr/support
hero_compact: true
hero_title: サポート
hero_image: /images/hero.png
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
ドキュメント

## ドキュメントを参照する

答えを見つける最も早い方法はドキュメントです。機能ページでは各オプションが詳細に説明されており、トラブルシューティングガイドでは最も一般的な問題を取り上げています。

[機能ドキュメント →](features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
コミュニティ

## Discordに参加する

DanceXRコミュニティはDiscordで活発です。他のユーザーを見つけ、作品を共有し、同じ問題に遭遇した可能性のある人から迅速な回答を得ましょう。

[Discordに参加 →](https://discord.gg/xN2MaM7C5q){: .btn-ghost}

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section section-light">
<div class="editions-header" markdown="1">

{:.section-label}
よくある質問

## よくある質問（FAQ）

</div>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 空だけが表示され、UIやカメラ操作ができない

これは通常、起動時に何らかの問題が発生していることを意味します。以下の手順を順番にお試しください：

- `license.txt`を削除して再起動する
- `config.json`を削除する（先にバックアップすること）—これによりすべての設定がリセットされ、破損した設定ファイルが原因の問題が解決します
- コンテンツライブラリから`cache.json`を削除する（先にバックアップすること）

</div>

<div class="faq-item" markdown="1">

### 起動するたびにクラッシュする—古いバージョンに戻しても改善しない

これは通常、DanceXR自体ではなく、VRランタイムの問題です。

- 複数のVRランタイムがある場合は、別のものに切り替えてみる
- SteamVRの場合：不要な起動オーバーレイやアドオンを無効にし、クリーン再インストールを試してください
- SteamVRの`driver`フォルダー内で、削除できる最近インストールまたは更新されたものがないか確認する

</div>

<div class="faq-item" markdown="1">

### 再度アクティベートを求められる

大規模なOSまたはハードウェアの変更後、DanceXRはシステムをライセンス発行時と同じものとして認識しない場合があります。アクティベーション手順を再度実行するだけで解決します。追加の費用はかかりません。[アクティベーションとライセンス](activation)ガイドを参照してください。問題がある場合は[お問い合わせ](#contact)ください。

</div>

<div class="faq-item" markdown="1">

### VRが起動できない

DanceXRはOpenXRを使用してVRを初期化します。複数のVRランタイムがインストールされている場合は、いずれか一つをアクティブなOpenXRランタイムとして設定する必要があります：

- **Oculus / Meta：** Oculusアプリを開く → 設定 → ベータ → OpenXRランタイム → 「Oculusをアクティブに設定」
- **SteamVR：** SteamVRを開く → 左上メニュー → 設定 → 開発者 → 「SteamVRをOpenXRランタイムに設定」
- **Windows Mixed Reality：** Microsoftストアから「Windows Mixed Reality OpenXR Developer Tools」をダウンロードし、そこからWMRをアクティブに設定する

</div>

<div class="faq-item" markdown="1">

### モデルを読み込んでも全部が白い

最も一般的な原因はファイル名のエンコーディングです。ファイル名が異なる文字エンコーディングを使用している場合、テクスチャを見つけることができません。

- ZIPパッケージの場合、エンコーディングをパッケージ名に追加して、DanceXRがファイル名を解析する方法を理解できるようにします。[詳細はこちら →](features/zip_format)
- ファイル名内の余分なスペースもテクスチャの読み込みを妨げることがあります。PMXEditorでモデルを開き、テクスチャ参照が実際のファイル名と完全に一致しているか確認してください。

</div>

<div class="faq-item" markdown="1">

### 髪のマテリアルが透けて見える

透明度の深度プリパスがデフォルトでオンになっています。これは、最上層の透明レイヤーのみをレンダリングすることで、透明度のソートを修正します—つまり、積み重ねられた透明レイヤー（層状の髪など）は最上層のみが表示されるということです。

- すべての透明レイヤーをレンダリングするために、透明度の深度プリパスをオフにする。モデルのマテリアルの順序が正しくない場合、ソートのアーティファクトが発生する可能性があります。
- 完璧な万能な解決策はありません—異なる設定を試して、視覚的な問題が少ないものを使用してください。

</div>

<div class="faq-item" markdown="1">

### ステージモデルのスカイスフィアに穴が開いている、またはピクセル化して見える

これも透明度の深度プリパスが原因です—複数のスカイスフィアが透明な場合、一部の領域では最上層のみが完全にレンダリングされます。

- 透明度の深度プリパスをオフにする、または
- 背景のスカイスフィアを見つけ、そのマテリアルを透明から不透明に変更する

</div>

</div>
</section>

<!-- ── Troubleshooting ───────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
トラブルシューティング

## ログファイルの場所

バグを報告する際、ログファイルを添付すると非常に役立ちます。ログファイルにはエラーの発生時の記録が含まれており、問題を素早く診断できます。

**ログファイルの場所（PC）：**

```
C:\Users\[your user name]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最後のフォルダー名は、お使いのバージョンによって異なります—`DanceXR HD`、`DanceXR LW`、または`DanceXR RT`の場合があります。

一部のフォルダーは初期設定で隠されています。`AppData`が見つからない場合は、まず[エクスプローラーで隠しファイルを表示する](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)を有効にしてください。

フォルダーを開いたら、レポートに**`Player.log`**（現在のセッション）と**`Player-prev.log`**（前のセッション）を添付してください。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
クイックフィックス

## 報告する前に

まずこれらの手順を実行してください—ほとんどの問題がこれで解決します：

1. **最新バージョンに更新する** — すでに問題が修正されている可能性があります
2. **設定をリセットする** — 破損した設定ファイルを排除するため、`config.json`をバックアップしてから削除する
3. **ログを確認する** — `Player.log`を開き、`ERROR`または`Exception`を検索して問題を特定する
4. **VRが起動しない** — OpenXRランタイムが正しく設定されているか確認する（上記のFAQを参照）
5. **白いテクスチャ** — テクスチャ参照のファイル名のエンコーディングと余分なスペースを確認する

これらで解決しない場合は、報告する価値があります。

</div>
</div>
</section>

<!-- ── Bug Report & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
お問い合わせ

## バグ報告またはお問い合わせ

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">推奨</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">バグ追跡・機能リクエスト</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>完全な問題の履歴とステータス</li>
      <li>スクリーンショットとログファイルを添付可能</li>
      <li>報告の進行状況を追跡</li>
      <li>新機能のリクエスト</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">Issueを開く</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">すばやい</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">コミュニティサポート</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>コミュニティからの迅速な回答</li>
      <li>作品やアイデアを共有</li>
      <li>開発者も参加中</li>
      <li>リアルタイムのディスカッション</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">Discordに参加</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">直接</p>
    <p class="edition-name">メール</p>
    <p class="edition-price">ビジネス・直接のお問い合わせ</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>添付ファイル付きのバグ報告</li>
      <li>ビジネスに関するお問い合わせ</li>
      <li>アクティベーションの問題</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">メールを送る</a>
  </div>

</div>
</section>