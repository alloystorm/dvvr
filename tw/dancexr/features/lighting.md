---
layout: release
title: 照明
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

# 照明

控制所有場景的照明——包含方向性太陽、最多三組獨立光源，以及全局亮度控制。內建預設提供了即時可用的完整外觀；之後所有參數均可自由調整。


## 預設值

內建預設值（例如 *Sunset*、*Daylight*、*Window*、*Stage*、*Projector* 等）可以在一鍵內建立完整的照明佈局。請先套用最接近的預設值，再從中調整各個獨立光源組。


## 整體亮度與天空環境光

**整體亮度**會一同縮放所有光源組和太陽的亮度，讓您只需一個滑桿即可推高或拉低整個場景的亮度。**天空環境光**控制著間接天光；提高此值會照亮陰影區域，減少強烈對比度，尤其在戶外場景中效果明顯。


## 太陽光

**天體**子區塊控制方向性太陽（在 HDRP 中控制月亮）。一天中的時間、朝向和黃道角度決定了太陽在天空的位置以及由此產生的陰影方向。


## 附加光源組

**附加 1**、**2** 和 **3** 是獨立、可完全配置的光源組——通常用於主光、補光和邊光。每個組件都可以是聚光燈、點光源、區域光源或投影儀，並且可以動態追蹤動作演員。


## 霧效

在攝影機和場景之間增加了深度霧化效果。低數值提供微妙的環境提示；較高的數值則能戲劇性地改變氛圍。霧效會與體積光錐相互作用，產生戲劇性的光束效果。


## 光與影限制

**光限制**限制了同時渲染的活動光源數量。**陰影限制**限制了投射陰影的子集——陰影成本較高，除非性能允許，否則請保持此數值較低（1–4）。


## 分配 (Allocation)

當光源組使用 *跟隨演員* 或 *保持距離* 等動態時，**分配**控制光源如何分配到多個舞者身上。*按距離*會最小化總位移，使效果自然；*按索引（固定）*則將光源固定在特定的演員插槽上。**刷新間隔**設定了重新分配之間經過的拍子數。

# 子組件

## 太陽光

控制方向性太陽（在 HDRP 中，也控制月亮和夜空）。太陽位置由一天中的時間、朝向和黃道角度定義，可為陰影方向和天空顏色提供完整的創作控制。


### 太陽位置


**一天中的時間**將太陽沿著弧線移動（0–24小時）。

**朝向**設定太陽升起的指南針方向。

**黃道角度**傾斜了軌道平面——這對於在沒有精確太陽追蹤的情況下匹配特定的地點或季節非常有用。


### 亮度與顏色


**太陽光強度**和**色溫**控制著方向性光的原始亮度與暖度。由於太陽光非常強大，啟用此光源的場景通常需要更高的曝光值或較低的整體亮度，以避免過曝。


### 月亮與夜空 (HDRP)


在 HDRP 中，同一個子區塊控制月亮的位置、週期和地球光，還包括星星和極光的亮度。對於夜景，請關閉太陽光並提高月光強度。


### 窗戶效果 (Window Effect)


**窗戶**子區塊會投射出模擬穿過窗格的矩形陰影網格。調整寬度、高度、行數和列數以匹配想像的房間內部。*天空光* 選項會增加來自相同方向的柔和補光，以補充陰影。


## 附加 1

一個可配置的光源組，可定位在相機場景或演員相對的位置。照明設定中可提供三個光源組，通常用於主光、補光和邊光，但每個組件都是透過此子區塊配置的。


### 類型與紋理 (Type & Cookie)


**類型**選擇光源形狀：聚光燈、點光源、區域光源、金字塔形或箱體投影儀。**紋理**會在光束中投射圖案（窗戶、百葉窗、光點、管狀、視頻）。設定**發射器半徑**以柔化錐體或紋理的邊緣，並使用 **可見** 來控制光源本身在渲染中看起來的亮度。


### 位置與朝向


**距離**和**高度**將光源放置在相對於目標物的位置，**角度**向下傾斜它，而**朝向**則沿垂直軸旋轉它。對於聚光燈類型，**寬度 X / Y**會擴大光束的橫截面；**錐體長度**控制體積散射深度。


### 動態 (Dynamics)


**動態**決定光源是保持固定（*靜止*）、圍繞指定的演員運行（*跟隨演員* / *後方演員*），還是沿著設定的半徑移動（*保持距離*）。啟用 **使用演員位置** 可以將光源的方向性設定為相對於演員的朝向。演員指派由上層照明面板中的分配設定處理。


### 重複 (Array)


**重複**子區塊將光源擴展成一個陣列。選擇 *圓形* 陣列來形成舞台光束環，或選擇 *網格* 陣列來進行天花板設備佈局。像 *4x Fan* 或 *8x Circle* 這樣的預設值可以在一步操作中設定陣列。


### 懸掛 (Suspension)


啟用 **懸掛** 將光源懸掛在虛擬懸掛點，使其產生緩慢的鐘擺擺動。**段數**設定了纜線關節的數量，**懸掛距離**設定了下降長度，**擺動速度**則控制了其保持擺動弧度的活躍程度。


### 陰影


每個光源組都有獨立的陰影控制。將模式保留為預設值，以繼承全局場景的品質；或者覆蓋它以強制對此組件應用光線追蹤或螢幕空間陰影。**陰影調光器**可以在不完全禁用陰影的情況下柔化陰影。


## 附加 2

一個可配置的光源組，可定位在相機場景或演員相對的位置。照明設定中可提供三個光源組，通常用於主光、補光和邊光，但每個組件都是透過此子區塊配置的。


### 類型與紋理 (Type & Cookie)


**類型**選擇光源形狀：聚光燈、點光源、區域光源、金字塔形或箱體投影儀。**紋理**會在光束中投射圖案（窗戶、百葉窗、光點、管狀、視頻）。設定**發射器半徑**以柔化錐體或紋理的邊緣，並使用 **可見** 來控制光源本身在渲染中看起來的亮度。


### 位置與朝向


**距離**和**高度**將光源放置在相對於目標物的位置，**角度**向下傾斜它，而**朝向**則沿垂直軸旋轉它。對於聚光燈類型，**寬度 X / Y**會擴大光束的橫截面；**錐體長度**控制體積散射深度。


### 動態 (Dynamics)


**動態**決定光源是保持固定（*靜止*）、圍繞指定的演員運行（*跟隨演員* / *後方演員*），還是沿著設定的半徑移動（*保持距離*）。啟用 **使用演員位置** 可以將光源的方向性設定為相對於演員的朝向。演員指派由上層照明面板中的分配設定處理。


### 重複 (Array)


**重複**子區塊將光源擴展成一個陣列。選擇 *圓形* 陣列來形成舞台光束環，或選擇 *網格* 陣列來進行天花板設備佈局。像 *4x Fan* 或 *8x Circle* 這樣的預設值可以在一步操作中設定陣列。


### 懸掛 (Suspension)


啟用 **懸掛** 將光源懸掛在虛擬懸掛點，使其產生緩慢的鐘擺擺動。**段數**設定了纜線關節的數量，**懸掛距離**設定了下降長度，**擺動速度**則控制了其保持擺動弧度的活躍程度。


### 陰影


每個光源組都有獨立的陰影控制。將模式保留為預設值，以繼承全局場景的品質；或者覆蓋它以強制對此組件應用光線追蹤或螢幕空間陰影。**陰影調光器**可以在不完全禁用陰影的情況下柔化陰影。


## 附加 3

一個可配置的光源組，可定位在相機場景或演員相對的位置。照明設定中可提供三個光源組，通常用於主光、補光和邊光，但每個組件都是透過此子區塊配置的。


### 類型與紋理 (Type & Cookie)


**類型**選擇光源形狀：聚光燈、點光源、區域光源、金字塔形或箱體投影儀。**紋理**會在光束中投射圖案（窗戶、百葉窗、光點、管狀、視頻）。設定**發射器半徑**以柔化錐體或紋理的邊緣，並使用 **可見** 來控制光源本身在渲染中看起來的亮度。


### 位置與朝向


**距離**和**高度**將光源放置在相對於目標物的位置，**角度**向下傾斜它，而**朝向**則沿垂直軸旋轉它。對於聚光燈類型，**寬度 X / Y**會擴大光束的橫截面；**錐體長度**控制體積散射深度。


### 動態 (Dynamics)


**動態**決定光源是保持固定（*靜止*）、圍繞指定的演員運行（*跟隨演員* / *後方演員*），還是沿著設定的半徑移動（*保持距離*）。啟用 **使用演員位置** 可以將光源的方向性設定為相對於演員的朝向。演員指派由上層照明面板中的分配設定處理。


### 重複 (Array)


**重複**子區塊將光源擴展成一個陣列。選擇 *圓形* 陣列來形成舞台光束環，或選擇 *網格* 陣列來進行天花板設備佈局。像 *4x Fan* 或 *8x Circle* 這樣的預設值可以在一步操作中設定陣列。


### 懸掛 (Suspension)


啟用 **懸掛** 將光源懸掛在虛擬懸掛點，使其產生緩慢的鐘擺擺動。**段數**設定了纜線關節的數量，**懸掛距離**設定了下降長度，**擺動速度**則控制了其保持擺動弧度的活躍程度。


### 陰影


每個光源組都有獨立的陰影控制。將模式保留為預設值，以繼承全局場景的品質；或者覆蓋它以強制對此組件應用光線追蹤或螢幕空間陰影。**陰影調光器**可以在不完全禁用陰影的情況下柔化陰影。


## 自動曝光 (Auto Exposure)

HDRP 的自動曝光設定，用於控制攝影機如何適應場景亮度變化。當此功能禁用時，攝影機使用由全局亮度滑桿控制的固定曝光；當啟用時，它會根據場景亮度持續調整。


### 計測模式 (Metering Mode)


決定採樣畫面的哪個部分來測量亮度。*平均* 會均勻讀取整個畫面；*光點* 只讀取中心區域；*加權中心* 則強調中心區域，同時包含周邊。當明亮的背景可能會導致主題看起來過暗時，請使用 *光點* 或 *加權中心*。


### 補償與範圍 (Compensation & Range)


**補償**將目標曝光值向上或向下移動 EV 級別。**範圍**限制了允許的最低和最高曝光值，防止攝影機在黑色場景中過暗或在過曝環境中過亮。


### 適應度 (Adaptation)


控制曝光在照明條件改變時改變的速度。*正常* 提供平穩、具電影感的響應；*快速* 對突然的變化作出迅速反應；*即時* 則無延遲地跳轉到新的曝光值。
## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
日落, <b>日光</b>, 窗戶, 舞台, 剪影, 投影機, 區域光, 點光陣列, </td></tr>
<tr><td colspan="6"><details>
<summary><strong>太陽 / 月亮 / 時間</strong> — <em>用於模擬日光設定。請注意，日光非常明亮，需要更高的曝光值。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>黃道角</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td>地平線與太陽運動所在平面的角度之間的夾角。</td></tr>
<tr><td><strong>方向</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>時間</strong></td><td>Float</td><td>0 – 24</td><td>9</td><td></td><td>在特定時間設定太陽角度（小時）。</td></tr>
<tr><td><strong>太陽</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>啟用或停用太陽。</td></tr>
<tr><td><strong>陽光強度</strong></td><td>Float</td><td>0 – 200</td><td>100</td><td></td><td>太陽的亮度。</td></tr>
<tr><td><strong>色溫</strong></td><td>Float</td><td>1000 – 20000</td><td>6500</td><td></td><td>日光色溫。</td></tr>
<tr><td><strong>點源半徑</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>這會影響程序化天空中的太陽圓盤大小和陰影的柔和度。</td></tr>
<tr><td><strong>體積乘數</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>月亮</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>啟用或停用月亮。</td></tr>
<tr><td><strong>月光強度</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>月亮的亮度。</td></tr>
<tr><td><strong>月亮位置</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>月亮在天空中的位置。</td></tr>
<tr><td><strong>月相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>月相，其中 0 為新月，1 為滿月。</td></tr>
<tr><td><strong>地球暉</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>月亮上地球輝的亮度。</td></tr>
<tr><td><strong>月相旋轉</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>月相的旋轉。</td></tr>
<tr><td><strong>恆星</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>恆星的亮度。</td></tr>
<tr><td><strong>極光</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>極光的亮度。</td></tr>
<tr><td colspan="6"><details>
<summary><strong>窗戶</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>寬度</strong></td><td>Float</td><td>0 – 16</td><td>8</td><td></td><td>當啟用捲餅圖時的窗戶寬度。</td></tr>
<tr><td><strong>高度</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>當啟用捲餅圖時的窗戶高度。</td></tr>
<tr><td><strong>底部</strong></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>位置</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>-2</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>行數</strong></td><td>Integer</td><td>0 – 8</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>列數</strong></td><td>Integer</td><td>0 – 8</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>間距 X</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>間距 Y</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>可見</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>在場景中顯示窗戶。</td></tr>
<tr><td><strong>來源</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>天空光</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td>天空光的亮度。</td></tr>
<tr><td><strong>天空光角度</strong></td><td>Float</td><td>0 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>天空光陰影</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>為天空光啟用陰影。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>陰影</strong> — <em>陰影設定。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>模式</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接觸陰影</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>為小細節啟用陰影。</td></tr>
<tr><td><strong>樣本計數</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>使用光線追蹤陰影時的樣本計數。數字越高 = 結果越好，但效能越差。</td></tr>
<tr><td><strong>去噪</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用光線追蹤陰影時啟用去噪。</td></tr>
<tr><td><strong>去噪半徑</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>陰影減光器</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>減低陰影的強度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>鏡頭光暈</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>啟用鏡頭光暈</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>附加 1</strong> — <em>配置光源組 1</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>聚光燈</b>, 點光源, 區域光源, 錐體投影機近, 錐體投影機遠, 方體投影機近, 方體投影機遠, 聚光燈陣列, 懸掛聚光燈, </td></tr>
<tr><td><strong>體積乘數</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>類型</strong></td><td>Options</td><td>聚光燈, 點光源, 區域光源, 錐體, 方體</td><td>聚光燈</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 紅色, 黃色, 藍色, 綠色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>使用舞台顏色</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用舞台環的顏色。</td></tr>
<tr><td><strong>色溫</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>遮光片</strong></td><td>Options</td><td>[無], [窗戶], [百葉窗], [聚光], [管狀], [影片]</td><td>[無]</td><td></td><td></td></tr>
<tr><td><strong>發射器半徑</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong>尺寸 X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>尺寸 Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可見</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染時的亮度。設定為 0 可使其不可見。</td></tr>
<tr><td><strong>錐體長度</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>體積光源錐體的長度。</td></tr>
<tr><td><strong>方向</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高度</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>光線的位置高度。</td></tr>
<tr><td><strong>動態</strong></td><td>Options</td><td>靜止, 跟隨角色, 後方角色, 維持距離</td><td>維持距離</td><td></td><td></td></tr>
<tr><td><strong>最大跟隨距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>懸掛</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>懸掛節段數</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>啟用懸掛效果。</td></tr>
<tr><td><strong>懸掛距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>擺動速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>控制維持擺動動作的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>使用角色位置</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用角色的位置和方向來定位光源。</td></tr>
<tr><td><strong>目標高度</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>鏡頭光暈</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>重複</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>關閉</b>, 3x3 網格, 2x 扇形, 4x 扇形, 4x 環形, 8x 環形, </td></tr>
<tr><td><strong>數量</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>陣列中的光源數量。</td></tr>
<tr><td><strong>排列</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>使用網格或環形排列。</td></tr>
<tr><td><strong>間距 / 半徑</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>網格模式中光源之間的距離。</td></tr>
<tr><td><strong>範圍</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>環形模式中光源的角度範圍。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>陰影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>模式</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接觸陰影</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>為小細節啟用陰影。</td></tr>
<tr><td><strong>樣本計數</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>使用光線追蹤陰影時的樣本計數。數字越高 = 結果越好，但效能越差。</td></tr>
<tr><td><strong>去噪</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用光線追蹤陰影時啟用去噪。</td></tr>
<tr><td><strong>去噪半徑</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>陰影減光器</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>降低陰影的強度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>附加 2</strong> — <em>配置光源組 2</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>聚光燈</b>, 點光源, 區域光源, 錐體投影機近, 錐體投影機遠, 方體投影機近, 方體投影機遠, 聚光燈陣列, 懸掛聚光燈, </td></tr>
<tr><td><strong>體積乘數</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>類型</strong></td><td>Options</td><td>聚光燈, 點光源, 區域光源, 錐體, 方體</td><td>聚光燈</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 紅色, 黃色, 藍色, 綠色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>使用舞台顏色</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用舞台環的顏色。</td></tr>
<tr><td><strong>色溫</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>遮光片</strong></td><td>Options</td><td>[無], [窗戶], [百葉窗], [聚光], [管狀], [影片]</td><td>[無]</td><td></td><td></td></tr>
<tr><td><strong>發射器半徑</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong>尺寸 X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>尺寸 Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可見</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染時的亮度。設定為 0 可使其不可見。</td></tr>
<tr><td><strong>錐體長度</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>體積光源錐體的長度。</td></tr>
<tr><td><strong>方向</strong></td><td>Float</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高度</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>光線的位置高度。</td></tr>
<tr><td><strong>動態</strong></td><td>Options</td><td>靜止, 跟隨角色, 後方角色, 維持距離</td><td>維持距離</td><td></td><td></td></tr>
<tr><td><strong>最大跟隨距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>懸掛</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>懸掛節段數</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>啟用懸掛效果。</td></tr>
<tr><td><strong>懸掛距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>擺動速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>控制維持擺動動作的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>使用角色位置</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用角色的位置和方向來定位光源。</td></tr>
<tr><td><strong>目標高度</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>鏡頭光暈</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>重複</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>關閉</b>, 3x3 網格, 2x 扇形, 4x 扇形, 4x 環形, 8x 環形, </td></tr>
<tr><td><strong>數量</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>陣列中的光源數量。</td></tr>
<tr><td><strong>排列</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>使用網格或環形排列。</td></tr>
<tr><td><strong>間距 / 半徑</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>網格模式中光源之間的距離。</td></tr>
<tr><td><strong>範圍</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>環形模式中光源的角度範圍。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>陰影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>模式</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接觸陰影</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>為小細節啟用陰影。</td></tr>
<tr><td><strong>樣本計數</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>使用光線追蹤陰影時的樣本計數。數字越高 = 結果越好，但效能越差。</td></tr>
<tr><td><strong>去噪</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用光線追蹤陰影時啟用去噪。</td></tr>
<tr><td><strong>去噪半徑</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>陰影減光器</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>降低陰影的強度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>附加 3</strong> — <em>配置光源組 3</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>聚光燈</b>, 點光源, 區域光源, 錐體投影機近, 錐體投影機遠, 方體投影機近, 方體投影機遠, 聚光燈陣列, 懸掛聚光燈, </td></tr>
<tr><td><strong>體積乘數</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>類型</strong></td><td>Options</td><td>聚光燈, 點光源, 區域光源, 錐體, 方體</td><td>聚光燈</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 紅色, 黃色, 藍色, 綠色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍色</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>使用舞台顏色</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用舞台環的顏色。</td></tr>
<tr><td><strong>色溫</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>遮光片</strong></td><td>Options</td><td>[無], [窗戶], [百葉窗], [聚光], [管狀], [影片]</td><td>[無]</td><td></td><td></td></tr>
<tr><td><strong>發射器半徑</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong>尺寸 X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>尺寸 Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可見</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染時的亮度。設定為 0 可使其不可見。</td></tr>
<tr><td><strong>錐體長度</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>體積光源錐體的長度。</td></tr>
<tr><td><strong>方向</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高度</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>光線的位置高度。</td></tr>
<tr><td><strong>動態</strong></td><td>Options</td><td>靜止, 跟隨角色, 後方角色, 維持距離</td><td>維持距離</td><td></td><td></td></tr>
<tr><td><strong>最大跟隨距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>懸掛</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>懸掛節段數</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>啟用懸掛效果。</td></tr>
<tr><td><strong>懸掛距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>擺動速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>控制維持擺動動作的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>使用角色位置</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用角色的位置和方向來定位光源。</td></tr>
<tr><td><strong>目標高度</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>鏡頭光暈</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>重複</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>關閉</b>, 3x3 網格, 2x 扇形, 4x 扇形, 4x 環形, 8x 環形, </td></tr>
<tr><td><strong>數量</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>陣列中的光源數量。</td></tr>
<tr><td><strong>排列</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>使用網格或環形排列。</td></tr>
<tr><td><strong>間距 / 半徑</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>網格模式中光源之間的距離。</td></tr>
<tr><td><strong>範圍</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>環形模式中光源的角度範圍。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>陰影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>模式</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接觸陰影</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>為小細節啟用陰影。</td></tr>
<tr><td><strong>樣本計數</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>使用光線追蹤陰影時的樣本計數。數字越高 = 結果越好，但效能越差。</td></tr>
<tr><td><strong>去噪</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用光線追蹤陰影時啟用去噪。</td></tr>
<tr><td><strong>去噪半徑</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>陰影減光器</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>降低陰影的強度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>總體強度</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>整體強度</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>所有光源的整體強度。</td></tr>
<tr><td><strong>天空環境光</strong></td><td>Float</td><td>0 – 14</td><td>1</td><td></td><td>來自天空的環境光強度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>自動曝光</strong> — <em>自動曝光設定。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>Toggle</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>測光模式</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td>選擇測光模式。</td></tr>
<tr><td><strong>補償</strong></td><td>Integer</td><td>0 – 24</td><td>12</td><td></td><td></td></tr>
<tr><td><strong>範圍</strong></td><td>Range</td><td>0 – 15</td><td></td><td></td><td></td></tr>
<tr><td><strong>適應</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td>照明條件變化時，自動曝光等級的變化速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>霧氣</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>霧氣等級</td></tr>
<tr><td><strong>光源限制</strong></td><td>Integer</td><td>0 – 16</td><td>8</td><td></td><td>設定場景中可用的最大光源數量。</td></tr>
<tr><td><strong>陰影限制</strong></td><td>Integer</td><td>0 – 16</td><td>4</td><td></td><td>設定可產生陰影的最大光源數量。</td></tr>
<tr colspan="6"><details>
<summary><strong>分配</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>自動分配</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>刷新間隔</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>每隔多久重新分配一次光源。單位為拍。</td></tr>
<tr><td><strong>手動刷新</strong></td><td>Action</td><td></td><td></td><td></td><td>強制重新分配光源。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>