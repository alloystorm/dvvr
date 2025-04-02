---
locale: ko-rKR
layout: single
title: 설정
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/all_settings) | [繁中](/tw/dancexr/menu/2025.4/actor/all_settings) | [日本語](/jp/dancexr/menu/2025.4/actor/all_settings) | [한국어](/kr/dancexr/menu/2025.4/actor/all_settings) | [简中](/zh/dancexr/menu/2025.4/actor/all_settings)

[액터](../menu#액터) > 설정



| Setting | Value | Description |
| :--- | --- | :--- |
| [얼굴 제어](#얼굴_제어) |
| [비율 및 오프셋](#비율_및_오프셋) |
| [실제와 같은 움직임](#실제와_같은_움직임) |
| [문제 해결](#문제_해결) |
| [물 상호작용](#물_상호작용) |
| [뼈 시각화](#뼈_시각화) |
| [모션 패스](#모션_패스) |


### **얼굴 제어**



| Setting | Value | Description |
| :--- | --- | :--- |
| 입 || 
| 입 모양 동기 사용 | OFF | 
| 눈썹 || 
| 눈꺼풀 || 


### **비율 및 오프셋**

(Allows configuration of the model's scale, ground offset, rotation, and positional offsets. Includes snapping options for precise adjustments.)

| Setting | Value | Description |
| :--- | --- | :--- |
|- 모델 비율 | [0] (-3 ~ 3) | (Adjust the overall scale of the model. Values are exponential for finer control.)
|- 지면 오프셋 | [0] (-2 ~ 2) | (Set the vertical offset of the model relative to the ground.)
| 균일 높이 | ON | (Enable to scale the model to an average human height.)
|- 회전 | [0] (-180 ~ 180) | (Set the rotation of the model in degrees.)
|- 오프셋 X | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the X-axis.)
|- 오프셋 Z | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the Z-axis.)
|- 스냅핑 | **(0)**, (0.1), (0.2), (0.5), (1), (2),  | (Set the snapping increment for drag adjustments. Smaller values allow finer control.)
| 프리셋 | **균일 실물 크기**, 미니어처, 거대, 원본,  |  |


### **실제와 같은 움직임**



| Setting | Value | Description |
| :--- | --- | :--- |
| 아이 콘택트 | ON | 눈 접촉을 활성화하여 시각 범위 내에 있을 때 카메라나 다른 모델 쪽으로 머리를 돌리기
| 응시 모드 | OFF | 가장 가까운 대상으로 지속적으로 바라봄
|- 카메라를 바라보기 | [1] (0 ~ 1) | 응시 대상으로서의 카메라 우선 순위
|- 동료를 바라보기 | [0.5] (0 ~ 1) | 응시 대상으로서의 다른 모델 우선 순위
|- 몸을 바라보기 | [0.5] (0 ~ 1) | 응시 대상으로서의 특정 신체 부위 우선 순위
|- 아이 콘택트 각도 | [80] (0 ~ 180) | 시각 범위의 각도, 이 각도 내의 객체만이 응시 대상이 될 수 있음
|- 아이 콘택트 머리 돌리기 | [0.7] (0 ~ 1) | 대상을 바라볼 때 머리 회전 비율
| 만화 눈 | ON | 눈 회전 감소, 큰 만화 눈을 가진 모델에 유용함
|- 만화 눈 한계 | [0.4] (0 ~ 1) | 만화 눈 모드에서의 회전 감소량
|- 미소 입 | [1] (0 ~ 1) | 
|- 미소 눈썹 | [0.5] (0 ~ 1) | 
| (Random Target) | ON | 
| 눈 깜박임 | ON | 랜덤 간격으로 자동으로 눈 깜박임
| 호흡 | ON | 호흡 모션
|- 호흡 속도 | [0.3] (0 ~ 1) | 
| 미세 움직임 | OFF | 미세 움직임 추가
|- 미세 움직임 범위 | [0.25] (0 ~ 1) | 
|- 미세 움직임 주기 | [3] (1 ~ 10) | 


### **문제 해결**



| Setting | Value | Description |
| :--- | --- | :--- |
| 몸 회전을 중앙에 적용 | OFF | 엉덩이와 몸통의 회전을 중앙 뼈에 적용
| 트위스트 수정 | OFF | 관절에서 팔 및 다리의 비틀림 줄이기
|- 상완 트위스트 | [0] (0 ~ 1) | 
|- 하완 트위스트 | [0] (0 ~ 1) | 
|- 하완 모드 | 상완에서, **손에서**,  | 
|- 다리 트위스트 | [0] (0 ~ 1) | 
|- 팔 트위스트 지우기 | [0] (0 ~ 1) | 
|- 팔꿈치 축 | [0] (-180 ~ 180) | 팔꿈치 관절의 회전 축
| 확산 색상 무시 | OFF | 
|- 손 크기 | [1] (0 ~ 1) | 손의 크기 설정
|- BVH 엄지 움직임 | [0.5] (0 ~ 1) | BVH 동작을 위한 엄지 움직임 줄이기
|- 목 회전 제한 | [0] (0 ~ 1) | 목 뼈의 회전 줄이기
|- 머리 회전 제한 | [0] (0 ~ 1) | 머리 뼈의 회전 줄이기
| 전환 초기화 | OFF | 물리 초기화 시 표준 자세에서 애니메이션 자세로 전환하여 물리 구성 요소가 제대로 안정되도록 합니다.
|- 초기화 중 다리 자세 | [30] (0 ~ 45) | 
| 운동학 업데이트 건너뛰기 | OFF | 애니메이션되지 않은 운동학 뼈를 업데이트하지 않음.


### **물 상호작용**



| Setting | Value | Description |
| :--- | --- | :--- |
| 리플 | OFF | 
|- 강도 | [1] (0 ~ 2) | 
|- 몸체 | [1] (0.1 ~ 2) | 
|- 손 | [0.5] (0.1 ~ 2) | 
|- 발 | [0.5] (0.1 ~ 2) | 
| 물방울 || 
|- 땀방울 | [0] (0 ~ 1) | 
|- 물방울 광채 | [5] (0 ~ 20) | 
|- 물방울 중력 | [3] (0 ~ 10) | 
|- 드래그 | [2.5] (0 ~ 10) | 
|- 금속성 | [0.25] (0 ~ 1) | 
|- 알파 | [0.25] (0 ~ 1) | 
|- 크기 | [0.003] (0 ~ 0.01) | 
|- 지속 시간 | [5] (0 ~ 10) | 
| 땀 충돌 | OFF | 


### **뼈 시각화**



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Visualize Bones) | OFF | 
| 가상 본 | ON | 
| 본 | OFF | 
| IK | OFF | 
| 랙돌 | OFF | 


### **모션 패스**



| Setting | Value | Description |
| :--- | --- | :--- |
| 본 초기화 | ON | 
| 애니메이션 | ON | 
| 오프셋 | ON | 
| IK | ON | 
| 가상 본 | ON | 
| 형상 후 업데이트 | ON | 
| 본 상속 | ON | 
| 변환 후 | ON | 
| 후 IK | ON | 
| 최종 업데이트 | ON | 
