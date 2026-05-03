---
layout: release
title: ./motion/proc/oneshot_cam
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---

# ./motion/proc/oneshot_cam

長鏡頭攝影機，每個節拍會隨機移動，同時跟隨演員。

## Movement

**旋轉範圍 (Rotate Range)** 限制了攝影機環繞演員左或右移動的最大角度。範圍越廣，拍攝畫面越飄逸；範圍越窄，攝影機看起來就越正對前方。

**曲線 (Curve)** 值控制了攝影機在每個節拍移動到新的隨機位置時的減速過渡 (easing)。負值開始緩慢並加快；正值開始快速並減慢；*0* 提供線性運動。

## Distance & Pitch

設定了攝影機距離和垂直角度的範圍。每個節拍，攝影機都會從這些限制內選擇一個隨機位置。

**距離 (Distance)** 控制攝影機與目標的遠近——數值越小，特寫鏡頭越近；數值越大，廣角鏡頭越遠。

**俯仰角 (Pitch Angle)** 設定垂直傾斜的角度範圍。負值會看向演員下方；正值會看向上方。

## Orientation

啟用 **使用演員朝向 (Use Actor Orientation)** 可以讓攝影機與演員的朝向對齊，這樣攝影機就會相對保持在演員看向的方向。

啟用 **近處提升焦點 (Raise Focus When Close)** 可以自動隨著攝影機越來越近，將焦點點向上移動，從而確保特寫鏡頭中演員的頭部保持在畫面內。

**防止低於地面 (Prevent Below Floor)** 會阻止攝影機移動到地平面下方。

## Configurations

<table class="table">
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設 (Preset)</td><td></td><td></td><td></td><td></td><td>預設 (重置)，</td></tr>
<tr><td><strong class="text-primary">目標選擇 (Target Select)</strong></td><td>選項 (Options)</td><td>自動 (Auto), 選定 (Selected), 群組 (Group), 旋轉 (Rotate), 旋轉 + 群組 (Rotate + Group), 場景中心 (Stage Center)</td><td>自動 (Auto)</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">追蹤模式 (Tracking Mode)</strong></td><td>選項 (Options)</td><td>中心 (Center), 頭部 (Head), 胸部 (Chest)</td><td>中心 (Center)</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">目標平滑度 (Target Smoothing)</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">預測 (Prediction)</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>1</td><td></td><td>用來預測目標位置，以減少因平滑度造成的延遲</td></tr>
<tr><td><strong class="text-primary">視野角 (FOV)</strong></td><td>浮點數 (Float)</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">節拍週期 (Beat Cycle)</strong></td><td>整數 (Integer)</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">旋轉範圍 (Rotate Range)</strong></td><td>浮點數 (Float)</td><td>0 – 180</td><td>60</td><td></td><td>水平旋轉範圍。</td></tr>
<tr><td><strong class="text-primary">距離 (Distance)</strong></td><td>範圍 (Range)</td><td>0.2 – 5</td><td></td><td></td><td></td></tr>
<tr><td><strong class="text-primary">俯仰角 (Pitch Angle)</strong></td><td>範圍 (Range)</td><td>-90 – 90</td><td></td><td></td><td></td></tr>
<tr><td><strong class="text-primary">曲線 (Curve)</strong></td><td>浮點數 (Float)</td><td>-1 – 1</td><td>0</td><td></td><td>改變運動時使用的減速曲線。</td></tr>
<tr><td><strong class="text-primary">防止低於地面 (Prevent Below Floor)</strong></td><td>開關 (Toggle)</td><td>開啟 (on) / 關閉 (off)</td><td>開啟 (on)</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">使用演員朝向 (Use Actor Orientation)</strong></td><td>開關 (Toggle)</td><td>開啟 (on) / 關閉 (off)</td><td>開啟 (on)</td><td></td><td></td></tr>
<tr><td><strong class="text-primary">近處提升焦點 (Raise Focus When Close)</strong></td><td>開關 (Toggle)</td><td>開啟 (on) / 關閉 (off)</td><td>關閉 (off)</td><td></td><td>當距離變小時，提高焦點位置</td></tr>
</tbody>
</table>