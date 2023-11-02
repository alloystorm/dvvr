---
layout: single
title: 시스템 물리학
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/system_physics) | [繁中](/tw/dancexr/features/system_physics) | [日本](/jp/dancexr/features/system_physics) | [한국어](/kr/dancexr/features/system_physics) | [简中](/zh/dancexr/features/system_physics)


## 시스템 전체 물리학 설정
시스템 전체 물리학 설정은 설정 -> 옵션 -> 물리학에서 찾을 수 있습니다.

![시스템 물리학](/images/system-physics.png)

활성화
: 물리 시뮬레이션을 켜거나 끕니다.

중력
: 중력 힘을 변경합니다. 음수로 설정하면 중력 방향이 반대로 됩니다.

충돌 비활성화
: 모델 부분 간의 충돌을 제어합니다. 모델에는 2 종류의 충돌체가 있습니다. A 유형은 팔과 다리와 같이 애니메이션과 함께 움직이는 것이고, B 유형은 자유롭게 움직이는 것으로, 일반적으로 하나 이상의 조인트로 다른 부분에 연결됩니다. 기본적으로 B 유형은 A 유형과 충돌하지만 "충돌 비활성화"를 켜면 B 유형 객체는 더 이상 A 유형 객체와 충돌하지 않고 통과합니다.

초당 단계 수
: 물리 시뮬레이션은 단계 간의 일정한 간격으로 계산되며, 일정한 간격이 가장 잘 작동합니다. 이 옵션은 1초에 수행되는 시뮬레이션 수를 제어합니다. 수가 많을수록 좋지만, 너무 많은 단계는 FPS를 늦출 수 있습니다. 부드러운 애니메이션을 위해 FPS와 일치시키는 것이 가장 좋습니다.