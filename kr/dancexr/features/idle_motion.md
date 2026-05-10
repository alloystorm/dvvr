---
layout: release
title: 대기 동작
locale: ko-KR
toc: true
---

# 대기 모션

<!-- TODO: confirm UI labels. Drafted from release notes (2025.12) and the procedural-motion family. -->

대기 모션은 캐릭터에게 다른 모션이 할당되지 않았을 때 재생되는 프로시저 모션입니다. 캐릭터가 정지된 것처럼 보이는 대신, 마치 숨쉬기, 체중 이동, 작은 머리 및 사지 움직임을 시뮬레이션하여 살아있는 것처럼 보이게 합니다.

---

## 대기 모션이 재생될 때

- 캐릭터에게 모션이 할당되기 전.
- 모션이 끝날 때 (그리고 캐릭터가 시퀀스에 포함되지 않은 경우).
- 시퀀스 중 일시 정지 시간 동안.

명시적인 모션이 재생 중이라면, 대기 모션은 실행되지 않습니다. 활성화된 모션 위에 미세한 움직임을 겹치려면 대신 [Lifelike Motions](lifelike_motions)를 참조하세요.

---

## 설정

<!-- TODO: confirm exact slider names and ranges. -->

- **강도** — 대기 움직임의 전반적인 진폭.
- **속도** — 호흡/체중 이동 사이클이 실행되는 속도.
- **몸 흔들림, 머리 움직임** — 영역별 승수.

---

## 새로운 대기 모션 (v2025.12)

DanceXR 2025.12는 새로운 프로시저 모션 제어 시스템으로 구동되는 더욱 자연스러운 대기 모션을 도입했습니다. 새로운 버전은 이전 빌드보다 더욱 부드럽고 반복성이 낮은 대기 애니메이션을 생성합니다. 프로시저 모션 제어에 대한 추가 개선 사항은 향후 출시 버전에 계획되어 있습니다.

---

## 관련 페이지

- [Lifelike Motions](lifelike_motions) — 어떤 모션 위에든 미세한 움직임 추가
- [Catwalk Motion](catwalk)
- [Auto Dance 3](autodance3)
- [Blink, Breathing & Eye Contact](eyecontact)
- [Motion Settings](motion_settings)