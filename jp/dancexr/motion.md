---
layout: release
title: # モーションシステム
locale: ja-JP
toc: true
---

# モーションシステム

DanceXRでのモーションは複数のソースから、複数のレベルで設定され、スタックすることができます。このページがそのマップです：モーションがどこから来て、設定がどこに存在し、レイヤーがどのように組み合わされるかを示します。

用語（モーションパス、オーバーライド、ダンスセット、リミックス、カスタムインヘリット）については、[Concepts & glossary](concepts#motion-concepts)を参照してください。

---

## モーションのソース

モーションが取り得る場所は5ヶ所あります。

1. ディスクからロードされた**モーションファイル**（VMDまたはBVH）。
2. **ダンスセット** — オーディオファイル1つと、それに対応する1つ以上のモーションをまとめたもの。フォルダやzipファイルにグループ化されている場合、自動検出されます。
3. **プロシージャルモーション** — Auto Dance、Idle Motion、Catwalk、Lifelike Motions、Secondary Motionによって実行時に生成されます。
4. **キーフレームアニメーション** — DanceXR内で手動で作成したポーズ。
5. **リミックス** — あるダンスセットのモーションデータと、別のダンスセットのオーディオを使用すること。

これらを混合できます。一般的なシーンでは、VMD駆動のダンスがプレイされ、その上にプロシージャルな[secondary motion](features/secondary_motion)レイヤーが加わり、さらに独自のシステムによって眼球の動きや呼吸が処理されます。

---

## ダンスセットユニット

[ダンスセット](features/dance_set)は、「一曲」の自然なグループ化単位です。1つのオーディオファイルと1つ以上の対応するVMD/BVHファイルを含むフォルダまたはzipファイルを`motion/`に配置すると、DanceXRが自動的にグループ化します。ロードされたダンスセットは以下の機能を持っています。

- オーディオを再生します。
- アクターにモーションをルーティングします（デフォルトではアクターごとに1モーション。再割り当て可能）。
- カメラVMDが含まれている場合、オプションでカメラを駆動します。
- オーディオのBPMに連動した共有の[music timing](features/music_timing)を持っています。

このセットがロード、保存、共有、およびリミックスする単位となります。個々のモーションは引き続き独自のセッティング（モーションごとの速度、ループ範囲など）を持っていますが、ダンスセットがそれらを連携させて保持します。

[VMD2PNG](features/dance_set#vmd2png-v20263)（2026.3で追加）を使用すると、VMDデータをエンコードしたPNGファイルからモーションデータをロードできます。これはファイルサイズが小さく、共有しやすく、サムネイルが含まれています。

---

## 設定の階層

モーション設定は3つのレベルに存在します。同じパラメータが複数のレベルに存在する場合、より具体的なレベルが優先されます。

| レベル | ページ | 適用範囲 |
|---|---|---|
| システム | [Motion settings](features/motion_settings) | シーン内のすべてのモーションのデフォルト設定 |
| アクターごと | [Actor motion settings](features/motion_settings) | 特定のアクターのモーションに対する上書き設定 |
| モーションごと | [Dance set](features/dance_set)内 | セット内でのモーションごとの調整 |

[Playback options](features/playback_options) — 速度、ループモード、範囲 — は再生レベル（オーディオ/モーションのタイムライン全体）に適用されます。

---

## モーションの割り当て

[Assigning motion](features/assign_motion)は、実際のメカニクスを網羅しています：VMDをウィンドウにドラッグ＆ドロップするか、オーディオ/モーションメニューで*Assign To*をクリックするか、またはアクターメニューを開いてすでにロードされたモーションから選択します。

複数のアクターが存在する場合、順序が重要です。アクターの[Tools menu](features/actor_tools#tools-menu)で**Move Up / Move Down**を行うとアクターの順序が変更され、その結果、ダンスセット内で自動割り当てされるモーションが変わります。

[Spectator mode](features/spectator_mode)では、アクターを自動割り当てから除外できます。

---

## レイヤーとオーバーライド

モーションを組み合わせたり、変更したりしたい場合、関連する機能を備えた4つのページがあります。目的に応じた適切なものを選んでください。

| 目的 | 使用するページ |
|---|---|
| 同じアクターで同時に2つのモーションを再生したい（例：ダンスとハンドウェーブ） | [Motion passes](features/motion_passes) |
| モーション内の特定のボーンを置き換えたい（腕のクリッピング修正、顔の差し替えなど） | [Motion override](features/motion_override) |
| PMXが使用するボーン追従関係を作成または修正したい | [Custom inherit motion](features/custom_inherit) |
| あるダンスセットのモーションと、別のオーディオをペアにしたい | [Remix motion](features/remix) |

モーションパスはレイヤーを重ねるもの、オーバーライドはボーンごとにマスクをかけるもの、インヘリットモーションは「何が何に従うか」という定義自体を変更するもの、リミックスは同一モーションの下でオーディオを入れ替える、より高レベルなスワップです。

---

## プロシージャルモーション

実行時に生成され、ソースとなるVMDは不要です：

- [Idle motion](features/idle_motion) — 他の何も再生されていないときの呼吸や静かなポーズ。
- [Catwalk motion](features/catwalk) — プロシージャルな歩行サイクル。
- [Auto Dance 1](features/autodance), [Auto Dance 2](features/autodance2), [Auto Dance 3](features/autodance3) — プロシージャルなダンスジェネレーター。早期の世代を選択する理由がない限り、**Auto Dance 3**を使用してください。これはリズム分析と最も強力なバリエーションを備えています。
- [Lifelike motions](features/lifelike_motions) — ポーズが停止している、またはアイドル状態のアクターに生命感を与えるマイクロモーション。
- [Secondary motion](features/secondary_motion) — いずれのモーションの上にも動作するプロシージャルレイヤー（揺れ、呼吸、フォロースルーなど）。
- [Keyframe animation](features/keyframe_animation) — 手動のキーフレームで独自のポーズを作成します。

[Idle motion](features/idle_motion)、[Auto Dance](features/autodance)、[Auto Dance 2](features/autodance2)、および[Motion override](features/motion_override)はすべて、ダイレクトなポージングのための[gizmo cubes](controls#gizmo-cubes)を公開しています。

---

## Music timing

[Music timing](features/music_timing)は、ロードされたオーディオのBPMとビートオフセットを検出します（または設定できます）。いくつかのシステムがこれを利用します。

- [Auto Dance 3](features/autodance3) は、モーションの変化をビートに同期させます。
- [Auto camera](features/auto_cam) は、ショットのトランジションをビートに同期させ、オーディオの感度に対応できます。
- [Auto update](features/autoupdate) は、ビート信号からあらゆる設定を駆動できます。

プロシージャルダンスがテンポからずれていると感じた場合は、まずミュージックタイミングを修正してください。

---

## キャラクターの動作 — 常時レイヤー

3つのシステムが、どのモーションが再生されていても継続的に実行され、キャラクターがロボットのように見えすぎるのを防ぎます：

- [Blink, breathing & eye contact](features/eyecontact) — まぶたの動き、自動的な視線追跡、呼吸の上下動。
- [Facial control](features/facial_control) — 手動または自動の表情/モーフブレンディング。
- [Lifelike motions](features/lifelike_motions) — 小さなアイドル時の調整。

これらは使用しているモーションソースと合成されます。

---

## よくある問題

| 症状 | 可能性の高い修正方法 |
|---|---|
| モーションをロードしたが何も起こらない | モーションはロードされたが割り当てられていない場合がある — [Assigning motion](features/assign_motion)を参照 |
| 間違ったアクターがダンスを踊る | [Tools menu](features/actor_tools#tools-menu)でMove Up / Downを使ってアクターの順序を変更する |
| モーションの速度がおかしい | [playback options](features/playback_options)と[dance set](features/dance_set)のモーションごとの速度を確認する |
| プロシージャルダンスのビートがズレる | [Music timing](features/music_timing) — BPMとオフセットを確認する |
| 腕がボディをすり抜ける | 問題の腕のボーンに対して[Motion override](features/motion_override)を使用する |
| モーション間でキャラクターが生き生きして見えない | [idle motion](features/idle_motion)、[eye contact](features/eyecontact)、[lifelike motions](features/lifelike_motions)を有効にする |

---

## 関連ページ

- [Concepts & glossary](concepts#motion-concepts)
- [Working with actors](actors)
- [AI in DanceXR](ai) — Auto DanceおよびAI駆動のモーション
- [Cinematic camera](cameras) — Auto Camはミュージックタイミングも読み取ります