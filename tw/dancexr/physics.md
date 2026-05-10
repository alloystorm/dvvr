---
layout: release
title: 物理系統
locale: zh-TW
toc: true
---

# 物理系統

DanceXR 為角色模型提供特定於模型格式的物理系統，此外還建構了自定義的 XPBD（擴展粒子動力學）系統，可模擬布料、軟體和簡化的剛體。

PMX 模型內建了物理元件定義，因此開箱即用。您可以在 [PMX 物理設定](features/pmx_physics) 中自定義和微調 PMX 模型的物理行為。

對於 XPS 和 FBX 模型，您需要使用提供的、為常見用例量身定制的物理工具從零開始設置物理。有關工具列表及其推薦的用例，請參閱下方。

預設情況下，物理系統使用基於 PhysX 的內建 Unity 物理引擎。我們還擁有一個基於 XPBD（擴展基於位置的動力學）的自定義物理引擎，它特別適用於布料和頭髮，並提供更佳的控制和穩定性。

有關術語（剛體、關節、碰撞器、彈簧力、阻尼、投影距離、投影角度），請參閱 [概念與術語表](concepts#bones-physics-and-colliders)。

---

## 物理工具

物理工具集是一組允許您快速為模型設置物理的工具。每個獨立工具都專注於特定的用例，最大限度地減少了您需要調整的參數數量以達到理想效果。大多數時候，您只需要選擇正確的骨骼就能獲得所需的行為。此外，還有預設值以幫助您快速找到良好的設定，並提供視覺化效果以了解每個參數的影響。

- [身體碰撞器](features/body_colliders) — 沿著角色身體配置的膠囊碰撞器，用於讓自由移動的部位（頭髮、布料、裙子）與身體發生碰撞，而不是穿透。
- [頭髮物理](features/hair_physics) — 在根植於頭部的骨骼樹上進行的彈簧骨骼模擬。設置根骨骼，DanceXR 會遍歷子骨骼來建構骨骼。
- [裙子物理](features/skirt_physics) — 具有水平連接的鏈式物理（類似網狀），適用於裙子和邊緣。
- [垂飾物理](features/dangling_physics) — 沒有水平連接的鏈式物理，適用於彩帶、繫帶、耳鏈、動物尾巴、任何懸掛的物體。
- [胸部物理](features/boobs_physics) — 基於關節的胸部擺動模擬，配有反重力以補償恆定的向下拉力。
- [軟體物理](features/softbody_physics) — 使用彈簧力約束網格連接骨骼，模擬身體部位（如臀部和大腿）的體積變形。
- [分離物體](features/detach_object) — 釋放一個骨骼或物體，讓您通過使其脫落來移除某些部分。當這些部分沒有單獨材料無法用透明度隱藏時，這非常有用。

演示影片：
{% include video id="-IZTzHUpROs" provider="youtube" %}

---

## 模擬系統

模擬系統是一個自定義的 XPBD（擴展粒子動力學）系統，可用於模擬布料、軟體和流體。

- [布料模擬](features/cloth_simulation) — 為模型添加布料。
- [網格到布料](features/mesh_to_cloth) — 將模型上的網格轉換為布料模擬物體。
- 流體模擬 — 使用粒子模擬簡單的流體效果，例如黏度。
- [觸手模擬](features/tentacles) — 通過用約束和驅動力連接節點來模擬觸手運動。

---

## 設定

您可以使用以下設定來控制物理行為。

- [系統級物理設定](features/system_physics) — 全局設定，不論模型格式或骨骼類型，都適用於 DanceXR 中的所有物理模擬。
- [PMX 物理設定](features/pmx_physics) — 覆蓋模型檔案中物理定義的 PMX 特定設定。
- 物理工具：
    - [身體碰撞器](features/body_colliders) — 身體沿著身體的碰撞器尺寸和位置。
    - [頭髮物理](features/hair_physics) — 頭髮物理的彈簧力、阻尼、碰撞器半徑和骨骼選擇。
    - [裙子物理](features/skirt_physics) — 裙子物理的彈簧力、阻尼、碰撞器半徑和骨骼選擇。
    - [垂飾物理](features/dangling_physics) — 垂飾物理的彈簧力、阻尼、碰撞器半徑和骨骼選擇。
    - [胸部物理](features/boobs_physics) — 胸部物理的彈簧力、阻尼、碰撞器半徑、骨骼選擇和反重力。
    - [軟體物理](features/softbody_physics) — 軟體物理的粒子尺寸、約束符合度和骨骼選擇。
    - [分離物體](features/detach_object) — 分離物體所需的骨骼選擇。
- [布料模擬設定](features/cloth_simulation) — 布料模擬的網格創建參數、模擬參數和碰撞器調整。它包括
    - Cloth Mesh 1
    - Cloth Mesh 2
    - Fluid Simulation
    - Mesh To Cloth
- [觸手模擬設定](features/tentacles) — 觸手模擬的節點數、彈簧力、阻尼和碰撞器半徑。
- [玩偶骨架設定](features/ragdoll) — 玩偶骨架模擬的關節限制、彈簧力、阻尼和碰撞器半徑。

---

## 進一步閱讀

- [概念與術語表](concepts#bones-physics-and-colliders)
- [使用角色模型](actors)
- [骨骼結構範例](features/bones) — 骨骼選擇參考骨骼