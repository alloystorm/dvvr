---
locale: ko-rKR
layout: single
title: 응용 프로그램 설정
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/system/application_settings) | [繁中](/tw/dancexr/menu/2025.4/system/application_settings) | [日本語](/jp/dancexr/menu/2025.4/system/application_settings) | [한국어](/kr/dancexr/menu/2025.4/system/application_settings) | [简中](/zh/dancexr/menu/2025.4/system/application_settings)

[시스템](../menu#시스템) > 응용 프로그램 설정



| Setting | Value | Description |
| :--- | --- | :--- |
| 이전 씬 로드 | OFF | 시작 시 마지막 씬 자동 로드
| VR에서 데스크톱 창 차단 | ON | VR 모드에서 데스크톱 창 차단
| 저장된 태그 복구 | OFF | 내용 캐시가 재구성되거나 손상된 경우 저장된 설정에서 태그 복구 시도
| DDS 압축 전환 | ON | 압축된 DDS 텍스처 전환
| DDS 비압축 전환 | OFF | 비압축된 DDS 텍스처 전환
| **VR 손** | | 
| ├&nbsp;손 보이기 | ON | 
| ├&nbsp;그림자 생성 | OFF | 
| ├&nbsp;(Time And FPS) | ON | 
| ├&nbsp;**손 방향** | | 
| │&nbsp;├&nbsp;오프셋 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.1 ~ 0.1) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.1 ~ 0.1) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.1 ~ 0.1) | 
| │&nbsp;├&nbsp;회전 | [45] (-90 ~ 90) | 
| │&nbsp;└&nbsp;포인터 업데이트 || 
| ├&nbsp;(Left Hand Pose: Auto) || 
| │&nbsp;왼손 포즈 | **자동** | 자동, (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 점, (Middle Finger), (Thumb Up), (Grab),  |
| ├&nbsp;**왼손 액세서리** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;(Model: [Pole]) || 
| │&nbsp;│&nbsp;모델 | **[기둥]** | [기둥],  |
| │&nbsp;├&nbsp;**앵커 오프셋** | | Set the anchor position for the attachment to attach to
| │&nbsp;│&nbsp;├&nbsp;위치 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;회전 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-90 ~ 90) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-90 ~ 90) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-90 ~ 90) | 
| │&nbsp;├&nbsp;크기 및 정렬 || 
| │&nbsp;├&nbsp;객체 반경 | [0.02] (0.01 ~ 0.05) | 
| │&nbsp;├&nbsp;객체 길이 | [0.2] (0 ~ 5) | 
| │&nbsp;├&nbsp;스케일 | [0] (-5 ~ 5) | 
| │&nbsp;├&nbsp;방향 | (Y Up) | (Y Up), (Y Down), (X Up), (X Down), (Z Up), (Z Down), 
| │&nbsp;├&nbsp;오프셋 || 
| │&nbsp;├&nbsp;(X) | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;(Y) | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;(Z) | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;회전 || 
| │&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;(Z) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;기타 모드 | OFF | 
| │&nbsp;├&nbsp;**모션** | | Apply up / down motion to the attachment model
| │&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;│&nbsp;├&nbsp;**속도** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;비트당 움직임 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;그룹당 움직임 | [8] (4 ~ 32) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;주기 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;곡선 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;변동 속도 | OFF | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;모드 | (Gradual) | (Gradual), 무작위, 볼륨, 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;최소 속도 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;최대 속도 | (3/2) | (1), (3/2), (2), (3), (4), 
| │&nbsp;│&nbsp;├&nbsp;거리 | [0.1] (0 ~ 0.3) | 
| │&nbsp;│&nbsp;└&nbsp;각도 | [0] (-60 ~ 60) | 
| │&nbsp;├&nbsp;(Animation: None) || 부착 모델에 사용할 로드된 모션 선택
| │&nbsp;│&nbsp;애니메이션 | **없음** | 없음, <br/>부착 모델에 사용할 로드된 모션 선택 |
| │&nbsp;├&nbsp;**표면** | | 
| │&nbsp;│&nbsp;├&nbsp;광택 | [0.9] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;금속성 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;범프 | [0.2] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;발광 | [0] (0 ~ 10) | 
| │&nbsp;│&nbsp;├&nbsp;앰비언트 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;알파 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;클립 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;**색상** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;색상 모드 | (RGB) | (RGB), (HSV), 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;색조 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;채도 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;밝기 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;빨간색 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;초록색 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;파란색 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;(Blend Mode: Blend) || 
| │&nbsp;│&nbsp;│&nbsp;│&nbsp;혼합 모드 | **혼합** | 원본, (Multiply), 혼합, (Color Shift),  |
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;혼합 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;(Presets: White) || 
| │&nbsp;│&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **흰색** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| │&nbsp;│&nbsp;├&nbsp;**툰 셰이더** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;쉐이딩 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;윤곽선 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;스페큘러 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;소프트 스페큘러 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;하이라이트 영역 | [0.25] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;부드러운 하이라이트 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;앰비언트 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;그림자 영역 | [0.65] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;그림자 | [0.75] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;부드러운 그림자 | [0.1] (0 ~ 1) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;│&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| │&nbsp;│&nbsp;├&nbsp;**특수 셰이더** | | 
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;│&nbsp;│&nbsp;모드 | **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| │&nbsp;│&nbsp;│&nbsp;├&nbsp;굴절 | [0.5] (1 ~ 3) | 
| │&nbsp;│&nbsp;│&nbsp;└&nbsp;두께 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Presets: Chrome) || 
| │&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **크롬** | 흰색 광택, 붉은색 광택, 크롬, 검은색 광택, 금색, 단단한 유리, 얇은 유리,  |
| │&nbsp;├&nbsp;X레이 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;알파 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;손을 당기기 | [0.1] (0 ~ 0.5) | 부착물에 가까워지면 손을 부착물 쪽으로 당김
| │&nbsp;├&nbsp;잡기 포즈 | ON | 부착물에 있을 때 자동으로 손 포즈를 잡기 자세로 변경
| │&nbsp;└&nbsp;손 동작 | [0] (-1 ~ 1) | 부착물 모션에 따라 손을 이동
| ├&nbsp;(Right Hand Pose: Auto) || 
| │&nbsp;오른손 포즈 | **자동** | 자동, (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 점, (Middle Finger), (Thumb Up), (Grab),  |
| └&nbsp;**오른손 액세서리** | | 
| &nbsp;&nbsp;├&nbsp;활성화 | OFF | 
| &nbsp;&nbsp;├&nbsp;(Model: [Pole]) || 
| &nbsp;&nbsp;│&nbsp;모델 | **[기둥]** | [기둥],  |
| &nbsp;&nbsp;├&nbsp;**앵커 오프셋** | | Set the anchor position for the attachment to attach to
| &nbsp;&nbsp;│&nbsp;├&nbsp;위치 || 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;회전 || 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(X) | [0] (-90 ~ 90) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-90 ~ 90) | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-90 ~ 90) | 
| &nbsp;&nbsp;├&nbsp;크기 및 정렬 || 
| &nbsp;&nbsp;├&nbsp;객체 반경 | [0.02] (0.01 ~ 0.05) | 
| &nbsp;&nbsp;├&nbsp;객체 길이 | [0.2] (0 ~ 5) | 
| &nbsp;&nbsp;├&nbsp;스케일 | [0] (-5 ~ 5) | 
| &nbsp;&nbsp;├&nbsp;방향 | (Y Up) | (Y Up), (Y Down), (X Up), (X Down), (Z Up), (Z Down), 
| &nbsp;&nbsp;├&nbsp;오프셋 || 
| &nbsp;&nbsp;├&nbsp;(X) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;(Y) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;(Z) | [0] (-2 ~ 2) | 
| &nbsp;&nbsp;├&nbsp;회전 || 
| &nbsp;&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;(Z) | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;기타 모드 | OFF | 
| &nbsp;&nbsp;├&nbsp;**모션** | | Apply up / down motion to the attachment model
| &nbsp;&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;**속도** | | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;비트당 움직임 | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;그룹당 움직임 | [8] (4 ~ 32) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;주기 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;곡선 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;변동 속도 | OFF | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;모드 | (Gradual) | (Gradual), 무작위, 볼륨, 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;최소 속도 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
| &nbsp;&nbsp;│&nbsp;│&nbsp;└&nbsp;최대 속도 | (3/2) | (1), (3/2), (2), (3), (4), 
| &nbsp;&nbsp;│&nbsp;├&nbsp;거리 | [0.1] (0 ~ 0.3) | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;각도 | [0] (-60 ~ 60) | 
| &nbsp;&nbsp;├&nbsp;(Animation: None) || 부착 모델에 사용할 로드된 모션 선택
| &nbsp;&nbsp;│&nbsp;애니메이션 | **없음** | 없음, <br/>부착 모델에 사용할 로드된 모션 선택 |
| &nbsp;&nbsp;├&nbsp;**표면** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;광택 | [0.9] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;금속성 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;범프 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;발광 | [0] (0 ~ 10) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;앰비언트 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;알파 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;클립 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;**색상** | | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;색상 모드 | (RGB) | (RGB), (HSV), 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;색조 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;채도 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;밝기 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;빨간색 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;초록색 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;파란색 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;(Blend Mode: Blend) || 
| &nbsp;&nbsp;│&nbsp;│&nbsp;│&nbsp;혼합 모드 | **혼합** | 원본, (Multiply), 혼합, (Color Shift),  |
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;혼합 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;└&nbsp;(Presets: White) || 
| &nbsp;&nbsp;│&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **흰색** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| &nbsp;&nbsp;│&nbsp;├&nbsp;**툰 셰이더** | | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;쉐이딩 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;윤곽선 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;스페큘러 | [0.25] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;소프트 스페큘러 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;하이라이트 영역 | [0.25] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;부드러운 하이라이트 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;앰비언트 | [0.75] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;그림자 영역 | [0.65] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;그림자 | [0.75] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;부드러운 그림자 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;└&nbsp;(Presets: Sharp) || 
| &nbsp;&nbsp;│&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| &nbsp;&nbsp;│&nbsp;├&nbsp;**특수 셰이더** | | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;(Mode: Off) || 
| &nbsp;&nbsp;│&nbsp;│&nbsp;│&nbsp;모드 | **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| &nbsp;&nbsp;│&nbsp;│&nbsp;├&nbsp;굴절 | [0.5] (1 ~ 3) | 
| &nbsp;&nbsp;│&nbsp;│&nbsp;└&nbsp;두께 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;(Presets: Chrome) || 
| &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;프리셋 | **크롬** | 흰색 광택, 붉은색 광택, 크롬, 검은색 광택, 금색, 단단한 유리, 얇은 유리,  |
| &nbsp;&nbsp;├&nbsp;X레이 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;알파 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;손을 당기기 | [0.1] (0 ~ 0.5) | 부착물에 가까워지면 손을 부착물 쪽으로 당김
| &nbsp;&nbsp;├&nbsp;잡기 포즈 | ON | 부착물에 있을 때 자동으로 손 포즈를 잡기 자세로 변경
| &nbsp;&nbsp;└&nbsp;손 동작 | [0] (-1 ~ 1) | 부착물 모션에 따라 손을 이동
| (Gizmo 3rd Axis: Rotation) || 
| 기즈모 3차 축 | **회전** | 회전, 깊이,  |
| 번역된 이름 사용 | ON | 
