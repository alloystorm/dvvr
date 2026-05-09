---
layout: release
title: 비트 링
locale: ko-KR
---

# 비트 링

<!-- TODO: full description. The Beats Ring is referenced as a tile on /dancexr/features under Stage & Props but no other page describes it. Likely an audio-reactive visualizer ring; confirm and fill in. -->

비트 링은 음악에 맞춰 맥동하는 오디오 반응형 비주얼라이저 프로프입니다. 이는 [auto-update](autoupdate) 데이터 소스 중 하나로, 다른 설정들이 이 출력을 통해 자체적으로 구동될 수 있음을 의미합니다.

---

## 작동 방식

<!-- TODO: confirm shape (ring? particles? geometry?), where it is rendered (around the actor? on the stage?), how it scales with audio. -->

비트 링은 현재의 오디오 신호를 가져와 비트 구동 값을 생성하며, 이 값은 다음 용도로 사용될 수 있습니다:

- 액터 또는 무대 주변에 보이는 링 또는 맥동 효과를 렌더링합니다.
- 음악에 맞춰 다른 auto-update 매개변수(조명 강도, 재질 매개변수, 동작 속도)를 구동합니다.

---

## 활성화하기

<!-- TODO: confirm the menu path. Likely under environment menu or a per-actor setting. -->

---

## 설정

<!-- TODO: list. Possibly: visibility, color, scale, sensitivity threshold, smoothing. -->

---

## 관련 페이지

- [Auto update](autoupdate) — 다른 설정을 위한 데이터 소스로 비트 링 사용
- [Music timing](music_timing) — 음악에 동작을 동기화
- [Audio options](audio_options)