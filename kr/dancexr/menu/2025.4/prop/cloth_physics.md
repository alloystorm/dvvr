---
locale: ko-rKR
layout: single
title: 드리블 물리
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/prop/cloth_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/cloth_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/cloth_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/cloth_physics) | [简中](/zh/dancexr/menu/2025.4/prop/cloth_physics)

[(Prop)](../menu#(Prop)) > 드리블 물리



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Dangling Physics) | ON | 0/13/True
| 뼈 선택 || 본 선택1/13/True
| 첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음2/13/True
| **입자 동역학** | | 3/13/True
| ├ (Enable Particle Dynamics) | ON | 0/18/False
| ├ 스윙 순응도 | [0.25] (0 ~ 1) | 1/18/False
| ├ 트위스트 순응도 | [0.75] (0 ~ 1) | 2/18/False
| ├ 입자 앵커 | [0.5] (0 ~ 1) | 3/18/False
| ├ 감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소4/18/False
| ├ 시각화 | OFF | 5/18/False
| ├ 최대 각속도 | [2] (0 ~ 4) | 6/18/False
| ├ 관성 | [2] (1 ~ 5) | 7/18/False
| ├ 부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.8/18/False
| ├ 입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기9/18/False
| ├ 중력 | [9.8] (-9.8 ~ 9.8) | 10/18/False
| ├ 마찰 | [1] (0 ~ 2) | 11/18/False
| ├ 지면 마찰 | [1] (-2 ~ 2) | 12/18/False
| ├ 항력 (공기) | [0] (0 ~ 2) | 공기 저항13/18/False
| ├ 항력 (수중) | [1] (0 ~ 2) | 수중 저항14/18/False
| ├ 부력 | [-0.1] (-1 ~ 1) | 15/18/False
| ├ **바람** | | 16/18/False
| │ ├ 바람 영향 | [0.25] (0 ~ 1) | 0/3/False
| │ ├ 난류 스케일 | [0] (-2 ~ 2) | 1/3/False
| │ ├ 난류 강도 | [1] (0 ~ 2) | 2/3/False
| │ └ 난류 시간 스케일 | [0] (-4 ~ 4) | 3/3/False
| ├ **충돌하기** | | 17/18/False
| │ ├ 머리 | ON | 0/8/False
| │ ├ 몸체 | ON | 1/8/False
| │ ├ 가슴 | ON | 2/8/False
| │ ├ 엉덩이 | ON | 3/8/False
| │ ├ (Arms) | ON | 4/8/False
| │ ├ 손 | ON | 5/8/False
| │ ├ 다리 | ON | 6/8/False
| │ ├ 발 | ON | 7/8/False
| │ └ 플레이어 | ON | 8/8/False
| └ **시뮬레이션 설정** | | 18/18/False
|   ├ 전역 사용 | ON | Pro / Cloth Simulation 아래에서 전역 설정 찾기0/10/False
|   ├ 드래그 활성화 | ON | 1/10/False
|   ├ 시뮬레이트 | ON | 2/10/False
|   ├ (Simulation FPS: Dynamic) || 3/10/False
|   │ 시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|   ├ 시간 스케일 | [0.65] (0.1 ~ 1) | 4/10/False
|   ├ 서브스텝 | [4] (1 ~ 20) | 5/10/False
|   ├ 반복 | [1] (0 ~ 10) | 6/10/False
|   ├ 짝수 서브스텝 역전 | OFF | 7/10/False
|   ├ 대체 그룹 크기 | [0] (0 ~ 20) | 8/10/False
|   ├ 테이블 크기 | [6] (1 ~ 20) | 9/10/False
|   └ 2단계 해결 | OFF | 10/10/False
| 스프링 | [0.5] (0 ~ 5) | 4/13/True
| 감쇠 | [0.01] (0 ~ 0.1) | 5/13/True
| 감소 비율 | [0.25] (0 ~ 1) | 각 레벨에서 강성 감소6/13/True
| 비틀림 한계 | [5] (0 ~ 180) | 비틀림 회전 한계7/13/True
| 한계 힘 | [3] (0 ~ 8) | 8/13/True
| 질량 | [0.05] (0 ~ 0.1) | 9/13/True
| 드래그 | [1] (0 ~ 10) | 10/13/True
| 콜라이더 반지름 | [0.01] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기11/13/True
| 콜라이더 길이 | [0.9] (0 ~ 1) | 12/13/True
| 앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커13/13/True
| 프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2),  |
