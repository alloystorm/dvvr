---
locale: zh-rCN
layout: single
title: 裙子物理
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/physics_skirt) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_skirt) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_skirt) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_skirt) | [简中](/zh/dancexr/menu/2025.4/actor/physics_skirt)

[物理](../menu#物理) > 裙子物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 启用</nobr>| [ON] | 
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 使用粒子动态</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>模拟设置</b></nobr>| | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 启用拖动</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 模拟</nobr>| [ON] | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 子步</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 反向偶数子步</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 两步求解</nobr>| [OFF] | 
|<nobr> <b>主组</b></nobr>|| 
|<nobr> 选择骨骼</nobr>|| 
|<nobr>![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>![slider icon](/images/icon/ic_slider.png) 附加组</nobr>| [0] (0 ~ 7) | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>父子关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>横向关节</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;![check_off icon](/images/icon/ic_check_off.png) 锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞体</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;![chevron icon](/images/icon/ic_chevron.png) 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>![list icon](/images/icon/ic_list.png) 预设</nobr>| **默认（重置）** | 默认（重置）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
