---
layout: release
title: ./motion/proc/auto_cam
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

# ./motion/proc/auto_cam

自動攝影機系統，能產生與音樂節拍和演員動作同步的電影式攝影機運動。

## Distance

**距離近** (Distance Near) 和 **距離遠** (Distance Far) 定義了攝影機可以從目標處的範圍。
範圍越窄，攝影機保持的距離越一致；範圍越寬，則能增加不同鏡頭之間的變化性。實際的距離也會受到下方 *目標選擇* 的機率影響。

## Target Selection

控制攝影機聚焦的身體部位。每個數值都是一個相對機率——數字越高，該目標被選擇的可能性越大。**頭部** (Head) 和 **胸部** (Chest) 適合近景特寫，而 **中心** (Center) 和 **腿部** (Legs) 則適合較廣闊的鏡頭。將數值設定為 *0* 可完全排除該目標。

## Distance Selection

描述攝影機自身定位距離的機率。**特寫** (Close Up) 會用演員填滿畫面，**拉近** (Zoom In) 和 **拉遠** (Zoom Out) 在鏡頭過程中在不同距離之間過渡，**中景** (Middle) 提供平衡的視角，而 **远景** (Far) 則捕捉整個場景。這裡只關心相對比例——最終距離仍會受上方 *距離* 範圍的限制。

## Path & Angles

**高角度** (High Angle) 和 **低角度** (Low Angle) 限制了攝影機向上或向下傾斜的最大範圍。數值越低，攝影機的水平感越強，看起來更為自然；範圍越大，則能營造戲劇性的頂視或蟲眼視角。

## Orientation

決定了攝影機拍攝的演員身體的側向。**正前中心** (Front Center) 正對著演員，**前右 45** (Front 45) 和 **側右 90** (Side 90) 從側邊拍攝，而 **後方 180** (Back 180) 則從背後拍攝。混合使用這些角度，可以讓攝影機運動更具視覺趣味。

## Effects

**淡出至黑屏** (Fade To Black) 設定了在鏡頭過渡過程中畫面淡出至黑屏的時間長度，而 **F2B 機率** (F2B Probability) 控制了此現象發生的頻率。使用這些參數可以在鏡頭間增加電影感的剪切效果。

**音訊敏感度** (Audio Sensitivity) 在啟用時，會使攝影機運動對音樂音量作出反應。數值越高，在音量較大的段落，攝影機運動會越快。

## Random Seed

**種子** (Seed) 值控制著攝影機運動的隨機數生成器。更改此值可以在保持所有其他設定不變的情況下，獲得不同的攝影機序列，或者將其設定為 *-1* 以每次生成一個新的隨機種子。


## Configurations

<table>
<thead><tr><th>設定項</th><th>類型</th><th>範圍 / 數值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設集</td><td></td><td></td><td></td><td></td><td>預設 (重置)</td></tr>
<tr><td><strong>目標選擇</strong></td><td>選項</td><td>自動 (Auto)、選擇 (Selected)、群體 (Group)、旋轉 (Rotate)、旋轉 + 群體 (Rotate + Group)、舞台中心 (Stage Center)</td><td>自動 (Auto)</td><td></td><td></td></tr>
<tr><td><strong>追蹤模式</strong></td><td>選項</td><td>中心 (Center)、頭部 (Head)、胸部 (Chest)</td><td>中心 (Center)</td><td></td><td></td></tr>
<tr><td><strong>目標平滑度</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>預測</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>1</td><td></td><td>用來預測目標位置，以減少平滑度造成的延遲</td></tr>
<tr><td><strong>視場角 (FOV)</strong></td><td>浮點數 (Float)</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>節拍週期</strong></td><td>整數 (Integer)</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>距離近</strong></td><td>浮點數 (Float)</td><td>0.5 – 3</td><td>1.5</td><td></td><td>攝影機到目標的最小距離。</td></tr>
<tr><td><strong>距離遠</strong></td><td>浮點數 (Float)</td><td>0.5 – 3</td><td>2.5</td><td></td><td>攝影機到目標的最大距離。</td></tr>
<tr><td><strong>使用演員朝向</strong></td><td>開關 (Toggle)</td><td>開/關 (on / off)</td><td>開 (on)</td><td></td><td>啟用或停用攝影機對齊到演員朝向。</td></tr>
<tr><td><strong>種子</strong></td><td>浮點數 (Float)</td><td></td><td>1234</td><td></td><td>用來生成隨機攝影機運動的種子值。</td></tr>
<tr><td><strong>淡出至黑屏</strong></td><td>浮點數 (Float)</td><td>0 – 0.25</td><td>0</td><td></td><td>過渡過程淡出至黑屏的持續時間。</td></tr>
<tr><td><strong>F2B 機率</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td>觸發淡出至黑屏效果的機率。</td></tr>
<tr><td><strong>音訊敏感度</strong></td><td>浮點數 (Float)</td><td>0 – 4</td><td>1</td><td></td><td>攝影機運動對音訊音量等級的敏感度。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>目標選擇</strong></summary>
<table><tbody>
<thead><tr><th>設定項</th><th>類型</th><th>範圍 / 數值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設集</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>頭部</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td>目標鎖定演員頭部的機率。</td></tr>
<tr><td><strong>胸部</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td>目標鎖定演員胸部的機率。</td></tr>
<tr><td><strong>中心</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td>目標鎖定演員中心的機率。</td></tr>
<tr><td><strong>腿部</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td>目標鎖定演員腿部的機率。</td></tr>
<tr><td><strong>腳部</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td>目標鎖定演員腳部的機率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>距離選擇</strong></summary>
<table><tbody>
<thead><tr><th>設定項</th><th>類型</th><th>範圍 / 數值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設集</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>特寫</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td>特寫攝影機距離的機率。</td></tr>
<tr><td><strong>拉近</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>拉近的機率。</td></tr>
<tr><td><strong>拉遠</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>拉遠的機率。</td></tr>
<tr><td><strong>中景</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>中景攝影機距離的機率。</td></tr>
<tr><td><strong>远景</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>遠景攝影機距離的機率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>路徑選擇</strong></summary>
<table><tbody>
<thead><tr><th>設定項</th><th>類型</th><th>範圍 / 數值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設集</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>高角度</strong></td><td>浮點數 (Float)</td><td>0 – 30</td><td>20</td><td></td><td>攝影機最大的向上角度。</td></tr>
<tr><td><strong>低角度</strong></td><td>浮點數 (Float)</td><td>-30 – 0</td><td>-20</td><td></td><td>攝影機最大的向下角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>朝向</strong></summary>
<table><tbody>
<thead><tr><th>設定項</th><th>類型</th><th>範圍 / 數值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設集</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>正前中心</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td>目標鎖定演員正前中心的機率。</td></tr>
<tr><td><strong>前右 45</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td>目標鎖定演員前方 45 度角度的機率。</td></tr>
<tr><td><strong>側右 90</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>目標鎖定演員側方 90 度角度的機率。</td></tr>
<tr><td><strong>後方 135</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td>目標鎖定演員後方 135 度角度的機率。</td></tr>
<tr><td><strong>後方 180</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td>目標鎖定演員正後方的機率。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>