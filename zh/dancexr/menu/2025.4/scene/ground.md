---
locale: zh-rCN
layout: single
title: 地面
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/scene/ground) | [繁中](/tw/dancexr/menu/2025.4/scene/ground) | [日本語](/jp/dancexr/menu/2025.4/scene/ground) | [한국어](/kr/dancexr/menu/2025.4/scene/ground) | [简中](/zh/dancexr/menu/2025.4/scene/ground)

[环境](../menu#环境) > 地面



| Setting | Value | Description |
| :--- | --- | :--- |
| 地面高度 | [0] (-2 ~ 2) | 
| 地面 | OFF | 
| 半径 | [200] (2 ~ 100) | 地面网格的大小
| 如果有舞台则隐藏 | ON | 当有舞台模型时隐藏地面
| **表面** | | 
| ├&nbsp;(Texture: [Tiles]) || 
| │&nbsp;纹理 | **[瓷砖]** | [天空贴图], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
| ├&nbsp;**镶嵌** | | 
| │&nbsp;├&nbsp;镶嵌 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;镶嵌 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重复 | 重复, 镜像 U, 镜像 V, 镜像两者, 
| │&nbsp;├&nbsp;X轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋转 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;变化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;适应纹理 | OFF | 
| ├&nbsp;光泽 | [0.95] (0 ~ 1) | 
| ├&nbsp;金属质感 | [0] (0 ~ 1) | 
| ├&nbsp;凹凸 | [0.2] (0 ~ 1) | 
| ├&nbsp;发光 | [0] (0 ~ 10) | 
| ├&nbsp;环境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪切 | [0] (0 ~ 1) | 
| ├&nbsp;**颜色** | | 
| │&nbsp;├&nbsp;颜色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;饱和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;红色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;绿色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;蓝色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Blend) || 
| │&nbsp;│&nbsp;混合模式 | **混合** | 原始模型, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Black) || 
| │&nbsp;&nbsp;&nbsp;预设 | **黑色** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
| ├&nbsp;**卡通着色器** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;着色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;轮廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光区域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;环境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影区域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和阴影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;预设 | **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
| ├&nbsp;**特效着色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;观察者高度 | [1.5] (0.5 ~ 3) | 投影到地面时使用的观察者高度
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和边缘 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;视角 | [1] (0 ~ 8) | 从一个角度观看时减少亮度。0 = 完美
| │&nbsp;├&nbsp;边缘 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;减少摩尔纹 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Black Gloss) || 
| &nbsp;&nbsp;预设 | **黑色光泽** | 天空贴图, 木材, 混凝土, 蓝色瓷砖, 投影仪屏幕, 自发光屏幕, LED 屏幕, 黑色光泽, 发光, 玻璃,  |
| **仅影子** | | 
| ├&nbsp;阴影颜色 || 
| ├&nbsp;(Presets: Black) || 
| │&nbsp;预设 | **黑色** | 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange), (Preset 1),  |
| ├&nbsp;颜色模式 | (RGB) | (RGB), (HSV), 
| ├&nbsp;色相 | [0] (0 ~ 1) | 
| ├&nbsp;饱和度 | [0] (0 ~ 1) | 
| ├&nbsp;亮度 | [0] (0 ~ 1) | 
| ├&nbsp;红色 | [0] (0 ~ 1) | 
| ├&nbsp;绿色 | [0] (0 ~ 1) | 
| ├&nbsp;蓝色 | [0] (0 ~ 1) | 
| └&nbsp;透明度 | [0.5] (0 ~ 1) | 
| 舞台 / 池塘 | OFF | 
| (Presets: Off) || 
| 预设 | **关闭** | 关闭, 跑道, 水池, 房间, 背景板, 投影仪屏幕, LED 屏幕,  |
| 提升 | [0.5] (-2 ~ 2) | 上下提升舞台
| (Front / Back Offset) | [0] (-10 ~ 10) | 
| **形状** | | 
| ├&nbsp;中心宽度 | [8] (0 ~ 10) | 中心区域的宽度
| ├&nbsp;中心深度 | [5] (0 ~ 9) | 中心区域的深度
| ├&nbsp;后高 | [0] (0 ~ 9) | 背景板的高度
| ├&nbsp;侧面延伸 | [0] (0 ~ 5) | 左右两侧的延伸
| ├&nbsp;前面延伸 | [0] (0 ~ 10) | 前面的延伸
| ├&nbsp;后面延伸 | [0] (0 ~ 10) | 后面的延伸
| ├&nbsp;墙高 | [0.05] (0 ~ 5) | 离地边缘的高度
| ├&nbsp;墙厚 | [0.1] (0 ~ 1) | 边缘的大小
| ├&nbsp;窗户 | [0] (0 ~ 1) | 
| └&nbsp;漂浮 | OFF | 
| **表面** | | 
| ├&nbsp;(Texture: [Wood1]) || 
| │&nbsp;纹理 | **[木材1]** | [空白], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
| ├&nbsp;**镶嵌** | | 
| │&nbsp;├&nbsp;镶嵌 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;镶嵌 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重复 | 重复, 镜像 U, 镜像 V, 镜像两者, 
| │&nbsp;├&nbsp;X轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋转 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;变化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;适应纹理 | OFF | 
| ├&nbsp;光泽 | [0.95] (0 ~ 1) | 
| ├&nbsp;金属质感 | [0] (0 ~ 1) | 
| ├&nbsp;凹凸 | [0.2] (0 ~ 1) | 
| ├&nbsp;发光 | [0] (0 ~ 10) | 
| ├&nbsp;环境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪切 | [0] (0 ~ 1) | 
| ├&nbsp;**颜色** | | 
| │&nbsp;├&nbsp;颜色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;饱和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;红色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;绿色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;蓝色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Blend) || 
| │&nbsp;│&nbsp;混合模式 | **混合** | 原始模型, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: White) || 
| │&nbsp;&nbsp;&nbsp;预设 | **白色** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
| ├&nbsp;**卡通着色器** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;着色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;轮廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光区域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;环境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影区域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和阴影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;预设 | **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
| ├&nbsp;**特效着色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和边缘 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;视角 | [1] (0 ~ 8) | 从一个角度观看时减少亮度。0 = 完美
| │&nbsp;├&nbsp;边缘 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;减少摩尔纹 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Wood) || 
| &nbsp;&nbsp;预设 | **木材** | 空白, 木材, 混凝土, 蓝色瓷砖, 投影仪屏幕, 自发光屏幕, LED 屏幕, 黑色光泽, 发光, 玻璃,  |
| **后表面** | | 
| ├&nbsp;(Texture: [Blank]) || 
| │&nbsp;纹理 | **[空白]** | [空白], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
| ├&nbsp;**镶嵌** | | 
| │&nbsp;├&nbsp;镶嵌 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;镶嵌 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重复 | 重复, 镜像 U, 镜像 V, 镜像两者, 
| │&nbsp;├&nbsp;X轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y轴偏移 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋转 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;变化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;适应纹理 | ON | 
| ├&nbsp;光泽 | [0.95] (0 ~ 1) | 
| ├&nbsp;金属质感 | [0] (0 ~ 1) | 
| ├&nbsp;凹凸 | [0.2] (0 ~ 1) | 
| ├&nbsp;发光 | [0] (0 ~ 10) | 
| ├&nbsp;环境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪切 | [0] (0 ~ 1) | 
| ├&nbsp;**颜色** | | 
| │&nbsp;├&nbsp;颜色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;饱和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;红色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;绿色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;蓝色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Original) || 
| │&nbsp;│&nbsp;混合模式 | **原始模型** | 原始模型, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: White) || 
| │&nbsp;&nbsp;&nbsp;预设 | **白色** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
| ├&nbsp;**卡通着色器** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;着色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;轮廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光区域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;环境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影区域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;阴影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和阴影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;预设 | **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
| ├&nbsp;**特效着色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和边缘 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;视角 | [1] (0 ~ 8) | 从一个角度观看时减少亮度。0 = 完美
| │&nbsp;├&nbsp;边缘 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;减少摩尔纹 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Blank) || 
| &nbsp;&nbsp;预设 | **空白** | 空白, 木材, 混凝土, 蓝色瓷砖, 投影仪屏幕, 自发光屏幕, LED 屏幕, 黑色光泽, 发光, 玻璃,  |
| 水系统 | OFF | 
| (Presets: Off) || 
| 预设 | **关闭** | 关闭, 水池, (Still Water), 海洋,  |
| 类型 | 水池 | 水池, 河流, 海洋, 
| 高度 | [-0.1] (-2 ~ 2) | 水位高度
| 涟漪 | [3] (0 ~ 10) | 小波浪强度
| 大波浪 | [30] (0 ~ 100) | 大波浪强度
| 折射最大距离 | [0.35] (0 ~ 3.5) | 控制用于限制水下折射深度的最大距离（以米为单位）。较高的值会增加扭曲量。
| 吸收距离 | [5] (1 ~ 10) | 从上方可以看到的水中的最大距离。
| 光晕 | [0.5] (0 ~ 1) | 光晕效果
| 吸收倍增器 | [2] (0 ~ 5) | 从下方查看时应用于吸收距离的倍增。
| (Presets: Black Gloss) || 
| 预设 | **黑色光泽** | 天空贴图, 黑色光泽, 舞台, 水池, 海洋, 背景板, 投影仪屏幕, 自发光屏幕, (Preset 1),  |
