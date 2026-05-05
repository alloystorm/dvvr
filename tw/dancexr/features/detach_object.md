---
layout: feature
title: 分離物件
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---

# 分離物件

將選定的骨骼從角色模型上分離，並套用獨立的物理模擬，讓配件或持有的物體能夠動態地掉落。

## 骨骼選擇

使用 **選擇骨骼** 來選取哪些骨骼將成為分離的物理物件。只能選取非運動學骨骼。

## 物理

**重力** 揷出現有骨骼上的重力力。**質量** 控制剛體（rigidbody）的重量——越重的物件掉得越快，推得越大力。**阻尼** 在時間的推移中增加空氣阻力，減緩移動速度。

## 碰撞體

選取碰撞形狀：*無*、*球體* 或 *膠囊體*。**碰撞體半徑** 設定球體/膠囊體的寬度。**碰撞體長度** 沿著骨骼軸延伸膠囊體。