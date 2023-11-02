---
layout: single
title: 眨眼、呼吸和眼神交流
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/tw/dancexr/features/eyecontact) | [繁中](/tw/tw/dancexr/features/eyecontact) | [日本語](/jp/tw/dancexr/features/eyecontact) | [한국어](/kr/tw/dancexr/features/eyecontact) | [简中](/zh/tw/dancexr/features/eyecontact)


## 眼神交流
基本上，我們試圖實現人類互動的自然眼神交流。
* 當你在演員的可見範圍內時，他們會看著你。
* 他們也會看著場景中的其他攝影機。
* 當場景中有多個演員時，他們也會互相看著對方。
* 觀眾不會看攝影機或彼此，他們只對演員感興趣。
* 顯然，這需要模型具有控制眼睛運動的骨骼。

{% include video id="zP966sQ6h0g" provider="youtube" %}

## 眨眼
演員會以隨機間隔眨眼。這需要控制眼瞼的骨骼。

## 呼吸
與眼睛運動一樣，呼吸運動是添加在演員被指定的任何運動之上的。因此，它可以在演員的任何運動或姿勢下工作。

## 逼真運動設置
上述運動的設置被分組在"逼真運動"設置下。在那裡，您可以微調每個運動的參數。

對於眼神交流，您有三個單獨的滑塊來影響他們選擇觀看目標的方式。調整權重將改變他們看待該類目標的可能性。
* 攝影機：玩家的主攝影機，或鏡子和場景中的其他攝影機。
* 同儕：其他演員和觀眾
* 身體部位：演員的身體部位，這使他們可以在臉部被遮擋時看著該人。