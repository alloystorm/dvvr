---
layout: release
title: リモートコントロール
locale: ja-JP
toc: true
---

# リモートコントロール

<!-- TODO: confirm everything below against current behavior. Drafted from the 2024.12 release notes (initial public beta) — feature has likely evolved since. -->

リモートコントロールを使用すると、**Androidアプリ**を、同じローカルネットワーク上の**別のデバイスで実行されているDanceXRのワイヤレスコントローラー**として機能させることができます。メインのDanceXRセッションがPC、ヘッドセット、またはリビングルームのスクリーンで実行されている間に、スマートフォンやタブレットからシーン、モーション、および設定を変更できます。

**2024.12**にパブリックベータとしてリリースされました。

---

## 使用するタイミング

- キーボードに向かうことなく、録画中に設定を調整する場合。
- スマートフォンからカウチ／大画面でのDanceXRセッションを操作する場合。
- VR内メニューをいじるのではなく、AndroidスマートフォンからQuestスタンドアローンセッションを操作する場合。

---

## 要件

<!-- TODO: confirm minimum Android version, whether Quest standalone (Mix / Immersion) is supported as the *controller*, whether iOS is supported. -->

- DanceXR AndroidアプリがインストールされたAndroidデバイス。
- 同じLANで到達可能なPC、Quest、またはその他のDanceXRインスタンス。
- 両方のデバイスが同じネットワークセグメントにあること（クライアント分離がないこと）。

---

## 接続方法

<!-- TODO: walk through the actual UI. Drafted from release notes only. -->

1. ホストデバイス（PC、Questなど）でDanceXRを起動します。
2. Androidアプリを開き、メインメニューから**リモートコントロール**を選択します。
3. アプリがローカルネットワーク上のDanceXRインスタンスを検出します。ホストを選択します。
4. AndroidのUIは、トウチパッドとメニューサーフェスに置き換わり、ホストのUIをミラー表示します。

---

## リモートで可能な操作

- ほぼすべてのメニューとオプションにアクセスできます。
- トウチパッドを使用してカメラの回転やアクターの移動ができます。
- モーション、シーン、ステージを切り替えることができます。

<!-- TODO: confirm which menus or actions are *not* available remotely. -->

---

## ネットワークプロトコル

<!-- TODO: confirm. Release notes mention a custom protocol for low-latency, but no further public spec. -->

リモートコントロールは、ローカルネットワーク上でHTTPではなく独自のDanceXRプロトコルを使用します。これはLANでの低遅延に調整されており、インターネットを介したルーティングのために設計されたものではありません。

---

## トラブルシューティング

<!-- TODO: fill in real cases users hit (firewall blocking discovery, mismatched versions, Wi-Fi vs Ethernet). -->

- **リストにホストが表示されない場合:** 両方のデバイスが同じネットワークにあり、ファイアウォールがDanceXRの検出ポートをブロックしていないことを確認してください。
- **入力が遅い、またはカクつく場合:** 5GHz Wi-Fiまたは有線ホストの使用を推奨します。クライアント分離のあるゲストネットワークは避けてください。
- **バージョン不一致:** ホストとAndroidコントローラーは同じDanceXRバージョンで実行する必要があります。

---

## 関連ページ

- [Application Settings](application_settings)
- [Controls & UI](../controls)
- [VR Operations](../vr_operations) — ホストでVRセッションを実行する場合