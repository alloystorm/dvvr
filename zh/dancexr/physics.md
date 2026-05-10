---
layout: release
title: 物理系统
locale: zh-CN
toc: true
---

# 物理系统

DanceXR 为角色模型提供了特定于模型格式的物理系统，此外还有一个自定义构建的 XPBD（扩展基于位置动力学）系统，可用于模拟布料、软体和简化的刚体。

PMX 模型自带物理组件定义，开箱即用。您可以在 [PMX物理设置](features/pmx_physics) 中自定义和微调 PMX 模型的物理行为。

对于 XPS 和 FBX 模型，您需要使用提供的、针对常见用例优化的物理工具从零开始设置物理效果。请参阅下方工具列表及推荐使用场景。

默认情况下，物理系统使用基于 PhysX 的内置 Unity 物理引擎。我们也提供了一个基于 XPBD（扩展基于位置动力学）的自定义物理引擎，它为布料和头发等提供了更好的控制和稳定性。

关于术语（刚体、关节、碰撞器、弹簧力、阻尼、投影距离、投影角度），请参阅 [概念与术语表](concepts#bones-physics-and-colliders)。

---

## 物理工具

物理工具集包含了一系列工具，使您能够快速为模型设置物理效果。每个独立的工具都侧重于特定的用例，最大程度地减少您为获得良好结果需要调整的参数数量。大多数时候，您只需选择正确的骨骼即可实现所需行为。此外，还提供了预设以帮助您快速找到良好的设置，并可视化了解每个参数的效果。

- [身体碰撞器](features/body_colliders) — 沿角色身体的胶囊体碰撞器，用于确保自由移动的部件（头发、布料、裙子）能够与身体发生碰撞，而不是穿透。
- [头发物理](features/hair_physics) — 在以头部为根的骨骼树上的弹簧骨骼模拟。设置根骨骼，DanceXR 会遍历子骨骼来构建骨架。
- [裙子物理](features/skirt_physics) — 带有水平连接（网状）的链式物理，适合裙子和下摆。
- [垂坠物物理](features/dangling_physics) — 没有水平连接的链式物理，适合彩带、绳结、耳链、动物尾巴、任何悬挂物。
- [胸部物理](features/boobs_physics) — 基于关节的胸部摇晃模拟，包含反重力来补偿恒定的向下拉力。
- [软体物理](features/softbody_physics) — 通过弹簧力约束连接骨骼，以模拟腹部和大腿等身体部位的体积形变。
- [分离物体](features/detach_object) — 释放一个骨骼或物体，使其可以作为独立部件脱落。有用时，这些部件没有单独的材质供您使用透明度隐藏。
- [自动重置](features/auto_reset) — 当速度达到特定阈值时，自动重置物理组件，以防止爆炸。

演示视频：
{% include video id="-IZTzHUpROs" provider="youtube" %}

---

## 模拟系统

模拟系统是一个自定义构建的 XPBD（扩展基于位置动力学）系统，可用于模拟布料、软体和流体。

- [布料模拟](features/cloth_simulation) — 为模型添加布料。
- [网格转布料](features/mesh_to_cloth) — 将模型上的网格转换为布料模拟对象。
- 流体模拟 — 使用粒子模拟简单的流体效果，如粘度。
- [触手模拟](features/tentacles) — 通过连接节点和驱动力，模拟触手运动。

---

## 设置

您可以使用以下设置来控制物理行为。

- [系统级物理设置](features/system_physics) — 适用于 DanceXR 中所有物理模拟的全局设置，无论模型格式或骨架类型如何。
- [PMX物理设置](features/pmx_physics) — 覆盖模型文件中物理定义的 PMX 特定设置。
- 物理工具：
    - [身体碰撞器](features/body_colliders) — 身体沿线的碰撞器尺寸和位置。
    - [头发物理](features/hair_physics) — 头发物理的弹簧力、阻尼、碰撞器半径和骨骼选择。
    - [裙子物理](features/skirt_physics) — 裙子物理的弹簧力、阻尼、碰撞器半径和骨骼选择。
    - [垂坠物物理](features/dangling_physics) — 垂坠物物理的弹簧力、阻尼、碰撞器半径和骨骼选择。
    - [胸部物理](features/boobs_physics) — 胸部物理的弹簧力、阻尼、碰撞器半径、骨骼选择和反重力。
    - [软体物理](features/softbody_physics) — 软体物理的粒子大小、约束符合度和骨骼选择。
    - [分离物体](features/detach_object) — 分离物体的骨骼选择。
    - [自动重置](features/auto_reset) — 自动重置的速度阈值。
- [布料模拟设置](features/cloth_simulation) — 布料模拟的网格创建参数、模拟参数和碰撞器调整。它包括
    - Cloth Mesh 1
    - Cloth Mesh 2
    - Fluid Simulation
    - Mesh To Cloth
- [触手模拟设置](features/tentacles) — 触手模拟的节点数量、弹簧力、阻尼和碰撞器半径。
- [玩偶服设置](features/ragdoll) — 玩偶服模拟的关节限制、弹簧力、阻尼和碰撞器半径。

---

## 更多阅读

- [概念与术语表](concepts#bones-physics-and-colliders)
- [处理角色](actors)
- [骨骼结构示例](features/bones) — 骨骼选择参考骨架