---
layout: feature
title: 身體彩繪與噴灑
locale: zh-TW
toc: true
---

# 身體彩繪與噴灑

**身體彩繪**可在 DanceXR Native 中直接把顏色、印章和發光畫在角色的皮膚和衣物上。**噴灑工具**會向角色噴水，水可以把顏料沖掉，並把顏色沿著身體帶下。兩者在所有版本中均為 **Pro** 功能。

顏料儲存在模型自身的貼圖空間中，因此無需額外操作就會跟隨姿勢和動畫。

---

## 開啟

身體彩繪是每個角色上的開關：**Actors > 角色 > Body Paint**。然後在 **Pointer Tool** 選單（或右鍵點擊空白處）中選擇 **Paint** 工具，在角色上拖曳。

只有開啟了身體彩繪的角色才能被繪製，如果沒有角色開啟，則不提供 Paint 工具。

## 繪製模式

在 **Pointer Tool > Brush** 中，**Draw Mode** 決定一次點擊如何變成顏料：

| 模式 | 作用 |
|---|---|
| **Point** | 每次點擊一個點。 |
| **Stroke** | 拖曳自由繪製。 |
| **Line** | 點擊兩個點。 |
| **Polygon** | 依序點擊各個角，再次點擊第一個角，或使用 **Finish Shape**，即可填滿該形狀。 |
| **Erase** | 用同一支筆刷擦除顏料。 |

**Cancel Shape** 會放棄已開始的直線或多邊形。Paint 為目前工具時，滑鼠滾輪改變筆刷大小，傾斜（Alt+滾輪）旋轉印章，中鍵點擊切換繪製模式。在 VR 中使用指向手的搖桿及其按下。Ctrl+滾輪一律交給相機。

### 筆刷

**Size**、**Hardness**、**Opacity**、**Colour**、**Glow** 與 **Glow Strength**（比白色更亮的顏色會發光）、**Preserve Color** 以及 **Paint Side**（兩面、僅正面或僅背面）決定每一筆的效果。在 **Stamp** 下，**Choose Picture...** 使用圖片作為筆刷，**Rotation** 旋轉它，**Round Brush** 恢復預設。

筆刷是全域的：其設定適用於所有可繪製的角色。

## 每個角色的設定

在角色的 **Body Paint** 欄中：

- **Canvas Resolution**：顏料的細緻程度，256 到 2048。
- **Surfaces**：**Default Surfaces**、**Skin Only** 或 **Paint Every Eligible Mesh**。
- **Save Painted Colour**：把繪製內容隨模型儲存。關閉時，顏料僅在本次工作階段中保留。
- **Clear Drawing**：清除該角色上的所有內容。

## 噴灑工具

在 Pointer Tool 選單中選擇 **Spray**，水會自動從檢視右下角朝指標噴出，落在每個開啟了 **Wet Skin & Fluid**（預設開啟）的角色上。你仍然可以環繞相機和拖曳角色。

- **Launch Speed**、**Spread**、**Interval** 和 **Drops per Burst** 決定噴灑的效果。
- 把滾輪及其傾斜（**Wheel Up / Down**、**Wheel Tilt**）綁定到 *Velocity*、*Spread* 或 *Quantity*，就能在瞄準時調整噴灑。
- 在角色上，Wet Skin & Fluid 可以 **Spawn** 一個帶有自己半徑的 **Shower** 或 **Fountain**，並可儲存預設。

### 把顏料沖掉

落在已繪製皮膚上的水會帶走顏料，並把顏色沿著身體帶下。在角色的 Body Paint 欄中：

- **Wash-Off Strength**：0 表示顏料永久保留；越高越快被沖掉。
- **Streak Length**：一道顏色水痕延伸的距離。
- **Stain Strength**：被沖下的顏色對乾淨皮膚的染色強度。
- **Water Tint**：水滴沾染被沖下顏色的程度。

要沖洗一個靜止的身體，請停止音樂和動作，而不要使用 Pause，因為 Pause 也會讓水停下。

---

## 相關頁面

- [擺姿工具](pose_tool)
- [絲襪](stockings)
- [DanceXR Native](native)
