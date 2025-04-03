---
locale: ko-rKR
layout: single
title: 물리
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[(Prop)](../menu#(Prop)) > 물리



| Setting | Value | Description |
| :--- | --- | :--- |
| PMX 물리 비활성화 | OFF | XPS 도구 사용을 위해 PMX 물리 비활성화
| 제약 감소 | ON | 보다 부드러운 시뮬레이션을 허용하기 위해 제약을 줄이는 실험적 설정 사용
| **충돌** | | 
| ├&nbsp;정적 포함 | ON | 
| ├&nbsp;정적 배타 | ON | 
| ├&nbsp;동적 포함 | ON | 
| └&nbsp;동적 배타 | ON | 
| **선형이동** | | Settings for linear movements
| ├&nbsp;제약 | 자동 | 자동, 제한됨, 잠김, 자유, 
| ├&nbsp;0 제한 고정 | ON | 
| ├&nbsp;최소 스프링 힘 | [5] (0 ~ 15) | 
| ├&nbsp;최대 제한 | [0.05] (0.05 ~ 0.1) | 
| ├&nbsp;튀는 정도 | [0.5] (0 ~ 1) | 
| ├&nbsp;접촉 거리 | [0.5] (0 ~ 1) | 
| ├&nbsp;감쇠 | [0.05] (0 ~ 1) | 
| └&nbsp;드래그 | [0.15] (0 ~ 1) | 
| **각이동** | | Settings for angular movements
| ├&nbsp;제약 | 자동 | 자동, 제한됨, 잠김, 자유, 
| ├&nbsp;0 제한 고정 | ON | 
| ├&nbsp;최소 스프링 힘 | [5] (0 ~ 15) | 
| ├&nbsp;최대 제한 | [90] (3 ~ 90) | 
| ├&nbsp;튀는 정도 | [0.5] (0 ~ 1) | 
| ├&nbsp;접촉 거리 | [0.5] (0 ~ 1) | 
| ├&nbsp;감쇠 | [0.05] (0 ~ 1) | 
| └&nbsp;드래그 | [0.15] (0 ~ 1) | 
| **선형운전** | | Apply linear drive
| ├&nbsp;활성화 | ON | 
| ├&nbsp;스프링 힘 | [3] (0 ~ 5) | 
| └&nbsp;감쇠 | [0.1] (0 ~ 1) | 
| **각운전** | | Apply angular drive
| ├&nbsp;활성화 | ON | 
| ├&nbsp;스프링 힘 | [0.1] (0 ~ 5) | 
| └&nbsp;감쇠 | [0.1] (0 ~ 1) | 
| **선형운동** | | Settings for linear motion
| ├&nbsp;단단함 | [0] (-1 ~ 1) | 
| ├&nbsp;주 동력 | [5] (0 ~ 8) | 
| ├&nbsp; 두 번째 동력 | [3] (0 ~ 8) | 
| ├&nbsp;목표 위치 | 제로 | 제로, 센터, 최소, 최대, 
| ├&nbsp;가능할 때 잠금 | ON | 
| ├&nbsp;가속 모드 | ON | 
| ├&nbsp;감쇠 | [0.05] (0 ~ 1) | 
| ├&nbsp;드래그 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
| **각운동** | | Settings for angular motion
| ├&nbsp;단단함 | [0] (-1 ~ 1) | 
| ├&nbsp;주 동력 | [5] (0 ~ 8) | 
| ├&nbsp; 두 번째 동력 | [5] (0 ~ 8) | 
| ├&nbsp;목표 위치 | 제로 | 제로, 센터, 최소, 최대, 
| ├&nbsp;가능할 때 잠금 | OFF | 
| ├&nbsp;가속 모드 | ON | 
| ├&nbsp;감쇠 | [0.05] (0 ~ 1) | 
| ├&nbsp;드래그 | [0.15] (0 ~ 1) | 
| └&nbsp;(Ignore Limit) | OFF | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
| **옵션** | | 
| ├&nbsp;최소 드래그 | [0] (0 ~ 1) | 자동 모드에서의 최소 드래그 값
| ├&nbsp;드래그 비율 | [1] (0 ~ 5) | 자동 모드에서 드래그 값에 적용되는 비율
| ├&nbsp;최소 질량 | [0] (0 ~ 1) | 자동 모드에서의 최소 질량 값
| ├&nbsp;질량 비율 | [1] (0 ~ 10) | 자동 모드에서 질량 값에 적용되는 비율
| ├&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| ├&nbsp;투영 거리 | [0.05] (0 ~ 0.1) | 물체 간의 중립상태에 대한 거리 이 값 초과 시 조인트를 강제로 초기화
| └&nbsp;투영 각도 | [5] (0 ~ 60) | 물체 간의 중립상태에 대한 각도가 이 값 초과 시 조인트를 강제로 초기화
| 자동 리셋 임계값 | [35] (0 ~ 100) | 속도가 이 값을 초과할 때 뼈와 그 자식 뼈를 자동으로 리셋
| **자동 재설정** | | 
| └&nbsp;임계값 | [30] (0 ~ 50) | 
| **신체 콜라이더** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;크기 | [0.5] (0 ~ 1) | 
| ├&nbsp;머리 반경 | [1] (0 ~ 2) | 
| ├&nbsp;팔 반경 | [1] (0 ~ 2) | 
| ├&nbsp;팔뚝 | [1] (0 ~ 2) | 
| ├&nbsp;가슴 너비 | [1] (0 ~ 2) | 
| ├&nbsp;허리 너비 | [0.5] (0 ~ 1) | 
| ├&nbsp;엉덩이 너비 | [0] (-1 ~ 1) | 
| ├&nbsp;엉덩이 반경 | [1] (0 ~ 2) | 
| ├&nbsp;엉덩이 위치 || 
| ├&nbsp;(X) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Y) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;(Z) | [0] (-0.1 ~ 0.1) | 
| ├&nbsp;배 반경 | [1] (0 ~ 2) | 
| ├&nbsp;배 위치 | [0] (-1 ~ 1) | 
| ├&nbsp;다리 반경 | [1] (0 ~ 2) | 
| ├&nbsp;허벅지 앞으로/뒤로 | [0] (-1 ~ 1) | 
| ├&nbsp;허벅지 시작 위치 | [0] (0 ~ 1) | 
| ├&nbsp;손 | [0] (0 ~ 1) | 
| ├&nbsp;시각화 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (amy), (misaki),  |
| **가슴 물리**<sup>[PRO]</sup> | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;뼈 선택 || 
| ├&nbsp;스프링 힘 | [1.5] (0 ~ 5) | 
| ├&nbsp;감쇠 | [0.1] (0 ~ 1) | 
| ├&nbsp;질량 | [0.1] (0 ~ 1) | 
| ├&nbsp;드래그 | [0.1] (0 ~ 10) | 
| ├&nbsp;중력 반대 | [10] (0 ~ 45) | 
| ├&nbsp;**회전 제한** | | 
| │&nbsp;├&nbsp;상한 | [100] (0 ~ 120) | 
| │&nbsp;├&nbsp;하한 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;좌측 / 우측 제한 | [15] (0 ~ 45) | 
| │&nbsp;├&nbsp;스프링 힘 | [1.25] (0 ~ 10) | 제한을 초과할 때 스프링 힘
| │&nbsp;├&nbsp;감쇠 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;접촉 거리 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;바운스 | [0.2] (0 ~ 1) | 
| ├&nbsp;**앵커** | | 
| │&nbsp;├&nbsp;(X) | [-0.03] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [0.03] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.08] (-0.2 ~ 0.2) | 
| ├&nbsp;**센터** | | 
| │&nbsp;├&nbsp;(X) | [0.02] (-0.2 ~ 0.2) | 
| │&nbsp;├&nbsp;(Y) | [-0.05] (-0.2 ~ 0.2) | 
| │&nbsp;└&nbsp;(Z) | [0.025] (-0.2 ~ 0.2) | 
| ├&nbsp;**충돌** | | 
| │&nbsp;├&nbsp;팔과 충돌 | OFF | 
| │&nbsp;├&nbsp;콜라이더 반지름 | [0.07] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;콜라이더 길이 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;콜라이더 곡선 | [2] (-2 ~ 2) | 천 시뮬레이션과 함께 작동합니다.
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;유두 활성화 | ON | 천 시뮬레이션과 함께 작동합니다.
| │&nbsp;├&nbsp;**유두 위치** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [-0.18] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.09] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0.2] (0 ~ 1) | 
| │&nbsp;└&nbsp;유두 크기 | [0.1] (0 ~ 1) | 
| ├&nbsp;**(Softbody)** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;조인트 || 
| │&nbsp;├&nbsp;깊이 | [0.4] (0 ~ 1) | 
| │&nbsp;├&nbsp;센터 포함 | ON | 
| │&nbsp;├&nbsp;부피 제약 | [0.85] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;내부 제약 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;표면 제약 | [0.75] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;회전 제약 | [0.65] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;엣지 잠금 | [0.85] (0.5 ~ 1) | 엣지에 입자 잠금.
| │&nbsp;├&nbsp;센터 잠금 | [1] (0.5 ~ 1) | 
| │&nbsp;├&nbsp;감쇠 | [15] (0 ~ 40) | 
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;├&nbsp;바람 영향 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;├&nbsp;몸체 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;가슴 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;엉덩이 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;├&nbsp;다리 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**시뮬레이션 설정** | | 
| │&nbsp;│&nbsp;├&nbsp;전역 사용 | ON | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │&nbsp;│&nbsp;├&nbsp;드래그 활성화 | ON | 
| │&nbsp;│&nbsp;├&nbsp;시뮬레이트 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;│&nbsp;시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │&nbsp;│&nbsp;├&nbsp;시간 스케일 | [0.65] (0.1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;서브스텝 | [4] (1 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;반복 | [1] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;짝수 서브스텝 역전 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;대체 그룹 크기 | [0] (0 ~ 20) | 
| │&nbsp;│&nbsp;├&nbsp;테이블 크기 | [6] (1 ~ 20) | 
| │&nbsp;│&nbsp;└&nbsp;2단계 해결 | OFF | 
| │&nbsp;└&nbsp;(Presets: Boobs) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **가슴** | 가슴, 엉덩이, 다리, (tina), (预设1), (预设2),  |
| ├&nbsp;소프트바디 전용 | OFF | 물리 조인트를 비활성화하고 소프트바디 입자만 사용합니다.
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| **스커트 물리**<sup>[PRO]</sup> | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;입자 역학 사용 | ON | 
| ├&nbsp;**시뮬레이션 설정** | | 
| │&nbsp;├&nbsp;전역 사용 | ON | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │&nbsp;├&nbsp;드래그 활성화 | ON | 
| │&nbsp;├&nbsp;시뮬레이트 | ON | 
| │&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;│&nbsp;시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │&nbsp;├&nbsp;시간 스케일 | [0.65] (0.1 ~ 1) | 
| │&nbsp;├&nbsp;서브스텝 | [4] (1 ~ 20) | 
| │&nbsp;├&nbsp;반복 | [1] (0 ~ 10) | 
| │&nbsp;├&nbsp;짝수 서브스텝 역전 | OFF | 
| │&nbsp;├&nbsp;대체 그룹 크기 | [0] (0 ~ 20) | 
| │&nbsp;├&nbsp;테이블 크기 | [6] (1 ~ 20) | 
| │&nbsp;└&nbsp;2단계 해결 | OFF | 
| ├&nbsp;기본 그룹 || 
| ├&nbsp;뼈 선택 || 
| ├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| ├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| ├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├&nbsp;**입자 동역학** | | 
| │&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| ├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| ├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| ├&nbsp;**측면 조인트** | | 
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;└&nbsp;Z 잠금 | OFF | 
| ├&nbsp;**충돌체** | | 
| │&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| ├&nbsp;추가 그룹 | [0] (0 ~ 7) | 
| ├&nbsp;**(Group 2)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 3)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 4)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 5)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 6)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 7)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| ├&nbsp;**(Group 8)** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;뼈 선택 || 
| │&nbsp;├&nbsp;(Sorting: Shortest Path) || 측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다.
| │&nbsp;│&nbsp;정렬 | **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │&nbsp;├&nbsp;폐쇄 루프 | ON | 각 레벨의 폐쇄 루프에 대한 본들
| │&nbsp;├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │&nbsp;├&nbsp;**입자 동역학** | | 
| │&nbsp;│&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;│&nbsp;├&nbsp;측면 순응도 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;측면 앵커 | [0] (0 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;│&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;│&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;│&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;│&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;│&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;│&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;│&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;│&nbsp;└&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;├&nbsp;**물리 속성** | | Physics properties like mass, drag and friction
| │&nbsp;│&nbsp;├&nbsp;질량 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;드래그 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;수평 겹침 | [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │&nbsp;│&nbsp;├&nbsp;질량 분포 | [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │&nbsp;│&nbsp;├&nbsp;마찰 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수 | [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │&nbsp;│&nbsp;└&nbsp;질량 중심 | 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │&nbsp;├&nbsp;**부모-자식 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;스윙 드라이브 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;트위스트 드라이브 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.01] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │&nbsp;├&nbsp;**측면 조인트** | | 
| │&nbsp;│&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;선형운전 | [5] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;각운전 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;드라이브 댐핑 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;감소 비율 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;Y 잠금 | OFF | 
| │&nbsp;│&nbsp;└&nbsp;Z 잠금 | OFF | 
| │&nbsp;├&nbsp;**충돌체** | | 
| │&nbsp;│&nbsp;├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.1) | 
| │&nbsp;│&nbsp;├&nbsp;(Collider Type: Box) || 
| │&nbsp;│&nbsp;│&nbsp;충돌체 유형 | **상자** | 상자, 캡슐, 구,  |
| │&nbsp;│&nbsp;├&nbsp;콜라이더 길이 | [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;│&nbsp;└&nbsp;(First Collider Length) | [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │&nbsp;└&nbsp;기본 그룹 설정 사용 | ON | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| **헤어 물리** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;뼈 선택 || 본 선택
| ├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├&nbsp;**입자 동역학** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;└&nbsp;**시뮬레이션 설정** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;전역 사용 | ON | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │&nbsp;&nbsp;&nbsp;├&nbsp;드래그 활성화 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이트 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;시간 스케일 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;서브스텝 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;반복 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;짝수 서브스텝 역전 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;대체 그룹 크기 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;테이블 크기 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;2단계 해결 | OFF | 
| ├&nbsp;스프링 | [1.25] (0 ~ 5) | 
| ├&nbsp;감쇠 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;감소 비율 | [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
| ├&nbsp;비틀림 한계 | [5] (0 ~ 180) | 비틀림 회전 한계
| ├&nbsp;한계 힘 | [3] (0 ~ 8) | 
| ├&nbsp;질량 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;드래그 | [1] (0 ~ 10) | 
| ├&nbsp;콜라이더 반지름 | [0.005] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
| ├&nbsp;콜라이더 길이 | [0.9] (0 ~ 1) | 
| ├&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (momiji bob), (Preset 1),  |
| **드리블 물리** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;뼈 선택 || 본 선택
| ├&nbsp;첫 X 본 건너뛰기 | [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├&nbsp;**입자 동역학** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;스윙 순응도 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;트위스트 순응도 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;입자 앵커 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;감소 비율 | [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │&nbsp;├&nbsp;시각화 | OFF | 
| │&nbsp;├&nbsp;최대 각속도 | [2] (0 ~ 4) | 
| │&nbsp;├&nbsp;관성 | [2] (1 ~ 5) | 
| │&nbsp;├&nbsp;부드럽게 만들기 | [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;마찰 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;지면 마찰 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;항력 (공기) | [0] (0 ~ 2) | 공기 저항
| │&nbsp;├&nbsp;항력 (수중) | [1] (0 ~ 2) | 수중 저항
| │&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;├&nbsp;바람 영향 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;난류 스케일 | [0] (-2 ~ 2) | 
| │&nbsp;│&nbsp;├&nbsp;난류 강도 | [1] (0 ~ 2) | 
| │&nbsp;│&nbsp;└&nbsp;난류 시간 스케일 | [0] (-4 ~ 4) | 
| │&nbsp;├&nbsp;**충돌하기** | | 
| │&nbsp;│&nbsp;├&nbsp;머리 | ON | 
| │&nbsp;│&nbsp;├&nbsp;몸체 | ON | 
| │&nbsp;│&nbsp;├&nbsp;가슴 | ON | 
| │&nbsp;│&nbsp;├&nbsp;엉덩이 | ON | 
| │&nbsp;│&nbsp;├&nbsp;(Arms) | ON | 
| │&nbsp;│&nbsp;├&nbsp;손 | ON | 
| │&nbsp;│&nbsp;├&nbsp;다리 | ON | 
| │&nbsp;│&nbsp;├&nbsp;발 | ON | 
| │&nbsp;│&nbsp;└&nbsp;플레이어 | ON | 
| │&nbsp;└&nbsp;**시뮬레이션 설정** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;전역 사용 | ON | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │&nbsp;&nbsp;&nbsp;├&nbsp;드래그 활성화 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이트 | ON | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;시간 스케일 | [0.65] (0.1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;서브스텝 | [4] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;반복 | [1] (0 ~ 10) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;짝수 서브스텝 역전 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;대체 그룹 크기 | [0] (0 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;테이블 크기 | [6] (1 ~ 20) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;2단계 해결 | OFF | 
| ├&nbsp;스프링 | [0.5] (0 ~ 5) | 
| ├&nbsp;감쇠 | [0.01] (0 ~ 0.1) | 
| ├&nbsp;감소 비율 | [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
| ├&nbsp;비틀림 한계 | [5] (0 ~ 180) | 비틀림 회전 한계
| ├&nbsp;한계 힘 | [3] (0 ~ 8) | 
| ├&nbsp;질량 | [0.05] (0 ~ 0.1) | 
| ├&nbsp;드래그 | [1] (0 ~ 10) | 
| ├&nbsp;콜라이더 반지름 | [0.01] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
| ├&nbsp;콜라이더 길이 | [0.9] (0 ~ 1) | 
| ├&nbsp;앵커 위치 | [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2),  |
| **객체 분리** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;뼈 선택 || 
| ├&nbsp;중력 | ON | 
| ├&nbsp;질량 | [0.1] (0 ~ 10) | 
| ├&nbsp;감쇠 | [0] (0 ~ 1) | 
| ├&nbsp;충돌체 | 구 | 없음, 구, 캡슐, 
| ├&nbsp;콜라이더 반지름 | [0.1] (0 ~ 1) | 
| └&nbsp;콜라이더 길이 | [0.3] (0 ~ 2) | 
| (Presets: Default (Reset)) || 
| 프리셋 | **기본값 (초기화)** | 기본값 (초기화),  |
