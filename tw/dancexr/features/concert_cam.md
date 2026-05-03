---
layout: release
title: ./motion/proc/concert_cam
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

# ./motion/proc/concert_cam

固定攝影機，定位在既定位置，始終朝向聚焦的表演者。

## 構圖 (Framing)

**大小 (Size)** 控制目標表演者在攝影機視圖中顯示的大小。數值越低，取景越近；數值越高，則能展示更多周圍場景。

**目標中心 (Target Center)** 將焦點向上或向下移動到表演者的身體上。負數值聚焦較低處（腿/腳）；正數值聚焦較高處（胸部/頭部）。

## 位置 (Position)

**偏移 (Offset)** 移動攝影機在 3D 空間中的固定位置。用此功能將攝影機放置在相對於場景原點的精確位置。

**傾角 (Shift)** 在保持固定位置的同時，將攝影機向上或向下傾斜。這改變了視角，但沒有移動攝影機本身的位置。

## 視野 (Field of View)

**FOV** 控制攝影機鏡頭的廣度。數值較低時，類似望遠鏡頭（視野窄，拉近）；數值較高時，類似廣角鏡頭（視野廣，更多透視失真）。

## 設定 (Configurations)

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
近, <b>遠</b>, </td></tr>
<tr><td><strong>目標選擇 (Target Select)</strong></td><td>選項</td><td>自動, 選取, 群組, 旋轉, 旋轉 + 群組, 舞台中心</td><td>自動</td><td></td><td></td></tr>
<tr><td><strong>追蹤模式 (Tracking Mode)</strong></td><td>選項</td><td>中心, 頭部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong>目標平滑度 (Target Smoothing)</strong></td><td>浮點數</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>預測 (Prediction)</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td>預測目標位置，以減少由平滑度引起的延遲</td></tr>
<tr><td><strong>鎖定目標 (Lock On Target)</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td>自動聚焦目標</td></tr>
<tr><td><strong>攝影機搖動 (Camera Shake)</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>鎖定旋轉 (Lock Rotation)</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td>攝影機跟隨目標的旋轉</td></tr>
<tr><td><strong>自動變焦 (Auto Zoom)</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td>自動放大和縮小，以在視圖中保持目標大小</td></tr>
<tr><td><strong>變焦速度 (Zoom Speed)</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td>變焦至目標 FOV 所需的時間</td></tr>
<tr><td><strong>目標 FOV 高度 (FOV Height At Target)</strong></td><td>浮點數</td><td>0.2 – 2</td><td>1</td><td></td><td>使用自動變焦時目標的垂直高度</td></tr>
<tr><td><strong>垂直偏移 (Vertical Offset)</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td>垂直偏移</td></tr>
<tr><td><strong>FOV</strong></td><td>浮點數</td><td>5 – 120</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>整數</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>大小 (Size)</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td>目標表演者在攝影機視圖中的大小。</td></tr>
<tr><td><strong>傾角 (Shift)</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td>將攝影機位置上下移動。</td></tr>
<tr><td><strong>目標中心 (Target Center)</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td>目標表演者焦點的中心位置。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>偏移 (Offset)</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>