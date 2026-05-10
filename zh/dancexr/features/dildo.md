---
layout: release
title: 性玩具
locale: zh-CN
toc: true
---

# 假阳具

<!-- TODO: confirm exact UI labels and configuration. Drafted from related Sex Overlay docs and the prop-attachment system. -->

配置附着在角色身上的假阳具资源。可单独用于单个角色，也可作为配对动作中的男性角色部分，当场景中未加载男性角色时使用。

---

## 设置

1. 在相关角色上启用假阳具。
2. 选择附着骨骼/位置——通常以骨盆为锚点。
3. 调整大小和偏移量。
4. 可选：配置与 [性动作](sex_motion_3) 关联的动画行为（推进模式）或与 [自动更新](autoupdate) 关联的动画行为。

详细的附着配置位于 [性覆盖与假阳具配置](smo_config)。

---

## 设置

<!-- TODO: confirm exact controls. Likely:
- Size / scale
- Position offset
- Rotation
- Curve / bend
- Procedural motion driver (e.g., bound to Sex Motion 3, or driven by Auto Update) -->

---

## 与动作配对

- 使用 [性动作 3](sex_motion_3)——假阳具可以在配对动作中充当男性角色。动作的接触框系统会将假阳具对齐到女性的接触点。
- 使用 [自动更新](autoupdate)——根据音频电平或节拍驱动推进模式，实现与音乐同步的动作。

---

## 相关页面

- [性覆盖与假阳具配置](smo_config)
- [性动作 3](sex_motion_3)
- [女上位性动作](scg_motion)
- [性动作 2](sfb_motion)
- [自动更新](autoupdate)