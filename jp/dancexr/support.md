---
layout: home
title: サポート — DanceXR
toc: false
locale: ja-JP
lang_path: /dancexr/support
permalink: /jp/dancexr/support
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

最も早く答えを見つける方法はドキュメントです。機能ページでは各オプションが詳しく説明されており、トラブルシューティングガイドでは最も一般的な問題を取り上げています。

[機能ドキュメント →](/jp/dancexr/features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
コミュニティ

## Discordに参加する

DanceXRコミュニティはDiscordで活発です。他のユーザーを見つけ、作品を共有し、同じ問題を経験した人からすばやく回答を得ましょう。

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

### 空だけ表示されてUIやカメラ操作ができない

起動時に何らかの問題が発生していることが多いです。以下の順番でお試しください：

- `license.txt` を削除して再起動する
- `config.json` をバックアップして削除する — 設定がリセットされ、破損した設定ファイルが原因の問題が解決します
- コンテンツライブラリから `cache.json` をバックアップして削除する

</div>

<div class="faq-item" markdown="1">

### 毎回クラッシュする — 古いバージョンに戻しても改善しない

これは通常DanceXR自体の問題ではなく、VRランタイムの問題です。

- 複数のVRランタイムがある場合は別のものに切り替えてみる
- SteamVRの場合：不要なスタートアップオーバーレイやアドオンを無効にする。クリーンインストールも試してください
- SteamVRの `driver` フォルダーに最近インストールまたは更新されたものがないか確認する

</div>

<div class="faq-item" markdown="1">

### 再アクティベーションを求められる

OSのアップデート、ハードウェアのアップグレード、その他のシステム変更後にデバイスIDが変わることがあります。アクティベーション手順をもう一度実行するだけで解決します。問題がある場合は[お問い合わせ](#contact)ください。

</div>

<div class="faq-item" markdown="1">

### VRが起動できない

DanceXRはOpenXRを使用してVRを初期化します。複数のVRランタイムがインストールされている場合は、いずれかをアクティブなOpenXRランタイムとして設定する必要があります：

- **Oculus / Meta：** OculusアプリをOpen → 設定 → ベータ → OpenXRランタイム → 「Oculusをアクティブに設定」
- **SteamVR：** SteamVRを開く → 左上メニュー → 設定 → 開発者 → 「SteamVRをOpenXRランタイムに設定」
- **Windows Mixed Reality：** MicrosoftストアでWMR OpenXRデベロッパーツールをインストールし、WMRをアクティブに設定する

</div>

<div class="faq-item" markdown="1">

### モデルを読み込んでも全部白い

最も一般的な原因はファイル名のエンコーディングです。異なる文字エンコーディングを使用しているとテクスチャが見つからない場合があります。

- ZIPパッケージの場合は、パッケージ名にエンコーディング情報を追加することでDanceXRが正しく解析できます。[詳細はこちら →](/dancexr/features/zip_format)
- ファイル名の余分なスペースもテクスチャの読み込みを妨げます。PMXEditorでモデルを開いてテクスチャ参照が実際のファイル名と一致しているか確認してください

</div>

<div class="faq-item" markdown="1">

### 髪のマテリアルが透けて見える

デフォルトで透明度の深度プリパスがオンになっています。これにより最上位の透明レイヤーのみがレンダリングされ、重なった透明レイヤー（髪など）が透けて見えることがあります。

- 透明度の深度プリパスをオフにすることで全ての透明レイヤーをレンダリングできますが、マテリアルの順序が正しくない場合に表示の乱れが生じる可能性があります
- 完璧な解決策はありません — 異なる設定を試してより問題の少ないものを使用してください

</div>

<div class="faq-item" markdown="1">

### ステージモデルのスカイスフィアに穴があったりピクセル化して見える

これも透明度の深度プリパスが原因です。複数のスカイスフィアが透明な場合、一部の領域では最上位のレイヤーのみが完全にレンダリングされます。

- 透明度の深度プリパスをオフにする、または
- 背景のスカイスフィアを見つけてマテリアルを透明から不透明に変更する

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

バグを報告する際にログファイルを添付すると非常に役立ちます。ログファイルにはエラーの発生時の記録が含まれており、問題を素早く診断できます。

**ログファイルの場所（PC）：**

```
C:\Users\[ユーザー名]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最後のフォルダー名はバージョンによって異なります — `DanceXR HD`、`DanceXR LW`、または `DanceXR RT` の場合があります。

`AppData` フォルダーが見つからない場合は、まず [エクスプローラーで隠しファイルを表示する設定](https://support.microsoft.com/ja-jp/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2) にしてください。

フォルダーを開いたら **`Player.log`**（現在のセッション）と **`Player-prev.log`**（前のセッション）を報告に添付してください。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
クイックフィックス

## 報告する前に

まず以下の手順を試してください — 多くの問題はこれで解決します：

1. **最新バージョンに更新する** — 問題がすでに修正されている可能性があります
2. **設定をリセットする** — `config.json` をバックアップして削除し、設定ファイルの破損を除外する
3. **ログを確認する** — `Player.log` を開いて `ERROR` または `Exception` を検索して問題を特定する
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
      <li>スクリーンショットとログを添付可能</li>
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
      <li>コミュニティからのすばやい回答</li>
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
