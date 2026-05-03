---
layout: release
title: 圖形
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

# 圖形

控制 DanceXR 高動態範圍渲染管線 (HD 和 RT) 版本的所有渲染品質設定。選擇預設值可以獲得一個平衡的起點，然後調整個別功能以達到您需要的效能和視覺目標。


## 預設值

六種預設值涵蓋了常用的範圍：*效能* 會禁用反射和大多數螢幕空間效果；*中等* 會增加霧效和螢幕空間陰影；*高* 會啟用螢幕空間反射；*室內全域照明* 和 *室外全域照明* 分別在有或無天空貢獻下啟動全域照明；*網點過濾 + TAA* 將時間抗鋸齒與網點過濾透明度配對，以達到清晰的外觀。


## 抗鋸齒與超採樣

**抗鋸齒** 選擇了每攝影機的技術 — 無抗鋸齒、SMAA (延遲)、或 TAA。**超採樣** 在支援時解鎖 DLSS 或 FSR 上採樣，這可以在犧牲少量銳利度的代價下提升幀率。


## 反射

螢幕空間反射或平面反射探針。使用 *螢幕空間* 模式用於一般表面；對於地板或鏡子等平面，切換到 *探針* 模式。品質、邊緣衰減距離和備用行為可在子區塊中調整。


## 環境遮蔽與全域照明

**環境遮蔽** 在縫隙中增加接觸陰影，增加紮實的深度感。**全域照明** 增加間接彈跳光 — 啟用 *外場回退至天空*，以便面向光源背面的表面仍能接收到天空的顏色。


## 後處理效果

**景深** 會模糊追蹤演員周圍失焦的物體。**動態模糊** 在快速移動時增加基於速度的模糊。**泛光** 使明亮的亮點發出光暈。**鏡頭耀光** 在明亮光源進入視野時增加螢幕空間散射效果 — 在 VR 中禁用以避免不適。


## 霧

啟用體積霧效並設定其高度帶和最大渲染距離。霧的密度本身由燈光面板中的 **霧效** 滑桿控制。


## 色彩調整

色調映射、曝光、對比度、色相偏移、飽和度、濾色器、兩點色調曲線和白平衡都在此處。**色彩曲線** 將輸入亮度映射到輸出亮度；對於風格化的外觀或保護高光很有用。


## 選項

各種渲染旗標：**透明度預過載** 隱藏穿透透明表面的物體；**卡通著色** 將演員或舞台轉換為平面的漫畫風格；**網點過濾透明度** 對所有透明材質強制使用網點混合；**凹圖陰影** 為法線圖增加微陰影；**計算物體厚度** 啟用亞表面皮膚效果。


## 色調化

一種自定義過載效果，可以在最終畫面上增加輪廓、色調化的照明或半色網。對於日式動畫或漫畫風格很有用。

# 子元件

## 反射

設定螢幕空間反射或平面反射探針。

*螢幕空間* 模式會對深度緩衝區進行光線步進，以找到反射表面 — 它適用於任何幾何體，但無法反射攝影機視圖外的物體。對於地板或鏡子等平面，請切換到 *探針* 模式，該模式使用一個始終完整的平面捕獲，但會消耗更多效能。


### 算法

在 *螢幕空間* 模式下，*近似* 更快，適用於大多數表面；*PBR 累積* 對於粗糙材料更具物理準確性，但需要 TAA 才能清晰收斂。

**邊緣衰減距離** 衰減接近螢幕邊界處的反射以隱藏瑕疵；**物體厚度** 控制步進算法假設的表面深度。


### 天空反射與回退

**天空反射** 允許攝影機的天空對向上表面的反射做出貢獻。**外場回退至天空** 會為螢幕空間通道遺漏的區域填補反射探針的覆蓋範圍，但會犧牲一點準確度。
## 色調化

一個全螢幕自定義過載，在最終渲染的影像上應用風格化效果。四個內建預設值提供了快速的起點：*輪廓*、*黑白*、*色調化* 和 *半色網*。


### 輪廓

根據深度和法線的不連續性追蹤邊緣。控制 **輪廓厚度** 和 **輪廓強度** 以調整權重。與選項面板中的卡通著色結合使用，非常適合呈現漫畫動感的外觀。


### 量化照明與顏色

**量化照明** 減少影像中的亮度步數；較低的值（例如 4–8）會產生醒目的色調化外觀。**量化顏色** 對顏色通道執行同樣的操作，但它們是獨立的。將兩者都設為 0 即可完全禁用量化，只使用其他效果。


### 網點過濾與半色網

**網點過濾** 增加有序雜訊，分解平滑漸變中的帶狀紋。**半色網** 在圖上疊加網點圖案；增加 **半色網大小** 和 **強度** 以獲得復古印刷的美學。


## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
效能, 中等, <b >高</b>, 室內全域照明, 室外全域照明, 網點過濾 + TAA, </td></tr>
<tr><td><strong >抗鋸齒</strong></strong ></td><td>選項</td><td>無抗鋸齒, 延遲 SMAA, 延遲 TAA</td><td>延遲 SMAA</td><td></td><td></td></tr>
<tr><td><strong >超採樣</strong></strong ></td><td>選項</td><td>關閉, DLSS 效能, DLSS 平衡, DLSS 品質, DLSS 超效能, FSR 50%, FSR 66%, FSR 75%, FSR 100%</td><td>關閉</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >反射</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >模式</strong></strong ></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong >算法</strong></strong ></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td>螢幕空間反射算法。</td></tr>
<tr><td><strong >邊緣衰減距離</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong >物體厚度</strong></strong ></td><td>浮點數</td><td>0 – 0.1</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong >外場回退至天空</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>光線追蹤未命中時回退至天空顏色。</td></tr>
<tr><td><strong >天空反射</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >霧效</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >體積霧效</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td><strong >底高</strong></strong ></td><td>浮點數</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >最大高度</strong></strong ></td><td>浮點數</td><td>10 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong >最大距離</strong></strong ></td><td>浮點數</td><td>0 – 10000</td><td>5000</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >環境遮蔽</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong >強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >全域照明</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >外場回退至天空</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >景深</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong >偏移量</strong></strong ></td><td>浮點數</td><td>-1 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >動態模糊</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >泛光</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >品質</strong></strong ></td><td>整數</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong >強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >鏡頭耀光</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >VR 中禁用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>此效果不建議用於 VR</td></tr>
<tr><td><strong >強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >顏色</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設</td><td></td><td></td><td></td><td>
<b >白色</b>, 日落, 紅, 黃, 藍, 綠, </td></tr>
<tr><td><strong >顏色模式</strong></strong ></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >色相</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >飽和度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >亮度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >紅</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >綠</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >藍</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >使用舞台顏色</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>使用舞台環的顏色</td></tr>
<tr><td><strong >色溫</strong></strong ></td><td>浮點數</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong >耀斑</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >光束</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong >長度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong >色差</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >色彩調整</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >色調映射</strong></strong ></td><td>整數</td><td>0 – 3</td><td>3</td><td></td><td></td></tr>
<tr><td><strong >調整</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>啟用色彩調整。</td></tr>
<tr><td><strong >後曝光</strong></strong ></td><td>整數</td><td>-12 – 12</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >對比度</strong></strong ></td><td>浮點數</td><td>-100 – 100</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >色相偏移</strong></strong ></td><td>浮點數</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >飽和度</strong></strong ></td><td>浮點數</td><td>-100 – 100</td><td>1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >濾色器</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >顏色模式</strong></strong ></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >色相</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >飽和度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >亮度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >紅</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >綠</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >藍</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong >色彩曲線</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td><strong >起始梯度</strong></strong ></td><td>浮點數</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >起始位置</strong></strong ></td><td>浮點數</td><td>0 – 0.5</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >起始值</strong></strong ></td><td>浮點數</td><td>0 – 0.5</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >結束梯度</strong></strong ></td><td>浮點數</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >結束位置</strong></strong ></td><td>浮點數</td><td>0.5 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >結束值</strong></strong ></td><td>浮點數</td><td>0.5 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >白平衡</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>啟用白平衡。</td></tr>
<tr><td><strong >溫度</strong></strong ></td><td>浮點數</td><td>-100 – 100</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >色度</strong></strong ></td><td>浮點數</td><td>-100 – 100</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong >色調化</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong >啟用</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td>
輪廓, 黑白, <b >色調化</b>, 半色網, </td></tr>
<tr><td><strong >輪廓厚度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong >輪廓強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong >量化照明</strong></strong ></td><td>整數</td><td>0 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong >量化顏色</strong></strong ></td><td>整數</td><td>0 – 64</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >網點過濾</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong >半色網大小</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.25</td><td></td><td>半色網大小</td></tr>
<tr><td><strong >半色網強度</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td>半色網強度</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong >選項</strong></strong ></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >透明度預過載</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>啟用透明度預過載。這將使被遮擋的透明材質隱形。</td></tr>
<tr><td><strong >螢幕空間陰影</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
<tr><td><strong >接觸陰影</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>用於微小細節的陰影。</td></tr>
<tr><td><strong >凹圖陰影</strong></strong ></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td>啟用凹圖和細節圖的陰影。</td></tr>
<tr><td><strong >阻止 NaN</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>防止後處理發生錯誤時出現黑屏。 </td></tr>
<tr><td><strong >計算物體厚度</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>開啟</td><td></td><td>計算可用於皮膚效果的厚度。</td></tr>
<tr><td><strong >演員模型卡通著色</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>對所有演員使用卡通著色。</td></tr>
<tr><td><strong >舞台模型卡通著色</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td>對舞台和道具使用卡通著色。</td></tr>
<tr><td><strong >網點過濾透明度</strong></strong ></td><td>開關</td><td>開啟 / 關閉</td><td>關閉</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>