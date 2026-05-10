---
layout: release
title: 生成法線貼圖
locale: zh-TW
toc: true
---

# 生成法線貼圖

DanceXR 可以使用**基本貼圖**或**高光貼圖**作為來源，為一個沒有發布法線貼圖的材質合成法線貼圖。這可以在不需要您繪製或提供單獨法線貼圖的情況下，增加表面的浮雕感。

---

## 適用時機

- 模型的基本紋理具有可見的細節（織物編織、鱗片、刺繡），但沒有單獨的法線貼圖。
- 模型的高光/遮罩貼圖編碼了您希望作為浮雕而非光澤度的細節。
- 您希望對平坦的材質快速添加程序化的細節層。

---

## 如何啟用

1. 開啟相關類別的材質設定，通常是 [Skin](material_skin)、[Hair](material_hair)、[Opaque](material_opaque) 或 [Custom](material_custom1)。
2. 啟用 **Generate Normal Map**。
3. 選擇來源：**基本貼圖**或**高光貼圖**。
4. 調整強度。

生成的法線貼圖在計算時執行一次，並在渲染時間使用。除了法線貼圖材質外，不會產生任何實時單幀的成本。

---

## 與其他紋理增強功能結合

生成法線貼圖與以下這些紋理增強功能屬於同一類：

- [Specular / Mask Map](specular_map) — 使用一個來源貼圖來處理多個 PBR 通道。
- [Custom Detail Map](custom_detail_map) — 疊加平鋪的細節紋理。
- [Hexagon Detail Map](hexagon_detail) — 程序化六角形圖案細節。

您可以將它們結合使用——例如，結合來自基本貼圖生成的法線，並在其上疊加六角形細節浮雕。

---

## 相關頁面

- [Specular / Mask Map](specular_map)
- [Custom Detail Map](custom_detail_map)
- [Hexagon Detail Map](hexagon_detail)
- [Material Settings](material_settings)