---
layout: release
title: 头发材质
locale: zh-CN
toc: true
---

# 头发材质

控制被归类为 **头发** 的材质属性。头发材质使用特殊的着色器，通过 **各向异性** 高光来产生真实头发具有的方向性光泽——光泽沿着头发的流动方向呈长条状，而非圆形高光。

---

## 此类别控制的内容

- **基础颜色** 和 **平滑度** — 与其他材质类别相同的控制参数。
- **各向异性高光** — 方向性光泽的形状和强度。
- **头发流动方向** — 高光沿着发丝流动的方向。
- <!-- TODO: confirm whether two-tone / tip-color / scatter parameters are exposed. -->

头发着色器随着时间不断改进。值得注意的发布版本包括：

- **2024.5** — 改进的程序化头发细节贴图。
- **2025.10** — 改进的 LW / Android 皮肤和头发着色器，减少头发上的过度天空反射。

---

## 材质分类

DanceXR 会自动将名称匹配通用头发关键词的材质分配到此类别。如果模型错误地分类了头发（或将头发材质名称分配给了非头发几何体），请从 [材质设置](material_settings) 手动重新分配。

[材质如何分类](material_settings#material-category)

---

## 头发物理属于独立部分

头发 **运动** — 头部转动或角色行走时骨骼的摆动 — 在 [头发物理](hair_physics)（或在新的模拟系统上的 [粒子动态](particle_dynamics)）中配置。此材质页面仅控制头发表面的渲染方式。

---

## 相关页面

- [材质设置](material_settings)
- [皮肤材质](material_skin)
- [头发物理](hair_physics)
- [粒子动态](particle_dynamics)
- [卡通着色](toon_shading)