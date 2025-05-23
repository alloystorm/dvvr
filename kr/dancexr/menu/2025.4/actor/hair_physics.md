---
locale: ko-rKR
layout: single
title: 헤어 물리
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/hair_physics) | [繁中](/tw/dancexr/menu/2025.4/actor/hair_physics) | [日本語](/jp/dancexr/menu/2025.4/actor/hair_physics) | [한국어](/kr/dancexr/menu/2025.4/actor/hair_physics) | [简中](/zh/dancexr/menu/2025.4/actor/hair_physics)

[물리](../menu#물리) > 헤어 물리



| Setting | Value | Description |
| :--- | --- | :--- |
|  ☑ 활성화| [ON] | 
|  뼈 선택|| 본 선택
|  ⊖ 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|  ☑ **입자 동역학**| | 
| ├─ ☑ 활성화| [ON] | 
| ├─ ⊖ 스윙 순응도| [0.25] (0 ~ 1) | 
| ├─ ⊖ 트위스트 순응도| [0.75] (0 ~ 1) | 
| ├─ ⊖ 입자 앵커| [0.5] (0 ~ 1) | 
| ├─ ⊖ 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| ├─ □ 시각화| [OFF] | 
| ├─ ⊖ 최대 각속도| [2] (0 ~ 4) | 
| ├─ ⊖ 관성| [2] (1 ~ 5) | 
| ├─ ⊖ 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| ├─ ⊖ 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| ├─ ⊖ 중력| [9.8] (-9.8 ~ 9.8) | 
| ├─ ⊖ 마찰| [1] (0 ~ 2) | 
| ├─ ⊖ 지면 마찰| [1] (-2 ~ 2) | 
| ├─ ⊖ 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| ├─ ⊖ 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| ├─ ⊖ 부력| [-0.1] (-1 ~ 1) | 
| ├─ ⚙️ **바람**| | 
| │ ├─ ⊖ 바람 영향| [0.25] (0 ~ 1) | 
| │ ├─ ⊖ 난류 스케일| [0] (-2 ~ 2) | 
| │ ├─ ⊖ 난류 강도| [1] (0 ~ 2) | 
| │ └─ ⊖ 난류 시간 스케일| [0] (-4 ~ 4) | 
| ├─ ⚙️ **충돌하기**| | 
| │ ├─ ☑ 머리| [ON] | 
| │ ├─ ☑ 몸체| [ON] | 
| │ ├─ ☑ 가슴| [ON] | 
| │ ├─ ☑ 엉덩이| [ON] | 
| │ ├─ ☑ (Arms)| [ON] | 
| │ ├─ ☑ 손| [ON] | 
| │ ├─ ☑ 다리| [ON] | 
| │ ├─ ☑ 발| [ON] | 
| │ └─ ☑ 플레이어| [ON] | 
| └─ ⚙️ **시뮬레이션 설정**| | 
|  ├─ ☑ 전역 사용| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
|  ├─ ☑ 드래그 활성화| [ON] | 
|  ├─ ☑ 시뮬레이트| [ON] | 
|  ├─ > 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|  ├─ ⊖ 시간 스케일| [0.65] (0.1 ~ 1) | 
|  ├─ ⊖ 서브스텝| [4] (1 ~ 20) | 
|  ├─ ⊖ 반복| [1] (0 ~ 10) | 
|  ├─ □ 짝수 서브스텝 역전| [OFF] | 
|  ├─ ⊖ 대체 그룹 크기| [0] (0 ~ 20) | 
|  ├─ ⊖ 테이블 크기| [6] (1 ~ 20) | 
|  └─ □ 2단계 해결| [OFF] | 
|  ⊖ 스프링| [1.25] (0 ~ 5) | 
|  ⊖ 감쇠| [0.01] (0 ~ 0.1) | 
|  ⊖ 감소 비율| [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
|  ⊖ 비틀림 한계| [5] (0 ~ 180) | 비틀림 회전 한계
|  ⊖ 한계 힘| [3] (0 ~ 8) | 
|  ⊖ 질량| [0.01] (0 ~ 0.1) | 
|  ⊖ 드래그| [1] (0 ~ 10) | 
|  ⊖ 콜라이더 반지름| [0.005] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
|  ⊖ 콜라이더 길이| [0.9] (0 ~ 1) | 
|  ⊖ 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|  ≡ 프리셋| **기본값 (초기화)** | 기본값 (초기화), (momiji bob), (Preset 1),  |
