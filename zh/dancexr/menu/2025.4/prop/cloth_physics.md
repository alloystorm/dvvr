---
locale: zh-rCN
layout: single
title: 悬挂物理
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > 悬挂物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ☑ 启用</nobr>| [ON] | 
|<nobr> 选择骨骼</nobr>|| 选择骨骼
|<nobr> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr> ☑ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr>└─ ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用拖动</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模拟</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶数子步</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_space.png"/>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr> ⊖ 弹簧</nobr>| [0.5] (0 ~ 5) | 
|<nobr> ⊖ 阻尼</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr> ⊖ 减少比例</nobr>| [0.25] (0 ~ 1) | 每个层级减少刚度
|<nobr> ⊖ 扭转限制</nobr>| [5] (0 ~ 180) | 限制扭转旋转
|<nobr> ⊖ 限制力</nobr>| [3] (0 ~ 8) | 
|<nobr> ⊖ 质量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr> ⊖ 拖拽</nobr>| [1] (0 ~ 10) | 
|<nobr> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
|<nobr> ⊖ 碰撞体长度</nobr>| [0.9] (0 ~ 1) | 
|<nobr> ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
