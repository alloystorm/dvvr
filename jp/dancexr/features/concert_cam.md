---
layout: release
title: ./motion/proc/concert_cam
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

# ./motion/proc/concert_cam

設定された位置に配置され、常にフォーカスされたアクターを見る固定カメラです。

## Framing

**Size**は、ターゲットアクターがカメラビュー内でどれだけ大きく見えるかを制御します。
値が低いほど、より狭いフレームでズームインします。値が高いほど、周囲のシーンのより多くの部分を表示します。

**Target Center**は、アクターの体の上の焦点位置を上下に移動させます。
負の値はより低い部分（脚/足）に焦点を合わせます。正の値はより高い部分（胸/頭）に焦点を合わせます。

## Position

**Offset**は、カメラの固定位置を3D空間で移動させます。これを使用して、カメラをシーン原点に対して希望する正確な場所に配置します。

**Shift**は、固定位置を保ちながらカメラを上下に傾けます。
これは、カメラの場所を移動させることなく、視野角を変更します。

## Field of View

**FOV**は、カメラレンズの広さを制御します。値が低いほど望遠レンズ（狭い視野、ズームイン）のように機能し、値が高いほど広角レンズ（より広い視野、より大きな透視歪み）のように機能します。


## Configurations

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
ニア、<b class="font-bolder">ファー</b>、
</td></tr>
<tr><td><strong class="font-bolder">ターゲットの選択</strong></td><td>オプション</td><td>自動、選択、グループ、回転、回転 + グループ、ステージ中央</td><td>自動</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">追跡モード</strong></td><td>オプション</td><td>中央、頭、胸</td><td>中央</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">ターゲットの平滑化</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">予測</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>平滑化によって引き起こされるラグを減らすため、ターゲットの位置を予測します。</td></tr>
<tr><td><strong class="font-bolder">ターゲットへのロックオン</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td>ターゲットに自動的に焦点を合わせます。</td></tr>
<tr><td><strong class="font-bolder">カメラシェイク</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">回転ロック</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td>カメラがターゲットの回転に従います。</td></tr>
<tr><td><strong class="font-bolder">自動ズーム</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>ターゲットサイズをビュー内で維持するために、自動的にズームインおよびズームアウトします。</td></tr>
<tr><td><strong class="font-bolder">ズーム速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>ターゲットFOVにズームするのにかかる時間です。</td></tr>
<tr><td><strong class="font-bolder">ターゲットにおけるFOVの高さ</strong></td><td>Float</td><td>0.2 – 2</td><td>1</td><td></td><td>自動ズームを使用する場合のターゲットの垂直高さです。</td></tr>
<tr><td><strong class="font-bolder">垂直オフセット</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>垂直にオフセットします。</td></tr>
<tr><td><strong class="font-bolder">FOV</strong></td><td>Float</td><td>5 – 120</td><td>10</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">ビートサイクル</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">Size</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>カメラビュー内でのターゲットアクターのサイズ。</td></tr>
<tr><td><strong class="font-bolder">Shift</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>カメラの位置を上下にシフトします。</td></tr>
<tr><td><strong class="font-bolder">ターゲットの中心</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>ターゲットアクター上の焦点位置の中心。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong class="font-bolder">Offset</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="font-bolder">X</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">Y</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="font-bolder">Z</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>