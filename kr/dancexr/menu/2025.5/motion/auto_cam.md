---
locale: ko-rKR
layout: single
title: [자동 카메라]
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.5/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.5/motion/auto_cam)

[프로시저](../menu#프로시저) > [자동 카메라]

(
## Overview
The Automatic Camera Motion System (AutoCam) is a dynamic camera control solution designed to enhance visual storytelling by synchronizing camera movements with music beats, actor orientation, and configurable parameters.

## Key Features
- Dynamic adjustment of camera motion based on music beats.
- Configurable parameters for distance, target selection, and motion paths.
- Support for actor orientation alignment.
- Randomized camera motion generation with seed control.
- Fade-to-black transitions with adjustable duration and probability.
- Audio sensitivity for motion responsiveness to sound levels.

## Use Cases
- Creating cinematic sequences in real-time.
- Enhancing the visual appeal of dance or music-based performances.
- Automating camera control for interactive applications or games.)

## 구성

| 설정 | 값 | 설명 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 메인에 할당 || 
| > 타겟 선택 | **자동** | 자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 센터,  |
| > 트래킹 모드 | **중심** | 중심, 머리, 가슴,  |
| ⊖ 타겟 스무딩 | [0.5] (0 ~ 2) | 
| ⊖ 예측 | [1] (0 ~ 2) | 스무딩으로 인한 지연을 줄이기 위해 타겟 위치 예측
| ⊖ FOV | [30] (5 ~ 120) | 
| ⊖ 비트 사이클 | [8] (1 ~ 16) | 
| ⊖ 거리 근접 | [1.5] (0.5 ~ 3) | 카메라가 타겟에서 최소 거리.
| ⊖ 거리 원거리 | [2.5] (0.5 ~ 3) | 카메라가 타겟에서 최대 거리.
| ☑ 액터 방향 사용 | [ON] | 카메라를 액터 방향에 맞추기 활성화 또는 비활성화.
| ⊖ 시드 | [1234] ((Unlimited)) | 무작위 카메라 움직임 생성을 위한 시드 값.
| ⊖ 검은색으로 페이드 | [0] (0 ~ 0.25) | 전환 중 페이드 투 블랙 효과 지속 시간.
| ⊖ 페이드 투 블랙 확률 | [0.5] (0 ~ 1) | 페이드 투 블랙 효과 발동 확률.
| ☐ 오디오 감도 | [1] (0 ~ 4) | 카메라 움직임의 오디오 레벨 민감도.
|  **타겟 선택** || 
| ⊖ 머리 | [1] (0 ~ 1) | 액터 머리 타겟팅 확률.
| ⊖ 가슴 | [1] (0 ~ 1) | 액터 가슴 타겟팅 확률.
| ⊖ 중심 | [1] (0 ~ 1) | 액터 중앙 타겟팅 확률.
| ⊖ 다리 | [0.5] (0 ~ 1) | 액터 다리 타겟팅 확률.
| ⊖ 발 | [0] (0 ~ 1) | 액터 발 타겟팅 확률.
|  **거리 선택** || 
| ⊖ 클로즈업 | [1] (0 ~ 1) | 클로즈업 카메라 거리 확률.
| ⊖ 줌 인 | [0.25] (0 ~ 1) | 줌 인 확률.
| ⊖ 줌 아웃 | [0.25] (0 ~ 1) | 줌 아웃 확률.
| ⊖ 중간 | [0.25] (0 ~ 1) | 중간 거리 카메라 확률.
| ⊖ 멀리 | [0.25] (0 ~ 1) | 원거리 카메라 확률.
|  **경로 선택** || 
| ⊖ 높은 각도 | [20] (0 ~ 30) | 카메라의 최대 상향 각도.
| ⊖ 낮은 각도 | [-20] (-30 ~ 0) | 카메라의 최대 하향 각도.
|  **방향** || 
| ⊖ 정면 중앙 | [1] (0 ~ 1) | 액터 앞 중앙 방향으로 카메라를 맞출 확률.
| ⊖ 전면 45도 | [0] (0 ~ 1) | 액터 앞 45도 방향으로 카메라를 맞출 확률.
| ⊖ 측면 90도 | [0.25] (0 ~ 1) | 액터 측면 90도 방향으로 카메라를 맞출 확률.
| ⊖ 후면 135도 | [0] (0 ~ 1) | 액터 뒤 135도 방향으로 카메라를 맞출 확률.
| ⊖ 후면 180도 | [0.25] (0 ~ 1) | 액터 뒤쪽 정면으로 카메라를 맞출 확률.
| ≡ 프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1),  |
