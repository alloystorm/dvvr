---
layout: release
title: ./motion/proc/free_cam
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

# ./motion/proc/free_cam

現在地と回転を完全に制御できる、完全に手動のカメラモードです。シーン内を自由に移動したり、ポイントを中心とした周回移動を行ったり、アクターを追尾したりすることができます。

## Movement

**移動減衰**はカメラの位置変化を滑らかにします。値を低くするとカメラの反応性が高まり、値を高くすると映画的なイージング（入退場）のための慣性が加わります。

**軌道移動の使用**は、自由な移動から軌道モードに切り替えます。このモードでは、カメラは前進するポイントから1.5 m先を中心として回転します。被写体の周りを周回するのに役立ちます。

**垂直移動の制限**（VRプラットフォーム専用）は、小さな垂直オフセットが意図せず発生し地面レベルに戻ってしまうのを防ぎます。

## Lock On Target

**対象追尾**が有効になっていると、カメラが選択されたアクターを自動的に追尾します。**トラッキングモード**では、どの身体部分（中心、頭、または胸）を追跡するかを選択できます。**対象平滑化**と**予測**は、追尾時の遅延や振動を軽減します。**自動ズーム**は、対象を画面サイズで一定に保つように視野を調整し、**対象におけるFOVの高さ**が望ましい見かけの高さを制御します。**カメラシェイク**は、追尾の遅延によって調整される、微妙な手持ち風の動きを加えます。**回転固定**は、カメラが対象の向きにも追従するようにします。

## Presets

一般的なセットアップをカバーする4つの組み込みプリセットがあります：*Freefly*（完全な手動制御）、*Lock On Actor*（ズームなしの追跡）、*Lock + Zoom Fullbody*、および *Lock + Zoom Upper Body*（胴体部分に焦点を絞ったよりタイトなフレーミング）。

## Configurations

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Freefly</b>、Lock On Actor、Lock + Zoom Fullbody、Lock + Zoom Upper Body、</td></tr>
<tr><td><strong >Target Select</strong ></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong >Tracking Mode</strong ></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong >Target Smoothing</strong ></td><td>Float</td><td>0 – 2</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong >Prediction</strong ></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td>平滑化によって生じる遅延を軽減するために、対象の位置を予測します。</td></tr>
<tr><td><strong >Lock On Target</strong ></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>対象に自動的にフォーカスします</td></tr>
<tr><td><strong >Camera Shake</strong ></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong >Lock Rotation</strong ></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>カメラが対象の回転に追従します</td></tr>
<tr><td><strong >Auto Zoom</strong ></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>対象のサイズを視野内で一定に保つために、自動的にズームイン/ズームアウトします</td></tr>
<tr><td><strong >Zoom Speed</strong ></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>対象FOVへのズームにかかる時間</td></tr>
<tr><td><strong >FOV Height At Target</strong ></td><td>Float</td><td>0.2 – 2</td><td>1</td><td></td><td>自動ズーム使用時の対象の垂直高さ</td></tr>
<tr><td><strong >Vertical Offset</strong ></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>垂直方向にオフセットします</td></tr>
<tr><td><strong >FOV</strong ></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong >Beat Cycle</strong ></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong >Movement Damping</strong ></td><td>Float</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong >Use Orbit Move</strong ></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>軌道移動を有効または無効にし、カメラを中心点周りに回転させることが可能になります。</td></tr>
</tbody>
</table>