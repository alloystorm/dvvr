---
layout: feature
title: 服裝與身體彩繪
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

# 服裝與身體彩繪

服裝層會在角色皮膚材質上應用一層程序化布料/繪畫層——用於添加絲襪、連體服、乳膠、六邊形細節、自由繪畫的身體彩繪和溶解過渡效果，而不會觸動底層的網格或材質。


## 模式

**模式**決定了這個層的行為方式。《身體彩繪》將角色變成一個你可以直接用游標繪畫的畫布——選擇畫筆顏色並自由繪畫。《服裝》會隱藏繪畫工具，而是從程序化的形狀/圖案設定來驅動這個層，因此你可以根據參數生成乾淨的絲襪或連體服。《服裝彩繪》結合了兩者：程序化形狀定義了服裝區域，而你可以在其上進行繪畫。面板中的可見性規則會在設定模式後自動折疊不相關的子區塊。


## 預設

七個內建預設涵蓋了常見的情況——身體彩繪、全身乳膠、V 形網狀、兩種絲襪變體和兩種連體服。它們只需點擊一下就能設定模式、形狀和三個表面預設；將它們視為需要調整的起點，而不是最終效果。


## 身體彩繪

{% include video id="chHk9--cUYE" provider="youtube" %}

參閱《身體彩繪》子區塊。畫筆大小、旋轉、顏色、圖章材質，以及現場儲存/載入繪圖功能均在此處。僅在《身體彩繪》和《服裝彩繪》模式下可見。


## 形狀與圖案

參閱《形狀》子區塊。控制服裝的程序化幾何體——包含絲襪高度、頂部線條、網狀/迷宮/曲線圖案以及邊緣處的突起效果。在純《身體彩繪》模式下隱藏，因為沒有程序化服裝可以進行塑形。


## 表面

三個表面層疊加在服裝上：**表面底層**是主要的布料（乳膠、絲襪、金色等），**表面圖案**驅動線/迷宮圖案填充，而**表面邊框**控制形狀邊緣周圍的飾邊。每個都是一個完整的表面區塊（金屬、光澤、顏色、各向異性、溶解、特殊著色器），因此你可以混合例如啞光絲襪與發光邊框。在《身體彩繪》模式下隱藏。


## 六邊形細節

參閱《六邊形圖》子區塊。在表面上添加程序化的六邊形/圓形微圖案，用於網狀風格細節或科幻面板。當您想要平滑的布料時，請關閉此功能。


## 溶解

**溶解**是控制服裝沿著溶解圖淡出的大致比例（0 – 1）——使用自動更新來驅動，可同步於音樂或其他數據的撕裂/熔化過渡效果。*溶解圖*子區塊用於配置圖本身：圖案頻率、邊緣寬度以及切口兩側的突起度，X/Y 偏移量和硬切口開關。在純《身體彩繪》模式下隱藏。

# 子組件

## 身體彩繪

在角色身體上進行自由繪畫。將游標（或VR指針）拖動過模型，將顏色或圖案筆觸直接應用到服裝畫布上。畫布會跨幀保留，因此你可以隨著時間積累繪圖、將其儲存為材質，並稍後重新載入。


### 畫筆

**畫筆大小**和**畫筆旋轉**設定筆觸形狀；旋轉僅在選擇圖章材質時才適用。**圖章**選擇可選的圖章——設定後，每次點擊會打上一個單一的貼花，而不是繪製連續筆觸，這對於紋身或標誌圖案是正確的選擇。**畫筆類型**在《服裝彩繪》模式下選擇你繪畫的通道（底層/圖案/邊緣/清除）；在《身體彩繪》模式下，通道是隱含的，因此此選項被隱藏。


### 顏色、發光與保留

**顏色**是《身體彩繪》模式下的畫筆顏色。**發光**會將繪製顏色強度乘上（超過 1 的強度會變成發光）。**保留顏色**調整發光增強，使其能夠增強亮度，但不會沖淡顏色的色調——當您想要飽和的霓虹效果而不是褪色的明亮效果時非常有用。**清除**將畫筆切換為清除而不是繪畫。


### 繪畫側

限制筆觸只能畫在身體的*正面*、*背面*或*兩側*。當您只想在胸部或背面繪製設計而不需要小心避開另一側時，請選擇一個側邊。


### 畫布操作

**清除畫布**會擦除繪圖。**儲存繪圖**將當前的畫布寫入磁碟，同時儲存 HDR 和 PNG，以確保完整的顏色/發光範圍不會在傳輸中丟失。**載入繪圖**選擇先前儲存的繪圖（或圖庫中的任何繪圖材質）作為畫布內容。


## 形狀

服裝層的程序化幾何體——定義了服裝覆蓋身體的位置以及填充了哪些圖案。所有內容都在著色器中計算，因此變化是實時的，且無需撰寫材質。


### 絲襪與頂部線條

服裝的邊界最多由三條對角切口限制：一條絲襪線（腿部覆蓋的底部）和兩條頂部線（軀幹上的V領風格切口）。每條線都有一個**高度**（它穿過中心的點）和一個**角度**（偏離水平線的角度）。組合這三者可以繪製絲襪、V形連體服、網狀吊飾等。**絲襪邊緣**和**頂部邊緣**將切口柔化成漸變——較小的值給出硬邊，較大的值讓服裝逐漸淡入皮膚。


### 線條圖案

**線條圖案類型**選擇填充方式：《無》使區域實心，《網格》瓷磚網狀，《迷宮》和《迷宮曲線》生成非重複的迷宮線，《平行》繪製條紋。**線條圖案密度**設定線條間距，**線條圖案旋轉**旋轉整個圖案，**線條圖案對稱**使其對稱於身體中心，使左右匹配。**線條圖案種子**在不改變密度的情況下重新排列隨機迷宮圖案。**邊框大小內/外**控制線條在其中心兩側的粗細——利用非對稱性來暗示縫線或滾邊。


### 突起

**內側/外側突起**提高了或降低了線邊附近的表面，**內側/外側距離**控制突起蔓延的範圍。微妙的正突起看起來像是凸起的縫線；負突起看起來像是壓紋的接縫。


## 六邊形圖

一種程序化的六邊形（或圓形）微圖案，疊加在表面上，用於網狀、科幻面板或鉚釘造型。當您想要平滑的布料時，請關閉此功能。


### 密度與形狀

**密度**設定六邊形能橫跨表面多少個單位（會對齊到 2 的次方以實現整齊的鋪排）。**大小**按比例縮放每個單元內的六邊形——較小的值會在六邊形之間留下間隙，較大的值則將它們緊密地塞在一起。**使用圓形**將六邊形形狀替換為圓形，適用於波點或鉚釘造型。**柔邊**控制每個單元邊界處的衰減；接近零的值給出清晰的邊界，較大的值則將圖案模糊到周圍的表面。


### 突起與噪聲

**突起**提高或降低每個單元相對於表面的高度（負值會壓入）。**噪聲**隨機化每個單元的高度，使圖案看起來不像完美的網格。


### UV 投影

對於服裝，單元可以遵循模型的 UV 排列，也可以從環繞身體的虛擬圓柱體上投影。**UV 投影**啟用了圓柱體模式——當拉伸或扭曲的 UV 破壞了圖案時，請開啟此功能。**投影半徑**縮放圓柱體，**旋轉**使其傾斜，使六邊形網格呈對角線方向而不是直線。


## 溶解圖

生成驅動父級的 *溶解* 滑桿的噪聲圖。此圖由兩個層疊圖案和一個邊緣輪廓構建而成，因此無論根據這些設定，相同的溶解比例都可能表現為龜裂、燃燒、熔化或乾淨的切口。


### 第 1 層與第 2 層

兩個獨立的噪聲層組合以打斷溶解前緣。**圖案 L1 / L2** 選擇一個噪聲變體（不同的值會產生明顯不同的形狀）。**密度 L1 / L2** 控制每個層的精細度——L1 通常是寬廣的形狀，L2 是小尺度的細節。**放大比例**縮放兩個層，**曲線**銳化或柔化溶解梯度。


### 邊緣

服裝溶解的地方會在切口兩側留下一個過渡帶。**邊緣大小**和**邊緣突起**塑造了仍然可見側的帶狀結構；**反向邊緣大小 / 突起**塑造了已溶解側的帶狀結構。負突起會使表面內凹（適用於磨損/燒焦的外觀）；正突起會使其凸起。**切口**會完全丟棄已溶解的像素，而不是淡化其透明度——當您希望服裝是「一個孔一個孔」地消失而不是淡出時，請選擇此項。


### 偏移

**偏移 X / Y** 將溶解圖沿著身體滑動。通過自動更新來動畫它們，使溶解前緣以某個方向掃過，而不是均勻地出現。


## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>身體彩繪</b>, 全身乳膠, V 形網狀, 絲襪, 網狀絲襪, 連體服 1, 連體服 2, </td></tr>
<tr><td><strong>模式</strong></td><td>整數</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>身體彩繪</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>繪畫側</strong></td><td>整數</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>圖章</strong></td><td>選項</td><td>[無]、[紋身]</td><td>[無]</td><td></td><td></td></tr>
<tr><td><strong>畫筆大小</strong></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>畫筆旋轉</strong></td><td>浮點數</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>畫筆類型</strong></td><td>整數</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>清除</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
白色、黑色、紅色、<b>黃色</b>、灰色、藍色、皮膚、肉色、橘色、</td></tr>
<tr><td><strong>顏色模式</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>飽和度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>發光</strong></td><td>浮點數</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>保留顏色</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>清除畫布</strong></td><td>動作</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>儲存繪圖</strong></td><td>動作</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>載入繪圖</strong></td><td>選項</td><td>[無]</td><td>[無]</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>形狀與圖案</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>全身</b>, V 形, 絲襪, 網狀全身, 網狀V 形, 網狀絲襪, 迷宮 1, 迷宮 2, 曲線 1, 曲線 2, </td></tr>
<tr><td><strong>頂部高度1</strong></td><td>浮點數</td><td>0 – 3</td><td>3</td><td></td><td>第一條線在中心的高度</td></tr>
<tr><td><strong>頂部角度1</strong></td><td>浮點數</td><td>-180 – 180</td><td>0</td><td></td><td>第一條線的角度</td></tr>
<tr><td><strong>頂部高度2</strong></td><td>浮點數</td><td>0 – 3</td><td>3</td><td></td><td>第二條線在中心的高度</td></tr>
<tr><td><strong>頂部角度2</strong></td><td>浮點數</td><td>-180 – 180</td><td>0</td><td></td><td>第二條線的角度</td></tr>
<tr><td><strong>頂部邊緣</strong></td><td>浮點數</td><td>0 – 0.2</td><td>0.05</td><td></td><td>第一條和第二條線的邊緣寬度</td></tr>
<tr><td><strong>絲襪高度</strong></td><td>浮點數</td><td>0 – 3</td><td>1.45</td><td></td><td>絲襪線在中心的高度</td></tr>
<tr><td><strong>絲襪角度</strong></td><td>浮點數</td><td>-180 – 180</td><td>0</td><td></td><td>絲襪線的角度</td></tr>
<tr><td><strong>絲襪邊緣</strong></td><td>浮點數</td><td>0 – 0.2</td><td>0.05</td><td></td><td>絲襪線的邊緣寬度</td></tr>
<tr><td><strong>圖案類型</strong></td><td>整數</td><td>0 – 4</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>圖案對稱</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td><strong>圖案密度</strong></td><td>浮點數</td><td>1 – 50</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>圖案旋轉</strong></td><td>浮點數</td><td>0 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>圖案種子</strong></td><td>浮點數</td><td>10 – 50</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>邊框大小內</strong></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>邊框大小外</strong></td><td>浮點數</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>外側突起</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>外側距離</strong></td><td>浮點數</td><td>0 – 0.025</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong>內側突起</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>內側距離</strong></td><td>浮點數</td><td>0 – 0.1</td><td>0.005</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>六邊形圖</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td><strong>啟用</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td>預設值</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>密度</strong></td><td>浮點數</td><td>0 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>大小</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>突起</strong></td><td>浮點數</td><td>-1 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>噪聲</strong></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>使用圓形</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td><strong>柔邊</strong></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>UV 投影</strong></td><td>切換</td><td>開 / 關</td><td>開</td><td></td><td></td></tr>
<tr><td><strong>投影半徑</strong></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>旋轉</strong></td><td>浮點數</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>表面底層</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>絲襪薄</b>, 絲襪厚, 白色絲襪, 乳膠, 透明乳膠, 銀色, 金色, 發光白色, 原版, </td></tr>
<tr><td><strong>光澤</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>金屬度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>突起</strong></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>發光</strong></td><td>浮點數</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度降低</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度曲線</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>剪裁</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
原版, <b>白色</b>, 黑色, 紅色, 黃色, 深灰色, 藍色, 皮膚, 肉色, 橘色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>飽和度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>混合模式</strong></td><td>選項</td><td>原版, 乘法, 混合, 色調偏移</td><td>混合</td><td></td><td></td></tr>
<tr><td><strong>混合</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>透明度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>各向異性</strong></td><td>浮點數</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>絲襪效果</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>絲襪漸變</strong></td><td>浮點數</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>細節密度</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>啟用溶解</strong></td><td>切換</td><td>開 / 關</td><td>開</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>表面圖案</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>絲襪薄</b>, 絲襪厚, 白色絲襪, 乳膠, 透明乳膠, 銀色, 金色, 發光白色, 原版, </td></tr>
<tr><td><strong>光澤</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>金屬度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>突起</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>發光</strong></td><td>浮點數</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度降低</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度曲線</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>剪裁</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
原版, <b>白色</b>, 黑色, 紅色, 黃色, 深灰色, 藍色, 皮膚, 肉色, 橘色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>飽和度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>混合模式</strong></td><td>選項</td><td>原版, 乘法, 混合, 色調偏移</td><td>混合</td><td></td><td></td></tr>
<tr><td><strong>混合</strong></td><td>浮點數</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>透明度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>各向異性</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>絲襪效果</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>絲襪漸變</strong></td><td>浮點數</td><td>-3 – 3</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>細節密度</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>啟用溶解</strong></td><td>切換</td><td>開 / 關</td><td>開</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>表面邊框</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
<b>絲襪薄</b>, 絲襪厚, 白色絲襪, 乳膠, 透明乳膠, 銀色, 金色, 發光白色, 原版, </td></tr>
<tr><td><strong>光澤</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>金屬度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>突起</strong></td><td>浮點數</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>發光</strong></td><td>浮點數</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度降低</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>透明度曲線</strong></td><td>浮點數</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>剪裁</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
原版, <b>白色</b>, 黑色, 紅色, 黃色, 深灰色, 藍色, 皮膚, 肉色, 橘色, </td></tr>
<tr><td><strong>顏色模式</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>飽和度</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>紅</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>綠</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>藍</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>混合模式</strong></td><td>選項</td><td>原版, 乘法, 混合, 色調偏移</td><td>混合</td><td></td><td></td></tr>
<tr><td><strong>混合</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>透明度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>各向異性</strong></td><td>浮點數</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>絲襪效果</strong></td><td>浮點數</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>絲襪漸變</strong></td><td>浮點數</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>細節密度</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>啟用溶解</strong></td><td>切換</td><td>開 / 關</td><td>開</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>溶解</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>溶解圖</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>溶解圖</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>圖案 L1</strong></td><td>浮點數</td><td>0 – 90</td><td>13</td><td></td><td>生成溶解圖時更改第 1 層圖案</td></tr>
<tr><td><strong>密度 L1</strong></td><td>浮點數</td><td>1 – 10</td><td>3.5</td><td></td><td>第 1 層圖案的密度</td></tr>
<tr><td><strong>圖案 L2</strong></td><td>浮點數</td><td>0 – 90</td><td>31</td><td></td><td>生成溶解圖時更改第 2 層圖案</td></tr>
<tr><td><strong>密度 L2</strong></td><td>浮點數</td><td>10 – 100</td><td>50</td><td></td><td>第 2 層圖案的密度</td></tr>
<tr><td><strong>放大比例</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>曲線</strong></td><td>浮點數</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>邊緣大小</strong></td><td>浮點數</td><td>0 – 0.2</td><td>0.05</td><td></td><td>正向區域的邊緣寬度</td></tr>
<tr><td><strong>邊緣突起</strong></td><td>浮點數</td><td>-1 – 1</td><td>-1</td><td></td><td>邊緣區域的突起效果</td></tr>
<tr><td><strong>反向邊緣大小</strong></td><td>浮點數</td><td>0 – 0.2</td><td>0.05</td><td></td><td>負向區域的邊緣寬度</td></tr>
<tr><td><strong>反向邊緣突起</strong></td><td>浮點數</td><td>-1 – 1</td><td>-1</td><td></td><td>邊緣區域的突起效果</td></tr>
<tr><td><strong>偏移 X</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td>沿 X 方向偏移溶解圖</td></tr>
<tr><td><strong>偏移 Y</strong></td><td>浮點數</td><td>-1 – 1</td><td>0</td><td></td><td>沿 Y 方向偏移溶解圖</td></tr>
<tr><td><strong>切口</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td>使溶解區域不可見</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>手動選擇</strong></td><td>切換</td><td>開 / 關</td><td>關</td><td></td><td></td></tr>
<tr><td><strong>選擇材質</strong></td><td>選擇</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>