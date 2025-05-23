---
locale: ko-rKR
layout: single
title: 재생 옵션
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.5/motion/motion_loader) | [繁中](/tw/dancexr/menu/2025.5/motion/motion_loader) | [日本語](/jp/dancexr/menu/2025.5/motion/motion_loader) | [한국어](/kr/dancexr/menu/2025.5/motion/motion_loader) | [简中](/zh/dancexr/menu/2025.5/motion/motion_loader)

[오디오 / 모션](../menu#오디오 / 모션) > 재생 옵션

## 구성

| 설정 | 값 | 설명 |
| :--- | --- | :--- |
| ☐ 배우 자동 로드 | [OFF] | 모션 트랙 수에 맞춰 배우를 자동으로 로드하고 각 배우에게 다른 모션을 할당
| ☐ 카메라 자동 할당 | [OFF] | 가능하면 카메라 모션을 자동 할당
| > 재생 모드 | **한 번 리스트** | 한 번 리스트, 단일, 리스트 반복, 단일 반복, 셔플,  |
| > 리믹스 모드 | **동기화** | 다음 계속, 동기화, 반복, 다음 셔플,  |
| ⊖ 속도 | [1] (0.5 ~ 2) | 오디오 속도 변경. 이 설정은 모션과 물리 속도에도 영향을 미침
| ☑ 피치 쉬프트 | [ON] | 속도 변경 후 원래 피치와 맞도록 오디오 조정
| > 자동 동기화 모드 | **끔** | 끔, 오디오 이동, 모션 이동,  |
| ⊖ 자동 동기화 임계값 | [0.05] (0 ~ 0.2) | 모션과 오디오의 시간 차이가 이 값을 초과하면 자동으로 동기화
| ☑ 타임라인 미세 조정 | [ON] | 타임라인에서 길게 눌러 재생 시간을 미세하게 조정
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **기본 타이밍** | | 
| ├─⊖ 오프셋 | [0] ((Unlimited)) | 
| ├─⊖ BPM | [120] (1 ~ 240) | 분당 비트 수
| ├─⊖ 비트 옵셋 | [0] (0 ~ 1) | 
| ├─⊖ 구문 당 비트 수 | [8] (4 ~ 64) | 
| ├─⊖ 구문 시작 | [0] (0 ~ 32) | 
| ├─ 자동 BPM 복사 || 자동으로 감지된 값으로 BPM 설정
| └─ 탭 비트 || 음악 재생 중에 탭하여 BPM 설정
| ☑ **오디오 분석** | | 
| ├─☑ 활성화 | [ON] | 
| ├─⊖ 처리율 | [45] (1 ~ 90) | 오디오 처리 비율. 시스템이 고정된 속도로만 오디오 데이터를 업데이트하므로 보통 45 FPS 이상으로 설정할 필요 없음
| ├─⊖ 밴드 선택 | [0] (0 ~ 1) | 음량 레벨 계산을 위한 밴드 범위 선택
| ├─⊖ 부드럽게 | [0.25] (0 ~ 1) | 음량 값 부드럽게 출력
| └─⊖ 페이드 인/아웃 | [0] (0 ~ 0.2) | 오디오 시작과 끝에서 오디오 레벨 페이드 인 및 아웃
| ☐ **립 싱크** | | 
| ├─☐ 활성화 | [OFF] | 
| └─⊖ 립 싱크 부드럽게 | [0.05] (0 ~ 0.1) | 
| ☐ **공간화** | | 
| ├─☐ 활성화 | [OFF] | 
| ├─⊖ 공간 혼합 | [0] (0 ~ 1) | 3D 공간 오디오 효과 혼합
| ├─☐ 액터 따라가기 | [OFF] | 
| └─> 액터 선택 |  |  |
