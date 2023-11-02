---
layout: single
title: 眨眼、呼吸和眼神交流
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/eyecontact) | [繁中](/tw/dancexr/features/eyecontact) | [日本](/jp/dancexr/features/eyecontact) | [한국어](/kr/dancexr/features/eyecontact) | [简中](/zh/dancexr/features/eyecontact)


## 眼神交流
基本上，我们试图实现人类互动的自然眼神交流。
* 演员会在你处于他们可见范围内时看着你。
* 他们也会看着场景中的其他摄像机。
* 当场景中有多个演员时，他们也会互相看着对方。
* 观众不会看着摄像机或彼此，他们只对演员感兴趣。
* 很明显，这需要模型具有控制眼睛运动的骨骼。

{% include video id="zP966sQ6h0g" provider="youtube" %}

## 眨眼
演员会以随机的间隔眨眼。这需要控制眼睑的骨骼。

## 呼吸
与眼睛运动类似，呼吸运动是在演员被分配的任何动作之上添加的。因此，它可以在演员的任何动作或姿势下工作。

## 逼真的动作设置
上述动作的设置被分组在“逼真的动作”设置下。在那里，您可以微调每个动作的参数。

对于眼神交流，您有3个单独的滑块来影响他们选择观看目标的方式。调整权重将改变他们看待该类目标的可能性。
* 摄像机：玩家的主摄像机，或镜像和场景中的任何其他摄像机。
* 同伴：其他演员和观众
* 身体部位：演员的身体部位，这使他们可以在面部被遮挡时看着这个人。