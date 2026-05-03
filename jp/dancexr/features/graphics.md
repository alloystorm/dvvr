---
layout: release
title: Graphics
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

# グラフィックス

DanceXRのHDRP (HDおよびRT) バージョンにおける、レンダリング品質設定をすべて制御します。プリセットを選択してバランスの取れた出発点を得た後、個々の機能を調整して、パフォーマンスとビジュアルの目標を達成してください。


## プリセット

一般的な範囲をカバーする6つのプリセットがあります：*Performance*はリフレクションとほとんどのスクリーン空間エフェクトを無効にします。*Medium*はフォグとスクリーン空間シャドウを追加します。*High*はスクリーン空間リフレクションを有効にします。*Indoor GI*と*Outdoor GI*は、天の寄与の有無にかかわらずグローバルイルミネーションをアクティブにします。*Dither + TAA*は、クリーンなルックのためにテンポラルアンチエイリアシングとディザリング透過を組み合わせたものです。


## アンチエイリアシングとスーパーサンプリング

**アンチエイリアシング**は、カメラごとの技術（AAなし、SMAA（デファード）、またはTAA）を選択します。**スーパーサンプリング**は、サポートされている場合はDLSSまたはFSRアップスケーリングを解除でき、わずかなシャープさのトレードオフを犠牲にすることでフレームレートを向上させることができます。


## リフレクション

スクリーン空間リフレクション、または平面リフレクションプロブ。一般的な表面には*Screen Space*モードを使用し、平らな床や鏡には*Probe*に切り替えます。品質、エッジフェード距離、およびフォールバック動作はサブセクションで調整できます。


## アンビエントオクルージョンとグローバルイルミネーション

**アンビエントオクルージョン**は、隙間にコンタクトシャドウを追加し、リアリティのある奥行きを与えます。**グローバルイルミネーション**は間接的なバウンスライトを追加します。屋外のシーンでは*Fallback To Sky*を有効にすると、光源から遠ざかる表面でも空の色が受けられます。


## ポストプロセスエフェクト

**被写界深度**は、追跡されているアクター周辺のピントが合っていないオブジェクトをぼかします。**モーションブラー**は、速い動きに速度ベースのブラーを追加します。**ブルーム**は明るいハイライトを光らせます。**レンズフレア**は、明るい光源の周りにスクリーン空間での散乱を追加します。VRでの不快感を避けるため、VRでは無効にしてください。


## フォグ

体積フォグを有効にし、その高さ帯と最大レンダリング距離を設定します。フォグ密度自体は、ライティングパネルの**Fog**スライダーによって制御されます。


## カラー調整

トーンマッピング、露出、コントラスト、色相シフト、彩度、カラーフィルター、2点トーンカーブ、ホワイトバランスがすべてここにあります。**Color Curve**は入力の輝度を出力の輝度にマッピングし、スタイライズされたルックやハイライトの保護に役立ちます。


## オプション

各種レンダリングフラグ：**Transparent Prepass**は透明な表面を通して見えるオブジェクトを隠します。**Toon Shading**は、アクターまたはステージを平らなセルルックに切り替えます。**Dithering Transparency**は、すべての透明なマテリアルにスタippleブレンディングを強制します。**Bump Map Shadow**は、法線マップからマイクロシャドウを追加します。**Compute Thickness**は、サブサーフェス・スキンエフェクトを可能にします。


## ポスタリゼーション

アウトライン、ポスタライズされたイルミネーション、またはハーフティーンスクリーンを最終フレームに重ねるカスタムパスエフェクト—アニメや漫画の美学に役立ちます。

# サブコンポーネント

## リフレクション

スクリーン空間リフレクション、または平面リフレクションプロブを設定します。

*Screen Space*モードは、深度バッファをレイマーチングして、反射する表面を見つけます—これはどのジオメトリでも機能しますが、カメラの視野外のオブジェクトを反射することはできません。平らな床や鏡などの平らな表面には*Probe*モードに切り替え、これは常に完全ですが、パフォーマンスコストがかかります。


### アルゴリズム


*Screen Space*モードでは、*Approximation*の方が高速でほとんどの表面に適しています。*PBR Accumulation*は粗い素材に対してより物理的に正確ですが、クリーンに収束するためにはTAAが必要です。

**Edge Fade Dist**は、スクリーン端の近くの反射をフェードさせ、アーティファクトを隠します。**Object Thickness**は、マーチがどれだけ深い表面を想定するかを制御します。


### スカイリフレクションとフォールバック


**Sky Reflection**は、空に向いている表面のリフレクションにカメラの空の寄与を可能にします。**Fallback To Sky**は、スクリーン空間パスが取りこぼしたエリアのリフレクションプロブのカバーを埋め、わずかな精度トレードオフを伴います。
## ポスタリゼーション

最終レンダリングされた画像の上にスタイライズされたエフェクトを適用するフルスクリーンのカスタムパスです。4つの組み込みプリセット（*Outline*、*Black & White*、*Posterize*、*Halftone*）が簡単な出発点を提供します。


### Outline


深度と法線の不連続性に基づいてエッジをトレースします。**Outline Thickness**と**Outline Intensity**を制御して、重みを調整します。オプションパネルのトゥーンシェーディングと組み合わせることで、セルアニメのようなルックがよく機能します。


### Quantize Illumination & Color


**Quantize Illumination**は画像内の輝度ステップ数を減らします。低い値（例：4〜8）は大胆なポスタライズされたルックを生み出します。**Quantize Color**は、色チャネルに対して同様の処理を行います。両方を0に設定すると、量子化を完全に無効にし、他のエフェクトのみを使用できます。


### Dithering & Halftone


**Dithering**は、滑らかなグラデーションのバンディングを解消するために、順序付けられたノイズを追加します。**Halftone**はドットスクリーンパターンをオーバーレイします。**Halftone Size**と**Strength**を増やすと、ヴィンテージの印刷美学になります。


## 設定

<table >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tbody >
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
Performance, Medium, <b >High</b >, Indoor GI, Outdoor GI, Dither + TAA,
</td></tr>
<tr ><td ><strong >アンチエイリアシング</strong ></th><td >Options</td><td >No AA, Deferred SMAA, Deferred TAA</td><td >Deferred SMAA</td><td ></td><td ></td></tr>
<tr ><td ><strong >スーパーサンプリング</strong ></th><td >Options</td><td >Off, DLSS Performance, DLSS Balance, DLSS Quality, DLSS Ultra Performance, FSR 50%, FSR 66%, FSR 75%, FSR 100%</td><td >Off</td><td ></td><td ></td></tr>
<tr ><td colspan="6"><details >
<summary><strong >Reflection</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Mode</strong ></td ><td >Integer</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >2</td><td ></td><td ></td></tr>
<tr ><td ><strong >Algorithm</strong ></td ><td >Integer</td><td >0 – 1</td><td >0</td><td ></td><td >スクリーン空間リフレクションのアルゴリズム。</td></tr>
<tr ><td ><strong >Edge Fade Dist</strong ></td ><td >Float</td><td >0 – 1</td><td >0.1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Object Thickness</strong ></td ><td >Float</td><td >0 – 0.1</td><td >0.01</td><td ></td><td ></td></tr>
<tr ><td ><strong >Fallback To Sky</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >レイマーチングがヒットしなかった場合の空へのフォールバック。</td></tr>
<tr ><td ><strong >Sky Reflection</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ><tr ><td colspan="6">
<details >
<summary><strong >Fog</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Volumetric Fog</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td ></td></tr>
<tr ><td ><strong >Base Height</strong ></td ><td >Float</td><td >0 – 10</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Max Height</strong ></td ><td >Float</td><td >10 – 100</td><td >25</td><td ></td><td ></td></tr>
<tr ><td ><strong >Max Distance</strong ></td ><td >Float</td><td >0 – 10000</td><td >5000</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Ambient Occlusion</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >2</td><td ></td><td ></td></tr>
<tr ><td ><strong >Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Global Illumination</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Fallback To Sky</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Depth Of Field</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >0.25</td><td ></td><td ></td></tr>
<tr ><td ><strong >Offset</strong ></td ><td >Float</td><td >-1 – 1</td><td >0.1</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Motion Blur</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >0.25</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Bloom</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Quality</strong ></td ><td >Integer</td><td >0 – 2</td><td >2</td><td ></td><td ></td></tr>
<tr ><td ><strong >Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >0.25</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Lens Flare</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td ></td></tr>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Disable in VR</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td >このエフェクトはVRには推奨されません。</td></tr>
<tr ><td ><strong >Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >0.1</td><td ></td><td ></td></tr>
<tr ><td colspan="6"><details >
<summary><strong >Color</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td >プリセット</th><td ></td><td ></td><td ></td><td ></td><td >
<b >White</b >, Sunset, Red, Yellow, Blue, Green,
</td></tr>
<tr ><td ><strong >Color Mode</strong ></td ><td >Integer</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Hue</strong ></td ><td >Float</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Satuation</strong ></td ><td >Float</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Brightness</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Red</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Green</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Blue</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Use Stage Color</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >ステージリングの色を使用します。</td></tr>
<tr ><td ><strong >Color Temp</strong ></td ><td >Float</td><td >3000 – 8000</td><td >6500</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td ><strong >Flares</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Streaks</strong ></td ><td >Float</td><td >0 – 1</td><td >0.2</td><td ></td><td ></td></tr>
<tr ><td ><strong >Length</strong ></td ><td >Float</td><td >0 – 1</td><td >0.5</td><td ></td><td ></td></tr>
<tr ><td ><strong >Chromatic Abberation</strong ></td ><td >Float</td><td >0 – 1</td><td >0.5</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Color Adjustment</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td >プリセット</td><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Tonemapping</strong ></td ><td >Integer</td><td >0 – 3</td><td >3</td><td ></td><td ></td></tr>
<tr ><td ><strong >Adjustment</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td >色調整を有効にします。</td></tr>
<tr ><td ><strong >Post Exposure</strong ></td ><td >Integer</td><td >-12 – 12</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Contrast</strong ></td ><td >Float</td><td >-100 – 100</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Hue Shift</strong ></td ><td >Float</td><td >-180 – 180</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Saturation</strong ></td ><td >Float</td><td >-100 – 100</td><td >1</td><td ></td><td ></td></tr>
<tr ><td colspan="6"><details >
<summary><strong >Color Filter</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td >プリセット</td><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Color Mode</strong ></td ><td >Integer</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Hue</strong ></td ><td >Float</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Satuation</strong ></td ><td >Float</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Brightness</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Red</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Green</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Blue</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td ><strong >Color Curve</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td ><strong >Start Gradient</strong ></td ><td >Float</td><td >0 – 4</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Start Position</strong ></td ><td >Float</td><td >0 – 0.5</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Start Value</strong ></td ><td >Float</td><td >0 – 0.5</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >End Gradient</strong ></td ><td >Float</td><td >0 – 4</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >End Position</strong ></td ><td >Float</td><td >0.5 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >End Value</strong ></td ><td >Float</td><td >0.5 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >White Balance</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >ホワイトバランスを有効にします。</td></tr>
<tr ><td ><strong >Temperature</strong ></td ><td >Float</td><td >-100 – 100</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Tint</strong ></td ><td >Float</td><td >-100 – 100</td><td >0</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Posterization</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td ><strong >Enabled</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td >プリセット</td><td ></td><td ></td><td ></td><td ></td><td >
Outline, Black & White, <b >Posterize</b >, Halftone,
</td></tr>
<tr ><td ><strong >Outline Thickness</strong ></td ><td >Float</td><td >0 – 1</td><td >0.1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Outline Intensity</strong ></td ><td >Float</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >Quantize Illumination</strong ></td ><td >Integer</td><td >0 – 16</td><td >8</td><td ></td><td ></td></tr>
<tr ><td ><strong >Quantize Color</strong ></td ><td >Integer</td><td >0 – 64</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >Dithering</strong ></td ><td >Float</td><td >0 – 1</td><td >0.25</td><td ></td><td ></td></tr>
<tr ><td ><strong >Halftone Size</strong ></td ><td >Float</td><td >0 – 1</td><td >0.25</td><td ></td><td >ハーフティーンサイズ</td></tr>
<tr ><td ><strong >Halftone Strength</strong ></td ><td >Float</td><td >0 – 1</td><td >0.1</td><td ></td><td >ハーフティーン強度</td></tr>
</tbody ></table >
</details ></td ></tr >
<tr ><td colspan="6"><details >
<summary><strong >Options</strong ></summary>
<table ><tbody >
<thead ><tr ><th >設定</th><th >タイプ</th><th >範囲 / 値</th><th >デフォルト</th><th >条件</th><th >説明</th></tr></thead>
<tr ><td >プリセット</td><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >Transparent Prepass</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td >透明な事前パスを有効にします。これにより、隠れた透明なマテリアルが見えなくなります。</td></tr>
<tr ><td ><strong >Screen Space Shadows</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
<tr ><td ><strong >Contact Shadow</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >小さなディテールへのシャドウ。</td></tr>
<tr ><td ><strong >Bump Map Shadow</strong ></td ><td >Float</td><td >0 – 1</td><td >0.5</td><td ></td><td >バンプマップおよびディテールマップのシャドウを有効にします。</td></tr>
<tr ><td ><strong >Stop NaN</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td >ポストプロセス中にエラーが発生した場合の黒画面を防ぎます。 </td></tr>
<tr ><td ><strong >Compute Thickness</strong ></td ><td >Toggle</td><td >on / off</td><td >on</td><td ></td><td >スキンエフェクトに使用できる厚さを計算します。</td></tr>
<tr ><td ><strong >Actor Model Toon Shading</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >すべてのアクターにトゥーンシェーディングを使用します。</td></tr>
<tr ><td ><strong >Stage Model Toon Shading</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td >ステージやプロップにトゥーンシェーディングを使用します。</td></tr>
<tr ><td ><strong >Dithering Transparency</strong ></td ><td >Toggle</td><td >on / off</td><td >off</td><td ></td><td ></td></tr>
</tbody ></table >
</details ></td ></tr >
</tbody >
</table >