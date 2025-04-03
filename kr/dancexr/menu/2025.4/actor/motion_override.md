---
locale: ko-rKR
layout: single
title: 모션 오버라이드
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[프로](../menu#프로) > 모션 오버라이드



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Motion Override) | OFF | 0/8/True
| **몸체** | | 1/8/True
| ├ 위치 | 자유 | 자유, 수평 고정, 수직 고정, 위치 고정, 0/13/False
| ├ 회전 | 자유 | 자유, 회전 고정, 1/13/False
| ├ 감쇠 | [0.5] (0 ~ 1) | 2/13/False
| ├ 기울기 | [0] (-45 ~ 90) | 3/13/False
| ├ 구부리기 | [0] (-150 ~ 150) | 4/13/False
| ├ 비틀기 | [0] (-90 ~ 90) | 5/13/False
| ├ 머리 | [0] (-90 ~ 90) | 6/13/False
| ├ 높이 | [0] (-1 ~ 1) | 7/13/False
| ├ 앞으로 / 뒤로 | [0] (-1 ~ 1) | 8/13/False
| ├ 거리 | OFF | 9/13/False
| ├ 대상 액터 || 10/13/False
| │ 대상 액터 |  |  |
| ├ 탐지 범위 | [2] (0 ~ 10) | 11/13/False
| ├ 최소 거리 | [0.5] (0 ~ 1) | 12/13/False
| └ 최대 거리 | [1] (0.5 ~ 2) | 13/13/False
| **흔드는 모션** | | 2/8/True
| ├ (Enable Rocking Motion) | ON | 0/8/False
| ├ **속도** | | 1/8/False
| │ ├ 비트당 움직임 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ ├ 그룹당 움직임 | [8] (4 ~ 32) | 1/7/False
| │ ├ 주기 | [0] (0 ~ 1) | 2/7/False
| │ ├ 곡선 | [0] (0 ~ 1) | 3/7/False
| │ ├ 변동 속도 | OFF | 4/7/False
| │ ├ 모드 | (Gradual) | (Gradual), 무작위, 볼륨, 5/7/False
| │ ├ 최소 속도 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ └ 최대 속도 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| ├ 흔드는 각도 | [30] (0 ~ 60) | 2/8/False
| ├ 위 / 아래 | [0.1] (0 ~ 0.3) | 3/8/False
| ├ 앞 / 뒤 | [0.1] (0 ~ 0.3) | 4/8/False
| ├ 깊이 변화 | [0.1] (0 ~ 0.3) | 5/8/False
| ├ 최대 깊이 | [0.15] (0 ~ 0.3) | 6/8/False
| ├ 깊이 추가 | [0] (-0.1 ~ 0.1) | 7/8/False
| └ 발 모션 | [0] (-1 ~ 1) | 8/8/False
| **헤드 포즈** | | 3/8/True
| ├ (Enable Head Pose) | OFF | 0/3/False
| ├ X 회전 | [0] (-90 ~ 90) | 1/3/False
| ├ Y 회전 | [0] (-90 ~ 90) | 2/3/False
| └ Z 회전 | [0] (-90 ~ 90) | 3/3/False
| **다리 포즈** | | 4/8/True
| ├ (Enable Leg Pose) | ON | 0/5/True
| ├ 바닥에 대한 상대적 위치 | ON | 1/5/True
| ├ 최대 비틀림 | [60] (0 ~ 90) | 2/5/True
| ├ 대칭적 | ON | 3/5/True
| ├ **왼쪽** | | 4/5/True
| │ ├ 열기 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 발 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 발 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 발 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 발 회전 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 발 회전 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 발 회전 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 발가락 | [0] (-180 ~ 180) | 7/7/False
| ├ **오른쪽** | | 5/5/True
| │ ├ 열기 | [0] (-90 ~ 90) | 0/7/False
| │ ├ 발 X | [0] ((Unlimited)) | 1/7/False
| │ ├ 발 Y | [0] ((Unlimited)) | 2/7/False
| │ ├ 발 Z | [0] ((Unlimited)) | 3/7/False
| │ ├ 발 회전 X | [0] ((Unlimited)) | 4/7/False
| │ ├ 발 회전 Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 발 회전 Z | [0] ((Unlimited)) | 6/7/False
| │ └ 발가락 | [0] (-180 ~ 180) | 7/7/False
| └ 프리셋 | **(Ride)** | (Sit), (Ride), (Kneel), (Stand),  |
| 손 대칭 | ON | 5/8/True
| **왼손** | | 6/8/True
| ├ (Enable Left Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 제스처 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 점, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **손 위치** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **손 회전** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 회전 유형 | 참조 본에 상대적인 | 참조 본에 상대적인, 자기 자신에 상대적인, 절대 회전, 회전 없음, 4/19/True
| ├ 팔꿈치 방향 | [0] (-180 ~ 180) | 5/19/True
| ├ 좌우 반전 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 참조 배우 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 참조 본 | **없음** | 없음, 엉덩이, 가슴, 머리, 센터, 폴, (Upperarm), (Forearm), 손, 다리, 무릎, 발, 배, 가슴, (Pussy), (Dick),  |
| ├ IK 모드 | 자동 | 자동, 보통, (Cylinder), 구, (Align), 9/19/True
| ├ 측면 선택 | 자동 | 자동, 왼쪽, 오른쪽, 10/19/True
| ├ 혼합 범위 | [0.75] (0 ~ 2) | 11/19/True
| ├ 대칭 오프셋 | [0] (-1 ~ 1) | 12/19/True
| ├ 액세서리 위치 사용 | ON | 13/19/True
| ├ **모션** | | 14/19/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **속도** | | 1/3/False
| │ │ ├ 비트당 움직임 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 그룹당 움직임 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 주기 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 곡선 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 변동 속도 | OFF | 4/7/False
| │ │ ├ 모드 | (Gradual) | (Gradual), 무작위, 볼륨, 5/7/False
| │ │ ├ 최소 속도 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 최대 속도 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 거리 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 각도 | [0] (-60 ~ 60) | 3/3/False
| ├ **사용자 정의 포즈** | | 15/19/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 열기 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 엄지 축 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 엄지 접기 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 엄지 구부리기 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 검지 구부리기 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 중지 구부리기 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 약지 구부리기 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 새끼손가락 구부리기 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 전파 | [1] (0 ~ 1) | 9/10/False
| │ └ 혼합 | [1] (0 ~ 1) | 10/10/False
| ├ 포즈 가중치 | [1] (0 ~ 1) | 16/19/True
| ├ 잡기 거리 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 잡기 위치 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 프리셋 | **(Rest)** | (Rest), 뒷면, 앞면, 엉덩이, 머리, 폴, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **오른손** | | 7/8/True
| ├ (Enable Right Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ 제스처 | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 점, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **손 위치** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **손 회전** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 회전 유형 | 참조 본에 상대적인 | 참조 본에 상대적인, 자기 자신에 상대적인, 절대 회전, 회전 없음, 4/19/True
| ├ 팔꿈치 방향 | [0] (-180 ~ 180) | 5/19/True
| ├ 좌우 반전 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 참조 배우 | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 참조 본 | **없음** | 없음, 엉덩이, 가슴, 머리, 센터, 폴, (Upperarm), (Forearm), 손, 다리, 무릎, 발, 배, 가슴, (Pussy), (Dick),  |
| ├ IK 모드 | 자동 | 자동, 보통, (Cylinder), 구, (Align), 9/19/True
| ├ 측면 선택 | 자동 | 자동, 왼쪽, 오른쪽, 10/19/True
| ├ 혼합 범위 | [0.75] (0 ~ 2) | 11/19/True
| ├ 대칭 오프셋 | [0] (-1 ~ 1) | 12/19/True
| ├ 액세서리 위치 사용 | ON | 13/19/True
| ├ **모션** | | 14/19/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **속도** | | 1/3/False
| │ │ ├ 비트당 움직임 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ 그룹당 움직임 | [8] (4 ~ 32) | 1/7/False
| │ │ ├ 주기 | [0] (0 ~ 1) | 2/7/False
| │ │ ├ 곡선 | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 변동 속도 | OFF | 4/7/False
| │ │ ├ 모드 | (Gradual) | (Gradual), 무작위, 볼륨, 5/7/False
| │ │ ├ 최소 속도 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 최대 속도 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 거리 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 각도 | [0] (-60 ~ 60) | 3/3/False
| ├ **사용자 정의 포즈** | | 15/19/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 열기 | [0] (-1 ~ 1) | 1/10/False
| │ ├ 엄지 축 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 엄지 접기 | [0] (-1 ~ 1) | 3/10/False
| │ ├ 엄지 구부리기 | [0] (-1 ~ 1) | 4/10/False
| │ ├ 검지 구부리기 | [0] (-1 ~ 1) | 5/10/False
| │ ├ 중지 구부리기 | [0] (-1 ~ 1) | 6/10/False
| │ ├ 약지 구부리기 | [0] (-1 ~ 1) | 7/10/False
| │ ├ 새끼손가락 구부리기 | [0] (-1 ~ 1) | 8/10/False
| │ ├ 전파 | [1] (0 ~ 1) | 9/10/False
| │ └ 혼합 | [1] (0 ~ 1) | 10/10/False
| ├ 포즈 가중치 | [1] (0 ~ 1) | 16/19/True
| ├ 잡기 거리 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ 잡기 위치 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ 프리셋 | **(Rest)** | (Rest), 뒷면, 앞면, 엉덩이, 머리, 폴, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **탑승 모델** | | 8/8/True
| ├ (Enable Ride Model) | ON | 0/14/False
| ├ (Model: [Hoverbike]) || 1/14/False
| │ 모델 | **([Hoverbike])** | ([Hoverbike]), ([Rocking Horse]),  |
| ├ 가속 | [10] (0 ~ 20) | 2/14/False
| ├ 드래그 | [0.05] (0 ~ 1) | 3/14/False
| ├ 회전 시 기울기 | [0.5] (0 ~ 1) | 4/14/False
| ├ 위치 || 5/14/False
| ├ (X) | [0] (-1 ~ 1) | 6/14/False
| ├ (Y) | [0] (-1 ~ 1) | 7/14/False
| ├ (Z) | [0] (-1 ~ 1) | 8/14/False
| ├ 회전 || 9/14/False
| ├ (X) | [0] (-90 ~ 90) | 10/14/False
| ├ (Y) | [0] (-90 ~ 90) | 11/14/False
| ├ (Z) | [0] (-90 ~ 90) | 12/14/False
| ├ 스케일 | [0] (-5 ~ 5) | 13/14/False
| └ 파티클 이펙트 | ON | 14/14/False
| 프리셋 | **자유** | 자유, 흔드는 모션, 호버바이크, 흔들말, 폴 모션, 폴 블렌드,  |
