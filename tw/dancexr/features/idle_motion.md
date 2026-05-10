---
layout: release
title: 待機動畫
locale: zh-TW
toc: true
---

# 靜止動作

<!-- TODO: confirm UI labels. Drafted from release notes (2025.12) and the procedural-motion family. -->

靜止動作是一種程序化動作，當角色未分配其他動作時會播放。它模擬呼吸、重心轉移以及細微的頭部和肢體移動，使角色在站立姿勢時看起來栩栩如生，而不是僵硬。

---

## 靜止動作播放時機

- 當分配給角色任何動作之前。
- 當動作結束時（且角色不屬於某個序列）。
- 在序列中的暫停期間。

如果正在播放明確指定的動作，靜止動作將不會運行。若要在活動動作上疊加細微的微小動作，請參閱 [Lifelike Motions](lifelike_motions) 頁面。

---

## 設定

<!-- TODO: confirm exact slider names and ranges. -->

- **強度 (Intensity)** — 靜止動作的整體振幅。
- **速度 (Speed)** — 呼吸/重心轉移週期運行的速度。
- **身體擺動、頭部動作 (Body sway, head movement)** — 各區域的乘數。

---

## 新的靜止動作 (v2025.12)

DanceXR 2025.12 引入了由新的程序化動作控制系統驅動的更自然靜止動作。新版本比早期版本產生更流暢、更不重複的靜止動畫。我們計劃在未來發布中對程序化動作控制進行更多改進。

---

## 相關頁面

- [Lifelike Motions](lifelike_motions) — 任何動作上的細微微小動作
- [Catwalk Motion](catwalk)
- [Auto Dance 3](autodance3)
- [Blink, Breathing & Eye Contact](eyecontact)
- [Motion Settings](motion_settings)