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
|<nobr>禁用 PMX 物理</nobr>| [OFF] | 禁用 PMX 物理以使用 XPS 工具
|<nobr>减少约束</nobr>| [ON] | 使用减少约束的实验设置以实现更平滑的模拟
|<nobr>**碰撞**</nobr>| | 
|<nobr>├&nbsp;静态包含</nobr>| [ON] | 
|<nobr>├&nbsp;静态排除</nobr>| [ON] | 
|<nobr>├&nbsp;动态包含</nobr>| [ON] | 
|<nobr>└&nbsp;动态排除</nobr>| [ON] | 
|<nobr>**线运动**</nobr>| | Settings for linear movements
|<nobr>├&nbsp;限制</nobr>| 自动 | 自动, 有限, 锁定, 自由, 
|<nobr>├&nbsp;锁定 0 限制</nobr>| [ON] | 
|<nobr>├&nbsp;最小弹簧力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;最大限制</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp;弹性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**角运动**</nobr>| | Settings for angular movements
|<nobr>├&nbsp;限制</nobr>| 自动 | 自动, 有限, 锁定, 自由, 
|<nobr>├&nbsp;锁定 0 限制</nobr>| [ON] | 
|<nobr>├&nbsp;最小弹簧力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;最大限制</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp;弹性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>**线驱动**</nobr>| | Apply linear drive
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;弹簧力</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp;阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**角驱动**</nobr>| | Apply angular drive
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;弹簧力</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp;阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>**线动**</nobr>| | Settings for linear motion
|<nobr>├&nbsp;坚固度</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;主驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;第二驱动力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;目标位置</nobr>| 零 | 零, 中心, 最小值, 最大值, 
|<nobr>├&nbsp;尽可能锁定</nobr>| [ON] | 
|<nobr>├&nbsp;加速模式</nobr>| [ON] | 
|<nobr>├&nbsp;阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | 通过忽略关节限制进一步减少约束
|<nobr>**角动**</nobr>| | Settings for angular motion
|<nobr>├&nbsp;坚固度</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;主驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;第二驱动力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;目标位置</nobr>| 零 | 零, 中心, 最小值, 最大值, 
|<nobr>├&nbsp;尽可能锁定</nobr>| [OFF] | 
|<nobr>├&nbsp;加速模式</nobr>| [ON] | 
|<nobr>├&nbsp;阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;拖拽</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | 通过忽略关节限制进一步减少约束
|<nobr>**选项**</nobr>| | 
|<nobr>├&nbsp;最小阻力</nobr>| [0] (0 ~ 1) | 自动模式下的最小阻力值
|<nobr>├&nbsp;阻力比例</nobr>| [1] (0 ~ 5) | 自动模式下应用于阻力值的比例
|<nobr>├&nbsp;最小质量</nobr>| [0] (0 ~ 1) | 自动模式下的最小质量值
|<nobr>├&nbsp;质量比例</nobr>| [1] (0 ~ 10) | 自动模式下应用于质量值的比例
|<nobr>├&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;投影距离</nobr>| [0.05] (0 ~ 0.1) | 当物体之间的距离超过这个值时，强制重置关节
|<nobr>└&nbsp;投影角度</nobr>| [5] (0 ~ 60) | 当物体之间的角度超过这个值时，强制重置关节
|<nobr>自动重置阈值</nobr>| [35] (0 ~ 100) | 当速度超过此值时自动重置骨骼及其子骨骼
|<nobr>**自动重置**</nobr>| | 
|<nobr>└&nbsp;阈值</nobr>| [30] (0 ~ 50) | 
|<nobr>**身体碰撞器**</nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;大小</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;头部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;手臂半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;前臂</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;胸宽</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;腰宽</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;髋宽</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;臀部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;臀部位置</nobr>|| 
|<nobr>├&nbsp;(X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;腹部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;腹部位置</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;腿部半径</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;大腿前/后</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;大腿起始位置</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;手</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (amy), (misaki),  |
|<nobr>**胸部物理**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;选择骨骼</nobr>|| 
|<nobr>├&nbsp;弹簧力</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp;阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;拖拽</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;反重力</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp;**旋转限制**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;上限</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp;下限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;左右限制</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;弹簧力</nobr>| [1.25] (0 ~ 10) | 超出限制时的弹簧力
|<nobr>│&nbsp;├&nbsp;阻尼</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;接触距离</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;弹跳</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;**锚点**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**中心**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;**碰撞**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;与手臂碰撞</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;碰撞体曲线</nobr>| [2] (-2 ~ 2) | 与布料模拟兼容。
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;启用乳头</nobr>| [ON] | 与布料模拟兼容。
|<nobr>│&nbsp;├&nbsp;**乳头位置**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;乳头大小</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;**(Softbody)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;关节</nobr>|| 
|<nobr>│&nbsp;├&nbsp;深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;包含中心</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;体积约束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;内部约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;表面约束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;旋转约束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;边缘锁定</nobr>| [0.85] (0.5 ~ 1) | 锁定边缘上的粒子。
|<nobr>│&nbsp;├&nbsp;中心锁定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;身体</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;腿</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**模拟设置**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>│&nbsp;│&nbsp;├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;模拟</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;两步求解</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;预设</nobr>| **胸部** | 胸部, 臀部, 腿, (tina), (预设1), (预设2),  |
|<nobr>├&nbsp;仅限软体</nobr>| [OFF] | 禁用物理连接，只使用软体粒子。
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr>**裙子物理**<sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;使用粒子动态</nobr>| [ON] | 
|<nobr>├&nbsp;**模拟设置**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>│&nbsp;├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;模拟</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp;两步求解</nobr>| [OFF] | 
|<nobr>├&nbsp;主组</nobr>|| 
|<nobr>├&nbsp;选择骨骼</nobr>|| 
|<nobr>├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>├&nbsp;附加组</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp;**(Group 2)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 3)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 4)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 5)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 6)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 7)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>├&nbsp;**(Group 8)**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;选择骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp;排序</nobr>| **最短路径** | 最短路径, 圆形, 线性, 不排序, <br/>设置横向连接时使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp;闭合循环</nobr>| [ON] | 每个层级的闭合循环骨骼
|<nobr>│&nbsp;├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>│&nbsp;├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向柔顺性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;横向锚点</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;**物理属性**</nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;拖拽</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;水平重叠</nobr>| [-0.2] (-1 ~ 1) | 碰撞体的水平重叠
|<nobr>│&nbsp;│&nbsp;├&nbsp;质量分布</nobr>| [0] (-1 ~ 1) | 在每个级别减少质量
|<nobr>│&nbsp;│&nbsp;├&nbsp;摩擦力</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;求解器迭代</nobr>| [20] (1 ~ 150) | 解决碰撞时的迭代次数
|<nobr>│&nbsp;│&nbsp;└&nbsp;质心</nobr>| 零 | 自动, 零, <br/>将质心设置为零或根据每个碰撞体的位置和大小自动设置
|<nobr>│&nbsp;├&nbsp;**父子关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;摆动驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;扭转驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>│&nbsp;├&nbsp;**横向关节**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;线驱动</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;角驱动</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;驱动阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;减幅率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;锁定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;锁定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;**碰撞体**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体类型</nobr>| **箱子** | 箱子, 胶囊, 球体,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;碰撞体长度</nobr>| [0.8] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 减少第一级骨骼的碰撞体长度，以避免与身体碰撞体的干扰。
|<nobr>│&nbsp;└&nbsp;使用主组设置</nobr>| [ON] | 
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr>**头发物理**</nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;**模拟设置**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;模拟</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;两步求解</nobr>| [OFF] | 
|<nobr>├&nbsp;弹簧</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp;阻尼</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;减少比例</nobr>| [0.25] (0 ~ 1) | 每个层级减少刚度
|<nobr>├&nbsp;扭转限制</nobr>| [5] (0 ~ 180) | 限制扭转旋转
|<nobr>├&nbsp;限制力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;质量</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;拖拽</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;碰撞体半径</nobr>| [0.005] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
|<nobr>├&nbsp;碰撞体长度</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (momiji bob), (Preset 1),  |
|<nobr>**悬挂物理**</nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;选择骨骼</nobr>|| 选择骨骼
|<nobr>├&nbsp;跳过前 X 个骨骼</nobr>| [0] (0 ~ 5) | 前 X 个层级不创建物理连接
|<nobr>├&nbsp;**粒子动力学**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;启用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;摆动柔顺性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;扭转柔顺性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;粒子锚点</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;减少比例</nobr>| [0] (0 ~ 1) | 在每个层级上减少质量
|<nobr>│&nbsp;├&nbsp;可视化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;惯性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;软化</nobr>| [0] (0 ~ 1) | 软化粒子约束。
|<nobr>│&nbsp;├&nbsp;粒子半径</nobr>| [5] (1 ~ 20) | 粒子大小（以毫米为单位）
|<nobr>│&nbsp;├&nbsp;重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;摩擦力</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;拖拽（空气）</nobr>| [0] (0 ~ 2) | 空气阻力
|<nobr>│&nbsp;├&nbsp;拖拽（水下）</nobr>| [1] (0 ~ 2) | 水下阻力
|<nobr>│&nbsp;├&nbsp;浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;**风**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;风的影响</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;湍流强度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;湍流时间比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;**碰撞与**</nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;头部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;身体</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;腿</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;脚</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;玩家</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;**模拟设置**</nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;使用全局</nobr>| [ON] | 在 Pro / 布料模拟下找到全局设置
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;启用拖动</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;模拟</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;模拟每秒帧数</nobr>| **动态** | 动态, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;时间比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;子步</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;迭代</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;反向偶数子步</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;备用组大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;表格大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;两步求解</nobr>| [OFF] | 
|<nobr>├&nbsp;弹簧</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp;阻尼</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;减少比例</nobr>| [0.25] (0 ~ 1) | 每个层级减少刚度
|<nobr>├&nbsp;扭转限制</nobr>| [5] (0 ~ 180) | 限制扭转旋转
|<nobr>├&nbsp;限制力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;质量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp;拖拽</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;碰撞体半径</nobr>| [0.01] (0 ~ 0.05) | 解决碰撞时使用的粒子大小
|<nobr>├&nbsp;碰撞体长度</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;锚点位置</nobr>| [0] (0 ~ 1) | 创建关节时选择锚点位置。0 = 锚点位于父骨骼，1 = 锚点位于子骨骼
|<nobr>└&nbsp;预设</nobr>| **默认（重置）** | 默认（重置）, (Preset 1), (Preset 2),  |
|<nobr>**分离对象**</nobr>| | 
|<nobr>├&nbsp;启用</nobr>| [ON] | 
|<nobr>├&nbsp;选择骨骼</nobr>|| 
|<nobr>├&nbsp;重力</nobr>| [ON] | 
|<nobr>├&nbsp;质量</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;阻尼</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;碰撞体</nobr>| 球体 | 无, 球体, 胶囊, 
|<nobr>├&nbsp;碰撞体半径</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp;碰撞体长度</nobr>| [0.3] (0 ~ 2) | 
|<nobr>预设</nobr>| **默认（重置）** | 默认（重置）,  |
