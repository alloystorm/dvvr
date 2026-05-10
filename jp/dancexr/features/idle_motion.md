---
layout: release
title: アイドルモーション
locale: ja-JP
toc: true
---

# アイドルモーション

<!-- TODO: confirm UI labels. Drafted from release notes (2025.12) and the procedural-motion family. -->

アイドルモーションは、アクターに他のモーションが割り当てられていないときに再生されるプロシージャルモーションです。呼吸、体重移動、そして頭や四肢の小さな動きをシミュレートすることで、アクターが静止しているように見えるのではなく、生き生きとしているように見せる役割を果たします。

---

## アイドルモーションが再生されるとき

- アクターにモーションが割り当てられる前。
- モーションが終了したとき（かつ、アクターがシークエンスの一部ではない場合）。
- シークエンスの中断時。

明示的なモーションが再生されている場合、アイドルモーションは実行されません。アクティブなモーションの上に微妙なマイクロムーブメントを重ねたい場合は、代わりに[Lifelike Motions](lifelike_motions)を参照してください。

---

## 設定

<!-- TODO: confirm exact slider names and ranges. -->

- **強度** — アイドルムーブメントの全体的な振幅。
- **速度** — 呼吸／体重移動のサイクルがどれだけ速く実行されるか。
- **体の揺れ、頭の動き** — 地域ごとの乗数。

---

## アイドルモーションの刷新 (v2025.12)

DanceXR 2025.12では、新しいプロシージャルモーションコントロールシステムによって駆動される、より自然なアイドルモーションが導入されました。新しいバージョンは、以前のビルドよりもスムーズで反復性の低いアイドルアニメーションを生成します。プロシージャルモーションコントロールのさらなる改善が今後のリリースで計画されています。

---

## 関連ページ

- [Lifelike Motions](lifelike_motions) — subtle micro-movements on top of any motion
- [Catwalk Motion](catwalk)
- [Auto Dance 3](autodance3)
- [Blink, Breathing & Eye Contact](eyecontact)
- [Motion Settings](motion_settings)