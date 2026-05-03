---
layout: release
title: 라그돌
locale: ko-KR
nav_links:
  - label: 소개
    url: /kr/dancexr
  - label: 기능
    url: /kr/dancexr/features
  - label: 출시
    url: /kr/dancexr/releases
  - label: 다운로드
    url: /kr/dancexr/download
---

# 래그돌

배우의 애니메이션 스켈레톤을 입자 기반 래그돌 물리 시뮬레이션으로 대체합니다. 몸이 흐느적거리며 중력 및 외부 힘에 반응합니다.

**스프링 힘(Spring Force)**과 **감쇠(Damping)**(둘 다 로그 스케일)는 래그돌이 애니메이션 포즈로 되돌아가려는 강도를 제어합니다. 낮은 값은 몸이 축 처지게 하고, 높은 값은 애니메이션에 더 가깝게 유지합니다. **중력(Gravity)**은 래그돌에 중력을 적용하는 스위치입니다.

**왼쪽/오른쪽 발 고정(Lock Left/Right Foot)**, **머리 고정(Lock Head)**, 그리고 **왼쪽/오른쪽 손 고정(Lock Left/Right Hand)**은 특정 신체 부위를 애니메이션 위치에 고정하여 축 처지지 않게 합니다. 이는 몸의 나머지 부분이 흐느적거리는 동안 발을 땅에 붙이고 있게 하는 데 유용합니다.

**세밀 조정(Fine Tune)**은 본별 힘 스케일을 0(완전히 축 늘어짐)부터 1(완전히 단단함)까지 설정합니다. 다리, 무릎, 팔, 어깨, 몸통, 목, 머리와 같은 개별 신체 부위를 조정하여 국소적인 경직도를 만들 수 있습니다. 예를 들어, 사지를 늘어뜨려 두고 몸통은 단단하게 유지할 수 있습니다.