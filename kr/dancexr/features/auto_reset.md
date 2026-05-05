---
layout: feature
title: 자동 초기화
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

# 자동 초기화

속도가 안전 한계를 초과할 때 본(bone)과 그 하위 본(children)을 자동으로 초기화합니다. 극단적인 힘이나 순간이동(teleportation) 시 발생하는 물리 폭발 및 메시 변형을 방지합니다.

## 임계값

물리가 초기화되는 속도 임계값을 설정합니다. 낮은 값은 초기화를 더 민감하게 발생시켜 클리핑을 방지할 수 있지만, 빠른 움직임 중에 눈에 띄는 끊김(snaps)을 유발할 수 있습니다. 높은 값은 개입하기 전에 더 극단적인 움직임을 허용합니다.