---
layout: release
title: HDR 显示器支持
locale: zh-CN
toc: true
---

# 高动态范围显示支持

DanceXR 可输出到 **高动态范围 (HDR) 显示器**，从而同时呈现更亮的亮点和更深的阴影。与 SDR 输出相比，HDR 模式在强光场景（皮肤上的阳光、舞台激光、带点光源的黑暗室内）中保留了更多的对比度。

新增于 **2024.1**。

---

## 要求

- 具备 HDR 功能的显示器。
- 在 **Windows 显示设置**中启用 HDR。

---

## 启用 HDR

当 Windows 报告 HDR 已启用时，DanceXR 会自动检测到 HDR。无需手动设置即可将其开启 **使用**。

如需明确关闭 HDR（例如，在比较截图或为 SDR 目标录制时），请使用 [图形设置](graphics) 中的 **HDR** 开关。

---

## HDR 最直观可见的场景

- 黑暗背景上的明亮高光——舞台聚光灯、[激光阵列](laser)、[光线追踪](raytracing) 场景。
- 强定向光下的肤色——与 [皮肤材质](material_skin) 效果良好。
- 可见太阳和月亮的夜空渐变（参见 [天空](sky) 和 2025.7 天空着色器说明）。

---

## 相关页面

- [图形设置](graphics)
- [显示设置](display_settings)
- [照明](lighting)
- [创作版](../creator) — 录制/视频输出注意事项