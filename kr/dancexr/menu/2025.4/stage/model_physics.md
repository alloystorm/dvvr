---
locale: ko-rKR
layout: single
title: 물리
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/model_physics) | [简中](/zh/dancexr/menu/2025.4/stage/model_physics)

[무대](../menu#무대) > 물리



| Setting | Value | Description |
| :--- | --- | :--- |
|  □ PMX 물리 비활성화| [OFF] | XPS 도구 사용을 위해 PMX 물리 비활성화
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 제약 감소| [ON] | 보다 부드러운 시뮬레이션을 허용하기 위해 제약을 줄이는 실험적 설정 사용
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 정적 포함| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 정적 배타| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 동적 포함| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 동적 배타| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>선형이동</b>| | Settings for linear movements
| ├─ ☑ 제약| 자동 | 자동, 제한됨, 잠김, 자유, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 0 제한 고정| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최소 스프링 힘| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 제한| [0.05] (0.05 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 튀는 정도| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 접촉 거리| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>각이동</b>| | Settings for angular movements
| ├─ ☑ 제약| 자동 | 자동, 제한됨, 잠김, 자유, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 0 제한 고정| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최소 스프링 힘| [5] (0 ~ 15) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 제한| [90] (3 ~ 90) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 튀는 정도| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 접촉 거리| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.05] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0.15] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>선형운전</b>| | Apply linear drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링 힘| [3] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>각운전</b>| | Apply angular drive
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링 힘| [0.1] (0 ~ 5) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>선형운동</b>| | Settings for linear motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 단단함| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 주 동력| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/>  두 번째 동력| [3] (0 ~ 8) | 
| ├─ ☑ 목표 위치| 제로 | 제로, 센터, 최소, 최대, 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가능할 때 잠금| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가속 모드| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>각운동</b>| | Settings for angular motion
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 단단함| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 주 동력| [5] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/>  두 번째 동력| [5] (0 ~ 8) | 
| ├─ ☑ 목표 위치| 제로 | 제로, 센터, 최소, 최대, 
| ├─ □ 가능할 때 잠금| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가속 모드| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.05] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0.15] (0 ~ 1) | 
| └─ □ (Ignore Limit)| [OFF] | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>옵션</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최소 드래그| [0] (0 ~ 1) | 자동 모드에서의 최소 드래그 값
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그 비율| [1] (0 ~ 5) | 자동 모드에서 드래그 값에 적용되는 비율
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최소 질량| [0] (0 ~ 1) | 자동 모드에서의 최소 질량 값
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 비율| [1] (0 ~ 10) | 자동 모드에서 질량 값에 적용되는 비율
| ├─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 투영 거리| [0.05] (0 ~ 0.1) | 물체 간의 중립상태에 대한 거리 이 값 초과 시 조인트를 강제로 초기화
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 투영 각도| [5] (0 ~ 60) | 물체 간의 중립상태에 대한 각도가 이 값 초과 시 조인트를 강제로 초기화
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 자동 리셋 임계값| [35] (0 ~ 100) | 속도가 이 값을 초과할 때 뼈와 그 자식 뼈를 자동으로 리셋
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>자동 재설정</b>| | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 임계값| [30] (0 ~ 50) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>신체 콜라이더</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 크기| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 머리 반경| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 팔 반경| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 팔뚝| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 가슴 너비| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 허리 너비| [0.5] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 엉덩이 너비| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 엉덩이 반경| [1] (0 ~ 2) | 
| ├─ <b>엉덩이 위치</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.1 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 배 반경| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 배 위치| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 다리 반경| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 허벅지 앞으로/뒤로| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 허벅지 시작 위치| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 손| [0] (0 ~ 1) | 
| ├─ □ 시각화| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (amy), (misaki),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>가슴 물리</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─ 뼈 선택|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링 힘| [1.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력 반대| [10] (0 ~ 45) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>회전 제한</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 상한| [100] (0 ~ 120) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 하한| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 좌측 / 우측 제한| [15] (0 ~ 45) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링 힘| [1.25] (0 ~ 10) | 제한을 초과할 때 스프링 힘
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 접촉 거리| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바운스| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>앵커</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.03] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.03] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.08] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>센터</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.02] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.05] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.025] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌</b>| | 
| │ ├─ □ 팔과 충돌| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.07] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 곡선| [2] (-2 ~ 2) | 천 시뮬레이션과 함께 작동합니다.
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 유두 활성화| [ON] | 천 시뮬레이션과 함께 작동합니다.
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>유두 위치</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.18] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.09] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.2] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 유두 크기| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>(Softbody)</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>조인트</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 깊이| [0.4] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 센터 포함| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 부피 제약| [0.85] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 내부 제약| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 표면 제약| [0.75] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 회전 제약| [0.65] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엣지 잠금| [0.85] (0.5 ~ 1) | 엣지에 입자 잠금.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 센터 잠금| [1] (0.5 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [15] (0 ~ 40) | 
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ ├─ □ 몸체| [OFF] | 
| │ │ ├─ □ 가슴| [OFF] | 
| │ │ ├─ □ 엉덩이| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ ├─ □ 다리| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>시뮬레이션 설정</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 전역 사용| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 드래그 활성화| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 시뮬레이트| [ON] | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 시간 스케일| [0.65] (0.1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 서브스텝| [4] (1 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반복| [1] (0 ~ 10) | 
| │ │ ├─ □ 짝수 서브스텝 역전| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대체 그룹 크기| [0] (0 ~ 20) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 테이블 크기| [6] (1 ~ 20) | 
| │ │ └─ □ 2단계 해결| [OFF] | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **가슴** | 가슴, 엉덩이, 다리, (tina), (预设1), (预设2),  |
| ├─ □ 소프트바디 전용| [OFF] | 물리 조인트를 비활성화하고 소프트바디 입자만 사용합니다.
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>스커트 물리</b><sup>[PRO]</sup>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 입자 역학 사용| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>시뮬레이션 설정</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 전역 사용| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 드래그 활성화| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 시뮬레이트| [ON] | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 시간 스케일| [0.65] (0.1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 서브스텝| [4] (1 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반복| [1] (0 ~ 10) | 
| │ ├─ □ 짝수 서브스텝 역전| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대체 그룹 크기| [0] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 테이블 크기| [6] (1 ~ 20) | 
| │ └─ □ 2단계 해결| [OFF] | 
| ├─ <b>기본 그룹</b>|| 
| ├─ 뼈 선택|| 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ ├─ □ Y 잠금| [OFF] | 
| │ └─ □ Z 잠금| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 추가 그룹| [0] (0 ~ 7) | 
| ├─ □ <b>(Group 2)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 3)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 4)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 5)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 6)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 7)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| ├─ □ <b>(Group 8)</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ 뼈 선택|| 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 정렬| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 폐쇄 루프| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 동역학</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 순응도| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 앵커| [0] (0 ~ 0.5) | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>물리 속성</b>| | Physics properties like mass, drag and friction
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 겹침| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량 분포| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 해결기 반복 횟수| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
| │ │ └─ ☑ 질량 중심| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>부모-자식 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 드라이브| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 드라이브| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.01] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.5] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>측면 조인트</b>| | 
| │ │ ├─ □ 시각화| [OFF] | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선형운전| [5] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 각운전| [0] (0 ~ 10) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드라이브 댐핑| [0.1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [1] (0 ~ 1) | 
| │ │ ├─ □ Y 잠금| [OFF] | 
| │ │ └─ □ Z 잠금| [OFF] | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌체</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 충돌체 유형| **상자** | 상자, 캡슐, 구,  |
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (First Collider Length)| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 기본 그룹 설정 사용| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>헤어 물리</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─ 뼈 선택|| 본 선택
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>입자 동역학</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>시뮬레이션 설정</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 전역 사용| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 드래그 활성화| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 시뮬레이트| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 시간 스케일| [0.65] (0.1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 서브스텝| [4] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반복| [1] (0 ~ 10) | 
| │ <img src="/images/icon/ic_space.png"/>├─ □ 짝수 서브스텝 역전| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대체 그룹 크기| [0] (0 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 테이블 크기| [6] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ 2단계 해결| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링| [1.25] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 비틀림 한계| [5] (0 ~ 180) | 비틀림 회전 한계
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 한계 힘| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.005] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (momiji bob), (Preset 1),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>드리블 물리</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─ 뼈 선택|| 본 선택
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 첫 X 본 건너뛰기| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>입자 동역학</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스윙 순응도| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 트위스트 순응도| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 앵커| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0] (0 ~ 1) | 각 레벨에서 질량 감소
| │ ├─ □ 시각화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 각속도| [2] (0 ~ 4) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 관성| [2] (1 ~ 5) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 만들기| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [1] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [1] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [0] (0 ~ 2) | 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [1] (0 ~ 2) | 수중 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0.25] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 스케일| [0] (-2 ~ 2) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 강도| [1] (0 ~ 2) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 난류 시간 스케일| [0] (-4 ~ 4) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>충돌하기</b>| | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 머리| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 몸체| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 가슴| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 엉덩이| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 손| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 다리| [ON] | 
| │ │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 발| [ON] | 
| │ │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 플레이어| [ON] | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>시뮬레이션 설정</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 전역 사용| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 드래그 활성화| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 시뮬레이트| [ON] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 시간 스케일| [0.65] (0.1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 서브스텝| [4] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반복| [1] (0 ~ 10) | 
| │ <img src="/images/icon/ic_space.png"/>├─ □ 짝수 서브스텝 역전| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대체 그룹 크기| [0] (0 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 테이블 크기| [6] (1 ~ 20) | 
| │ <img src="/images/icon/ic_space.png"/>└─ □ 2단계 해결| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스프링| [0.5] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감소 비율| [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 비틀림 한계| [5] (0 ~ 180) | 비틀림 회전 한계
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 한계 힘| [3] (0 ~ 8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.05] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 드래그| [1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.01] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.9] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 위치| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>객체 분리</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─ 뼈 선택|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 중력| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 질량| [0.1] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 감쇠| [0] (0 ~ 1) | 
| ├─ ☑ 충돌체| 구 | 없음, 구, 캡슐, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 반지름| [0.1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 콜라이더 길이| [0.3] (0 ~ 2) | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화),  |
