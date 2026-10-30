---
layout: feature
title: 身体彩绘与喷洒
locale: zh-CN
toc: true
---

# 身体彩绘与喷洒

**身体彩绘**可在 DanceXR Native 中直接把颜色、图章和发光画在角色的皮肤和衣物上。**喷洒工具**会向角色喷水，水可以把颜料冲掉，并把颜色沿着身体带下。两者在所有版本中均为 **Pro** 功能。

颜料保存在模型自身的贴图空间中，因此无需额外操作就会跟随姿势和动画。

---

## 开启

身体彩绘是每个角色上的开关：**Actors > 角色 > Body Paint**。然后在 **Pointer Tool** 菜单（或右键点击空白处）中选择 **Paint** 工具，在角色上拖动。

只有开启了身体彩绘的角色才能被绘制，如果没有角色开启，则不提供 Paint 工具。

## 绘制模式

在 **Pointer Tool > Brush** 中，**Draw Mode** 决定一次点击如何变成颜料：

| 模式 | 作用 |
|---|---|
| **Point** | 每次点击一个点。 |
| **Stroke** | 拖动自由绘制。 |
| **Line** | 点击两个点。 |
| **Polygon** | 依次点击各个角，再次点击第一个角，或使用 **Finish Shape**，即可填充该形状。 |
| **Erase** | 用同一支画笔擦除颜料。 |

**Cancel Shape** 会放弃已开始的直线或多边形。Paint 为当前工具时，鼠标滚轮改变画笔大小，倾斜（Alt+滚轮）旋转图章，中键点击切换绘制模式。在 VR 中使用指向手的摇杆及其按下。Ctrl+滚轮始终交给相机。

### 画笔

**Size**、**Hardness**、**Opacity**、**Colour**、**Glow** 与 **Glow Strength**（比白色更亮的颜色会发光）、**Preserve Color** 以及 **Paint Side**（两面、仅正面或仅背面）决定每一笔的效果。在 **Stamp** 下，**Choose Picture...** 使用图片作为画笔，**Rotation** 旋转它，**Round Brush** 恢复默认。

画笔是全局的：其设置适用于所有可绘制的角色。

## 每个角色的设置

在角色的 **Body Paint** 栏中：

- **Canvas Resolution**：颜料的精细程度，256 到 2048。
- **Surfaces**：**Default Surfaces**、**Skin Only** 或 **Paint Every Eligible Mesh**。
- **Save Painted Colour**：把绘制内容随模型保存。关闭时，颜料仅在本次会话中保留。
- **Clear Drawing**：清除该角色上的所有内容。

## 喷洒工具

在 Pointer Tool 菜单中选择 **Spray**，水会自动从视图右下角朝指针喷出，落在每个开启了 **Wet Skin & Fluid**（默认开启）的角色上。你仍然可以环绕相机和拖动角色。

- **Launch Speed**、**Spread**、**Interval** 和 **Drops per Burst** 决定喷洒的效果。
- 把滚轮及其倾斜（**Wheel Up / Down**、**Wheel Tilt**）绑定到 *Velocity*、*Spread* 或 *Quantity*，就能在瞄准时调整喷洒。
- 在角色上，Wet Skin & Fluid 可以 **Spawn** 一个带有自己半径的 **Shower** 或 **Fountain**，并可保存预设。

### 把颜料冲掉

落在已绘制皮肤上的水会带走颜料，并把颜色沿着身体带下。在角色的 Body Paint 栏中：

- **Wash-Off Strength**：0 表示颜料永久保留；越高越快被冲掉。
- **Streak Length**：一道颜色水痕延伸的距离。
- **Stain Strength**：被冲下的颜色对干净皮肤的染色强度。
- **Water Tint**：水滴沾染被冲下颜色的程度。

要冲洗一个静止的身体，请停止音乐和动作，而不要使用 Pause，因为 Pause 也会让水停下。

---

## 相关页面

- [摆姿工具](pose_tool)
- [丝袜](stockings)
- [DanceXR Native](native)
