---
locale: zh-rCN
layout: single
title: 软体物理
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/physics_softbody) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_softbody) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_softbody) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_softbody) | [简中](/zh/dancexr/menu/2025.4/actor/physics_softbody)

[物理](../menu#物理) > 软体物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 启用</nobr>| [ON] | 
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
|<nobr> 选择骨骼</nobr>|| 选择骨骼
|<nobr>![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>├&nbsp; <b>关节</b></nobr>|| 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
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
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![slider icon](/images/icon/ic_slider.png) 附加组</nobr>| [0] (0 ~ 7) | 
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 启用</nobr>| [OFF] | 
|<nobr>├&nbsp; 选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 沿轴锚定</nobr>| [OFF] | 
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>锚点偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;![tune icon](/images/icon/ic_tune.png) <b>粒子动力学</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>关节</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 可视化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>&nbsp;&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>风</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>碰撞与</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 头部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 身体</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) 腿</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) 脚</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp;![check_on icon](/images/icon/ic_check_on.png) 玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>![list icon](/images/icon/ic_list.png) 预设</nobr>| **默认（重置）** | 默认（重置）,  |
