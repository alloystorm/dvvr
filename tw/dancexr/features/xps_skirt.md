---
locale: zh-TW
layout: single
title: 裙子物理
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/xps_skirt) | [繁中](/tw/dancexr/features/xps_skirt) | [日本語](/jp/dancexr/features/xps_skirt) | [한국어](/kr/dancexr/features/xps_skirt) | [简中](/zh/dancexr/features/xps_skirt)

## 裙子物理

裙子物理創建了一個相互連接的骨骼網格，用於模擬布料物理效果。

## 設置

* 選擇骨骼：選擇與裙子相關的骨骼。
* 排序：選擇確定裙子骨骼順序的排序方法。這很重要，因為骨骼需要按照正確的順序連接，以使物理效果正常工作。
* 閉合環：如果裙子是一個閉合環，啟用此選項將最後一個骨骼連接到第一個骨骼。對於有多個部分的裙子，禁用此選項，並在下面的其他部分選項中使用。
* 可視化：可視化創建的骨骼連接。
* 跳過前 X 個骨骼：這允許您在創建骨骼連接時跳過前 x 個骨骼。當有太多骨骼需要單獨選擇時，這很有用。
* 物理屬性：骨骼連接的質量、阻力、碰撞器半徑、摩擦力、重心和求解器迭代次數。
* 父級骨骼：調整父子骨骼的連接配置。
* 骨骼間：調整骨骼之間的連接配置。
* 錨點位置：調整骨骼連接的錨點位置。
* 應用於其他組：將相同設置應用於其他骨骼組。
* 其他組：設置您需要的其他組數量。
* 組 N：如果裙子有多個部分，您可以使用此功能為其他部分創建骨骼連接。對於每個組，您可以選擇不同的骨骼集。