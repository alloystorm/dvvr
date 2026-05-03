---
layout: release
title: 俳優オプション
locale: ja-JP
nav_links:
  - label: イントロ
    url: /jp/dancexr
  - label: 機能
    url: /jp/dancexr/features
  - label: リリース
    url: /jp/dancexr/releases
  - label: ダウンロード
    url: /jp/dancexr/download
---

# アクターオプション

アクターモデルが読み込まれたり、置き換えられたりする方法を制御する設定です。

## キャッシュ

モデルは初回ロード後、メモリ上のキャッシュに保持されるため、アクター間の切り替えがほぼ瞬時に行えます。**キャッシュサイズ**は一度に保持するモデルの数を設定します。頻繁に切り替える場合はこれを増やし、RAMの使用量を減らしたい場合は下げてください。

## テクスチャ圧縮

*テクスチャ圧縮*を有効にすると、テクスチャがロード時にGPU圧縮形式に変換されます。これにより複雑なモデルのVRAMが大幅に削減されますが、一部の素材ではわずかな画質の低下が生じる場合があります。

## トランジション

アクターモデルの追加、削除、または置き換えが発生する際の遷移効果を制御します。

## 自動アクター変更

複数のモデルがキャッシュされている場合、*自動アクター変更*の値に基づいて実行時にそれらの間で自動的に切り替わります。

この値に対して自動更新を有効にすると、音楽の進行や選択した任意のデータソースから自動的にアクターを切り替えることが可能になります。

# サブコンポーネント

## トランジションエフェクト

アクターや他のオプションのメッシュが追加、削除、または置き換えされる際に適用される再利用可能なトランジションエフェクトです。このエフェクトは、移動するエッジに沿ってメッシュをディゾルブさせ、オプションのパーティクル、色、グローを追加します。単一の設定が、シェーダー側の燃焼エフェクトとVFXのスポーンの両方を駆動します。

### エッジ形状

**方向**は、エッジがメッシュを*上向き*に掃引するか*下向き*に掃引するかを選択します。**Vシェイプ**は、エッジを平らな水平線（0）から角度のあるV字に曲げ、機械的でないディゾルブに適しています。**トランジションモード**は、エッジを分解するパターンを選択します。チャンキーな細胞様のルックには*セル*、正方形のタイリングには*モザイク*、柔らかいオーガニックなディゾルブには*ノイズ*が使用できます。**スケール**はパターンをリサイズし（対数）、**幅**はディゾルブが広がる帯域を、シャープな線から拡散したフェードまで広げます。

### 色とグロー

**色**は、ディゾルブの先端のエッジで描画される燃焼色です。**グロー**は、そのエッジをエミッシブな強度にブーストし、単なる色味ではなく熱い燃焼として認識させます。**ブレンド**は、トランジション帯における元の色と燃焼色のオーバーライド量を制御します。これを下げることで、エフェクトを通して元の素材が見えるように保持できます。

### 継続時間とパーティクル

**トランジション期間**はオン/オフの浮動小数点数です。カスタムの期間を使用するにはオンに、システムデフォルトにフォールバックするにはオフにします。Questビルドでは、トランジションは強制的に無効化されます。

**パーティクルエフェクト**はスポーンレート（対数 — 0で完全にパーティクルを無効化）を設定し、**パーティクル期間**はそれらが生き続ける長さを設定します。パーティクル期間がトランジション期間を超える場合、パーティクルが空中で途切れるのを防ぐため、トランジションがそれに合わせて引き伸ばされます。

## 設定項目

<table aria-label="アクターオプション設定表">
<thead role="row">
<tr role="row">
<th role="cell">設定</th>
<th role="cell">タイプ</th>
<th role="cell">範囲 / 値</th>
<th role="cell">デフォルト</th>
<th role="cell">条件</th>
<th role="cell">説明</th>
</tr>
</thead>
<tbody role="row">
<tr role="row">
<td role="cell">プリセット</td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell">
</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">キャッシュサイズ</strong></td>
<td role="cell">整数</td>
<td role="cell">0 – 20</td>
<td role="cell">10</td>
<td role="cell"></td>
<td role="cell">キャッシュに保持するアクターモデル数</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">保持オプション</strong></td>
<td role="cell">トグル</td>
<td role="cell">オン / オフ</td>
<td role="cell">オフ</td>
<td role="cell"></td>
<td role="cell">アクターを置き換える際、元の（出ている）アクターの設定を新しい（入ってくる）アクターに自動的に適用します。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">テクスチャ圧縮</strong></td>
<td role="cell">トグル</td>
<td role="cell">オン / オフ</td>
<td role="cell">オフ</td>
<td role="cell"></td>
<td role="cell">VRAM使用量を削減するためにテクスチャを圧縮します</td>
</tr>
<tr role="row">
<td colspan="6">
<details>
<summary><strong role="text">トランジションエフェクト</strong></summary>
<table aria-label="トランジションエフェクト設定表">
<tbody role="row">
<thead role="row">
<tr role="row">
<th role="cell">設定</th>
<th role="cell">タイプ</th>
<th role="cell">範囲 / 値</th>
<th role="cell">デフォルト</th>
<th role="cell">条件</th>
<th role="cell">説明</th>
</tr>
</thead>
<tr role="row">
<td role="cell">プリセット</td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell">
デフォルト（リセット）、
</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">方向</strong></td>
<td role="cell">整数</td>
<td role="cell">0 – 1</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell">アニメーションの方向。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">Vシェイプ</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 5</td>
<td role="cell">1</td>
<td role="cell"></td>
<td role="cell">エッジの角度を制御します。0は平らです。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">トランジションモード</strong></td>
<td role="cell">整数</td>
<td role="cell">0 – 2</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">スケール</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">-3 – 3</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell">パターンのスケール。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">幅</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0.1</td>
<td role="cell"></td>
<td role="cell">トランジションエリアのサイズ。</td>
</tr>
<tr role="row">
<td colspan="6">
<details>
<summary><strong role="text">色</strong></summary>
<table aria-label="色設定表">
<tbody role="row">
<thead role="row">
<tr role="row">
<th role="cell">設定</th>
<th role="cell">タイプ</th>
<th role="cell">範囲 / 値</th>
<th role="cell">デフォルト</th>
<th role="cell">条件</th>
<th role="cell">説明</th>
</tr>
</thead>
<tr role="row">
<td role="cell">プリセット</td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell"></td>
<td role="cell">ホワイト、ブラック、レッド、<b role="text">イエロー</b>、グレー、ブルー、スキン、フレッシュ、オレンジ、</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">色モード</strong></td>
<td role="cell">整数</td>
<td role="cell">0 – 1</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">色相</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0.1667</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">彩度</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">1</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">明度</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0.9</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">赤</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0.9</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">緑</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0.9</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">青</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell"></td>
</tr>
</tbody>
</table>
</details>
</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">グロー</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 10</td>
<td role="cell">1</td>
<td role="cell"></td>
<td role="cell">燃焼エフェクトの明るさ。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">ブレンド</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">1</td>
<td role="cell"></td>
<td role="cell">元の色と燃焼色のブレンド。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">トランジション期間</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 5</td>
<td role="cell">2</td>
<td role="cell"></td>
<td role="cell">アニメーションの期間。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">パーティクルエフェクト</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 10</td>
<td role="cell">2</td>
<td role="cell"></td>
<td role="cell">パーティクルの量を制御します。</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">パーティクル期間</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 5</td>
<td role="cell">2.5</td>
<td role="cell"></td>
<td role="cell">パーティクルの寿命を制御します。</td>
</tr>
</tbody>
</table>
</details>
</td>
</tr>
<tr role="row">
<td role="cell"><strong role="text">自動アクター変更</strong></td>
<td role="cell">浮動小数点数</td>
<td role="cell">0 – 1</td>
<td role="cell">0</td>
<td role="cell"></td>
<td role="cell">この値に基づいてキャッシュ内のアクター間で自動的に切り替わります</td>
</tr>
</tbody>
</table>
`;