---
layout: release
title: XPS 物理學
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

## XPS 模型特定設置
XPS 模型不包含物理定義，因此程式不知道要在哪裡添加物理組件。為了解決這個問題，為每個 XPS 模型添加了幾個物理設置，供您配置 XPS 模型上的物理組件。

這包括：
* [身體碰撞器](body_colliders)
* [胸部物理](boobs_physics)
* [頭髮物理](hair_physics)
* [衣服物理](dangling_physics)
* [裙子物理](skirt_physics)
* [軟體物理](softbody_physics)
* [偵測物體](detach_object)
* [自動重置](auto_reset)

### 演示
{% include video id="-IZTzHUpROs" provider="youtube" %}

使用 XPS 物理工具時，大部分情況下您只需要找到並選取正確的骨骼，程式會幫您處理剩下的部分。

像馬尾辮和絲帶這樣的東西非常簡單，就像上面的影片演示的那樣。

有時候子骨骼太多，您需要的骨骼可能實際上埋在這些子骨骼的幾層深處。這種情況下，您可以選取父骨骼，然後使用「跳過前 X 個骨骼」設置來微調您的選擇。

如果在過程中出現混亂，請不要驚慌。完成您的選取後，您可以在設置中嘗試穩定情況。
* 首先，嘗試將「交互鏈接距離」減小到 0 以停用交互鏈接關節，然後
* 嘗試稍微增大碰撞器尺寸（切勿過度），
* 如果仍然無法解決，可以嘗試停用再重新啟用設置，
* 然後最終重新載入模型，因為這有時可以解決不穩定性。