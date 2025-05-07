---
locale: ko-rKR
layout: single
title: 시뮬레이션
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[프로](../menu#프로) > 시뮬레이션



| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
|  초기화|| 
|  □ <b>옷 1</b>| | 
| ├─ □ 활성화| [OFF] | 
| ├─ 메시 재구성|| 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 토폴로지| **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 끈 연결| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 내부 반경| [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 경사| [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 호| [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 길이| [0.25] (0 ~ 0.75) | 길이(미터)
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 팔 구멍| [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)| [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 뒤쪽 길이| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 길이| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 해상도| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수직 해상도| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 거리 제약 준수| [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV 매핑| **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>앵커</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 상단 레이어| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>상단 앵커</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 선택| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선택 오프셋| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 앵커 본| **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 잠금 모드| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │ │ ├─ <b>앵커 위치</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>앵커 회전</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 하단 레이어| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>하단 앵커</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 선택| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선택 오프셋| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 앵커 본| **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ 측면 바꾸기| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 잠금 모드| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>앵커 위치</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>앵커 회전</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 속성</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 끈적임| [0] (0 ~ 1) | 
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
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 구부림 제한 활성화| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 구부림 순응| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스케일| [1] (0 ~ 2) | 
| │ ├─ □ 자기 충돌| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 질량| [2] (0 ~ 4) | 그립 입자의 질량
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 마찰| [2] (-2 ~ 4) | 그립 입자에 대한 마찰
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 끈적임| [0.25] (0 ~ 1) | 그립 입자의 끈적임
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 항력| [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 스케일| [1] (0 ~ 2) | 
| │ ├─ □ 찢어짐 활성화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 찢어짐 임계값| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 찢어짐 속도 제한| [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **(Top)** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C1 재질</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>표면</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
| ├─ □ 유리 모드| [OFF] | 
| ├─ □ 알파를 광택으로 사용| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 양면| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 어두운 배경| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 그림자 생성| [0.5] (0 ~ 1) | 
| ├─ □ 깊이 사전 패스| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 광택| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 금속성| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 범프| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 발광| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앰비언트| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 알파| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 클립| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>색상</b>| | 
| │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 색조| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 채도| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밝기| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 빨간색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 초록색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 파란색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 혼합 모드| **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 혼합| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| ├─ □ <b>툰 셰이더</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 쉐이딩| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 윤곽선| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스페큘러| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 소프트 스페큘러| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 하이라이트 영역| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 하이라이트| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앰비언트| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그림자 영역| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그림자| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 그림자| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>특수 셰이더</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 모드| **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 굴절| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 두께| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 텍스처| **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>디테일 맵</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 활성화| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밀도| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 크기| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 범프| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 노이즈| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ (Use Circle)| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 모서리| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 맵 선택| **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 회전| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 크기| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 범프| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> AO에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러움에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 금속성에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 컬러 혼합에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 비등방성| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP 맵 바이어스| [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
|  □ <b>옷 2</b>| | 
| ├─ □ 활성화| [OFF] | 
| ├─ 메시 재구성|| 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 토폴로지| **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 끈 연결| [4] (1 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 내부 반경| [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 경사| [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 호| [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 길이| [0.25] (0 ~ 0.75) | 길이(미터)
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 팔 구멍| [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Arm Hole Height)| [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 뒤쪽 길이| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 길이| [1] (0.1 ~ 1.9) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수평 해상도| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 수직 해상도| [0.01] (0.005 ~ 0.025) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 거리 제약 준수| [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> UV 매핑| **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>앵커</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 상단 레이어| [2] (0 ~ 10) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>상단 앵커</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 선택| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선택 오프셋| [0.5] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 앵커 본| **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │ │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 잠금 모드| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │ │ ├─ <b>앵커 위치</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.2] (-0.5 ~ 0.5) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ │ ├─ <b>앵커 회전</b>|| 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 하단 레이어| [0] (0 ~ 10) | 
| │ └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>하단 앵커</b>| | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앵커 선택| [1] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 선택 오프셋| [0.5] (0 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 앵커 본| **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
| │ <img src="/images/icon/ic_space.png"/>├─ □ 측면 바꾸기| [OFF] | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 잠금 모드| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
| │ <img src="/images/icon/ic_space.png"/>├─ <b>앵커 위치</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.5 ~ 0.5) | 
| │ <img src="/images/icon/ic_space.png"/>├─ <b>앵커 회전</b>|| 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-1 ~ 1) | 
| │ <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 속성</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 입자 반경| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 끈적임| [0] (0 ~ 1) | 
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
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 구부림 제한 활성화| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 구부림 순응| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스케일| [1] (0 ~ 2) | 
| │ ├─ □ 자기 충돌| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 질량| [2] (0 ~ 4) | 그립 입자의 질량
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 마찰| [2] (-2 ~ 4) | 그립 입자에 대한 마찰
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 끈적임| [0.25] (0 ~ 1) | 그립 입자의 끈적임
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 항력| [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그립 스케일| [1] (0 ~ 2) | 
| │ ├─ □ 찢어짐 활성화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 찢어짐 임계값| [2] (1 ~ 10) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 찢어짐 속도 제한| [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **치마** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>C2 재질</b>| | 
| ├─<img src="/images/icon/ic_texture.png" alt="texture icon"/> <b>표면</b>|| 
| ├─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
| ├─ □ 유리 모드| [OFF] | 
| ├─ □ 알파를 광택으로 사용| [OFF] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 양면| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 어두운 배경| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 그림자 생성| [0.5] (0 ~ 1) | 
| ├─ □ 깊이 사전 패스| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 광택| [0.3] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 금속성| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 범프| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 발광| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앰비언트| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 알파| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 클립| [0] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>색상</b>| | 
| │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 색조| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 채도| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밝기| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 빨간색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 초록색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 파란색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 혼합 모드| **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 혼합| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
| ├─ □ <b>툰 셰이더</b>| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 쉐이딩| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 윤곽선| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스페큘러| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 소프트 스페큘러| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 하이라이트 영역| [0.25] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 하이라이트| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 앰비언트| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그림자 영역| [0.65] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 그림자| [0.75] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 그림자| [0.1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>특수 셰이더</b>| | 
| │ ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 모드| **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 굴절| [0.5] (1 ~ 3) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 두께| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 텍스처| **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>디테일 맵</b>| | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─ □ <b>(Hexagon Map)</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 활성화| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밀도| [2] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 크기| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 범프| [0.5] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 노이즈| [0.2] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ (Use Circle)| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러운 모서리| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 맵 선택| **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 회전| [0] (-180 ~ 180) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 크기| [6] (0 ~ 8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 디테일 맵 범프| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> AO에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러움에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 금속성에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 컬러 혼합에 영향을 미침| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 비등방성| [0] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_slider.png" alt="slider icon"/> MIP 맵 바이어스| [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
|  □ 결합| [OFF] | 옷 1과 2를 단일 시뮬레이션으로 결합합니다. 이는 두 객체 간의 충돌을 가능하게 하지만 속도가 느려집니다.
|  □ <b>유체 (실험적)</b>| | 
| ├─ □ 활성화| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>스폰</b>| | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>위치</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] ((Unlimited)) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [2.5] ((Unlimited)) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] ((Unlimited)) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>회전</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-180 ~ 180) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-180 ~ 180) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-180 ~ 180) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스폰 반경| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 확산| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스폰 비율| [20] (0 ~ 20) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 속도| [5] (0 ~ 10) | 
| │ ├─ □ 마우스 / 손 조작| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 자동 조준| [ON] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 최대 TTL| [10] (5 ~ 15) | 이 시간 후에 입자가 사라졌다가 다시 스폰됩니다.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바닥의 TTL| [0.1] (0 ~ 1) | 바닥에 닿은 후의 생존 시간.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드럽게 하기| [0.5] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **스프링클러** | 샤워, 분수, 스프링클러, 휴대용,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>유체</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 응집| [0.5] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 점도| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 표면에 달라붙기| [0.1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대상 밀도| [2] (1 ~ 10) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 응집 범위| [20] (1 ~ 50) | 응집 효과의 최대 거리
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대상 거리| [10] (1 ~ 20) | 응집이 꺼졌을 때 입자 간의 최소 거리 (MM)
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 고도| [0.25] (0 ~ 0.5) | 입자의 크기에 비례하여 상승
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **물** | 물, 점성, 모래,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>렌더</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 입자 렌더링| [ON] | 
| │ ├─ □ 물방울 렌더링| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 물방울 크기| [2] (0 ~ 50) | 물방울 크기 (MM)
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밀도에 따라 스케일| [0] (0 ~ 5) | 유체의 밀도에 따라 물방울 크기를 조정
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>색상</b>| | 
| │ │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 색조| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 채도| [0] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 밝기| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 빨간색| [1] (0 ~ 1) | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 초록색| [1] (0 ~ 1) | 
| │ │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 파란색| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 금속성| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부드러움| [0.95] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 발광| [0] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 투명도| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>입자 속성</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 중력| [9.8] (-9.8 ~ 9.8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 마찰| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 지면 마찰| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (공기)| [-2] (0 ~ 2) | 공기 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 항력 (수중)| [-2] (0 ~ 2) | 수중 저항
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 부력| [-0.1] (-1 ~ 1) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>바람</b>| | 
| │ │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 바람 영향| [0] (0 ~ 1) | 
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
| │ <img src="/images/icon/ic_space.png"/>└─ □ 플레이어| [OFF] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>지오메트리 콜라이더</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─ □ 가시적| [OFF] | 
| ├─ 내보내기 모양|| 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>머리</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.04] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.5] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.11] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.8] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>목</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.045] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.065] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.045] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>가슴</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.08] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.023] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.04] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.15] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.88] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.7] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>갈비뼈</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.075] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>허리</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.032] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.11] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [-0.3] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.8] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>배</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.013] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.15] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.073] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.125] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.65] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>엉덩이</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.0425] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.05] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.105] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.066] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.012] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.09] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>어깨</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.02] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.05] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.4] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>상완</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.15] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.035] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>하완</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.0445] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.44] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.01] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>손</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.0315] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [-0.0316] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.05] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>엉덩이</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.027] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.1] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.455] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.1] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.085] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>허벅지</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.073] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.455] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [-0.01] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.05599999] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>정강이</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.05926838] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0] (-2 ~ 2) | 
| │ ├─ <b>위치 중간</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.009999919] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0.05999992] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.01666657] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 중간| [0.06707321] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선 중간| [0] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.03231711] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>발</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| │ ├─ <b>위치 시작</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [-0.03166673] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0.015] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 시작| [0.053] (0 ~ 0.15) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 곡선| [0.1] (-2 ~ 2) | 
| │ ├─ <b>위치 끝</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0.028] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.25 ~ 0.25) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반경 끝| [0.0625] (0 ~ 0.15) | 
| │ ├─ <b>스케일</b>|| 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [1] (0 ~ 1) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>메시 충돌기</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 활성화| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 지오메트리 충돌기 비활성화| [ON] | 
| ├─ □ 시각화| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 깊이| [0.025] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Edge)| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Skip Point)| [ON] | 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Single Collision)| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>시뮬레이션 설정</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 드래그 활성화| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 스케일 초기화| [1] (1 ~ 5) | 재설정 시 옷감의 더 큰 스케일로 전환하여 맞춤에 도움을 줌.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 시뮬레이트| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 시뮬레이션 FPS| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 시간 스케일| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 서브스텝| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 반복| [1] (0 ~ 10) | 
| ├─ □ 짝수 서브스텝 역전| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 대체 그룹 크기| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 테이블 크기| [6] (1 ~ 20) | 
| └─ □ 2단계 해결| [OFF] | 
| <img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋| **기본값 (초기화)** | 기본값 (초기화),  |
