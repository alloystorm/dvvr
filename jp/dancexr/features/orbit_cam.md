---
layout: release
title: ./motion/proc/orbit_cam
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

# ./motion/proc/orbit_cam

焦点となるアクターの周りを回転するマニュアルおよび自動軌道カメラ。

## 手動制御

自動モードでない場合、ドラッグしてアクターの周りにカメラを軌道移動させます。
**コントローラー入力の使用**は、ゲームパッド/VRコントローラーでの軌道移動のサポートを可能にします。
**床下移動防止**は、カメラが地面より下を移動するのを防ぎます。

**慣性維持**は、入力を放してもカメラが回転し続け、徐々に減速します。**最小速度**と**最大速度**が維持される回転速度を制限します。長時間のシネマティックな回転をさせたい場合は*最大速度*を上げ、より細かい制御をしたい場合は下げる必要があります。

## 自動モード

有効にすると、カメラが、サイン波を使用してサイクルする距離、ピッチ、高さで自動的に軌道移動を行います。

**最小距離**と**最大距離**は、各サイクルでカメラが移動する近距離/遠距離の範囲を設定します。**距離サイクル**は、完全な往復サイクルにかかる秒数を表します。

**最小ピッチ**と**最大ピッチ**が垂直角度範囲を制御し、**ピッチサイクル**はカメラが上下に傾く速度を設定します。

**最小高さ**と**最大高さ**がカメラターゲットの垂直オフセットを調整し、**高さサイクル**が振動周期を制御します。

**速度**は、自動モードがアクティブなときのカメラの水平方向の軌道速度を設定します。速いスウィープショットには値を上げ、ゆっくりと意図的な円を描く場合は値を下げてください。


## 設定

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>スムージングによる遅延を減らすためにターゲットの位置を予測します</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Use Controller Input</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Prevent Below Floor</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td><strong>Retain Velocity</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>入力がないときも回転を維持します</td></tr>
<tr><td><strong>Max Speed</strong></td><td>Float</td><td>0 – 30</td><td>15</td><td></td><td>最大回転速度</td></tr>
<tr><td><strong>Min Speed</strong></td><td>Float</td><td>0 – 30</td><td>0</td><td></td><td>最小回転速度</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>自動モード</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>最小距離</strong></td><td>Float</td><td>0 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>最大距離</strong></td><td>Float</td><td>1 – 10</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>距離サイクル</strong></td><td>Float</td><td></td><td>12</td><td></td><td></td></tr>
<tr><td><strong>最小ピッチ</strong></td><td>Float</td><td>-45 – 0</td><td>-15</td><td></td><td></td></tr>
<tr><td><strong>最大ピッチ</strong></td><td>Float</td><td>0 – 45</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>ピッチサイクル</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>最小高さ</strong></td><td>Float</td><td>-1 – 0</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>最大高さ</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>高さサイクル</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>速度</strong></td><td>Float</td><td>0 – 90</td><td>10</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>