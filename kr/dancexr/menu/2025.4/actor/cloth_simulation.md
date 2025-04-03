---
locale: ko-rKR
layout: single
title: 시뮬레이션
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[프로](../menu#프로) > 시뮬레이션



| Setting | Value | Description |
| :--- | --- | :--- |
| 활성화 | ON | 
| 초기화 || 
| **옷 1** | | 
| ├&nbsp;활성화 | OFF | 
| ├&nbsp;메시 재구성 || 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;토폴로지 | **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
| ├&nbsp;끈 연결 | [4] (1 ~ 10) | 
| ├&nbsp;내부 반경 | [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
| ├&nbsp;경사 | [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
| ├&nbsp;호 | [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
| ├&nbsp;길이 | [0.25] (0 ~ 0.75) | 길이(미터)
| ├&nbsp;팔 구멍 | [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
| ├&nbsp;뒤쪽 길이 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;측면 길이 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;수평 해상도 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;수직 해상도 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;거리 제약 준수 | [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV 매핑 | **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
| ├&nbsp;**앵커** | | 
| │&nbsp;├&nbsp;상단 레이어 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**상단 앵커** | | 
| │&nbsp;│&nbsp;├&nbsp;앵커 선택 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;선택 오프셋 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;앵커 본 | **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;잠금 모드 | **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │&nbsp;│&nbsp;├&nbsp;앵커 위치 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;앵커 회전 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;하단 레이어 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**하단 앵커** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 선택 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;선택 오프셋 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;앵커 본 | **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;측면 바꾸기 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;잠금 모드 | **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 위치 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 회전 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**입자 속성** | | 
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;끈적임 | [0] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;구부림 제한 활성화 | ON | 
| │&nbsp;├&nbsp;구부림 순응 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;스케일 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;자기 충돌 | OFF | 
| │&nbsp;├&nbsp;그립 질량 | [2] (0 ~ 4) | 그립 입자의 질량
| │&nbsp;├&nbsp;그립 마찰 | [2] (-2 ~ 4) | 그립 입자에 대한 마찰
| │&nbsp;├&nbsp;그립 끈적임 | [0.25] (0 ~ 1) | 그립 입자의 끈적임
| │&nbsp;├&nbsp;그립 항력 | [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
| │&nbsp;├&nbsp;그립 스케일 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;찢어짐 활성화 | OFF | 
| │&nbsp;├&nbsp;찢어짐 임계값 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;찢어짐 속도 제한 | [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
| └&nbsp;(Presets: Top) || 
| &nbsp;&nbsp;프리셋 | **(Top)** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C1 재질** | | 
| ├&nbsp;표면 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;프리셋 | **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;유리 모드 | OFF | 
| ├&nbsp;알파를 광택으로 사용 | OFF | 
| ├&nbsp;양면 | ON | 
| ├&nbsp;어두운 배경 | [1] (0 ~ 1) | 
| ├&nbsp;그림자 생성 | [0.5] (0 ~ 1) | 
| ├&nbsp;깊이 사전 패스 | [0.8] (0 ~ 1) | 
| ├&nbsp;광택 | [0.3] (0 ~ 1) | 
| ├&nbsp;금속성 | [0] (0 ~ 1) | 
| ├&nbsp;범프 | [0.2] (0 ~ 1) | 
| ├&nbsp;발광 | [0] (0 ~ 10) | 
| ├&nbsp;앰비언트 | [1] (0 ~ 1) | 
| ├&nbsp;알파 | [1] (0 ~ 1) | 
| ├&nbsp;클립 | [0] (0 ~ 1) | 
| ├&nbsp;**색상** | | 
| │&nbsp;├&nbsp;색상 모드 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;색조 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;채도 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;밝기 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;빨간색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;초록색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;파란색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;혼합 모드 | **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
| │&nbsp;├&nbsp;혼합 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| ├&nbsp;**툰 셰이더** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;쉐이딩 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;윤곽선 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;스페큘러 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;소프트 스페큘러 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;하이라이트 영역 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;부드러운 하이라이트 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;앰비언트 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;그림자 영역 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;그림자 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;부드러운 그림자 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| ├&nbsp;**특수 셰이더** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;모드 | **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| │&nbsp;├&nbsp;굴절 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;두께 | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;텍스처 | **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
| └&nbsp;**디테일 맵** | | 
| &nbsp;&nbsp;├&nbsp;활성화 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;밀도 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;크기 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;범프 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;노이즈 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;부드러운 모서리 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;맵 선택 | **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
| &nbsp;&nbsp;├&nbsp;디테일 맵 회전 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;디테일 맵 크기 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;디테일 맵 범프 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;AO에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;부드러움에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;금속성에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;컬러 혼합에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;비등방성 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP 맵 바이어스 | [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
| **옷 2** | | 
| ├&nbsp;활성화 | OFF | 
| ├&nbsp;메시 재구성 || 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
| ├&nbsp;(Topology: Horizontal Layout) || 
| │&nbsp;토폴로지 | **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
| ├&nbsp;끈 연결 | [4] (1 ~ 10) | 
| ├&nbsp;내부 반경 | [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
| ├&nbsp;경사 | [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
| ├&nbsp;호 | [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
| ├&nbsp;길이 | [0.25] (0 ~ 0.75) | 길이(미터)
| ├&nbsp;팔 구멍 | [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
| ├&nbsp;(Arm Hole Height) | [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
| ├&nbsp;뒤쪽 길이 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;측면 길이 | [1] (0.1 ~ 1.9) | 
| ├&nbsp;수평 해상도 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;수직 해상도 | [0.01] (0.005 ~ 0.025) | 
| ├&nbsp;거리 제약 준수 | [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
| ├&nbsp;(UV Mapping: Mirror Scaled) || 
| │&nbsp;UV 매핑 | **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
| ├&nbsp;**앵커** | | 
| │&nbsp;├&nbsp;상단 레이어 | [2] (0 ~ 10) | 
| │&nbsp;├&nbsp;**상단 앵커** | | 
| │&nbsp;│&nbsp;├&nbsp;앵커 선택 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;선택 오프셋 | [0.5] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Anchor Bone: Torso) || 
| │&nbsp;│&nbsp;│&nbsp;앵커 본 | **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │&nbsp;│&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;│&nbsp;│&nbsp;잠금 모드 | **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │&nbsp;│&nbsp;├&nbsp;앵커 위치 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0.2] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;│&nbsp;├&nbsp;앵커 회전 || 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| │&nbsp;├&nbsp;하단 레이어 | [0] (0 ~ 10) | 
| │&nbsp;└&nbsp;**하단 앵커** | | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 선택 | [1] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;선택 오프셋 | [0.5] (0 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Anchor Bone: Waist) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;앵커 본 | **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;측면 바꾸기 | OFF | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Lock Mode: None) || 
| │&nbsp;&nbsp;&nbsp;│&nbsp;잠금 모드 | **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 위치 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Z) | [0] (-0.5 ~ 0.5) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;앵커 회전 || 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(X) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;├&nbsp;(Y) | [0] (-1 ~ 1) | 
| │&nbsp;&nbsp;&nbsp;└&nbsp;(Z) | [0] (-1 ~ 1) | 
| ├&nbsp;**입자 속성** | | 
| │&nbsp;├&nbsp;입자 반경 | [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │&nbsp;├&nbsp;끈적임 | [0] (0 ~ 1) | 
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
| │&nbsp;├&nbsp;구부림 제한 활성화 | ON | 
| │&nbsp;├&nbsp;구부림 순응 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;스케일 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;자기 충돌 | OFF | 
| │&nbsp;├&nbsp;그립 질량 | [2] (0 ~ 4) | 그립 입자의 질량
| │&nbsp;├&nbsp;그립 마찰 | [2] (-2 ~ 4) | 그립 입자에 대한 마찰
| │&nbsp;├&nbsp;그립 끈적임 | [0.25] (0 ~ 1) | 그립 입자의 끈적임
| │&nbsp;├&nbsp;그립 항력 | [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
| │&nbsp;├&nbsp;그립 스케일 | [1] (0 ~ 2) | 
| │&nbsp;├&nbsp;찢어짐 활성화 | OFF | 
| │&nbsp;├&nbsp;찢어짐 임계값 | [2] (1 ~ 10) | 
| │&nbsp;└&nbsp;찢어짐 속도 제한 | [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
| └&nbsp;(Presets: Skirt) || 
| &nbsp;&nbsp;프리셋 | **치마** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| **C2 재질** | | 
| ├&nbsp;표면 || 
| ├&nbsp;(Presets: Matt Gray) || 
| │&nbsp;프리셋 | **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
| ├&nbsp;유리 모드 | OFF | 
| ├&nbsp;알파를 광택으로 사용 | OFF | 
| ├&nbsp;양면 | ON | 
| ├&nbsp;어두운 배경 | [1] (0 ~ 1) | 
| ├&nbsp;그림자 생성 | [0.5] (0 ~ 1) | 
| ├&nbsp;깊이 사전 패스 | [0.8] (0 ~ 1) | 
| ├&nbsp;광택 | [0.3] (0 ~ 1) | 
| ├&nbsp;금속성 | [0] (0 ~ 1) | 
| ├&nbsp;범프 | [0.2] (0 ~ 1) | 
| ├&nbsp;발광 | [0] (0 ~ 10) | 
| ├&nbsp;앰비언트 | [1] (0 ~ 1) | 
| ├&nbsp;알파 | [1] (0 ~ 1) | 
| ├&nbsp;클립 | [0] (0 ~ 1) | 
| ├&nbsp;**색상** | | 
| │&nbsp;├&nbsp;색상 모드 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;색조 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;채도 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;밝기 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;빨간색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;초록색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;파란색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Multiply) || 
| │&nbsp;│&nbsp;혼합 모드 | **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
| │&nbsp;├&nbsp;혼합 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Gray) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| ├&nbsp;**툰 셰이더** | | 
| │&nbsp;├&nbsp;활성화 | OFF | 
| │&nbsp;├&nbsp;쉐이딩 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;윤곽선 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;스페큘러 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;소프트 스페큘러 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;하이라이트 영역 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;부드러운 하이라이트 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;앰비언트 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;그림자 영역 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;그림자 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;부드러운 그림자 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| ├&nbsp;**특수 셰이더** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;모드 | **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| │&nbsp;├&nbsp;굴절 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;두께 | [1] (0 ~ 1) | 
| ├&nbsp;(Texture: [Solid Color]) || 
| │&nbsp;텍스처 | **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
| └&nbsp;**디테일 맵** | | 
| &nbsp;&nbsp;├&nbsp;활성화 | ON | 
| &nbsp;&nbsp;├&nbsp;**(Hexagon Map)** | | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;활성화 | OFF | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;밀도 | [2] (0 ~ 8) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;크기 | [1] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;범프 | [0.5] (-1 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;노이즈 | [0.2] (0 ~ 1) | 
| &nbsp;&nbsp;│&nbsp;├&nbsp;(Use Circle) | OFF | 
| &nbsp;&nbsp;│&nbsp;└&nbsp;부드러운 모서리 | [0.1] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;(Select Map: Fabric 3) || 
| &nbsp;&nbsp;│&nbsp;맵 선택 | **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
| &nbsp;&nbsp;├&nbsp;디테일 맵 회전 | [0] (-180 ~ 180) | 
| &nbsp;&nbsp;├&nbsp;디테일 맵 크기 | [6] (0 ~ 8) | 
| &nbsp;&nbsp;├&nbsp;디테일 맵 범프 | [0.5] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;AO에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;부드러움에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;금속성에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;컬러 혼합에 영향을 미침 | [0] (0 ~ 1) | 
| &nbsp;&nbsp;├&nbsp;비등방성 | [0] (-1 ~ 1) | 
| &nbsp;&nbsp;└&nbsp;MIP 맵 바이어스 | [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
| 결합 | OFF | 옷 1과 2를 단일 시뮬레이션으로 결합합니다. 이는 두 객체 간의 충돌을 가능하게 하지만 속도가 느려집니다.
| **유체 (실험적)** | | 
| ├&nbsp;활성화 | OFF | 
| ├&nbsp;**스폰** | | 
| │&nbsp;├&nbsp;**위치** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] ((Unlimited)) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [2.5] ((Unlimited)) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] ((Unlimited)) | 
| │&nbsp;├&nbsp;**회전** | | 
| │&nbsp;│&nbsp;├&nbsp;(X) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;├&nbsp;(Y) | [0] (-180 ~ 180) | 
| │&nbsp;│&nbsp;└&nbsp;(Z) | [0] (-180 ~ 180) | 
| │&nbsp;├&nbsp;스폰 반경 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;확산 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;스폰 비율 | [20] (0 ~ 20) | 
| │&nbsp;├&nbsp;속도 | [5] (0 ~ 10) | 
| │&nbsp;├&nbsp;마우스 / 손 조작 | OFF | 
| │&nbsp;├&nbsp;자동 조준 | ON | 
| │&nbsp;├&nbsp;최대 TTL | [10] (5 ~ 15) | 이 시간 후에 입자가 사라졌다가 다시 스폰됩니다.
| │&nbsp;├&nbsp;바닥의 TTL | [0.1] (0 ~ 1) | 바닥에 닿은 후의 생존 시간.
| │&nbsp;├&nbsp;부드럽게 하기 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sprinkler) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **스프링클러** | 샤워, 분수, 스프링클러, 휴대용,  |
| ├&nbsp;**유체** | | 
| │&nbsp;├&nbsp;응집 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;점도 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;표면에 달라붙기 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;대상 밀도 | [2] (1 ~ 10) | 
| │&nbsp;├&nbsp;응집 범위 | [20] (1 ~ 50) | 응집 효과의 최대 거리
| │&nbsp;├&nbsp;대상 거리 | [10] (1 ~ 20) | 응집이 꺼졌을 때 입자 간의 최소 거리 (MM)
| │&nbsp;├&nbsp;고도 | [0.25] (0 ~ 0.5) | 입자의 크기에 비례하여 상승
| │&nbsp;└&nbsp;(Presets: Water) || 
| │&nbsp;&nbsp;&nbsp;프리셋 | **물** | 물, 점성, 모래,  |
| ├&nbsp;**렌더** | | 
| │&nbsp;├&nbsp;입자 렌더링 | ON | 
| │&nbsp;├&nbsp;물방울 렌더링 | OFF | 
| │&nbsp;├&nbsp;물방울 크기 | [2] (0 ~ 50) | 물방울 크기 (MM)
| │&nbsp;├&nbsp;밀도에 따라 스케일 | [0] (0 ~ 5) | 유체의 밀도에 따라 물방울 크기를 조정
| │&nbsp;├&nbsp;**색상** | | 
| │&nbsp;│&nbsp;├&nbsp;색상 모드 | (RGB) | (RGB), (HSV), 
| │&nbsp;│&nbsp;├&nbsp;색조 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;채도 | [0] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;밝기 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;빨간색 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;├&nbsp;초록색 | [1] (0 ~ 1) | 
| │&nbsp;│&nbsp;└&nbsp;파란색 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;금속성 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;부드러움 | [0.95] (0 ~ 1) | 
| │&nbsp;├&nbsp;발광 | [0] (0 ~ 1) | 
| │&nbsp;└&nbsp;투명도 | [0.1] (0 ~ 1) | 
| ├&nbsp;**입자 속성** | | 
| │&nbsp;├&nbsp;중력 | [9.8] (-9.8 ~ 9.8) | 
| │&nbsp;├&nbsp;마찰 | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;지면 마찰 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;항력 (공기) | [-2] (0 ~ 2) | 공기 저항
| │&nbsp;├&nbsp;항력 (수중) | [-2] (0 ~ 2) | 수중 저항
| │&nbsp;├&nbsp;부력 | [-0.1] (-1 ~ 1) | 
| │&nbsp;├&nbsp;**바람** | | 
| │&nbsp;│&nbsp;├&nbsp;바람 영향 | [0] (0 ~ 1) | 
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
| │&nbsp;&nbsp;&nbsp;└&nbsp;플레이어 | OFF | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화),  |
| **지오메트리 콜라이더** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;가시적 | OFF | 
| ├&nbsp;내보내기 모양 || 
| ├&nbsp;**머리** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.04] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.5] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**목** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.065] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.045] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**가슴** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.08] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.023] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.04] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [0.88] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.7] (0 ~ 1) | 
| ├&nbsp;**갈비뼈** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0.075] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**허리** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.032] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.11] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [-0.3] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.8] (0 ~ 1) | 
| ├&nbsp;**배** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.013] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.15] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.073] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.125] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [0.65] (0 ~ 1) | 
| ├&nbsp;**엉덩이** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.0425] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.05] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.105] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0.066] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.012] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.09] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**어깨** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [-0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.02] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.4] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**상완** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.15] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.035] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**하완** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.0445] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.44] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.01] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**손** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.0315] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [-0.0316] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.05] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**엉덩이** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.027] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.1] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.1] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.085] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**허벅지** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.073] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.455] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [-0.01] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.05599999] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**정강이** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.05926838] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 중간 || 
| │&nbsp;├&nbsp;(X) | [0.009999919] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0.05999992] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.01666657] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 중간 | [0.06707321] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 중간 | [0] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.03231711] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| ├&nbsp;**발** | | 
| │&nbsp;├&nbsp;활성화 | ON | 
| │&nbsp;├&nbsp;위치 시작 || 
| │&nbsp;├&nbsp;(X) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [-0.03166673] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0.015] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 시작 | [0.053] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;곡선 | [0.1] (-2 ~ 2) | 
| │&nbsp;├&nbsp;위치 끝 || 
| │&nbsp;├&nbsp;(X) | [0.028] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Y) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;(Z) | [0] (-0.25 ~ 0.25) | 
| │&nbsp;├&nbsp;반경 끝 | [0.0625] (0 ~ 0.15) | 
| │&nbsp;├&nbsp;스케일 || 
| │&nbsp;├&nbsp;(X) | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Y) | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Z) | [1] (0 ~ 1) | 
| └&nbsp;(Presets: Default (Reset)) || 
| &nbsp;&nbsp;프리셋 | **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| **메시 충돌기** | | 
| ├&nbsp;활성화 | ON | 
| ├&nbsp;지오메트리 충돌기 비활성화 | ON | 
| ├&nbsp;시각화 | OFF | 
| ├&nbsp;깊이 | [0.025] (0 ~ 0.1) | 
| ├&nbsp;(Skip Edge) | ON | 
| ├&nbsp;(Skip Point) | ON | 
| └&nbsp;(Single Collision) | ON | 
| **시뮬레이션 설정** | | 
| ├&nbsp;드래그 활성화 | ON | 
| ├&nbsp;스케일 초기화 | [1] (1 ~ 5) | 재설정 시 옷감의 더 큰 스케일로 전환하여 맞춤에 도움을 줌.
| ├&nbsp;시뮬레이트 | ON | 
| ├&nbsp;(Simulation FPS: Dynamic) || 
| │&nbsp;시뮬레이션 FPS | **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| ├&nbsp;시간 스케일 | [0.65] (0.1 ~ 1) | 
| ├&nbsp;서브스텝 | [4] (1 ~ 20) | 
| ├&nbsp;반복 | [1] (0 ~ 10) | 
| ├&nbsp;짝수 서브스텝 역전 | OFF | 
| ├&nbsp;대체 그룹 크기 | [0] (0 ~ 20) | 
| ├&nbsp;테이블 크기 | [6] (1 ~ 20) | 
| └&nbsp;2단계 해결 | OFF | 
| (Presets: Default (Reset)) || 
| 프리셋 | **기본값 (초기화)** | 기본값 (초기화),  |
