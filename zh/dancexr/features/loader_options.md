---
layout: release
title: 角色选项
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

# 演员选项

控制演员模型如何加载和替换的设置。

## 缓存

模型在首次加载后会被保留在内存缓存中，因此在演员之间切换时几乎是即时的。**缓存大小**设置了一次可保留的模型数量——如果经常切换演员，请增加它；如果想减少内存使用，请降低它。

## 纹理压缩

启用*压缩纹理*会将纹理转换为加载时的GPU压缩格式。这可以显著减少复杂模型的VRAM占用，但在某些材料上可能会引入轻微的画质损失。

## 过渡

控制添加、移除或替换演员模型时的过渡效果。

## 自动演员更换

当缓存中有多个模型时，*自动演员更换*的值将在运行时在它们之间自动切换。

如果为该值启用自动更新，您可以通过音乐进度或您选择的任何其他数据源实现自动的演员切换。

# 子组件

## 过渡效果

当添加、移除或替换演员或其他可选网格时应用的重用过渡效果。此效果沿着移动边缘溶解网格，并可选择附加粒子、颜色和光芒——单一配置同时驱动了着色器端的烧蚀和特效的生成。

### 边缘形状



**方向**选择边缘是沿着网格*向上*还是*向下*扫动。**V形状**将边缘从平坦的水平线 (0) 弯曲成有角度的 V 形——这对于看起来不那么机械的溶解效果很有用。**过渡模式**选择破坏边缘的图案：*单元格*用于粗块的蜂窝状外观，*马赛克*用于方格平铺，*噪点*用于柔和的有机溶解。**缩放**调整该图案的大小（对数），**宽度**则扩大溶解跨越的区域，范围从锐利线条到漫射渐变。

### 颜色和光芒



**颜色**是在溶解前缘绘制的烧蚀颜色。**光芒**将该边缘增强到发光强度，使其看起来像是炽热的灼伤，而不是简单的色调。**混合**控制烧蚀颜色在过渡区域覆盖网格自身颜色的程度——将其降低可以使原始材料通过效果仍然可见。

### 持续时间和粒子



**过渡持续时间**是一个开关式浮点数——打开它可使用自定义持续时间，关闭它则回退到系统默认值。在Quest设备构建上，过渡无论如何都会被禁用。

**粒子效果**设置了生成速率（对数——0 完全禁用粒子），**粒子持续时间**设置了它们存活的长度。如果粒子持续时间超过过渡持续时间，系统会拉伸过渡以匹配，防止粒子在半空中被切断。

## 配置

<table >
<thead ><tr ><th >设置</th><th >类型</th><th >范围 / 值</th><th >默认</th><th >条件</th><th >描述</th></tr></thead>
<tbody >
<tr ><td >预设</td><td ></td><td ></td><td ></td><td ></td><td >
</td></tr>
<tr ><td ><strong >缓存大小</strong></td><td >整数</td><td >0 – 20</td><td >10</td><td ></td><td >保留多少个演员模型到缓存中</td></tr>
<tr ><td ><strong >保留选项</strong></td><td >切换开关</td><td >开 / 关</td><td >关</td><td ></td><td >在替换演员时，自动将源演员的设置应用于目标演员。</td></tr>
<tr ><td ><strong >压缩纹理</strong></td><td >切换开关</td><td >开 / 关</td><td >关</td><td ></td><td >压缩纹理以减少VRAM占用</td></tr>
<tr ><td colspan="6"><details>
<summary><strong >过渡效果</strong></strong ></summary>
<table ><tbody >
<thead ><tr ><th >设置</th><th >类型</th><th >范围 / 值</th><th >默认</th><th >条件</th><th >描述</th></tr></thead>
<tr ><td >预设</td><td ></td><td ></td><td ></td><td ></td><td >
默认 (重置)， </td></tr>
<tr ><td ><strong >方向</strong></strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td ></td><td >动画的方向。</td></tr>
<tr ><td ><strong >V形状</strong></strong ></td ><td >浮点数</td><td >0 – 5</td><td >1</td><td ></td><td >控制边缘的角度，0即为平直。</td></tr>
<tr ><td ><strong >过渡模式</strong></strong ></td ><td >整数</td><td >0 – 2</td><td >0</td><td ></td><td ></tr>
<tr ><td ><strong >缩放</strong></strong ></td ><td >浮点数</td><td >-3 – 3</td><td >0</td><td ></td><td >图案的缩放。</td></tr>
<tr ><td ><strong >宽度</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0.1</td><td ></td><td >过渡区域的大小。</td></tr>
<tr colspan="6"><details>
<summary><strong >颜色</strong></strong ></summary>
<table ><tbody >
<thead ><tr ><th >设置</th><th >类型</th><th >范围 / 值</th><th >默认</th><th >条件</th><th >描述</th></tr></thead>
<tr ><td >预设</td><td ></td><td ></td><td ></td><td ></td><td >白色、黑色、红色、<b >黄色</b>、灰色、蓝色、皮肤、肉色、橙色、</td></tr>
<tr ><td ><strong >颜色模式</strong></strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
<tr ><td ><strong >色相</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0.1667</td><td ></td><td ></td></tr>
<tr ><td ><strong >饱和度</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >1</td><td ></td><td ></td></tr>
<tr ><td ><strong >亮度</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0.9</td><td ></td><td ></td></tr>
<tr ><td ><strong >红色</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0.9</td><td ></td><td ></td></tr>
<tr ><td ><strong >绿色</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0.9</td><td ></td><td ></td></tr>
<tr ><td ><strong >蓝色</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0</td><td ></td><td ></td></tr>
</tbody ></table >
</details></td ></tr >
<tr ><td ><strong >光芒</strong></strong ></td ><td >浮点数</td><td >0 – 10</td><td >1</td><td ></td><td >烧蚀效果的亮度。</td></tr>
<tr ><td ><strong >混合</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >1</td><td ></td><td >原始颜色和烧蚀颜色之间的混合。 </td></tr>
<tr ><td ><strong >过渡持续时间</strong></strong ></td ><td >浮点数</td><td >0 – 5</td><td >2</td><td ></td><td >动画的持续时间。</td></tr>
<tr ><td ><strong >粒子效果</strong></strong ></td ><td >浮点数</td><td >0 – 10</td><td >2</td><td ></td><td >控制粒子数量。</td></tr>
<tr ><td ><strong >粒子持续时间</strong></strong ></td ><td >浮点数</td><td >0 – 5</td><td >2.5</td><td ></td><td >控制粒子存活时间。</td></tr>
</tbody ></table >
</details></td ></tr >
<tr ><td ><strong >自动演员更换</strong></strong ></td ><td >浮点数</td><td >0 – 1</td><td >0</td><td ></td><td >根据值自动在缓存中的演员之间切换</td></tr>
</tbody >
</table >