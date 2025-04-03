---
locale: zh-rCN
layout: single
title: 物理
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/actor/model_physics) | [繁中](/tw/dancexr/menu/2025.4/actor/model_physics) | [日本語](/jp/dancexr/menu/2025.4/actor/model_physics) | [한국어](/kr/dancexr/menu/2025.4/actor/model_physics) | [简中](/zh/dancexr/menu/2025.4/actor/model_physics)

[演员](../menu#演员) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
| 禁用 PMX 物理 | OFF | 禁用 PMX 物理以使用 XPS 工具
| 减少约束 | ON | 使用减少约束的实验设置以实现更平滑的模拟
| **碰撞** | | 
| ├&nbsp;静态包含 | ON | 
| ├&nbsp;静态排除 | ON | 
| ├&nbsp;动态包含 | ON | 
| └&nbsp;动态排除 | ON | 
| **线运动** | | Settings for linear movements
| ├&nbsp;限制 | 自动 | 自动, 有限, 锁定, 自由, 
| ├&nbsp;锁定 0 限制 | ON | 
| ├&nbsp;最小弹簧力 | [5] (0 ~ 15) | 
| ├&nbsp;最大限制 | [0.05] (0.05 ~ 0.1) | 
| ├&nbsp;弹性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接触距离 | [0.5] (0 ~ 1) | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| └&nbsp;拖拽 | [0.15] (0 ~ 1) | 
| **角运动** | | Settings for angular movements
| ├&nbsp;限制 | 自动 | 自动, 有限, 锁定, 自由, 
| ├&nbsp;锁定 0 限制 | ON | 
| ├&nbsp;最小弹簧力 | [5] (0 ~ 15) | 
| ├&nbsp;最大限制 | [90] (3 ~ 90) | 
| ├&nbsp;弹性 | [0.5] (0 ~ 1) | 
| ├&nbsp;接触距离 | [0.5] (0 ~ 1) | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| └&nbsp;拖拽 | [0.15] (0 ~ 1) | 
| **线驱动** | | Apply linear drive
| ├&nbsp;启用 | ON | 
| ├&nbsp;弹簧力 | [3] (0 ~ 5) | 
| └&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| **角驱动** | | Apply angular drive
| ├&nbsp;启用 | ON | 
| ├&nbsp;弹簧力 | [0.1] (0 ~ 5) | 
| └&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| **线动** | | Settings for linear motion
| ├&nbsp;坚固度 | [0] (-1 ~ 1) | 
| ├&nbsp;主驱动力 | [5] (0 ~ 8) | 
| ├&nbsp;第二驱动力 | [3] (0 ~ 8) | 
| ├&nbsp;目标位置 | 零 | 零, 中心, 最小值, 最大值, 
| ├&nbsp;尽可能锁定 | ON | 
| ├&nbsp;加速模式 | ON | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| ├&nbsp;拖拽 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 通过忽略关节限制进一步减少约束
| **角动** | | Settings for angular motion
| ├&nbsp;坚固度 | [0] (-1 ~ 1) | 
| ├&nbsp;主驱动力 | [5] (0 ~ 8) | 
| ├&nbsp;第二驱动力 | [5] (0 ~ 8) | 
| ├&nbsp;目标位置 | 零 | 零, 中心, 最小值, 最大值, 
| ├&nbsp;尽可能锁定 | OFF | 
| ├&nbsp;加速模式 | ON | 
| ├&nbsp;阻尼 | [0.05] (0 ~ 1) | 
| ├&nbsp;拖拽 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 通过忽略关节限制进一步减少约束
| **选项** | | 
| ├&nbsp;最小阻力 | [0] (0 ~ 1) | 自动模式下的最小阻力值
| ├&nbsp;阻力比例 | [1] (0 ~ 5) | 自动模式下应用于阻力值的比例
| ├&nbsp;最小质量 | [0] (0 ~ 1) | 自动模式下的最小质量值
| ├&nbsp;质量比例 | [1] (0 ~ 10) | 自动模式下应用于质量值的比例
| ├&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| ├&nbsp;投影距离 | [0.05] (0 ~ 0.1) | 当物体之间的距离超过这个值时，强制重置关节
| └&nbsp;投影角度 | [5] (0 ~ 60) | 当物体之间的角度超过这个值时，强制重置关节
| 自动重置阈值 | [35] (0 ~ 100) | 当速度超过此值时自动重置骨骼及其子骨骼
| **自动重置** | | 
| └&nbsp;阈值 | [30] (0 ~ 50) | 
| **身体碰撞器** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;大小 | [0.5] (0 ~ 1) | 
| ├&nbsp;头部半径 | [1] (0 ~ 2) | 
| ├&nbsp;手臂半径 | [1] (0 ~ 2) | 
| ├&nbsp;前臂 | [1] (0 ~ 2) | 
| ├&nbsp;胸宽 | [1] (0 ~ 2) | 
| ├&nbsp;腰宽 | [0.5] (0 ~ 1) | 
| ├&nbsp;髋宽 | [0] (-1 ~ 1) | 
| ├&nbsp;臀部半径 | [1] (0 ~ 2) | 
| ├&nbsp;臀部位置 || 
| ├&nbsp;(X) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Y) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Z) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;腹部半径 | [1] (0 ~ 2) | 
| ├&nbsp;腹部位置 | [0] (-1 ~ 1) | 
| ├&nbsp;腿部半径 | [1] (0 ~ 2) | 
| ├&nbsp;大腿前/后 | [0] (-1 ~ 1) | 
| ├&nbsp;大腿起始位置 | [0] (0 ~ 1) | 
| ├&nbsp;手 | [0] (0 ~ 1) | 
| ├&nbsp;可视化 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (amy), (misaki),  |
| **胸部物理**<sup>[PRO]</sup> | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;选择骨骼 || 
| ├&nbsp;弹簧力 | [1.5] (0 ~ 5) | 
| ├&nbsp;阻尼 | [0.1] (0 ~ 1) | 
| ├&nbsp;质量 | [0.1] (0 ~ 1) | 
| ├&nbsp;拖拽 | [0.1] (0 ~ 10) | 
| ├&nbsp;反重力 | [10] (0 ~ 45) | 
| ├&nbsp;**旋转限制** | | 
| │&nbsp;├&nbsp;上限 | [100] (0 ~ 120) | 
| │&nbsp;├&nbsp;下限 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;左右限制 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;弹簧力 | [1.25] (0 ~ 10) | 超出限制时的弹簧力
| │&nbsp;├&nbsp;阻尼 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;接触距离 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;弹跳 | [0.2] (0 ~ 1) | 
| ├&nbsp;**锚点** | | 
| │&nbsp;├&nbsp;(X) | [-0.03] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [0.03] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.08] (-0.2 ~ 0.2) | 
| ├&nbsp;**中心** | | 
| │&nbsp;├&nbsp;(X) | [0.02] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [-0.05] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.025] (-0.2 ~ 0.2) | 
| ├&nbsp;**碰撞** | | 
| │&nbsp;├&nbsp;与手臂碰撞 | OFF | 
| │&nbsp;├&nbsp;碰撞体半径 | [0.07] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;碰撞体长度 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;碰撞体曲线 | [2] (-2 ~ 2) | 与布料模拟兼容。
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;启用乳头 | ON | 与布料模拟兼容。
| │&nbsp;├&nbsp;**乳头位置** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [-0.18] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.09] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0.2] (0 ~ 1) | 
| │&nbsp;└&nbsp;乳头大小 | [0.1] (0 ~ 1) | 
| ├&nbsp;**(Softbody)** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;关节 || 
| │&nbsp;├&nbsp;深度 | [0.4] (0 ~ 1) | 
| │&nbsp;├&nbsp;包含中心 | ON | 
| │&nbsp;├&nbsp;体积约束 | [0.85] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;内部约束 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;表面约束 | [0.75] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;旋转约束 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;边缘锁定 | [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
| │&nbsp;├&nbsp;中心锁定 | [1] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;阻尼 | [15] (0 ~ 40) | 
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;├&nbsp;风的影响 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;├&nbsp;身体 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;胸部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;臀部 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;├&nbsp;腿 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**模拟设置** | | 
| │&nbsp;│&nbsp;├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| │&nbsp;│&nbsp;├&nbsp;启用拖动 | ON | 
| │&nbsp;│&nbsp;├&nbsp;模拟 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;│&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;│&nbsp;├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;子步 | [4] (1 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;迭代 | [1] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;反向偶数子步 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;表格大小 | [6] (1 ~ 20) | 
| │&nbsp;│&nbsp;└&nbsp;两步求解 | OFF | 
| │&nbsp;└&nbsp;(Presets: Boobs) || 
| │&nbsp;&nbsp;&nbsp;预设 | **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
| ├&nbsp;仅限软体 | OFF | 禁用物理连接，只使用软体粒子。
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| **裙子物理**<sup>[PRO]</sup> | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;使用粒子动态 | ON | 
| ├&nbsp;**模拟设置** | | 
| │&nbsp;├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| │&nbsp;├&nbsp;启用拖动 | ON | 
| │&nbsp;├&nbsp;模拟 | ON | 
| │&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;├&nbsp;子步 | [4] (1 ~ 20) | 
| │&nbsp;├&nbsp;迭代 | [1] (0 ~ 10) | 
| │&nbsp;├&nbsp;反向偶数子步 | OFF | 
| │&nbsp;├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| │&nbsp;├&nbsp;表格大小 | [6] (1 ~ 20) | 
| │&nbsp;└&nbsp;两步求解 | OFF | 
| ├&nbsp;主组 || 
| ├&nbsp;选择骨骼 || 
| ├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| ├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| ├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| ├&nbsp;**粒子动力学** | | 
| │&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
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
| │&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| ├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| ├&nbsp;**父子关节** | | 
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| ├&nbsp;**横向关节** | | 
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;└&nbsp;锁定 Z | OFF | 
| ├&nbsp;**碰撞体** | | 
| │&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| ├&nbsp;附加组 | [0] (0 ~ 7) | 
| ├&nbsp;**(Group 2)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 3)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 4)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 5)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 6)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 7)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| ├&nbsp;**(Group 8)** | | 
| │&nbsp;├&nbsp;启用 | OFF | 
| │&nbsp;├&nbsp;选择骨骼 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 设置横向连接时使用的排序方法。
| │&nbsp;│&nbsp;排序 | **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
| │&nbsp;├&nbsp;闭合循环 | ON | 每个层级的闭合循环骨骼
| │&nbsp;├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| │&nbsp;├&nbsp;**粒子动力学** | | 
| │&nbsp;│&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;│&nbsp;├&nbsp;横向柔顺性 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;横向锚点 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;│&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
| │&nbsp;│&nbsp;├&nbsp;重力 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;地面摩擦 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽（空气） | [0] (0 ~ 2) | 空气阻力
| │&nbsp;│&nbsp;├&nbsp;拖拽（水下） | [1] (0 ~ 2) | 水下阻力
| │&nbsp;│&nbsp;├&nbsp;浮力 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**风** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**碰撞与** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家 | ON | 
| │&nbsp;├&nbsp;**物理属性** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;质量 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;拖拽 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;水平重叠 | [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
| │&nbsp;│&nbsp;├&nbsp;质量分布 | [0] (-1 ~ 1) | 在每个级别减少质量
| │&nbsp;│&nbsp;├&nbsp;摩擦力 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;求解器迭代 | [20] (1 ~ 150) | 解决碰撞时的迭代次数
| │&nbsp;│&nbsp;└&nbsp;质心 | 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
| │&nbsp;├&nbsp;**父子关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;摆动驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;扭转驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| │&nbsp;├&nbsp;**横向关节** | | 
| │&nbsp;│&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;线驱动 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;角驱动 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;驱动阻尼 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;减幅率 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;锁定 Y | OFF | 
| │&nbsp;│&nbsp;└&nbsp;锁定 Z | OFF | 
| │&nbsp;├&nbsp;**碰撞体** | | 
| │&nbsp;│&nbsp;├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;碰撞体类型 | **箱子** | 箱子, 胶囊, 球体,  |
| │&nbsp;│&nbsp;├&nbsp;碰撞体长度 | [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
| │&nbsp;└&nbsp;使用主组设置 | ON | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| **头发物理** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;选择骨骼 || 选择骨骼
| ├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| ├&nbsp;**粒子动力学** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
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
| │&nbsp;└&nbsp;**模拟设置** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| │&nbsp;&nbsp;&nbsp;├&nbsp;启用拖动 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;模拟 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;子步 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;迭代 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;反向偶数子步 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;表格大小 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;两步求解 | OFF | 
| ├&nbsp;弹簧 | [1.25] (0 ~ 5) | 
| ├&nbsp;阻尼 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;减少比例 | [0.25] (0 ~ 1) | 每个层级减少刚度
| ├&nbsp;扭转限制 | [5] (0 ~ 180) | 限制扭转旋转
| ├&nbsp;限制力 | [3] (0 ~ 8) | 
| ├&nbsp;质量 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;拖拽 | [1] (0 ~ 10) | 
| ├&nbsp;碰撞体半径 | [0.005] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
| ├&nbsp;碰撞体长度 | [0.9] (0 ~ 1) | 
| ├&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (momiji bob), (Preset 1),  |
| **悬挂物理** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;选择骨骼 || 选择骨骼
| ├&nbsp;跳过前 X 个骨骼 | [0] (0 ~ 5) | 前 X 个层级不创建物理连接
| ├&nbsp;**粒子动力学** | | 
| │&nbsp;├&nbsp;启用 | ON | 
| │&nbsp;├&nbsp;摆动柔顺性 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;扭转柔顺性 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;粒子锚点 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;减少比例 | [0] (0 ~ 1) | 在每个层级上减少质量
| │&nbsp;├&nbsp;可视化 | OFF | 
| │&nbsp;├&nbsp;最大角速度 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;惯性 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;软化 | [0] (0 ~ 1) | 软化粒子约束。
| │&nbsp;├&nbsp;粒子半径 | [5] (1 ~ 20) | 粒子大小（以毫米为单位）
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
| │&nbsp;└&nbsp;**模拟设置** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;使用全局 | ON | 在 Pro / 布料模拟下找到全局设置
| │&nbsp;&nbsp;&nbsp;├&nbsp;启用拖动 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;模拟 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;模拟每秒帧数 | **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;时间比例 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;子步 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;迭代 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;反向偶数子步 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;备用组大小 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;表格大小 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;两步求解 | OFF | 
| ├&nbsp;弹簧 | [0.5] (0 ~ 5) | 
| ├&nbsp;阻尼 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;减少比例 | [0.25] (0 ~ 1) | 每个层级减少刚度
| ├&nbsp;扭转限制 | [5] (0 ~ 180) | 限制扭转旋转
| ├&nbsp;限制力 | [3] (0 ~ 8) | 
| ├&nbsp;质量 | [0.05] (0 ~ 0.1) | 
| ├&nbsp;拖拽 | [1] (0 ~ 10) | 
| ├&nbsp;碰撞体半径 | [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
| ├&nbsp;碰撞体长度 | [0.9] (0 ~ 1) | 
| ├&nbsp;锚点位置 | [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;预设 | **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
| **分离对象** | | 
| ├&nbsp;启用 | ON | 
| ├&nbsp;选择骨骼 || 
| ├&nbsp;重力 | ON | 
| ├&nbsp;质量 | [0.1] (0 ~ 10) | 
| ├&nbsp;阻尼 | [0] (0 ~ 1) | 
| ├&nbsp;碰撞体 | 球体 | 无, 球体, 胶囊, 
| ├&nbsp;碰撞体半径 | [0.1] (0 ~ 1) | 
| └&nbsp;碰撞体长度 | [0.3] (0 ~ 2) | 
| (Presets: Default (Reset)) || 
| 预设 | **默认（重置）** | 默认（重置）,  |
