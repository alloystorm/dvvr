---
locale: zh-rCN
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[(Prop)](../menu#(Prop)) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> □ 禁用 PMX 物理</nobr>| [OFF] | 禁用 PMX 物理以使用 XPS 工具
|<nobr> ☑ 减少约束</nobr>| [ON] | 使用减少约束的实验设置以实现更平滑的模拟
|<nobr> ⚙️ <b>碰撞</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 静态包含</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 静态排除</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 动态包含</nobr>| [ON] | 
|<nobr>└─ ☑ 动态排除</nobr>| [ON] | 
|<nobr> ⚙️ <b>线运动</b></nobr>| | Settings for linear movements
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 限制</nobr>| 自动 | 自动, 有限, 锁定, 自由, 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 锁定 0 限制</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最小弹簧力</nobr>| [5] (0 ~ 15) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最大限制</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹性</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└─ ⊖ 拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ⚙️ <b>角运动</b></nobr>| | Settings for angular movements
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 限制</nobr>| 自动 | 自动, 有限, 锁定, 自由, 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 锁定 0 限制</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最小弹簧力</nobr>| [5] (0 ~ 15) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最大限制</nobr>| [90] (3 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹性</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└─ ⊖ 拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ☑ <b>线驱动</b></nobr>| | Apply linear drive
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧力</nobr>| [3] (0 ~ 5) | 
|<nobr>└─ ⊖ 阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ☑ <b>角驱动</b></nobr>| | Apply angular drive
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧力</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└─ ⊖ 阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ⚙️ <b>线动</b></nobr>| | Settings for linear motion
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 坚固度</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 主驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 第二驱动力</nobr>| [3] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 目标位置</nobr>| 零 | 零, 中心, 最小值, 最大值, 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 尽可能锁定</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 加速模式</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└─ □ (Ignore Limit)</nobr>| [OFF] | 通过忽略关节限制进一步减少约束
|<nobr> ⚙️ <b>角动</b></nobr>| | Settings for angular motion
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 坚固度</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 主驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 第二驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 目标位置</nobr>| 零 | 零, 中心, 最小值, 最大值, 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 尽可能锁定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 加速模式</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└─ □ (Ignore Limit)</nobr>| [OFF] | 通过忽略关节限制进一步减少约束
|<nobr> ⚙️ <b>选项</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最小阻力</nobr>| [0] (0 ~ 1) | 自动模式下的最小阻力值
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻力比例</nobr>| [1] (0 ~ 5) | 自动模式下应用于阻力值的比例
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 最小质量</nobr>| [0] (0 ~ 1) | 自动模式下的最小质量值
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 质量比例</nobr>| [1] (0 ~ 10) | 自动模式下应用于质量值的比例
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 投影距离</nobr>| [0.05] (0 ~ 0.1) | 当物体之间的距离超过这个值时，强制重置关节
|<nobr>└─ ⊖ 投影角度</nobr>| [5] (0 ~ 60) | 当物体之间的角度超过这个值时，强制重置关节
|<nobr> ⊖ 自动重置阈值</nobr>| [35] (0 ~ 100) | 当速度超过此值时自动重置骨骼及其子骨骼
|<nobr> ⚙️ <b>自动重置</b></nobr>| | 
|<nobr>└─ ⊖ 阈值</nobr>| [30] (0 ~ 50) | 
|<nobr> ☑ <b>身体碰撞器</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 大小</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 头部半径</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 手臂半径</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 前臂</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 胸宽</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 腰宽</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 髋宽</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 臀部半径</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>臀部位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ (Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 腹部半径</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 腹部位置</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 腿部半径</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 大腿前/后</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 大腿起始位置</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 手</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (amy), (misaki),  |
|<nobr> ☑ <b>胸部物理</b><sup>[PRO]</sup></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧力</nobr>| [1.5] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0.1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 反重力</nobr>| [10] (0 ~ 45) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>旋转限制</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 上限</nobr>| [100] (0 ~ 120) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 下限</nobr>| [15] (0 ~ 45) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 左右限制</nobr>| [15] (0 ~ 45) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧力</nobr>| [1.25] (0 ~ 10) | 超出限制时的弹簧力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 弹跳</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>锚点</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>中心</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 与手臂碰撞</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.65] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体曲线</nobr>| [2] (-2 ~ 2) | 与布料模拟兼容。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用乳头</nobr>| [ON] | 与布料模拟兼容。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>乳头位置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ (Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 乳头大小</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>(Softbody)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> <b>关节</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 身体</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 腿</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用拖动</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模拟</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶数子步</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_line_t.png"/> □ 仅限软体</nobr>| [OFF] | 禁用物理连接，只使用软体粒子。
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr> ☑ <b>裙子物理</b><sup>[PRO]</sup></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 使用粒子动态</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用拖动</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模拟</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶数子步</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>主组</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 附加组</nobr>| [0] (0 ~ 7) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 2)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 3)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 4)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 5)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 6)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 7)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> □ <b>(Group 8)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 启用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>物理属性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>父子关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>横向关节</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 锁定 Y</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ □ 锁定 Z</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞体</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> > 碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ☑ 使用主组设置</nobr>| [ON] | 
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr> ☑ <b>头发物理</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 选择骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用拖动</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模拟</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶数子步</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧</nobr>| [1.25] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0.25] (0 ~ 1) | 每个层级减少刚度
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转限制</nobr>| [5] (0 ~ 180) | 限制扭转旋转
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 限制力</nobr>| [3] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.005] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.9] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (momiji bob), (Preset 1),  |
|<nobr> ☑ <b>悬挂物理</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 选择骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ <b>粒子动力学</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> □ 可视化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 惯性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>风</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ⊖ 湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ⚙️ <b>碰撞与</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 头部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 身体</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 胸部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 臀部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 腿</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 脚</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/>└─ ☑ 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/>└─ ⚙️ <b>模拟设置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 启用拖动</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ☑ 模拟</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> > 模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 子步</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 迭代</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> □ 反向偶数子步</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> ⊖ 表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_space.png"/>└─ □ 两步求解</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 弹簧</nobr>| [0.5] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 减少比例</nobr>| [0.25] (0 ~ 1) | 每个层级减少刚度
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 扭转限制</nobr>| [5] (0 ~ 180) | 限制扭转旋转
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 限制力</nobr>| [3] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 拖拽</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体长度</nobr>| [0.9] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
|<nobr> ☑ <b>分离对象</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 启用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 选择骨骼</nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/> ☑ 重力</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 质量</nobr>| [0.1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 阻尼</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/>☑ 碰撞体</nobr>| 球体 | 无, 球体, 胶囊, 
|<nobr><img src="/images/icon/ic_line_t.png"/> ⊖ 碰撞体半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└─ ⊖ 碰撞体长度</nobr>| [0.3] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 预设</nobr>| **默认（重置）** | 默认（重置）,  |
