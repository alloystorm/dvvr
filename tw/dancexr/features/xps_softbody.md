---
locale: zh-TW
layout: single
title: 柔體物理學
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/xps_softbody) | [繁中](/tw/dancexr/features/xps_softbody) | [日本語](/jp/dancexr/features/xps_softbody) | [한국어](/kr/dancexr/features/xps_softbody) | [简中](/zh/dancexr/features/xps_softbody)

## 軟體物理

軟體物理透過在一組骨骼之間創建互相連接的網格來模擬軟體物理。與裙擺物理不同，後者有明確的從根部到尖端的層級關係，這種方式更像是所有骨骼之間的平面關係。

這種方式對於臀部和大腿物理效果最為理想。

[胸部物理](xps_boobs.md)中的軟體模式使用了相同的機制。

## 設定

* 選擇骨骼：選擇與軟體物理相關的骨骼。
* 物理屬性：質量、阻力、碰撞器半徑、摩擦、質心及關節的求解器迭代次數。
* 父關節：調整父子關節的配置。
* 關節間：調整骨骼之間關節的配置。
* 視覺化：視覺化創建的關節。
* 應用於其他組：對其他骨骼組使用相同的設定。
* 額外組：設置所需的額外組數量。
* 組 N：配置額外組。
* 懸掛設置 (v2025.11)：允許軟體物理使用懸掛設置以更好地控制。