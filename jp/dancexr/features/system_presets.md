---
layout: release
title: システムプリセット
locale: ja-JP
toc: true
---

# システムプリセット

<!-- TODO: confirm exact contents and UI flow. Drafted from the 2024.1 release notes. -->

システムプリセットは、**シーン全体および環境設定** — グラフィックス品質、ライティング、空、地面 — を単一の名前付きプリセットとして保存し、後で再適用したり他者と共有したりできます。

**2024.1** で追加されました。プリセットは、[content library](../preparecontent) に個別の JSON ファイルとして保存されます。

---

## システムプリセットの内容

<!-- TODO: confirm the exact list of settings captured. The release notes call out: graphics quality, lighting, sky, ground. There are likely more. -->

一般的なシステムプリセットがキャプチャするのは以下の内容です。

- [グラフィックス設定](graphics) — レンダリング品質、ポストエフェクト。
- [ライティング](lighting) — 方向および環境光の設定、[ライトボール](light_ball)。
- [空と雲](skymap) および [空の色](sky)。
- [地面](ground) — マテリアル、シャドウオンリーモードなど。
- <!-- TODO: confirm whether camera, weather, simulation, or audio settings are included. -->

システムプリセットに含まれないもの:

- アクターごとの設定 — これは[actor presets](actor_presets)に保存されています。
- ロードされたアクター、モーション、音楽、またはステージアセット — これは[saved scene](save_scene)に保存されています。

---

## 保存と読み込み

<!-- TODO: confirm exact UI path. -->

1. シーンを希望の方法で設定します。
2. 関連するシーン/システムメニューを開きます。
3. **プリセットを保存** — 名前を付けます。プリセットは、コンテンツライブラリ内の `presets/` （または system-presets サブフォルダ）に JSON ファイルとして書き込まれます。
4. **プリセットを読み込み** — 名前で保存されたプリセットを選択して適用します。

各プリセットは個別のファイルであるため、マシン間でコピーしたり、他のユーザーと共有したりできます。

---

## システムプリセットとその他のプリセットタイプ

| プリセット | 適用範囲 | 一般的な内容 | ページ |
|---|---|---|---|
| **システムプリセット** | シーン全体 | グラフィックス、ライティング、空、地面 | (このページ) |
| **アクタープリセット** | アクターごと | マテリアル、物理、衣装 | [Actor Presets](actor_presets) |
| **保存されたシーン** | すべて | シーン全体 + アクター + モーション + 割り当て | [Save Scene](save_scene) |
| **シーンバンドル** | すべて + アセット | 保存されたシーン + 依存するモデル/モーション/音楽ファイル | [Scene Bundle](scene_bundle) |

---

## 関連ページ

- [Actor Presets](actor_presets)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)