---
locale: zh-rCN
layout: single
title: 图形
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

# 图形

## 

| Setting | Value | Description |
| :--- | --- | :--- |
|**图形** | | 
| 抗锯齿 |  No AA,  **Deferred SMAA**,  Deferred TAA,  |  |
|**光线追踪** | | 
| (Enable Raytracing) | ON | 
| 反射 | ON | 
| 环境光遮蔽 | ON | 
| 全局光照 | ON | 
| 阴影 | ON | 
| 接触阴影 | OFF | 
|- 光线长度| [50] (0 ~ 100) | 
| 去噪 | ON | 
|- 去噪半径| [0.1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
| 超采样 |  **Off**,  DLSS Performance,  DLSS Balance,  DLSS Quality,  DLSS Ultra Performance,  FSR 50%,  FSR 66%,  FSR 75%,  FSR 100%,  |  |
|**反射** | | 
| (Enable Reflection) | ON | 
|- 模式|  **Screen Space**,  | 
|- 质量|  Low,  Medium,  **High**,  | 
|- 算法|  **Approximation**,  | 用于屏幕空间反射的算法。
|- 边缘渐变距离| [0.1] (0 ~ 1) | 
|- 物体厚度| [0.01] (0 ~ 0.1) | 
| 回退到天空 | ON | 当光线追踪没有命中时回退到天空颜色。
| 天空反射 | ON | 
| 重置 || 
| (Confirm Reset) || 
|
|**雾** | | 
| (Enable Fog) | ON | 
| 体积雾 | ON | 
|- 基础高度| [0] (0 ~ 10) | 
|- 最大高度| [25] (10 ~ 100) | 
|- 最大距离| [5000] (0 ~ 10000) | 
| 重置 || 
| (Confirm Reset) || 
|
|**环境光遮蔽** | | 
| (Enable Ambient Occlusion) | OFF | 
|- 质量|  Low,  Medium,  **High**,  | 
|- 强度| [1] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**全局光照** | | 
| (Enable Global Illumination) | OFF | 
|- 质量|  **Low**,  | 
| 回退到天空 | ON | 
| 重置 || 
| (Confirm Reset) || 
|
|**景深** | | 
| (Enable Depth Of Field) | OFF | 
|- 质量|  Low,  **Medium**,  | 
|- 强度| [0.25] (0 ~ 1) | 
|- 偏移| [0.1] (-1 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**运动模糊** | | 
| (Enable Motion Blur) | OFF | 
|- 质量|  Low,  **Medium**,  | 
|- 强度| [0.25] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**辉光** | | 
| (Enable Bloom) | ON | 
|- 质量|  Low,  Medium,  **High**,  | 
|- 强度| [0.25] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**镜头光晕** | | 
| (Enable Lens Flare) | ON | 
| 在 VR 中禁用 | ON | 不推荐在 VR 中使用此效果
|- 强度| [0.1] (0 ~ 1) | 
|**颜色** | | 
|- 颜色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 饱和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 红色| [1] (0 ~ 1) | 
|- 绿色| [1] (0 ~ 1) | 
|- 蓝色| [1] (0 ~ 1) | 
| 使用舞台颜色 | OFF | 使用舞台环的颜色
|- 色温| [6500] (3000 ~ 8000) | 
| 预设 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 光晕| [1] (0 ~ 1) | 
|- 条纹| [0.2] (0 ~ 1) | 
|- 长度| [0.5] (0 ~ 1) | 
|- 色差| [0.5] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**颜色调整** | | 
| (Enable Color Adjustment) | ON | 
|- 后期曝光| [0] (-12 ~ 12) | 
|- 对比度| [1] (-100 ~ 100) | 
|- 色相偏移| [0] (-180 ~ 180) | 
|- 饱和度| [1] (-100 ~ 100) | 
|**颜色滤镜** | | 
|- 颜色模式|  RGB,  **HSV**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 饱和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 红色| [1] (0 ~ 1) | 
|- 绿色| [1] (0 ~ 1) | 
|- 蓝色| [1] (0 ~ 1) | 
|- 发光| [1] (0 ~ 20) | 
| 预设 |  **White**,  Red,  Green,  Blue,  Animated Hue,  Glow w/ Music,  |  |
|
| 重置 || 
| (Confirm Reset) || 
|
|**颜色曲线** | | 
| (Enable Color Curve) | ON | 
|- 起始渐变| [1] (0 ~ 4) | 
|- 起始位置| [0] (0 ~ 0.5) | 
|- 起始值| [0] (0 ~ 0.5) | 
|- 结束渐变| [1] (0 ~ 4) | 
|- 结束位置| [1] (0.5 ~ 1) | 
|- 结束值| [1] (0.5 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**白平衡** | | 
| (Enable White Balance) | ON | 
|- 温度| [0] (-100 ~ 100) | 
|- 色调| [0] (-100 ~ 100) | 
| 重置 || 
| (Confirm Reset) || 
|
|**特殊渲染** | | 
| (Enable Special Render) | OFF | 
|- 模式|  **Depth Output**,  | 
|- 深度范围| [1] (0 ~ 1) | 
|- 深度缩放| [0.25] (0 ~ 1) | 
|- 法线缩放| [1] (0 ~ 1) | 
|- 法线混合| [0] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|- 色调映射|  None,  Neutral,  ACES,  **Custom**,  | 
| 演员卡通着色 | OFF | 对所有角色使用卡通着色。
| 阶段卡通着色 | OFF | 对场景和道具使用卡通着色。
|**选项** | | 
| 透明预处理 | ON | 启用透明预处理。这将使被遮挡的透明材质不可见。
| 屏幕空间阴影 | ON | 
| 接触阴影 | OFF | 小细节的阴影。
|- 凹凸贴图阴影| [0.5] (0 ~ 1) | 为凹凸贴图和细节贴图启用阴影。
| 停止 NaN | ON | (Prevent black screen when error happens during post processing. )
| 计算厚度 | ON | 计算可用于皮肤效果的厚度。
| 重置 || 
| (Confirm Reset) || 
|
| 预设 |  Performance,  Medium,  **High**,  Indoor GI,  Outdoor GI,  Toon Effect,  |  |
|
