---
layout: release
title: アクタープリセット
locale: ja-JP
toc: true
---

# アクタープリセット

アクタープリセットは、アクターの各種設定（物理、マテリアル、ドレッシング、モーションの好み）のスナップショットを保存します。これにより、後で同じ構成を同じモデル、または骨格が類似した別のモデルに再適用できます。

**2024.1** に追加されました。`[content library](/dancexr/preparecontent)` 内の `presets/` に保存されるため、プリセットは同じ DanceXR バージョンのユーザー間で共有できます。

---

## プリセットの内容

<!-- TODO: confirm the exact list of settings included. -->

典型的なアクタープリセットがキャプチャする要素は以下の通りです。

- アクターごとの [モーション設定](/dancexr/features/actor_motion_settings)
- [ドレッシングシステム](/dancexr/features/optionals) のステータス（可視/非可視アイテム）
- スロットごとの [マテリアル設定](/dancexr/features/material_settings)
- [物理](/dancexr/features/physics) の設定（PMXまたはXPS、[髪](/dancexr/features/hair_physics)、[スカート](/dancexr/features/skirt_physics)、[胸](/dancexr/features/boobs_physics)、[ボディコライダー](/dancexr/features/body_colliders) を含む）
- [足の調整](/dancexr/features/feet_adjustment) および [スケール＆オフセット](/dancexr/features/scale_offset)

プリセットに含まれないもの：

- モデルファイル自体（プリセットは設定を参照するものであり、アセット自体ではありません）。
- システム全体の設定 — これらは [システムプリセット](#system-presets) にあります。
- シーンの構成（ステージ、ライティング、カメラ） — これは [シーン](/dancexr/features/save_scene) にあります。

---

## 保存とロード

<!-- TODO: confirm exact UI path and naming flow. -->

1. アクターを希望の通りに設定します。
2. アクターメニューから **ツールメニュー**（レンチとハンマーのアイコン）を開きます。
3. プリセットを保存し、名前を付けます。
4. 適用するには、任意のギアに対して同じツールメニューを開き、名前で保存されたプリセットを選択します。

プリセットは、コンテンツライブラリの `presets/` に保存されます。プリセットファイルをマシン間でコピーできます。

---

## モデルを越えて再利用可能な場合

プリセットが最も信頼できるのは、以下のモデルに適用された場合です。

- プリセットを保存した **同じモデル**。
- **密接に関連したモデル**（同じソースキャラクター、同じボーン）。
- **類似のビルドを持つ同じフォーマットのモデル**（PMXからPMXへの変換、類似のボーン命名）。

非常に異なるモデル間では、ボーン名に依存する設定（XPS物理リグ、[ボーンマッパー](/dancexr/features/bone_mapper) のオーバーライドなど）は、クリーンに引き継がれない場合があります。

---

## システムプリセット

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

システムプリセットは、アクターごとの設定ではなく、シーン全体の設定（ライティング、環境、カメラ、グラフィックス）を保存します。保存および適用フローは似ていますが、システムプリセットは個別に保存されます。

---

## 関連ページ

- [シーンを保存](/dancexr/features/save_scene) — 単一のアクターの設定ではなく、シーン全体をキャプチャします
- [シーンバンドル](/dancexr/features/scene_bundle) — 保存されたシーンに、その依存アセットをパッケージ化します
- [コンテンツライブラリ](/dancexr/preparecontent) — `presets/` フォルダーの場所
- [アクターメニューとツール](/dancexr/features/actor_tools)