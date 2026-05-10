---
layout: release
title: 走秀動作
locale: zh-TW
toc: true
---

# 走秀動作

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

走秀動作是一種程序化的行走/走秀動作。該角色以走秀的步態（包括髖部擺動、有意識的邁步、抬頭的姿態）行進到目標點，且無需 VMD 走路動作資源。

適用場景：

- 角色從舞台外入場的擺姿場景。
- 走秀/時尚影片。
- 在另一個動作開始前填補時間。

---

## 行為

- 角色沿著場景 Z 軸前進（或朝著目標移動 — <!-- TODO: confirm whether target selection is exposed -->）。
- 邁步間距是程序化的；如果設定了音樂 BPM ([Music Timing](music_timing))，步伐可以與節拍同步。
- 此動作會循環；角色會持續行走，直到您停止它或指派另一個動作。

---

## 相關頁面

- [Idle Motion](idle_motion)
- [Auto Dance 3](autodance3)
- [Lifelike Motions](lifelike_motions)
- [Feet Adjustment](feet_adjustment)
- [Music Timing](music_timing)