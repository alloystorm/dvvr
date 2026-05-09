---
layout: release
title: 物理系统
locale: zh-CN
toc: true
---

# 物理系统

DanceXR 为 PMX 和 XPS 提供了模型格式特定的物理系统，此外还有一个自定义构建的 XPBD（扩展粒子系统动力学）系统，可用于模拟布料、软体和简化的刚体。

对于 PMX 模型，物理骨架定义在文件中，并通过 PMX 物理设置暴露。

对于 XPS 模型，文件中没有内置骨架，因此您需要使用 XPS 物理工具从头开始设置物理效果。

PMX 和 XPS 物理默认使用基于 PhysX 的内置 Unity 物理引擎，但也可以切换到 XPBD 后端。

使用 XPBD 系统进行的布料模拟同时适用于 PMX 和 XPS 模型，并在布料模拟设置中进行配置。

有关术语（刚体、关节、碰撞器、弹簧力、阻尼、投影距离、投影角度），请参阅 [概念与术语表](concepts#bones-physics-and-colliders)。

> 有关系统级物理对话框和每个 PMX 模型级对话框的详细参数参考，请参阅 [物理（设置参考）](features/physics)。

---

## 两种路径：PMX vs XPS

最大的决策分支是模型格式。

| | PMX | XPS |
|---|---|---|
| 是否有物理骨架？ | 是 — 内置于文件中 | 否 — 在 DanceXR 中设置 |
| 默认行为 | 开箱即用 | 未配置则无任何运动 |
| 配置位置 | [PMX物理](features/pmx_physics)（按角色设置） | [XPS物理工具](features/xps_physics)（按角色设置） |
| 常见陷阱 | 模型作者设置的关节刚度可能需要覆盖 | 您必须预先**选择骨骼**用于头发、胸部、裙子，它们才能动起来 |

两种路径共享系统级对话框（重力、模拟步数）和下面同一系列专业骨架。

---

## 系统级设置

系统级的物理设置对 DanceXR 中的所有物理模拟都具有全局适用性，无论模型格式或骨架类型如何。

---

## 骨架家族

这些是按身体部位划分的物理骨架。大多数骨架都适用于 PMX 和 XPS，但有些是 XPS 特有的，因为 PMX 模型已经为相同部位包含了自身的刚体。

### 身体形状

[身体碰撞器](features/body_colliders) — 沿角色身体的胶囊体碰撞器，用于确保自由移动的部件（头发、布料、裙子）能与身体碰撞，而不是穿透。

### 头发

[头发物理](features/hair_physics) — 在以头部为根的骨骼树上的弹簧骨骼模拟。设置根骨骼，DanceXR 会遍历子骨骼来构建骨架。

### 裙子和垂坠物

- [裙子物理](features/skirt_physics) — 带有水平连接（网格状）的链式物理，适合裙子和下摆。
- [垂坠物物理](features/dangling_physics) — 没有水平连接的链式物理，适合彩带、绳结、耳链、动物尾巴、任何悬挂物。

区别在于附近链是否水平连接。没有这些连接，裙子会塌陷；如果连接了，彩带会挂得不自然。

### 胸部

[胸部物理](features/boobs_physics) — 基于关节的胸部骨骼摇晃模拟，并包含反重力以补偿恒定的向下拉力。在 XPS 中相关，因为 PMX 模型通常在其文件中自带胸部关节。

### 布料（基于网格）

- [布料模拟](features/cloth_simulation) — 对服装网格进行的 Unity 布料风格模拟。
- [网格转布料](features/mesh_to_cloth) — 将模型上的网格转换为布料模拟对象。

这些与裙子/垂坠物链式物理不同：布料模拟的是整个网格，而不是少量控制骨骼。它更重；更适用于戏剧性、全套服装的运动。

### 软体

- [软体物理](features/softbody_physics) — 体积形变。 <!-- TODO: 确认主要用例。 -->
- [粒子动力学](features/particle_dynamics) — 基于粒子的二次运动。

### 全身

- [玩偶服](features/ragdoll) — 物理系统接管整个骨骼；角色身体变得松弛。
- [分离物体](features/detach_object) — 释放一个骨骼或物体，使其由物理系统独立驱动。
- [二次运动](features/secondary_motion) — 程序化层，在现有运动之上增加呼吸、摇摆和跟随动作。

---

## 如何选择使用

| 想实现 | 推荐使用 |
|---|---|
| 头发摆动 | [头发物理](features/hair_physics) — 设置根骨骼 |
| 裙子飘扬 | [裙子物理](features/skirt_physics) (XPS)，或 [PMX物理](features/pmx_physics) (PMX) |
| 彩带、尾巴或绳结悬挂 | [垂坠物物理](features/dangling_physics) |
| XPS 上的胸部摇晃 | [胸部物理](features/boobs_physics) — 分配骨骼 |
| 整个服装模拟布料感 | [布料模拟](features/cloth_simulation) |
| 身体部位感觉体积感 | [软体物理](features/softbody_physics) |
| 角色倒下 | [玩偶服](features/ragdoll) |
| 动态移除身体部位 | [分离物体](features/detach_object) |
| 任何运动上增加微妙的生命力 | [二次运动](features/secondary_motion) |
| 头发/布料真正与身体碰撞 | [身体碰撞器](features/body_colliders) |

---

## 常见问题

| 症状 | 可能原因 |
|---|---|
| 头发/布料穿过身体 | 未设置 [身体碰撞器](features/body_colliders)，或在 [物理设置](features/physics) 中开启了 *禁用碰撞* |
| 选择了头发但无任何运动 | 选择的骨骼可能不是根骨骼；请检查 [骨骼结构示例](features/bones) |
| 胸部不晃动 | 胸部物理开关已打开，但未分配骨骼 — 参阅 [胸部物理](features/boobs_physics) |
| 骨骼随时间漂移 | 减小 *投影距离* / *投影角度*，或在 [物理设置](features/physics) 中启用 *变化时重置* |
| 高帧率时出现抖动 | 增加 [模拟](features/simulation) 中的每秒步数 |
| 物理启用时帧率下降 | 减小每秒步数；关闭您不需要的重型骨架（布料、软体） |
| 裙子看起来像硬锥体 | 您使用的是垂坠物物理而不是裙子物理；切换 ([裙子](features/skirt_physics) 与 [垂坠物](features/dangling_physics)) |

---

## 相关页面

- [概念与术语表](concepts#bones-physics-and-colliders)
- [处理角色](actors)
- [物理（设置参考）](features/physics) — 系统级和 PMX 特定对话框参数
- [XPS物理](features/xps_physics) — XPS 骨架配置
- [骨骼结构示例](features/bones) — 骨骼选择参考骨架

<!-- TODO Phase 3: resolve duplicate pages — cloth_sim.md vs cloth_simulation.md, physics_softbody.md vs softbody_physics.md, transparency.md vs material_transparent.md. Also consider renaming features/physics.md to features/pmx_physics_settings.md to make this hub the canonical "Physics" entry. -->