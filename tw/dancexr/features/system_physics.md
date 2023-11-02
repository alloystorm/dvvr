---
layout: single
title: 系統物理學
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/system_physics) | [繁中](/tw/dancexr/features/system_physics) | [日本](/jp/dancexr/features/system_physics) | [한국어](/kr/dancexr/features/system_physics) | [简中](/zh/dancexr/features/system_physics)


## 系統物理學設定
您可以在「設定」->「選項」->「物理學」中找到系統物理學設定。

![系統物理學](/images/system-physics.png)

啟用
: 開啟或關閉物理模擬

重力
: 改變重力力量。將其設為負數將反轉重力方向。

禁用碰撞
: 控制模型部件之間的碰撞。模型中有兩種碰撞器，類型 A 是隨著動畫移動的部件，例如手臂和腿部，類型 B 是自由移動的部件，通常它們通過一個或多個關節與其他部件相連。默認情況下，類型 B 會與類型 A 發生碰撞，但如果您打開「禁用碰撞」，則類型 B 物件將不再與類型 A 物件發生碰撞，而是穿透過去。

每秒步數
: 物理模擬是在一定的間隔步數之間計算的，如果間隔是固定的，效果最好。此選項控制在一秒內執行多少次模擬。次數越多越好，但太多步數會降低幀率。最好與您的幀率相匹配，以獲得平滑的動畫。