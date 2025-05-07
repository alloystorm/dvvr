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
|<nobr> ☑ 启用</nobr>| [ON] | 
|<nobr> 重置</nobr>|| 
|<nobr> □ <b>布料 1</b></nobr>| | 
|<nobr>├─ □ 启用</nobr>| [OFF] | 
|<nobr>├─ 重建网格</nobr>|| 大多数参数需要重建网格才能生效。
|<nobr>├─ > 拓扑</nobr>| **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
|<nobr>├─ ⊖ 绳索连接</nobr>| [4] (1 ~ 10) | 
|<nobr>├─ ⊖ 内半径</nobr>| [0.08] (0 ~ 0.2) | 内圆半径（米）
|<nobr>├─ ⊖ 斜率</nobr>| [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
|<nobr>├─ ⊖ 弧度</nobr>| [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
|<nobr>├─ ⊖ 长度</nobr>| [0.25] (0 ~ 0.75) | 长度（米）
|<nobr>├─ ⊖ 手臂孔</nobr>| [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
|<nobr>├─ ⊖ (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
|<nobr>├─ ⊖ 后长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├─ ⊖ 侧长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├─ ⊖ 水平分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├─ ⊖ 垂直分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├─ ⊖ 距离约束的合规性</nobr>| [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
|<nobr>├─ > UV 映射</nobr>| **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
|<nobr>├─ ⚙️ <b>锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 顶层</nobr>| [2] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>顶部锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ > 锚点骨骼</nobr>| **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ > 锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ <b>锚点位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ <b>锚点旋转</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 底层</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>底部锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ 锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ 选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ > 锚点骨骼</nobr>| **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ □ 交换侧面</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ > 锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ <b>锚点位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ <b>锚点旋转</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├─ ⚙️ <b>粒子属性</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粘性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用弯曲约束</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 弯曲顺应性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 缩放</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 自我碰撞</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地质量</nobr>| [2] (0 ~ 4) | 抓地粒子的质量
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地摩擦</nobr>| [2] (-2 ~ 4) | 抓地粒子的摩擦
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地粘性</nobr>| [0.25] (0 ~ 1) | 抓地粒子的粘性
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地拖拽</nobr>| [0] (-2 ~ 2) | 抓地粒子的空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地比例</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 启用撕裂</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 撕裂阈值</nobr>| [2] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **(Top)** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ⚙️ <b>C1 材质</b></nobr>| | 
|<nobr>├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr>├─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├─ □ 玻璃模式</nobr>| [OFF] | 
|<nobr>├─ □ 透明度作为光泽</nobr>| [OFF] | 
|<nobr>├─ ☑ 双面</nobr>| [ON] | 
|<nobr>├─ ⊖ 暗背景</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ 投射阴影</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├─ □ 深度预处理</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├─ ⊖ 光泽</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├─ ⊖ 金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr>├─ ⊖ 凹凸</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├─ ⊖ 发光</nobr>| [0] (0 ~ 10) | 
|<nobr>├─ ⊖ 环境光</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ⊖ 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ⊖ 剪切</nobr>| [0] (0 ~ 1) | 
|<nobr>├─ ⚙️ <b>颜色</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 红色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 绿色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ > 混合模式</nobr>| **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 混合</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
|<nobr>├─ □ <b>卡通着色器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 着色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 轮廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 高光</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 高光区域</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 环境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 阴影区域</nobr>| [0.65] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 阴影</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和阴影</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
|<nobr>├─ ⚙️ <b>特效着色器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ > 模式</nobr>| **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ > 纹理</nobr>| **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
|<nobr>└─ ☑ <b>细节贴图</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 密度</nobr>| [2] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 大小</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 凹凸</nobr>| [0.5] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 噪声</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ (Use Circle)</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 柔和边缘</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ > 选择贴图</nobr>| **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图旋转</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图缩放</nobr>| [6] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图的凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响环境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响金属感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响颜色混合</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 各向异性</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─ ⊖ MIP贴图偏差</nobr>| [0] (-5 ~ 5) | 调整细节纹理的锐度。
|<nobr> □ <b>布料 2</b></nobr>| | 
|<nobr>├─ □ 启用</nobr>| [OFF] | 
|<nobr>├─ 重建网格</nobr>|| 大多数参数需要重建网格才能生效。
|<nobr>├─ > 拓扑</nobr>| **水平布局** | 自适应六边形, 自适应矩形, 水平布局, 横向绳索, 垂直布局, 垂直绳索,  |
|<nobr>├─ ⊖ 绳索连接</nobr>| [4] (1 ~ 10) | 
|<nobr>├─ ⊖ 内半径</nobr>| [0.08] (0 ~ 0.2) | 内圆半径（米）
|<nobr>├─ ⊖ 斜率</nobr>| [45] (0 ~ 90) | 沿长度扩展网格的角度。0 = 管状，90 = 平面圆。
|<nobr>├─ ⊖ 弧度</nobr>| [0] (-1 ~ 1) | 沿长度向外或向内的弧度。正值 = 气球形状，负值 = 钟形
|<nobr>├─ ⊖ 长度</nobr>| [0.25] (0 ~ 0.75) | 长度（米）
|<nobr>├─ ⊖ 手臂孔</nobr>| [0.5] (0 ~ 1) | 手臂孔相对于周长的大小
|<nobr>├─ ⊖ (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 手臂孔相对于总长度的高度
|<nobr>├─ ⊖ 后长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├─ ⊖ 侧长</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├─ ⊖ 水平分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├─ ⊖ 垂直分辨率</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├─ ⊖ 距离约束的合规性</nobr>| [0] (0 ~ 0.1) | 粒子之间距离约束的合规性
|<nobr>├─ > UV 映射</nobr>| **镜像缩放** | 圆形, 镜像缩放, 镜像实际, 包裹缩放, 包裹实际,  |
|<nobr>├─ ⚙️ <b>锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 顶层</nobr>| [2] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>顶部锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ > 锚点骨骼</nobr>| **躯干** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ > 锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ <b>锚点位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ <b>锚点旋转</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 底层</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>底部锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ 锚点选择</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ 选择偏移</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ > 锚点骨骼</nobr>| **腰部** | 腰部, 躯干, 臀部, 头部, 大腿, 小腿, 上臂, 前臂, 手, 胸部,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ □ 交换侧面</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ > 锁定模式</nobr>| **无** | 无, 锁定, 锁定高度, 黏性,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ <b>锚点位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ <b>锚点旋转</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ⊖ (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ⊖ (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├─ ⚙️ <b>粒子属性</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粘性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用弯曲约束</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 弯曲顺应性</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 缩放</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 自我碰撞</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地质量</nobr>| [2] (0 ~ 4) | 抓地粒子的质量
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地摩擦</nobr>| [2] (-2 ~ 4) | 抓地粒子的摩擦
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地粘性</nobr>| [0.25] (0 ~ 1) | 抓地粒子的粘性
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地拖拽</nobr>| [0] (-2 ~ 2) | 抓地粒子的空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 抓地比例</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 启用撕裂</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 撕裂阈值</nobr>| [2] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂后的冷却间隔（以帧为单位）
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **裙子** | 裙子, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ⚙️ <b>C2 材质</b></nobr>| | 
|<nobr>├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>表面</b></nobr>|| 
|<nobr>├─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **灰色哑光** | 原始模型, 灰色哑光, 半透明, 发光, 银色, 实心玻璃, 薄玻璃, 轮廓, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├─ □ 玻璃模式</nobr>| [OFF] | 
|<nobr>├─ □ 透明度作为光泽</nobr>| [OFF] | 
|<nobr>├─ ☑ 双面</nobr>| [ON] | 
|<nobr>├─ ⊖ 暗背景</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ 投射阴影</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├─ □ 深度预处理</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├─ ⊖ 光泽</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├─ ⊖ 金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr>├─ ⊖ 凹凸</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├─ ⊖ 发光</nobr>| [0] (0 ~ 10) | 
|<nobr>├─ ⊖ 环境光</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ⊖ 透明度</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ⊖ 剪切</nobr>| [0] (0 ~ 1) | 
|<nobr>├─ ⚙️ <b>颜色</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 红色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 绿色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ > 混合模式</nobr>| **(Multiply)** | 原始模型, (Multiply), 混合, (Color Shift),  |
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 混合</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **(Gray)** | 原始模型, 白色, 黑色, 红色, (Yellow), (Dark Gray), 蓝色, 皮肤, (Gray), (Orange),  |
|<nobr>├─ □ <b>卡通着色器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 着色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 轮廓</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 高光</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 高光区域</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和高光</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 环境光</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 阴影区域</nobr>| [0.65] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 阴影</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 柔和阴影</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **锐利** | 锐利, 柔和, 明亮, 平面 + 高光, 平面,  |
|<nobr>├─ ⚙️ <b>特效着色器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ > 模式</nobr>| **关闭** | 关闭, 厚折射, 薄折射, 轮廓, 未点亮, (Experiment),  |
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 折射</nobr>| [0.5] (1 ~ 3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 厚度</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ > 纹理</nobr>| **[纯色]** | [纯色], [木材1], [木材2], [瓷砖], [混凝土], [视频],  |
|<nobr>└─ ☑ <b>细节贴图</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 密度</nobr>| [2] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 大小</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 凹凸</nobr>| [0.5] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 噪声</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>├─ □ (Use Circle)</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 柔和边缘</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ > 选择贴图</nobr>| **面料 3** | 碳纤维, 皮革, 面料 1, 面料 2, 面料 3, 羊毛 1, 羊毛 2, 金属缎面, 金属拉丝, 头发,  |
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图旋转</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图缩放</nobr>| [6] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 细节贴图的凹凸</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响环境光遮蔽</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响光滑度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响金属感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 影响颜色混合</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>├─ ⊖ 各向异性</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─ ⊖ MIP贴图偏差</nobr>| [0] (-5 ~ 5) | 调整细节纹理的锐度。
|<nobr> □ 合并</nobr>| [OFF] | 将布料 1 和 2 合并为一个单一的仿真，这将允许两者之间的碰撞，但会变得较慢。
|<nobr> □ <b>流体（实验性）</b></nobr>| | 
|<nobr>├─ □ 启用</nobr>| [OFF] | 
|<nobr>├─ ⚙️ <b>生成</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>位置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>旋转</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 生成半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 扩散</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 生成率</nobr>| [20] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 速度</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 鼠标 / 手部控制</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 自动瞄准</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 最大生存时间</nobr>| [10] (5 ~ 15) | 粒子在经过此时间后消失并重新生成。
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 地面上的生存时间</nobr>| [0.1] (0 ~ 1) | 触及地面后的生存时间。
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 平滑</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **喷雾器** | 淋浴, 喷泉, 喷雾器, 手持式,  |
|<nobr>├─ ⚙️ <b>流体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 凝聚</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粘度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 粘附在表面</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 目标密度</nobr>| [2] (1 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 凝聚范围</nobr>| [20] (1 ~ 50) | 凝聚效果的最大距离
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 目标距离</nobr>| [10] (1 ~ 20) | 在关闭凝聚时粒子之间的最小距离（以毫米计）。
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 高度</nobr>| [0.25] (0 ~ 0.5) | 根据其大小提升粒子
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **水** | 水, 粘稠, 沙子,  |
|<nobr>├─ ⚙️ <b>渲染</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 渲染粒子</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ □ 渲染液滴</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 液滴大小</nobr>| [2] (0 ~ 50) | 液滴大小（以毫米计）
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 按密度缩放</nobr>| [0] (0 ~ 5) | 根据流体的密度缩放液滴大小
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>颜色</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ☑ 颜色模式</nobr>| (RGB) | (RGB), (HSV), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 色相</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 饱和度</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 亮度</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 红色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 绿色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 蓝色</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 金属质感</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 平滑度</nobr>| [0.95] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 发光</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 透明度</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├─ ⚙️ <b>粒子属性</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 摩擦力</nobr>| [0] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 地面摩擦</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（空气）</nobr>| [-2] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 拖拽（水下）</nobr>| [-2] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>├─ ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ □ 玩家</nobr>| [OFF] | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）,  |
|<nobr> ☑ <b>几何体碰撞器</b></nobr>| | 
|<nobr>├─ ☑ 启用</nobr>| [ON] | 
|<nobr>├─ □ 可见</nobr>| [OFF] | 
|<nobr>├─ 导出形状</nobr>|| 
|<nobr>├─ ☑ <b>头部</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.5] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>脖子</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>胸部</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├─ ☑ <b>肋骨</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>腰部</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├─ ☑ <b>腹部</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├─ ☑ <b>臀部</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>肩膀</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.4] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>上臂</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.15] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>下臂</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.44] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>手</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>臀部（髋部）</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.455] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>大腿</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.455] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>小腿</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>中间位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 中间半径</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 中间曲线</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├─ ☑ <b>脚</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>起始位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 起始半径</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 曲线</nobr>| [0.1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>结束位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ 结束半径</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ <b>缩放</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (X)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>├─ ⊖ (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr> ☑ <b>网格碰撞体</b></nobr>| | 
|<nobr>├─ ☑ 启用</nobr>| [ON] | 
|<nobr>├─ ☑ 禁用几何碰撞体</nobr>| [ON] | 
|<nobr>├─ □ 可视化</nobr>| [OFF] | 
|<nobr>├─ ⊖ 深度</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├─ ☑ (Skip Edge)</nobr>| [ON] | 
|<nobr>├─ ☑ (Skip Point)</nobr>| [ON] | 
|<nobr>└─ ☑ (Single Collision)</nobr>| [ON] | 
|<nobr> ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr>├─ ☑ 启用拖动</nobr>| [ON] | 
|<nobr>├─ ⊖ 重置比例</nobr>| [1] (1 ~ 5) | 在重置时从更大比例过渡到布料以帮助拟合。
|<nobr>├─ ☑ 模拟</nobr>| [ON] | 
|<nobr>├─ > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├─ ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├─ ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr>├─ ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>├─ □ 反向偶数子步</nobr>| [OFF] | 
|<nobr>├─ ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├─ ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）,  |
