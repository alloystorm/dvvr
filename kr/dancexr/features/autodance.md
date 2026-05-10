---
layout: release
title: 자동 댄스
locale: ko-KR
toc: true
---

# 자동 댄스

<!-- TODO: settings 확인 필요. 프로시저 모션 계열에서 작성됨. -->

Auto Dance는 **초기 세대**의 프로시저 댄스 생성기입니다. 내장 모션 라이브러리에서 댄스 동작을 실시간으로 생성하며, 음악의 비트와 음량에 반응하여 동작을 선택하고 블렌딩합니다.

Auto Dance는 [Auto Dance 2](autodance2)와 [Auto Dance 3](autodance3)에 의해 상당 부분 대체되었습니다. 최신 버전들은 더 많은 변화, 더 정교한 제어, 그리고 향상된 음악 싱크를 제공합니다. 원래 생성기의 동작을 특별히 원할 때 Auto Dance를 사용하십시오.

---

## 작동 방식

- DanceXR는 재생되는 오디오에서 **비트** (타이밍)와 **음량** (에너지)을 분석합니다.
- 각 비트마다 생성기는 짧게 제작된 댄스 세그먼트 라이브러리에서 다음 동작을 선택하고 이전 동작과 블렌딩합니다.
- 음량이 높은 구간에서는 더 크거나 에너지가 넘치는 동작이 활성화됩니다.

Auto Dance를 위해 VMD 파일을 로드할 필요가 없습니다. 동작이 생성됩니다.

---

## 설정

<!-- TODO: 정확한 설정을 확인해야 합니다. 가능한 후보:
- 변화 폭 / 풀 크기
- 에너지 승수
- 난수 시드 (재현 가능한 시퀀스를 위해) -->

---

## Auto Dance와 최신 버전의 선택 시기

- **Auto Dance (이 페이지)** — 원래의 생성기입니다. 동작 라이브러리가 더 작고, 음악 반응이 더 단순합니다.
- **[Auto Dance 2](autodance2)** — 2세대이며, 풀(pool)이 더 크고 동작 간 변화가 더 많습니다.
- **[Auto Dance 3](autodance3)** — 현재 기본값입니다. 사용자 정의가 매우 뛰어나고, [Sex Motion 3](sex_motion_3) 공유 모션 제어 시스템과 통합되며, 비트 감지 기능이 있는 실시간 오디오 분석기를 사용합니다.

---

## 관련 페이지

- [Auto Dance 2](autodance2)
- [Auto Dance 3](autodance3)
- [Music Timing](music_timing)
- [Audio Options](audio_options)
- [AI in DanceXR](../ai)