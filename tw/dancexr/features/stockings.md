---
layout: feature
title: 絲襪
locale: zh-TW
toc: true
---

# 絲襪

**絲襪**在 DanceXR Native 中為角色的皮膚覆上一層輕薄的針織物。它不是服裝網格：而是讓皮膚自身的材質按有一層針織物繃在其上的方式著色，因此適用於任何模型，並且在路徑追蹤器和光柵算繪器中都可使用。針織物會**在皮膚被拉伸處（如彎曲的膝蓋）變薄**，**在皮膚放鬆處變厚**，隨身體運動而變化。在所有版本中均為 **Pro** 功能。

在 **Actors > 角色 > Stockings** 中開啟。

---

## 覆蓋範圍

- **Region** 決定覆蓋範圍：腿、腿和臀部、身體，或身體和手臂。手永遠不會被覆蓋。
- **Height** 設定襪口距模型最低點的高度，**Angle** 讓襪口向兩側傾斜（負值向外側升高），**Edge** 讓襪口柔化（0 為硬邊）。無論姿勢如何，襪口都停留在腿上的同一位置。

## 外觀

**Colour** 和 **Smoothness**（織物的光澤）決定針織物的外觀。**Base Density** 是正面不拉伸時織物遮住皮膚的程度：低則輕薄，1 為不透明。**Taper** 向上增加紗線，讓大腿在拉伸下保持顏色；**Fresnel Power** 決定織物朝肢體輪廓變厚的快慢。**Live Update** 每個影格重新測量姿勢，使拉伸和皺褶跟隨身體；**Skin Only** 讓織物不覆蓋該範圍內的衣物和鞋子。

### Welt and Edge

襪口內側較厚的針織帶，也就是絲襪頂部的收邊：

- **Welt Width** 和 **Welt Density**：針織帶本身及其遮蓋皮膚的程度。
- **Rim Width** 和 **Rim Bump**：針織帶邊緣捲起的邊沿。
- **Skin Width** 和 **Skin Bump**：襪口外側被它壓陷的皮膚。

## Signals

**Signals** 子選單決定哪些因素讓針織物變薄或變厚：

- **Relaxed Girth** 和 **Girth Strength**：織物未拉伸時的圍度；身體比它粗的地方，織物會被拉薄。
- **Pose Stretch Strength** 和 **Squeeze Strength**：姿勢的拉伸讓織物變薄多少，擠壓讓它變厚多少。
- **Crease Strength (Rest)** 和 **Crease Strength (Pose)**：身體靜止時有的摺痕（如膝蓋後側）和姿勢造成的摺痕處的增厚。
- **Fold Tightness** 和 **Fold Smoothing**：哪種曲率被全額計入，以及摺痕擴散得多寬。
- **Minimum Density** 和 **Maximum Density**：無論如何拉伸或摺疊，織物都不會比它們更輕薄或更不透明。

## 預設

內建預設可幫你快速上手；也可以從該列的備選操作中儲存自己的預設。設定會隨模型一同儲存。

---

## 相關頁面

- [身體彩繪與噴灑](paint_and_spray)
- [DanceXR Native](native)
