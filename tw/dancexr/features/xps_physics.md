---
locale: zh-TW
layout: single
title: XPS 物理
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/xps_physics) | [繁中](/tw/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics) | [한국어](/kr/dancexr/features/xps_physics) | [简中](/zh/dancexr/features/xps_physics)

## XPS模型特定設置
XPS模型不附帶物理定義，因此程序不知道在哪裡添加物理組件。為了應對這一情況，為每個XPS模型添加了幾個物理設置，供您配置XPS模型上的物理組件。

這包括
* [身體碰撞器](xps_body_colliders.md)
* [胸部物理](xps_boobs.md)
* [頭髮物理](xps_hair.md)
* [衣服物理](xps_cloth.md)
* [裙子物理](xps_skirt.md)
* [軟體物理](xps_softbody.md)
* [檢測物件](xps_detech.md)


### 演示
{% include video id="-IZTzHUpROs" provider="youtube" %}

要使用XPS物理工具，大多數情況下只需找到並選擇正確的骨骼，程序將為您處理其餘事項。

像馬尾辮和絲帶這樣的東西非常容易，就像上面的視頻中演示的那樣。

有時候子骨骼太多，您實際上需要的骨骼可能被埋在這些子骨骼的幾個層級下。在這種情況下，您可以選擇父骨骼，然後使用“跳過前X個骨骼”設置來微調您的選擇。

如果在過程中出現混亂，不要驚慌。完成您的選擇，然後您可以嘗試在設置中穩定事物。
* 首先嘗試將“交互連接距離”減少到0以禁用交互連接關節，然後
* 嘗試稍微增加碰撞器大小（不要過度）， 
* 如果仍然不起作用，您可以嘗試禁用並重新啟用設置， 
* 然後最終重新加載模型，有時可以解決不穩定性。