---
layout: studio-home
title: サポート
toc: false
locale: ja-JP
lang_path: /dancexr/support
hero_compact: true
hero_title: サポート
hero_image: /images/hero.png
support_sections:
  - id: known-issues
    light: true
    label: 既知の問題
    title: 既知の問題と回避策
    subsections:
      - title: 🌐 全バージョン共通
        items:
          - question: モデルを読み込んでも全部が白い
            answer: |
              最も一般的な原因はファイル名のエンコーディングです。ファイル名が異なる文字エンコーディングを使用している場合、テクスチャを見つけることができません。
              
              - ZIPパッケージの場合、エンコーディングをパッケージ名に追加して、DanceXRがファイル名を解析する方法を理解できるようにします。[詳細はこちら →](features/zip_format)
              - ファイル名内の余分なスペースもテクスチャの読み込みを妨げることがあります。PMXEditorでモデルを開き、テクスチャ参照が実際のファイル名と完全に一致しているか確認してください。
          - question: 髪のマテリアルが透けて見える
            answer: |
              透明度の深度プリパスがデフォルトでオンになっています。これは、最上層の透明レイヤーのみをレンダリングすることで透明度のソートを修正します。つまり、積み重ねられた透明レイヤー（層状の髪など）は最上層のみが表示されます。
              
              - すべての透明レイヤーをレンダリングするために、透明度の深度プリパスをオフにします。モデルのマテリアルの順序が正しくない場合、ソートのアーティファクトが発生する可能性があります。
              - 完璧な万能の解決策はありません。異なる設定を試して、視覚的な問題が少ないものを使用してください。
          - question: ステージモデルのスカイスフィアに穴が開いている、またはピクセル化して見える
            answer: |
              これも透明度の深度プリパスが原因です。複数のスカイスフィアが透明な場合、一部の領域では最上層のみが完全にレンダリングされます。
              
              - 透明度の深度プリパスをオフにする、または
              - 背景のスカイスフィアを見つけ、そのマテリアルを透明から不透明に変更する。
      - title: 📌 バージョン 2026.6
        items:
          - question: Tポーズまたはカスタムリグの使用時にモーションが壊れる
            answer: |
              これはモーションスムージングシステムのバグが原因です。一時的な回避策として、モーション設定でモーションスムージングを無効にしてください。
      - title: 📌 バージョン 2025.12
        items:
          - question: プレースホルダーの問題
            answer: |
              *これはバージョン固有の既知の問題のためのプレースホルダーです。後で内容を追加します。*
  - id: faq
    label: よくある質問
    title: よくある質問（FAQ）
    subsections:
      - title: 🛠️ 報告前のチェックリスト
        items:
          - question: バグを報告する前に、以下の簡単な修正をお試しください：
            answer: |
              1. **最新バージョンに更新** — 問題が新しいリリースですでに解決されている可能性があります。
              2. **設定のリセット** — 破損した設定ファイルを排除するために、バックアップを取ってから `config.json` を削除します。
              3. **ライセンスのリセット** — アプリの起動に失敗したり動作がおかしい場合は、インストールディレクトリから `license.txt` を削除して再起動してみてください。
              4. **ライブラリキャッシュのクリア** — コンテンツライブラリフォルダから `cache.json` をバックアップして削除し、プレイヤーにファイルの再スキャンを強制します。
              5. **OpenXRセットアップ** — VRが起動しない場合は、VRソフトウェアの設定でアクティブなOpenXRランタイムが正しく設定されているか再確認してください。
          - question: ログファイルはどこにありますか？
            answer: |
              バグを報告する際、ログファイルを添付すると非常に役立ちます。バグ報告には、**`Player.log`**（現在のセッション）と**`Player-prev.log`**（以前のセッション）を添付してください。
              
              **Windows PCのパス:**
              ```
              C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
              ```
              *注: `[User]`をWindowsのユーザー名に置き換えてください。AppDataが隠しフォルダになっている場合は、エクスプローラーで「隠しファイル」を表示する設定にしてください。*
              
              **Android & Meta Questのパス:**
              ```
              /Android/data/com.vrstormlab.dancexr/files/Player.log
              ```
              *注: デバイスをUSBでPCに接続し、ファイル転送モードを使用してこのファイルを見つけてください。*
      - title: "🖥️ システム & VRの起動"
        items:
          - question: 空だけが表示され、UIやカメラ操作ができない
            answer: |
              これは通常、起動時に何らかの問題が発生していることを意味します。以下の手順を順番にお試しください：
              
              - `license.txt`を削除して再起動する。
              - `config.json`を削除する（先にバックアップすること）—これによりすべての設定がリセットされ、破損した設定ファイルが原因の問題が解決します。
              - コンテンツライブラリから`cache.json`を削除する（先にバックアップすること）。
          - question: 起動するたびにクラッシュする—古いバージョンに戻しても改善しない
            answer: |
              これは通常、DanceXR自体ではなく、VRランタイムの問題です。
              
              - 複数のVRランタイムがある場合は、別のものに切り替えてみる。
              - SteamVRの場合：不要な起動オーバーレイやアドオンを無効にし、クリーン再インストールを試してください。
              - SteamVRの`driver`フォルダー内で、削除できる最近インストールまたは更新されたものがないか確認する。
          - question: VRが起動できない
            answer: |
              DanceXRはOpenXRを使用してVRを初期化します。複数のVRランタイムがインストールされている場合は、いずれか一つをアクティブなOpenXRランタイムとして設定する必要があります：
              
              - **Oculus / Meta：** Oculusアプリを開く → 設定 → ベータ → OpenXRランタイム → 「Oculusをアクティブに設定」
              - **SteamVR：** SteamVRを開く → 左上メニュー → 設定 → 開発者 → 「SteamVRをOpenXRランタイムに設定」
              - **Windows Mixed Reality：** Microsoftストアから「Windows Mixed Reality OpenXR Developer Tools」をダウンロードし、そこからWMRをアクティブに設定する
      - title: "📦 モデル & コンテンツライブラリ"
        items:
          - question: AndroidまたはMeta Questでコンテンツライブラリを設定するにはどうすればよいですか？
            answer: |
              Androidシステムには厳格なファイルアクセス制限があります。デフォルトでは、コンテンツライブラリはアプリの内部ストレージ内に配置されます。
              
              - デバイスをUSB経由でPCに接続し、「ファイル転送」を選択し、`/Android/data/com.vrstormlab.dancexr/files/`またはルートの`/DanceXR/`フォルダに移動して、zipや画像ファイルをコピーします。
              - AndroidおよびMeta Quest（バージョン2024.3以降）では、DanceXRにストレージ権限を付与して、システムファイルアプリまたは組み込みのコンテンツマネージャーアプリを使用してライブラリを共有・管理します。
              - 詳細については、[Android & Quest用コンテンツライブラリ](content_android_quest)ガイドを参照してください。
      - title: "🔑 ライセンス & 支払い"
        items:
          - question: 再度アクティベートを求められる
            answer: |
              大規模なOSまたはハードウェアの変更後、DanceXRはシステムをライセンス発行時と同じものとして認識しない場合があります。アクティベーション手順を再度実行するだけで解決します。追加の費用はかかりません。[アクティベーションとライセンス](activation)ガイドを参照してください。問題がある場合は[お問い合わせ](#contact)ください。
---


<div class="support-search-container">
  <input type="text" id="supportSearch" class="support-search-input" placeholder="Search issues, keywords, or error codes...">
</div>
<script src="/assets/js/support-search.js"></script>

{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item{% if section.id == 'known-issues' %} known-issue{% endif %}" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
サポートハブ

## どのようなご用件でしょうか？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">ドキュメントを参照</h3>
    <p class="support-desc">機能とオプションのガイド</p>
    <a href="features" class="support-cta">ドキュメントを開く</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">トラブルシューティング</h3>
    <p class="support-desc">報告前のチェックリスト</p>
    <a href="#troubleshooting" class="support-cta">チェックリストを表示</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">アクティベーション</h3>
    <p class="support-desc">ライセンスキーの管理</p>
    <a href="activation" class="support-cta">アクティベーションガイド</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
お問い合わせ

## バグ報告またはお問い合わせ

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">バグ追跡・機能リクエスト</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">Issueを開く</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">コミュニティサポート</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">Discordに参加</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">メール</h3>
    <p class="support-desc">ビジネス・直接のお問い合わせ</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">メールを送る</a>
  </div>

</div>

</section>