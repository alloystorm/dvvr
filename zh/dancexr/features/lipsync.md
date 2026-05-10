---
layout: release
title: 口型同步
locale: zh-CN
toc: true
---

# 口型同步

口型同步（LipSync）可根据音频信号实时驱动角色的口型，使角色看起来能随着播放的任何音频说话或唱歌。与内置于 [AI Voice Chat](ai_chat) 的旧版口型同步不同，本系统**适用于所有平台**，包括 Android 和 Quest。

新增于 **2024.9**。

---

## 启用口型同步

<!-- TODO: confirm exact UI path. -->

1. 在 [Playback Options](playback_options) 中全局开启口型同步。
2. 对于需要活动嘴巴的每个角色，打开 [Facial Control](facial_control) 并启用 **口型同步**。

两个开关都必须启用：全局开关控制是否分析音频；每个角色开关控制哪些角色会对此做出反应。

---

## 与空间音频配对

口型同步与 [Spatial Audio](spatial_audio) 天然匹配——将音频锚定到角色的头部，并在该角色上启用口型同步，效果就会呈现出“该角色正在说话”的印象。

---

## 与 AI 语音聊天配对

[AI Voice Chat](ai_chat) 生成的语音音频，可以像音乐或视频音频一样被口型同步系统分析。 <!-- TODO: confirm whether AI Voice Chat uses LipSync directly, or its own internal mouth driver, or both. -->

---

## 设置

<!-- TODO: list. Likely candidates: sensitivity / gain, smoothing, mouth-open intensity, which morph(s) drive what. -->

---

## 限制

<!-- TODO: confirm. Areas to verify:
- Does it require specific blendshapes / morphs (a / i / u / e / o)? What if the model lacks them?
- Does it work with PMX, XPS, and FBX equally?
- Latency on Android / Quest. -->

---

## 相关页面

- [Playback Options](playback_options)
- [Facial Control](facial_control)
- [Spatial Audio](spatial_audio)
- [AI Voice Chat](ai_chat)
- [Blink, Breathing & Eye Contact](eyecontact)