---
layout: feature
title: 頭髮物理學
locale: zh-TW
---

# 髮絲物理

將鏈式物理應用於模型上的髮絲。選定的根骨骼會連接成一個物理鏈，每個子骨骼都會根據彈簧阻尼動力學擺動和彈跳。

## 骨骼選擇

使用 **Select Bones** 選擇根髮骨骼—系統會自動遍歷子骨骼來建立鏈。**Skip First X Bones** 會讓根骨骼保持未連接狀態，以獲得更穩定的基礎。**Max Levels** 設定鏈的最大深度（0 = 無限）。預設設定讓您能在不同模型間儲存配置。

## 物理模式

**Auto** 遵循系統預設值。**PhysX** 使用基於關節的剛體物理，搭配膠囊體或球體碰撞體。**XPBD** 使用基於粒子的模擬，對於長鏈更穩定。此模式決定了顯示哪些設定面板。

## PhysX 設定

當使用 PhysX 模式時顯示。**Spring Force**（對數）控制剛度—數值越高，髮絲越接近其靜止姿勢。**Damping** 減少振盪。**Stiffness Reduction** 在每個鏈節點處軟化彈簧，使髮梢更自由地擺動。**Twist Limit** 限制骨骼軸周圍的旋轉。**Limit Force** 控制關節抵抗其約束力的強度。**Mass** 和 **Drag** 影響慣性和空氣阻力。**Collider Radius** 設定碰撞球體的大小；**Collider Length** 將其沿著骨骼尺寸化為膠囊體。**Anchor Position** 選擇關節的連接位置（0 = 父骨骼，1 = 子骨骼）。

## XPBD 鏈

當使用 XPBD 模式時顯示。配置基於粒子的鏈模擬，包含**Rotation Compliance**（旋轉相容度）、**Twist Compliance**（扭轉相容度）、**Stiffness Reduction**（剛度降低）、**Mass Reduction**（質量降低）和**Constraint Damping**（約束阻尼）。**Particle Anchor** 控制連接位置。碰撞層設定為 Hair，用於與場景其他部分互動。

## 視覺化

**Visualize Bodies** 渲染物理體的碰撞體形狀。
**Visualize Joints** 顯示關節限制和驅動目標為線框縮圖。

# 子組件

## XPBD

為髮絲、布料和其他懸垂部件配置基於粒子的鏈或網格模擬。**Rotation Compliance** 控制鏈在每個關節處彎曲的程度（越高 = 越靈活）。**Twist Compliance** 控制骨骼軸周圍的旋轉。對於網格模式，**Lateral Compliance** 會在相鄰鏈之間添加橫向連接。

**Stiffness Reduction**（10的次方尺度）會乘上每個級別的相容度—超過 1 的數值會使鏈逐漸變得更鬆弛，直到髮梢。**Mass Reduction**（2的次方尺度）會在每個級別減少質量。**Particle Anchor** 定位了沿著片段的關節。**Constraint Damping** 平滑了求解步驟之間的振盪。**Inertia** 增加了對運動變化的阻力。**Particle Radius** 設定碰撞體的大小（單位為毫米）。**Use Sphere Shape** 用球體替換膠囊體粒子，用於除錯。