---
layout: release
title: 髮絲材質
locale: zh-TW
toc: true
---

# 髮質材料

控制分類為**髮質**的材質屬性。髮質材料使用帶有**各向異性**高光的特殊著色器，產生真實頭髮具有的方向性光澤——這是一種沿著髮流方向而非圓形的鏡面反射條狀高光。

---

## 本類別控制內容

- **基礎顏色** 和 **平滑度** — 與其他材質類別相同的控制。
- **各向異性高光** — 方向性光澤的形狀和強度。
- **髮流方向** — 高光沿著髮絲的哪個方向運行。
- <!-- TODO: confirm whether two-tone / tip-color / scatter parameters are exposed. -->

髮質著色器隨著時間不斷改進。值得注意的發布版本包括：

- **2024.5** — 改善了程序化髮質細節圖譜。
- **2025.10** — 更好的 LW / Android 膚質和髮質著色器，頭髮上的天空反射更少。

---

## 類別化

DanceXR 會自動將名稱符合常見髮質關鍵字的材質分配到此類別。如果模型誤分類了其髮質（或將髮質材質名稱分配給非髮質幾何體），請從 [材質設定](material_settings) 手動重新分配。

[材質如何被分類](material_settings#material-category)

---

## 髮質物理獨立於此處

髮質**運動** — 拍攝者轉頭或角色行走時骨骼擺動 — 是在 [髮質物理](hair_physics) 中配置的（或在新的模擬系統中透過 [粒子動力學](particle_dynamics)）。材質頁面僅控制髮質表面的渲染方式。

---

## 相關頁面

- [材質設定](material_settings)
- [膚質材質](material_skin)
- [髮質物理](hair_physics)
- [粒子動力學](particle_dynamics)
- [卡通著色](toon_shading)