---
locale: zh-CN
layout: single
title: 软体物理
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/xps_softbody) | [繁中](/tw/dancexr/features/xps_softbody) | [日本語](/jp/dancexr/features/xps_softbody) | [한국어](/kr/dancexr/features/xps_softbody) | [简中](/zh/dancexr/features/xps_softbody)

## 软体物理

软体物理通过在一组骨骼之间创建相互连接的关节网状结构来模拟软体物理。与从根部到尖端有明确层级的裙摆物理不同，这更像是所有骨骼之间的平坦关系。

这对于臀部和大腿物理效果最佳。

[胸部物理](xps_boobs.md)中的软体模式使用相同的机制。

## 设置

* 选择骨骼：选择与软体物理相关的骨骼。
* 物理属性：质量、阻力、碰撞体半径、摩擦力、质心和关节的求解器迭代次数。
* 父关节：调整父子关节的配置。
* 关节间：调整骨骼之间关节的配置。
* 可视化：可视化创建的关节。
* 应用到其他组：对其他骨骼组使用相同的设置。
* 额外组：设置所需的额外组的数量。
* 组 N：配置额外组。
* 悬挂设置（v2025.11）：允许软体物理使用悬挂设置以获得更好的控制。