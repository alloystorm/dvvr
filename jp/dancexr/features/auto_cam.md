---
layout: release
title: ./motion/proc/auto_cam
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

# ./motion/proc/auto_cam

音楽のビートと俳優の動作に同期した、映画的なカメラムーブメントを生成する自動カメラシステム。

## Distance

**Distance Near** と **Distance Far** は、カメラがターゲットから取り得る距離の範囲を定義します。範囲が狭いほどカメラの距離は一定に保たれますが、範囲が広いほどショット間でより多くのバリエーションが加わります。実際の距離は、下記の *Distance Selection* の確率によっても影響を受けます。

## Target Selection

カメラがどの身体部分に焦点を合わせるかを制御します。各値は相対的な確率であり、数値が高いほどそのターゲットが選ばれる可能性が高くなります。クローズアップには **Head** と **Chest** が適しており、ワイドなショットには **Center** と **Legs** が適しています。そのターゲットを完全に除外するには、値を *0* に設定してください。

## Distance Selection

カメラがどれだけ離れるかの確率です。**Close Up** は俳優をフレームいっぱいに捉え、**Zoom In** と **Zoom Out** はショット中に距離を変化させ、**Middle** はバランスの取れた視点を提供し、**Far** は全体的なシーンを捉えます。重要なのは相対比率のみであり、最終的な距離は上記の *Distance* 範囲によって制限されます。

## Path & Angles

**High Angle** と **Low Angle** は、カメラが上下にどれだけ傾くかを制限します。低い値に設定すると、カメラはより水平な（ニュートラルな）ルックを保ちます。より広い範囲に設定すると、劇的なオーバーヘッド視点やローアングル視点が導入されます。

## Orientation

カメラが俳優のどの側をフレームするかを決定します。**Front Center** は俳優を直接向き、**Front 45** および **Side 90** は俳優の横顔を捉え、**Back 180** は後ろから撮影します。これらを組み合わせることで、カメラの動きに視覚的な面白さが保たれます。

## Effects

**Fade To Black** は、ショットの移行中に画面が黒にフェードする時間を設定し、**F2B Probability** はそれがどのくらいの頻度で発生するかを制御します。これらを使用して、ショット間に映画的なカットを追加できます。

**Audio Sensitivity** は、有効にすると、カメラの動きが音楽の音量に反応するようにします。高い値に設定すると、大きな音量の箇所でカメラの動きが加速します。

## Random Seed

**Seed** の値は、カメラの動きのための乱数ジェネレーターを制御します。他のすべての設定を同じに保ちながら異なるカメラシーケンスを得るために変更するか、毎回新しいランダムシードを得るために *-1* に設定してください。

## Configurations

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
デフォルト（リセット）、</td></tr>
<tr><td><strong>ターゲット選択</strong></td><td>オプション</td><td>Auto, Selected, Group, Rotate, Rotate + Group, ステージ中心</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>トラッキングモード</strong></td><td>オプション</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>ターゲットスムージング</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>予測</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>スムージングによるラグを減らすため、ターゲットの位置を予測する</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>ビートサイクル</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Distance Near</strong></td><td>Float</td><td>0.5 – 3</td><td>1.5</td><td></td><td>ターゲットからカメラまでの最小距離。</td></tr>
<tr><td><strong>Distance Far</strong></td><td>Float</td><td>0.5 – 3</td><td>2.5</td><td></td><td>ターゲットからカメラまでの最大距離。</td></tr>
<tr><td><strong>Use Actor Orientation</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td>カメラを俳優の向きに合わせる機能を有効または無効にする。</td></tr>
<tr><td><strong>Seed</strong></td><td>Float</td><td></td><td>1234</td><td></td><td>ランダムなカメラムーブメントを生成するためのシード値。</td></tr>
<tr><td><strong>Fade To Black</strong></td><td>Float</td><td>0 – 0.25</td><td>0</td><td></td><td>移行中のフェード・トゥ・ブラック効果の持続時間。</td></tr>
<tr><td><strong>F2B Probability</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>フェード・トゥ・ブラック効果を誘発する確率。</td></tr>
<tr><td><strong>Audio Sensitivity</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>音声レベルに対するカメラの動きの感度。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>ターゲット選択</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Head</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>俳優の頭部をターゲットとする確率。</td></tr>
<tr><td><strong>Chest</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>俳優の胸部をターゲットとする確率。</td></tr>
<tr><td><strong>Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>俳優の中心部をターゲットとする確率。</td></tr>
<tr><td><strong>Legs</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>俳優の脚をターゲットとする確率。</td></tr>
<tr><td><strong>Feet</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>俳優の足元をターゲットとする確率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>距離選択</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Close Up</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>クローズアップカメラ距離の確率。</td></tr>
<tr><td><strong>Zoom In</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>ズームインする確率。</td></tr>
<tr><td><strong>Zoom Out</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>ズームアウトする確率。</td></tr>
<tr><td><strong>Middle</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>中距離カメラ距離の確率。</td></tr>
<tr><td><strong>Far</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>遠距離カメラ距離の確率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>パス選択</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>High Angle</strong></td><td>Float</td><td>0 – 30</td><td>20</td><td></td><td>カメラが上げられる最大角度。</td></tr>
<tr><td><strong>Low Angle</strong></td><td>Float</td><td>-30 – 0</td><td>-20</td><td></td><td>カメラが下げられる最大角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Orientation</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Front Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>カメラを俳優の正面中心に向ける確率。</td></tr>
<tr><td><strong>Front 45</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>カメラを俳優の正面45度に方向付ける確率。</td></tr>
<tr><td><strong>Side 90</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>カメラを俳優の側面90度に方向付ける確率。</td></tr>
<tr><td><strong>Back 135</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>カメラを俳優の背面135度に方向付ける確率。</td></tr>
<tr><td><strong>Back 180</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>カメラを俳優の真後ろに方向付ける確率。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>