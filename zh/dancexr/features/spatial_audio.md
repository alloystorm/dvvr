---
layout: release
title: 空间音频
locale: zh-CN
toc: true
---

# 空间音频

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. -->

空间音频播放场景音频时，不是作为一个平面立体声混音，而是从 3D 空间中的特定位置播放。将音频锚定到角色的头部，会使声音随着该角色移动，这极大地增强了 VR 和多角色舞台的临场感。

添加于 **2024.9**。

---

## 启用空间音频

<!-- TODO: confirm exact menu path. Drafted from the release notes which name the option as "Spatialize" under Playback Options. -->

1. 打开 [播放选项](playback_options)。
2. 开启 **空间化**。
3. 从下拉菜单中选择一个角色——该角色的 **头部位置** 将成为音频源。

音频随后会随距离衰减，并相对于摄影机或 VR 头戴设备进行正确的环绕播放。

---

## 行为

- 音频源会随着角色移动，跟随所选角色的头部骨骼。
- 在 VR 中，该效果使用头部追踪，因此转动头部可以自然改变左右声场平衡。
- <!-- TODO: confirm whether stereo is preserved or audio is downmixed to mono at the source. -->
- <!-- TODO: confirm distance attenuation curve and whether it is configurable. -->

---

## 与口型同步的组合使用

空间音频与同一版本中引入的 [音频驱动的口型同步](lipsync) 完美结合：将音频锚定到角色的头部，并使用同一音频驱动该角色的口型，可以提供持续的“这是该角色在说话”的效果。

---

## 限制

<!-- TODO: confirm. Likely areas to verify: which audio types this applies to (music vs voice chat vs video), behavior with multiple actors, behavior on Android / Quest, behavior in AR mode. -->

---

## 相关页面

- [播放选项](playback_options)
- [音频选项](audio_options)
- [口型同步](lipsync)
- [AI语音聊天](ai_chat)