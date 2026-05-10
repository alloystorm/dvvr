---
layout: release
title: 眼材質
locale: zh-TW
toc: true
---

# 眼睛材質

<!-- TODO: confirm exact settings exposed in the eyes submenu. Drafted from sister material pages. -->

控制被歸類為**眼睛**的材質屬性。眼睛材質預設的光滑度更高，因此它們比皮膚或頭髮更能反射環境，呈現出其特有的光澤感。

眼睛材質在 **2024.1** 版本獲得了自己的預設列表。

---

## 本類控制內容

- 光滑度/粗糙度 — 眼睛光澤度/濕潤度。
- 環境反射強度。
- <!-- TODO: confirm:
  - Iris / sclera split, if exposed.
  - Pupil size or eye-shine controls.
  - Anisotropic shading for irises (sometimes used to simulate fiber direction). -->

---

## 歸類方式

DanceXR 會將名稱與常見眼睛關鍵字匹配的材質自動歸類到此類。如果模型將眼睛幾何體錯誤地分類為不透明或皮膚，請透過 [材質設定](material_settings) 手動重新指定。

[材質如何歸類](material_settings#material-category)

---

## 眼睛行為與材質是分開的

眼睛**運動**—例如眨眼、凝視、視線接觸—是在 [眨眼、呼吸與視線接觸](eyecontact) 中配置的，而不是在這裡。材質頁面僅控制眼睛表面的渲染方式。

---

## 相關頁面

- [材質設定](material_settings)
- [皮膚材質](material_skin)
- [頭髮材質](material_hair)
- [眨眼、呼吸與視線接觸](eyecontact)