---
layout: release
title: T台走動
locale: zh-TW
toc: true
---

# 走秀動作

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

走秀動作是一種程序化的行走/T台走動動作。角色的走路步伐帶有走秀的氣勢——包括髖部擺動、有意識的邁步以及抬頭的姿態——即使沒有 VMD 走路動作檔案，也能呈現。

適用場景：

- 角色從場外入場的擺姿場景。
- 走秀/時尚影片。
- 在另一個動作開始之前填補時間。

---

## 行為

- 角色沿著場景 Z 軸前進（或朝著目標移動 — <!-- TODO: confirm whether target selection is exposed -->）。
- 邁步間距是程序化的；如果設定了音樂 BPM ([Music Timing](music_timing))，步伐可以與節拍同步。
- 這個動作會循環；角色會持續行走，直到您停止它或分配另一個動作。

---

## 設定

<!-- TODO: confirm exact slider names. Likely candidates:
- Walk speed
- Stride length
- Hip sway intensity
- Arm swing intensity
- Direction / target -->

---

## 與其他動作的組合

走秀動作很適合作為**次要動作**，層疊在臉部/面部表情軌道上 ([Secondary Motion](secondary_motion), [Motion Passes](motion_passes))。建議使用 [Feet Adjustment](feet_adjustment) 中的「腳底著地」調整，以確保程序化的腳步能正確地落地。

---

## 相關頁面

- [Idle Motion](idle_motion)
- [Auto Dance 3](autodance3)
- [Lifelike Motions](lifelike_motions)
- [Feet Adjustment](feet_adjustment)
- [Music Timing](music_timing)