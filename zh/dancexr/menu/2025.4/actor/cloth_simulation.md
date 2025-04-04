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
|<nobr>启用</nobr>| [ON] | 
|<nobr>重置</nobr>|| 
|<nobr><b>布料 1</b></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [OFF] | 
|<nobr>├&nbsp;重建网格</nobr>|| 大多数参数需要重建网格才能生效。
|<nobr>├&nbsp;拓扑</nobr>| **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
|<nobr>├&nbsp;绳索连接</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;内半径</nobr>| [0.08] (0 ~ 0.2) | 内圆半径（米）
|<nobr>├&nbsp;斜率</nobr>| [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
|<nobr>├&nbsp;弧度</nobr>| [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
|<nobr>├&nbsp;长度</nobr>| [0.25] (0 ~ 0.75) | 长度（米）
|<nobr>├&nbsp;手臂孔</nobr>| [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
|<nobr>├&nbsp;(Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
|<nobr>├&nbsp;后长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;侧长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;水平分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;垂直分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;距离约束的合规性</nobr>| [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
|<nobr>├&nbsp;UV 映射</nobr>| **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
|<nobr>├&nbsp;<b>锚点</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;顶层</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<b>顶部锚点</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锚点骨骼</nobr>| **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>锚点位置</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>锚点旋转</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;底层</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<b>底部锚点</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锚点骨骼</nobr>| **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;交换侧面</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<b>锚点位置</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<b>锚点旋转</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;<b>粒子属性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;粘性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;启用弯曲约束</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;弯曲顺应性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;缩放</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;自我碰撞</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;抓地质量</nobr>| [2] (0 ~ 4) | 抓地粒子的质量
|<nobr>│&nbsp;├&nbsp;抓地摩擦</nobr>| [2] (-2 ~ 4) | 抓地粒子的摩擦
|<nobr>│&nbsp;├&nbsp;抓地粘性</nobr>| [0.25] (0 ~ 1) | 抓地粒子的粘性
|<nobr>│&nbsp;├&nbsp;抓地拖拽</nobr>| [0] (-2 ~ 2) | 抓地粒子的空气阻力
|<nobr>│&nbsp;├&nbsp;抓地比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;启用撕裂</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;撕裂阈值</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
|<nobr>└&nbsp;预设</nobr>| **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr><b>C1 材质</b></nobr>| | 
|<nobr>├&nbsp;<b>表面</b></nobr>|| 
|<nobr>├&nbsp;预设</nobr>| **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;玻璃模式</nobr>| [OFF] | 
|<nobr>├&nbsp;透明度作为光泽</nobr>| [OFF] | 
|<nobr>├&nbsp;双面</nobr>| [ON] | 
|<nobr>├&nbsp;暗背景</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;投射阴影</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;深度预处理</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;光泽</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;凹凸</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;发光</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;环境光</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;透明度</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;剪切</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<b>颜色</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;红色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;绿色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;混合模式</nobr>| **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
|<nobr>├&nbsp;<b>卡通着色器</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;着色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;轮廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;高光</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;高光区域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;环境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;阴影区域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;阴影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和阴影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
|<nobr>├&nbsp;<b>特效着色器</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;模式</nobr>| **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;厚度</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;纹理</nobr>| **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
|<nobr>└&nbsp;<b>细节贴图</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;大小</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;凹凸</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;噪声</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;柔和边缘</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;选择贴图</nobr>| **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图旋转</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图缩放</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图的凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响环境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响金属感</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响颜色混合</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;各向异性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIP贴图偏差</nobr>| [0] (-5 ~ 5) | 调整细节纹理的锐度。
|<nobr><b>布料 2</b></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [OFF] | 
|<nobr>├&nbsp;重建网格</nobr>|| 大多数参数需要重建网格才能生效。
|<nobr>├&nbsp;拓扑</nobr>| **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
|<nobr>├&nbsp;绳索连接</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp;内半径</nobr>| [0.08] (0 ~ 0.2) | 内圆半径（米）
|<nobr>├&nbsp;斜率</nobr>| [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
|<nobr>├&nbsp;弧度</nobr>| [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
|<nobr>├&nbsp;长度</nobr>| [0.25] (0 ~ 0.75) | 长度（米）
|<nobr>├&nbsp;手臂孔</nobr>| [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
|<nobr>├&nbsp;(Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
|<nobr>├&nbsp;后长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;侧长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp;水平分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;垂直分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp;距离约束的合规性</nobr>| [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
|<nobr>├&nbsp;UV 映射</nobr>| **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
|<nobr>├&nbsp;<b>锚点</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;顶层</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;<b>顶部锚点</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锚点骨骼</nobr>| **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>锚点位置</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>锚点旋转</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;底层</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;<b>底部锚点</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锚点骨骼</nobr>| **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;交换侧面</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<b>锚点位置</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;<b>锚点旋转</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;(Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;<b>粒子属性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;粘性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;启用弯曲约束</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;弯曲顺应性</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;缩放</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;自我碰撞</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;抓地质量</nobr>| [2] (0 ~ 4) | 抓地粒子的质量
|<nobr>│&nbsp;├&nbsp;抓地摩擦</nobr>| [2] (-2 ~ 4) | 抓地粒子的摩擦
|<nobr>│&nbsp;├&nbsp;抓地粘性</nobr>| [0.25] (0 ~ 1) | 抓地粒子的粘性
|<nobr>│&nbsp;├&nbsp;抓地拖拽</nobr>| [0] (-2 ~ 2) | 抓地粒子的空气阻力
|<nobr>│&nbsp;├&nbsp;抓地比例</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;启用撕裂</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;撕裂阈值</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp;限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
|<nobr>└&nbsp;预设</nobr>| **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr><b>C2 材质</b></nobr>| | 
|<nobr>├&nbsp;<b>表面</b></nobr>|| 
|<nobr>├&nbsp;预设</nobr>| **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp;玻璃模式</nobr>| [OFF] | 
|<nobr>├&nbsp;透明度作为光泽</nobr>| [OFF] | 
|<nobr>├&nbsp;双面</nobr>| [ON] | 
|<nobr>├&nbsp;暗背景</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;投射阴影</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;深度预处理</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;光泽</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp;金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;凹凸</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;发光</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;环境光</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;透明度</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;剪切</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;<b>颜色</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;红色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;绿色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;混合模式</nobr>| **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp;混合</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
|<nobr>├&nbsp;<b>卡通着色器</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;着色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;轮廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;高光</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;高光区域</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;环境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;阴影区域</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;阴影</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;柔和阴影</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
|<nobr>├&nbsp;<b>特效着色器</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;模式</nobr>| **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
|<nobr>│&nbsp;├&nbsp;折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp;厚度</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;纹理</nobr>| **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
|<nobr>└&nbsp;<b>细节贴图</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;<b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;密度</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;大小</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;凹凸</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;噪声</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;柔和边缘</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;选择贴图</nobr>| **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图旋转</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图缩放</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;细节贴图的凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响环境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响金属感</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;影响颜色混合</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;各向异性</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp;MIP贴图偏差</nobr>| [0] (-5 ~ 5) | 调整细节纹理的锐度。
|<nobr>合并</nobr>| [OFF] | 将布料 1 和 2 合并为一个单一的仿真，这将允许两者之间的碰撞，但会变得较慢。
|<nobr><b>流体（实验性）</b></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>生成</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;<b>位置</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;├&nbsp;<b>旋转</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp;生成半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;扩散</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;生成率</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;速度</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;鼠标 / 手部控制</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;自动瞄准</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;最大生存时间</nobr>| [10] (5 ~ 15) | 粒子在经过此时间后消失并重新生成。
|<nobr>│&nbsp;├&nbsp;地面上的生存时间</nobr>| [0.1] (0 ~ 1) | 触及地面后的生存时间。
|<nobr>│&nbsp;├&nbsp;平滑</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **喷雾器** | 淋浴, 喷泉, 喷雾器, 手持式,  |
|<nobr>├&nbsp;<b>流体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;凝聚</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粘度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粘附在表面</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;目标密度</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;凝聚范围</nobr>| [20] (1 ~ 50) | 凝聚效果的最大距离
|<nobr>│&nbsp;├&nbsp;目标距离</nobr>| [10] (1 ~ 20) | 在关闭凝聚时粒子之间的最小距离（以毫米计）。
|<nobr>│&nbsp;├&nbsp;高度</nobr>| [0.25] (0 ~ 0.5) | 根据其大小提升粒子
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **水** | 水, 粘稠, 沙子,  |
|<nobr>├&nbsp;<b>渲染</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;渲染粒子</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;渲染液滴</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;液滴大小</nobr>| [2] (0 ~ 50) | 液滴大小（以毫米计）
|<nobr>│&nbsp;├&nbsp;按密度缩放</nobr>| [0] (0 ~ 5) | 根据流体的密度缩放液滴大小
|<nobr>│&nbsp;├&nbsp;<b>颜色</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;│&nbsp;├&nbsp;色相</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;亮度</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;红色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;绿色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;平滑度</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;发光</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>粒子属性</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [-2] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [-2] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [OFF] | 
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）,  |
|<nobr><b>几何体碰撞器</b></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;可见</nobr>| [OFF] | 
|<nobr>├&nbsp;导出形状</nobr>|| 
|<nobr>├&nbsp;<b>头部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>脖子</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>胸部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp;<b>肋骨</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>腰部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp;<b>腹部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp;<b>臀部</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>肩膀</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>上臂</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>下臂</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>手</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>臀部（髋部）</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>大腿</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>小腿</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>中间位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;中间半径</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;中间曲线</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>脚</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>起始位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;起始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;<b>结束位置</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;(Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp;结束半径</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp;<b>缩放</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr><b>网格碰撞体</b></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;禁用几何碰撞体</nobr>| [ON] | 
|<nobr>├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>├&nbsp;深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp;(Skip Edge)</nobr>| [ON] | 
|<nobr>├&nbsp;(Skip Point)</nobr>| [ON] | 
|<nobr>└&nbsp;(Single Collision)</nobr>| [ON] | 
|<nobr><b>模拟设置</b></nobr>| | 
|<nobr>├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>├&nbsp;重置比例</nobr>| [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。
|<nobr>├&nbsp;模拟</nobr>| [ON] | 
|<nobr>├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;两步求解</nobr>| [OFF] | 
|<nobr>预设</nobr>| **默认（重置）** | 默认（重置）,  |
