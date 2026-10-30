---
layout: feature
title: 丝袜
locale: zh-CN
toc: true
---

# 丝袜

**丝袜**在 DanceXR Native 中为角色的皮肤覆上一层轻薄的针织物。它不是服装网格：而是让皮肤自身的材质按有一层针织物绷在其上的方式着色，因此适用于任何模型，并且在路径追踪器和光栅渲染器中都可使用。针织物会**在皮肤被拉伸处（如弯曲的膝盖）变薄**，**在皮肤放松处变厚**，随身体运动而变化。在所有版本中均为 **Pro** 功能。

在 **Actors > 角色 > Stockings** 中开启。

---

## 覆盖范围

- **Region** 决定覆盖范围：腿、腿和臀部、身体，或身体和手臂。手永远不会被覆盖。
- **Height** 设置袜口距模型最低点的高度，**Angle** 让袜口向两侧倾斜（负值向外侧升高），**Edge** 让袜口柔化（0 为硬边）。无论姿势如何，袜口都停留在腿上的同一位置。

## 外观

**Colour** 和 **Smoothness**（织物的光泽）决定针织物的外观。**Base Density** 是正面不拉伸时织物遮住皮肤的程度：低则轻薄，1 为不透明。**Taper** 向上增加纱线，让大腿在拉伸下保持颜色；**Fresnel Power** 决定织物朝肢体轮廓变厚的快慢。**Live Update** 每帧重新测量姿势，使拉伸和褶皱跟随身体；**Skin Only** 让织物不覆盖该范围内的衣物和鞋子。

### Welt and Edge

袜口内侧较厚的针织带，也就是丝袜顶部的收边：

- **Welt Width** 和 **Welt Density**：针织带本身及其遮盖皮肤的程度。
- **Rim Width** 和 **Rim Bump**：针织带边缘卷起的边沿。
- **Skin Width** 和 **Skin Bump**：袜口外侧被它压陷的皮肤。

## Signals

**Signals** 子菜单决定哪些因素让针织物变薄或变厚：

- **Relaxed Girth** 和 **Girth Strength**：织物未拉伸时的围度；身体比它粗的地方，织物会被拉薄。
- **Pose Stretch Strength** 和 **Squeeze Strength**：姿势的拉伸让织物变薄多少，挤压让它变厚多少。
- **Crease Strength (Rest)** 和 **Crease Strength (Pose)**：身体静止时有的折痕（如膝盖后侧）和姿势造成的折痕处的增厚。
- **Fold Tightness** 和 **Fold Smoothing**：哪种曲率被全额计入，以及折痕扩散得多宽。
- **Minimum Density** 和 **Maximum Density**：无论如何拉伸或折叠，织物都不会比它们更轻薄或更不透明。

## 预设

内置预设可帮你快速上手；也可以从该行的备选操作中保存自己的预设。设置会随模型一同保存。

---

## 相关页面

- [身体彩绘与喷洒](paint_and_spray)
- [DanceXR Native](native)
