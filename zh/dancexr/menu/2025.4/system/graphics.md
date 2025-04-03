---
locale: zh-rCN
layout: single
title: 图形
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[系统](../menu#系统) > 图形



| Setting | Value | Description |
| :--- | --- | :--- |
| (Anti-Aliasing: Deferred SMAA) || 0/18/True
| 抗锯齿 | **延迟 SMAA** | 无抗锯齿, 延迟 SMAA, 延迟 TAA,  |
| **光线追踪** | | 1/18/True
| ├ (Enable Raytracing) | ON | 0/8/False
| ├ 反射 | ON | 1/8/False
| ├ 环境光遮蔽 | ON | 2/8/False
| ├ 全局光照 | ON | 3/8/False
| ├ 阴影 | ON | 4/8/False
| ├ 接触阴影 | OFF | 5/8/False
| ├ 光线长度 | [50] (0 ~ 100) | 6/8/False
| ├ 去噪 | ON | 7/8/False
| └ 去噪半径 | [0.1] (0 ~ 1) | 8/8/False
| (Super Sampling: Off) || 2/18/True
| 超采样 | **关闭** | 关闭, DLSS 性能, DLSS 平衡, DLSS 质量, DLSS 超性能, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **反射** | | 3/18/True
| ├ (Enable Reflection) | ON | 0/7/False
| ├ 模式 | 屏幕空间 | 屏幕空间, 探头, 1/7/False
| ├ 质量 | 高 | 低, 中型, 高, 2/7/False
| ├ 算法 | 近似 | 近似, 基于物理的渲染积累, <br/>用于屏幕空间反射的算法。3/7/False
| ├ 边缘渐变距离 | [0.1] (0 ~ 1) | 4/7/False
| ├ 物体厚度 | [0.01] (0 ~ 0.1) | 5/7/False
| ├ 回退到天空 | ON | 当光线追踪没有命中时回退到天空颜色。6/7/False
| └ 天空反射 | ON | 7/7/False
| **雾** | | 4/18/True
| ├ (Enable Fog) | ON | 0/4/False
| ├ 体积雾 | ON | 1/4/False
| ├ 基础高度 | [0] (0 ~ 10) | 2/4/False
| ├ 最大高度 | [25] (10 ~ 100) | 3/4/False
| └ 最大距离 | [5000] (0 ~ 10000) | 4/4/False
| **环境光遮蔽** | | 5/18/True
| ├ (Enable Ambient Occlusion) | OFF | 0/2/False
| ├ 质量 | 高 | 低, 中型, 高, 1/2/False
| └ 强度 | [1] (0 ~ 1) | 2/2/False
| **全局光照** | | 6/18/True
| ├ (Enable Global Illumination) | OFF | 0/2/False
| ├ 质量 | 低 | 低, 中型, 高, 1/2/False
| └ 回退到天空 | ON | 2/2/False
| **景深** | | 7/18/True
| ├ (Enable Depth Of Field) | OFF | 0/3/False
| ├ 质量 | 中型 | 低, 中型, 高, 1/3/False
| ├ 强度 | [0.25] (0 ~ 1) | 2/3/False
| └ 偏移 | [0.1] (-1 ~ 1) | 3/3/False
| **运动模糊** | | 8/18/True
| ├ (Enable Motion Blur) | OFF | 0/2/False
| ├ 质量 | 中型 | 低, 中型, 高, 1/2/False
| └ 强度 | [0.25] (0 ~ 1) | 2/2/False
| **辉光** | | 9/18/True
| ├ (Enable Bloom) | ON | 0/2/False
| ├ 质量 | 高 | 低, 中型, 高, 1/2/False
| └ 强度 | [0.25] (0 ~ 1) | 2/2/False
| **镜头光晕** | | 10/18/True
| ├ (Enable Lens Flare) | ON | 0/7/False
| ├ 在 VR 中禁用 | ON | 不推荐在 VR 中使用此效果1/7/False
| ├ 强度 | [0.1] (0 ~ 1) | 2/7/False
| ├ **颜色** | | 3/7/False
| │ ├ 颜色模式 | (RGB) | (RGB), (HSV), 0/8/True
| │ ├ 色相 | [0] (0 ~ 1) | 1/8/True
| │ ├ 饱和度 | [0] (0 ~ 1) | 2/8/True
| │ ├ 亮度 | [1] (0 ~ 1) | 3/8/True
| │ ├ 红色 | [1] (0 ~ 1) | 4/8/True
| │ ├ 绿色 | [1] (0 ~ 1) | 5/8/True
| │ ├ 蓝色 | [1] (0 ~ 1) | 6/8/True
| │ ├ 使用舞台颜色 | OFF | 使用舞台环的颜色7/8/True
| │ ├ 色温 | [6500] (3000 ~ 8000) | 8/8/True
| │ └ 预设 | **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
| ├ 光晕 | [1] (0 ~ 1) | 4/7/False
| ├ 条纹 | [0.2] (0 ~ 1) | 5/7/False
| ├ 长度 | [0.5] (0 ~ 1) | 6/7/False
| └ 色差 | [0.5] (0 ~ 1) | 7/7/False
| **颜色调整** | | 11/18/True
| ├ (Enable Color Adjustment) | ON | 0/5/False
| ├ 后期曝光 | [0] (-12 ~ 12) | 1/5/False
| ├ 对比度 | [1] (-100 ~ 100) | 2/5/False
| ├ 色相偏移 | [0] (-180 ~ 180) | 3/5/False
| ├ 饱和度 | [1] (-100 ~ 100) | 4/5/False
| └ **颜色滤镜** | | 5/5/False
|   ├ 颜色模式 | (HSV) | (RGB), (HSV), 0/7/True
|   ├ 色相 | [0] (0 ~ 1) | 1/7/True
|   ├ 饱和度 | [0] (0 ~ 1) | 2/7/True
|   ├ 亮度 | [1] (0 ~ 1) | 3/7/True
|   ├ 红色 | [1] (0 ~ 1) | 4/7/True
|   ├ 绿色 | [1] (0 ~ 1) | 5/7/True
|   ├ 蓝色 | [1] (0 ~ 1) | 6/7/True
|   ├ 发光 | [1] (0 ~ 20) | 7/7/True
|   └ 预设 | **白色** | 白色, 红色, 绿色, 蓝色, 动画色相, 伴音乐的辉光,  |
| **颜色曲线** | | 12/18/True
| ├ (Enable Color Curve) | ON | 0/6/False
| ├ 起始渐变 | [1] (0 ~ 4) | 1/6/False
| ├ 起始位置 | [0] (0 ~ 0.5) | 2/6/False
| ├ 起始值 | [0] (0 ~ 0.5) | 3/6/False
| ├ 结束渐变 | [1] (0 ~ 4) | 4/6/False
| ├ 结束位置 | [1] (0.5 ~ 1) | 5/6/False
| └ 结束值 | [1] (0.5 ~ 1) | 6/6/False
| **白平衡** | | 13/18/True
| ├ (Enable White Balance) | ON | 0/2/False
| ├ 温度 | [0] (-100 ~ 100) | 1/2/False
| └ 色调 | [0] (-100 ~ 100) | 2/2/False
| **特殊渲染** | | 14/18/True
| ├ (Enable Special Render) | OFF | 0/5/False
| ├ 模式 | 深度输出 | 深度输出, 法线输出, 1/5/False
| ├ 深度范围 | [1] (0 ~ 1) | 2/5/False
| ├ 深度缩放 | [0.25] (0 ~ 1) | 3/5/False
| ├ 法线缩放 | [1] (0 ~ 1) | 4/5/False
| └ 法线混合 | [0] (0 ~ 1) | 5/5/False
| 色调映射 | 自定义 | 无, 中性, ACES, 自定义, 15/18/True
| 演员卡通着色 | OFF | 对所有角色使用卡通着色。16/18/True
| 阶段卡通着色 | OFF | 对场景和道具使用卡通着色。17/18/True
| **选项** | | 18/18/True
| ├ 透明预处理 | ON | 启用透明预处理。这将使被遮挡的透明材质不可见。0/5/False
| ├ 屏幕空间阴影 | ON | 1/5/False
| ├ 接触阴影 | OFF | 小细节的阴影。2/5/False
| ├ 凹凸贴图阴影 | [0.5] (0 ~ 1) | 为凹凸贴图和细节贴图启用阴影。3/5/False
| ├ 停止 NaN | ON | (Prevent black screen when error happens during post processing. )4/5/False
| └ 计算厚度 | ON | 计算可用于皮肤效果的厚度。5/5/False
| 预设 | **高** | 性能, 中型, 高, 室内全局光照, 室外全局光照, 卡通效果,  |
