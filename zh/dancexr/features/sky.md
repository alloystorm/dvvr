---
layout: feature
title: 天空
locale: zh-CN
nav_links:
  - label: 简介
    url: /zh/dancexr
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
---

# 天空

控制所有上方的元素——填满地平线的天空背景、它投射到场景中的环境光，以及驱动云、布料和粒子系统的全局风力。预设将这些元素组合成名为 *Skymap*、*Procedural*、*Indoor*、*Thin Cloud* 和 *Cloudy* 的外观组。

## 模式 (Mode)

**模式** 选择三种天空渲染器之一，其余面板会相应调整。*颜色 (Color)* 从 **天空颜色 (Sky Color)** / **中间颜色 (Middle Color)** / **地面颜色 (Ground Color)** 的值绘制一个平坦的渐变天空，这是成本最低的选项。*天空贴图 (Sky Map)* 将一个 360° 全景图（内置或导入）包裹到场景周围——适用于室外或风格化的背景。*程序化 (Procedural)* 渲染一个基于物理的天空，并且（在 HDRP 上）是唯一支持体积云的模式。

## 天空贴图和方向 (Sky Map and Orientation)

当模式为 *Sky Map* 时，**天空贴图** 从内置集合和内容库中导入的任何全景图选择相应的贴图。加载大型天空贴图是异步的，这样 UI 保持响应性。**方向 (Orientation)** 围绕垂直轴以度数旋转天空——这也会旋转用于地面天空穹顶材质的投影，因此调整它也会移动地面反射。

## 背景和环境光 (Background and Ambient)

**背景 (Background)** (HDRP) 调节屏幕上天空的亮度程度。**天空环境光 (Sky Ambient)** 控制天空作为环境光泄漏到场景其余部分的程度——如果明亮的贴图正在冲淡角色的阴影，则降低此值。在 URP 上，*天空曝光 (Sky Exposure)* 和 *强度 (Intensity)* 起到相同的作用，其中天空曝光还影响反射探针的亮度。

## 天空颜色 (Sky Colors)

在 *颜色 (Color)* 模式下，**天空颜色 (Sky Color)**、**中间颜色 (Middle Color)** 和 **地面颜色 (Ground Color)** 定义了三段式渐变的上部、地平线和底部。它们还驱动三光环境光（以及在 HDRP 上，雾气反照率），因此更改它们除了可见背景外，还会改变场景从天空接收到的色调。

## 风 (Wind)

**风 (Wind)** 设置一个全局风速，驱动布料模拟、粒子动力学以及（在 HDRP 上）体积云的移动。**风向 (Wind Direction)** 设置其指南针方位。保持适度——过高的风速会使头发和裙子明显地飘扬。

## 风场 (Wind Field)

一个叠加在全局风力之上的局部风力区域，适用于舞台效果，例如风扇吹向某个角色。打开它，然后使用 **位置 (Position)** / **旋转 (Rotation)**（菜单打开时会出现一个交互式小方块）对圆柱形区域进行定位和定向。**距离 (Distance)** 是圆柱体的长度，**半径 (Radius)** 是其宽度，**速度 (Speed)** 是其强度。仅影响体积内的布料和粒子。

## 云 (Clouds) (HDRP)

体积云，仅在 *程序化 (Procedural)* 模式下可用。**开关 (Toggle)** 打开它们。**形状尺度 (Shape Scale)** 和 **形状因子 (Shape Factor)** 控制大尺度的轮廓；**侵蚀尺度 (Erosion Scale)** 和 **侵蚀因子 (Erosion Factor)** 添加模糊的边缘细节；**密度 (Density)** 控制整体覆盖率。**阴影 (Shadow)** 将云阴影投射到场景中——成本较高，但在室外舞台上增加了大量真实感。**风力乘数 (Wind Multiplier)** 仅对云进行全局风力缩放，因此它们可以比场景其余部分飘移得更快或更慢。