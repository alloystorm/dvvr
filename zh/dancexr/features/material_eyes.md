---
layout: release
title: 眼睛材质
locale: zh-CN
toc: true
---

# 眼睛材质

<!-- TODO: confirm exact settings exposed in the eyes submenu. Drafted from sister material pages. -->

控制归类为**眼睛**的材质属性。眼睛材质默认具有更高的平滑度，因此比皮肤或毛发更能反射环境，呈现出其特有的光亮外观。

眼睛材质在 **2024.1** 版本中拥有了自己的预设列表。

---

## 此类别控制的内容

- 平滑度/粗糙度 — 眼睛的光泽度/湿润度。
- 从环境反射的强度。
- <!-- TODO: confirm:
  - Iris / sclera split, if exposed.
  - Pupil size or eye-shine controls.
  - Anisotropic shading for irises (sometimes used to simulate fiber direction). -->

---

## 分类

DanceXR 会将名称匹配常见眼部关键词的材质自动分配到此类别。如果模型错误地将眼部几何体分类为不透明或皮肤，请通过 [Material Settings](material_settings) 手动重新分配。

[如何分类材质](material_settings#material-category)

---

## 眼睛的行为与材质是分离的

眼睛的**运动**（如眨眼、注视、眼神交流）是在 [Blink, Breathing & Eye Contact](eyecontact) 中配置的，而不是在此处。材质页面只控制眼睛表面如何渲染。

---

## 相关页面

- [Material Settings](material_settings)
- [Skin Materials](material_skin)
- [Hair Materials](material_hair)
- [Blink, Breathing & Eye Contact](eyecontact)