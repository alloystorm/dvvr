---
layout: release
title: 地面
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

# 地面

控制場景所坐的地面和周圍舞台 — 包括地面表面、程序化舞台和泳池幾何體，以及（在 HDRP 中）水系統。一套預設值將這些子功能組合成一鍵式造型，例如 *木材*、*舞台*、*泳池*、*海洋* 和 *音頻視覺化器*。


## 地面高度

舞台中心的垂直偏移量，單位為米。您可以使用此功能將地板與追蹤的表演區域或捕捉的場景對齊，以防止演員沉入或漂浮在地面之上。其他錨點（連接到舞台的燈光、攝影機）都會遵循此偏移量。


## 地面設定

定義地板本身的一個子群組 — 包括其表面材質、半徑和舞台感知的可見性。有關詳細資訊，請參閱下方的 *地面* 群組。


## 舞台幾何體

環繞地面圓盤的程序化舞台、紅毯、牆壁和內部泳池深槽。有關詳細資訊，請參閱下方的 *舞台/泳池* 群組。舞台幾何體與地面圓盤結合 — 兩者可以同時顯示。


## 水系統 (HDRP)

僅限 HDRP 的水表面，錨定在舞台中心，用於海洋和泳池預設值。有關詳細資訊，請參閱下方的 *水系統* 群組。每當舞台幾何體改變時都會重新應用，確保水體能追蹤泳池深槽。在 URP 上不可用 — 相反，水著色器全域變數會被清除。


## 預設值

預設值列表將子功能組合為命名的外觀。選擇一個預設值可以在一步內切換地面開關、選擇地板表面、並選擇舞台幾何體和水體變體。預設值是快速切換平坦地板、紅毯舞台、泳池、海洋、音頻視覺化器地板、投影螢幕或 LED 箱最快的方式。

# 子組件

## 地面

場景所坐的平坦地面圓盤。將其切換關閉會完全隱藏地面（當舞台道具或 AR passthrough 應該接管時非常有用）。**半徑** 設置圓盤的大小 — 對於戶外場景，半徑需要足夠大以填充可見地平線；對於較緊湊的室內場景則較小。**舞台存在時隱藏** 會在載入具有 *舞台* 目的的演員時自動抑制地面，這樣實體舞台模型就不會疊加在程序化圓盤之上。**表面** 子群組選擇地板材質 — 紋理瓷磚、天空投影穹頂或實心顏色 — 它也與父級的預設值包共享預設值列表。

## 舞台/泳池

從紅毯板加上可選的外牆、內部深槽和後牆組成的程序化舞台 — 用於紅毯、泳池、房間、投影螢幕和 LED 箱。內建預設值涵蓋了常見的造型；下面的欄位讓您可以對其進行調整。


### 位置


**提升高度** 將舞台提升到地面上方或沉降到下方；負值提升高度會在地面圓盤上挖出一個孔，以便內部深槽能裝水。**前後偏移** 沿 Z 軸將整個舞台向前或向後移動，有助於與追蹤的表演區域對齊。


### 幾何體


**幾何體** 子群組調整板材的大小。**中心寬度** / **中心深度** 定義了主矩形；**側/前/後延伸** 在其外增加了紅毯區段。**牆壁高度** 和 **牆壁厚度** 控制環繞周邊的邊緣 — 將牆壁高度設置為 0 可獲得齊平平台。**後牆高度** 會在舞台後方抬起一個垂直板，用於背景和投影螢幕。**漂浮** 將板材從地面幾何體上分離，使其可以在水面上放置，避免 Z 軸戰鬥（z-fighting）。


### 表面


三個獨立的地板表面 — *頂部*、*側面* 和 *背景* — 各自具有自己的紋理、平鋪和顏色。這允許舞台頂部、環繞邊緣和後板讀出不同的材質（例如，木質頂部配金屬側面）。


### 定製孔洞


預設情況下，挖出的孔洞會沿著舞台輪廓。切換 **定製孔洞** 可以用 **左** / **右** / **前** / **後** / **上** / **下** 的值來明確覆蓋邊界 — 對於非矩形切口或將孔洞與導入的場景對齊非常有用。

## 水系統

錨定在舞台中心的 HDRP 水表面。僅限專業版 (Pro)。用於位於舞台內部深槽的泳池、靜水湖和無限海洋。預設值包裝了常見的外觀。


### 類型和高度


**類型** 選擇水幾何體。*泳池* 會將表面尺寸調整到舞台的紅毯尺寸，當舞台有挖深槽時，這是最佳選擇。*河流* 是一個覆蓋地面圓盤的有限四邊形。*海洋* 是無限的 — 用於填滿地平線、不受舞台限制的水域。**高度** 是水面相對於舞台中心的水平。負值會將水面沉到地板下方（與通過負值舞台 *提升高度* 挖出的泳池深槽匹配）。


### 波浪


**漣漪** 驅動小的風浪狀波紋 — 對於靜水保持此值較低。**大浪** 驅動定義海洋外觀的廣泛湧浪；對於玻璃般平靜的表面，將其設置為 0。**波浪範圍** 控制水波效果向上延伸到接觸到水面的物體的高度。


### 光學屬性


**吸收距離** 是您從上方能看到水深多遠；對於混濁的水，降低此值；對於清澈的水，提高此值。**吸收倍數** 在從水面下方觀看時，會按比例縮放該距離。**折射最大距離** 限制水下的折射深度 — 較高的值會加劇扭曲。**焦散** 設定了投射在水下幾何體上的焦散圖案的亮度。
## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
天空圖、<b>木材</b>、舞台、泳池、海洋、音訊視覺化、投影螢幕、LED盒子、</td></tr>
<tr><td><strong aria-label="Ground Height">地面高度</strong></td><td>浮點數 (Float)</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Ground">地面</strong> — <em aria-label="Ground Settings.">地面設定。</em></summary>
<table aria-label="Ground Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong aria-label="Radius">半徑</strong></td><td>浮點數 (Float)</td><td>2 – 100</td><td>200</td><td></td><td>地面網格的大小。</td></tr>
<tr><td><strong aria-label="Hide If Stage Present">若有舞台則隱藏</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>開</td><td></td><td>當有舞台模型時，隱藏地面。</td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Surface">表面</strong></summary>
<table aria-label="Surface Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
天空圖、<b>木材</b>、混凝土、藍色瓷磚、投影螢幕、發光螢幕、LED螢幕、黑色亮光、音訊視覺化、白光、</td></tr>
<tr><td><strong aria-label="Texture">紋理</strong></td><td>選項 (Options)</td><td>[天空圖], [木材1], [DanceXR], [瓷磚], [混凝土], [影片]</td><td>[木材1]</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Tiling">平鋪</strong></summary>
<table aria-label="Tiling Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong aria-label="Tiling X">X方向平鋪</strong></td><td>浮點數 (Float)</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Tiling Y">Y方向平鋪</strong></td><td>浮點數 (Float)</td><td>0.1 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Wrap Mode">環繞模式</strong></td><td>整數 (Integer)</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Offset X">X軸偏移</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Offset Y">Y軸偏移</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Rotation">旋轉</strong></td><td>浮點數 (Float)</td><td>0 – 360</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Variation">變化度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Fit Texture">貼合紋理</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong aria-label="Gloss">光澤</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.95</td><td></td><td></td></tr>
<tr><td><strong aria-label="Metallic">金屬度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Bump">凹凸</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong aria-label="Glow">發光</strong></td><td>浮點數 (Float)</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Ambient">環境光</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Alpha Reduction">透明度降低</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Alpha Curve">透明度曲線</strong></td><td>浮點數 (Float)</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Clip">裁切</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Color">顏色</strong></summary>
<table aria-label="Color Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
原色、<b>白色</b>、黑色、紅色、黃色、深灰色、藍色、皮膚、膚色、橙色、</td></tr>
<tr><td><strong aria-label="Color Mode">顏色模式</strong></td><td>整數 (Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Hue">色相</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Satuation">飽和度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Brightness">亮度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Red">紅色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Green">綠色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blue">藍色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blend Mode">混合模式</strong></td><td>選項 (Options)</td><td>原色、乘積、混合、色相偏移</td><td>乘積</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blend">混合</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Alpha">透明度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Toon Shader">卡通渲染器</strong></summary>
<table aria-label="Toon Shader Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td><strong aria-label="Enabled">啟用</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
<b>銳利</b>、柔和、明亮、平坦 + 反射光、平坦、</td></tr>
<tr><td><strong aria-label="Shading">陰影處理</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Outline">輪廓線</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Specular">高光反射</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong aria-label="Soft Specular">柔和高光反射</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Highlight Area">高光區域</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong aria-label="Soft Highlight">柔和高光</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Ambient">環境光</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong aria-label="Shadow Area">陰影區域</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.65</td><td></td><td></td></tr>
<tr><td><strong aria-label="Shadow">陰影</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong aria-label="Soft Shadow">柔和陰影</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Special Shader">特殊渲染器</strong></summary>
<table aria-label="Special Shader Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong aria-label="Mode">模式</strong></td><td>選項 (Options)</td><td>關、折射粗、折射細、輪廓、無光照、實驗</td><td>關</td><td></td><td></td></tr>
<tr><td><strong aria-label="Refraction">折射</strong></td><td>浮點數 (Float)</td><td>1 – 3</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Thickness">厚度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="LED Mode">LED模式</strong></summary>
<table aria-label="LED Mode Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td><strong aria-label="Enabled">啟用</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong aria-label="Density">密度</strong></td><td>浮點數 (Float)</td><td>4 – 10</td><td>5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Size">大小</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong aria-label="Soft Edge">柔和邊緣</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong aria-label="Viewing Angle">觀看角度</strong></td><td>浮點數 (Float)</td><td>0 – 8</td><td>1</td><td></td><td>從角度觀看時減少亮度。0 = 完美</td></tr>
<tr><td><strong aria-label="Edge">邊緣</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Reduce Moire">減少莫爾紋</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Audio Visualizer">音訊視覺化</strong></summary>
<table aria-label="Audio Visualizer Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td><strong aria-label="Enabled">啟用</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
預設（重設），</td></tr>
<tr><td><strong aria-label="Layout">佈局</strong></td><td>整數 (Integer)</td><td>0 – 2</td><td>2</td><td></td><td></td></tr>
<tr><td><strong aria-label="Transparent">透明度</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td><strong aria-label="Shadow">陰影</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Radius">半徑</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Ring Size">環大小</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Data Scale">資料縮放</strong></td><td>浮點數 (Float)</td><td>-2 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Color Transition">顏色過渡</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong aria-label="Align">對齊</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Gap">間隙</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong aria-label="Shape Shift">形狀變動</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Beat Clock">節拍計時器</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Ring Color">環顏色</strong></summary>
<table aria-label="Ring Color Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>、黑色、黃色、藍色、動畫色相、與音樂發光、</td></tr>
<tr><td><strong aria-label="Color Mode">顏色模式</strong></td><td>整數 (Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Hue">色相</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Satuation">飽和度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Brightness">亮度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Red">紅色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Green">綠色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blue">藍色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Glow">發光</strong></td><td>浮點數 (Float)</td><td>0 – 5</td><td>20</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Background Color">背景顏色</strong></summary>
<table aria-label="Background Color Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>、黑色、黃色、藍色、動畫色相、與音樂發光、</td></tr>
<tr><td><strong aria-label="Color Mode">顏色模式</strong></td><td>整數 (Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Hue">色相</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Satuation">飽和度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Brightness">亮度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Red">紅色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Green">綠色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blue">藍色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Glow">發光</strong></td><td>浮點數 (Float)</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong aria-label="Background Image">背景圖片</strong></td><td>選項 (Options)</td><td>[無], [木材1], [DanceXR], [瓷磚], [混凝土], [影片]</td><td>[無]</td><td></td><td></td></tr>
<tr><td><strong aria-label="Background Vibration">背景震動</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Foreground Color">前景顏色</strong></summary>
<table aria-label="Foreground Color Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>、黑色、黃色、藍色、動畫色相、與音樂發光、</td></tr>
<tr><td><strong aria-label="Color Mode">顏色模式</strong></td><td>整數 (Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Hue">色相</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Satuation">飽和度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Brightness">亮度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Red">紅色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Green">綠色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blue">藍色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Glow">發光</strong></td><td>浮點數 (Float)</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong aria-label="Foreground Image">前景圖片</strong></td><td>選項 (Options)</td><td>[無], [木材1], [DanceXR], [瓷磚], [混凝土], [影片]</td><td>[DanceXR]</td><td></td><td></td></tr>
<tr><td><strong aria-label="Foreground Vibration">前景震動</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong aria-label="Foreground Scale">前景縮放</strong></td><td>浮點數 (Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong aria-label="Auto BPM">自動BPM</strong></td><td>開關 (Toggle)</td><td>開 / 關</td><td>關</td><td></td><td>使用實時自動偵測的BPM，而非設定的BPM。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong aria-label="Shadow Only">僅陰影</strong></summary>
<table aria-label="Shadow Only Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details open>
<summary><strong aria-label="Shadow Color">陰影顏色</strong></summary>
<table aria-label="Shadow Color Settings"><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設</th><th>條件</th><th>說明</th></tr></thead>
<tbody>
<tr><td>預設</td><td></td><td></td><td></td><td></td><td>
白色、黑色、紅色、<b>黃色</b>、灰色、藍色、皮膚、膚色、橙色、</td></tr>
<tr><td><strong aria-label="Color Mode">顏色模式</strong></td><td>整數 (Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Hue">色相</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Satuation">飽和度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Brightness">亮度</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Red">紅色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Green">綠色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong aria-label="Blue">藍色</strong></td><td>浮點數 (Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
</tbody>
</table>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>
<p>（省略）</p>