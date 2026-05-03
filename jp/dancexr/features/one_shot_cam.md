---
layout: release
title: ./motion/proc/oneshot_cam
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

# ./motion/proc/oneshot_cam

アクターを追跡しながら、ビートごとにランダムに動く長回しカメラです。

## Movement

**Rotate Range**（回転範囲）は、カメラがアクターの周りを左右にどれだけ周回できるかを制限します。範囲が広いほど広範囲のショットになり、範囲が狭いほどカメラがアクターの方を向いた状態を保ちます。

**Curve**（カーブ）の値は、ビートごとにカメラが新しいランダムな位置に移動する際のイージングを制御します。負の値はゆっくり始まって速くなり、正の値は速く始まってゆっくりになります。*0* は線形な動きになります。

## Distance & Pitch

カメラの距離と垂直角度の範囲を設定します。カメラはビートごとにこれらの制限内でランダムな位置を選択します。

**Distance**（距離）は、カメラとターゲットの距離を制御します。値が小さいほどクローズアップ、大きいほど広角のショットになります。

**Pitch Angle**（ピッチ角度）は、垂直な傾き範囲を設定します。負の値はアクターを見下ろし、正の値は見上げます。

## Orientation

**Use Actor Orientation**（アクターの向きの使用）を有効にすると、カメラをアクターの向いている方向と合わせ、アクターが見ている相対的な位置を保つことができます。

**Raise Focus When Close**（近接時のフォーカス上昇）を有効にすると、カメラが近づくにつれてフォーカスポイントが自動的に上に移動し、クローズアップショットでアクターの頭部がフレーム内に収まるようにします。

**Prevent Below Floor**（床下移動防止）は、カメラが地面の平面の下に移動するのを防ぎます。

## Configurations

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
デフォルト（リセット）、</td></tr>
<tr><td><strong>ターゲット選択</strong></td><td>オプション</td><td>自動、選択、グループ、回転、回転 + グループ、ステージ中央</td><td>自動</td><td></td><td></td></tr>
<tr><td><strong>追跡モード</strong></td><td>オプション</td><td>中央、頭部、胸部</td><td>中央</td><td></td><td></td></tr>
<tr><td><strong>ターゲット平滑化</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>予測</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>平滑化による遅延を減らすためにターゲットの位置を予測します。</td></tr>
<tr><td><strong>視野角</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>ビートサイクル</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>回転範囲</strong></td><td>Float</td><td>0 – 180</td><td>60</td><td></td><td>水平な回転範囲です。</td></tr>
<tr><td><strong>距離</strong></td><td>範囲</td><td>0.2 – 5</td><td></td><td></td><td></td></tr>
<tr><td><strong>ピッチ角度</strong></td><td>範囲</td><td>-90 – 90</td><td></td><td></td><td></td></tr>
<tr><td><strong>カーブ</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>モーションを変更する際に使用されるイージングカーブです。</td></tr>
<tr><td><strong>床下移動防止</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td><strong>アクターの向きの使用</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td><strong>近接時のフォーカス上昇</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td>距離が短くなるにつれてフォーカス位置を上に移動させます。</td></tr>
</tbody>
</table**>