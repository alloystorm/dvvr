---
layout: release
title: 遥控器
locale: zh-CN
toc: true
---

# 远程控制

<!-- TODO: confirm everything below against current behavior. Drafted from the 2024.12 release notes (initial public beta) — feature has likely evolved since. -->

远程控制允许 **Android 应用**充当连接到同一局域网内**另一设备上运行的 DanceXR** 的无线控制器。当主 DanceXR 会话在 PC、头戴设备或客厅屏幕上运行时，您可以使用手机或平板电脑更改场景、动作和设置。

于 **2024.12** 作为公开测试版发布。

---

## 何时使用

- 在录制过程中调整设置，无需走到键盘前。
- 从手机控制沙发/大屏幕 DanceXR 会话。
- 从 Android 手机操作 Quest 独立会话，而不是摸索着使用虚拟现实（VR）内的菜单。

---

## 要求

<!-- TODO: confirm minimum Android version, whether Quest standalone (Mix / Immersion) is supported as the *controller*, whether iOS is supported. -->

- 安装了 DanceXR Android 应用的 Android 设备。
- 可在同一局域网 (LAN) 上访问的 PC、Quest 或其他 DanceXR 实例。
- 两台设备必须位于同一网络段（无客户端隔离）。

---

## 如何连接

<!-- TODO: walk through the actual UI. Drafted from release notes only. -->

1. 在主机设备（PC、Quest 等）上启动 DanceXR。
2. 打开 Android 应用，并在主菜单中选择 **远程控制**。
3. 应用会在本地网络上发现 DanceXR 实例。选择主机。
4. Android UI 会用一个触摸板加菜单表面替换其自身的场景视图，该表面会镜像主机的用户界面 (UI)。

---

## 远程可执行的操作

- 访问（几乎所有）菜单和选项。
- 使用触摸板旋转摄影机并移动角色。
- 切换动作、场景和舞台。

<!-- TODO: confirm which menus or actions are *not* available remotely. -->

---

## 网络协议

<!-- TODO: confirm. Release notes mention a custom protocol for low-latency, but no further public spec. -->

远程控制使用本地网络上的自定义 DanceXR 协议，而不是 HTTP。此协议针对局域网的低延迟进行了优化；它并非设计用于跨越互联网的路由。

---

## 故障排除

<!-- TODO: fill in real cases users hit (firewall blocking discovery, mismatched versions, Wi-Fi vs Ethernet). -->

- **列表中未显示主机：** 确认两台设备位于同一网络，并且防火墙没有阻止 DanceXR 的发现端口。
- **输入延迟或卡顿：** 最好使用 5 GHz Wi-Fi 或有线主机；避免带有客户端隔离功能的访客网络。
- **版本不匹配：** 主机和 Android 控制器应运行相同版本的 DanceXR。

---

## 相关页面

- [应用设置](application_settings)
- [控制与用户界面](../controls)
- [VR 操作](../vr_operations) — 用于在主机上运行的 VR 会话