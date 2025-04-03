---
locale: ko-rKR
layout: single
title: [오토 캠]
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[프로시저](../menu#프로시저) > [오토 캠]



| Setting | Value | Description |
| :--- | --- | :--- |
| 메인에 할당 || 
| (Target Select: Auto) || 
| 타겟 선택 | **자동** | 자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 중앙,  |
| (Tracking Mode: Center) || 
| 트래킹 모드 | **센터** | 센터, 머리, 가슴,  |
| 타겟 부드럽게 만들기 | [0.5] (0 ~ 2) | 
| 예측 | [1] (0 ~ 2) | 부드러움으로 인한 지연을 줄이기 위해 타겟의 위치를 예측
| FOV | [30] (5 ~ 120) | 
| 비트 사이클 | [8] (1 ~ 16) | 
| 근거리 | [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
| 원거리 | [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
| 배우 방향 사용 | ON | (Enable or disable alignment of the camera to the actor's orientation.)
| 시드 | [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
| 검은색으로 페이드 | [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
| F2B 확률 | [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
| 오디오 민감도 | [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
| 대상 선택 || 
| 머리 | [1] (0 ~ 1) | (Probability of targeting the actor's head.)
| 가슴 | [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
| 센터 | [1] (0 ~ 1) | (Probability of targeting the actor's center.)
| 다리 | [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
| 발 | [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
| 거리 선택 || 
| 클로즈 업 | [1] (0 ~ 1) | (Probability of a close-up camera distance.)
| 줌 인 | [0.25] (0 ~ 1) | (Probability of zooming in.)
| 줌 아웃 | [0.25] (0 ~ 1) | (Probability of zooming out.)
| 중간 | [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
| 멀리 | [0.25] (0 ~ 1) | (Probability of a far camera distance.)
| 경로 선택 || 
| 높은 각도 | [20] (0 ~ 30) | (Maximum upward angle for the camera.)
| 낮은 각도 | [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
| 방향 || 
| 앞 중앙 | [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
| 앞 45도 | [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
| 측면 90도 | [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
| 뒤 135도 | [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
| 뒤 180도 | [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
| (Presets: Default (Reset)) || 
| 프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1),  |
