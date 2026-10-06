---
layout: release
title: 紋理增強
locale: zh-TW
---


## 紋理增強
您可以通過利用特定效果的高光貼圖來增強此類材質的紋理，從基本貼圖或高光貼圖生成法線貼圖，並使用自定義細節貼圖來改善材質的細節。

### 高光/遮罩貼圖控制
[使用高光/遮罩貼圖](texture_enhancement#specular-mask-map)

### 生成法線貼圖
* [生成法線貼圖](texture_enhancement#generate-normal-map)

### 自定義細節貼圖
* [使用自定義細節貼圖](texture_enhancement#custom-detail-map)

### 漸變控制

允許沿著漸變路徑改變材質屬性。

{% include video id="Yi2W_cwufNk" provider="youtube" %}

{% include video id="d8GP3G0wF3M" provider="youtube" %}

{% include video id="atIdSd2TIrA" provider="youtube" %}

## 反射 / 遮罩地图 {#specular-mask-map}

## 鏡面反射 / 遮罩圖

使用鏡面反射或遮罩圖來控制材質的某些屬性。例如金屬感、環境光遮蔽、發光和光滑度。

這使您可以選擇地圖的每個通道來控制材質的不同屬性。

對於每個屬性，請選擇控制該屬性的地圖通道並調整屬性的強度。

## 生成法線貼圖 {#generate-normal-map}

# 生成法線貼圖

DanceXR 可以使用**基本貼圖**或**高光貼圖**作為來源，為一個沒有發布法線貼圖的材質合成法線貼圖。這可以在不需要您繪製或提供單獨法線貼圖的情況下，增加表面的浮雕感。

---

## 適用時機

- 模型的基本紋理具有可見的細節（織物編織、鱗片、刺繡），但沒有單獨的法線貼圖。
- 模型的高光/遮罩貼圖編碼了您希望作為浮雕而非光澤度的細節。
- 您希望對平坦的材質快速添加程序化的細節層。

---

## 如何啟用

1. 開啟相關類別的材質設定，通常是 [Skin](material_skin)、[Hair](material_hair)、[Opaque](material_settings#opaque-materials) 或 [Custom](material_settings#custom-materials)。
2. 啟用 **Generate Normal Map**。
3. 選擇來源：**基本貼圖**或**高光貼圖**。
4. 調整強度。

生成的法線貼圖在計算時執行一次，並在渲染時間使用。除了法線貼圖材質外，不會產生任何實時單幀的成本。

---

## 與其他紋理增強功能結合

生成法線貼圖與以下這些紋理增強功能屬於同一類：

- [Specular / Mask Map](texture_enhancement#specular-mask-map) — 使用一個來源貼圖來處理多個 PBR 通道。
- [Custom Detail Map](texture_enhancement#custom-detail-map) — 疊加平鋪的細節紋理。
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern) — 程序化六角形圖案細節。

您可以將它們結合使用——例如，結合來自基本貼圖生成的法線，並在其上疊加六角形細節浮雕。

---

## 相關頁面

- [Specular / Mask Map](texture_enhancement#specular-mask-map)
- [Custom Detail Map](texture_enhancement#custom-detail-map)
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern)
- [Material Settings](material_settings)

## 自定義細節地圖 {#custom-detail-map}

## 自定義細節地圖
自定義細節地圖允許您將自定義細節地圖添加到材質中。此地圖可用於為材質添加在基本地圖中不存在的細節。

內建的細節地圖列表可供使用，您可以將細節地圖放在內容庫的紋理文件夾中以供使用。

還有一個程序化的[六角形細節地圖](texture_enhancement#hexagon-pattern)可用於為材質添加六角形細節。

## 六角形圖案細節地圖 {#hexagon-pattern}

## 六角形圖案細節地圖
這是一個即時生成的程序化細節地圖。可用於支持細節地圖和服裝效果的材質類別中。

## 設置
* 密度：六角形的密度。
* 圓形：使用圓形代替六角形。
* 尺寸：六角形中心區域的大小。
* 凸起：六角形邊緣的凸起效果強度。可以是負值以反轉凸起方向。
* 噪音：為每個六角形單元的法線貼圖添加隨機方向。
* 柔邊：使六角形的邊緣變得柔和，以便它能夠融入正常紋理中。

## 典型用法
* 為材料添加六角形圖案凸起效果：啟用細節地圖和六角形圖案，調整凸起值以獲得所需效果。
* 為材料添加閃爍效果：啟用細節地圖和六角形圖案，增加密度，增加噪音值，調整光滑度和金屬度值以獲得所需效果。

{% include video id="G9SSJQieO-E" provider="youtube" %}

{% include video id="BV1VD421W7YK" provider="bilibili" %}
