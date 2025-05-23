---
locale: ko-KR
layout: single
title: 시뮬레이션
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/simulation) | [繁中](/tw/dancexr/features/simulation) | [日本語](/jp/dancexr/features/simulation) | [한국어](/kr/dancexr/features/simulation) | [简中](/zh/dancexr/features/simulation)

## 시뮬레이션 개요

DanceXR의 시뮬레이션 시스템은 고급 입자 동역학, 의류 시뮬레이션 및 실험적인 유체 시뮬레이션을 포함하여 다양한 사용 사례에 대해 현실적이고 성능이 우수한 물리학을 제공합니다.

---

### 입자 동역학

입자 동역학 시스템은 머리카락, 의류 및 치마에 대한 전통적인 물리학을 대체하여 보다 부드럽고 안정적인 결과를 제공합니다.

- **주요 설정**:
  - 관성
  - 스윙 컴플라이언스
  - 트위스트 컴플라이언스
  - 축소 비율
  - 입자 앵커
  - 측면 컴플라이언스 및 앵커 (치마용)

- **바람과 난기류**:
  - 속도 및 방향에 대한 전역 바람 설정
  - 개별 그룹에 대한 난기류 힘
  - 팬이나 터널과 같은 국소 효과를 위한 바람 필드

---

### 의류 시뮬레이션

의류 시뮬레이션 시스템은 XPS 및 PMX 모델을 지원하며, 깨지지 않는 안정성과 맞춤형 곡선 콜라이더와 같은 기능을 제공합니다.

- **설정**:
  - 조정 가능한 반경, 길이, 경사 및 해상도로 메시 생성
  - 신체 부위에 고정
  - 드래그 및 찢어짐을 위한 상호작용 설정
  - 자체 충돌 및 물리 속성

- **성능 팁**:
  - 최적의 시뮬레이션을 위해 고정된 프레임 속도 사용
  - 모델 별 조정을 위한 콜라이더 형태 조정

- **수중 행동**:
  - 수중 시뮬레이션을 위한 부력 및 드래그 설정

---

### 유체 시뮬레이션 (실험적)

유체 시뮬레이션은 입자 시스템을 확장하여 유체 행동을 시뮬레이션합니다.

- **속성**:
  - 응집력
  - 점도
  - 끈적임

- **렌더링**:
  - 포인트 또는 구체로 렌더링된 유체 입자
  - 미래 업데이트에서 제공될 유체 셰이더

- **사용 사례**:
  - 샤워, 분수 또는 정원 호스와 같은 시나리오 시뮬레이션

---

### 추가 기능

- **부드러운 물체 시뮬레이션**:
  - 가슴, 엉덩이 및 다리와 같은 신체 부분에 대한 현실적인 부드러운 물체 물리학
  - 세밀한 조정을 위한 부피 및 거리 제약
  - 입자 연결을 위한 시각화 도구

- **립 싱크 및 공간 오디오**:
  - 립 싱크는 오디오에서 얼굴 움직임을 생성
  - 공간 오디오는 3D 공간에서 배우의 위치에 따라 소리를 재생

자세한 내용은 [릴리스 노트](/dancexr/releases)를 참조하십시오.