---
layout: release
title: 屏幕
locale: zh-CN
toc: true
---

# 屏幕

<!-- TODO: confirm exact settings. Drafted from release notes (2024.5 LED screen mode, props release notes). -->

屏幕是一种可定制的道具，可在平坦的表面上显示图像、视频或场景摄影机的视图。可用于舞台背景、显示器、投影屏幕，或作为 [room stage](room_stage) 内部的媒体表面。

在早期版本中，之前的“屏幕”道具被拆分成了两个：[Mirror](mirror)（反射型）和屏幕（显示型）。它们共享基础的放置和尺寸，但材质和源设置不同。

---

## 源

选择屏幕显示的内容：

- **Camera** — 场景摄影机的视图（要在舞台屏幕上看到角色的表演，请在场景中使用第二个摄影机）。
- **Video** — 通过 [视频播放器](video_player) 播放的视频文件。请将视频放置在您的 [content library](../preparecontent) 的 `videos/` 文件夹中。
- **Image** — 静态纹理。

---

## 表面模式

于 2024.4 / 2024.5 版本添加：

- **Standard** — 平坦材质；适用于需要可调节反射率的电视式屏幕。
- **Emissive** — 屏幕表面向场景发出光线，无需外部照明。
- **LED screen** — 模拟舞台 LED 面板的外观，包括像素网格和辉光特性。适用于音乐会舞台。
- **Projector** — 需搭配光图案器使用；请参阅 [Lighting](lighting)。

当屏幕源设置为 *Camera* 模式时（该模式随道具拆分而来），角色会与连接到屏幕道具的摄影机进行眼神交流。

---

## 反射

屏幕表面可从光滑（电视式房间反射）到磨砂（投影屏幕行为）不等。请在表面设置中调整粗糙度。

---

## 可见摄影机模型

当屏幕源是场景摄影机时，屏幕位置会渲染一个小摄影机模型。这在音乐会模式下设置舞台镜头时非常有用。请在屏幕设置中切换可见性。

---

## 相关页面

- [视频播放器](video_player)
- [Mirror](mirror)
- [Props](props)
- [Room Stage](room_stage)
- [Lighting](lighting)