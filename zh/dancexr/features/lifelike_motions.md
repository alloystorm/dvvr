---
layout: release
title: 逼真的动作
locale: zh-CN
nav_links:
  - label: 简介
    url: /zh/dancexr
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
---

# 栩栩如生的动作

当没有动画播放时，添加空闲行为，使角色感觉更具生命力：呼吸、眨眼、微小动作和眼神接触。

## 眼神接触

开启后，角色会注视摄影机、其他角色或指定视角内的身体部位。**Look At Camera**、**Look At Peers** 和 **Look At Body** 设置了每种目标类型的相对优先级。**Eye Contact Head Turn** 控制注视是通过转动头部还是仅仅通过眼部实现，（人类通常转动头部约占总角度的 70%）。

**Cartoon Eyes** 降低了大型动漫眼模型的眼部旋转振幅，以防止其外翻；**Cartoon Eyes Limit** 设置了减小幅度。**Stare Mode** 会锁定最近的目标，而不是自然地转换注视方向。**Smile Mouth** 和 **Smile Eyebrow** 在进行眼神接触的同时，增加了微妙的表情变化。

## 形态变化眼部控制

这是一种替代基于骨骼的眼部旋转的方法，它使用混合形状（morphs）。开启此开关并为每个注视方向（左眼左、左眼右等）分配形态变化。**Left Right Range** 和 **Up Down Range** 设置了混合形状的激活角度。

## 呼吸

通过微妙地旋转躯干和颈部的骨骼，模拟呼吸过程中的胸腔扩张。**Breath Rate** 控制循环的速度。

## 微动

向头部和躯干添加微小的随机旋转，防止角色看起来完全僵硬。**Extent** 缩放振幅；**Cycle** 设置振荡周期。

## 眨眼

在 2–10 秒的间隔内随机眨眼。**Blink Duration** 控制每次眨眼持续的时间。