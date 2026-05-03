---
layout: release
title: 環繞式攝影機
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

# 環繞式攝影機

手動和自動環繞攝影機，會在聚焦的演員周圍旋轉。

## 手動控制

當未處於自動模式時，拖動以將攝影機環繞演員。
**使用控制器輸入** 開啟遊戲手柄/VR 控制器來支持環繞功能。
**防止低於地板** 可防止攝影機移動到地面平面下方。

**保持速度** 在釋放輸入後，使攝影機繼續旋轉，逐漸減速。**最小速度** 和 **最大速度** 會限制保留的旋轉速度——如果需要長篇電影般的環繞，請提高 *最大速度*；如果需要更緊湊的控制，則降低它。

## 自動模式

當啟用時，攝影機會自動環繞，其距離、俯仰角和高度是可配置的，並使用正弦波循環變化。

**距離最小** 和 **距離最大** 設定了攝影機在每個循環中經過的近/遠範圍。**距離循環** 是完整一次來回循環的週期（以秒為單位）。

**俯仰最小** 和 **俯仰最大** 控制垂直角度範圍，而 **俯仰循環** 設定了攝影機上下傾斜的速度。

**高度最小** 和 **高度最大** 調整了攝影機目標的垂直偏移量，**高度循環** 控制振盪週期。

**速度** 設定了自動模式激活時攝影機水平環繞的速度。提高此值以實現快速掃描鏡頭，或降低此值以實現緩慢、刻意的圓圈移動。


## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
預設（重設）</td></tr>
<tr><td><strong>目標選擇</strong></td><td>選項</td><td>自動, 選取, 群組, 旋轉, 旋轉 + 群組, 舞台中心</td><td>自動</td><td></td><td></td></tr>
<tr><td><strong>追蹤模式</strong></td><td>選項</td><td>中心, 頭部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong>目標平滑</strong></td><td>浮點數</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>預測</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td>預測目標位置以減少平滑引起的延遲</td></tr>
<tr><td><strong>FOV</strong></td><td>浮點數</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>節拍週期</strong></td><td>整數</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>使用控制器輸入</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td><strong>防止低於地板</strong></td><td>開關</td><td>開 / 關</td><td>開</td><td></td><td></td></tr>
<tr><td><strong>保持速度</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td>在沒有輸入時維持旋轉</td></tr>
<tr><td><strong>最大速度</strong></td><td>浮點數</td><td>0 – 30</td><td>15</td><td></td><td>最大旋轉速度</td></tr>
<tr><td><strong>最小速度</strong></td><td>浮點數</td><td>0 – 30</td><td>0</td><td></td><td>最小旋轉速度</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>自動模式</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>距離最小</strong></td><td>浮點數</td><td>0 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>距離最大</strong></td><td>浮點數</td><td>1 – 10</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>距離循環</strong></td><td>浮點數</td><td></td><td>12</td><td></td><td></td></tr>
<tr><td><strong>俯仰最小</strong></td><td>浮點數</td><td>-45 – 0</td><td>-15</td><td></td><td></td></tr>
<tr><td><strong>俯仰最大</strong></td><td>浮點數</td><td>0 – 45</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>俯仰循環</strong></td><td>浮點數</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>高度最小</strong></td><td>浮點數</td><td>-1 – 0</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>高度最大</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>高度循環</strong></td><td>浮點數</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>速度</strong></td><td>浮點數</td><td>0 – 90</td><td>10</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>