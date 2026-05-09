---
layout: release
title: 物理システム
locale: ja-JP
toc: true
---

# 物理システム

DanceXRには、PMXおよびXPS向けにモデル形式ごとの物理システムがあり、さらに布、ソフトボディ、簡易剛体のシミュレーションに使用できるカスタム構築されたXPBD（拡張粒子ベースダイナミクス）システムがあります。

PMXモデルの場合、物理リグはファイル内に定義され、PMX物理設定を通じて公開されます。

XPSモデルの場合、ファイル内にリグがないため、XPS物理ツールを使用して物理をゼロから設定する必要があります。

PMXおよびXPSの物理は、デフォルトでPhysXベースの組み込みUnity物理エンジンを使用しますが、XPBDバックエンドに切り替えることも可能です。

XPBDシステムを使用した布のシミュレーションは、PMXおよびXPSの両方のモデルで利用可能であり、布シミュレーション設定を通じて構成します。

用語（剛体、ジョイント、コライダー、ばね力、減衰、射影距離、射影角度）については、[コンセプトと用語集](concepts#bones-physics-and-colliders)を参照してください。

> システム全体に適用される物理ダイアログと、個々のPMXモデルに適用されるダイアログの詳細なパラメーター参照は、[物理（設定参照）](features/physics)にあります。

---

## 2つの経路：PMX vs XPS

最大の違いはモデル形式です。

| | PMX | XPS |
|---|---|---|
| 物理リグがあるか？ | はい — ファイルに組み込み | いいえ — DanceXRで設定 |
| デフォルト動作 | すぐに機能する | 設定するまで何も動かない |
| 設定を行う場所 | [PMX物理](features/pmx_physics)（アクターごと） | [XPS物理ツール](features/xps_physics)（アクターごと） |
| よくある落とし穴 | モデル製作者によるジョイントの剛性が上書きされる必要がある場合がある | 髪、胸、スカートなど、何かをさせる前に**ボーンを選択**する必要がある |

どちらの経路も、システムレベルのダイアログ（重力、シミュレーションステップ）と、以下の特殊リグ群を共有しています。

---

## システムレベルの設定

システムレベルの物理設定は、モデル形式やリグの種類に関わらず、DanceXRのすべての物理シミュレーションにグローバルに適用されます。

---

## リグ群

これらはパーツごとの物理リグです。ほとんどがPMXとXPSの両方で機能しますが、PMXモデルがすでに同じパーツの剛体を含んでいるため、一部はXPS固有のものとなっています。

### 体の形状 (Body shape)

[ボディコライダー](features/body_colliders) — アクターの体沿いに配置されるカプセルコライダー。これにより、自由に動くパーツ（髪、布、スカート）が体と貫通する代わりに衝突するようになります。

### 髪 (Hair)

[髪の物理](features/hair_physics) — 頭に根ざしたボーンのツリー上でのばねボーンシミュレーション。ルートボーンを設定すると、DanceXRが子ボーンを処理してリグを構築します。

### スカートおよび垂れ下がるもの (Skirt and dangling)

- [スカート物理](features/skirt_physics) — 水平な接続を持つ（メッシュのような）チェーン物理。スカートや裾に適しています。
- [垂れ下がる物理](features/dangling_physics) — 水平な接続を持たないチェーン物理。リボン、紐、耳飾り、尻尾など、ぶら下がるものに適しています。

違いは、近くのチェーンが水平にリンクされているかどうかです。リンクがないとスカートは崩れ落ち、リンクがあるとリボンは不自然にぶら下がります。

### 胸 (Breast)

[バストの物理](features/boobs_physics) — バストボーンによるジョイントベースの揺れ（ジグル）。常に下向きに引っ張られる力に打ち消す反重力を適用します。PMXモデルが通常ファイル内に独自の胸ジョイントを持っているため、XPS関連性が高いです。

### 布 (Cloth)（メッシュベース）

- [布シミュレーション](features/cloth_simulation) — ガウンメッシュ上のUnityの布スタイルシミュレーション。
- [メッシュから布へ](features/mesh_to_cloth) — モデルのメッシュを布シミュレーションされたオブジェクトに変換します。

これらはスカート／垂れ下がるチェーン物理とは異なります。布は小さな制御ボーンのセットではなく、メッシュ全体をシミュレートします。重く、ドラマチックで全身的な動きに向いています。

### ソフトボディ (Soft body)

- [ソフトボディ物理](features/softbody_physics) — 体積変形。 <!-- TODO: primary use cases を確認する。 -->
- [粒子ダイナミクス](features/particle_dynamics) — 粒子ベースの二次モーション。

### 全身 (Whole-body)

- [ラグラ人形](features/ragdoll) — 物理が全身のボーンを制御し、アクターがぐにゃりと弛緩します。
- [オブジェクトを分離](features/detach_object) — ボーンやオブジェクトを解放し、物理によって独立して動くようにします。
- [二次モーション](features/secondary_motion) — 既存の動きに呼吸、揺れ、フォローアップを追加するプロシージャルレイヤーです。

---

## 何を使うかを選ぶ

| したいこと | 推奨されるもの |
|---|---|
| 振れる髪 | [髪の物理](features/hair_physics) — ルートボーンを設定 |
| 広がるスカート | [スカート物理](features/skirt_physics)（XPS）、または [PMX物理](features/pmx_physics)（PMX） |
| ぶら下がるリボン、尾、または紐 | [垂れ下がる物理](features/dangling_physics) |
| XPSでのバストの揺れ | [バストの物理](features/boobs_physics) — ボーンを割り当てる |
| 生地のようにシミュレーションされる全身の衣装 | [布シミュレーション](features/cloth_simulation) |
| 体のパーツを立体的に感じさせたい | [ソフトボディ物理](features/softbody_physics) |
| アクターを倒れたようにさせたい | [ラグラ人形](features/ragdoll) |
| 体の一部を動的に取り除きたい | [オブジェクトを分離](features/detach_object) |
| 任意の動きにわずかな生きた感じを加えたい | [二次モーション](features/secondary_motion) |
| 髪／布が実際に体に衝突するようにしたい | [ボディコライダー](features/body_colliders) |

---

## よくある問題

| 症状 | 考えられる原因 |
|---|---|
| 髪／布が体に貫通する | [ボディコライダー](features/body_colliders) が設定されていない、または [物理設定](features/physics) で *衝突無効* がオンになっている |
| 髪を選択したが何も動かない | 選択したボーンがルートではない可能性があります。 [ボーン構造の例](features/bones) を確認してください |
| バストが動かない | バスト物理のトグルはオンですが、ボーンが割り当てられていません。 [バストの物理](features/boobs_physics) を参照してください |
| 時間とともにボーンが漂う | *射影距離* / *射影角度* を減らすか、[物理設定](features/physics) で *変更時にリセット* を有効にしてください |
| 高FPSでのちらつき | [シミュレーション](features/simulation) で毎秒ステップ数を増やす |
| 物理がオンのときFPSが落ちる | ステップ数を減らします。不要な重いリグ（布、ソフトボディ）はオフにしてください |
| スカートが硬い円錐のように見える | スカート物理ではなく、垂れ下がる物理を使用しています。設定を切り替えてください（[スカート](features/skirt_physics) 対 [垂れ下がる](features/dangling_physics)） |

---

## 関連ページ

- [コンセプトと用語集](concepts#bones-physics-and-colliders)
- [アクターの操作](actors)
- [物理（設定参照）](features/physics) — システム全体およびPMX固有のダイアログパラメーター
- [XPS物理](features/xps_physics) — XPSリグ設定
- [ボーン構造の例](features/bones) — ボーン選択用の参照スケルトン

<!-- TODO Phase 3: resolve duplicate pages — cloth_sim.md vs cloth_simulation.md, physics_softbody.md vs softbody_physics.md, transparency.md vs material_transparent.md. Also consider renaming features/physics.md to features/pmx_physics_settings.md to make this hub the canonical "Physics" entry. -->