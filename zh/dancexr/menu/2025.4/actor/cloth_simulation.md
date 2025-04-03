---
locale: zh-rCN
layout: single
title: 仿真
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[专业版](../menu#专业版) > 仿真



| Setting | Value | Description |
| :--- | --- | :--- |
| 启用 | ON | 
| 重置 || 
| **布料 1** | | 
| ├&nbsp;启用 | OFF | 
| ├&nbsp;重建网格 || 大多数参数需要重建网格才能生效。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;拓扑 | **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
| ├&nbsp;绳索连接 | [4] (1 ~ 10) | 
| ├&nbsp;内半径 | [0.08] (0 ~ 0.2) | 内圆半径（米）
| ├&nbsp;斜率 | [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
| ├&nbsp;弧度 | [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
| ├&nbsp;长度 | [0.25] (0 ~ 0.75) | 长度（米）
| ├&nbsp;手臂孔 | [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
| ├&nbsp;后长 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;侧长 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平分辨率 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直分辨率 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距离约束的合规性 | [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV 映射 | **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
| ├&nbsp;**锚点** | | 
| │&nbsp;├&nbsp;顶层 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**顶部锚点** | | 
| │&nbsp;│&nbsp;├&nbsp;锚点选择 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;选择偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;锚点骨骼 | **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;锁定模式 | **无** | 无, 锁定, 锁定高度, 黏性,  |
| │&nbsp;│&nbsp;├&nbsp;锚点位置 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;锚点旋转 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;底层 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**底部锚点** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点选择 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;选择偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;锚点骨骼 | **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;交换侧面 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;锁定模式 | **无** | 无, 锁定, 锁定高度, 黏性,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点位置 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点旋转 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子属性** | | 
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;├&nbsp;粘性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;启用弯曲约束 | ON | 
| │&nbsp;├&nbsp;弯曲顺应性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;缩放 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自我碰撞 | OFF | 
| │&nbsp;├&nbsp;抓地质量 | [2] (0 ~ 4) | 抓地粒子的质量
| │&nbsp;├&nbsp;抓地摩擦 | [2] (-2 ~ 4) | 抓地粒子的摩擦
| │&nbsp;├&nbsp;抓地粘性 | [0.25] (0 ~ 1) | 抓地粒子的粘性
| │&nbsp;├&nbsp;抓地拖拽 | [0] (-2 ~ 2) | 抓地粒子的空气阻力
| │&nbsp;├&nbsp;抓地比例 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;启用撕裂 | OFF | 
| │&nbsp;├&nbsp;撕裂阈值 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
| └&nbsp;(Presets: Top) || 
| &nbsp;&nbsp;预设 | **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C1 材质** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;预设 | **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;玻璃模式 | OFF | 
| ├&nbsp;透明度作为光泽 | OFF | 
| ├&nbsp;双面 | ON | 
| ├&nbsp;暗背景 | [1] (0 ~ 1) | 
| ├&nbsp;投射阴影 | [0.5] (0 ~ 1) | 
| ├&nbsp;深度预处理 | [0.8] (0 ~ 1) | 
| ├&nbsp;光泽 | [0.3] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;混合模式 | **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;预设 | **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
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
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;纹理 | **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
| └&nbsp;**细节贴图** | | 
| &nbsp;&nbsp;├&nbsp;启用 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;启用 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;大小 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;凹凸 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;噪声 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;柔和边缘 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;选择贴图 | **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
| &nbsp;&nbsp;├&nbsp;细节贴图旋转 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;细节贴图缩放 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;细节贴图的凹凸 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响环境光遮蔽 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响光滑度 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响金属感 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响颜色混合 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;各向异性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP贴图偏差 | [0] (-5 ~ 5) | 调整细节纹理的锐度。
| **布料 2** | | 
| ├&nbsp;启用 | OFF | 
| ├&nbsp;重建网格 || 大多数参数需要重建网格才能生效。
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;拓扑 | **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
| ├&nbsp;绳索连接 | [4] (1 ~ 10) | 
| ├&nbsp;内半径 | [0.08] (0 ~ 0.2) | 内圆半径（米）
| ├&nbsp;斜率 | [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
| ├&nbsp;弧度 | [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
| ├&nbsp;长度 | [0.25] (0 ~ 0.75) | 长度（米）
| ├&nbsp;手臂孔 | [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
| ├&nbsp;后长 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;侧长 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;水平分辨率 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;垂直分辨率 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;距离约束的合规性 | [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV 映射 | **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
| ├&nbsp;**锚点** | | 
| │&nbsp;├&nbsp;顶层 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**顶部锚点** | | 
| │&nbsp;│&nbsp;├&nbsp;锚点选择 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;选择偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;锚点骨骼 | **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;锁定模式 | **无** | 无, 锁定, 锁定高度, 黏性,  |
| │&nbsp;│&nbsp;├&nbsp;锚点位置 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;锚点旋转 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;底层 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**底部锚点** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点选择 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;选择偏移 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;锚点骨骼 | **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;交换侧面 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;锁定模式 | **无** | 无, 锁定, 锁定高度, 黏性,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点位置 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;锚点旋转 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**粒子属性** | | 
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;├&nbsp;粘性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;启用弯曲约束 | ON | 
| │&nbsp;├&nbsp;弯曲顺应性 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;缩放 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;自我碰撞 | OFF | 
| │&nbsp;├&nbsp;抓地质量 | [2] (0 ~ 4) | 抓地粒子的质量
| │&nbsp;├&nbsp;抓地摩擦 | [2] (-2 ~ 4) | 抓地粒子的摩擦
| │&nbsp;├&nbsp;抓地粘性 | [0.25] (0 ~ 1) | 抓地粒子的粘性
| │&nbsp;├&nbsp;抓地拖拽 | [0] (-2 ~ 2) | 抓地粒子的空气阻力
| │&nbsp;├&nbsp;抓地比例 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;启用撕裂 | OFF | 
| │&nbsp;├&nbsp;撕裂阈值 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;限制撕裂速度 | [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
| └&nbsp;(Presets: Skirt) || 
| &nbsp;&nbsp;预设 | **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C2 材质** | | 
| ├&nbsp;表面 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;预设 | **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;玻璃模式 | OFF | 
| ├&nbsp;透明度作为光泽 | OFF | 
| ├&nbsp;双面 | ON | 
| ├&nbsp;暗背景 | [1] (0 ~ 1) | 
| ├&nbsp;投射阴影 | [0.5] (0 ~ 1) | 
| ├&nbsp;深度预处理 | [0.8] (0 ~ 1) | 
| ├&nbsp;光泽 | [0.3] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;混合模式 | **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;预设 | **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
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
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;纹理 | **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
| └&nbsp;**细节贴图** | | 
| &nbsp;&nbsp;├&nbsp;启用 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;启用 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;密度 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;大小 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;凹凸 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;噪声 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;柔和边缘 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;选择贴图 | **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
| &nbsp;&nbsp;├&nbsp;细节贴图旋转 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;细节贴图缩放 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;细节贴图的凹凸 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响环境光遮蔽 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响光滑度 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响金属感 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;影响颜色混合 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;各向异性 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP贴图偏差 | [0] (-5 ~ 5) | 调整细节纹理的锐度。
| 合并 | OFF | 将布料 1 和 2 合并为一个单一的仿真，这将允许两者之间的碰撞，但会变得较慢。
| **流体（实验性）** | | 
| ├&nbsp;启用 | OFF | 
| ├&nbsp;**生成** | | 
| │&nbsp;├&nbsp;**位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] ((Unlimited)) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [2.5] ((Unlimited)) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] ((Unlimited)) | 
| │&nbsp;├&nbsp;**旋转** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;生成半径 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;扩散 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;生成率 | [20] (0 ~ 20) | 
| │&nbsp;├&nbsp;速度 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;鼠标 / 手部控制 | OFF | 
| │&nbsp;├&nbsp;自动瞄准 | ON | 
| │&nbsp;├&nbsp;最大生存时间 | [10] (5 ~ 15) | 粒子在经过此时间后消失并重新生成。
| │&nbsp;├&nbsp;地面上的生存时间 | [0.1] (0 ~ 1) | 触及地面后的生存时间。
| │&nbsp;├&nbsp;平滑 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sprinkler) || 
| │&nbsp;&nbsp;&nbsp;预设 | **喷雾器** | 淋浴, 喷泉, 喷雾器, 手持式,  |
| ├&nbsp;**流体** | | 
| │&nbsp;├&nbsp;凝聚 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;粘度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;粘附在表面 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;目标密度 | [2] (1 ~ 10) | 
| │&nbsp;├&nbsp;凝聚范围 | [20] (1 ~ 50) | 凝聚效果的最大距离
| │&nbsp;├&nbsp;目标距离 | [10] (1 ~ 20) | 在关闭凝聚时粒子之间的最小距离（以毫米计）。
| │&nbsp;├&nbsp;高度 | [0.25] (0 ~ 0.5) | 根据其大小提升粒子
| │&nbsp;└&nbsp;(Presets: Water) || 
| │&nbsp;&nbsp;&nbsp;预设 | **水** | 水, 粘稠, 沙子,  |
| ├&nbsp;**渲染** | | 
| │&nbsp;├&nbsp;渲染粒子 | ON | 
| │&nbsp;├&nbsp;渲染液滴 | OFF | 
| │&nbsp;├&nbsp;液滴大小 | [2] (0 ~ 50) | 液滴大小（以毫米计）
| │&nbsp;├&nbsp;按密度缩放 | [0] (0 ~ 5) | 根据流体的密度缩放液滴大小
| │&nbsp;├&nbsp;**颜色** | | 
| │&nbsp;│&nbsp;├&nbsp;颜色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;│&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;饱和度 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;红色 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;绿色 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;蓝色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;金属质感 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;平滑度 | [0.95] (0 ~ 1) | 
| │&nbsp;├&nbsp;发光 | [0] (0 ~ 1) | 
| │&nbsp;└&nbsp;透明度 | [0.1] (0 ~ 1) | 
| ├&nbsp;**粒子属性** | | 
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;拖拽（空气） | [-2] (0 ~ 2) | 空气阻力
| │&nbsp;├&nbsp;拖拽（水下） | [-2] (0 ~ 2) | 水下阻力
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;├&nbsp;风的影响 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）,  |
| **几何体碰撞器** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;可见 | OFF | 
| ├&nbsp;导出形状 || 
| ├&nbsp;**头部** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.04] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.5] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**脖子** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.065] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**胸部** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.023] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.04] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [0.88] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.7] (0 ~ 1) | 
| ├&nbsp;**肋骨** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.075] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**腰部** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.032] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [-0.3] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.8] (0 ~ 1) | 
| ├&nbsp;**腹部** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.013] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.073] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.65] (0 ~ 1) | 
| ├&nbsp;**臀部** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.0425] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.105] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.012] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.09] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**肩膀** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [-0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.4] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**上臂** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.15] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.035] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**下臂** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.0445] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.44] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.01] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**手** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.0315] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [-0.0316] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**臀部（髋部）** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.027] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.1] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.1] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.085] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**大腿** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.073] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.05599999] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**小腿** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.05926838] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;中间位置 || 
| │&nbsp;├&nbsp;(X) | [0.009999919] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05999992] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01666657] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;中间半径 | [0.06707321] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;中间曲线 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.03231711] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**脚** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;起始位置 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.03166673] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;起始半径 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;曲线 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;结束位置 || 
| │&nbsp;├&nbsp;(X) | [0.028] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;结束半径 | [0.0625] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;缩放 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| **网格碰撞体** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;禁用几何碰撞体 | ON | 
| ├&nbsp;可视化 | OFF | 
| ├&nbsp;深度 | [0.025] (0 ~ 0.1) | 
| ├&nbsp;(Skip Edge) | ON | 
| ├&nbsp;(Skip Point) | ON | 
| └&nbsp;(Single Collision) | ON | 
| **模拟设置** | | 
| ├&nbsp;启用拖动 | ON | 
| ├&nbsp;重置比例 | [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。
| ├&nbsp;模拟 | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| ├&nbsp;子步 | [4] (1 ~ 20) | 
| ├&nbsp;迭代 | [1] (0 ~ 10) | 
| ├&nbsp;反向偶数子步 | OFF | 
| ├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| ├&nbsp;表格大小 | [6] (1 ~ 20) | 
| └&nbsp;两步求解 | OFF | 
| (Presets: Default (Reset)) || 
| 预设 | **默认（重置）** | 默认（重置）,  |
