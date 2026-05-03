---
layout: release
title: 角色選項
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

# 演員選項

控制如何載入和替換演員模型的設定。


## 快取

模型在首次載入後會被保留在記憶體快取中，以便在演員之間切換時幾乎沒有延遲。**快取大小**設定了同時保留多少模型——如果經常切換，請增加此數值；如果需要減少記憶體（RAM）使用，請降低此數值。


## 紋理壓縮

啟用 *壓縮紋理* 會在載入時將紋理轉換為 GPU 壓縮格式。這能顯著減少複雜模型的 VRAM，但可能會導致某些材質出現輕微的畫質損失。


## 轉場

控制新增、移除或替換演員模型時的轉場效果。


## 自動演員更換

當快取中有多個模型時，*自動演員更換* 的數值會在運行時自動在這些模型之間切換。

如果為此數值啟用了自動更新，您就可以根據音樂進度或您選擇的任何其他資料來源實現自動演員切換。

# 子元件

## 轉場效果

當新增、移除或替換演員或其他可選網格時所使用的可重複轉場效果。該效果會在沿著一個移動邊緣，並可選地搭配粒子、顏色和光暈，來溶解網格。單一配置同時驅動了著色器端的燃燒效果和 VFX 的生成。


### 邊緣形狀



**方向**選擇邊緣是沿著網格*向上*還是*向下*掃描。**V Shape** 將邊緣從一條平坦的水平線（0）彎曲成角度的 V 形——這對於看起來不那麼機械化的溶解效果非常有用。**轉場模式**選擇分解邊緣的圖案：*單元格*適用於塊狀的單元格外觀，*馬賽克*適用於方形平鋪，*噪點*適用於柔和的有機溶解。**尺度**調整該圖案（對數）的大小，而**寬度**則擴展溶解所跨越的範圍，從銳利的線條到瀰漫的漸變。


### 顏色與光暈



**顏色**是在溶解前緣繪製的燃燒顏色。**光暈**將該邊緣增強為發光強度，使其看起來像熱燃燒而不是單純的色調。**混合**控制燃燒顏色在轉場範圍內覆蓋網格自身顏色的程度——降低此值可以讓原始材質透過效果仍可見。


### 持久時間與粒子



**轉場持續時間**是一個開關浮點數——開啟它使用自訂持續時間，關閉則回退到系統預設值。在 Quest 構建中，轉場無論如何都會被強制禁用。

**粒子效果**設定生成速率（對數——0 完全禁用粒子），而**粒子持續時間**設定它們的壽命。如果粒子持續時間超過轉場持續時間，系統會將轉場拉長以匹配，確保粒子不會在中途斷空。


## 配置

<table>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>快取大小</strong></td><td>整數</td><td>0 – 20</td><td>10</td><td></td><td>保留多少演員模型在快取中</td></tr>
<tr><td><strong>保留選項</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td>在替換演員時，自動將離開的演員的設定應用到進入的演員上。</td></tr>
<tr><td><strong>壓縮紋理</strong></td><td>開關</td><td>開 / 關</td><td>關</td><td></td><td>壓縮紋理以減少 VRAM 使用</td></tr>
<tr><td colspan="6"><details>
<summary><strong>轉場效果</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td>
預設（重設），</td></tr>
<tr><td><strong>方向</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td>動畫的方向。</td></tr>
<tr><td><strong>V Shape</strong></td><td>浮點數</td><td>0 – 5</td><td>1</td><td></td><td>控制邊緣的角度，0 為平坦。</td></tr>
<tr><td><strong>轉場模式</strong></td><td>整數</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>尺度</strong></td><td>浮點數</td><td>-3 – 3</td><td>0</td><td></td><td>圖案的尺度。</td></tr>
<tr><td><strong>寬度</strong></td><td>浮點數</td><td>0 – 1</td><td>0.1</td><td></td><td>轉場區域的大小。</td></tr>
<tr colspan="6"><details>
<summary><strong>顏色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>類型</th><th>範圍 / 值</th><th>預設值</th><th>條件</th><th>描述</th></tr></thead>
<tr><td>預設值</td><td></td><td></td><td></td><td></td><td>
白色、黑色、紅色、<b style="color: yellow;">黃色</b>、灰色、藍色、皮膚、肉色、橙色、</td></tr>
<tr><td><strong>顏色模式</strong></td><td>整數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮點數</td><td>0 – 1</td><td>0.1667</td><td></td><td></td></tr>
<tr><td><strong>飽和度</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>亮度</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>紅</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>綠</strong></td><td>浮點數</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>藍</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>光暈</strong></td><td>浮點數</td><td>0 – 10</td><td>1</td><td></td><td>燃燒效果的亮度。</td></tr>
<tr><td><strong>混合</strong></td><td>浮點數</td><td>0 – 1</td><td>1</td><td></td><td>原始顏色與燃燒顏色之間的混合。 </td></tr>
<tr><td><strong>轉場持續時間</strong></td><td>浮點數</td><td>0 – 5</td><td>2</td><td></td><td>動畫的持續時間。</td></tr>
<tr><td><strong>粒子效果</strong></td><td>浮點數</td><td>0 – 10</td><td>2</td><td></td><td>控制粒子數量。</td></tr>
<tr><td><strong>粒子持續時間</strong></td><td>浮點數</td><td>0 – 5</td><td>2.5</td><td></td><td>控制粒子的壽命。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>自動演員更換</strong></td><td>浮點數</td><td>0 – 1</td><td>0</td><td></td><td>根據數值在快取中的演員之間自動切換</td></tr>
</tbody>
</table